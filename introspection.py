class Obj:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def age(self):
        age = 2024 - self.birth
        return age


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return info


number_info = introspection_info(42)
print(number_info)
a = Obj('Vasya', 1999)
number_info2 = introspection_info(a)
print(number_info2)
