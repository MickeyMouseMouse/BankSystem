import signal
import socket
import re

def sendMessage(msg):
    try:
        client.send(msg.encode('utf-8'))
    except socket.error:
        print("Server disconnected")
        exit(0)

def receiveMessage():
    try:
        return str(client.recv(40).decode('utf-8'))
    except socket.error:
        print("Server disconnected")
        exit(0)

# actions before ending (on sigint)
def sigint_handler(sig, frame):
    client.send("exit".encode('utf-8'))
    client.close()
    exit(0)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1.5)
try:
    client.connect(("127.0.0.1", 8080))
except socket.error:
    print("Server is unavailable")
    exit(0)

signal.signal(signal.SIGINT, sigint_handler)
print("Ctrl-C to exit")

print("1) sign in <Client ID>")
print("2) sign up <Client Name>")
while True:
    line = input(">>> ") 

    if re.fullmatch("sign in [0-9]+", line):
        sendMessage(line)
        name = receiveMessage()
        if name == "-1":
            print("Error occurred. Try again")
            continue
        else:
            print("Hello,", name)
            break

    if re.fullmatch("sign up [A-z]+", line):
        sendMessage(line)
        _id_ = receiveMessage()
        print("Your ID is", _id_)
        break
        
    print("Incorrect input")

print("You are signed in")
print("1) select <card ID> <pin code>")
print("2) new <pin code>")
print("3) amount")
print("4) get <money>")
print("5) put <money>")
while True:
    line = input(">>> ")
        
    if re.fullmatch("select [0-9]+ [0-9]{4}|new [0-9]{4}|amount|(get|put) [0-9]+", line):
        sendMessage(line)
        print(receiveMessage())
    else:
        print("Incorrect input")