from abc import ABC
import random

class Character(ABC):
    def __init__(self, name, health, attack, defense, ultima) -> None:
        self.health = health
        self.name = name
        self.attack = attack
        self.defense = defense
        self.ultima = ultima

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} byl poražen!")

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.take_damage(damage)
            print(f"{self.name} útočí a ubírá {damage} hápek.")
        else:
            print(f"{self.name} nemůžeš nic.")
    

    def display_stats(self):
        
        print(f"{self.name} - Hápéčka: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Ultima: {self.ultima}")

class Hero(Character):
    def __init__(self, name, health, attack, defense, ultima):
        super().__init__(name, health, attack, defense, ultima)

    def use_ultima(self):
            self.health += 20
            print(f"{self.name} využívá speciální schopnost a přidává 20 životů.")
    def attack_ultima(self, enemy):
        ultimatka = self.ultima - enemy.defense
        if ultimatka > 0:
            enemy.take_damage(ultimatka)
            print(f"{self.name} útočí a ubírá {ultimatka} hápek.")

class Enemak(Character):
    def pc_attack(self):
        attacks = ["normal_attack", "ultimatka"]
        return random.choice(attacks)

    def do_attack(self, hero):
        chosen_attack = self.pc_attack()
        if chosen_attack == "normal_attack":
            damage = self.attack
            hero.take_damage(damage)
            print(f"{self.name} používá normální útok a způsobuje {damage} poškození.")
            print("")
        elif chosen_attack == "ultimatka":
            ultimatka = self.ultima
            hero.take_damage(ultimatka)
            print(f"{self.name} používá ultimatku. a ubírá {ultimatka} hp")
            print("")


choices = ["Brumbál", "Haagrid", "Ginger"]
pocitac = random.choice(choices)

if pocitac == "Brumbál":
    pocitac = Enemak("Brumbál", 90, 10, 15, 40)
elif pocitac == "Haagrid":
    pocitac = Enemak("Haagrid", 60, 19, 8, 30)
elif pocitac == "Ginger":
    pocitac = Enemak("Ginger", 110, 15, 0, 20)


print("Alfons, Agrag, Bengos")
uzivatel = input("Vyber hrdinu, kterého chceš: ")

if uzivatel == "Alfons":
    uzivatel = Hero("Alfons", 80, 20, 10, 35)
elif uzivatel == "Agrag":
    uzivatel = Hero("Agrag", 100, 10, 5, 15)
elif uzivatel == "Bengos":
    uzivatel = Hero("Bengos", 60, 35, 20, 60)
else:
    print("Něco jsi zadal špatně")


while uzivatel.health > 0 and pocitac.health > 0:
    uzivatel.display_stats()
    pocitac.display_stats()

    action = input("Zadejte akci buď heal nebo attack ultima: ").lower()

    if action == "attack":
        print("")
        uzivatel.attack_enemy(pocitac)
    elif action == "heal":
        print("")
        uzivatel.use_ultima()
    elif action == "ultima":
        print("")
        uzivatel.attack_ultima(pocitac)
    else:
        print("Neplatná akce. Zadejte znovu.")

    if pocitac.health > 0:
        pocitac.do_attack(uzivatel)

print("Hra skončila.")