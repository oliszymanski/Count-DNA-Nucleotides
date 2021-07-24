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

def Count(s_file_path : str):

        ls_a = []       # lists for inserting data
        ls_c = []
        ls_g = []
        ls_t = []

        s_file_path = open(s_file_path, 'rb')
        if (_DBG9_): print('s_file_path', s_file_path, '\n\n')


        return s_file_path



#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):
    counted = Count('demo-data/Acetobacter_pasterianus_dna.txt')




#================================================
#   END OF FILE
#================================================