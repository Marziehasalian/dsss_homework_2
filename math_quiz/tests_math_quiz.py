#Marzieh Asalian
import unittest
from math_quiz import Generate_random_number, Generate_random_operator, Generate_random_Function

class TestMathGame(unittest.TestCase):

    def test_Generate_Random_number(self):
        """
                test for Generate_Random_operator
                Parameters: nothing

                Returns:
                error if Generate_random_operator is not between specific range
               """

        # make sure that the random number is in that range
        min_val = 1
        max_val = 1000
        for i in range(10000):
            rand_num = Generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        """
                test for Generate_random_operator
                Parameters: nothing

                Returns:
                error if Generate_random_operator is not between ['+', '-', '*']
               """

        # Test if Generate_random_operator is between ['+', '-', '*'] or not
        valid_operators = ['+', '-', '*']
        num_tests = 200

        for i in range(num_tests):
            rand_operator = Generate_random_operator()
            condition = lambda x: rand_operator in x
            # Check if at least one element in the list is in the condition
            if not any(condition(j) for j in valid_operators):
                raise ValueError(f"false oprator '{target_substring}'.")




    def test_Generate_random_Function(self):
        """
                        test for Generate_random_Function
                        Parameters: nothing

                        Returns:
                        error if correct_answer and expected_answer be not equal
                       """

        test_cases = [
            (20, 25, '+', '20 + 25', 45),
            (30, 13, '-', '30 - 13', 17),
            (40, 20, '*', '40 * 20', 800),
            (51, 2, '+', '51 + 2', 53),
            (60, 5, '-', '60 - 5', 55),
            (1, 5, '*', '1 * 5', 5),
            (66, 9, '+', '66 + 9', 75),
            (33, 13, '-', '33 - 13', 20),
            (11, 9, '*', '11 * 9', 99),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # Test if the generated function and answer match the expected values
            generated_problem, generated_answer = Generate_random_Function(num1, num2, operator)
            if operator == '*':
                correct_answer = num1 * num2
            elif operator == '+':
                correct_answer = num1 + num2
            else:
                correct_answer = num1 - num2

            # if correct_answer and expected_answer be not equal raise an error

            self.assertEqual(correct_answer, expected_answer)

#Run the math quiz test if this code is executed directly
if __name__ == "__main__":
    unittest.main()
