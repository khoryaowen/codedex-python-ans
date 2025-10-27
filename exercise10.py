# Write code below 💖

pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

pesosToUSD = pesos * 0.00026 
solesToUSD = soles * 0.3 
reaisToUSD = reais * 0.29

totalUSD = pesosToUSD + solesToUSD + reaisToUSD
print(totalUSD)
