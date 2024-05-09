
#denotes seconds in an hour 
global seconds
seconds = 3600
minute = 60

def how_many_seconds():
    entry = int(input("Please enter the amount of hours you would like to convert:"))
    conversion = entry*seconds
    statement = str(entry)+" "+"hours"+" "+"= "+" "+ str(conversion)+" " +"seconds"
    print(statement)
    




how_many_seconds()