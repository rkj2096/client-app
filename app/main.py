from app.widgets import *
from app.utils import *


class Application:
    def __init__(self, rooms, selected_room, conversations):
        self.selected_room = selected_room
        self.rooms_box = SimpleListBox(rooms)
        self.conversations_box = SimpleListBox(conversations)
        self.editor = EditBox(u"\u27A4" + " ", self)

    def add_conversation(self, conversation, align='left'):
        # backend code
        self.conversations_box.body.append(ConversationText(conversation, align))
        self.conversations_box.body.append(urwid.Divider())

    def add_room(self, room):
        # backend code
        self.rooms_box.body.append(room)
        self.rooms_box.body.append(('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2500'), 'line')))

    def main(self):
        board = urwid.Columns([
            ('weight', 3, urwid.Frame(
                body=self.conversations_box,
                header=urwid.Pile([
                    urwid.Text(('header', u"{}".format(self.selected_room))),
                    ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2501'), 'line'))
                ]),
                footer=urwid.LineBox(self.editor),
            )),
            ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2502'), 'line')),
            ('weight', 2, urwid.Frame(
                body=self.rooms_box,
                header=urwid.Pile([
                    urwid.Text(('header', u"Rooms")),
                    ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2501'), 'line'))
                ]),
            ))
        ],
            dividechars=1, focus_column=1
        )

        board = urwid.Padding(board, ('fixed left', 1), ('fixed right', 0))
        board = urwid.AttrWrap(board, 'body')
        board = urwid.LineBox(board)
        board = urwid.AttrWrap(board, 'line')
        return board

    def key_handler(self, key):
        if key in ('Q', 'q'):
            urwid.ExitMainLoop()
