"""
To do: 

- figure out Git integration
- 

"""

# Character definitions

# human
define hum = Character("Human")
# human images:
image human neutral = "human neutral.png"
image human surprised = "human surprised.png"

# ibex
define ibex = Character("Ibex")
# ibex images:
image ibex neutral = "ibex neutral.png"

#capy
define capy = Character("Capybara")
#capy images:
image capy neutral = "capy neutral.png"
image capy curious = "capy curious.png"

# Scene definitions
image bg trainstation present = "bg trainstation present.png"
image bg trainstation past = "bg trainstation past.png"
image bg clothespizza = "bg clothespizza.png"
image bg clothes-pizza = "bg clothes-pizza.png"
image bg arcade = "bg arcade.png"

# The game starts here.
label start:

    jump intro1


    return
