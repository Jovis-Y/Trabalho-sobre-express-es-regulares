from re import match

def colorir(texto, cor):
    return f'\033[{cor}m{texto}\033[0m'

def validarNome(nome):
    pattern = r'^[A-Z][a-z]+(?: [A-Z][a-z]+)? [A-Z][a-z]+$'
    return match(pattern, nome)

def testarNomes(nomes):
    print("padrão: ^[A-Z][a-z]+(?: [A-Z][a-z]+)? [A-Z][a-z]+$")
    for nome in nomes:
        print(f'{nome}: {colorir("Válido", "32") if validarNome(nome) else colorir("Inválido", "31")}')

def validarEmail(email):
    pattern = r'^[a-z]+@[a-z]+(.com.br|.br)$'
    return match(pattern, email)

def testarEmails(emails):
    print("padrão: ^[a-z]+@[a-z]+[.com.br|.br]$")
    for email in emails:
        print(f'{email}: {colorir("Válido", "32") if validarEmail(email) else colorir("Inválido", "31")}')

def validarSenhas(senha):
    pattern = r'^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$'
    return match(pattern, senha)

def testarSenhas(senhas):
    print("padrão: ^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$")
    for senha in senhas:
        print(f'{senha}: {colorir("Válido", "32") if validarSenhas(senha) else colorir("Inválido", "31")}')

def validarCPF(cpf):
    pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return match(pattern, cpf)

def testarCPFs(cpfs):
    print("padrão: ^\d{3}\.\d{3}\.\d{3}-\d{2}$")
    for cpf in cpfs:
        print(f'{cpf}: {colorir("Válido", "32") if validarCPF(cpf) else colorir("Inválido", "31")}')


def validarTelefone(telefone):
    pattern = r'^((\(\d\d\) 9\d{4}-?\d{4})|(\d\d 9\d{8}))$'
    return match(pattern, telefone)

def testarTelefones(telefones):
    print("padrão: ^((\(\d\d\) 9\d{4}-?\d{4})|(\d\d 9\d{8}))$")
    for telefone in telefones:
        print(f'{telefone}: {colorir("Válido", "32") if validarTelefone(telefone) else colorir("Inválido", "31")}')

def validarTimestamp(timestamp):
    pattern = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$'
    return match(pattern, timestamp)

def testarTimestamps(timestamps):
    print("padrão: ^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$")
    for timestamp in timestamps:
        print(f'{timestamp}: {colorir("Válido", "32") if validarTimestamp(timestamp) else colorir("Inválido", "31")}')

def validarNumero(numero):
    pattern = r'^(\+|-)?\d+(\.\d+)?$'
    return match(pattern, numero)

def testarNumeros(numeros):
    print("padrão: ^(\+|-)?\d+(\.\d+)?$")
    for numero in numeros:
        print(f'{numero}: {colorir("Válido", "32") if validarNumero(numero) else colorir("Inválido", "31")}')
