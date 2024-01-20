import json
from test_json import entry



def print_with_indent(value, indent=0):
    indentation = " " * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def to_dict(self):
        res = {
            'title': self.title,
            'entries': [entry.to_dict() for entry in self.entries]
        }
        return res

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, value: dict):
        new_entry = cls(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.from_dict(item))  # Рекурсивный вызов from_dict
        return new_entry

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls.from_dict(data)

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    @classmethod
    def entry_from_json(cls, entry):
        pass

new_entry = Entry.entry_from_json(entry)

if __name__ == '__main__':
    new_entry = Entry.entry_from_json(entry)
    new_entry.print_entries()
    print(new_entry.json())

    new_entry1 = Entry.entry_from_json(new_entry.json())
    new_entry1.print_entries()

    json_str = new_entry.to_json()
    print(json_str)

    # Десериализация из JSON
    new_entry_from_json = Entry.from_json(json_str)
    new_entry_from_json.print_entries()
