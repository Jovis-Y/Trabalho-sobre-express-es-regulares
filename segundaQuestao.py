import re

def colorir(texto, cor):
    return f'\033[{cor}m{texto}\033[0m'

def verificaxy (x,y):
    if (x > 0 and y > 0) :
        if x<=y:
            return (x,y)
        else:
            print("x não pode ser maior que y, usando valores padrões")
            return (1, 3)
    else: 
        print("x e y devem ser positivos, usando valores padrões")
        return (1, 3)

def padraoG(min, max):
    return r'^(M|H){' + str(min) + ',' + str(max) + r'}((h|m){0,2}|(h*m*)*mh{0,2})$'

padroes = {
    'a': r'^(HM|MH)[hm]*(m.*m|h|hh.*m|hh.*hh.*m).*',
    'b': r'^(HM|MH)h*((mh*){2})*mh*$',
    'c': r'^(HM|MH)m(h|m)*h$',
    'd': r'^(HH|MM)(hm|mh)(h|m)*(hm|mh)$',
    'e': r'^(HH|MM)h?(mh)*m?$',
    'f': r'^(HH|MM)(m|h)?(((m+)h?)*)?$',
}

def verificar_familia(padrao, familia):
    if re.match(padrao, familia):
        return True
    return False

def testar_familias(padrao, familias):
    print("padrão: " + padrao)
    for familia in familias:
        if verificar_familia(padrao, familia):
            print(colorir(familia + " é uma família válida", "32"))
        else:
            print(colorir(familia + " é uma família inválida", "31"))