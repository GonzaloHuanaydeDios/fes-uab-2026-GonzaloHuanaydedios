###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

print("\nExercici 1:")
i = 10
while i >= 1:
    print(i)
    i -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

print("\nExercici 2:")
num = 2
suma_parells = 0
while num <= 20:
    suma_parells += num
    num += 2
print("Suma dels parells entre 1 i 20:", suma_parells)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nExercici 3:")
numero = int(input("Introdueix un número enter positiu: "))
factorial = 1
comptador = 1
while comptador <= numero:
  factorial *= comptador
  comptador += 1
print(f"El factorial de {numero} és: {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
print("\nExercici 4:")
contrasenya = input("Introdueix una contrasenya: ")
while len(contrasenya) < 8:
    print("Massa curta (mínim 8 caràcters).")
    contrasenya = input("Torna a introduir la contrasenya: ")
print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
print("\nExercici 5:")
taula_num = int(input("Introdueix un número per veure la taula: "))
k = 1
while k <= 10:
    print(f"{taula_num} x {k} = {taula_num * k}")
    k += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
print("\nExercici 6:")
N = int(input("Introdueix un número enter positiu N: "))
candidat = 2
print(f"Números primers fins a {N}:")
while candidat <= N:
    divisor = 2
    es_primer = True
    while divisor * divisor <= candidat:
        if candidat % divisor == 0:
            es_primer = False
            break
        divisor += 1
    if es_primer:
        print(candidat)
    candidat += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
print("\nExercici 7:")
suma = 0
numero = int(input("Introdueix un número enter (0 per acabar): "))

while numero != 0:
  suma += numero
  numero = int(input("Introdueix un altre número enter (0 per acabar): "))

print(f"La suma total és: {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
print("\nExercici 8:")
numero_xifres = int(input("Introdueix un número enter positiu: "))
xifres = 0
aux = numero_xifres
if aux == 0:
    xifres = 1
else:
    while aux > 0:
        xifres += 1
        aux //= 10
print(f"El número {numero_xifres} té {xifres} xifres.")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
print("\nExercici 9:")
termes = int(input("Quants termes de Fibonacci vols veure?: "))
a, b = 0, 1
comptador_fibo = 0
while comptador_fibo < termes:
    print(a, end=" ")
    a, b = b, a + b
    comptador_fibo += 1
print()

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
print("\nExercici 10:")
numero_secret = 7
intent = int(input("Endevina el número secret: "))

while intent != numero_secret:
    if intent < numero_secret:
        print("El número secret és més gran.")
    else:
        print("El número secret és més petit.")
    intent = int(input("Torna-ho a provar: "))

print("Correcte")