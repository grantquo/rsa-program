######################################################################
import sys
from os.path import exists
def assertexists(filename: str):
    """ This asserts that a file exists, and issues an error message
        and exits if the file does not exist.
        Parameters:
            filename: the filename to be tested for existence
        Returns:
            nothing
    """
    try:
        assert exists(filename)
    except AssertionError:
        print(f"AssertionError: File '{filename}' does not exist.")
        sys.exit()


