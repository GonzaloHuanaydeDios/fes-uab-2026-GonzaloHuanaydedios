###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))

if num1 > num2:
    print(f"El nombre {num1} és més gran.")
elif num2 > num1:
    print(f"El nombre {num2} és més gran.")
else:
    print("Tots dos nombres són接 iguals.")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

n1 = float(input("Introdueix el primer nombre: "))
n2 = float(input("Introdueix el segon nombre: "))
op = input("Introdueix l'operació (+, -, *, /): ")

if op == "+":
    print(f"Resultat: {n1 + n2}")
elif op == "-":
    print(f"Resultat: {n1 - n2}")
elif op == "*":
    print(f"Resultat: {n1 * n2}")
elif op == "/":
    if n2 == 0:
        print("Error: No es pot dividir per zero.")
    else:
        print(f"Resultat: {n1 / n2}")
else:
    print("Operació no vàlida.")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any_int = int(input("Introdueix un any: "))

if (any_int % 4 == 0 and any_int % 100 != 0) or (any_int % 400 == 0):
    print(f"L'any {any_int} és de traspàs.")
else:
    print(f"L'any {any_int} no és de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Introdueix la teva edat: "))

if 0 <= edat <= 2:
    print("Nadó")
elif 3 <= edat <= 12:
    print("Infant")
elif 13 <= edat <= 17:
    print("Adolescent")
elif 18 <= edat <= 64:
    print("Adult")
elif edat >= 65:
    print("Persona gran")
else:
    print("Edat no vàlida.")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = float(input("Introdueix el nivell de senyal RSSI (dBm): "))

if rssi >= -50:
    print("Cobertura excel·lent")
elif -67 <= rssi < -50:
    print("Cobertura bona")
elif -75 <= rssi < -67:
    print("Cobertura feble")
else:
    print("Cobertura molt feble")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Introdueix la potència òptica rebuda (dBm): "))

if potencia < -27:
    print("Nivell massa baix")
elif -27 <= potencia <= -8:
    print("Nivell acceptable")
else:
    print("Nivell massa alt")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Introdueix el consum de dades en GB: "))

if consum <= 20:
    print("El consum està dins del límit de 20 GB.")
else:
    addicionals = consum - 20
    print(f"Has superat el límit. Has consumit {addicionals:.2f} GB addicionals.")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("L'indicador LOS està encès? (si/no): ").lower()
internet = input("L'indicador d'Internet està encès? (si/no): ").lower()

if los == "si":
    print("Cal revisar el cable de fibra.")
elif internet == "no":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = float(input("Introdueix el percentatge de bateria del SAI: "))

if bateria < 0 or bateria > 100:
    print("Error: Valor fora del rang del 0% al 100%.")
elif bateria < 20:
    print("Nivell crític")
elif bateria <= 49:
    print("Nivell baix")
else:
    print("Nivell suficient")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0 or perdua < 0 or perdua > 100:
    print("Error: Valors introduïts no vàlids.")
elif latencia <= 30 and perdua <= 1:
    print("Connexió excel·lent")
elif latencia <= 80 and perdua <= 3:
    print("Connexió bona")
elif latencia <= 150 and perdua <= 5:
    print("Connexió acceptable")
else:
    print("Connexió deficient")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = input("Introdueix el tipus de pla (bàsic/plus): ").lower()
consum = float(input("Introdueix el consum mensual en GB: "))

if consum < 0 or pla not in ["bàsic", "basic", "plus"]:
    print("Error: Consum negatiu o tipus de pla desconegut.")
else:
    if pla in ["bàsic", "basic"]:
        cost = 10
        if consum > 10:
            cost += (consum - 10) * 1.50
    else:
        cost = 20
        if consum > 30:
            cost += (consum - 30) * 0.75
    print(f"Cost total del mes: {cost:.2f}€")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

actiu = input("El compte està actiu? (si/no): ").lower()

if actiu != "si":
    print("Accés denegat: el compte està desactivat.")
else:
    contrasenya = input("Introdueix la contrasenya: ")
    if contrasenya != "1234":
        print("Accés denegat: contrasenya incorrecta.")
    else:
        codi = input("Introdueix el codi de doble verificació: ")
        if codi != "9999":
            print("Accés denegat: el codi ha fallat.")
        else:
            print("Accés permès.")

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router_ences = input("El router està encès? (si/no): ").lower()

if router_ences != "si":
    print("Cal encendre el router.")
else:
    los = input("L'indicador LOS està encès? (si/no): ").lower()
    if los == "si":
        print("Cal revisar el cable de fibra.")
    else:
        internet = input("L'indicador d'Internet està encès? (si/no): ").lower()
        if internet != "si":
            print("Cal contactar amb el proveïdor.")
        else:
            print("La connexió funciona correctament.")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.


servei_critic = input("Afecta un servei crític? (si/no): ").lower() == "si"
usuaris = int(input("Introdueix el nombre d'usuaris afectats: "))

if usuaris < 0:
    print("Error: El nombre d'usuaris no pot ser negatiu.")
else:
    alternativa = input("Hi ha connexió alternativa disponible? (si/no): ").lower() == "si"
    
    if (servei_critic and not alternativa) or (usuaris >= 50 and not alternativa):
        print("Prioritat: Crítica")
    elif usuaris >= 10 or servei_critic:
        print("Prioritat: Alta")
    else:
        print("Prioritat: Baixa")