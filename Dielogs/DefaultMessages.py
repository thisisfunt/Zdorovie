from Responses.DefaultMessages import *


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