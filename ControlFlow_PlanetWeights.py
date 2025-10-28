
# Write code below 💖

earthWeight = float(input("What is your earth weight?"))
planetNumber = int(input("What is your planet number?"))

if planetNumber == 1:
  relativeGravity = 0.38
elif planetNumber == 2:
  relativeGravity = 0.91
elif planetNumber == 3:
  relativeGravity = 0.38
elif planetNumber == 4:
  relativeGravity = 2.53
elif planetNumber == 5:
  relativeGravity = 1.07
elif planetNumber == 6:
  relativeGravity = 0.89
elif planetNumber == 7:
  relativeGravity = 1.14
else:
  print('Invalid planet number')
  return

destinationWeight = earthWeight * relativeGravity

print(f'Your destination weight is {destinationWeight}')
