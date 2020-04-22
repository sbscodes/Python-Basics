import argparse
import random
if __name__=='__main__':
    Myparser = argparse.ArgumentParser(
        description="This is One of the Trending Instagram thing\n"
                    "where user enter their name and the app shows\n"
                    "them their name and some other related quotes to user\n"
                    "so I am Satish Birhade Trying to impliment that thing in\n"
                    "python Script\n"
                    "To Execute Script Enter Into The CMD and CD into the path Where\n"
                    "the File is Stored and Execute it Into Following Manner\n\t"
                    "\n\t-->python Name.py --Name YourName or (-n=YourName)<--"
    )
    Myparser.add_argument("-n", "--Name", help="Enter Your Name", type=str, default="Unknown")
    args = Myparser.parse_args()
    name = str(args.Name)
    Uppername = name.upper()
    MalesQuality = []
    Namemean = {"A": "Audacious", "B": "Brave", "C": "Compassionate", "D": "Driven"
        , "E": "Encouraging", "F": "Fearless", "G": "Generous"
        , "H": "Honest", "I": "Inspirational", "J": "Just", "K": "Kind"
        , "L": "Loyal", "M": "Magnanimous", "N": "Nobel", "O": "Optimistic"
        , "P": "Perseverant", "Q": "Quiet", "R": "Resilient", "S": "Stalwart"
        , "T": "Team player", "U": "Understandable", "V": "Visionary", "W": "Wise"
        , "X": "X-Factor", "Y": "Youthful", "Z": "Zealous"}
    firstquote =["is boy who is famouus in girls","take care of girls",
                 "is very respectful towerds girls"
                   ,"is caretaker of girls offenly"]
    middlequote = ["is Cool", "is Charming", "is Handsom", "is dashing", "is adorable"
         ,"is funny","is hot","is open minded"]
    lastquote = ["is the best friend you ever meet in your life",
             "is the best person who do not heart you in life"]
    if name == "Unknown":
      print("Please Enter Your Name First......!")
    else:
        print("-->%s<--MEANS " % Uppername)
        for a in Uppername:
            print("{0}->{1}".format(a, Namemean[a]))
        lastrandomquote=random.choice(lastquote)
        middlerandomquote = random.choice(middlequote)
        firstrandomquote = random.choice(firstquote)
        print(Uppername, firstrandomquote)
        print(Uppername ,middlerandomquote)
        print(Uppername, lastrandomquote)