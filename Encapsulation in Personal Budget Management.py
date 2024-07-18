# A class for creating a budget category with the amount to allocate toward that category
class BudgetCategory:
    def __init__(self, name, allocation):
        self.__category_name = name
        self.__allocated_budget = allocation

    # Getter for current budget category name
    def get_category_name(self):
        return self.__category_name

    # Setter set new budget category name
    def set_category_name(self, new_name):
        self.__category_name = new_name

    # Getter for the current allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter to set new allocated budget
    def set_allocated_budget(self, new_allocation):
        self.__allocated_budget = new_allocation

    # Method to add an expense to the category
    def add_expense(self, amount):
        self.__allocated_budget = self.__allocated_budget + amount

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"The budget for {self.__category_name} is ${self.__allocated_budget}.")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()