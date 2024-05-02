lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
print(friends)


friends.remove("Jim")
print(friends)

friends.clear()
print(friends)

# pop odstraní posledního ze seznamu
friends2 = ["Michael", "Dennis", "Monika", "Leona", "Martin", "Jacob"]

friends2.pop()
print(friends2)

# Řekne jaký index má Jim
print(friends2.index("Monika"))

# Řekne kolikrát je Oscar v seznamu
print(friends2.count("Jacob"))


friends3 = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends3.sort()
friends3.reverse()
print(friends3)

# friends4 je kopie lucky_numbers
friends4 = lucky_numbers.copy()
print(friends4)

