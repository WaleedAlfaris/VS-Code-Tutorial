from datetime import datetime as dt

from folder_1.getters import get_tail, get_user_age

def main():

    user_birthdate = input('Enter your birthday as MM/DD/YYYY\n')
    today = dt.today()

    happy_birthday, user_age = get_user_age(user_birthdate, today)

    tail = get_tail(user_age)

    if happy_birthday == True:
        print(f"Happy {user_age}{tail} Birthday!\n")
    else:
        print(f'You are {user_age} years old.\n')



if __name__ == '__main__':
    main()
