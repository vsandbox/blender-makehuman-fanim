import sys
from importlib import reload


class FReload:
    @staticmethod
    def reload(module_names):
        for module_name in module_names:
            if module_name in sys.modules.keys():
                reload(sys.modules[module_name])