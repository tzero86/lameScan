# LameScan - a very lame port scanner made with Python3

I've decided to start playing with Python3 again, and been putting a bits and pieces 
of what I lean into creating this basic example of a port scanner.

## Features

- Scans all ports by default unless a range is specified.
  - Right now if no range is entered, it scans all 65535 ports.
- Supports domain names and IPs by default.
- Attempts to grab the banner of the port and prints the result  
- Supports multiple targets separated by commas: 
    - Example: **facebook.com,192.168.1.1,google.com,127.0.0.1**
  
## Enhancements
- Add threading support to enhance scanning speed
- Add the scan option to have the top 1000 TCP ports scanned
- add support to specify ports specific ports instead of range only.
- Add support to have results collected and saved to a file
  
![](https://i.imgur.com/tBFae3s.gif)

> **NOTE**: Like I mentioned I'm just going through python3 learning process, so don't expect this to become
a useful tool any time soon or even ever. This is just a 'have fun and learn some Python3' kind of thing. 


