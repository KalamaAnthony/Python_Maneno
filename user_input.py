name = input("What is your name? ")
role = input("What is your role at Equity?")

passion=input("Do you love what you do?, (Give a yes or no answer)")
if passion == "yes":
    passion = "I love what I do"
elif passion == "no":   
    passion = "I don't love what I do"
else:
    passion = "Please offer a valid answer"


print("Hello " + name + " you are a " + role + " at Equity bank and  " + passion)

x= {}
x[2]=10
x[1]=[10,30,40]
print(x[1][2])

a= 10
b = 3
print(a%b)

