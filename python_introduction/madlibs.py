# Mad Libs Generator with Conditional Logic

# Prompting the user for input
adjective1 = input("Enter an adjective to describe the day: ")
adjective2 = input("Enter another adjective to describe a monkey: ")
adjective3 = input("Enter a majestic adjective for a lion: ")
adjective4 = input("Enter an adjective to describe the whole experience: ")
animal = input("Name another animal you might see at a zoo: ")
action = input("What is something funny the animal might do? (verb): ")
favorite_color = input("What's your favorite color? ")

# Conditional logic to add variation
if favorite_color.lower() == "blue":
    bonus_line = "The sky was so clear and blue, it felt like a dream."
elif favorite_color.lower() == "red":
    bonus_line = "A parrot with bright red feathers flew right past me!"
else:
    bonus_line = f"I even saw a {favorite_color.lower()} balloon float above the giraffe enclosure."

# Building the story with user inputs and conditional content
story = f"""
On a beautiful {adjective1} day, I went to the zoo.
I saw a funny {adjective2} monkey swinging from the trees.
Then, I spotted a {adjective3} lion lounging in the sun.
What a wild and {adjective4} experience!

Suddenly, a {animal} appeared and started to {action} right in front of everyone!
{bonus_line}

I'll never forget this zoo trip!
"""

# Displaying the final story
print("\nYour Mad Libs Story:")
print(story)
