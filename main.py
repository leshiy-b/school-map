from flask import Flask, request

app = Flask(__name__)

@app.route('/test_request', methods=['GET'])
async def test_request():
    p = request.args["test_p"]
    print(f"test_request: {p}")

    html_page = f"""
<html>
<body>
<h1>My First Heading</h1>
<p>My first paragraph: {p}.</p>
</body>
</html>    
    """

    return html_page, 200


# flask --app main run
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
