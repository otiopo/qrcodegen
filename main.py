import flask, qrcode

app = flask.Flask(__name__)

@app.route("/")
def index():
  return flask.render_template("index.html")

@app.route("/makeQr")
def makeQr():
  qr = qrcode.make(flask.request.args.get("text"))
  qr.save("qr.png")
  return flask.send_file("qr.png")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80)