from pymongo import MongoClient
import datetime

class mongo(object):


    def getConnection(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['local']
        self.posts = self.database.posts
        # self.insertPost(post)

    def insertPost(self, post):
        print("-----------------------")
        self.getConnection()
        post_id = self.posts.insert_one(post).inserted_id
        print(post_id)
        print("post insert")
        print("-----------------------")
