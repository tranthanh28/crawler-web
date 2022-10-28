# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from elasticsearch2 import Elasticsearch
import hashlib
# import MySQLdb

class ScrapyWebPipeline:

    def process_item(self, item, spider):
#         self.conn = MySQLdb.connect(user="root",
#                     passwd="root",
#                     db="crawler_test",
#                     host="localhost")
#         cur = self.conn.cursor()
#         cur.execute("SELECT VERSION()")
#
#         data = cur.fetchone()
#
#         print ("Database version : %s " % data)
        es = Elasticsearch('http://localhost:9200')
        doc = {
            'title': item['title'],
            'describe': item['describe'],
            'content': item['content'],
            'time': item['time'],
            'author': item['author'],
            'category': item['category'],
        }
#         resp = es.search(index="test-index", query={"match_all": {}})
#         resp = es.index(index="test-index", id=2, body=doc, timeout=30)
#         resp = es.index(index="test-index2", id=1, document=doc)
        string = str(item["web_link"])
        key_insert = hashlib.md5(str(string).encode('utf-8')).hexdigest()
#         duplicate = es.search(index=self.es_index_v2, doc_type=self.es_doc_type_v2, id=key_insert)
        try:
            duplicate = es.get(index="test-index1", id=key_insert)
        except Exception:
            pass
        resp = es.index(index="test-index1", doc_type ='raw', id=key_insert, body=doc)
        return item
