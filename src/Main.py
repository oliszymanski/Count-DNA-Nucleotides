#================================================
#   IMPORTS
#================================================

import count_nucleotide as cn



#================================================
#   GLOBALS
#================================================

s_file_path = "src-data/Acetobacter_pasterianus_dna.txt"
s_second_file_path = "src-data/Escherichia_phage.txt"
s_third_file_path = "src-data/sars-cov-2.txt"


#================================================
#   MAIN
#================================================

if (__name__ == '__main__'):
    print("Hello")

    # testing the class
    search_nucleotides = cn.CountNucleotides()          # main object

    print(search_nucleotides.test())



    nucleotide_number = search_nucleotides.count_nucleotides(s_file_path)       # acetobacter genome
    print("nucleotide_number =", nucleotide_number, "\n\n")


    nucleotide_percentage = search_nucleotides.count_nucleotide_percentage(s_file_path)
    print("nucleotide_percentage =", nucleotide_percentage, "\n\n\n\n")





    second_nucleotides_number = search_nucleotides.count_nucleotides(s_second_file_path)    # Escherichia genome
    print("second_nucleotides_number =", second_nucleotides_number, "\n\n")


    second_nucleotide_percentage = search_nucleotides.count_nucleotide_percentage(s_second_file_path)
    print("second_nucleotides_number =", second_nucleotide_percentage, "\n\n\n\n")





    third_nucleotide_number = search_nucleotides.count_nucleotides(s_third_file_path)
    print("third_nucleotide_number =", third_nucleotide_number, "\n\n")


    third_nucleotide_percentage = search_nucleotides.count_nucleotide_percentage(s_third_file_path)
    print("third_nucleotide_percentage =", third_nucleotide_percentage, '\n\n\n\n')





    # testing the display chart
    dict_nucleotide_number = search_nucleotides.get_nucleo_dict(s_third_file_path)
    print("dict_nucleotide_number =", dict_nucleotide_number, '\n')

    search_nucleotides.display_nucleotide_chart(dict_nucleotide_number)




#================================================
#   END OF FILE
#================================================