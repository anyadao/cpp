#	Find the result of the expression, having next 3 variables ( ln( 1 + c ) / -b )^4+ | a |
import math
var_a = 298
var_b = 175
var_c = 328

result_abc = math.pow((math.log(1 + var_c) / - var_b), 4) + math.fabs(var_a)
print("The result of the expression ( ln( 1 + c ) / -b )^4+ | a |, where a = %.2f,b = %.2f, c = %.2f is: %.2f "
      % (var_a, var_b, var_c, result_abc))
