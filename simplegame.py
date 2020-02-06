print("Hello , welcome to Q&A-game")
ans=input("are u ready to play ?(yes/no): ")
result=0
no_q=5

if ans.lower()=="yes":
        
    ans=input("what is the best video game in the world ? ")
    if ans.lower()=="lol":
        print("correct")
        result+=1
        
    else:
        print("incorrect")

    ans=input("Can pigs walk on two feet?")
    if ans.lower()=="yes":
        print("correct")
        result+=1
    else:
        print("incorrect")

    ans=input("Can you stretch a rock?")
    if ans.lower()=="yes":
        print("correct")
        result+=1
    else:
        print("incorrect")

    ans=input("Are roses tall trees?")
    if ans.lower()=="yes":
        print("correct")
        result+=1
    else:
        print("incorrect")

    ans=input("Can you kill your self by holding your breath ?")
    if ans.lower()=="no":
        print("correct")
        result+=1
    else:
        print("incorrect")



ttl=(result/no_q)*100
print("Your Mark : ", ttl,"%")
print("GoodBye")

        



