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



    def Count(self, s_file_path):

        ls_a = []       # lists for inserting data
        ls_c = []
        ls_g = []
        ls_t = []

        ls_file = open(s_file_path, 'r')       # read the file in binary

        ls_file = self.convert_elements_to_string(ls_file)


        return



#================================================
#   END OF FILE
#================================================