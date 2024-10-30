def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
   if y !=0:
    return x / y
   else:
       return "Erro: Divisão por zero não é permitida"
       
# Função para armazenar as últimas 5 operações
def armazenar_operacao(operacao, historico):
    if len(historico) >=5:
        historico.pop(0) #Remove a operação mais antiga
    historico.append(operacao) #Adiciona a nova operação

