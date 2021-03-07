# LameScan - a very lame port scanner made with python3

I've decided to start playing with Python3 again, and been putting a bits and pieces 
of what I lean into creating this basic example of a port scanner.

## Features

- (To do) Scan TOP 1000 ports by default unless a range is specified.
  - Right now if no range is entered, it scans all 65535 ports.
- Supports domain names and IPs by default.
- Attempts to grab the banner of the port and print the result  
- User can specify multiple targets separated by commas: 
    - Example: **facebook.com,192.168.1.1,google.com,127.0.0.1**
    
> **NOTE**: Like I mentioned I'm just going through python3 learning process, so don't expect this to become
a useful tool any time soon.

@tzero86