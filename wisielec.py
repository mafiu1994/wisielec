from random import randint
from sys import exit

import wisielec_grafika

# wczytywanie słownika
with open('list_words.txt', mode='r') as f:

    list_words = []
    for line in f:
        list_words.append(line)

wisielec_grafika.ekran_startowy()
print('\n' * 3)
input('                              Wciśnij ENTER')
print('\n' * 30)
# ekran startowy
number_of_word = len(list_words)
name_user = input('Witaj, wpisz swoje imię: \n')
print('Cześć {}, zagrajmy w wisielca.\n'.format(name_user))
print('W dzisiejszym słowniku mamy {} słów.\n'.format(number_of_word))


# list ze słowami, które były już użyte
used_word = set({})

number_of_missed = 0
user_choice = True
play_game = True
while play_game:
    while user_choice:
        #losowanie słowa
        random_word = randint(0, number_of_word - 1)
        # word play - slowo do gry
        word_play = list_words[random_word]
        if word_play in used_word and len(used_word) == len(list_words):
            print('To wszystko na dziś!\nOdgadłeś już wszystki słowa.')
            exit()
        elif word_play not in used_word:
            used_word.add(word_play)
            spell_in_word = len(word_play) -1
            word_list_char = []
            user_word = []
            used_letter = []
            for n in word_play[:-1]:
                word_list_char.append(n)
                user_word.append('_')
            #słowo zamienione na ciąg
            print('Losowanie słowa....')
            print()
            for n in range(0, len(user_word)):
                print(user_word [n], end=' ')
            print()
            while user_choice:
                user_char = input('Podaj litere: ')
                print()
                if user_char in word_list_char:
                    for n in range(0, spell_in_word):
                        if user_char in word_list_char [n]:
                            user_word[n] = user_char
                    if '_' not in user_word:
                        user_choice = False
                        for n in range(0, len(user_word)):
                            print(user_word [n], end=' ')
                        print()
                        wisielec_grafika.wygrana()

                        user_choice = False
                        break

                else:
                    print('Pudło\n')
                    used_letter.append(user_char)
                    used_letter.sort()
                    number_of_missed += 1
                for n in range(0, len(user_word)):
                    print(user_word [n], end=' ')
                print('\n')
                print('Uzyte litery: ')
                for n in range(0, len(used_letter)):
                    print(used_letter[n], end=' ')
                print()
                if number_of_missed == 0:
                    wisielec_grafika.wisielec_0()
                elif number_of_missed == 1:
                    wisielec_grafika.wisielec_1()
                elif number_of_missed == 2:
                    wisielec_grafika.wisielec_2()
                elif number_of_missed == 3:
                    wisielec_grafika.wisielec_3()
                elif number_of_missed == 4:
                    wisielec_grafika.wisielec_4()
                elif number_of_missed == 5:
                    wisielec_grafika.wisielec_5()
                elif number_of_missed == 6:
                    wisielec_grafika.wisielec_6()
                elif number_of_missed == 7:
                    wisielec_grafika.wisielec_7()
                elif number_of_missed == 8:
                    wisielec_grafika.wisielec_8()
                elif number_of_missed == 9:
                    wisielec_grafika.wisielec_9()
                elif number_of_missed == 10:
                    wisielec_grafika.wisielec_10()
                elif number_of_missed == 11:
                    wisielec_grafika.wisielec_11()
                    user_choice = False
                    number_of_missed = 0
                print()
                print('*' * 30)
            input()
            if len(used_word) == len(list_words):
                print('To wszystko na dziś!\nOdgadłeś już wszystki słowa.')
                exit()
        elif word_play in used_word and len(used_word) != len(list_words):
            continue

    number_of_missed = 0
    user_choice = False
    print('Chcesz zagrać jeszcze raz?')
    print('t - tak')
    print('n- nie, koniec na dzis')
    next_play = input()
    if next_play == 't':
        user_choice = True
        continue
    elif next_play == 'n':
        play_game = False
    else:
        print('Zły wybór, wpisz "t" lub "n"')
        user_choice = False



