is_student=input("Are u student(Yes/No)").lower().strip()
has_id=input("Do u have student id(Yes/No)").upper().strip()
has_ticket=("Do u have ticket (Yes/no)").capitalize().strip()


if is_student=="no":
        is_student=False
elif is_student=="yes":
         is_student=True


if has_id=="YES":
        has_id=True
elif has_id=="NO":
 has_id=False


if has_ticket=="Yes":
        has_ticket=True
elif has_ticket=="No":
        has_ticket=False


if  is_student and has_id and has_ticket: 
                                            print("Allowed")
else: 
        print("Not allowed")