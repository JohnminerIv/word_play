from starter_code.dictogram import Dictogram
from my_code.my_module import clean_return_list, read_file, _format

clean_list = clean_return_list(read_file('text_files/1661-.txt'))
histogram = Dictogram(clean_list)
print(histogram.types)
