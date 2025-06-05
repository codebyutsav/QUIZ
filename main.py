def run_quiz():
    questions={
        "1.What is the largest organ in human body?\n":
        {
            "options":[
                "A.Heart",
                "B.Liver",
                "C.Skin",
                "D.Lungs\n"
            ],
            "answer":"C"
        },
        "2.Who invented the light bulb?\n":
        {
            "options":[
                "A.Nikola Tesla",
                "B.Alexander",
                "C.Thomas Edison",
                "D.Albert Einstein\n"
            ],
            "answer":"C"
        },
        "3.What is square root of 64?\n":
        {
            "options":[
                "A.8",
                "B.7",
                "C.6",
                "D.9\n"
            ],
            "answer":"A"
        },
        "4.How many legs spider have?\n":
        {
            "options":[
                "A.6",
                "B.8",
                "C.10",
                "D.12\n"
            ],
            "answer":"B"
        },
        "5.What is H20?\n":
        {
            "options":[
                "A.Oxygen",
                "B.Hydrogen",
                "C.Salt",
                'D.Water'
            ],
            "answer":"D"
        }
    }

    score=0
    print("Welcome to Quiz\n")


    for question,data in questions.items():
        print(question)

        for option in data["options"]:
            print(option)
            
        answer=input("Enter your choice:").strip().upper()

        if answer in ["A","B","C","D"]:
            if(answer == data["answer"]):
                print("Correct answer!You have scored a point.\n")
                score+=1
            else:
                print(f"Wrong answer.\nCorrect answer is {data["answer"]}")
        else:
            print("Invalid choice!")

    print(f"\nYour final score is {(score)*100/len(questions)}")

    if score == len(questions):
        print("Very Good!Your all answers are correct")
    elif score >= len(questions)*0.6:
        print("Good!")
    else:
        print("Keep practising!")


if __name__ == "__main__":
    run_quiz()