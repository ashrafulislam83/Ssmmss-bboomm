import os
import requests
import time

def banner():
    os.system("clear")
    print("\033[1;34m")
    print("█████╗ ███████╗██╗  ██╗██████╗ ██████╗ ██╗   ██╗███████╗██╗     ")
    print("██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██║   ██║██╔════╝██║     ")
    print("███████║███████╗███████║██████╔╝██████╔╝██║   ██║█████╗  ██║     ")
    print("██╔══██║╚════██║██╔══██║██╔═══╝ ██╔═══╝ ██║   ██║██╔══╝  ██║     ")
    print("██║  ██║███████║██║  ██║██║     ██║     ╚██████╔╝███████╗███████╗")
    print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝")
    print("               Created by \033[1;32mAshraful\033[1;34m")
    print("\033[0m")

def send_sms(number):
    url = f"https://smsapi.example.com/send?number={number}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[1;32m[+] SMS sent to {number}\033[0m")
        else:
            print(f"\033[1;31m[-] Failed to send SMS\033[0m")
    except:
        print(f"\033[1;31m[!] Error sending SMS\033[0m")

if __name__ == "__main__":
    banner()
    num = input("Enter target number (e.g. 01xxxxxxxxx): ")
    amount = int(input("How many SMS to send: "))
    
    for i in range(amount):
        send_sms(num)
        time.sleep(1)
