#!/usr/bin/python
import random
import os
import pymysql.cursors
from asterisk.agi import AGI
from gtts import gTTS

agi = AGI()

caller_id = agi.env['agi_callerid']
dest_no = agi.env['agi_dnid']
blacklist_table = 'blacklist'
whitelist_table = 'whitelist'

# Connect to MySQL database
connection = pymysql.connect(
    host='your-mysql-host',
    user='your-mysql-username',
    password='your-mysql-password',
    db='asterisk',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def blacklist(caller_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {blacklist_table} WHERE caller_id = %s", (caller_id,))
        return cursor.fetchone()

def whitelist(caller_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {whitelist_table} WHERE caller_id = %s", (caller_id,))
        return cursor.fetchone()

def add_whitelist(caller_id):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO {whitelist_table} (caller_id) VALUES (%s)", (caller_id,))
        connection.commit()

def add_blacklist(caller_id):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO {blacklist_table} (caller_id) VALUES (%s)", (caller_id,))
        connection.commit()

try:
    # If the caller is in the blacklist, terminate the call
    if blacklist(caller_id):
        agi.verbose('Call terminated. Caller is in the blacklist.')
        agi.hangup()
        exit(0)

    # If the caller is in the whitelist, allow the call to proceed
    if whitelist(caller_id):
        agi.verbose('Caller is trusted. Forwarding call to destination extension.')
        agi.exec('Dial', f'SIP/{dest_no}')
    else:
        # Perform the verification challenge using gTTS
        verification_code = str(random.randint(1000, 9999))
        audio_message = f"Please enter the following code on your keypad: {verification_code}"
        tts = gTTS(audio_message, lang='en', slow=False)

        # Save the TTS audio to a temporary file
        temp_file_path = '/etc/asterisk/tmp/verification_prompt.wav'
        tts.save(temp_file_path)

        # Play the audio prompt
        agi.stream_file(temp_file_path, escape_digits='#')

        # Collect user input
        digits = 4  # Number of digits to collect
        timeout = 7000 # Timeout in milliseconds
        user_input = agi.answer(timeout, digits)

        if user_input == verification_code:
            # Add the caller to the whitelist
            add_whitelist(caller_id)
            agi.verbose('Caller passed the verification challenge. Forwarding the call...')
            agi.exec('Dial', f'SIP/{dest_no}')
        else:
            # Add the caller to the blacklist
            add_blacklist(caller_id)
            agi.verbose('Caller failed the verification challenge. Goodbye spam!')
            agi.hangup()

finally:
    connection.close() # Close the MySQL connection

    if os.path.exists(temp_file_path): # Remove the temporary audio file
        os.remove(temp_file_path)