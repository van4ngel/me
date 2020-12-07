import base64
import json

print("Tell me your name ?", end="\n")
n = str(input()).lower()
nEncoded = base64.b64encode(n.encode())

with open("people.json", "r") as f:
    people = json.load(f)

r = people['people'][nEncoded.decode()]
print(base64.b64decode(r).decode())
