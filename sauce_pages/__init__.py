import sys

sys.path.append('.')
#append which folder you want to access. in this case it's in different folder
sys.path.append('./sauce_test')

#this file is created to mend pytest detecting 'NoSuchModuleError'
#name of the file is fixed and can't be changed