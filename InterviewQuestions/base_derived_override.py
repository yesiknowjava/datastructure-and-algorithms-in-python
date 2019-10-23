#How do I call a method defined in a base class from a derived class that overrides it?
class Base:
    def method(self):
        print("I am base method")

class Derived(Base):
    def method(self):
        print("I am derived method")
        super().method()




a = Derived()
a.method()