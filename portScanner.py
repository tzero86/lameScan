import socket
from IPy import IP
from pyfiglet import Figlet
from colorama import Fore, Back, Style


def print_welcome():
    custom_fig = Figlet(font='nancyj')
    print(Fore.GREEN + '------------------------------------------------------------------')
    print(Fore.GREEN + custom_fig.renderText('LameScan'))
    print(Fore.RED + 'v0.0.1')
    print(Fore.RED + 'A basic <<Im learning python>> port scanner made made by Tzero86')
    print(Fore.GREEN + '------------------------------------------------------------------')


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + f'[*] Scanning target (TOP 1000 ports): {target}')
    for port in range(1, 1000):
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
        sock.settimeout(0.2)
        sock.connect((r_ip, r_port))
        try:
            banner = get_banner(sock)
            banner = banner.decode().strip("\n")
            print(f'[Found!] Host: {r_ip} - Port open: {r_port} - Banner: {banner}')
        except:
            print(f'[Found!] Host: {r_ip} - Port open: {r_port}')
    except:
        # print(f'[-] Host: {r_ip} -> Port {r_port} is closed')
        pass


print_welcome()

targets = input('[?] Enter the target(s) to scan separated by ,: ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)

