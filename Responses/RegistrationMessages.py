def ReturnSuccessRegisterMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Ура! Ты успешно зарегестрировался!\nСкажи "Помощь", чтобы вывести информацию о командах',
            'end_session': False
        }
    }