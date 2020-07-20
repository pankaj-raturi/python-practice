#!/usr/bin/env python3

perHourCharges = 0.51

dailyCost = perHourCharges * 24
monthlyCost = dailyCost * 30

print( 'Cost to operate per day: ${:.2f}'. format(dailyCost) )
print( 'Cost to operate per month: ${:.2f}'. format(monthlyCost) )