import csv
import datetime
import time

import pygame
pygame.init()

from pygame.mixer import Sound
audio = pygame.mixer.Sound('som.ogg')



while True:

	dataAtual = datetime.datetime.now()
	x = dataAtual.strftime("%H:%M")


	with open('dadosAgenda.csv', encoding='utf-8') as referencia:
		tabela = csv.reader(referencia, delimiter=',')
		next(tabela)
		for i in tabela:
			
			dataHoje = dataAtual.strftime("%X")
			dia = dataAtual.strftime("%B")
			horario = i[0]
			descricao = i[1]
			
			if horario == x:

				print(f"{dataHoje} - {dia}, São {x} Descrição: {descricao}")
				audio.play()
				time.sleep(60)
				
	

    	

    		

    	
    		


