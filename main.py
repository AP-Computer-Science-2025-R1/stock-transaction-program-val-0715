#at purchase
number_of_shares= 1000
per_share= 32.87
total= number_of_shares * per_share
commission= .5*total
joe_total= total-commission

#after selling
new_per_share= 33.92
new_total= number_of_shares*new_per_share
new_commission= .02*new_total
new_joe_total= new_total-new_commission

#profit
result =  joe_total - new_joe_total 

print("Joe originally paid $", total, " for the stock.")
print("Joe paid his stockbroker $", commission, " in commission.")
print("Joe had $", joe_total, "leftover.")
print("Joe sold the stock for $", new_total,".")
print("Joe paid his stock broker $", new_commission, "in commission again.")
print("Joe had a new total of $", new_joe_total, "left over.")

print(result)


print()
if  result > 0:
    print("Joe made profit")
else:
    print("Joe lost money")