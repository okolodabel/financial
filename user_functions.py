def add_expenses(expense_1, expense_2, expense_3, expense_4, expense_5, expense_6):

  '''Returns the sum of all the expenses given by the user.
    
     Args:
       inputs of user for different possible expenses they have. Takes six expenses input and returns the sum of all six 
    
     Returns:
        An integer that represents the sum of all six integers 
        for expenses not incurred by the user, the program takes that as a 0. 
  
     Examples:
       add_expenses(700, 500, 100, 200, 500, 100) = 2100
       add_expenses(1000, 600, 500, 0, 0, 0) = 2100   
    '''
  addition = expense_1 + expense_2 + expense_3 + expense_4 + expense_5 + expense_6
  
  return addition

def highest_expense(expense_1, expense_2, expense_3, expense_4, expense_5, expense_6):

  '''Returns the highest of all the expenses given by the user.
    
     Args:
       inputs of user for different possible expenses they have. Takes six expenses input and returns the highest of all three.
    
     Returns:
       An integer that represents the highest of all six integers 
       for expenses not incurred by the user, the program takes that as a 0 . 
        
     Examples:
       highest_expense(500, 700, 100, 50, 600, 150) = 700
       highest_expense(2000, 5500, 600, 3000, 4500, 600) = 5500 
   '''
  
  highest_value = max(expense_1, expense_2, expense_3, expense_4, expense_5, expense_6)

  
  return highest_value