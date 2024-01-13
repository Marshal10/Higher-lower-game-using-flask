from flask import Flask
from random import randint

app=Flask(__name__)
random_number=randint(0,9)

@app.route("/")
def hello():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media0.giphy.com/media/grDFHLDd6Bl9vDCr4Z/200w.webp?cid=ecf05e47faa08eizq9bjb1cj4ss8nafs33ypy7stcooqp0gw&ep=v1_gifs_search&rid=200w.webp&ct=g" width="500" height="500">'\


@app.route("/<int:num>")
def guess(num):
    if num==random_number:
        return '<h1 style="color:green;">That\'s Right.</h1>'\
                '<img src="https://media4.giphy.com/media/i1ryib8WmQE6vObauh/200w.webp?cid=ecf05e472slr7n0v4lahu12uw96ievjhppslphas07wc83py&ep=v1_gifs_search&rid=200w.webp&ct=g" width="500" height="500">'
    elif num<random_number:
        return '<h1 style="color:red;">Too low,try again!</h1>'\
                '<img src="https://media3.giphy.com/media/DigJbk2sGt74qoZPc2/200w.webp?cid=ecf05e47uok7qm1rlq6g5f1b0r1jd370deq19qiq8du8ss14&ep=v1_gifs_search&rid=200w.webp&ct=g" width="500" height="500">'
    elif num>random_number:
        return '<h1 style="color:violet;">Too high,try again!</h1>'\
                '<img src="https://media1.giphy.com/media/zhUJywzAANH5f3MpKy/200.webp?cid=ecf05e47bo6aaohybprwc8sfnzy00wafvbtgjrx7e7uy5g78&ep=v1_gifs_search&rid=200.webp&ct=g" width="500" height="500">'
    else:
        return '<h1>Please Type in a number only!</h1>'

if __name__=="__main__":
    app.run(debug=True)