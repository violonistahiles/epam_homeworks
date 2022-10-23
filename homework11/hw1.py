class SimplifiedEnum(type):
    """
    Metaclass for creation enum class from __keys tuple as class attribute
    """
    def __new__(mcs, name, bases, dct):
        cls_instance = super().__new__(mcs, name, bases, dct)

        for data in dct[f'_{name}__keys']:
            setattr(mcs, data, data)

        return cls_instance
