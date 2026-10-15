
###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
nom_encaminador=" Router"
ubicacio="Planta principal"
nombre_ports= 4
enca_encès=True

# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
print(f"El encaminador {nom_encaminador} està a {ubicacio} i té {nombre_ports} ports.")
print(f"Està encès? {enca_encès}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
dades_incloses_gb= 10
dades_consumides_gb= 3
dades_restants_gb= dades_incloses_gb - dades_consumides_gb
print(f"Queden {dades_restants_gb} GB de dades.")

# Actualitza el consum amb un valor nou i torna a calcular quants GB queden.
dades_consumides_gb= 5
dades_restants_gb= dades_incloses_gb - dades_consumides_gb
print(f"Queden {dades_restants_gb} GB de dades.")