# Flask, Pymongo, jsonify, request 패키지
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient 
from flask_jwt_extended import *
from flask import session 



# ObjectId Json 파싱용 
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter

# Json파일 Encoing -> ObjectId값만 문자열(str)으로 변환
class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)

# ObjectId 파싱용 클래스 및 구문
class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)

app = Flask(__name__)
# ObjectId -> Json으로 파싱하기 위한 구문
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter


client = MongoClient('localhost', 27017)
db = client.nameHarmony


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/main')
def main():
    return render_template('main.html')
    
# get 라우트 전체출력
@app.route('/self', methods=['GET'])
def get():
    memos = db.self.find()

    return jsonify({'memos': list(memos)})

# GET 라우트 특정 id값만 출력
@app.route('/self/<objectid:id>', methods=['GET'])
def getOne(id):
    memo = db.self.find_one({'_id': id})

    return jsonify({'memo' : memo})


# POST 메소드
@app.route('/self', methods=['POST'])
def post():
    title = request.json.get('title')

    db.self.insert_one({'title':title})

    return jsonify({'result' : 'POST success'})

# PUT 메소드
@app.route('/self/<objectid:id>', methods=['PUT'])
def put(id):
    title = request.json.get('title')
    body = request.json.get('body')

    db.self.update_one({'_id':id}, {'$set' : {'title' : title}})

    return jsonify({'status' : 'UPDATE success'})

# DELETE 메소드
@app.route('/self/<objectid:id>', methods=['DELETE'])
def delete(id):
    db.self.delete_one({'_id':id})

    return {'status' : 'DELETE success'}



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)