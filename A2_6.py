import random
code4 = ""
code3 = ""
for i in range(3):
    code3 += str(random.randint(0, 9))

for i in range(4):
    code4 += str(random.randint(1, 6))

print(f"3-digit code is {code3}")
print(f"4-digit code:is {code4}")