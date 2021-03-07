# LameScan - a very lame port scanner made with Python3

![](https://i.imgur.com/EZAehd1.png)

I've decided to start playing with Python3 again, and been putting a bits and pieces 
of what I lean into creating this basic example of a port scanner.

## Features

- Supports Multi-threaded scans for better performance and quick results
- Scans all ports by default unless a range is specified.
  - Right now if no range is entered, will scan the `top 1000` ports.
- Supports domain names and IPs by default.
- Attempts to grab the banner of the port and prints the result
- Scan results are automatically saved into a JSON formatted file (super basic for now)  
- Supports multiple targets separated by commas: 
    - **Example:** `facebook.com,192.168.1.1,google.com,127.0.0.1`
  
## Future Enhancements

- Edd support to specify ports specific ports instead of range only.
- Enhance banner detection.
- Enhance JSON export (possibly include other formats).
- Fix the bugs!



> **NOTE**: Like I mentioned I'm just going through python3 learning process, so don't expect this to become
a useful tool any time soon or even ever. This is just a 'have fun and learn some Python3' kind of thing. 


