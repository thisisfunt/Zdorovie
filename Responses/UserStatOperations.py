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
    if len(pulse_stat) > 0:
        res['response']['text'] += 'Статистика Пульса:\n'
        pulse_sum = 0
        for string in pulse_stat:
            res['response']['text'] += f'{string[0]} - {string[1]} Ударов \n'
            pulse_sum += string[1]
        mean_pulse = pulse_sum // len(pulse_stat)

        if pulseStatistic['min-pulse'] < mean_pulse < pulseStatistic['max-pulse']:
            res['response']['text'] += 'У вас все в норме'
        elif pulseStatistic['min-pulse'] - pulseStatistic['space'] < mean_pulse < pulseStatistic['max-pulse'] + pulseStatistic['space']:
            res['response']['text'] += 'В последнее время у вас небольшое отклонение'\
                                       ' Это не критично, но желательно вернуть его к норме'
        else:
            res['response']['text'] += 'У вас довольно значительное отклонение'\
                                        'Настоятельно рекомедую привести его внорму, или ,при плохом самучувствии обратиться к специалисту!'

        res['response']['text'] += f'\n Ваш средний пульс равен {mean_pulse}'
    else:
        res['response']['text'] += 'По вам нет статистики.\nЧтобы записать свой пульс в базу данных скажите "Пульс" + число ударов'
    return res

