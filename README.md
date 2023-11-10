# GoodbyeSpam - Spam Call Mitigation for Asterisk PBX
A security model within Asterisk using blacklist, Asterisk Gateway Interface (AGI) and Interactive Voice Response (IVR) system to automatically hang up spam calls before reaching the clients.

## Features
- **Blacklist**: A blacklist created in MySQL to store the caller IDs of known spam callers.
- **AGI**: An AGI script written in Python language that connects to MySQL and label if the caller is blacklisted or not.
- **IVR system**: Prompts non-blacklisted callers to input the last digit of the extension they wish to call.

![AGI and IVR](https://github.com/warlocksmurf/GoodbyeSpam/assets/121353711/12cc891b-7e70-48c6-a7bf-699d19262eb7)
