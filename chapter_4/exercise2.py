#!/usr/bin/env python3

perHourCharges = 0.51
saving = 918
servers = 20

dailyCost = perHourCharges * 24
monthlyCost = dailyCost * 30

serversDailyCost = dailyCost * servers
serversMonthlyCose = monthlyCost * servers

# One server days from budget
oneWithSaving = saving / dailyCost

print( 'Cost to operate one server per day: ${:.2f}'. format(dailyCost) )
print( 'Cost to operate one server per month: ${:.2f}'. format(monthlyCost) )

print( 'Cost to operate twenty server per day: ${:.2f}'. format(serversDailyCost) )
print( 'Cost to operate twenty server per month: ${:.2f}'. format(serversMonthlyCose) )

print( 'Can operate one server with ${0:.2f}: for {1:.0f} days'. format(saving, oneWithSaving) )