###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets = int(input("Quants paquets has rebut? "))
total = paquets + 1200
print(f"El total de paquets és: {total}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_mbps = float(input("Introdueix la velocitat en Mbps: "))
velocitat_mb_s = velocitat_mbps / 8
print(f"La velocitat equivalent en MB/s és: {velocitat_mb_s}")