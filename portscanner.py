import socket
from IPy import IP

def scan(target, port):
    converted_ip = check_ip(target)
    print('\n' + '[-_-] Scanning Target ' + str(target))
    for port in range(1, port):
        scan_port(converted_ip, port)

def check_ip(ipaddress):
    try:
        IP(ipaddress)
        return ipaddress
    except ValueError:
        socket.gethostbyname(ipaddress)
        return ipaddress

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is open.')
    except:
        # print('[-] Port ' + str(port) + ' is closed.')
        pass

if __name__ == "__main__":
    targets = input('Enter Target\'s To Scan (split multiple targets using comma): ')
    port = int(input('Enter Port Number To Scan (500 means first 500 ports): '))
    if ',' in targets:
        print('\n[*] Scanning Multiple Targets')
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), port)
    else:
        scan(targets, port)







