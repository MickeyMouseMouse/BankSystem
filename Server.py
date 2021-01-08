import threading
import os.path
import signal
import BankSystemThread
import Database
import Account
import socket

# actions before ending (on sigint)
def signal_handler(sig, frame):
	server.close()
	database.save()
	exit(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)

database = Database.Database("Database.txt")

signal.signal(signal.SIGINT, signal_handler)
print("Ctrl-C to exit")

while True:
	sock, _ = server.accept()
	BankSystemThread.BankSystemThread(sock, database).start() # start new thread for new client