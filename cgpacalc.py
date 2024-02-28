def calc():
    credits=[]
    sgpa=[]
    cgpa=0
    total_credits=0
    credits = list(map(float, input("Enter the credits separated by space: ").split()))
    sgpa = list(map(float, input("Enter the sgpa separated by space: ").split()))
    for i in range(len(credits)):
        cgpa += credits[i] * sgpa[i]
        total_credits += credits[i]
    cgpa/=total_credits
    cgpa=round(cgpa,2)
    print("your cgpa is ",cgpa)
calc()
