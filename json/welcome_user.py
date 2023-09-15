from pathlib import Path
import json


def get_user():
    path = Path("username.json")
    if path.exists():
        file = path.read_text(encoding="utf-8")
        username = json.loads(file)
        print(f"welcome {username}")
        return username

    return None  


def save_user(user):
    content = json.dumps(user)
    path = Path("username.json")

    path.write_text(content)
    print(f"user save success {user}")


def main(user):
    if not get_user():
        save_user(user)


user = input("its your name: ")
main(user)
