from flask import Flask, request
from html_pages import main_html
from SchoolImages import SchoolImages
import json


app = Flask(__name__)
school_images = SchoolImages("rooms.json")

@app.route('/', methods=['GET'])
def root():
    room = request.args.get("room")
    images = school_images.create_image_list(room)
    # Add "clear" button
    # Use room to show proper images
    return main_html(images), 200



# flask --app main run
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)

