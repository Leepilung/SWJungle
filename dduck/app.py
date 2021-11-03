
from os import name
from flask import Flask, flash, request, jsonify, render_template, url_for, redirect
from pymongo import MongoClient
from datetime import datetime
import hashlib
import jwt

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
SECRET_KEY = '8조'  
client = MongoClient ('localhost', 27017)
db = client.signuptest


@app.route('/')
def home():
    return render_template('register.html')\

@app.route('/register', methods=["GET", "POST"])
def bulletin_write():
    if request.method == "POST":
        id = request.form.get("id", type=str)
        pw = request.form.get("pw", type=str)
        pwchk = request.form.get("pwchk", type=str)
        name = request.form.get("name", type=str)
      
        if id == "":
            flash("아이디를 입력하세요.")
            return render_template("register.html")
        elif pw =="":
            flash("비밀번호를 입력하세요.")
            return render_template("register.html")
        elif pw != pwchk:
            flash("비밀번호가 다릅니다.")
            return render_template("register.html")
        elif name =="":
            flash("이름을 입력하세요.")
            return render_template("register.html")      

        check_cnt = db.users.find({"id" : id}).count()
        if check_cnt > 0:
            flash("등록된 id입니다.")
            return render_template("register.html")
            
        to_db = {
            "id" : id,
            "pw" : generate_password_hash(pw),
            "name" : name,
        }        
        db.users.insert_one(to_db)
       
        flash("회원 가입 되었습니다")
        return render_template("register.html") 
    else:
        return render_template("register.html")    
        

@app.route('/sign_up', methods=['POST'])
def sign_up_save():
    # 회원 가입 시 받을 정보 3가지
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    email_receive = request.form['email_give']
    # password의 경우 보안을 위해 hash 처리
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    user_data = {
        'username': username_receive,
        'password': password_hash,
        'email': email_receive
    }
    db.users.insert_one(user_data)
    return jsonify({'result': 'success'})


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


@app.route('/asd')
def home2():
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