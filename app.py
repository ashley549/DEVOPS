from flask import Flask,render_template

app = Flask(__name__)#obj named flask

@app.route('/')
def greet():
    return render_template('index.html')#connecting html file

if __name__ == '__main__':
    app.run(debug=True)  # for live changes in development