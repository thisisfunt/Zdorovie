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
            'text': """
                        Привет! Ты можешь использовать следующие команды.
                        Пульс {число ударов} - Записать число ударов.
                        Статистика - вывести последние данные.
                        Помощь - вывести это сообщение.
                        Мой Идентификатор - выводит ваш идентификатор.
                        Вы можете передать ваш идентификатор врачу в клинике поддерживающей технологию нашего приложения.
                        Доктор сможет получить подробную информацию о вашем состоянии.
                    """,
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

def ReturnUserIDMessage(req, user_id : int):
    return {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': f'Ваш ID : {user_id}',
            'end_session': False
        }
    }