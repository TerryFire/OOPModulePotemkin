class PinDescriptor:
    def __get__(self, instance, owner):
        return instance._pin_code

    def __set__(self, instance, value):
        if len(value) == 4:
            instance._pin_code = value
        else:
            raise ValueError("PIN must be 4 characters long")