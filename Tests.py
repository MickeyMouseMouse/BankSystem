import socket
import os
import  subprocess
import time
import signal

if os.path.exists("db.json"): os.remove("db.json")

serverProcess = subprocess.Popen("python3 Server.py", shell = True) # start Server
time.sleep(2) # wait a little

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

# Test 1
client.send("sign up Ivan".encode('utf-8'))
if str(client.recv(25).decode('utf-8')) == "1":
	print("Test 1: Pass")
else:
	print("Test 1: Fail")

# Test 2
client.send("amount".encode('utf-8'))
if str(client.recv(25).decode('utf-8')) == "First select your card":
	print("Test 2: Pass")
else:
	print("Test 2: Fail")

# Test 3
client.send("new 1111".encode('utf-8'))
if str(client.recv(25).decode('utf-8')) == "Card id is 1":
	print("Test 3: Pass")
else:
	print("Test 3: Fail")

# Test 4
client.send("get 10".encode('utf-8'))
if str(client.recv(25).decode('utf-8')) == "There is no such money":
	print("Test 4: Pass")
else:
	print("Test 4: Fail")

# Test 5
client.send("put 20".encode('utf-8'))
if str(client.recv(25).decode('utf-8')) == "20":
	print("Test 5: Pass")
else:
	print("Test 5: Fail")

client.send("exit".encode('utf-8'))
client.close()

try:
	os.killpg(os.getpgid(serverProcess.pid), signal.SIGINT) # stop Server
except KeyboardInterrupt:
	exit(0)