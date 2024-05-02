# 1. příklad
for letter in "Giraffe Academy":
    print(letter)

# 2. Příklad: Pro každý friend v friends vypiš každého frienda
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# 3 Příklad (se slovníkem). Vypíše klíče 1 2 3
friends2 = {1: "Carl", 2: "John", 3: "Tom"}
for friend in friends2:
    print(friend)

# 4. Příklad: Vypíš 0 až 9
for index in range(10):
    print(index)

 # 5. Příklad: Vypíš 3 až 8
for index in range(3, 9):
    print(index)

# 6. Příklad: Vypíše 0 1 2. Len spočítá počet objektů v proměnné friends
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(index)

# 7. Příklad: Vypíše Jim Karen Kevin.
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

# 8. Příklad:
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first iteration")
