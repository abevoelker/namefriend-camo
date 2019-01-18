# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class UsernameGeneratorPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.usernames_seen = set()

    def process_item(self, item, spider):
        if item['username'] in self.usernames_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.usernames_seen.add(item['username'])
            return item

class FileWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('usernames/%s.txt' % spider.name, 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = item['username'] + "\n"
        self.file.write(line)
        return item
