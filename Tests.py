import socket
import os
import  subprocess
import time
import signal

if os.path.exists("Database.txt"): os.remove("Database.txt")

serverProcess = subprocess.Popen("python3 Server.py", shell = True) # start Server
time.sleep(2) # wait a little

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

# Test 1
client.send("sign up Ivan 1234".encode('utf-8'))
if str(client.recv(10).decode('utf-8')) == "1":
	print("Test 1: Pass")
else:
	print("Test 1: Fail")

# Test 2
client.send("amount".encode('utf-8'))
if str(client.recv(10).decode('utf-8')) == "0":
	print("Test 2: Pass")
else:
	print("Test 2: Fail")

# Test 3
client.send("get 10".encode('utf-8'))
if str(client.recv(10).decode('utf-8')) == "Error":
	print("Test 3: Pass")
else:
	print("Test 3: Fail")

# Test 4
client.send("put 10".encode('utf-8'))
if str(client.recv(10).decode('utf-8')) == "10":
	print("Test 4: Pass")
else:
	print("Test 4: Fail")

client.send("exit".encode('utf-8'))
client.close()

try:
	os.killpg(os.getpgid(serverProcess.pid), signal.SIGINT) # stop Server
except KeyboardInterrupt:
	exit(0)