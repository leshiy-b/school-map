from flask import Flask, request
from html_pages import main_html
import json


app = Flask(__name__)
school_images = SchoolImages("rooms.json")

@app.route('/', methods=['GET'])
def root():
    room = request.args.get("room")

    # json_data = open("rooms.json", "r")
    # rooms = json.load(json_data)
    # floors = rooms["floors"]
    # images = []
    # for i in floors:
    #     images.append(i["default"])
    images = school_images.get(room)

    # Add "clear" button
    # Use room to show proper images
    return main_html(images), 200



# flask --app main run
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)

