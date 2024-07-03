class Field:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Entity:

    def __init__(self, class_name, fields=None):
        if fields is None:
            fields = []
        self.fields = fields
        self.class_name = class_name

    def add_field(self, field: Field):
        self.fields.append(field)

    def add_field(self, name, type):
        self.fields.append(Field(name, type))


class EntityInstance:
    entities: dict[str, Entity] = {}

    def __init__(self, class_name):
        if class_name and self.entities.__contains__(class_name) is False:
            print(f'初始化parent_class_name: {class_name}')
            self.entities[class_name] = Entity(class_name)

    @classmethod
    def entity(cls, class_name):
        return cls.entities[class_name]

    @classmethod
    def get_entities(cls):
        return cls.entities

    @classmethod
    def clear(cls):
        cls.entities.clear()


