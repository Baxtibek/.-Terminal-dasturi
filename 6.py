# File
f = open("file.txt", "w")
f.write("Bu yerda fayl yaratildi.")

f =  open("file.txt")
text = f.read()
print(text)
f.close()

# JSON fayl
import json

x = {
    "name": "Ali",
    "age": 20,
    "city": "Toshkent"
}

y = json.dumps(x)

f= open("file.json", "w")
f.write(y)
f.close()
print("json filega yozildi")