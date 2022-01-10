def get_tail(user_age):
    age_tails_dict = {
        'th': ['0', '4', '5', '6', '7', '8', '9'],
        'st': ['1'],
        'nd': ['2'],
        'rd': ['3']
    }

    if 1 <= user_age <= 19:
        tail = 'th'
    else:
        for age_tail in age_tails_dict.items():
            if str(user_age)[-1] in age_tail[1]:
                tail = age_tail[0]
    return tail

def get_user_age(user_birthdate, today):
    happy_birthday = False
    user_birthdate = dt.strptime(user_birthdate, '%m/%d/%Y')
    user_age = (today.year - user_birthdate.year) - 1
    if today.month > user_birthdate.month:
        user_age += 1
    if user_birthdate.month == today.month:
        if user_birthdate.day == today.day:
            happy_birthday = True
            user_age += 1
        if user_birthdate.day > today.day:
            user_age += 1
    return happy_birthday,user_age