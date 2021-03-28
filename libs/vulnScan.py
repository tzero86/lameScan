import json
import subprocess


class vuln_scanner:

    def __init__(self):
        pass

    # Handles calling an nmap scan via subprocess.
    # The ports used are those found by lameScan but needs support for direct user input.
    @staticmethod
    def nmap_scan(ports, ip):
        nmap_proc = subprocess.Popen(["nmap", "-sV", "--script", "nmap-vulners", f"{ip}", f"-{ports}"],
                                     stdout=subprocess.PIPE)
        (output, err) = nmap_proc.communicate()
        print(output.decode('utf-8').strip())

    @staticmethod
    def read_config():
        # TODO: handle reading the results file to feed the vuln scan with target and ports
        res_dir = './libs/'
        file_name = f'{res_dir}res_cfg'
        with open(file_name) as config_file:
            json_cfg = json.load(config_file)
            print(json_cfg)
            # TODO: call nmap_scan() with the appropriate parameters
            return json_cfg

    # handles the new scan flow with nmap subprocess
    def new_scan(self):
        cfg = self.read_config()
        ports = ''
        if cfg["open_ports_found"].len > 1:
            for port in cfg["open_ports_found"]:
                ports = ports + port + ','
            self.nmap_scan(ports, cfg['target'])
        else:
            self.nmap_scan(cfg['port'], cfg['target'])
