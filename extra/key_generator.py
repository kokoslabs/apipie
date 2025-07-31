import secrets
import hashlib

def generate_api_key():
    # Generate a secure random API key
    key = secrets.token_hex(32)  # 64 characters, 256-bit
    return key

def hash_api_key(api_key):
    return hashlib.sha256(api_key.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    api_key = generate_api_key()
    hashed = hash_api_key(api_key)

    print("Generated API Key (save this!):")
    print(api_key)
    print("/nStore this hash in config:")
    print(hashed)