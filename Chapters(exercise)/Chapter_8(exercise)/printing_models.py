from printing_function import print_models, show_completed_models


unprinted_designs = ["phone case", "robot pendant", "dodecaherdon"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


import printing_function
printing_function.new_fun("Taimoor")

from printing_function import new_fun
new_fun("Taimoor (2)")

from printing_function import new_fun as fun
fun("Taimoor (3)")

import printing_function as g
g.new_fun("Taimoor (4)")    

from printing_function import *
new_fun("Taimoor (5)")