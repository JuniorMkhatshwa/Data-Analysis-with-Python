# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from pprint import pprint

from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
pprint(mean_var_std.calculate([i for i in range(0, 9)]))
{'max': [[6, 7, 8], [2, 5, 8], 8],
 'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 'min': [[0, 1, 2], [0, 3, 6], 0],
 'standard deviation': [[2.449489742783178,
                         2.449489742783178,
                         2.449489742783178],
                        [0.816496580927726,
                         0.816496580927726,
                         0.816496580927726],
                        2.581988897471611],
 'sum': [[9, 12, 15], [3, 12, 21], 36],
 'variance': [[6.0, 6.0, 6.0],
              [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
              6.666666666666667]}
# Run unit tests automatically
main(module='test_module', exit=False)