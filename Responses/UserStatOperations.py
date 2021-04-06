from data.PulseRating import pulseStatistic


def ReturnPulseDetectedMessage(req, pulse_count):
    res = {
        'version': req['version'],
        'session': req['session'],
        'response': {
            'text': 'Ваш пульс записан в базу!\n',
            'end_session': False
        }
    }

    if pulseStatistic['min-pulse'] < pulse_count < pulseStatistic['max-pulse']:
        res['response']['text'] += 'У вас все в норме'
    elif pulseStatistic['min-pulse'] - pulseStatistic['space'] < pulse_count < pulseStatistic['max-pulse'] + pulseStatistic['space']:
        res['response']['text'] += 'У вас небольшое отклонение от нормы.'\
                                   ' Это не критично, но желательно вернуть его к норме'
    else:
        res['response']['text'] += 'У вас довольно значительное отклонение'\
                                    'Настоятельно рекомедую привести его внорму, или ,при плохом самучувствии обратиться к специалисту!'
    return res


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

