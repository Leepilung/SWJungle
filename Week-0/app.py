from flask import Flask, request, jsonify, render_template, url_for, redirect
from pymongo import MongoClient
import datetime,hashlib,jwt


app = Flask(__name__)

client = MongoClient ('localhost', 27017)
db = client.nameHarmony
app.secret_key = '8조'
SECRET_KEY = '8조'

@app.route('/')
def Home():
    token_receive = request.cookies.get('mytoken')


    if token_receive is not None :
        token_receive = bytes(token_receive.encode('ascii'))
        user_list = []
        try:
            payload= jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_info = db.users.find_one({'id': payload['ID']})
            early_list = list(db.users.find({},{"_id":False,"password":False})) 
            for i in early_list:
                if i['id'] == payload['ID']:
                    continue
                else:
                    user_list.append(i)

            return render_template('main.html', user_info=user_info, user_list=user_list)
        except jwt.ExpiredSignatureError:
            return redirect(url_for('/', message = '로그인 시간이 만료되었습니다.'))
    else :
        return render_template('login.html')

@app.route('/join')
def join():
    return render_template('register.html')

@app.route('/register', methods=["GET", "POST"])
def bulletin_write():
    if request.method == "POST":
        id = request.json.get("id")
        name = request.json.get("name")
        password = request.json.get("password")
        passwordCheck = request.json.get("passwordCheck")

        if len(id) == 0:    # 6 ~ 18
            return jsonify({'msg':'아이디를 입력해야 합니다.'}), 400
        elif len(id) < 4 or len(id) > 18:
            return jsonify({'msg':'아이디의 길이를 6글자 ~ 18자로 입력해야 합니다.'}),400 
        elif name =="": 
            return jsonify({'msg':'이름를 입력하세요.'}), 400
        elif len(name) > 12:
            return jsonify({'msg' : '이름을 12자 이내로 입력해야 합니다.'})
        elif password =="": #6~18
            return jsonify({'msg':'비밀번호를 입력하세요.'}),400 
        elif len(password) < 6 or len(password) > 18:
            return jsonify({'msg':'비밀번호의 길이를 6글자 ~ 18자로 입력해야 합니다.'}),400 
        elif passwordCheck == "":
            return jsonify({'msg':'비밀번호를 확인 해주세요'}),400 
        elif password != passwordCheck:
            return jsonify({'msg':'비밀번호가 서로 다릅니다.'}),400 

    
        check_cnt = db.users.find({"id" : id}).count()
        if check_cnt > 0:
            return jsonify({'msg':'이미 등록된 id입니다.'})
            
        to_DB = {
            "id" : id,
            "password" : hashlib.sha256(password.encode('utf-8')).hexdigest(),
            "name" : name,
        }

        db.users.insert_one(to_DB)
       
        return jsonify({'msg' : '회원가입에 성공했습니다 !'})
    else:
        return render_template("register.html")

#로그인 시도 시 토큰 생성.
@app.route('/sign_in', methods=['POST'])
def sign_in_user():
    id_receive = request.json.get("id")
    password_receive = request.json.get("password")
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'id': id_receive, "password": password_hash})


    if result is not None :
        payload = {
            'ID': id_receive,
            'NAME': result['name'],
            'EXP': str(datetime.datetime.utcnow() + datetime.timedelta(seconds = 60 * 60 * 24*1000))
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': str(token)})
    else :
        return jsonify({'result': 'fail', 'msg': 'ID / Password가 정확하지 않습니다.'}),400


if __name__ == "__main__":
    app.secret_key = '8조'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0' , debug=True, port=5000)
