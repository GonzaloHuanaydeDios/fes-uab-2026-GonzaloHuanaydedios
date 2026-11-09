###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_encaminador = "Router-noreste"
ubicacion = "Sala de servidors"
port = 24
ence = True

print(f"L'encaminador {nom_encaminador} està a {ubicacion}, té {port} ports i el seu estat encès és {ence}.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gbtotal = 30
gbconsumits = 15

gbrestants = gbtotal - gbconsumits
print(f"GB restants: {gbrestants} GB")

gb_consumits = 200
gbrestants = gbtotal - gbconsumits
print(f"Després d'actualitzar, queden: {gbrestants} GB") 

