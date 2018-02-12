import os
import tkinter
from tkinter.filedialog import Open, Directory, SaveAs

# Find the cureent working directory.
here = os.getcwd()


def conditional_kwargs(**nkwargs):
    """Returns function with conditionally supplied kwargs.

    This decorator is intended for use with higher level functions that
    act more like wrappers for other functions or classes.
    """
    def decorator(some_function):
        def wrapper(nkwargs=nkwargs, *args, **kwargs):
            for k, v in nkwargs.items():
                if k not in kwargs:
                    kwargs[k] = v
                else:
                    pass
            return some_function(*args, **kwargs)
        return wrapper
    return decorator


def root_topmost():
    """Return root as a withdrawn topmost window.
    """
    root = tkinter.Tk()
    # Hide the main window.
    root.withdraw()
    root.call('wm', 'attributes', ".", '-topmost', True)
    return root


class filedialog(object):
    """Jupyter Notebook freindly tkinter filedialogs."""
    # The following functions have been modified from the following;

    # https://github.com/python/cpython/blob/3.6/Lib/tkinter/filedialog.py

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def askopenfilename(**options):
        "Ask for a filename to open."
        return Open(**options).show()

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def asksaveasfilename(**options):
        "Ask for a filename to save as."
        return SaveAs(**options).show()

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def askopenfilenames(**options):
        """Ask for multiple filenames to open.
        Returns a list of filenames or empty list if
        cancel button selected
        """
        options["multiple"] = 1
        return Open(**options).show()

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def askopenfile(mode="r", **options):
        "Ask for a filename to open, and returned the opened file"

        filename = Open(**options).show()
        if filename:
            return open(filename, mode)
        return None

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def askopenfiles(mode="r", **options):
        """Ask for multiple filenames and return the open file
        objects
        returns a list of open file objects or an empty list if
        cancel selected
        """

        files = askopenfilenames(**options)
        if files:
            ofiles = []
            for filename in files:
                ofiles.append(open(filename, mode))
            files = ofiles
        return files

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def asksaveasfile(mode="w", **options):
        "Ask for a filename to save as, and returned the opened file"

        filename = SaveAs(**options).show()
        if filename:
            return open(filename, mode)
        return None

    @staticmethod
    @conditional_kwargs(parent=root_topmost(), initialdir=here)
    def askdirectory(**options):
        "Ask for a directory, and return the file name"
        return Directory(**options).show()
