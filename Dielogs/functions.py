from Responses.resps import *
from Models.db import *
from datetime import datetime

def RegisterProcedure(req, users_table):
    context = req['request']['nlu']['tokens']
    users_table.InsertNewUser(req['session']['user']['user_id'], req['request']['nlu']['tokens'][1],
                        req['request']['nlu']['tokens'][2], int(req['request']['nlu']['tokens'][3]))
    res = ReturnSuccessRegisterMessage(req)
    return res

def FirstHelloProcedure(req):
    res = ReturnFirstHelloMessage(req)
    return res

def HelloProcedure(req):
    res = ReturnHelloMessage(req)
    return res

def DontUnderstandProcedure(req):
    res = ReturnDontUnderstandMessage(req)
    return res

def InsertNewPulseProcedure(req, user_table, pulse_table):
    date = datetime.now()
    date = date.strftime('%d/%m/%Y %H:%M')
    pulse_count = int(req['request']['nlu']['tokens'][1])
    user_id_in_yandex = req['session']['user']['user_id']
    user_id = user_table.GetUserData(user_id_in_yandex)[0]
    pulse_table.InsertNewPulseData(user_id, pulse_count, date)
    req = ReturnPulseDetectedMessage(req)
    return req

def OuputHelpingMessage(req):
    res = ReturnHelpingMessage(req)
    return res

def OutputLastStatistic(req, user_table, pulse_table):
    user_id_in_yandex = req['session']['user']['user_id']
    user_id = user_table.GetUserData(user_id_in_yandex)[0]
    pulse_stat = pulse_table.GetLastPulse(user_id)
    res = ReturnUserStat(req, pulse_stat)
    return res