from Responses.RegistrationMessages import *


def RegisterProcedure(req, users_table):
    context = req['request']['nlu']['tokens']
    users_table.InsertNewUser(req['session']['user']['user_id'], req['request']['nlu']['tokens'][1],
                        req['request']['nlu']['tokens'][2], int(req['request']['nlu']['tokens'][3]))
    res = ReturnSuccessRegisterMessage(req)
    return res