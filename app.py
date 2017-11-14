from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

"""english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")"""

english_bot = ChatBot(
    'cds',
    trainer='chatterbot.trainers.ListTrainer'
)

english_bot.train([

    "I would to run a security test on web, need to identify best tool",
    "You can use https://www.websecurify.com/ to test the website vlunaribility.",
    "What is CDS",
    "CDS is an software company.",
    "I need help with Photoshop",
    "Here is the link to Photoshop http://www.adobe.com/products/photoshop.html",
    "I need help with Graphic Design",
    "Here is the link to Graphic Design https://www.behance.net/search?field=44",
    "I need help with Coding",
    "Here is the link to Coding http://www.codeconquest.com/what-is-coding/"
])


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(english_bot.get_response(query))


if __name__ == "__main__":
    app.run()
