import socket
import re

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

print("1) sign in <Client ID> <Card ID> <Pin Code>")
print("2) sign up <Client ID> <Pin Code>")
print("3) exit")
while True:    
    while True:
        line = input(">>> ")
        
        if line == "exit":
            client.send(line.encode('utf-8'))
            client.close()
            exit(0)
        
        if re.fullmatch("sign (in [A-z]+ [0-9]+ [0-9]{4}|up [A-z]+ [0-9]{4})", line):
            client.send(line.encode('utf-8'))
            break
        
        print("Incorrect input")

    card_ID = str(client.recv(10).decode('utf-8'))
    if card_ID == "-1":
        print("Something went wrong. Try again")
    else:
        if card_ID != "0": print("Your Card ID is", card_ID) 
        print("You are signed in")
        break
        
print("1) amount")
print("2) get <money>")
print("3) put <money>")
print("4) exit")
while True:
    line = input(">>> ")
    
    if line == "exit":
        client.send(line.encode('utf-8'))
        client.close()
        break
        
    if re.fullmatch("amount|(get|put) [0-9]+", line):
        client.send(line.encode('utf-8'))
        print(str(client.recv(40).decode('utf-8')))
    else:
        print("Incorrect input")