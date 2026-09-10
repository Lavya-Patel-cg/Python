age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

reasons = []

if not (18 <= age <= 25):
    reasons.append("Age not in the required range")
if marks < 85:
    reasons.append("Marks below 85")
if attendance < 75:
    reasons.append("Attendance below 75%")
if income > 300000:
    reasons.append("Family income above ₹300000")

if not reasons:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
    for reason in reasons:
        print("Reason:", reason)