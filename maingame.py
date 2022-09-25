import time
import random
import colorama 
from colorama import Fore

class Slime:
	def __init__(self, name, size, color, hunger, thirst, type, hp, lvl, xp, dmg):
		self.name = name
		self.size = size
		self.color = color
		self.hunger = hunger
		self.thirst = thirst
		self.type = type
		self.hp = hp
		self.lvl = lvl
		self.xp = xp
		self.dmg = dmg
	def lifeprocesses(self):
			self.hunger -= 1
			self.thirst -= 1
			print(f"-> Hunger: {self.hunger}\n-> Thirst: {self.thirst}")
			time.sleep(5)
				
	def feedslime(self):
			if self.hunger < 100 - 10:
				self.hunger += 10
			elif self.hunger > 100 - 10:
				self.hunger = 0
				self.hunger +=100
		
					
			
	def drinkslime(self):
		if self.thirst < 100 - 10:
			self.thirst += 10
		elif self.thirst > 100 - 10:
				self.thirst = 0
				self.thirst += 100
	
class Monster:
	def __init__(self, look, hp):
		self.look = look
		self.hp = hp
		
class Rat(Monster):
	def ratattack(self, target):
		target.hp -= 1

monsterlist = ["Rat"]
def welcome():
	print(f"☆ Welcome to Slime Sim!\n☆Your health and thirst are at 100.\n☆Every 10 seconds lowers your hunger and thirst levels.\n☆Consistently feed {slime1.name} so it doesn't die! ") 	
def start_game():
    if len(slime1.name) >= 1:
        welcome()
    else: 
    	print("》Please input a name.")
def viewstats():
	global attrpoints
	print(f"""
	「Name: {slime1.name}, level: {slime1.lvl} XP: {slime1.xp}/{xpcap}, Points: {attrpoints}」														
	""")
	print("☆ 1: Upgrade DMG, 2: Upgrade HP, 3: Close")
	options = input("☆ What would you like to do?: ")
	if options == "1":
		if attrpoints > 0:
			attrpoints -= 1
			slime1.dmg += 1
		else:
			print("☆ Not enough points.")
			pass
	elif options == "2":
		if attrpoints > 0:
			attrpoints -= 1
			slime1.hp += 1
		else:
			print("☆ Not enough points.")
	elif options == "3":
		pass
def next_action():
	print("☆ What is your next action?\nEat, Drink, View Stats,  Skip?")
	nextaction = input()
	if nextaction == "Eat":
		slime1.feedslime()
		print(f"》{slime1.name}: Yum! Fed.")
	elif nextaction == "Drink":
		slime1.drinkslime()
		print(f"》{slime1.name}: Ahh... Drank.")
	elif nextaction == "View Stats":
		viewstats()
	elif nextaction == "Skip":
		pass
		print("》Skipped")
	time.sleep(5)
	
	

monsterlist = [Rat]
monster = {Rat: r"""

              ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒              
      ░░░░░░        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████        
  ░░░░▒▒                ▒▒▒▒▒▒████              ▒▒▒▒  
░░▒▒▒▒▒▒░░░░░░░░░░░░    ▒▒██▒▒          ░░▒▒▒▒▒▒▒▒▒▒▒▒
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▓▓▒▒▒▒    ██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒██
  ▒▒▒▒▒▒▒▒              ▒▒▒▒▒▒░░              ▒▒▓▓▓▓  
      ▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒        ██████      
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
                          ██                          
                          ██                          
                          ██                          
              ▓▓▓▓  ▓▓▓▓  ██                          
            ██░░▒▒██░░▒▒████                          
            ████████▒▒▒▒████                          
          ████░░░░░░▒▒▒▒░░██▓▓                        
        ██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒░░██                      
      ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                    
      ████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                  
                  ▓▓▒▒▒▒▒▒██▒▒██████                  
                  ██████████▒▒██████                  
                ████████████▒▒████▒▒██                
              ▓▓░░██▒▒▒▒██░░▒▒██▒▒▒▒██                
              ██▒▒██▒▒▒▒██▒▒██▒▒▒▒▒▒██                
                ████░░▒▒▒▒██▒▒▒▒░░▒▒██                
                ██░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██                
                ██░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██                
                  ░░▒▒▒▒▒▒▓▓▓▓░░▒▒▒▒██                
                  ▒▒████  ▒▒██▓▓████                  
                  ▒▒██    ▒▒██  ▒▒██                  
                  ████    ▒▒██  ▓▓██                  
                  ░░░░    ▒▒██  ░░░░                  
                          ▒▒██                        
                          ▒▒██                        
                          ▒▒██                        
                        ░░▓▓                          
                        ▒▒██                          
                        ▒▒██                          
                        ▒▒██                          
                        ▒▒██                          
                        ▒▒██                          



"""}
def initiatebattle():
	a = 0
	moveslist = []
	for move in range(100):
		moveslist.append(100)
		moveslist.append(49)
	if slime1.lvl <= 5:
			one = monsterlist[a](f"{monster[(monsterlist[a])]}", 10)
			print(f"You encountered a monster! Rat")
			print(monster[(monsterlist[a])])
			print(f"HP: {one.hp}")
			time.sleep(4)
			for t in moveslist:
				if t == 100:
					one.hp -= slime1.dmg
					print(f"Enemy HP: {one.hp}")
					if one.hp == 0:
						print("☆ Enemy died! You won!")
						break
				elif t == 49:
					slime1.hp -= 1
					print(f"Your HP: {slime1.hp}")
					if slime1.hp == 0:
						print(f"☆ {slime1.name} died!")
						exit()
	elif 10 > slime1.lvl > 5:
		one = monsterlist[a](f"{monster[(monsterlist[a])]}", 20)
		print(one)
		print(f"HP: {one.hp}")
		for t in moveslist:
			if t == 100:
				one.hp -= 2
				print(f"Enemy HP: {one.hp}")
				time.sleep(1)
			elif t == 49:
				slime1.hp -= 1
				print(f"Your HP: {slime1.hp}")
				time.sleep(1)
attrpoints = 0				
def initiateslime():
		global xpcap
		xpcap = 25
		chancelist = []
		for i in range(100):
			chancelist.append(100)
			chancelist.append(49)
		#print(chancelist)
		for s in range(5):
			stepcounter = 0
			for c in chancelist:
		#	print(c)
				if c == 100:
					stepcounter += 1
					slime1.lifeprocesses()
				elif c == 49:
					stepcounter +=1
					next_action()
					print(f"[Steps: {stepcounter}]")
				if stepcounter >= 4 and stepcounter % 2 == 0:
					slime1.xp += 5
					print(f"☆ 5xp+! Total xp for {slime1.name}: {slime1.xp}/{xpcap}")
					if slime1.xp == xpcap:
						attrpoints += 1
						slime1.lvl += 1
						xpcap += 20
						print(f"☆ {slime1.name} LEVELED UP! CONGRATULATIONS! {slime1.name} is level {slime1.lvl}")
						slime1.xp = 0
				if stepcounter >= 10 and stepcounter % 10 == 0:
					initiatebattle()
						
	
slimes = {1: r"""

          ██████████          
      ████░░░░░░░░░░████      
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
  ██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██  
██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██
██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██
██▓▓▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▓▓██
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  
    ██████████████████████    



""", 2: r"""


                ██████████                
        ████████░░░░░░░░░░████████        
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░██      
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
  ██░░░░░░░░░░░░░░░░░░            ░░██    
  ██░░░░░░░░░░░░░░                  ░░██  
██░░░░░░░░░░                        ░░░░██
██░░░░░░░░░░                        ░░░░██
██░░░░░░░░░░        ██        ██      ░░██
██░░░░░░░░          ██        ██      ░░██
██░░░░░░░░          ██        ██      ░░██
██░░░░░░░░                            ░░██
██░░░░░░░░░░                          ░░██
██░░░░░░░░░░░░                        ░░██
██░░░░░░░░░░░░░░                      ░░██
██░░░░░░░░░░░░░░░░░░                ░░░░██
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████
    ██████████████████████████████████    



""", 3: r"""

    ▓
            ▓▓▓
           ▓▓▓▓▓
       ░░▓▓▓▓▓▓▓▓▓▓
    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ░▓▓▓▓░░░░▓▓▓▓░░░░▓▓▓▓▓
 ▓▓▓▓▓░░▓▓░░▓▓░░▓▓░░▓▓▓▓▓
▓▓▓▓▓▓░░▓▓░░▓▓░░▓▓░░▓▓▓▓▓▓
▓▓▓▓██▓░░░░▓▓▓▓░░░░▓██▓▓▓▓
▓▓▓▓████▓▓▓▓▓▓▓▓▓▓████▓▓▓▓
  ▓▓▓▓██████████████▓▓▓▓
     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓	

"""
    }			
a= random.randint(1, 3)
slime1 = Slime(input("- Slime Name:"), 5, input("- Slime Color:"), 100, 100, slimes[a], 10, 0, 0, 2)	

if slime1.color == "White":
	white = Fore.WHITE
	print(white, f"White Slime {slime1.name}", slime1.type, Fore.WHITE)
elif slime1.color == "Red":
	red = Fore.RED
	print(red, f"Red Slime {slime1.name}", slime1.type, Fore.WHITE)
elif slime1.color == "Blue":
	blue = Fore.BLUE
	print(blue, f"Blue Slime {slime1.name}", slime1.type, Fore.WHITE)
elif slime1.color == "Yellow":
	yellow = Fore.YELLOW
	print(yellow, f"Yellow Slime {slime1.name}", slime1.type, Fore.WHITE)
elif slime1.color == "Green":
	green = Fore.GREEN
	print(green, f"Green Slime {slime1.name}", slime1.type, Fore.WHITE)
	
	
start_game()
initiateslime()

