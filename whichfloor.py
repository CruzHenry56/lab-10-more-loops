maximum_stories = 100
userstring = int(input("On what floor of the building is your office "))

while userstring > maximum_stories:
    print("You entered:"+ str(userstring) +" but there are only " + str(maximum_stories) + " floors in the building try agin...")
    userstring = int(input("On what floor of the building is your office "))

print("Congrats! You work on floor: " + str(userstring))
