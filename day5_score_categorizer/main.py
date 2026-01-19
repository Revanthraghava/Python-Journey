score = []
while True:
    element = input("Enter scores of students(or done):")

    if element == "done":
        break
    score.append(int(element))
if score:
    total = len(score)
    print("Total students: ",total)
    print("scores given: ",score)

    p = []
    for i in score:
        if i >= 40:
            p.append(int(i))
    a = len(p)
    print("Number of students passed: ",a)
        
        
    pass_percent = a*100 / total
    print("Pass percentage: ",pass_percent)
        

                
    f = []
    for i in score:
        if i < 40:
            f.append(int(i))
    b = len(f)
    print("Number of students failed: ",b)
        
    fail_percent = b*100 / total
    print("Fail percentage: ",fail_percent)

        
        


    
    print(f"""This is the overall analysis of students results done by SCORE CATEGORIZER.
          {total} number of students were considered. {a} number of students passed the 
          exam.{b} number of students failed the exam.Overall pass percentage is{pass_percent}.
          Overall fail percentage is {fail_percent}.Thank you. """)

else:
    print("No scores entered.")
