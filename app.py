from flask import Flask, render_template, request, redirect, url_for
from my_code.dictionary_words import read_file, choose_words, _format, main
app = Flask(__name__)


@app.route('/')
def home():
    sentence = main('text_files/1661-.txt', 7)
    return f"""<p> {sentence} </p>"""


if __name__ == '__main__':
    app.run(debug=True, port=5000)
