class UsernameDescriptor:
    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value):
        if len(value) > 1:
            instance._username = value
        else:
            raise ValueError("Username must have more than 1 character")