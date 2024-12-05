from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = "Welcome to My Portfolio"  # This is the dynamic message
    return render_template('home.html', message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)