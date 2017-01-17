#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-

import sqlite3
import urllib
from lxml import html, etree
from contextlib import contextmanager

class Loteria(object):

    def __init__(self, sourcefile, db='loteria.db'):
        self.db = db
        self.db = sourcefile

    def _open(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = conn.cursor()

    @contextmanager
    def execSql(self, query):
        self._open()
        self.cursor.execute(query)
        yield cursor.fetchall()
        self.conn.close()

    def execSqlu(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()

    def _importdata(self):
        pass

    def _buildschema(self):

        query = """
            CREATE TABLE IF NOT EXISTS megasena (
                Concurso INTEGER,
                Data_Sorteio DATE NOT NULL,
                Dezena_1 VARCHAR(2) NOT NULL,
                Dezena_2 VARCHAR(2) NOT NULL,
                Dezena_3 VARCHAR(2) NOT NULL,
                Dezena_4 VARCHAR(2) NOT NULL,
                Dezena_5 VARCHAR(2) NOT NULL,
                Dezena_6 VARCHAR(2) NOT NULL,
                Arrecadacao_Total TEXT,
                Ganhadores_Sena TEXT,
                Cidade TEXT,
                UF VARCHAR(2) NOT NULL,
                Rateio_Sena TEXT,
                Ganhadores_Quina TEXT,
                Rateio_Quina TEXT,
                Ganhadores_Quadra TEXT,
                Rateio_Quadra TEXT,
                Acumulado TEXT,
                Valor_Acumulado TEXT,
                Estimativa_Premio TEXT,
                Acumulado_Mega_da_Virada TEXT
            );
        """

        self.execSqlu(query)

page = urllib.urlopen("megasena.html").read()
tree = html.fromstring(page)
finaldata = []

head = [t.text_content() for t in tree.xpath('//tr[1]/th')]

for tr in tree.xpath('//tr[position() > 1]'):
    print tr.xpath('./td[position() > 2 and position() < 9]/text()')