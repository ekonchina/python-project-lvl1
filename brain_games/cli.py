import prompt


def welcome_user():
    prompt._prompt_input('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    prompt._prompt_input('Hello, {}!'.format(name))
