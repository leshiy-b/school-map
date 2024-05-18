from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test_request():
    # p = request.args["test_p"]
    # print(f"test_request: {p}")
    #
    html_page = f"""
<html>
<body>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
<p> <var>i<var> <p>
<img src="/static/test_plan.png" alt="Plan" width="519" height="415"> 
<p>Please enter some text below:<p>
<input type="text" name="first_name" placeholder="John" required>
</body>
</html>    
    """

    return html_page, 200


# flask --app main run
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)

#<img src="https://i.pinimg.com/564x/da/dc/9e/dadc9e5808e2e9a2b98fe48217a3e5a7.jpg" alt="Plan" width="519" height="415">