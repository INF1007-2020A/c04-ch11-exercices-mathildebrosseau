"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	def __init__(self, name: str, power: int, min_level: int):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(self, name):
		UNARMED_POWER = 20
		return Weapon("Unarmed", UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level

	def weapon(self, weapon):
		self.weapon = weapon

	def hp(self, hp):
		self.hp = hp

	def compute_damage(self, defender):
		random_percentage = random.randint(85, 101) / 100  # random number between 0.85 and 1.0
		random_16 = random.randint(1, 17)  # random number between 1 and 16
		crit = 1 if random_16 < 16 else 2
		modifier = crit * random_percentage
		dmg = modifier * ((((2 * self.level / 5 + 2) * self.weapon.power * self.attack / defender.defense)
						   / 50) + 2)
		return round(dmg)


def deal_damage(attacker: Character, defender: Character):
	# TODO: Calculer dégâts
	dmg = defender.compute_damage(defender)
	defender.hp = defender.max_hp - dmg
	print(f"{attacker.name} used {attacker.weapon.name}.\n   {defender.name} took {dmg} dmg.")


def run_battle(c1: Character, c2: Character):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	print(f"{c1.name} starts a battle with {c2.name} !")
	rounds_number = 0
	print(attacker.hp)
	attacker.hp = attacker.max_hp
	defender.hp = defender.max_hp

	while attacker.hp > 0 and defender.hp > 0:
		rounds_number += 1
		deal_damage(attacker, defender)
		attacker, defender = defender, attacker

	return rounds_number
