import webbrowser
from colorama import init, Fore

init(autoreset=True)

GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RESET = "\033[0m"
ROSA = "\033[91m\033[97m"

yt = "1"
thm = "2"
htb = "3"
gpt = "4"
Personalizada = "5"

while True:
    
    print("Opciones:\n")
    print(f"[{Fore.BLUE}1{Fore.RESET}] {Fore.BLUE}Abrir Youtube{Fore.RESET}")
    print(f"[{Fore.RED}2{Fore.RESET}] {Fore.RED}Abrir Tryhackme{Fore.RESET}")
    print(f"[{Fore.GREEN}3{Fore.RESET}] {Fore.GREEN}Abrir Hackthebox{Fore.RESET}")
    print(f"[{Fore.WHITE}4{Fore.RESET}] {Fore.WHITE}Abrir ChatGpt{Fore.RESET}")
    print(f"[{Fore.MAGENTA}5{Fore.RESET}] {Fore.MAGENTA}Abrir URL Personalizada{Fore.MAGENTA}\n")
    
    opcion = input("selecciona una opcion: ")
    
    
    if opcion == yt:
        webbrowser.open('https://www.youtube.com/')
        print("Abriendo Youtube")
        break
    elif opcion ==  thm:
        webbrowser.open('https://tryhackme.com/dashboard')
        print("Abriendo Tryhackme")
        break
    elif opcion == htb:
        webbrowser.open('https://app.hackthebox.com/home')
        print("Abriendo Hackthebox")
        break
    elif opcion == gpt:
        webbrowser.open('https://chat.openai.com/')
        print("Abriendo ChatGpt")
        break
    elif opcion == Personalizada:
        url_Personalizada = input("Ingresa una url: ")
        if url_Personalizada.startswith('https://'):
            webbrowser.open(url_Personalizada)
    else:
        print("Opcion no valida")
        
        