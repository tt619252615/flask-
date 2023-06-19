# inverted_indexes.py
from .data_processing import process
from .document_frequency import calculate as calculate_df
from collections import defaultdict
import jieba

class InvertedIndex:
    def __init__(self):
        self.inverted_index = defaultdict(set)
        self.documents = []

    def create_from_folder(self, directory):
        for document in process(directory):
            print("Adding document: ", document)  # 打印正在添加的文档
            self.add_document(document)
        print("Inverted index: ", self.inverted_index)  # 打印生成的倒排索引


    def add_document(self, document):
        self.documents.append(document)
        doc_id = len(self.documents) - 1
        for word in jieba.cut(document['content']):
            self.inverted_index[word].add(doc_id)

    def search(self, keyword, df, num):
        doc_ids = self.inverted_index.get(keyword, set())
        # 按照文档频率排序
        doc_ids = sorted(doc_ids, key=lambda id: df[self.documents[id]['title']], reverse=True)
        return [self.documents[id] for id in doc_ids[:num]]

inverted_index = InvertedIndex()

def create(directory):
    inverted_index.create_from_folder(directory)

def search(keyword, df, num):
    return inverted_index.search(keyword, df, num)
