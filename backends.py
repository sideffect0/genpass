def stdout(data):
    print(data)

def json(data):
    import json
    with open("file.json", "w") as file:
         file.write(json.dumps(data))

def sqlite_cipher(data):
    pass
