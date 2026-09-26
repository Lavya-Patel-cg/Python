Outstanding_count=0
Excellent_count=0
Good_count=0
Average_count=0
Poor_count=0
Rating=0


for i in range(1,11):
    rating=float(input("Enter ratings of movie{i}:-"))
    if 9.1<=rating<=10:
        Outstanding_count+=1
        Rating+=rating
        print("OutStanding")
    elif 7.1<=rating<=9:
        Excellent_count+=1
        Rating+=rating
        print("Excellent")
    elif 5.1<=rating<=7:
        Good_count+=1
        Rating+=rating
        print("Good")
    elif 3.1<=rating<=5:
        Average_count+=1
        Rating+=rating
        print("Average")
    elif 0<=rating<=3:
        Poor_count+=1
        Rating+=rating
        print("Poor")

print("Movies falling in outstanding category:-",Outstanding_count)
print("Movies falling in Excellent category:-",Excellent_count)
print("Movies falling in Good category:-",Good_count)
print("Movies falling in Average category:-",Average_count)
print("Movies falling in Poor category:-",Poor_count) 
total=Rating
average_rating=total/10
print("Average Rating of all the movies",average_rating)
