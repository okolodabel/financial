from user_functions import add_expenses, highest_expense

def test_add_expenses():
    assert add_expenses(700, 500, 100, 200, 500, 100) == 2100
    assert add_expenses(1000, 600, 500, 0, 0, 0) == 2100
def test_highest_expense():
    assert highest_expense(500, 700, 100, 150, 600, 70) == 700
    assert highest_expense(2000, 5500, 600, 3000, 4500, 150) == 5500

    

if __name__ == "__main__":
    test_add_expenses()
    test_highest_expense()