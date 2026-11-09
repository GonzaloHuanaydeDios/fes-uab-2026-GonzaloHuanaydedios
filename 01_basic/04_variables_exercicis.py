###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_encaminador = "Router-noreste"
ubicacio = "Sala de servidors"
ports = 24
ences = True

print(f"L'encaminador {nom_encaminador} està a {ubicacio}, té {ports} ports i el seu estat encès és {ences}.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_totals = 30
gb_consumits = 15

gb_restants = gb_totals - gb_consumits
print(f"GB restants: {gb_restants} GB")

gb_consumits = 200
gb_restants = gb_totals - gb_consumits
print(f"Després d'actualitzar, queden: {gb_restants} GB")