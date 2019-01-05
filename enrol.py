print(" Welcome to my academy\n Academy of Science and technology")
print(" Enter '1' for admisson(Registration)\n Enter '2' to check free structre \n Enter 3 to check contact info")
print("...ENTER CHOICE..")
choice=int(input())
def adm():
    name=input(" Enter your name ")
    parentage=input(" Enter ur parentage ")
    dob=(input(" Enter ur Dob:- "))
    print("name={} parentage={} dob={}".format(name,parentage,dob))
if choice==1:
    adm()

