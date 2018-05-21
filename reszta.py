zakupy = ['mleko', 'ser', 'mieso']

monety = {5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0}

zakupy = 23.50

banknot = 50

reszta = banknot - zakupy

reszta_slownie = "Reszta składa się z "

for moneta in monety.keys():
    il_monet = reszta // moneta
    monety[moneta] = il_monet
    reszta -= (il_monet * moneta)
    reszta_slownie += str(il_monet) + " monet " + str(moneta) + "zł, "

print(reszta_slownie)