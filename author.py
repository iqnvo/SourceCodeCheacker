# import Files
import json
import os
import platform
import random
import threading
import time
import requests

from colorama import Fore

def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())


os.system("cls")
class checker:

    online = None
    path = None
    ModeRun = None

    Found = [] #[0] users
    FoundNumber = 0
    number = 0
    bad = 0
    Unavailable = 0


    def setPath(self, path):
        self.path = str(path) + f"@[{platform.node()}] $"
    
    def getPath(self):
        return self.path
    
    def __init__(self): 

        self.animation()
        
        self.setPath("checker")

        value = self.cheackToolIsOnline()
        if value == "offline":
            self.offline()
        else:
            threading.Thread(target=self.run).start()

    def animation(self, back = False):

        os.system("cls")
        text = """
            _               _       
       __ _| |__   ___  ___| |_ ___ 
      / _` | '_ \ / _ \/ __| __/ __|
     | (_| | | | | (_) \__ \ |_\__ \\
      \__, |_| |_|\___/|___/\__|___/
      |___/                         

                ___
              _/ 66\\
             ( \  ^/__
              \    \__)
              /     \\
        001  /      _\\
             ```````
            """

        faded = ''
        red = 40

        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255

        if back == False:
            print(center(faded))
            
            timer = 5

            while timer >= 0:
                print(center(str(timer)), end="\r")
                time.sleep(1)
                timer = timer - 1


        else:
            return text


    def offline(self):
        os.system("cls")
        textArt = f"""{Fore.RED}
                          .-.
             heehee      /aa \_
                       __\-  / )                 .-.
             .-.      (__/    /        haha    _/oo \\
           _/ ..\       /     \               ( \\v  /__
          ( \  u/__    /       \__             \/   ___)
           \    \__)   \_.-._._   )  .-.       /     \\{Fore.LIGHTRED_EX}This Tool Is Offline{Fore.RED}
           /     \             `-`  / ee\_    /       \_
        __/       \               __\  o/ )   \_.-.__   )
       (   _._.-._/     hoho     (___   \/           '-'
    001 '-'                        /     \\
{Fore.LIGHTRED_EX}try another time{Fore.RED}                 _/       \    teehee
                                (   __.-._/{Fore.RESET}"""
        print(center(textArt))
        input()
        exit()

        



    def cheackToolIsOnline(self):
        
        cheack = requests.get("https://raw.githubusercontent.com/iqnvo/SourceCodeCheacker/main/status.py").text

        try:
            if ('"app": True') in str(cheack):
                app = "online"
            else:
                app = "offline"

        except:
            app = "offline"

            

        finally:
            print(cheack)
            cheack = None
            return app
            
    def getHeadersLogin(self):
        headers = {
            'cookie': 'csrftoken=missing; mid=missing',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'x-csrftoken': 'missing'
        }
        return headers
    
    def getUrlLogin(self):
        return "https://www.instagram.com/accounts/login/ajax/"
    
    def getPayloadLogin(self, username):
        payload = {
            'username': username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:{}'.format(username)
        }
        return payload

    #<cheakers>
    def cheackRandom(self, long, File = None):
        self.online = False
        

        while True:
            username = "".join(random.choice("qazwsxedcrfvtgbyhnujmikolp1234567890")for i in range(long))

            try:
                cheack = requests.post(self.getUrlLogin(), headers=self.getHeadersLogin(), data=self.getPayloadLogin(username)).text
                
                if ('"message":"Sorry, your password was incorrect. Please double-check your password."') in cheack or ('"user":false') in cheack:
                    
                    self.Found.append(username)
                    self.FoundNumber +=1

                    with open("Found.txt", "a") as File:
                        File.write(username + "\n")
                        File.close()

                elif ('"user":true') in cheack:
                    self.number +=1
                    self.Unavailable +=1



                else:
                    self.bad +=1
            except:
                self.bad +=1

            finally:
                os.system("cls")
                print(f"{Fore.LIGHTYELLOW_EX}BAD [{self.bad}]{Fore.LIGHTBLUE_EX}, {Fore.LIGHTGREEN_EX}Found [{self.FoundNumber}]{Fore.LIGHTBLUE_EX}, {Fore.LIGHTRED_EX}Unavailable [{self.Unavailable}]{Fore.RESET}\n", end="\r")
                #time.sleep(int(random.choice([19, 9, 30, 7, 15, 18])))
                time.sleep(int(7))



    def listCheaker(self):
        return f"""{Fore.LIGHTYELLOW_EX}[+] normal\n{Fore.LIGHTRED_EX}[UPDATE] soon...{Fore.RESET}"""
    #</cheakers>
    
    def cleanLin(self, Lin):
        t1 = None
        __text = ""

        for text in Lin:
            
            if text == " " and t1 == None:
                __text = __text + text
                t1 = True
            elif text == " " and t1 != None:
                pass
            else:
                __text = __text + text
                t1 = None
        

        
        print(__text)
        return __text.split(" ")
                



    def checkFile(self, File):
        try:
            open(File, "r").close()
            return True
        except FileNotFoundError:
            return False
                    
                
            

    def setCommand(self, command):
        command = self.cleanLin(command)
        command1 = command[0]

        if command1 == "normal": #normal checker
            t1 = None

            try:
                command[2]
                t1 = True
            except IndexError:
                t1 = False
            
            try:
                if t1 == True:
                    if self.checkFile(command[2]) == True:
                        #threading.Thread(target=self.cheackRandom, args=(int(command[1]), command[2])).start()
                        self.cheackRandom(int(command1), str(command[2]))
                    else:
                        print(f"{Fore.LIGHTRED_EX}[normal] File Not Found{Fore.RESET}")

                else:
                    #print(command[1])
                    #threading.Thread(target=self.cheackRandom, args=(int(command[1]))).start()
                    self.cheackRandom(int(command[1]))

                
            except:
                print(f"{Fore.LIGHTRED_EX}[command] set [long] | set [File]{Fore.RESET}\n")
            
            finally:
                t1 = None
                return True
        
        if command1 == "cls" or command1 == "Cls" or command1 == "clear" or command1 == "Clear": #cls | clear cmd
            os.system("cls")
            return True
        

        if command1 == "99" or command1 == "exit" or command1 == "Exit" or command1 == "leave" or command1 == "Leave":
            print(f"{Fore.LIGHTRED_EX}GOOD BYE ...  press ENTER for exit{Fore.RESET}")
            input()
            exit()
        
        if command1 == "list" or command1 == "List":
            print(self.listCheaker())

        



    def run(self):
        os.system("cls")

        text = f"""            ██████████              
        ████          ████          
      ██                  ██        
    ██                      ██      
    ██                      ██      
  ██    ████    ████          ██    
  ██  ██████    ██████        ██    
  ██  ██████    ██████        ██    
  ██  ████        ████        ██    
  ██                          ██    Online
  ██        ████      ████    ██    
██  ██      ████    ██        ██    
██  ▒▒██            ██  ██      ██  
  ▒▒  ▒▒████        ████          ██
  ▒▒  ▒▒    ██████              ██  
  ░░░░░░          ██████████████    
░░░░░░░░░░                          
░░  ░░  ░░                          
  ░░░░░░                            
"""
        faded = ''
        red = 40

        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        print(center(faded))

        if self.online == None:
            self.online = True

            while self.online:
                command = input(self.getPath())

                self.setCommand(command)
                
    
        



cheack = checker()
