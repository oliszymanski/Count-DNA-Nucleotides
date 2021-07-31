#================================================
#   IMPORTS
#================================================



#================================================
#   CLASSES
#================================================

class CountNucleotides:

    def __init__(self):
        '''Initializing class'''

        return




    def test(self):

        return "Hello there!"




    def convert_to_string(self, ls_data):
        """
            input:
                ls_data:    list with data,

            output:
                ls_data:    list with elements converted to string;
        """

        ls_data = [ str( element ) for element in ls_data ]

        return ls_data




    def count_nucleotides(self, file_path):

        """
            input:
                file_path:      path of the file,

            output:
                dict_data:      dictionary of data about nucleotides;
        """


        ls_s_a = []         # lists for nucleotides
        ls_s_c = []
        ls_s_g = []
        ls_s_t = []

        dict_data = {}      # dictionary for data


        ls_data_file = open(file_path, 'r')                         # opening data fiel
        ls_fixed_data = self.convert_to_string(ls_data_file)        # every element (element is in every line) converted to string


        for line in ls_fixed_data:
            for element in line:

                if (element == 'A' or element == 'a'): ls_s_a.append(element)       # find adenine

                elif (element == 'C' or element == 'c'): ls_s_c.append(element)     # find cytosine

                elif (element == 'G' or element == 'g'): ls_s_g.append(element)     # find guanine

                elif (element == 'T' or element == 't'): ls_s_t.append(element)     # find thymine



        dict_data["A"] = len(ls_s_a)
        dict_data["C"] = len(ls_s_c)
        dict_data["G"] = len(ls_s_g)
        dict_data["T"] = len(ls_s_t)


        return dict_data




    def count_nucleotide_percentage(self, file_path):
        '''
            input:
                file_path:      path of the file with data,

            output:
                dict_percent_data:  dictionary with percentage data
        '''

        ls_s_a = []         # lists for nucleotides
        ls_s_c = []
        ls_s_g = []
        ls_s_t = []

        ls_all_data = []
        ls_nucleotide_percentage = []

        dict_nucleotide_percentage = {}      # dictionary for nucleotide percentage data


        ls_data_file = open(file_path, 'r')
        ls_fixed_data = self.convert_to_string(ls_data_file)

        for line in ls_fixed_data:
            for element in line:

                if (element == 'A' or element == 'a'): ls_s_a.append(element)       # find adenine

                elif (element == 'C' or element == 'c'): ls_s_c.append(element)     # find cytosine

                elif (element == 'G' or element == 'g'): ls_s_g.append(element)     # find guanine

                elif (element == 'T' or element == 't'): ls_s_t.append(element)     # find thymine



        ls_all_data.append(len(ls_s_a))
        ls_all_data.append(len(ls_s_c))
        ls_all_data.append(len(ls_s_g))
        ls_all_data.append(len(ls_s_t))

        all_data = sum(ls_all_data)         # number of all nucleotides



        for value in ls_all_data:
            percent_value = round( (  value / all_data ) * 100, 3  )      # counting percentage of every nucleotide
            ls_nucleotide_percentage.append( percent_value )



        dict_nucleotide_percentage["A"] = ls_nucleotide_percentage[0]
        dict_nucleotide_percentage["C"] = ls_nucleotide_percentage[1]
        dict_nucleotide_percentage["G"] = ls_nucleotide_percentage[2]
        dict_nucleotide_percentage["T"] = ls_nucleotide_percentage[3]


        return dict_nucleotide_percentage



#================================================
#   END OF FILE
#================================================