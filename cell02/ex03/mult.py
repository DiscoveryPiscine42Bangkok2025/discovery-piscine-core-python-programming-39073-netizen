fn = int(input("Enter the first number: " \
""))
ln = int(input("Enter the second number: " \
""))

result = fn * ln 

print(fn, "*",ln, "=", fn * ln)

if (result == 0): 
    print("The result is positive and negative.")
if (result > 0): 
    print("The result is positive.")
if (result < 0): 
    print("The result is negative.")
