import urwid


chat_rooms = urwid.Pile([
    ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2501'), 'line')),
    urwid.Text([("message", "Team Dragon  "), ("sender", u"2+")]),
    ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2500'), 'line')),
    urwid.Text([("message", "Team Dragon  "), ("sender", u"2+")]),
    ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2500'), 'line')),
    urwid.Text([("message", "kernel team  "), ("sender", u"2+")]),
    ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2500'), 'line')),
])


conversations = urwid.Pile([
    urwid.Text([('sender', "aka:"), ('message', u" How are you? "), ('time', '10:10pm')]),
    urwid.Divider(),
    urwid.Text([("message", u" I am fine "), ('time', '10:01pm')], align='right'),
    urwid.Divider(),
])


class ConversationListBox(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleFocusListWalker([conversations])
        super(ConversationListBox, self).__init__(body)


class ChatRoomListBox(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleFocusListWalker([chat_rooms])
        super(ChatRoomListBox, self).__init__(body)


e = urwid.Edit(u"\u27A4"+" ")
e = urwid.LineBox(e)

chat_box = ConversationListBox()
room_box = ChatRoomListBox()
top = urwid.Pile([
        ('weight',3, urwid.Text(('header', u"Team Dragon"))),
        ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2501'), 'line'))
    ]
)


w = urwid.Columns([
        ('weight',3,urwid.Frame(
            chat_box,
            header=top,
            footer=e,
            focus_part='footer'
        )),
        ('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2502'), 'line')),
        ('weight',2, urwid.Frame(
            room_box,
            header= urwid.AttrWrap(urwid.Text(u"Rooms"), 'header'),
        ))
    ],
    dividechars=1, focus_column=1
)

w = urwid.Padding(w,('fixed left',1),('fixed right',0))
w = urwid.AttrWrap(w,'body')
w = urwid.LineBox(w)
w = urwid.AttrWrap(w,'line')


palette = [
        ('body', 'white', 'black'),
        ('header', 'white, bold', 'black'),
        ('room', 'white', 'black', 'standout'),
        ('message', 'light gray', 'black'),
        ('editor', 'white', 'black', 'standout'),
        ('line', 'white', 'black', 'standout'),
        ('dent', 'light gray', 'black'),
        ('sender', 'white, bold', 'black'),
        ('time', 'white, italics', 'black')
        ]

urwid.MainLoop(w, palette=palette).run()