#!/usr/bin/env python3

import pymysql
from asterisk.agi import AGI

agi = AGI() # Initialize AGI
agi.verbose("AGI STARTED")

caller_id = agi.env['agi_callerid']

try:
    # Establish database connection
    db = pymysql.connect(host='localhost', user='asterisk', password='123', database='capstone')
    cursor = db.cursor()

    # Use cursor to execute queries
    cursor.execute("SELECT COUNT(*) FROM blacklist WHERE caller_id = %s", (caller_id,))
    result = cursor.fetchone()

    # Check if caller is in the blacklist table
    if result and result[0] > 0:
        agi.set_variable("BLACKLIST", "TRUE")
        agi.verbose("Caller is blacklisted")
    else:
        agi.set_variable("BLACKLIST", "FALSE")
        agi.verbose("Caller is non-blacklisted")

except Exception as e:
    agi.verbose("Error: {}".format(e))

finally:
    db.close() #close database connection
