
class InventoryItem:
    def __init__(self, name, look, examine=None):
        self.name = name
        self.look = look
        if examine:
            self.examine = examine
        else:
            self.examine = "You see nothing special about the {}.".format(name)

class picture_of_moon(InventoryItem):
    def __init__(self):
        super().__init__(
            "PICTURE OF THE MOON",
            "You look at the PICTURE OF THE MOON. It is a picture of the moon.",
            "You see nothing special about the PICTURE OF THE MOON. It is a " \
            "picture of the moon."
        )


