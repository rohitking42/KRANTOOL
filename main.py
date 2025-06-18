# Logo
logo = """
\033[1;37m⌌\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;34m━━━━\033[1;35m━━\033[1;37m⌍
\033[1;38m▏ 
  
 ____  ____  _     _  _____   
/  __\/  _ \/ \ /|/ \/__ __\  
|  \/|| / \|| |_||| |  / \    
|    /| \_/|| | ||| |  | |    
\_/\_\\____/\_/ \|\_/  \_/    
                              

                                     
\033[1;37m⌎\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;34m━━━━\033[1;35m━━\033[1;37m⌏                                              
                                             
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[37m[*] 𝐊𝐑𝐈𝐗    : \033[36𝗺 𝐊𝐑𝐈𝐗
\033[37m[*] 𝐆𝐈𝐓𝐇𝐔𝐁     : \033[33m𝗥𝗢𝗛𝗜𝗧 𝗫𝗗 
\033[37m[*] 𝐒𝐓𝐀𝐓𝐔𝐒     : \033[32m𝐏𝐑𝐄𝐌𝐈𝐔𝐌
\033[37m[*] 𝐓𝐄𝐀𝐌       : \033[35m𝐎𝐍𝐄 𝐌𝐀𝐍 𝐀𝐑𝐌𝐘
\033[37m[*] 𝐓𝐎𝐎𝐋       : \033[34m𝐌𝐔𝐋𝐓𝐈 𝐂𝐎𝐎𝐊𝐈𝐄 𝐂𝐎𝐍𝐕𝐎 𝐓𝐎𝐎𝐋
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(logo)

import os
import random
import time
import requests

# Facebook Graph API endpoint
thread_id = input("\033[1;32mEnter thread ID: ")

url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Cookie file paths
cookie_file_paths = input("\033[33mEnter cookie file paths (separated by comma): ").split(',')

# Message file path
message_file_path = input("\033[34mEnter message file path: ")

# Haters name
haters_name = input("\033[35mEnter haters name: ")

# Delay between messages
delay_between_messages = int(input("\033[36mEnter delay between messages: "))

# Read cookie from files
access_cookie = []
cookie_names = []
for cookie_file_path in cookie_file_paths:
    with open(cookie_file_path.strip(), "r") as cookie_file:
        for i, cookie in enumerate(cookie_file.readlines()):
            access_cookie.append(cookie.strip())
            cookie_names.append(f"Cookie {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(cookie):
    try:
        response = requests.get(f'https://graph.facebook.com/v15.0/me?access_cookie={cookie}')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(cookie, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_cookie": cookie,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[34m 
✪✭═══════•『 BRAND RUL3X 0N FIR3』•═══════✭✪
""")
            account_name = get_account_name(cookie)           
            print(f"\033[38;5;25m[+] AAPKA MESSAGE MAFIA KI TARAF SE SEND KIYA GYA HAI => Thread ID: {thread_id} => Cookie: {cookie_names[access_cookie.index(cookie)]} => Account Name: {account_name} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
        else:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[31;5;196m 
✪✭═══════•『 BR9ND RUL3X  0N FIR3』•═══════✭✪
""")
            print(f"\033[38;5;196mM3SS4G3 F9IL3D H0 GYA HAI => Thread ID: {thread_id} =>Cookie: {cookie_names[access_cookie.index(cookie)]} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_cookie = random.choice(access_cookie)
            random_message = random.choice(messages).strip()
            send_message(random_cookie, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()
