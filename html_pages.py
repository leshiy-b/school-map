def main_html(image: str) -> str:
    return f"""<html>
<body>
<h1>My test map</h1>
<p>Search for room number:</p>
<form action="/">
<input type="text" name="room" placeholder="" required>
<input type="submit">
</form>
<img src={image} alt="Plan" width="519" height="415"> 
</body>
</html>    
"""
