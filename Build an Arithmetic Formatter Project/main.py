def arithmetic_arranger(problems, show_answers=False):
    first_row = []
    second_row = []
    third_row = []
    fourth_row = []
    solution = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'


    for problem in problems:
        if '/' in problem or '*' in problem:
            return 'Error: Operator must be \'+\' or \'-\'.'
            break

        for operand in problem.split():
            if not operand.isdigit() and operand != '+' and operand != '-':
                return 'Error: Numbers must only contain digits.'
                break

            if operand.isdigit() and len(operand) > 4:
                return 'Error: Numbers cannot be more than four digits.'
                break

        current_operation = problem.split()
      
    
        max_value = max(len(current_operation[0]), len(current_operation[2]))
        min_value = min(len(current_operation[0]), len(current_operation[2]))
        third_row += ['-' * (max_value + 2)]
        
        print((max_value + 2) - min_value)
        first_number = (' ' * 2)+current_operation[0] if len(current_operation[0]) >= len(current_operation[2]) else  (' ' * ((max_value + 2) - min_value)) + current_operation[0]
        operation = current_operation[1]
        second_number = ' '+current_operation[2] if len(current_operation[2]) >= len(current_operation[0]) else (' ' * ((max_value + 1) - min_value)) + current_operation[2]
        
        
        first_row.append(first_number)

        second_row.append(operation + second_number) 
        
        
        if show_answers:
            max_value = max(len(current_operation[0]), len(current_operation[2]))
            if current_operation[1] == "+":
                result = str(int(current_operation[0]) + int(current_operation[2]))
                result = (' ' * ((max_value + 2) - len(result))) + result
            else:
                result = str(int(current_operation[0]) - int(current_operation[2]))
                result = (' ' * ((max_value + 2) - len(result))) + result
                
            fourth_row.append(result)
            
            
    solution = '    '.join(first_row) + '\n' + '    '.join(second_row) + '\n' + '    '.join(third_row)  
    if show_answers:
        solution +=   '\n' + '    '.join(fourth_row)
       
    return solution