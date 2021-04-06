

import tika
import time
from tika import parser


def extract_tika(filename):
    t_start = time.time()
    tika.TikaClientOnly = True

    # file_to_proc = "/Users/tylerskluzacek/Desktop/conference-proceeding.pdf"
    # file_to_proc = "/Users/tylerskluzacek/Desktop/king-cholera.jpeg"

    # opening pdf file
    parsed_pdf = parser.from_file(filename)

    # saving content of pdf
    # you can also bring text only, by parsed_pdf['text']
    # parsed_pdf['content'] returns string
    data = parsed_pdf['metadata']

    # Printing of content
    # print(data)
    t_end = time.time()
    # print(f"Total time: {t_end - t_start}")

    # <class 'str'>
    # print(type(data))
    return {'mdata': data, 'tot_time': t_end-t_start}


if __name__ == '__main__':
    file_to_proc = "/king-cholera.jpeg"
    print(extract_tika(file_to_proc))
