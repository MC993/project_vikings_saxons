# WAR !!!
from vikingsClasses import War, Viking, Saxon
import random
import time
from colorama import Fore, Style, init
import pygame

# Colorama
init(autoreset=True)

# Pygame mixer
pygame.mixer.init()

# Load sound files
victory_sound = pygame.mixer.Sound("sounds/victory_sound.wav")
death_sound = pygame.mixer.Sound("sounds/death_sound.wav")
viking_attack_sound = pygame.mixer.Sound("sounds/viking_attack_sound.wav")
saxon_attack_sound = pygame.mixer.Sound("sounds/saxon_attack_sound.wav")

soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]
great_war = War()

# Create 5 Vikings
for _ in range(5):  
    great_war.addViking(Viking(random.choice(soldier_names).capitalize(), 100, random.randint(20, 50)))

# Create 5 Saxons
for _ in range(5):  
    great_war.addSaxon(Saxon(100, random.randint(20, 50)))

round = 1
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(Fore.WHITE + f"Round {round}... The battle rages on...\n")

    # Simulate Viking attack
    saxon_damage_before = sum(saxon.health for saxon in great_war.saxonArmy)
    result_viking_attack = great_war.vikingAttack()
    saxon_damage_after = sum(saxon.health for saxon in great_war.saxonArmy)
    saxon_damage_taken = saxon_damage_before - saxon_damage_after

    if "died" in result_viking_attack:
        print(Fore.RED + result_viking_attack)
        death_sound.play()
    elif "received" in result_viking_attack:
        print(Fore.MAGENTA + result_viking_attack)
    else:
        print(Fore.YELLOW + result_viking_attack)

    # Simulate Saxon attack
    viking_damage_before = sum(viking.health for viking in great_war.vikingArmy)
    result_saxon_attack = great_war.saxonAttack()
    viking_damage_after = sum(viking.health for viking in great_war.vikingArmy)
    viking_damage_taken = viking_damage_before - viking_damage_after

    if "died" in result_saxon_attack:
        print(Fore.RED + result_saxon_attack)
        death_sound.play()
    elif "received" in result_saxon_attack:
        print(Fore.MAGENTA + result_saxon_attack)
    else:
        print(Fore.CYAN + result_saxon_attack)

    # Battle Sounds Interval
    if round == 1 or round % 5 == 0:
        if saxon_damage_taken > viking_damage_taken:
            viking_attack_sound.play()
        elif viking_damage_taken > saxon_damage_taken:
            saxon_attack_sound.play()

    # Army status
    print(Fore.CYAN + f"Viking army: {len(great_war.vikingArmy)} warriors" + Fore.WHITE + " | " + 
          Fore.YELLOW + f"Saxon army: {len(great_war.saxonArmy)} warriors\n")

    # Victory message
    final_status = great_war.showStatus()
    if "Vikings have won" in final_status or "Saxons have fought" in final_status:
        pygame.mixer.stop()
        victory_sound.play()
        time.sleep(victory_sound.get_length())
        print(Fore.GREEN + final_status)
    else:
        print(Fore.WHITE + final_status)

    time.sleep(2)
    
    round += 1
