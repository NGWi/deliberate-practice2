# https://learning.edx.org/course/course-v1:edX+DemoX.1+2T2019
"""
We are searching for the smallest monthly payment such that we can pay off the entire balance of a loan within a year.

The following values might be useful when writing your solution

Monthly interest rate
= (Annual interest rate) / 12
Monthly payment lower bound
= Balance / 12
Monthly payment upper bound
= (Balance x (1 + Monthly interest rate)12) / 12
The following variables contain values as described below:

balance
- the outstanding balance on the credit card
annualInterestRate
- annual interest rate as a decimal
Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent such that we can pay off the debt within a year.

Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers. If you get a message that states "Your submission could not be graded. Please recheck your submission and try again. If the problem persists, please notify the course staff.", check to be sure your code doesn't take too long to run.

The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.
"""
def increase(bal, mon_rate, mons, payment):
    for _mon in range(mons):
        bal = (bal - payment) * (1 + mon_rate)
    return bal

def adjustment(end_bal, mon_rate, mons):
    lower_bound = end_bal/mons
    upper_bound = (end_bal * (1 + mon_rate)**mons) / mons
    return (lower_bound + upper_bound)/2

def search(bal, mon_rate, mons):
    payment = 0
    end_bal = bal
    while abs(end_bal) >= 0.06:
        payment += adjustment(end_bal, mon_rate, mons)
        end_bal = increase(bal, mon_rate, mons, payment)
        # print(payment, end_bal)
    return round(payment, 2)

def solution(balance, annualInterestRate):
    mon_rate = annualInterestRate/12
    # print(mon_rate)
    return search(balance, mon_rate, 12)

print(solution(balance, annualInterestRate))

print(solution(100, 0.5))
print(solution(320000, 0.2))
print(solution(999999, 0.18))

