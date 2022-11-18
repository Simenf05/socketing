import json

noe = [print("hey")]

noe2 = json.dumps(noe).encode("utf-8")

noe3 = noe2.decode("utf-8")

noe4 = json.loads(noe3)

print(noe3)
print(noe4)

