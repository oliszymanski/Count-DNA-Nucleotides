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




def count_percentage(ls_amounts):

    ls_percentages = []

    all_data = sum(ls_amounts)


    for element_num in ls_amounts:
         percentage = ( element_num / all_data )

         percentage = int( ( percentage * 100 ) )       # rounding up the data ( to 1/100 place )
         ls_percentages.append(percentage)


    # if (_DBG9_): print('s', sum(ls_percentages))        # dummy check

    return ls_percentages




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


        for line in ls_file:
            for element in line:

                if (element == 'A'): ls_a.append(element)       # find adenine

                elif (element == 'C'): ls_c.append(element)     # find cytosine

                elif (element == 'G'): ls_g.append(element)     # find guanine

                elif (element == 'T'): ls_t.append(element)     # find thymine


        a = len(ls_a)
        c = len(ls_c)
        g = len(ls_g)
        t = len(ls_t)

        ls_percentage = [a, c, g, t]

        per = count_percentage(ls_percentage)
        if(_DBG9_): print('per', per)

        return a, c, g, t



#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):
    a, c, g, t = Count('demo-data/Acetobacter_pasterianus_dna.txt')
    print('counted ls_a', a)
    print('counted ls_c', c)
    print('counted ls_g', g)
    print('counted ls_t', t)




#================================================
#   END OF FILE
#================================================