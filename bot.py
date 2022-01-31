def space():
    print("""
---
""")


def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input('Your answer: ')
    print('What a great name you have, ' + name + '!')


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input('Your answer: '))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    points = 0

    print("Let's test your knowledge about Denmark.")
    print('''Denmark has land border to only one country! Which country is it?
    1. Sweden
    2. Norway
    3. Finland
    4. Germany''')
    if int(input('Your answer: ')) == 4:
        points += 1
    else:
        print('Wrong! It is Germany. The border is 68 kilometres')
    space()

    print('''What’s the name of famous bridge with 16 km direct link between Denmark and Sweden?
    1. Storstrøm Bridge
    2. The Øresund Bridge
    3. Great Belt''')
    if int(input('Your answer: ')) == 2:
        points += 1
    else:
        print('Wrong! It is The Øresund Bridge')
    space()

    print('''Which famous author especially famous with his fairy was born in Odense?
    1. Hans Christian Andersen
    2. Karl May
    3. Wilhelm Grimm
    4. Oscar Wilde''')
    if int(input('Your answer: ')) == 1:
        points += 1
    else:
        print('Wrong! It is Hans Christian Andersen')
    space()

    print('''Which iconic company was founded in 1932 in Billund??
    1. SAS
    2. Ørsted
    3. LEGO
    4. Carlsberg''')
    if int(input('Your answer: ')) == 3:
        points += 1
    else:
        print('Wrong! It is LEGO. From a wooden toy to impressive models')
    print('You have earned ' + str(points) + ' points!')
    print('Completed!')


def end():
    print('Congratulations, have a nice day!')


greet('Barbara', '2021')  # change it as you need
remind_name()
space()
count()
space()
test()
end()
