from datetime import datetime

#VERIFICAR SE A DATA DE NASCIMENTO É MENOR QUE A DATA ATUAL
def data_menor(data):
    dataAtual = datetime.now()
    dataNascimento = datetime.strptime(data, '%Y-%m-%d')

    if dataNascimento > dataAtual:
        return False
        
    return True