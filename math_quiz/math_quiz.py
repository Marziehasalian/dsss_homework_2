#Marzieh Asalian
import random
# Generate_random_number generates a random integer between min and max and include this max and min
# for example: if max:3 and min:1 randomly this function pic two number from 1,2,3
def Generate_random_number(min_random, max_random):
    """
        Generate_random_number
        Parameters:
        - min_random (int): The max number.
        - min_random (int): The min number.
        Returns:
        int: a random int between min_random and  max_random
        """
    return random.randint(min_random, max_random)
def Generate_random_operator():
    """
            Generate_Random_operator
            Parameters: nothing

            Returns:
            str: Generate_random_operator randomly choose between '+', '-', '*'
           """

    return random.choice(['+', '-', '*'])

# Generate_random_Function: with random numbers from Generate_random_number and random sign form Generate_random_operator creat math problem
#calculate the correct answer for that math problem
def Generate_random_Function(first_random_number, second_random_number, Random_operator):
    """
        Generate_random_number
        Parameters:
        - first_random_number (int): random number .
        - second_random_number (int): random number.
        - Random_operator (str): random operator.
        Returns:
        random_function(str): a random function
        correct_answer(int): correct answer of that random function
        """
    random_function = f"{first_random_number} {Random_operator} {first_random_number}"
    if Random_operator == '+':
        correct_answer = first_random_number + first_random_number
    elif Random_operator == '-':
        correct_answer = first_random_number - first_random_number
    else:
        correct_answer = first_random_number * first_random_number

    return random_function, correct_answer

def math_quiz():
    """
            create math quiz:
            str: get the answer of the math quiz from participant
            str: print out that if the answer is correct and if is not print out the correct number
            str: at the end of the game print out if the participant win or not
            """
    Counter_correct = 0
    # put the value of zero for the counting the number of the correct answers
    # our quiz has ask 3 question, so we put steps_of_quiz=3
    steps_of_quiz = 3
    # Initiation message for stating the Game

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(steps_of_quiz):
        #first_random_number:generate first random unt number between 1 and 10, first_random_number: generate second random int number between 1 and 5,
        # and o generate random operation
        first_random_number = Generate_random_number(1, 10); first_random_number = Generate_random_number(1, 5);
        Random_operator = Generate_random_operator()
        #PROBLEM is the random function with that random variable and ANSWER is the correct answer to that function
        PROBLEM, ANSWER = Generate_random_Function(first_random_number, first_random_number, Random_operator)
        print(f"\nQuestion: {PROBLEM}")
        #Error handling: making sure that participants input an integer
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError:
                print("your answer is not integer, please enter an integer for answer")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            Counter_correct += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    if Counter_correct==steps_of_quiz :
        print(f"\nYou won! Your score is: {Counter_correct}/{steps_of_quiz}")
    else:
        print(f"\nGame over! Your score is: {Counter_correct}/{steps_of_quiz}")
#Run the math quiz if this code is executed directly
if __name__ == "__main__":
    math_quiz()
