import os
import sys

#atenção! o comando 'pass' que está nas funções não implementadas serve para que o programa funcione sem tudo pronto. Ele basicamente insere uma instrução que não faz nada, apenas manda o programa seguir em frente, pois a função precisa ter um corpo.
#quando for implementar as funções, remova os 'pass' (ensinando o padre a rezar missa)

def limpaTela():
	if sys.platform() == "linux2":
		os.system("clear")
	else:
		os.system("cls")
	
def lerGabarito(nome_arq):
	#Não esqueça de fazer o tratamento de erros!
	gab = open(nome_arq,'r')
	sGab = gab.readlines()

def lerProva(nome_arq):pass
	#implementar
	#recebe uma string com nome do arquivo lê o arquivo e retorna a lista de strings com as respostas da prova

def corrigirProva (sGab,sProva):pass
	#implementar
	#recebe duas listas de strings
	#retorna uma string de saída
	#corrija a prova
	#string de saída deve conter em cada linha o número da questão e "correto" se estiver correto ou  "incorreto" caso contrário
	
def imprimeResultados(sRelatorio):pass
	#implementar
	#recebe a string de correção
	#imprime em tela quantas respostas estão corretas e quantas estão erradas

def escreverRelatorio(sRelatorio):pass
	#implementar
	#recebe a string de correção
	#escreva a string no arquivo "correcao.txt"




