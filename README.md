# GoodbyeSpam - Spam Call Mitigation for Asterisk PBX
An Asterisk AGI (Asterisk Gateway Interface) script and IVR (Interactive Voice Response) system was implemented to mitigate spam calls and robocalls on an Asterisk PBX.

## Features
- **Blacklist**: The Python AGI script connects to MySQL and immediately hangs up calls from blacklisted callers based on their caller IDs.
- **Interactive Voice Response (IVR)**: Non-blacklisted callers are prompted to input the last digit of the extension they want to call using their dialpad for caller verification and automated call routing.
