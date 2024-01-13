from flask import Flask

app=Flask(__name__)


@app.route("/")
def hello():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media0.giphy.com/media/grDFHLDd6Bl9vDCr4Z/200w.webp?cid=ecf05e47faa08eizq9bjb1cj4ss8nafs33ypy7stcooqp0gw&ep=v1_gifs_search&rid=200w.webp&ct=g" width="500" height="500">'



if __name__=="__main__":
    app.run(debug=True)