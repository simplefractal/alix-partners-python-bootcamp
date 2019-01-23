import math


def compute_breakeven_point(fixed_costs, unit_cost, unit_income, num_consultants=None):
    if num_consultants:
        total_costs = fixed_costs + num_consultants * unit_cost
        unit_profit = unit_income  # since cost already accounted for
    else:
        total_costs = fixed_costs

        # Get profit per consultant
        unit_profit = unit_income - unit_cost

    # See how many unit profits are needed to cover total_costs
    return math.ceil(total_costs / unit_profit)


print(compute_breakeven_point(100000, 18000, 25000)) # BEP
print(compute_breakeven_point(100000, 18000, 25000, num_consultants=100)) # BEP given staff of 100
print(compute_breakeven_point(100000, 18000, 25000, num_consultants=10)) # BEP given staff of 10