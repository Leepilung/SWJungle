
from os import name
from flask import Flask, flash, request, jsonify, render_template, url_for, redirect
from pymongo import MongoClient
from datetime import datetime
import hashlib
import jwt

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

client = MongoClient ('localhost', 27017)
db = client.nameHarmony
app.secret_key = '8조'
SECRET_KEY = '8조'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def bulletin_write():
    if request.method == "POST":
        id = request.form.get("id", type=str)
        name = request.form.get("name", type=str)
        password = request.form.get("password", type=str)
        passwordCheck = request.form.get("passwordCheck", type=str)

        if id == "":
            flash("아이디를 입력하세요.")
            return jsonify({'stauts':'failed','msg':'아이디를 입력하세요.'})
        elif name =="":
            flash("이름을 입력하세요.")
            return render_template("register.html") 
        elif password =="":
            flash("비밀번호를 입력하세요.")
            return render_template("register.html")
        elif passwordCheck == "":
            flash('비밀번호 확인을 해주세요')
            return render_template("register.html")
        elif password != passwordCheck:
            flash("비밀번호가 다릅니다.")
            return render_template("register.html")


        check_cnt = db.users.find({"id" : id}).count()
        if check_cnt > 0:
            flash("이미 등록된 id입니다.")
            return render_template("register.html")
            
        to_db = {
            "id" : id,
            "pw" : hashlib.sha256(password.encode('utf-8')).hexdigest(),
            "name" : name,
        }

        db.users.insert_one(to_db)
       
        flash("회원 가입이 되었습니다!")
        return render_template("login.html") 
    else:
        return render_template("register.html")

@app.route('/sign_in', methods=['POST'])
def sign_in_user():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'email': email_receive, 'password': password_hash})
    if result is not None :
        payload = {
            'ID': email_receive,
            'NAME': result['username'],
            'EXP': str(datetime.datetime.utcnow() + datetime.timedelta(seconds = 60 * 60 * 24))
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'resul': 'success', 'token': str(token)})
    else :
        return jsonify({'result': 'fail', 'message': 'E-mail/Password가 정확하지 않습니다.'})


@app.route('/asda')
def cookiehome():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None :
        token_receive = bytes(token_receive[2:-1].encode('ascii'))
        try:
            payload= jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_info = db.users.find_one({'email': payload['ID']})
            return render_template('index.html', user_info=user_info)
        except jwt.ExpiredSignatureError:
            return redirect(url_for('/sign_in', message = '로그인 시간이 만료되었습니다.'))
    else :
        return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = '8조'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0' , debug=True, port=5000)

# from os import name
# from flask import Flask, render_template, jsonify, request, flash
# from pymongo import MongoClient 

# app = Flask(__name__)

# client = MongoClient('localhost', 27017)
# db = client.nameHarmony

# app.secret_key = '8조'

# @app.route('/')
# def Home():
#     return render_template('login.html')

# @app.route('/join')
# def register():
#     return render_template('join.html')

# # 회원가입 POST 메소드
# @app.route('/join', methods=['POST'])
# def post():
#     id = request.json.get('id')
#     name = request.json.get('name')
#     password = request.json.get('password')
#     passwordCheck = request.json.get('passwordCheck')

#     if id == "":
#         flash("아이디를 입력하세요.")
#         return render_template("join.html")
#     if name == "":
#         flash("이름을 입력하세요.")
#         return render_template("join.html")
#     if password == "":
#         flash("비밀번호를 입력하세요.")
#         return render_template("join.html")
#     if password != passwordCheck:
#         flash("비밀번호가 다릅니다.")
#         return render_template("join.html")

#     check_cnt = db.login.find({"id" : id}).count()
#     if check_cnt > 0:
#         flash("등록된 id입니다.")
#         return render_template("join.html")

#     db.login.insert_one({'id':id,'name':name,'password':password})

#     flash("회원 가입 되었습니다")
#     return jsonify({'result' : 'POST success'})

# @app.route('/login', methods=['POST'])
# def login():

#     user_id = request.json.get('id')
#     user_password = request.json.get('password')
#     print(user_id,user_password)

#     if not user_id:
#         return jsonify({"msg": "Missing user_id parameter"}), 400
#     if not user_password:
#         return jsonify({"msg": "Missing user_password parameter"}), 400

#     List = list(db.login.find({'id' : user_id},{'_id':0}))
#     id = List[0]['id']
#     password = List[0]['password']
#     if(user_id == id and user_password == password):
#         return jsonify(
# 			result = "success",
# 			# 검증된 경우, access 토큰 반환
# 			access_token = create_access_token(identity = user_id,
# 											expires_delta = False)
# 		)
#     # 아이디, 비밀번호가 일치하지 않는 경우
    
#     else:
#         return jsonify(
# 			result = "Invalid Params!"
# 		),401

# @app.route('/user_only', methods=['GET'])
# @jwt_required()
# def main():
#     cur_user = get_jwt_identity()
#     if cur_user is None:
#         return "로그인이 필요합니다."
#     else:
#         return "Hi!," + cur_user


# # get 라우트 전체출력
# @app.route('/self', methods=['GET'])
# def get():
#     memos = db.self.find()

#     return jsonify({'memos': list(memos)})

# # GET 라우트 특정 id값만 출력
# @app.route('/self/<objectid:id>', methods=['GET'])
# def getOne(id):
#     memo = db.self.find_one({'_id': id})

#     return jsonify({'memo' : memo})




# # PUT 메소드
# @app.route('/self/<objectid:id>', methods=['PUT'])
# def put(id):
#     title = request.json.get('title')
#     body = request.json.get('body')

#     db.self.update_one({'_id':id}, {'$set' : {'title' : title}})

#     return jsonify({'status' : 'UPDATE success'})

# # DELETE 메소드
# @app.route('/self/<objectid:id>', methods=['DELETE'])
# def delete(id):
#     db.self.delete_one({'_id':id})

#     return {'status' : 'DELETE success'}


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)