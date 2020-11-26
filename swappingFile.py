def countcharactersinfile():
    filename=input("Enter File Name")
    Noofcharacters=0
    file=open(filename,"r")
    for chara in file:
        chara=line.split()
        Noofcharacters=Noofcharacters+len(characters)
    print("Noofcharacters:")
    print(Noofcharacters)
countcharactersinfile()

def countwordsinfile():
    filename=input("Enter File Name")
    Noofwords=0
    file=open(filename,"r")
    for wo in file:
        wo=line.spilt()
        Noofwords=Noofwords+len(words)
    print("Noofwords:")
    print(Noofwords)
countwordsinfile()