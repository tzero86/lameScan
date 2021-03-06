import socket
from IPy import IP
from pyfiglet import Figlet
from colorama import Fore, Back, Style

VERSION_N = 'v0.0.1'
RANGE = 1000
TIMEOUT = 0.2


def print_welcome():
    custom_fig = Figlet(font='nancyj')
    print(Fore.GREEN + '------------------------------------------------------------------')
    print(Fore.GREEN + custom_fig.renderText('LameScan'))
    print(Fore.RED + f'{VERSION_N} A basic <<Im learning python>> port scanner by @Tzero86')
    print(Fore.GREEN + '------------------------------------------------------------------')
    print(Fore.WHITE)


def scan(target):
    converted_ip = check_ip(target)
    print(Fore.LIGHTBLUE_EX + f'[*] Scanning TOP 1000 ports on the target: {target}')
    for port in range(1, RANGE):
        scan_port(converted_ip, port)


def get_banner(s):
    return s.recv(1024)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(r_ip, r_port):
    try:
        sock = socket.socket()
        sock.settimeout(TIMEOUT)
        sock.connect((r_ip, r_port))
        try:
            banner = get_banner(sock)
            banner = banner.decode().strip("\n")
            print(Fore.GREEN + f'[+] Host: {r_ip} - Port open: {r_port} - Banner: {banner}' + Fore.WHITE)
        except:
            print(Fore.GREEN + f'[+] Host: {r_ip} - Port open: {r_port}' + Fore.WHITE)
    except:
        # print(f'[-] Host: {r_ip} -> Port {r_port} is closed')
        pass


print_welcome()

targets = input(Fore.LIGHTBLUE_EX + '[?] Enter the target(s) to scan separated by ,: ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)

print(Fore.LIGHTBLUE_EX + f'[*] LameScan {VERSION_N} has finished processing the task.')