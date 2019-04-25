def translate(phrase):
    transalation = ""
    for i in phrase:
        if i in "AEIOUaeiou":
            transalation = transalation + "g"
        else:
            transalation = transalation + i
    return transalation



def new():
    t=0
    t= int(input("enter t"))
    print (type(t))
    while (t) > 0:
      print(translate(input("Enter the phrase:")))
      t= t-1

new()