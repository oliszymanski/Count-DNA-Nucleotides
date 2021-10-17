#================================================
#   IMPORTS
#================================================



#================================================
#   CLASSES
#================================================

class CountNucleotides:

    def __init__(self):     # for initializing class

        return




    def convert_elements_to_string(self, ls):

        ls = [str(element) for element in ls]

        return ls




    def count_percentage(self, ls_amounts):

        ls_percentages = []

        all_data = sum(ls_amounts)


        for element_num in ls_amounts:
            percentage = ( element_num / all_data )

            percentage = int( ( percentage * 100 ) )       # rounding up the data ( to 1/100 place )
            ls_percentages.append(percentage)


        return ls_percentages




    def count_amount(self, s_file_path):

        ls_a_amount = []       # lists for inserting data
        ls_c_amount = []
        ls_g_amount = []
        ls_t_amount = []

        ls_data_amount = []



        ls_file = open(s_file_path, 'r')       # read the file in binary

        ls_file = self.convert_elements_to_string(ls_file)


        for line in ls_file:
            for element in line:

                if (element == 'A'): ls_a_amount.append(element)       # find adenine

                elif (element == 'C'): ls_c_amount.append(element)     # find cytosine

                elif (element == 'G'): ls_g_amount.append(element)     # find guanine

                elif (element == 'T'): ls_t_amount.append(element)     # find thymine


        ls_data_amount.append(len(ls_a_amount))     # adding the amount of adenine, guanine etc.
        ls_data_amount.append(len(ls_c_amount))
        ls_data_amount.append(len(ls_g_amount))
        ls_data_amount.append(len(ls_t_amount))

        ls_percentage = self.count_percentage(ls_data_amount)


        return ls_data_amount, ls_percentage




    def count_sequences(self, ls_meta : list, sequence):

        """
            input:
                ls_meta :       meta data which theoretically contains the searched sequence,
                sequence :      searched sequence;

            output:

        """

        ls_second = []

        for val in ls_meta:
            if ( ls_meta[ ls_meta[val] : len(sequence) ] == sequence  ):        # checking if metadata contains the sequence (going from i-th element to )
                ls_second.append(True)

            else:
                ls_second.append(False)


        return  None



#================================================
#   END OF FILE
#================================================