# crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado,
# opicional ou obrigatório nas eleições

def voto(a):
    """
    analisa retorna se a pessoa tem a opção, obrigação ou se não tem permissão para votar
    :param a: recebe o ano de nascimento
    :return: retorna qual a permissão para votar dessa pessoa
    """
    from datetime import datetime
    a = datetime.now().year - a
    if 60 > a >= 18:
        return f'com {a} anos, você precisa votar'
    elif 16 > a:
        return f'com {a} anos, você ainda não pode votar'
    else:
        return f'com {a} anos, o voto é opicional'


print(voto(int(input('em que ano você nasceu? '))))
