from flask import Flask, request
from html_pages import main_html

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    image = "/static/test_plan.png"
    room = request.args.get("room")
    # 1. Learn json format, fill in rooms.json file
    # 2. Load json from file, convert to dict
    # 3. Use dict instead of if-else's
    if room == "2":
        image = "/static/test_plan2.jpg"
    elif room == "3":
        image = "/static/test_plan3.jpg"
    elif room == "4":
        image = "/static/test_plan4.jpg"
    elif room == "5":
        image = "/static/test_plan5.jpg"

    # Add "clear" button
    # Show several floors
    return main_html(image), 200

    # {
    #     "floors": [
    #                     {"default":"img100", "101":"img1", "102":"img1", "103":"img1"},
    #                     {"default":"img200", "201": "img1", "202": "img1", "203": "img1"},
    #                     …
    #                 ]
    # }


# flask --app main run
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)

