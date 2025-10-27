# Write code below 💖

# i like my answer more hmph
# import random

# answerList = ["OMG yes", "Bro, come on. You know", "WTF NO?????", "That question doesn't deserve an answer"]
# arraySize = len(answerList) - 1
# randomNumber = random.randint(0, arraySize)

# input("Question:     ")
# print("Magic 8 Ball: " + answerList[randomNumber])

import random

question = input('Question:     ')
random_number = random.randint(1, 9)

if random_number == 1:
  answer = "yes"
elif random_number == 2:
  answer = "yes please"
elif random_number == 3:
  answer = "yes yes please"
elif random_number == 4:
  answer = "NUH UH"
elif random_number == 5:
  answer = "no"
elif random_number == 6:
  answer ="I think so"
elif random_number == 7:
  answer = "...maybe?"
elif random_number == 8:
  answer = "most likely no"
elif random_number == 9:
  answer = "i think so"
else:
  answer = "error bro, ask again"

print("Magic 8 ball: " + answer)
