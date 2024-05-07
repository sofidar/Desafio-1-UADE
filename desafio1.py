import random

jugadoras_arg=[
    ("Agustina Albertario", 19), ("Cristina Cosentino", 13), ("Julieta Jankunas", 28),
    ("Valentina Marcucci", 31), ("Rocío Sánchez Moccia", 17), ("Victoria Sauze Valdez", 18),
    ("Eugenia Trinchinetti", 22), ("Valentina Costa Biondi", 32), ("Agustina Gorzelany", 3),
    ("María José Granatto", 15), ("Sofia Toccalino", 2), ("Agostina Alonso", 5),
    ("Valentina Raposo", 4), ("Clara Barberi", 14), ("Delfina Thome", 4), ("Sofía Cairo", 8),
    ("María Pilar Campoy", 23)
]

jugadoras_aus=[
    ("Ashlee Wells", 5), ("Jocelyn Bartram", 19), ("Rachel Lynch", 27), ("Sophie Taylor", 1),
    ("Karri McMahon", 11), ("Edwina Bone", 13), ("Kaitlin Nobbs", 15), ("Madison Fitzpatrick", 10),
    ("Amy Lawton", 4), ("Karri Somerville", 20), ("Kate Jenner", 22), ("Georgia Wilson", 8),
    ("Lily Brazel", 9), ("Greta Hayes", 12), ("Stephanie Kershaw", 14), ("Jane Claxton", 18),
]


def generar_pases(jugadoras_arg, jugadoras_aus):
    pases = []
    for _ in range(50000):
        equipo = random.choice(["Argentina", "Australia"])
        jugadoras = jugadoras_arg if equipo == "Argentina" else jugadoras_aus
        jugador = random.choice(jugadoras)
        minutos = random.randint(1, 90)
        resultado = random.choice([0, 1])
        pases.append(f"{equipo};{jugador[1]};{jugador[0]};{resultado};{minutos}\n")
    return pases

pases = generar_pases(jugadoras_arg, jugadoras_aus)

with open("pases.txt", "w") as file:
    file.writelines(pases)
