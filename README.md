# Instructions of what and how my program runs

This program has been designed to be as user friendly as possible.

A quick overview of my accounting program is that it receives a level(number) between 2-20 then due to the dictionary available, it is easy to determine how much can be gotten at that level.

Run down of my program:
   
   1. Accepts input of users name.
        1. Uses the name of the user throughout the code to create a more personal atmosphere/interference.
        2. Finally displays the name at the end of the end of code to highlight total of expenses incurred in a month, as well as what the highest expense incurred is.
  2. Accepts input of the present month.
         1. This makes it easier for user to create a report for different months and have an easy snapshot of what those expense and their sums each month are.
  3. I recently just added an extension of allowing this app/program to be useful to both those in my home country-Nigeria, and those in the United states.
       1. So, my code accepts either an NG or a US to clarify what country the user is trying to get a statement from, and also to make sure that if the country is Nigeria, then the pay rate would be converted to naira by multiplying by 450.
    
  3. Next, it requires the user to input their level (note, their level vcan only be between 2-20).
        1. This input serves as a key to get the value from the dictionary in income_data.py.
  4. Lists of possible expenses are then displayed so that user gets an idea of what expenses we are taking into account.
  5. My program goes ahead to highlight the individual expenses one after the other.
         1. It then gives the user the option to say 'y'-yes or 'n'-no.
              1. If the user inputs 'y' then my program then goes ahead to ask for an input in numbers only i.e without any entry of currency.
              2. If the user inputs 'n', then the program moves on to the next possible expense.
                  1. This same process goes to all five current expenses I have in my code.
  6. My program then gives the approximate total of expenses to the user.
  7. Next, a table is displayed with the snap shot of expenses and the values given by the user. 
     1. The table starts with gross pay which would be determined by the input level of the user.
  8. After the table, the net income is displayed to the user. 
     1. The next income is determined by subtracting the expenses from the gross pay.
     2. And if your expenses are more than your gross pay, there would be a minus.
  9. Lastly, according to my function 'highest_expense', I would be able to give the user their highest expense and advice a reduction if possible. 
    1. But before the above is given, I was able to create an extension that would require an inout from the user to specify if they are satisfied with their statement or not, or if they would want advice.
       1. If my user says 'y' for satisfied, then that's the end of using the app. 
       2. If they say 'n' for not satisfied, then my program would advise.