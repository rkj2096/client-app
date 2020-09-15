import urwid
from app import Application
from app.utils import room_list, conversations_list


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

rooms = [
    {'name': u'Team Cobra', 'count': u"1+"},
    {'name': u'Kernel Lion', 'count': u"2+"},
    {'name': u'Desi Boys', 'count': u""}
]

conversations = [
    {'message': u"How are you?", 'by': u"aka", 'time': u'12:09PM'},
    {'message': u"I am fine", 'by': u"you", 'time': u'12:09PM'}
]

app = Application(rooms=room_list(rooms), selected_room='Desi Boys', conversations=conversations_list(conversations))
urwid.MainLoop(app.main(), palette=palette, unhandled_input=app.key_handler).run()