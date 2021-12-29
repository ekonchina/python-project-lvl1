import random
import sys
import prompt

def welcome_user():
    prompt._prompt_input('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    prompt._prompt_input('Hello, {}!'.format(user_name))
    return user_name


def even_or_not_even():
    user_name = welcome_user()
    expected_answer = ''
    iteration_number = 1
    prompt._prompt_input('Answer "yes" if the number is even, otherwise answer "no".')

    while iteration_number < 4:
        number = random.randint(0, sys.maxsize)

        if number % 2:
            expected_answer = 'no'
        else:
            expected_answer = 'yes'

        prompt._prompt_input('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')

        if answer.__eq__(expected_answer):
            prompt._prompt_input('Correct!\n')
            iteration_number = iteration_number + 1
        else:
            prompt._prompt_input("{} is wrong answer ;(. Correct answer was {}.\nLet's try again, {}!"
                  .format(answer, expected_answer, user_name))
            break
