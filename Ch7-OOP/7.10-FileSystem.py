import datetime import datetime


class Entry:
    def __init__(self, n, p):
        self.name = n
        self.parent = p
        self.created = datetime.now()
        self.last_updated = datetime.now()
        self.last_accessed = datetime.now()

    def delete(self):
        if not self.parent:
            return False
        return self.parent.delete_entry(self)

    def path(self):
        if not self.parent:
            return self.name
        else:
            return self.parent.path + "/" + self.name


class File(Entry):
    pass


class Directory(Entry):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kw)
        self.contents = []

    def delete_entry(self, entry):
        self.contents.remove(entry)

    def add_entry(self, entry):
        self.contents.add(entry)
