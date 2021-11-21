# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) #== changed to = since its assignment; ' to " since both quotes should be identical
                                                              #. after int changed to ( since that is the format
if year < 1900: #colon (:) was missing; above comment says 'before 1900' so its only <
    print ("Woah, that's the past!") #used "" to make print full line and allow ' to be in string
elif year >= 1900 and year <= 2020:   #changed && to 'and' for syntax and 2020 & 1900 counted so <= & >=
    print ("That's totally the present!")
else:  #elif changed to else since its last condition
    print ("Far out, that's the future!!")
