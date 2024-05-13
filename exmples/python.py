import os
from contextlib import contextmanager


@contextmanager
class NovaThemeExample:
    """Class doc string"""
    class_attribute_as_string = 'string value'

    def init(self):
        """Initialize an instance."""
        some_env_variable = 1
        some_other_env_variable = True
        some_other_variable = (1, 2, 3)
        os.environ['SOME_ENV_VAR'] = some_env_variable
        os.environ['SOME_OTHER_ENV_VAR'] = some_other_env_variable
        self.some_method()

    def some_method(self):
        print('calling some method')
