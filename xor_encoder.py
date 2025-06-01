import base64
import requests

url = "https://raw.githubusercontent.com/utkuberkaytan/notorious_project/refs/heads/main/keys"
res = requests.get(url)
lines = res.text.strip().split("\n")

def xor_encrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open("payload.py", "rb") as f:
    payload = f.read()

b64_payload = base64.b64encode(payload)
xor_key = lines[0].strip().encode()
encrypted = xor_encrypt(b64_payload, xor_key)

with open("payload.bin", "wb") as f:
    f.write(encrypted)
