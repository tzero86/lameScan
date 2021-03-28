from libs import lameScanner
from libs import vulnScan


class ConfigMenu:
    lame = lameScanner.LameScan()
    vuln = vulnScan.vuln_scanner()

    # General settings
    VERSION = {
        'v': '0.0.1'
    }

    lameScan_config = {
        'debug': False,
        'max_thread_workers': 60
    }

    # General scan specific settings
    scan_config = {
        'debug': False,
        'max_thread_workers': 60,
        'range': {
            'low_port': 0,
            'high_port': 65535
        },
        'sock_conn_timeout': 0.3,
        'show_closed_ports': False,
        'run_top1k_ports': False,
        'Auto_generate_report': False
    }

    def __init__(self):
        pass

    def callPortScanner(self):
        self.lame.new_run()

    def do_exit(self):
        print(f'By bye :)')
        print(
            '\n' + self.lame.RED + '[------------------------{*| Noli umquam discere desinere |*}------------------'
                                   '------]' + self.lame.WHITE
            + '\n')

        quit()

    def print_options(self):
        self.lame.print_welcome()
        menu = (
                f'{self.lame.CYAN}'
                f'|---------------------------------------(:MENU:)-------------------------------------|' + '\n'
                + '\n'
                  f'{self.lame.CYAN}Please select a module to execute:{self.lame.LBLUE}' + '\n' + '\n'
                  f'[01] Multi-threaded Port Scanner' + '\n'
                  f'[02] Vulnerability Scanner' + '\n'f'[99] Exit LameSacan' + f'\n{self.lame.CYAN} '
        )
        print(menu)
        mod_selection = input('[Input] Enter the Menu Number and press ENTER: ')
        print(f'DEBUG: Options entered: {mod_selection}')
        try:
            if int(mod_selection) == 1:
                self.callPortScanner()
            elif int(mod_selection) == 2:
                self.vuln.new_scan()
            elif int(mod_selection) == 99:
                self.do_exit()
            else:
                self.print_options()
        except:
            self.do_exit()

    def load_menu(self):
        # TODO: create a function that displays menu options and takes user input
        self.print_options()
