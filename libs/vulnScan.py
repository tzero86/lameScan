import json
import subprocess


class VulnScanner:

    def __init__(self):
        pass

    def show_menu(self):
        from libs import menu
        menu.ConfigMenu().print_options()

    # Handles calling an nmap scan via subprocess.
    # The ports used are those found by lameScan but needs support for direct user input.
    def nmap_scan(self, ports, ip):
        print(f' nmap_scan() function: args {ports, ip}')
        from libs import lameScanner
        port = '-p '+ports
        ip = str(lameScanner.LameScan().check_ip(ip))
        print(ip, ports)
        # TODO this needs to also be a multi-threaded process, otherwise it's too slow
        #  (convert this to a subprocess by port)
        nmap_proc = subprocess.Popen(["nmap", "-sV", "--script=vulners", '-T5', '-v4', f'-p{ports}', ip]
                                     , bufsize=2048, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     close_fds=True)
        nmap_proc.wait()
        stdout, stderr = nmap_proc.communicate()
        print(stdout.decode('utf-8'))
        print(stderr.decode('utf-8'))
        from libs import menu
        menu.ConfigMenu().print_options()


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
        try:
            res_dir = './libs/'
            file_name = f'{res_dir}res_cfg'
            with open(file_name) as config_file:
                config_data = config_file.read()
                cfg = json.loads(config_data)
                ports = ''
                print(f'new_scan(): Total num of elements in ports list: {len(cfg["open_ports_found"])}')
                print(f'new_scan(): is length of list greater than 1: {len(cfg["open_ports_found"]) > 1}')
                if len(cfg["open_ports_found"]) > 1:
                    # FIXME: This needs to be refactored. We need to process each port so better leave them in the list
                    ports = ','.join(map(str, cfg["open_ports_found"]))
                    print(f'Parameters sent to nmap: {ports}')
                    # TODO: We need a helper function that handles firing the vuln scan by port in threads. Then we
                    #  can just call the existing function with on port by port basis. Still need to account for
                    #  each target which is another problem to solve. Maybe it makes more sense to switch to the
                    #  python nmap module which could be easier to handle with multiple threads and overall config
                    self.nmap_scan(','.join(map(str, cfg["open_ports_found"])), cfg['targets'][0])
                    # TODO: Fix this, we need to handle each target individually
                elif len(cfg["open_ports_found"]) < 1:
                    # FIXME: This could be triggered automatically, or even allow the user to just specify
                    #  target and ports and scan options.
                    print(f'[Error] You need to run a port scan first, from the menu select the appropriate option.')
                    from libs import menu
                    menu.ConfigMenu().print_options()
                else:
                    print(f'Parameters sent to nmap: {ports}')
                    self.nmap_scan(cfg['port'], cfg['targets'][0])
        except IOError as error:
            print(error)
            print(f'[Error] You need to run a port scan first, from the menu select the appropriate option.')
            from libs import menu
            menu.ConfigMenu().print_options()
