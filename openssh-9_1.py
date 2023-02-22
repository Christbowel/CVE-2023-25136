import paramiko
import socket
from termcolor import colored
import pyfiglet

ascii_text = pyfiglet.figlet_format("openssh 9.1", font="starwars")
ascii_text += "\n\033[38;2;255;153;51m\033[2m✨💥by christbowel🎭💻\033[0m"
print(ascii_text)

print ("")

ip_file = input("Entrer la liste d'adresse ip a tester 🔥 : ")

client_id = "PuTTY_Release_0.64"

def check_ssh_vulnerability(ip):
    try:
        transport = paramiko.Transport(ip, timeout=1)

        transport.local_version = f"SSH-2.0-{client_id}"

        transport.connect(username='', password='')

        print(colored(f"{ip}: Vulnérable", 'green'))

        transport.close()

    except (socket.error, paramiko.AuthenticationException, paramiko.SSHException):

        print(colored(f"{ip}: Non vulnérable", 'red'))


with open(ip_file, 'r') as f:
    for line in f:
        ip = line.strip()
        check_ssh_vulnerability(ip)

