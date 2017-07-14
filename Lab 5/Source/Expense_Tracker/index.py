
class MonthlyExpenses(object):

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    def ExpensesAdd(self):
        x = 0
        exp = []
        n = int(input("How many Expenses do You want Enter :"))
        for i in range(0,n):
            temp = int(input("Enter your expense "))
            exp.append(temp)
        print("You added following expenses :", exp)

        return sum(exp)

class ManageBudget(MonthlyExpenses):
    def __init__(self, name, budget, total_exp):
        MonthlyExpenses.__init__(self, name, budget)
        self.total_exp = total_exp

    def BudgetTracker(self):
        balence = 0
        balence = budget - total_exp

        if balence < budget:
            print("You have Money to Spend :", balence)
        else:
            print("You exceeded your Budget :", balence)

        return balence

# class FinalResult(ManageBudget,MonthlyExpenses):
#     def __init__(self):
#         super(ManageBudget,self).__init__()
#
#     def BalanceExplanation(self):
#         remain = 0
#         if total_exp <= (budget*0.5):
#             print("You have more than 50% of monthly budget left")
#         else:
#             print("You spended more than 50% of your monthly Budget")


name = input("Enter your Name: ")

bud = input("Enter Your Monthly Salary :")
budget = int(bud)
me = MonthlyExpenses(name, budget)
total_exp = me.ExpensesAdd()

manage_bud = ManageBudget(name, budget, total_exp)
rem_bal = manage_bud.BudgetTracker()

# FinalResult.BalanceExplanation()

print("Your Final results are ")
print("Your Monthly Budget is : ", budget)
print("Your Expenses till now : ", total_exp)
print("Your Remaining balence of budget this month : ", rem_bal)

