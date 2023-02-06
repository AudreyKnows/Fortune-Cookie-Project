import random
lucky_number = random.randint(1,100)

fortune_number = random.randint(1,100)

fortune_text =""

if fortune_number == 10:
  fortune_text = "Collect your Prize"

if fortune_number == 20:
  fortune_text = "That apartment is yours!"

if fortune_number == 30:
  fortune_text = "Call your mom"

if fortune_number == 40:
  fortube_text = "Let's cut down on the sugar"

if fortune_number == 50:
  fortune_text = "Buy that bag"

if fortune_number == 60:
  fortune_text = "Despite all your resources and exasperated efforts she still made it"

if fortune_number == 70:
  fortune_text = "Apply to your dream job"

if fortune_number == 80:
  fortune_text = "May your enemies forever look up to you from beneath and behind you"

if fortune_number == 90:
  fortune_text = "Theres no time frame....for reciprocity"

if fortune_number == 100:
  fortune_text = "May the Best villain win!"
  
print(f"{fortune_text} Today your lucky number is {lucky_number}")