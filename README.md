# LameScan - v0.0.2 
### A very lame & simple port scanner(attempt) made with Python3

![](https://i.imgur.com/5IdZKc8.png)

I've decided to start playing with Python3 again, and been putting bits and pieces 
of what I learn into creating this basic example of a port scanner.

## Features

- Supports Multi-threaded scans for better performance and quick results
- Scans the `top 1000` ports by default unless a range is specified.
- Supports domain names and IPs by default for targets: `target.com or 127.0.1.1`
- Attempts to grab the banner of the port and prints the result
- Scan results are automatically saved into a JSON formatted file  
- Supports multiple targets separated by commas: 
    - **Example:** `facebook.com,192.168.1.1,google.com,127.0.0.1`
  
# Install Dependencies & Use

To start git clone the repository and enter the lameScan directory:
- `git clone https://github.com/tzero86/lameScan && cd lameScan`

Then run the following to install the requirements:
- `pip3 install -r requirements.txt`

After that is done just execute with:
- `python3 lameScan.py`

The just use ir as per the program's instructions, it is very simple. Just provide the target, port range and optional
settings and let it run.

  
## Future Enhancements

- Add support to scan specific ports instead of range/TOP1000 only.
- Enhance banner detection.
- Enhance JSON export (possibly include other formats).
- Implement a menu to configure scan settings, define targets, etc.
- Add support to get parameters by commandline arguments  
- Known Issues to be fixed:
  - [BUG] Need to tie the results to each target and provide a sectioned report by Target.
  - [BUG] After a second scan, the user is no longer prompted to run another scan.
  - [BUG] The spacing between open port logs needs fixing, right now they all print a new line which is a waste 
    of screen space.



> **NOTE**: Like I mentioned I'm just going through python3 learning process, so don't expect this to become
a useful tool any time soon or even ever. This is just a 'have fun and learn some Python3' kind of thing. 


