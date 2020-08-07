import importlib
from typing import Any


def instantiate_class_from_path(path: str, instance_of: Any = None) -> Any:
    """
    Given a dotted path, loads the module and instantiates the class instance
    if a subclass is provided, will enforce the class instantiated is infact as subclass of this type
    :param path: the path to attempt to find the module (and subsequently the class)
    :param instance_of: an expected class to compare isinstance on with the found class
    :return: the instance of the class
    """
    try:
        module_name, class_name = path.rsplit(".", 1)
        loaded_module = importlib.import_module(module_name)
        cfg_subclass = getattr(loaded_module, class_name)()
        if instance_of and not isinstance(cfg_subclass, instance_of):
            raise ValueError(
                f"Unable to load a class of: {type(instance_of)} from: {path}"
            )
        return cfg_subclass
    except (ModuleNotFoundError, AttributeError) as error:
        raise error from None
