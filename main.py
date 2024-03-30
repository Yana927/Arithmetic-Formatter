def arithmetic_arranger(problems, answer=False):
  
  # The problems`s limit is five
  if len(problems) > 5:
    return "Error: Too many problems."
    
  arranged_problems = ""
  top_line = ""
  bottom_line = ""
  dash_line = ""
  answer_line = ""
  answers = []
  for problem in problems:
    first_num = problem.split()[0]
    operator = problem.split()[1]
    second_num = problem.split()[2]
    
    #The appropriate operators are addition and subtraction  
    if operator != '+' and operator != '-':
      return "Error: Operator must be '+' or '-'."
    #Each number has a max of four digits in width   
    if len(first_num) > 4 or len(second_num) > 4:
      return "Error: Numbers cannot be more than four digits."
      
    #Each number is a digit
    if not first_num.isdigit() or not second_num.isdigit():
      return "Error: Numbers must only contain digits."
      
    length = max(len(first_num), len(second_num)) + 2
    top_line += first_num.rjust(length) + '    '
    bottom_line += operator + second_num.rjust(length - 1) + '    '
    dash_line += '-' * length + '    '
    
    if answer:
        if operator == '+':
            answers.append(str(int(first_num) + int(second_num)).rjust(length) + '    ')
        elif operator == '-':
            answers.append(str(int(first_num) - int(second_num)).rjust(length) + '    ')


  arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dash_line.rstrip()    
  if answer:
    answer_line = ''.join(answers)
    arranged_problems += '\n' + answer_line.rstrip() 
          
      
  return arranged_problems

