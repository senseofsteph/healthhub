"""Server route for healthhub landing page."""

# TODO:
# Fix localhost connection
# Same images
# Add CSS styling

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_landing_page():
  "Display landing page."

  return render_template("base.html")


# if __name__ == '__main__':
#   app.run(debug=True, host="0.0.0.0", port="5000")

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    app.debug = True
    app.run('0.0.0.0', port="8080")
