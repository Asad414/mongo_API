
import pymongo
from flask import Flask, jsonify

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://klaxx:klaxx@cluster0.44ffm.mongodb.net/?retryWrites=true&w=majority")
db = client['myFirstDatabase']
collection = db['products']


@app.route('/')
def index():
    data = collection.find()
    li = []
    li2 = []
    for item in data:
        li.append(item)
    for i in range(len(li)):
        li2.append({'name':li[i]['name'],'price':li[i]['price'],'description':li[i]['description'],'image':li[i]['image'],'createdAt':li[i]['createdAt']})
    return jsonify(li2)
#data = collection.find_one({'name':'Slip-On Cross'})

if __name__=='__main__':
    app.run(host='0.0.0.0')