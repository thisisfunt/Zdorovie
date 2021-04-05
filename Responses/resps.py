

def ReturnFirstHelloMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Привет! Я твой персональный помошник в твоем уходе за здоровьем. Чтобы зарегестрироваться скажите: "Зарегистрироваться" и поочереди назовите свое имя, пол, возраст',
            'end_session': False
        }
    }

def ReturnHelpingMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Привет! Ты можешь использовать следующие команды \n\tПульс {число ударов} - Записать число ударов\n\tПомощь - вывести это сообщение',
            'end_session': False
        }
    }

def ReturnSuccessRegisterMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Ура! Ты успешно зарегестрировался',
            'end_session': False
        }
    }

def ReturnHelloMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Привет!',
            'end_session': False
        }
    }

def ReturnDontUnderstandMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Я ТВАЯ НЕ ПОНИМАТЬ!',
            'end_session': False
        }
    }

def ReturnPulseDetectedMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Ваш пульс записан в базу',
            'end_session': False
        }
    }

def ReturnUserStat(req, pulse_stat):
    res = {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': '',
            'end_session': False
        }
    }
    res['response']['text'] += 'Статистика Пульса:\n'
    for string in pulse_stat:
        res['response']['text'] += f'{string[0]} - {string[1]} Ударов \n'
    return res