import random
import urllib
from lxml import html, etree

class Sorteio:

    def __init__(self, rd):
        self.rangeDozens = [str(d).zfill(2) for d in range(1, rd + 1)]
        self.percent = 0
        self.teimozinha = 0

    def getPercent(self):
        return ((self.percent) / self.teimozinha) * 100

    def getDozens(self):
        return random.sample(self.rangeDozens, k=6)

    def sorteio(self, Dozens, teimozinha=1):
        for n in range(teimozinha):
            self.teimozinha += 1
            resultado = [d for d in self.getDozens() if d in Dozens]
            self.percent += (len(resultado) / float(len(Dozens)))
            yield resultado

def getDozensSorteadas():
    page = urllib.urlopen("megasena.html").read()
    tree = html.fromstring(page)
    retorno = []
    for tr in tree.xpath('//tr[position() > 1]'):
        dz = tr.xpath('./td[position() > 2 and position() < 9]/text()')
        if dz:
            retorno.append(dz)
    return retorno

loteria = Sorteio(60)

#print loteria.getDozens()
# for d in loteria.sorteio(Dozens=['10','20','30','40','50','60'], teimozinha=100000):
#     if len(d) > 4:
#         print d
# print loteria.getPercent();

for Dozens in getDozensSorteadas():
    dados = loteria.sorteio(Dozens=Dozens, teimozinha=10000)
    for d in dados:
        if len(d) > 4:
            print Dozens
            print d
            print loteria.getPercent()