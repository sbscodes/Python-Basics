from math import *
a=30.24
print(sqrt(a)) #sqrt funtion return the square root of the given number
print(pow(a,2)) #pow function is used to make a^n where a and n are paramters
print(pi)#return the constant pi value which is 3.14
print(e)#return the constant e
print(tau)#return the constant tau
"""
Trignometric Functions
acos,acosh,asin,asinh,atan,atan2,
atanh,cos,cosh,sin,sinh,tan,tanh
"""
print(acosh(90))
#Return the inverse hyperbolic cosine of x.
print(asinh(90))
#Return the inverse hyperbolic sine of x.
#print(atanh(90))
#Return the inverse hyperbolic tangent of x.
print(cosh(90))
#Return the hyperbolic cosine of x.
print(sinh(90))
#Return the hyperbolic sine of x.
print(tanh(90))
#Return the hyperbolic tangent of x.

'''Power and logarithmic functions'''
print(exp(1e-5)-1)
print(expm1(2e-5))

#rint(log(2[3,10]))
#With one argument, return the natural logarithm of x (to base e).

#With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).

print(log1p(9))
#Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.

print(log2(12))
#Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).

print(log10(15))
#Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).

print(ceil(23.5464567)) #print aproximate number eg.30.24 o/p-->31
print(copysign(10,-0))#copy the sign of second parameter to the first parameter
print(factorial(4))#return the factorial of the given number
print(gcd(12,48))#returns the greatest common divisor of the given numbers
print(gamma(20))#print the gamma value of the given number
print(remainder(4,3))#divide first no with second one and return the remainder of their division
print(degrees(1.5707963267948966))#Convert angle x from radians to degrees.
print(radians(90))#Convert angle x from degrees to radians.
print(isfinite(2.e453))#return number is finite or not

