#coding: utf-8

#1: Portugues
#2: Ingles
#3: Espanhol

COUNTRIES = {
	1: ['Brasil', 'Brasil', 'Brasil'],
	2: ['Japão', 'Japão', 'Japão'],
	3: ['Austrália', 'Austrália', 'Austrália'],
	4: ['Irã', 'Irã', 'Irã'],
	5: ['Coreia do Sul', 'Coreia do Sul', 'Coreia do Sul'],
	6: ['Holanda', 'Holanda', 'Holanda'],
	7: ['Itália', 'Itália', 'Itália'],
	8: ['Argentina', 'Argentina', 'Argentina'],
	9: ['Estados Unidos', 'Estados Unidos', 'Estados Unidos'],
	10: ['Costa Rica', 'Costa Rica', 'Costa Rica'],
	11: ['Alemanha', 'Alemanha', 'Alemanha'],
	12: ['Bélgica', 'Bélgica', 'Bélgica'],
	13: ['Suíça', 'Suíça', 'Suíça'],
	14: ['Colômbia', 'Colômbia', 'Colômbia'],
	15: ['Espanha', 'Espanha', 'Espanha'],
	16: ['Bósnia', 'Bósnia', 'Bósnia'],
	17: ['Rússia', 'Rússia', 'Rússia'],
	18: ['Inglaterra', 'Inglaterra', 'Inglaterra'],
	19: ['Chile', 'Chile', 'Chile'],
	20: ['Equador', 'Equador', 'Equador'],
	21: ['Honduras', 'Honduras', 'Honduras'],
	22: ['Nigéria', 'Nigéria', 'Nigéria'],
	23: ['Camarões', 'Camarões', 'Camarões'],
	24: ['Costa do Marfim', 'Costa do Marfim', 'Costa do Marfim'],
	25: ['Portugal', 'Portugal', 'Portugal'],
	26: ['França', 'França', 'França'],
	27: ['Grécia', 'Grécia', 'Grécia'],
	28: ['Croácia', 'Croácia', 'Croácia'],
	29: ['Argélia', 'Argélia', 'Argélia'],
	30: ['Gana', 'Gana', 'Gana'],
	31: ['México', 'México', 'México'],
	32: ['Uruguai ', 'Uruguai ', 'Uruguai '],
}


CITY_CHOICES = (
	('RJ', 'Rio de Janeiro'),
	('SP', 'São Paulo'),
	('MG', 'Belo Horizonte'),
	('RS', 'Porto Alegre'),
	('DF', 'Brasília'),
	('MT', 'Cuiabá'),
	('PR', 'Curitiba'),
	('CE', 'Fortaleza'),
	('AM', 'Manaus'),
	('RN', 'Natal'),
	('PE', 'Recife'),
	('BA', 'Salvador'),
)


GROUP_CHOICES = (
	('', 'Nao é fase de grupo'),
	('a', 'Grupo A'),
	('b', 'Grupo B'),
	('c', 'Grupo C'),
	('d', 'Grupo D'),
	('e', 'Grupo E'),
	('f', 'Grupo F'),
	('g', 'Grupo G'),
	('h', 'Grupo H'),
)


TYPE_MATCH_CHOICES = (
	(1, 'amistoso', 'Amistoso'),
	(2, 'primeira_fase', 'Primeira Fase'),
	(3, 'oitavas_de_finais', 'Oitavas de Final'),
	(4, 'quartas_de_finais', 'Quartas de Final'),
	(5, 'semi_finais', 'Semi-finais'),
	(6, 'terceiro', 'Terceiro'),
	(7, 'final', 'Final'),
)
