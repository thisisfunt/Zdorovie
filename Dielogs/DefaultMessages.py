from Responses.DefaultMessages import *
from Models.db import Users

def FirstHelloProcedure(req):
    res = ReturnFirstHelloMessage(req)
    return res

def HelloProcedure(req):
    res = ReturnHelloMessage(req)
    return res

def DontUnderstandProcedure(req):
    res = ReturnDontUnderstandMessage(req)
    return res

def OuputHelpingMessage(req):
    res = ReturnHelpingMessage(req)
    return res

def UserIDMessage(req):
    res = ReturnUserIDMessage(req, Users().GetUserData(req['session']['user']['user_id'])[0])
    return res