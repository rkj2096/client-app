import urwid


class RoomText(urwid.Text):
    def __init__(self, room):
        self.room = [
            ('message', u" {} ".format(room['name'])),
            ('sender', room['count'])
        ]
        super(RoomText, self).__init__(self.room)


class ConversationText(urwid.Text):
    def __init__(self, conversation, align='left'):
        self.conversation = [
            ('sender', conversation['by']),
            ('message', u" {} ".format(conversation['message'])),
            ('time', conversation['time'])
        ]
        super(ConversationText, self).__init__(self.conversation, align=align)