#importe as funções do Modulo de correção

continua = True
gab = False
prov = False

while (continua):
	print ("Entre com a opção desejada:")
	print ("1 - Carregar gabarito")
	print ("2 - Carregar prova")
	print ("3 - Gerar correção")
	print ("4 - Sair")
	resp = input("Opção:")
	resp = int(resp)
	if (resp < 1 or resp > 4):
		print("Entrada Inválida:")
		#moduloCorr.limpaTela()
		continue
	else:
		if (resp == 1):
			if (not gab):
				sGab = moduloCorr.lerGabarito('gab.txt')
				print ("Gabarito lido com sucesso")
				gab = True
				input()
				#limpaTela()
				continue
			else:
				input("Gabarito já foi lido")
				#limpaTela()
				continue
			
		elif (resp == 2):
			#continue implementando..
			#sResp = moduloCorr.lerProva('prova.txt')
			#continue implementando..
			
		elif (resp == 3):
			#continue implementando
			#sRelatorio = moduloCorr.corrigirProva(sGab,sResp)
			#moduloCorr.imprimeResultados(sRelatorio)
			#moduloCorr.escreverRelatorio(sRelatorio)
			#continue implementando..
		else:
			#pergunte se o usuário tem certeza
			continua = False
