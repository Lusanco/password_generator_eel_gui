import eel
import json
import os

history_count = 0
# favorit_count = 0

eel.init("web")


def read_from_history():
    with open("history.json", "r") as history_file:
        history_content = json.loads(history_file.read())
        return history_content


def write_to_history(history_content):
    with open("data.json", "w") as history_file:
        history_file.write(json.dumps(history_content))
        return history_content


@eel.expose
def create_password(password):
    global history_count

    new_password = {"id": history_count + 1, "password": password}

    history_content = read_from_history()
    history_content["history"].append(new_password)

    write_to_history(history_content)
    history_count += 1

    return new_password


@eel.expose
def show_password_history():
    return read_from_history()


@eel.expose
def clear_password_history():
    global history_count

    history_content = read_from_history()
    for password in history_content["history"]:
        history_content["history"].remove(password)
        history_count -= 1
    write_to_history(history_content)


if not os.path.exists("history.json"):
    history_content = open("history.json", "w")
    history_content.write(json.dumps({"history": []}))
else:
    history_content = read_from_history()
    history_count = len(history_content["history"])

eel.start("index.html")
