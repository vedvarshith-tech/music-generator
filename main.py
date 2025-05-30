from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Music Player</title>
</head>
<body>
  <h1>🎶 Simple Music Player 🎶</h1>
  <audio controls autoplay>
    <source src="{{ url_for('static', filename='music.wav') }}" type="audio/wav">
    Your browser does not support the audio element.
  </audio>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
