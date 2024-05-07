#Importamos modulo de elecciones aleatorias
import random

#Listas de jugadoras y numeros
jugadoras_arg=[
("Agustina Albertario", 19),
("Cristina Cosentino", 13),
("Julieta Jankunas", 28),
("Valentina Marcucci", 31),
("Rocío Sánchez Moccia", 17),
("Victoria Sauze Valdez", 18),
("Eugenia Trinchinetti", 22),
("Valentina Costa Biondi", 32),
("Agustina Gorzelany", 3),
("María José Granatto", 15),
("Sofia Toccalino", 2),
("Agostina Alonso", 5),
("Valentina Raposo", 4),
("Clara Barberi", 14),
("Delfina Thome", 4),
("Sofía Cairo", 8),
("María Pilar Campoy", 23)
]

jugadoras_aus=[
("Ashlee Wells", 5),
("Jocelyn Bartram", 19),
("Rachel Lynch", 27),
("Sophie Taylor", 1),
("Karri McMahon", 11),
("Edwina Bone", 13),
("Kaitlin Nobbs", 15),
("Madison Fitzpatrick", 10),
("Amy Lawton", 4),
("Karri Somerville", 20),
("Kate Jenner", 22),
("Georgia Wilson", 8),
("Lily Brazel", 9),
("Greta Hayes", 12),
("Stephanie Kershaw", 14),
("Jane Claxton", 18),
]

#funcion para generar pases
def generar_pases(equipo,jugadoras,minuto):
    jugador = random.choice(jugadoras) #utilizamos el modulo para seleccionar una jugadora al azar
    resultado = random.choice([0,1]) #el modulo elige si el pase se concreta (1) o no (0)
    return f"{equipo};{jugador[1]};{jugador[0]};{resultado};{minuto}"

#generamos los pases en un documento .txt en modo escritura (w)
with open("pases.txt", "w") as file:
    for _ in range(50000): #cantidad de registros maximos 
        minutos = random.randint(1,90) #modulo selecciona un minuto aleatorio 1>=x<=90
        if random.choice([True,False]): #modulo divide si el pase fue Argentina o Australia
            file.write(generar_pases("Argentina", jugadoras_arg, minutos) + "\n")
        else:
            file.write(generar_pases("Australia", jugadoras_aus, minutos) + "\n")