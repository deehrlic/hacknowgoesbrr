from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("frontpage.html")

@app.route("/parse", methods=['GET', 'POST'])
def parse():
    if request.method == "POST":
        return request.form['what']

        #make verbose
        #get image
        #send to mongo
        #assemble image

if __name__ == "__main__":
    app.run(debug=True)
