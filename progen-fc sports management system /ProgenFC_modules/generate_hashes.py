import hashlib

passwords = {
    "admin": "progenfcadmin",
    "C001": "progenfcC001",
    "finofficer": "progenfcfinofficer",
    "facmanager": "progenfcfacmanager",
    "compmanager": "progenfccompmanager",
    "A001": "progenfcA001",
}
for username, password in passwords.items():
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    print(username)
    print(password_hash)
    print()
