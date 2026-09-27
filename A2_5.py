from typing import Literal

talent=float(input("please enter  talent"))
pound = float(input("please enter  pound"))
lot = float(input("please enter  lot"))
h1 = talent * 20
h2 = h1 * 32 + pound * 32
h3 = h2 * 13.3 + lot*13.3
calc1= h3 //1000
calc2= h3%1000
print(f"the weight in modern units: {calc1}kg and {calc2:.2f}g")