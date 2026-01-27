def score_input():
    score = []
    while True:
        element = input("Enter scores here(or done): ")
        if element == "done":
            break
        score.append(int(element))

    return score

def score_analysis(score):
    count_distinction = 0
    count_pass = 0
    count_fail= 0
    for i in score:
        if i >= 75:
            count_distinction += 1
        elif 40 <= i < 75:
            count_pass += 1
        else:
            count_fail +=1
    return count_distinction,count_pass,count_fail

score = score_input()
if score:
    total = len(score)
    count_distinction,count_pass,count_fail = score_analysis(score)
    distinction_percentage = count_distinction*100/total
    pass_percentage = count_pass*100/total
    fail_percentage = count_fail*100/total
    print(f"""
          This is score analyzer.Scores given were {score}.
          Total number of scores taken were {total}.
          Total distinction percentage is {distinction_percentage}%.
          Total pass percentage is {pass_percentage}%.
          Total fail percentage is {fail_percentage}%.
          """)
    
else:
    print("NO SCORES WERE GIVEN.")
    

