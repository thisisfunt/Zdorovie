from Responses.UserStatOperations import *
from Models.db import *
from datetime import datetime


def InsertNewPulseProcedure(req, user_table, pulse_table):
    date = datetime.now()
    date = date.strftime('%d/%m/%Y %H:%M')
    pulse_count = int(req['request']['nlu']['tokens'][1])
    user_id_in_yandex = req['session']['user']['user_id']
    user_id = user_table.GetUserData(user_id_in_yandex)[0]
    pulse_table.InsertNewPulseData(user_id, pulse_count, date)
    req = ReturnPulseDetectedMessage(req, pulse_count)
    return req

def ReturnLastStatistic(req, user_table, pulse_table):
    user_id_in_yandex = req['session']['user']['user_id']
    user_id = user_table.GetUserData(user_id_in_yandex)[0]
    pulse_stat = pulse_table.GetLastPulse(user_id)
    res = ReturnUserStat(req, pulse_stat)
    return res