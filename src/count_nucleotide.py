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

        ls_s_a = []
        ls_s_c = []
        ls_s_g = []
        ls_s_t = []

        ls_main_data = []

        ls_data_file = open(file_path, 'r')
        ls_fixed_file = self.convert_to_string(ls_data_file)        # every element (element is in every line) converted to string

        for line in ls_fixed_file:
            for element in line:

                if (element == 'A'): ls_s_a.append(element)       # find adenine

                elif (element == 'C'): ls_s_c.append(element)     # find cytosine

                elif (element == 'G'): ls_s_g.append(element)     # find guanine

                elif (element == 'T'): ls_s_t.append(element)     # find thymine



        dict_data = {"A" : len(ls_s_a)  , "C" : len(ls_s_c) , "G" : len(ls_s_g) , "T" : len(ls_s_t) }          # dictionary of data (symbol of nucleotide is key and value is data)



        return dict_data




    def count_nucleotide_percentage(self, ls_amount):

        # some code


        dict_percent_data = {}

        return dict_percent_data



#================================================
#   END OF FILE
#================================================