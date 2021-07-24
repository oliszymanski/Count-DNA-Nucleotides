#================================================
#   IMPORTS
#================================================



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = False						# Errors
_DBG1_ = False						# Warnings
_DBG8_ = False                      # Other issues
_DBG9_ = True						# Standard debug



#================================================
#   FUNCTIONS
#================================================

def convert_elements_to_string(ls):

        ls = [str(element) for element in ls]

        return ls



def Count(s_file_path):

        ls_a = []       # lists for inserting data
        ls_c = []
        ls_g = []
        ls_t = []

        ls_file = open(s_file_path, 'r')       # read the file in binary
        if (_DBG9_): print('ls_file:', ls_file, '\n')

        ls_file = convert_elements_to_string(ls_file)

        for element in ls_file:
            if (_DBG9_): print(element)

        return



#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):
    counted = Count('demo-data/Acetobacter_pasterianus_dna.txt')




#================================================
#   END OF FILE
#================================================