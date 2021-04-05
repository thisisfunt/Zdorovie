from flask import Flask, request
import json
from Models.db import *
from Responses.resps import *
from Dielogs.functions import *

app = Flask(__name__)

users_table = Users()
pulse_table = Pulse()


@app.route('/', methods=['POST'])
def _main():
    print('new request')
    req = request.json

    print("REQUEST: -------------------------")
    print(req)

    if len(req['request']['nlu']['tokens']) == 0 and not users_table.CheckUserExist(req['session']['user']['user_id']):
        print('new user')
        res = FirstHelloProcedure(req)
    elif len(req['request']['nlu']['tokens']) == 0 and users_table.CheckUserExist(req['session']['user']['user_id']):
        print('user')
        res = HelloProcedure(req)
    elif req['request']['nlu']['tokens'][0] == 'зарегистрироваться' and not users_table.CheckUserExist(req['session']['user']['user_id']):
        print('registration')
        res = RegisterProcedure(req, users_table)
    elif req['request']['nlu']['tokens'][0] == 'пульс' and users_table.CheckUserExist(req['session']['user']['user_id']):
        print('wrote pulse')
        res = InsertNewPulseProcedure(req, users_table, pulse_table)
    elif req['request']['command'] == 'помощь':
        res = OuputHelpingMessage(req)
    elif req['request']['command'] == 'статистика':
        res = OutputLastStatistic(req, users_table, pulse_table)
    else:
        res = DontUnderstandProcedure(req)

    print("RESPONSE: ------------------------")
    print(res)

    return json.dumps(res, indent=2)



if __name__ == '__main__':
    app.run(port=8080)