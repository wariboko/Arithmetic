def arithmetic_arranger(problems, results=False):

  #Empty line
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  #Problems shouldn't be more than 5
  if len(problems) > 5:
    return Error: Too many problems.
  #Splitting the operators and operands with digits in them.
  for a, problem in enumerate(problems):
    print_first_line, operator, print_second_line = problem.split()
    #Only the given operators are allowed
    if operator not in ['+', '-']:
      return Error: Operator must be + or -.
    #Must be digits only
    if print_first_line.isdigit() == False:
      return Error: Numbers must only contain digits.
    elif print_second_line.isdigit() == False: 
      return Error: Numbers must only contain digits.
    #Operands musts not be more than four.
    if len(print_first_line) > 4:
      return Error: Numbers cannot be more than four digits.
    elif len(print_second_line) > 4:
      return Error: Numbers cannot be more than four digits.
    #Finding the operators and solving the problem
    if operator.find(+) != -1:
      answer = int(print_first_line) + int(print_second_line)
    else:
      answer = int(print_first_line) - int(print_second_line)
    #Assigning space length to the lines
    spaces = max(len(print_first_line), len(print_second_line)) + 2
  #Filling the lines with corresponding spaces
    line1 += print_first_line.rjust(spaces)
    line2 += operator + print_second_line.rjust(spaces - 1)
    line3 += '-' * spaces
    line4 += str(answer).rjust(spaces)
    #Entering the spaces after problem solving
    if a < len(problems) - 1:
      line1 += '    '
      line2 += '    '
      line3 += '    '
      line4 += '    '
  #Return result
  arranged_problems = line1 + n + line2 + n + line3
  if results:
    arranged_problems += n + line4

  return arranged_problems


def arithmetic_arranger(problems, results=False):

  #Empty line
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  #Problems shouldn't be more than 5
  if len(problems) > 5:
    return Error: Too many problems.
  #Splitting the operators and operands with digits in them.
  for a, problem in enumerate(problems):
    print_first_line, operator, print_second_line = problem.split()
    #Only the given operators are allowed
    if operator not in ['+', '-']:
      return Error: Operator must be + or -.
    #Must be digits only
    if print_first_line.isdigit() == False:
      return Error: Numbers must only contain digits.
    elif print_second_line.isdigit() == False: 
      return Error: Numbers must only contain digits.
    #Operands musts not be more than four.
    if len(print_first_line) > 4:
      return Error: Numbers cannot be more than four digits.
    elif len(print_second_line) > 4:
      return Error: Numbers cannot be more than four digits.
    #Finding the operators and solving the problem
    if operator.find(+) != -1:
      answer = int(print_first_line) + int(print_second_line)
    else:
      answer = int(print_first_line) - int(print_second_line)
    #Assigning space length to the lines
    spaces = max(len(print_first_line), len(print_second_line)) + 2
  #Filling the lines with corresponding spaces
    line1 += print_first_line.rjust(spaces)
    line2 += operator + print_second_line.rjust(spaces - 1)
    line3 += '-' * spaces
    line4 += str(answer).rjust(spaces)
    #Entering the spaces after problem solving
    if a < len(problems) - 1:
      line1 += '    '
      line2 += '    '
      line3 += '    '
      line4 += '    '
  #Return result
  arranged_problems = line1 + n + line2 + n + line3
  if results:
    arranged_problems += n + line4

  return arranged_problems


