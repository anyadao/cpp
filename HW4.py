# -*- coding: cp1251 -*-
#4.	Find the result of the expression, having next 3 variables a,b,c: (a - b * c ) / ( a + b ) % c

var_a = 5
var_b = 4
var_c = 23
result_var_abc = (var_a - var_b * var_c) / (var_a + var_b) % var_c
print("The result of the expression (a - b * c ) / ( a + b ) %% c, where a = %.2f, b = %.2f, c = %.2f is: %.2f"
      % (var_a, var_b, var_c, result_var_abc))
