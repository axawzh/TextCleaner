import logging

import pdf_client
from pdf_client import config
from pdf_client.api import book
from pdf_client.multithread.worker import MultiThreadWorker
from pdf_client.multithread.processor import TextProcessor

from main import CleanStart

# load global config
config.load_from_file('/Users/Zhenghao/Documents/URECA/TextCleaner/config.json')


class MyProcessor(TextProcessor):
    def process(self, text, section_id):
        cleaner = CleanStart()
        text = cleaner.run(text)
        return text


def book_list():
    """get a list of book_id's"""
    book_list = list()
    book_list_api = book.List().execute()
    for book_dict in book_list_api:
        book_list.append(book_dict['id'])
    return book_list


def postbook(book_id):
    # enable INFO level logging
    logging.basicConfig()
    logging.getLogger(pdf_client.multithread.worker.__name__).setLevel(logging.INFO)

    worker = MultiThreadWorker(processor=MyProcessor(), book=book_id, target=3)
    worker.start()

    # completed = worker.start()
    # for future in completed:
    #     section_id, text = future.result()
    #     # handle the results


# if __name__ == '__main__':
#     main()

for book_id in book_list():
    postbook(book_id)
