import random as rd

grammar = {'S':['SJ PR'],
            'SJ':['A N','N'],
            'PR':['V','V SJ'],
            'A':['voc_a'],
            'N':['voc_n'],
            'V':['voc_v']}

voc_a = ['un', 'una', 'el', 'la']
voc_n = ['gato', 'perro', 'persona']
voc_v = ['camina', 'pasea', 'pide', 'acoge', 'habla']

frase = ['S']

def leng(frase):
    for i in range(len(frase)):
        try:
            item = frase[i]
            opt = rd.choice(grammar[item])
            fraso = opt.split(' ')
            leng(fraso)
        except:
            #frase[i] contiene una palabra, hay que añadirla a frase y terminar
            break
