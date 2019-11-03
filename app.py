from flask import Flask, render_template, request, redirect, url_for
from starter_code.dictogram import Dictogram
from my_code.my_module import clean_return_list, read_file, _format
app = Flask(__name__)


@app.route('/')
def home():
    clean_list = clean_return_list(read_file('text_files/1661-.txt'))
    histogram = Dictogram(clean_list)
    sentence = _format(histogram.random_word(10))
    return f"""<p> {sentence} </p>"""


if __name__ == '__main__':
    app.run(debug=True, port=5000)
