from flask import Flask, request, jsonify
from time import sleep

app             = Flask(__name__)
app.id_count    = 1
app.users       = {}
app.tweets      = []

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

# 회원가입
@app.route("/sign-up", methods=['POST'])
def sign_up():
    new_user                = request.json
    new_user["id"]          = app.id_count
    app.users[app.id_count] = new_user
    app.id_count            = app.id_count + 1

    return jsonify(new_user)

@app.route("/tweet", methods=['POST'])
def tweet():
    payload = request.json
    user_id = int(payload['id'])
    tweet   = payload['tweet'])

    if user.id not in app.users:
        return '사용자가 존재하지 않습니다.', 400

    if len(tweet) > 300 :
        return "300자를 초과했습니다.", 400

    user_id = int[payload['id'])
    app.tweets.append({
        'user_id' : user_id,
        'tweet'   : tweet
    })
    
    return '', 200
