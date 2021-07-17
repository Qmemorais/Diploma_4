import sys
import main_console_work_interface as mcwi
import work_with_csv as wws

##load "Welcome"
mcwi.first_load()

##load csv and try to read
try:
    data_from_csv = wws.read_csv()
except:
    ##if we don`t have csv
    print("Something go wrong when we try to load csv. Please try again")
    sys.exit()
mcwi.main_interface(data_from_csv)