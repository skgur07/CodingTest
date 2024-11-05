import hashlib

x = input()

encode_x = x.encode()

sha256 = hashlib.sha256()
sha256.update(encode_x)

result = sha256.hexdigest()

print(result)