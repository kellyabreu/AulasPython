# Aula 18 - 03-12-2019

# Ao receber a seguinte lista, faça um metodo que retorne cada um destes itens de forma individual 
# com cabaçalho dizendo em que posição estes itens estão dentro da lista principal:
# Exemplo: 
# ############# posição 0 ##################
# Agua
# mamão
# ############# posição 1 ##################
# banana
# limão

#Regra: Não pode usar a função range e no máximo 2 print()

lista = [
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['skol','kaiser','sol','schin','brahma','itaipava','bavaria'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
          ['rizoto','macarronada','polenta','guizado','dobradinha','revirado','pure'],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
          ['agua','cachoeira','rio','lagoa','sanga','brejo','laguna'],
          ['vento','ciclone','tufão','furacão','brisa','minuano','zefiro'],
          ['carro','moto','vespa','caminhão','sprinter','kombi','fusca'],
          ['calça','camisa','japona','jaqueta','camiseta','bone','regata']
        ]


def lista_iten(lista):
  numero = 0
  for lista_pequena in lista:
    print(f"############# Posição: {numero} ################")
    numero = numero +1
    for abioluz in lista_pequena:
      print(abioluz)
      # for i in abioluz:
      #   print(i)




lista_iten(lista)