likefootball=int(input("enter student who like football:  "))
likebadminton=int(input("enter student who like badminton:  "))
likeboth=int(input("enter student who like both:  "))
dontlike=int(input("enter student who dont like both:  "))
total=likefootball+likebadminton-likeboth+dontlike
print("the total no of stidents is:",total)