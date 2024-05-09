
#denotes seconds in an hour 
global seconds
seconds = 3600
#denotes minutes in an hour
global minute
minute = 60
global entry

def how_many_seconds():
    global entry
    entry = int(input("Please enter the amount of hours you would like to convert:"))
    conversion = entry*seconds
    statement = str(entry)+" "+"hours"+" "+"= "+" "+ str(conversion)+" " +"seconds"
    print(statement)

def how_many_minutes():
    entry
    math = minute * entry
    print(str(entry)+" "+ "hours "+" "+ " ="+" "+str(math) +" " "minutes")




how_many_seconds()
how_many_minutes()