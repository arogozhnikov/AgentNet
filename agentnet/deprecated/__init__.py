__doc__= """Here lie parts of architecture that is no longer supported and will be removed in one of the following versons"""


import warnings
class deprecated:
    def __init__(self,new_name=None,removed_after="next major patch"):
        self.new_name = new_name
        self.removed_after = removed_after
    def __call__(self,func):
        """This is a decorator which can be used to mark functions
        as deprecated. It will result in a warning being emmitted
        when the function is used."""
        def newFunc(*args, **kwargs):
            warning = "%s is deprecated and will be removed in %s. " % (func.__name__,self.removed_after)
            if self.new_name is not None:
                warning += "This functionality has been replaced with %s." % self.new_name
            warnings.warn(warning,
                          category=DeprecationWarning)
            return func(*args, **kwargs)
        newFunc.__name__ = func.__name__
        newFunc.__doc__ = func.__doc__
        newFunc.__dict__.update(func.__dict__)
        return newFunc
