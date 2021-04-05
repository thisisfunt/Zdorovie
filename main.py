from flask import Flask, request
import json
from Models.db import Users
from Responses.resps import *
from Dielogs.functions import *

app = Flask(__name__)


def main():
    users = Users()
    req = request.json
    print(req)
    if len(req['request']['nlu']['tokens']) > 0:
        if req['request']['nlu']['tokens'][0] == 'зарегистрироваться' and not users.CheckUserExist(req['session']['user']['user_id']):
            context = req['request']['nlu']['tokens']
            users.InsertNewUser(req['session']['user']['user_id'], req['request']['nlu']['tokens'][1], req['request']['nlu']['tokens'][2], int(req['request']['nlu']['tokens'][3]))
            res = ReturnSuccessRegisterMessage(req)
            print("Прошла рекистрация")
        else:
            res = ReturnFirstHelloMessage(req)
            print("Первое приветственное сообщение")
    elif not users.CheckUserExist(req['session']['user']['user_id']):
        res = ReturnFirstHelloMessage(req)
        print("Первое приветственное сообщение")
    else:
        res = ReturnHelloMessage(req)
        print("Приветственное сообщение")

    print("REQUEST: -------------------------")
    print(req)
    print("RESPONSE: ------------------------")
    print(res)
    del users
    return json.dumps(res, indent=2)

@app.route('/', methods=['POST'])
def _main():
    print('new request')
    users_table = Users()
    req = request.json
    if len(req['request']['nlu']['tokens']) == 0 and not users_table.CheckUserExist(req['session']['user']['user_id']):
        print('new user')
        res = FirstHelloProcedure(req)
    elif len(req['request']['nlu']['tokens']) == 0 and users_table.CheckUserExist(req['session']['user']['user_id']):
        print('user')
        res = HelloProcedure(req)
    elif req['request']['nlu']['tokens'][0] == 'зарегистрироваться' and not users_table.CheckUserExist(req['session']['user']['user_id']):
        print('registration')
        res = RegisterProcedure(req, users_table)

    else:
        res = DontUnderstandProcedure(req)
    print("REQUEST: -------------------------")
    print(req)
    print("RESPONSE: ------------------------")
    print(res)

    return json.dumps(res, indent=2)



if __name__ == '__main__':
    app.run(port=8080)