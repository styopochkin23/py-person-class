class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_object = []
    for person in people:
        p = Person(person["name"], person['age'])
        person_object.append(p)

    for person in people:
        current = Person.people[person['name']]
        if 'wife' in person and person['wife'] is not None:
            current.wife = Person.people[person['wife']]
        if 'husband' in person and person['husband'] is not None:
            current.husband = Person.people[person['husband']]

    return person_object
