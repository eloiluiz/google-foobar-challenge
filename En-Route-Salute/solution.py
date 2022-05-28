def solution(s):
    """ Decodes the input string and counts the number of salutes.
    """
    import string
    from sets import Set

    salute_number = 0
    has_employee = True
    hall_length = len(s)

    print("Hall: " + s)

    # Check for an empty string
    if (hall_length == 0):
        return salute_number

    # Check if string only has valid characters
    allowed_chars = Set('-<>')
    if (Set(s).issubset(allowed_chars) == False):
        return salute_number

    # Iterate over the input string
    s = list(s)
    while (has_employee == True):
        has_employee = False
        i = 0
        while (i < hall_length):
          
            print("Hall[" + str(i).zfill(2) + "]: " + "".join(s))
            print("salute_number: " + str(salute_number) + "\n")

            # Check if the hall spot is empty
            if (s[i] == '-'):
                i += 1
                continue

            # Check for employee
            if (s[i] == '<'):
                if (i == 0):
                    s[i] = '-'
                else:
                    has_employee = True

                    if (s[i-1] == '<'):
                        i += 1
                        continue
                    elif (s[i-1] == '>'):
                        salute_number += 2
                        s[i] = '>'
                    else:
                        s[i] = '-'

                    s[i-1] = '<'

            elif (s[i] == '>'):
                if (i == (hall_length - 1)):
                    s[i] = '-'
                else:
                    has_employee = True

                    if (s[i+1] == '>'):
                        i += 1
                        continue
                    if (s[i+1] == '<'):
                        i += 1
                        continue

                    s[i] = '-'
                    s[i+1] = '>'
                    i += 1

            i += 1

    return salute_number


def test():
    """ Application test function
    """
    input = "\0"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = ""
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = "a"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = ">----<"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = "<<>><"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = "--->-><-><-->-"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")


# Application entry point
if __name__ == "__main__":
    test()
