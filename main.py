def dog_story():
  Dogname = input ("Type a name:")
  Dogverb = input("Type a verb:")
  Dogfood = input("Type a food:")
  Dogboyname = input("Type a boy name:")
  Dognoun = input("Type a noun:")
  Dogadjective = input("Type an adjective:")
  Dogdogbreed = input("Type a dog breed:")
  Dogplace = input("Type a place:")
  Dognametwo = input("Type another name:")
  print("Hello my name is " + str(Dogname) + " and I LOVE to " + str(Dogverb) + " with my pet dog. My dog loves to eat " + str(Dogfood) + " but he's not supposed to eat that. My dog's name is " + str(Dogboyname) + " and he does not like " + str(Dognoun)+ " My dog has a bunch of friends, one of his favorite friends is, " + str(Dogadjective) + " the " + str (Dogdogbreed) + ". They will always play and go to the " + str(Dogplace) + " with her owner, " + str(Dognametwo) + ". Me and " + str(Dognametwo) + " hang out all the time so " + str(Dogboyname) + " and " + str(Dogadjective) + " can keep on playing.")
def arcade_story():
  ArcadeName = input("Type a name:")
  ArcadeLocation = input("Type a location:")
  ArcadeNoun = input("Type a Noun:")
  ArcadeVerb = input("Type a Verb:")
  ArcadeFriend = input("Type another name:")
  ArcadeRestaurant = input("Type a restaurant name:")
  ArcadeFood = input("Type another noun:")
  print("There is a fun Arcade place called " + str(ArcadeName) + " and it is located in " + str(ArcadeLocation) + ". This is a really fun place to go because they have my favorite game, " + str(ArcadeNoun) + " the " + str(ArcadeVerb) + ". Whenever I go to " + str(ArcadeName) + " I go with my friend " + str(ArcadeFriend) + ". In this arcade they have a restaurant called " + str(ArcadeRestaurant) + " and they serve me and " + str(ArcadeFriend) + "‘s FAVORITE FOOD, "+ str(ArcadeFood) + " I would highly recommend going to " + str(ArcadeName) + " when you get the change!")
def forest_story():
  ForestName = input("Type a name:")
  ForestCamp = input("Type an adjactive:")
  ForestVerb = input("Type a verb:")
  ForestNoun = input("Type a Noun:")
  ForestAdjactive = input("Type a Adjactive:")
  ForestMonster = input("Type a animal:")
  ForestFamous = input("Type a Famous Person:")
  print("Today I went to the forest with my good friend, " + str(ForestName) + ". We went up there with Camp " + str(ForestCamp) + " because we heard a rumor about this forest called  " + str(ForestVerb) + ". People have been saying that there is a " + str(ForestNoun) + ", " + str(ForestAdjactive) + ", " + str(ForestMonster) + ". We went because me and " + str(ForestName) + " LOVE  " + str(ForestFamous) + " and they said that it is real so we trust them!!")
def taylor_swift():
  TaylorTown = input("Type a Noun:")
  TaylorHevan = input("Type a Person:")
  TaylorTall = input("Type an Adjactive:")
  TaylorAnimal = input("Type a Verb:")
  TaylorNiceDress = input("Type a artical of clothing:")
  TaylorSunset = input("Type another Noun:")
  TaylorRosyCheeks = input("Type another Verb:")
  TaylorWildestDreams = input("Type another Adjactive:")
  print("He said, Let's get out of this " + str(TaylorTown) + "\n\nDrive out of the city, away from the crowds\n\nI thought " + str(TaylorHevan) + " can't help me now\n\nNothing lasts forever, but this is gonna take me down\n\nHe's so " + str(TaylorTall) + " and handsome as " + str(TaylorAnimal) + "\n\nHe's so bad but he does it so well\n\nI can see the end as it begin\n\nMy one condition is\n\nSay you'll remember me standing in a  " + str(TaylorNiceDress) + "\n\nStaring at the " + str(TaylorSunset) + ", babe\n\nRed lips and " + str(TaylorRosyCheeks) + "\n\nSay you'll see me again\n\nEven if it's just in your " + str(TaylorWildestDreams) + ", ah-ha\n\n" + str(TaylorWildestDreams) + ", ah-ha\n")


again='y'


while again == 'y':

  print("Pick A Mad lib story!!! \n")

  selection = input("1. Dog Story \n2. Arcade Story \n3. Spooky Forest Story \n4. Taylor Swift Wildest Dreams \n\nChoose Story number 1-4: ")
  if selection == "1":
    dog_story()
  if selection == "2":
    arcade_story()
  if selection == "3":
    forest_story()
  if selection == "4":
    taylor_swift()

  again = input("\nDo you want to play again? y or n")



 