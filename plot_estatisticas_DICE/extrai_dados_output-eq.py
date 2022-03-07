import re


def extrai_texto():
    '''
    Essa função é utilizada para extrair do arq_dados.txt a informação:
    - Current CBMC acceptance ratio:  27.52 % -. Observando que a porcentagem
    sempre muda ao longo do arquivo.
    '''

    with open('arq_dados.txt') as t:
        arq_t = t.read()

    frase = re.compile(r'((\w+)( )(\w+)( )(\w+)( )(\w+):(  )(\d+).(\d+)( )(%))')
    separador = frase.findall(arq_t)
    separador1 = [i[0] for i in separador]

    lista_dados = arq_t.split('\n')
    for info in separador1:
        lista_dados.remove(info)

    with open('arq_dados.dat', 'w') as f:
        f.write('\n'.join(lista_dados))

    return f


def extrai_dados_output_eq():
    '''
    Essa função recebe o arquivo de output de uma simulação de equilíbrio,
    retira os dados de cabeçalho e cria um novo arquivo chamado de
    arq_dados.txt.
    '''

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
    '''
    Essa função extrai os dados do arquivo de médias *.avr de saidas
    em uma simulação DICE.
    '''

    with open('outB0TMC2.avr') as f:
        arq_inf = f.read()

    separador1 = 'NMOVE'
    separador2 = 'cv_intra'

    string_dados = arq_inf.split(separador1)[1].split(separador2)[1]

    with open('arq_dados_avr.txt', 'w') as f:
        f.write(string_dados)

    return f

if __name__ == "__main__":

    extrai_dados_output_eq()
    extrai_dados_output_avr()
    extrai_texto()
