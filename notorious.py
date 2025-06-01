def importing():
    import importlib
    global AES, get_random_bytes, base64
    aes_module = importlib.import_module("Crypto.Cipher.AES")
    AES = aes_module  # AES.new(...) kullanılacak
    random_module = importlib.import_module("Crypto.Random")
    get_random_bytes = getattr(random_module, "get_random_bytes")
    base64 = importlib.import_module("base64")

def encrypt_payload(payload, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(payload)
    encrypted = base64.b64encode(cipher.nonce + tag + ciphertext)
    return encrypted

def decrypt_payload(encrypted_payload, key):
    data = base64.b64decode(encrypted_payload)
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    payload = cipher.decrypt_and_verify(ciphertext, tag)
    return payload

importing()
key = get_random_bytes(16)
payload = b"print('Hello World')"

encrypted_payload = encrypt_payload(payload, key)
print("Encrypted:", encrypted_payload)

decrypted_payload = decrypt_payload(encrypted_payload, key)
print("Decrypted:", decrypted_payload.decode())

exec(decrypted_payload.decode())
