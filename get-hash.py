import hashlib

hasher = hashlib.md5()
with open('testfile.txt', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(hasher.hexdigest())
