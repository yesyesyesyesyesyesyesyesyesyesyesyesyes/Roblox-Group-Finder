import os 
import threading
import requests, random
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Aleks Group Finder")


def groupfinder():
    id = random.randint(1000000, 1150000)
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+] Hit: {id}")
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")


print("""


____ _    ____ _  _ ____    ____ ____ ____ _  _ ___  
|__| |    |___ |_/  [__     | __ |__/ |  | |  | |__] 
|  | |___ |___ | \_ ___]    |__] |  \ |__| |__| |    
                                                     
____ _ _  _ ___  ____ ____ 
|___ | |\ | |  \ |___ |__/ 
|    | | \| |__/ |___ |  \ 
                           
""")

#your webhook
hook = input("[-] https://discord.com/api/webhooks/1025806453916835932/ZTtAPnydT8knzTypJ4QUIcMnSrRTWrin6OtHo8VjK-j6hjar0ID-4KGj_LtuzeTS4cyS: "))
#number of threads
threads = int(input("[-] 25: "))

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
