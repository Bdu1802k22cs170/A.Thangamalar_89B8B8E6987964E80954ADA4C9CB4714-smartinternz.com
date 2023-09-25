'''implement a class called player that represents a cricket player the player class should have a
method called play () which prints"the player is playing cricket derive two classes,batsman and
bowler, from the player class.override the play() method in each derived class to print"the batsman
is batting and"the bowler is bowling", respectively.write a program to create objects of both the
batsman and bowler classes and cell the play() method for each object.'''


#define the base class player
class player:
  def Play(self):
print ("the Play is playing cricket."):

#define the derived class batsman
class batsman (player):
  def play (self):
    print ("the batsman is batting.")

#define the derived class bowler
class bowler (player):
  def Play(self):
    print ("the bowler is bowling.")

#create objects of batsman and bowler classes
batsman=batsman ()
bowler=bowler ()

#call the play() method for each object
batsman.play()
