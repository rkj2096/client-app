import urwid
from app.widgets import RoomText, ConversationText


def room_list(rooms):
    formatted_rooms = []
    for room in rooms:
        formatted_rooms.append(RoomText(room))
        formatted_rooms.append(('fixed', 1, urwid.AttrWrap(urwid.SolidFill(u'\u2500'), 'line')))
    return formatted_rooms

def conversations_list(conversations):
    formatted_conversations = []
    for conversation in conversations:
        align = 'right' if conversation['by'] == 'you' else 'left'
        formatted_conversations.append(ConversationText(conversation, align=align))
        formatted_conversations.append(urwid.Divider())
    return formatted_conversations