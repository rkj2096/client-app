import urwid
from datetime import datetime


class EditBox(urwid.Edit):
    def __init__(self, prompt, app):
        self.app = app
        super(EditBox, self).__init__(prompt)

    def keypress(self, size, key):
        if key != 'enter':
            return super(EditBox, self).keypress(size, key)
        elif len(self.get_text()[0].lstrip('u"\u27A4" + " "')) > 0:
            conversation = {
                'by': "you",
                'message': self.get_text()[0].lstrip('u"\u27A4" + " "'),
                'time': datetime.now().strftime("%-I:%M%p"),
                'date': datetime.now().strftime("%d/%m/%Y")
            }
            self.set_edit_text("")
            self.app.add_conversation(conversation, align='right')
            self.app.conversations_box.set_focus(
                len(self.app.conversations_box.body) - 1
            )