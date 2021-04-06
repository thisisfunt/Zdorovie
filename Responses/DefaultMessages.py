def ReturnFirstHelloMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Привет! Я твой персональный помощник в твоем уходе за здоровьем. Чтобы зарегистрироваться скажите: "Зарегистрироваться" и поочереди назовите свое имя, пол, возраст',
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

def ReturnHelpingMessage(req):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Привет! Ты можешь использовать следующие команды \n\tПульс {число ударов} - Записать число ударов\n\tСтатистика - вывести последние данные\n\tПомощь - вывести это сообщение',
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