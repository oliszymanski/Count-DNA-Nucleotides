#================================================
#   IMPORTS
#================================================

import count_nucleotide as cn



#================================================
#   GLOBALS
#================================================

s_file_path = "src-data/Acetobacter_pasterianus_dna.txt"



#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):
    print("Hello")

    # testing the class
    search_nucleotides = cn.CountNucleotides()          # main object

    print(search_nucleotides.test())



    nucleotide_number = search_nucleotides.count_nucleotides(s_file_path)

    print("nucleotide_number =", nucleotide_number, "\n\n")


    nucleotide_percentage = search_nucleotides.count_nucleotide_percentage(s_file_path)
    print("nucleotide_percentage =", nucleotide_percentage)



#================================================
#   END OF FILE
#================================================