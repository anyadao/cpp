# -*- coding: cp1251 -*-
#	Find the result of the expression, having next three variables a,b,c: | a - b | /( a + b)?^3? - cos( c )
import math
var_a = 12
var_b = 55
var_c = 512
result_abc = math.fabs(var_a - var_b) / math.pow((var_a + var_b), 3) - math.cos(var_c)
print("The result of the expression | a - b | /( a + b)^3 - cos( c ), where a = %.2f, b = %.2f, c = %.2f is: %.2f"
      % (var_a, var_b, var_c, result_abc))
