from flask import Flask, request

app = Flask(__name__)
image = "/static/test_plan.png"

@app.route('/', methods=['GET'])
def root():
    image = ""
    room = request.args.get("room")
    if room == 2:
        image = "/static/test_plan2.png"
    elif room == 3:
        image = "/static/test_plan3.png"
    elif room == 4:
        image = "/static/test_plan4.png"
    elif room == 5:
        image = "/static/test_plan5.png"
    return image

    html_page = f"""
<html>
<body>
<h1>My test map</h1>
<p>Search for room number:</p>
<form action="/">
<input type="text" name="room" placeholder="" required>
<input type="submit">
</form>
<img src= {image} alt="Plan" width="519" height="415"> 
</body>
</html>    
"""
    return html_page, 200




# flask --app main run
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)

#<img src="https://i.pinimg.com/564x/da/dc/9e/dadc9e5808e2e9a2b98fe48217a3e5a7.jpg" alt="Plan" width="519" height="415">