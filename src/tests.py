#================================================
#   IMPORTS
#================================================

import count_nucleotide as cn



#================================================
#   GLOBALS
#================================================

s_file_path = "src-data/Acetobacter_pasterianus_dna.txt"        # main file path



#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):

    search_nucleotides = cn.CountNucleotides()          # create object

    search_nucleotides.count_nucleotides(s_file_path)







#================================================
#   END OF FILE
#================================================