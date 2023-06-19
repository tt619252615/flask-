# # document_frequency.py

# import jieba
# from collections import Counter

# def calculate(documents):
#     freq = Counter()
#     for document in documents:  # 注意这里是遍历 documents，而不是单个 document
#         words = list(jieba.cut(document['content']))
#         freq.update(words)
#     return freq

# document_frequency.py

import jieba
from collections import Counter
from .data_processing import process

def calculate(directory):
    documents = process(directory)
    freq = Counter()
    for document in documents:
        words = list(jieba.cut(document['content']))
        freq.update(words)
    return freq
