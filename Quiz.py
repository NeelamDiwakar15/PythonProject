choice =input("Will you want to play?\t yes or no = ").title()
marks=0
if choice=='Yes':
    answer=input("Where is Taj Mahal? ").title()
    if (answer=='Agra'):
        print(f"{answer}  :Correct!!!✅")
        marks+=1
    else:
        print("Incorrect ❌!!")
    answer=input("What is full form of CPU? ").title()
    if (answer=='Central Processing Unit'):
        print(f"{answer}  :Correct!!!✅")
        marks+=1
    else:
        print("Incorrect ❌!")
    answer=input("What is capital of India? ").title()
    if (answer=='New Delhi'):
        print(f"{answer}  :Correct!!!✅")
        marks+=1
    else:
        print("Incorrect ❌:")
    answer=input("Pink City is? ").title()
    if (answer=='Jaipur'):
        print(f"{answer}  :Correct!!!✅")
        marks+=1
    else:
        print("Incorrect ❌!")
else:
    print("Exit")
print("\t\tTHANKYOU !!\tyou got marks :",marks)
