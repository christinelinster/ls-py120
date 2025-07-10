# Banner Class.

class Banner:
    def __init__(self, message, width = None):
        self.message = message
        if not width:
            self.width = len(self.message)
        else:
            self.width = max(width, len(self.message))

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {' ' * self.width} |"

    def _horizontal_rule(self):
        return f"+-{'-' * self.width}-+"

    def _message_line(self):
        empty_space = self.width - len(self.message)
        left_pad = empty_space // 2
        right_pad = empty_space - left_pad
        return f"| {' ' * left_pad}{self.message}{' ' * right_pad} |"
    

    # Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 59)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+