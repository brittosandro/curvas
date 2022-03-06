import re

def extrai_texto():
    '''Essa função é utilizada para extrair do meio dos dados a informação:
     - Current CBMC acceptance ratio:  27.52 % -.
    A variável t denota o texto como string
    '''

    with open('arq_dados.txt') as t:
        arq_t = t.read()

    texto_int = re.compile(r'((\w+)( )(\w+)( )(\w+)( )(\w+):(  )(\d+).(\d+)( )(%))')
    separador = texto_int.findall(arq_t)
    separador1 = [i[0] for i in separador]

    lista_dados = arq_t.split('\n')
    for info in separador1:
        lista_dados.remove(info)

    with open('arq_dados.dat', 'w') as f:
        f.write('\n'.join(lista_dados))

    return f


def extrai_dados_output_eq():

    with open("B0TMC2.in.out") as f:
        arq_inf = f.read()

    separador1 = '*' * 52
    separador2 = 'NMOVE'
    separador3 = 'Density'
    separador4 = 'Averages'

    cabecalho = arq_inf.split(separador1)[1]
    string_dados = arq_inf.split(separador3)[2].split(separador4)[0]

    with open('arq_dados.txt', 'w') as f:
        f.write(string_dados)

    return f

def extrai_dados_output_avr():
    with open('outB0TMC2.avr') as f:
        arq_inf = f.read()

    separador1 = 'NMOVE'
    separador2 = 'cp'

    string_dados = arq_inf.split(separador1)[1].split(separador2)[1]

    with open('arq_dados_avr.txt', 'w') as f:
        f.write(string_dados)

    return f

extrai_dados_output_eq()
extrai_dados_output_avr()
extrai_texto()
