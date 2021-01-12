import signal
import Database
import socket
import BankSystemThread

# actions before ending (on sigint)
def sigint_handler(sig, frame):
	for thread in threads:
		thread.stop_event.set()
		thread.join()
	
	server.close()
	database._update_()
	exit(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)

database = Database.Database("db.json")

signal.signal(signal.SIGINT, sigint_handler)
print("Ctrl-C to exit")

threads = []
while True:
	sock, _ = server.accept()
	threads.append(BankSystemThread.BankSystemThread(sock, database))
	threads[-1].start() # start new thread for new client