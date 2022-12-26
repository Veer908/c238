import hashlib

filename="screenshot (2).png"

with open(filename,'rb') as f:
	file_data=f.read()

image_hash=hashlib.sha256(file_data).hexdigest()

print(image_hash)