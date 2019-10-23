class Character:
    def __init__(self, name="", **kwargs):
        if name:
            self.name = name
        else:
            raise ValueError("Name is required")
        for key, value in kwargs.items():
            setattr(self, key, value)