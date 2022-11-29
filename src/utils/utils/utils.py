import unicodedata, os

class Utils:
    """
    Class Utils have a set of functions to help the transformations
    in the ETL process.
    """
    @staticmethod
    def search_str(string:str, pattern:str):
        """
        This function returns a boolean value if the pattern if you want
        contains in string value
        Args:
            string (str): is the string value to search some pattern 
        value.
            pattern (str): is the pattern to search in the string
        Returns:
            boolean: returns a boolean value if the pattern is within a
        string value
        """
        if string.find(pattern) >= 0:
            return True
        else:
            return False

    @staticmethod
    def remove_accent(string:str):
        """
        This function removes the entire accent presents in a
        string
        Args:
            string (str): string value 
        Returns:
            None
        """
        return ''.join(c for c in unicodedata.normalize('NFD', string)
                        if unicodedata.category(c) != 'Mn')\
                            .strip()\
                            .replace(' ', '_')
    @staticmethod
    def list_path(path:str):
        """
        This function return a list of files according to path informed
        Args:
            path (str): the path of the directory with you want list
        recursively the files
        Returns:
            List: list of files
        """
        list_paths = []
        for root, directory, files in os.walk(path):
            for f in files:
                list_paths.append(os.path.join(root,f))
        return list_paths
 
                      