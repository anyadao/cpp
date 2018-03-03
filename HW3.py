# -*- coding: cp1251 -*-
#3.	Find the result of the expression, having next three variables a,b,c: ( a + b ) / 12 * c % 4 + b

var_a = 50
var_b = 32
var_c = 98
result_var_abc = (var_a + var_b) / 12 * var_c % 4 + var_b
print("The result of the expression (a + b) / 12 * c %% 4 + b, where a = %.2f, b = %.2f, c = %.2f is: %.2f" 
      % (var_a, var_b, var_c, result_var_abc))
