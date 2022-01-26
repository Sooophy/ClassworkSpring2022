print("This is the database module and python calls it {}".format(__name__))

import blood_calculator as bc
# from blood_calculator import*
# maynot remember where is come from if import*, always better to keep the module name, be readable!
# python overwrites the function with same name and only keep the most recent one


HDL_value = 55
classification = bc.check_HDL(HDL_value)
print("55 is {}".format(classification))