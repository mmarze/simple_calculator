import re
import math


def check_regex(expression, keyword):
    var = re.search(keyword, expression)
    if var is not None:
        var2 = re.search(r'\d+(\.\d*)?', expression[var.end():])
        if var2 is not None:
            var2 = var2.group()
            return 'math.' + keyword + '(' + var2 + ')'
        else:
            raise ValueError
    else:
        raise ValueError


def main():
    print("This simple calculator enables mathematical operations on maximum two real numbers.")
    print("Available operations: +, -, *, /, //, %, !, sqrt, log10, ln, sin, cos, tan")
    print("For !, 2nd argument ignored")
    print("For sqrt, log10, ln, sin, cos, tan, the 1st argument is ignored")
    print("-----")

    while True:
        try:
            expression = input("Provide your input: \n")
            pattern = r"[\+\-\*\/\%\!ictrgn]"
            expression = expression.lower()
            a = re.search(pattern, expression)

            if a is not None:
                start = a.start()
                stop = a.end()
                match = a.group()

                if match == 'i':
                    expression2 = check_regex(expression, 'sin')
                elif match == 'c':
                    expression2 = check_regex(expression, 'cos')
                elif match == 't':
                    expression2 = check_regex(expression, 'tan')
                elif match == 'r':
                    expression2 = check_regex(expression, 'sqrt')
                elif match == 'g':
                    expression2 = check_regex(expression, 'log10')
                elif match == 'n':
                    expression2 = check_regex(expression, 'ln')
                    expression2 = expression2.replace('ln', 'log')
                elif match == '!':
                    var1 = re.search(r'\d+(\.\d*)?', expression[:start])
                    if var1 is not None:
                        var1 = var1.group()
                        expression2 = 'math.factorial(' + var1 + ')'
                    else:
                        raise ValueError
                elif match == r'/':
                    var1 = re.search(r'\d+(\.\d*)?', expression[:start])
                    var2 = re.search(r'\d+(\.\d*)?', expression[stop:])
                    if var1 is not None:
                        var1 = var1.group()
                        if var2 is not None:
                            var2 = var2.group()
                            if expression[stop] == r'/':
                                match = r'//'
                            expression2 = var1 + match + var2
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                else:
                    var1 = re.search(r'\d+(\.\d*)?', expression[:start])
                    var2 = re.search(r'\d+(\.\d*)?', expression[stop:])
                    if var1 and var2 is not None:
                        var1 = var1.group()
                        var2 = var2.group()
                        expression2 = var1 + match + var2
                    else:
                        raise ValueError

                result = eval(expression2)

                print("Your formula: \n\t", expression2, "\n")
                print("Solution: \n\t", result, "\n")
            else:
                raise ValueError

        except ValueError:
            print(f"\n\t ERROR! Invalid input!")
        except ZeroDivisionError:
            print("\n\t ERROR! Cannot divide by zero!")
        finally:
            print("-----")
            print("Do you want to try again? [Y/N]")
            resp = input()
            if resp != 'Y':
                print("-----\n\tBYE!")
                break
            print("-----")


if __name__ == "__main__":
    main()
