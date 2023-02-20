from flask import Flast, jsonity, request       # 1

app             =Flask(__name__)
app.users       ={}                             # 2
app.id_count    = 1                             # 3

@app.route("/sign-up", methods=['POST'])        # 4
def sign_up():
    new_user                = request           # 5
    new_user["id"]          = app.id_count      # 6
    app.users[app.id_count] = new_uset          # 7
    app.id_count            = app.id_count + 1  # 8

    return jsonity(new_user)                    # 9

# 1) request => 사용자가 HTTP request를 통해 전송한 JSON 데이터를 읽어들임
#   jsonity => dictionary 객체를 JSON으로 변환하여 HTTP response로 보냄
# 2) 새로 가입한 사용자를 저장할 dictionary를 users 변수에 정의
#   key는 사용자 ID이며, value는 dictionary에 저장된 사용자 정보
# 3) 사용자 ID값을 저장하는 변수. ID는 1부터 시작하여 새 사용자 생성시마다 1 증가
# 4) route 데코레이터를 사용하여 엔드포인트를 정의
# 5) HTTP request를 통해 전송된 회원 정보를 읽어들임. request.json은 요청을 통해 전송된 JSON 데이터를 파이썬 dictionary로 변환함
# 6) HTTP request로 전송된 회원가입 정보에 id값을 더함
# 7) 가입하는 사용자 정보를 2)에서 생성한 dictionary에 저장
# 8) id값에 1을 더하여 id값이 중복되지 않도록 함
# 9) 가입한 사용자 정보를 JSON 형태로 전송함. jsonity를 사용해 dictionary를 JSON으로 변환함
#   status code는 200이 됨. 원래는 status code도 지정해야 하지만, 지정하지 않으면 default 값인 200으로 리턴됨.
