#discount= 0 is the default argument with the
#          value of zero if no discount argument pass on input
#           automatic default argument will choose

def net_prince(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)



print(net_prince(500))
print(net_prince(1000, 0.08))
print(net_prince(1000, 0.08, 0))

#
