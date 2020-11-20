from flask import Flask, render_template, request, redirect, url_for
from starter_code.dictogram import Dictogram
from my_code.markov import Chain
from my_code.my_module import clean_return_list, read_file, _format
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    m_level = request.form.get('m_level')
    s_amount = request.form.get('s_amount')
    if m_level is not None:
        m_level = int(m_level)
    if s_amount is not None:
        s_amount = int(s_amount)
    if m_level is None or m_level <= 0:
        m_level = 3
    if s_amount is None or s_amount <= 0:
        s_amount = 1

    clean_list = clean_return_list(read_file('text_files/The_Way_of_Kings.txt'))
    histogram = Chain(m_level, clean_list)
    sentence = _format(histogram.sample(s_amount))
    return render_template('index.html', sentence=sentence)


if __name__ == '__main__':
    app.run(port=5000)
