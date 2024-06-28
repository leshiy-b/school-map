def main_html(images: list) -> str:
    return f"""<html>
<body>
<h1>My test map</h1>
<p>Search for room number:</p>
<form action="/">
<input type="text" name="room" placeholder="" required>
<input type="submit">
</form>
{images_html(images)}
</body>
</html>    
"""


def images_html(images: list) -> str:
    res = ""
    for i in range(len(images)):
        res += f"""<img src="/static/{images[i]}" alt="Plan" width="519" height="415" style="position:fixed; top:300px; left:{550 * i}px;">"""

    return res
