from flask import Flask, request, abort
from datetime import datetime, date, time
import time

app = Flask(__name__)
messages = [
    {"username": "Nick",  "text": "Hello", "time": 0.0}
]

users = {
    "Nik": "12345"
}


@app.route("/status")
def status():
    return {
        "status": True,
        "name": "Messeger",
        "time": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }

@app.route("/send", methods=["POST"])
def send():
    username = request.json["username"]
    password = request.json["password"]

    if username in users:
        if password != users[username]:
            return abort(401)
        else:
            users[username] = password

    text = request.json["text"]
    current_time = time.time()
    message = {"username": username, "text": text, "time": current_time}
    messages.append(message)
    print(message)
    return {"ok": True}

@app.route("/messages", methods=["GET"])
def messages_view():
    after = float(request.args.get("after"))

    filtered_messages = [message for message in messages if message["time"] > after]

    return {
        "messages": filtered_messages
    }


app.run()
