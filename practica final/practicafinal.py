from os import write
import random


print("\n\t\t--> Welcome to bosco's the Guess My world app <--\n")

juego = {
    'sports':['basketball', 'baseball', 'volleyball', 'football', 'golf', 'tennis', 'rugby'],
    'colors':['blue', 'red', 'yellow', 'white', 'black', 'green'],
    'movies':['it', '', 'avatar', 'jumanji', '300', 'exorcist', 'focus'],
    'fruits':['apple', 'banana', 'orange', 'mango', 'strawberry', 'passionfruit', 'pineapple']
}

keys_juego = list(juego.keys())
active = True

while active:
    categoria_juego = keys_juego[random.randint(0,len(keys_juego)-1)]
    palabra_juego = juego[categoria_juego][random.randint(0,len(juego[categoria_juego])-1)]
    longitud_juego = len(list(palabra_juego))
    palabra_blanco = list()
    for i in range(0, longitud_juego):
        palabra_blanco.append('-')
    print(f'\n Guess the word which belongs to {categoria_juego} category and has {longitud_juego} letters')
    adivinar=""
    adivinar_contador = 0
    while adivinar != palabra_juego:
        palabra_blanco_list = ' '.join(palabra_blanco)
        print(f'\n Word to guess {palabra_blanco_list}')
        adivinar = input('\n make a guess :').lower()
        adivinar_contador +=1
        if adivinar_contador == longitud_juego - 2:
            print(f'\n Too many guesses. correct word is {palabra_juego}. Thank you for playing with us.')
            break

        if adivinar ==  palabra_juego:
            win = print(f'\n\t\t----> You won the game!! You took {adivinar_contador} chances.\n')
            file = open("practicafinal.txt","w")
            str_win = repr(win)
            file.write(f"win = \n{win}\n " + str_win + "\n")
            file.close()
            break
        else:
            print('\n Oops! That\'s a wrong guess. Try Again. ')
            running=True
            while running:
                indice_letras = random.randint(0,longitud_juego-1)
                if palabra_blanco[indice_letras] == '-':
                    palabra_blanco[indice_letras] = palabra_juego[indice_letras]
                    running=False

            continuar_programa = input('\nDo you want to try again? (y/n) : ').lower().strip()
            if continuar_programa.startswith('n'):
                    
                print("\nOk,that word was too hard")
                break
                         

    continuar_programa = input('Do you want to play again ? (y/n) : ').lower().strip()
    if continuar_programa.startswith('n'):
            active = False
            print('\n Goodbye\n\nHave a nice day!')
