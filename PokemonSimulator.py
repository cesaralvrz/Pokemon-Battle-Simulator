import time
import numpy as np
import sys

# Delay en cada prit
def delay_print(s):
    # Imprimir personaje uno por uno
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creación de Pokémon
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # Guardar variables como atributos
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        # Definir número de barras de vida
        self.bars = 20 


    def fight(self, Pokemon2):
        # Permiso para que dos Pokémon combatan

        # Texto de la pelea
        print("-----POKEMONE BATTLE-----")
        print("Pokemon 1:", self.name)
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print("Pokemon 2:", Pokemon2.name)
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Ventajas de tipo
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Cuando son del mismo tipo
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Cuando el Pokémon2 es superior
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Cuando el Pokémon2 es inferior
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        
        # Bucle while mientras tengan vida cada Pokémon
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Imprimir la vida de cada Pokémon
            print(self.name ,"health:", self.health)
            print(Pokemon2.name ,"health:", Pokemon2.health)

            print("Go", {self.name}, "!")
            for i, x in enumerate(self.moves):
                print(i+1, x)
            index = int(input('Pick a move: '))
            print(self.name ,"used", self.moves[index-1])
            time.sleep(1)
            delay_print(string_1_attack)

            # Determinar cuanto daño hacer
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Añadir barras en plus de defensa
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(self.name ,"health:", self.health)
            print(Pokemon2.name ,"health:", Pokemon2.health)
            time.sleep(.5)

            # Verificar si el Pokémon 'fainted'
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Turno del segundo Pokémon
            print("Go",  Pokemon2.name, "!")
            for i, x in enumerate(Pokemon2.moves):
                print(i+1, x)
            index = int(input('Pick a move: '))
            print(Pokemon2.name ,"used", Pokemon2.moves[index-1])
            time.sleep(1)
            delay_print(string_2_attack)

            # Determinar daño
            self.bars -= Pokemon2.attack
            self.health = ""

            # Añadir barras en plus de defensa
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(self.name ,"health:", self.health)
            print(Pokemon2.name ,"health:", Pokemon2.health)
            time.sleep(.5)

            # Verificar si el Pokémon 'fainted'
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break






if __name__ == '__main__':
    # Creamos cada Pokémon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    Charizard.fight(Blastoise) # Empezar batalla
