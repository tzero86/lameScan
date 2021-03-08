# LameScan - v0.0.2 
### A very lame & simple port scanner(attempt) made with Python3

![](https://i.imgur.com/5IdZKc8.png)

I've decided to start playing with Python3 again, and been putting a bits and pieces 
of what I lean into creating this basic example of a port scanner.

## Features

- Supports Multi-threaded scans for better performance and quick results
- Scans the `top 1000` ports by default unless a range is specified.
- Supports domain names and IPs by default for targets: `target.com or 127.0.1.1`
- Attempts to grab the banner of the port and prints the result
- Scan results are automatically saved into a JSON formatted file  
- Supports multiple targets separated by commas: 
    - **Example:** `facebook.com,192.168.1.1,google.com,127.0.0.1`
  
## Future Enhancements

- Add support to scan specific ports instead of range/TOP1000 only.
- Enhance banner detection.
- Enhance JSON export (possibly include other formats).
- Implement a menu to configure scan settings, define targets, etc.
- Add support to get parameters by commandline arguments  
- Fix the bugs!



> **NOTE**: Like I mentioned I'm just going through python3 learning process, so don't expect this to become
a useful tool any time soon or even ever. This is just a 'have fun and learn some Python3' kind of thing. 


