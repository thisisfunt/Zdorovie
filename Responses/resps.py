

def ReturnFirstHelloMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Привет! Я твой персональный помошник в твоем уходе за здоровьем. Чтобы зарегестрироваться скажите: "Зарегистрироваться" и поочереди назовите свое имя, пол, возраст',
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

