#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.11 MPG
"""

"""Calculating miles per gallon."""
total_miles = 0
total_gallons = 0

gallons = float(input('Enter the gallons used (-1 to end): '))

while gallons != -1:
    miles = float(input('Enter the miles driven: '))

    total_miles += miles
    total_gallons += gallons

    if gallons != 0:
        miles_per_gallon = miles / gallons
        print(f'The miles/gallon for this tank was {miles_per_gallon}')           

    gallons = float(input('Enter the gallons used (-1 to end): '))

if total_gallons != 0:
    total_miles_per_gallon = total_miles / total_gallons
    print(f'Total MPG so far: {total_miles_per_gallon}')