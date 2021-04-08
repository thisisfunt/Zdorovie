from flask import Flask, request, make_response, render_template, redirect
import json
from Models.db import *
from Dielogs.DefaultMessages import *
from Dielogs.RegistrationMessages import *
from Dielogs.UserStatOperations import *
from Models import *


app = Flask(__name__)

users_table = Users()
pulse_table = Pulse()
au_table = AdminUsers()

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
        res = ReturnLastStatistic(req, users_table, pulse_table)
    else:
        res = DontUnderstandProcedure(req)

    print("RESPONSE: ------------------------")
    print(res)

    return json.dumps(res, indent=2)


@app.route('/login', methods=['POST', 'GET'])
def login():
    res = make_response(render_template('index.html'))
    if request.method == 'POST' and not request.cookies.get('login') and not request.cookies.get('password'):
        if au_table.CheckUserExist(request.form['login'], request.form['password']):
            res.set_cookie('login', request.form['login'])
            res.set_cookie('password', request.form['password'])
    elif 'login' in request.cookies and 'password' in request.cookies:
        if au_table.CheckUserExist(request.form['login'], request.form['password']):
            return redirect("/admin")
    return res



if __name__ == '__main__':
    app.run(port=8080)