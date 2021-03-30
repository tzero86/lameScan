import json
import subprocess


class VulnScanner:

    def __init__(self):
        pass

    # Handles calling an nmap scan via subprocess.
    # The ports used are those found by lameScan but needs support for direct user input.
    def nmap_scan(self, ports, ip):
        print(f' nmap_scan() function: args {ports, ip}')
        from libs import lameScanner
        port = '-p'+ports
        ip = str(lameScanner.LameScan().check_ip(ip))
        nmap_proc = subprocess.Popen(["nmap", "-sV", "--script", "nmap-vulners", ip, port]
                                     , bufsize=2048, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     close_fds=True)
        nmap_proc.wait()
        print(nmap_proc.stdout)
        print(nmap_proc.stderr)

    def read_config(self):
        # TODO: handle reading the results file to feed the vuln scan with target and ports
        res_dir = './libs/'
        file_name = f'{res_dir}res_cfg'
        with open(file_name) as config_file:
            json_cfg = json.load(config_file)
            print(json.dumps(json_cfg, indent=4))
            # TODO: call nmap_scan() with the appropriate parameters
        return json_cfg

    # handles the new scan flow with nmap subprocess
    def new_scan(self):
        res_dir = './libs/'
        file_name = f'{res_dir}res_cfg'
        with open(file_name) as config_file:
            config_data = config_file.read()
            cfg = json.loads(config_data)
            ports = ''
            print(f'new_scan(): Total num of elements in ports list: {len(cfg["open_ports_found"])}')
            print(f'new_scan(): is length of list greater than 1: {len(cfg["open_ports_found"]) > 1}')
            if len(cfg["open_ports_found"]) > 1:
                ports = ','.join(map(str, cfg["open_ports_found"]))
                print(f'Parameters sent to nmap: {ports}')
                self.nmap_scan(','.join(map(str, cfg["open_ports_found"])), cfg['targets'][0])
                # TODO: Fix this, we need to handle each target individually
            else:
                print(f'Parameters sent to nmap: {ports}')
                self.nmap_scan(cfg['port'], cfg['targets'][0])
