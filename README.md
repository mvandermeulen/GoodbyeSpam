# GoodbyeSpam - Spam Call Mitigation for Asterisk PBX

GoodbyeSpam is an Asterisk AGI (Asterisk Gateway Interface) script and an IVR (Interactive Voice Response) system designed to mitigate spam calls and robocalls on an Asterisk PBX. It effectively identifies and filters out unwanted calls before they reach the intended client.

## Features
- **Blacklist**: The AGI script immediately hangs up on blacklisted callers, preventing them from reaching your system.
- **Interactive Voice Response (IVR)**: Non-blacklisted callers are prompted to input the last digit of the extension they want to call using their dialpad. This simple verification step helps ensure that the caller is a human, not a spam call.
