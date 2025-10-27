# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input("Q1) Do you like Dawn or Dusk?\n    1) Dawn\n    2) Dusk\n"))
if q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

q2 = int(input("Q2) When I'm dead, I want people to remember me as:\n    1) The Good\n    2) The Great\n    3) The Wise\n    4) The Bold\n"))
if q2  == 1:
  Hufflepuff += 2
elif q2 == 2:
  Slytherin += 2
elif q2 == 3:
  Ravenclaw += 2
elif q2 == 4:
  Gryffindor += 2
else:
  print("Wrong input.") 

q3 = int(input("Q3) Which kind of instrument most pleases your ear:\n    1) The violin\n    2) The trumptet\n    3) The piano\n    4) The drum\n"))
if q3  == 1:
  Slytherin += 4
elif q3 == 2:
  Hufflepuff += 4
elif q3 == 3:
  Ravenclaw += 4
elif q3 == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print("Gryffindor points: " + str(Gryffindor))
print("Slytherin points:  " + str(Slytherin))
print("Hufflepuff points: " + str(Hufflepuff))
print("Ravenclaw points:  " + str(Ravenclaw))

if Gryffindor > Ravenclaw and Gryffindor > Slytherin and Gryffindor > Hufflepuff:
  answer = "Gryffindor!"
elif Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
  answer = "Ravenclaw!"
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
  answer = "Slytherin!"
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
  answer = "Hufflepuff!"
else:
  answer = "expulsion, Muggle!"

print("Welcome to " + answer)
