__CHANNEL__ = 'Telegram : @esfelurm'

import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
from time import sleep

init()

print(f"""{Fore.CYAN}
   ____     _____     _____              ________    _____   _____      
  (    )   (  __ \   (_   _)            (___  ___)  / ___/  (_   _)     
  / /\ \    ) )_) )    | |    ________      ) )    ( (__      | |       
 ( (__) )  (  ___/     | |   (________)    ( (      ) __)     | |       
  )    (    ) )        | |                  ) )    ( (        | |   __  
 /  /\  \  ( (        _| |__               ( (      \ \___  __| |___) ) 
/__(  )__\ /__\      /_____(               /__\      \____\ \________/  
                                                                        
    {Fore.YELLOW}Tool to create an app and retrieve api hash and api id of a Telegram account 
    {Fore.LIGHTGREEN_EX}Git & Telegram : @esfelurm\n
""")
Phone = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter your number along with the country code [Ex: +98XXXXXX]: {Fore.RED}")
with requests.Session() as req:
    phone_number = Phone
    
    login0 = req.post('https://my.telegram.org/auth/send_password', data={'phone': phone_number})

    if 'Sorry, too many tries. Please try again later.' in login0.text:
        print(f'{Fore.RED}Your account has been banned!\n Please try again in 8 hours.')
        exit()

    login_data = login0.json()
    random_hash = login_data['random_hash']

    code = input(f'{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Send the code sent in the Telegram account: {Fore.RED}')
    
    login_data = {
        'phone': phone_number,
        'random_hash': random_hash,
        'password': code
    }
    
    login = req.post('https://my.telegram.org/auth/login', data=login_data)
    
    # Create an app
    app_name = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter a name for your app: {Fore.RED}")
    short_name = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter a short name for your app: {Fore.RED}")
    platform = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter the platform for your app (e.g., web, android): {Fore.RED}")
    url = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter the URL of your app: {Fore.RED}")
    description = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter a description for your app: {Fore.RED}")
    
    app_creation_data = {
        'app_title': app_name,
        'app_shortname': short_name,
        'app_url': url,
        'app_platform': platform,
        'app_desc': description
    }
    
    app_creation = req.post('https://my.telegram.org/apps/create', data=app_creation_data)
    if app_creation.status_code == 200:
        print(f"{Fore.GREEN}App created successfully!")
    else:
        print(f"{Fore.RED}Failed to create the app. Status Code: {app_creation.status_code}")
        exit()
    
    # Retrieve API credentials
    apps_page = req.get('https://my.telegram.org/apps')
    soup = BeautifulSoup(apps_page.text, 'html.parser')
    try:
        api_id = soup.find('label', string='App api_id:').find_next_sibling('div').select_one('span').get_text()
        api_hash = soup.find('label', string='App api_hash:').find_next_sibling('div').select_one('span').get_text()
        sleep(3)
        print(f"""{Fore.GREEN}
    APIs successfully received:

        {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Api ID: {Fore.YELLOW}{api_id}
        {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Api HASH: {Fore.YELLOW}{api_hash}
    """)
    except Exception as e:
        print(f'{Fore.RED}Failed to retrieve APIs: {e}')
