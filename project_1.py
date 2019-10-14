#!/usr/bin/env python3
""" Projekt #1 - Textovy analyzator """

# Privitani uzivatele
print('=' * 80)
print('Vitejte v textovem analyzatoru!')
print('=' * 80)

# Vyzadani prihlasovaciho jmena a hesla
print('=' * 80)
jmeno = input('Vlozte, prosim, jmeno: ')
heslo = input('Vlozte, prosim, heslo: ')
print('=' * 80)

# Zjisteni spravnosti jmena a hesla
registrovani = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
jmena = registrovani.keys()
if jmeno in jmena:
    if registrovani[jmeno] == heslo:
        print('Pristup udelen.')
    else:
        print('Nespravne heslo!')
        exit()
else:
    print('Nespravne uzivatelske jmeno!')
    exit ()
print('=' * 80)

# Vybrani textu
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
vyber = int(input('''
Vyberte si cislem 1, 2 nebo 3 z nasledujicich textu:

1 - Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.

2 - At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.

3 - The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.
Vaše volba:
'''))
vybrany_text = TEXTS[vyber - 1]
print('=' * 80)

# Ziskani statistik
vybrane = vybrany_text.split()
pocet_slov = len(vybrane)
slovo = []
Titulky = 0
KAPITALKY = 0
mala = 0
cisla = 0
soucet = float()
pocitadlo = {}
while vybrane != []:
    slovo = vybrane.pop()
    slovo = slovo.strip('.,:/;')
    delka = len(slovo)
    pocitadlo[delka] = pocitadlo.get(delka, 0) + 1
    if slovo.istitle():
        Titulky = Titulky + 1
    elif slovo.isupper():
        KAPITALKY = KAPITALKY + 1
    elif slovo.islower():
        mala = mala + 1
    elif slovo.isnumeric():
        cisla = cisla + 1
        soucet = soucet + int(slovo)
print(f'Pocet_slov je {pocet_slov}.')
print(f'Pocet slov zacinajicich velkymi pismeny je {Titulky}.')
print(f'Pocet slov psanych velkymi pismeny je {KAPITALKY}.')
print(f'Pocet slov psanych malymi pismeny je {mala}.')
print(f'Pocet cisel je {cisla}.')
print('=' * 80)

# Sloupcovy graf
i = 0
serazene_pocitadlo = sorted(pocitadlo)
while i < len(serazene_pocitadlo):
    delka = serazene_pocitadlo[i]
    opakovani = pocitadlo[delka]
    if len(str(delka)) == 1:
        delka_slova = ' ' + str(delka)
    else:
        delka_slova = str(delka)
    print(f' {delka_slova} - {"*" * opakovani} {opakovani}')
    i = i + 1
print('=' * 80)
print(f'Pokud secteme vsechna cisla v textu dostaneme cislo: {soucet}.')


