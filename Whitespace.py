#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def transform():
    crypt = []
    print('Mit dieser Funktion können Sie die Whitespace - trafo eines Zeichens ausgeben lassen!')
    char = raw_input('Geben Sie das Zeichen ein!\n')
    char = ord(char)
    print('ASCII response '+ str(char))
    while char != 1:
        if char % 2 == 1:
            crypt = crypt + [' Tab ']
        else:
            crypt = crypt + [' Space ']

        char //= 2

    crypt = crypt + [' Tab ']
    print(crypt[::-1])
    print('\n\n\n')
    pass
        
def getAscii():
    print('Mit dieser Funktion können Sie die ASCII Nummer eines Zeichens ausgeben lassen!')
    char = raw_input('Geben Sie das Zeichen ein!\n')
    char = ord(char)
    print('ASCII response: '+ str(char))
    print('\n\n\n')
    pass

def getSign():
    print('Mit dieser Funktion können Sie das Zeichen zur ASCII Nummer ausgeben lassen!')
    char = raw_input('Geben Sie das ASCII - Zeichen ein!\n')
    char = unichr(int(char))
    print('Zeichen: ' + str(char))
    print('\n\n\n')
    pass
def main():
    auswahl = True

    while auswahl is True:
        print('Was wollen Sie durchführen?')
        print('\t1. Zahl in Anweisung umwandeln..........1')
        print('\t2. ASCII Code zu Zeichen................2')
        print('\t3. Zeichen zu ASCII Code................3')
        print('\t4. Programm beenden.....................4')

        num = input('Geben sie ihre Auswahl ein!\n')

        if num == 1:
            transform()

        elif num == 2:
            getAscii()

        elif num == 3:
            getSign()

        elif num == 4:
            auswahl = False

        else:
            print('Keine Aktion gewählt!')

        num = raw_input('Wollen sie eine weitere Aktion ausführen? y/n \n')

        if ord(str.lower(num)) == 121:
            auswahl = True
        else:
            auswahl = False
            print('Das Programm wird nun beendet')
    
if __name__ =='__main__':
    main()

    

