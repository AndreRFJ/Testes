#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import psycopg2


def ler_tabela_de_csv(nome_ficheiro_csv):
    """
    Requires: o nome de um ficheiro CSV com cabeçalho na primeira linha.
    Ensures: retorna uma tabela no formato de lista de dicionários.
    """
    with open(nome_ficheiro_csv, 'rU') as ficheiro_csv:
        leitor = csv.reader(ficheiro_csv, delimiter=',')
        return [linha for linha in leitor]


#print ler_tabela_de_csv('volei.csv')
lista = ler_tabela_de_csv('volei.csv')
print ''

lista2 = []
for i in range(len(lista)):
	for j in range(1):
		lista2.append(lista[i][j].split(";"))

dict1 = {}

for l2 in lista2:
    dict1[l2[0]] = l2[1:]

for x in dict1:
    print dict1[x]

print json.dumps(dict1)

conn = psycopg2.connect(database = "cenas", user = "andrejorge", password = "", host = "127.0.0.1", port = "5432")

print "Opened database successfully"

cur = conn.cursor()

for x in dict1:
    cur.execute("INSERT INTO players (name,team) VALUES (%s, %s )",(x,dict1[x]));


conn.commit()
print "Records created successfully";
conn.close()


#alteracao branch


