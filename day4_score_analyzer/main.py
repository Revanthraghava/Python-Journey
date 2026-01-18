scores = []

while True:
    element = input("Enter scores here (or done): ")

    if element == "done":
        break

    scores.append(int(element))

if scores:
    print("List of scores:", scores)

    total = 0
    for i in scores:
        total += i

    print("Total of scores:", total)

    count = len(scores)
    avg = total / count
    print(f"Average score: {avg}")

    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")

    if avg >= 40:
        print("PASS")
    else:
        print("FAIL")
else:
    print("NO SCORE AVAILABLE")
