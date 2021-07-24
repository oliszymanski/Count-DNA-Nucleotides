#================================================
#   IMPORTS
#================================================

import nucleotide_count as nc



#================================================
#   GLOBALS
#================================================

s_file_path = 'demo-data/Acetobacter_pasterianus_dna.txt'




#================================================
#   MAIN
#================================================


if (__name__ == '__main__'):

    find_nucleoid_data = nc.CountNucleotides()   # create main object

    ls_amount, ls_amount_percentage = find_nucleoid_data.count_amount(s_file_path)      # get all data


    # count how many nucleotides are there in the code (adenine guanine cytosine and thymine)
    print("Nucleoids amount", ls_amount)

    # count percentage of nucleotides in the genetic sequence
    print("percentage of nucleoids", ls_amount_percentage)



#================================================
#   END OF FILE
#================================================