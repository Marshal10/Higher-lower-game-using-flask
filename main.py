from flask import Flask
from random import randint

app=Flask(__name__)
random_number=randint(0,9)

@app.route("/")
def hello():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media0.giphy.com/media/grDFHLDd6Bl9vDCr4Z/200w.webp?cid=ecf05e47faa08eizq9bjb1cj4ss8nafs33ypy7stcooqp0gw&ep=v1_gifs_search&rid=200w.webp&ct=g" width="500" height="500">'


@app.route("/<int:num>")
def guess(num):
    if num==random_number:
        pass
    elif num<random_number:
        pass
    elif num>random_number:
        pass
    else:
        return "<h1>Please Type in a number only!</h1>"

if __name__=="__main__":
    app.run(debug=True)