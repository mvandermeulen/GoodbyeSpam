# GoodbyeSpam - Spam Call Mitigation for Asterisk PBX
A security model within Asterisk using MySQL, AGI and IVR system to automatically hang up spam calls before reaching the clients.

## Features
- **Blacklist**: A blacklist created in MySQL to store every blacklisted callers using their caller IDs.
- **AGI script**: The Python AGI script connects to MySQL and immediately hangs up blacklisted callers and pass non-blacklisted callers back to Asterisk
- **Interactive Voice Response (IVR)**: Non-blacklisted callers are prompted to input the last digit of the extension they want to call using their dialpad for caller verification and automated call routing.
