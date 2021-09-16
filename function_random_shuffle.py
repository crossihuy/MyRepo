from random import shuffle as shuf

def mult(ans_list, quest, ans, points):
    abcd =["A", "B", "C", "D"]
    shuf(list1)
    print(quest)
    for i,j in zip(abcd, ans_list):
        print(f"  {i}.  {j}")
    while True:
        answer = input("Answer: ").upper()
        if answer in abcd:
            break
        else:
            print("Invalid Entry")
    if abcd.index(answer) == ans_list.index(ans): #makes ans_list.index into ans
        points = points + 10
    return points

def main():

        score = 0
        print(score)
        list1 = ["Blue", "Brown", "Green", "Purple"]
        score = mult(list1, "What color is the sky on a nice day?", "Blue", score)
        print(score)

        list2 = ["Green", "Yellow", "Pink", "orange"]
        score = mult(list2, "ask a question ?", "put correct answer", score)

        list3 = []
        score = mult(list3, "ask a question ?", "put correct answer", score)

        list4 = []
        score = mult(list4, "ask a question ?", "put correct answer", score)

        list5 = []
        score = multi (list5,"ask a question ?", "put correct answer", score)

        if score >90:
            print("You get an A.")
        elif score >80:
            print("You get a B.")
if__nam__=="__main__":
main()