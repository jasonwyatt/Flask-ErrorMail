from flask import Flask, request
from flask_errormail import mail_on_500

ADMINISTRATORS = [
    "jason.feinstein@gmail.com",
]

app = Flask(__name__)

# Where the magic happens.
mail_on_500(app, ADMINISTRATORS)

@app.route("/")
def hello():
    assert 1==2, "1 is not equal to 2!!!"

if __name__ == "__main__":
    app.run()
