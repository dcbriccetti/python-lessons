foods = ['soup', 'oranges']
print('foods is', foods)

foods.append('milk')
print ('After appending milk, foods is', foods)

print('foods[0] is', foods[0])
print('foods[1] is', foods[1])

foods.append(input('Enter a food: '))
print ('foods is now', foods)

print('Looping through foods: ')
for food in foods:
    print('A food:', food)
