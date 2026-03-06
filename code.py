num1=10
num2=20
operator='+'
if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='/':
    result=num1/num2
elif operator=='*':
    result=num1*num2
else:
    result="Invalid operator"
print(result)