from pet import Pet

# Create your pet
my_pet = Pet("trixy")

# Show the initial status of the pet
my_pet.get_status()

print("\n--- Interacting with trixy-")

# Perform actions
my_pet.eat()
my_pet.sleep()
my_pet.play()

# Teach some tricks
my_pet.train("sit")
my_pet.train("roll over")
my_pet.train("jump")  

# Show tricks Buddy knows
my_pet.show_tricks()

# Display the updated status
my_pet.get_status()


my_pet.energy = 1
print (f"{my_pet.name}'s energy is {my_pet.energy}")
my_pet.play()
my_pet.train("dance")