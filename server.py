"""Server route for healthhub landing page"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_landing_page():
  "Display landing page."

  return render_template("base.html")


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port="5000")
