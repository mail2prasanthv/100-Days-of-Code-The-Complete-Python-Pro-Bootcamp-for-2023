# List Comprehension

items = [1,2,3,4,5]

new_items = [each for each in items]

print("items:", items)
print("new_items:",new_items)

# multiply each item by 2
new_items = [each*2 for each in items]
print("multiplied each item by 2:",new_items)

# multiply each item by 2 if it is even number
new_items = [each*2 for each in items if each%2 ==0]
print("multiplied each item by 2:",new_items)
