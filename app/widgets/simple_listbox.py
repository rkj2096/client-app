import urwid


class SimpleListBox(urwid.ListBox):
    def __init__(self, list):
        self.list = list
        body = urwid.SimpleFocusListWalker([urwid.Pile(self.list)])
        super(SimpleListBox, self).__init__(body)

    def add_entry(self, entry):
        self.body.append(entry)

    def add_entries(self, entries):
        self.body += entries