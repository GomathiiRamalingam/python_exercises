# Store the names in a list
dinner = ['father', 'mother', 'brother', 'best friend', 'girlfriend']

# Print the inviation to all names stored in the dinner list.
message = ('I invite you to have dinner tomorrow at my house.')
print(dinner[0].title()+ ', '+ message)
print(dinner[1].title()+ ', '+ message)
print(dinner[2].title()+ ', '+ message)
print(dinner[3].title()+ ', '+ message)
print(dinner[4].title()+ ', '+ message)


print(f'My {dinner[2]} can\'t make the dinner.')

# Change a name on the dinner list, and print all the names with
# the message again.
dinner[2] = 'eduardo'
print(dinner[0].title()+ ', '+ message)
print(dinner[1].title()+ ', '+ message)
print(dinner[2].title()+ ', '+ message)
print(dinner[3].title()+ ', '+ message)



