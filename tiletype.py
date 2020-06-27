from Animation import Animation


class TileType:
    def __init__(self, sprite, accessible_to, accessible_from):
        if type(sprite) is Animation:
            self.anim = sprite
            self.sprite = None
        else:
            self.sprite = sprite
            self.anim = None
        
        self.accessible_to = accessible_to
        self.accessible_from = accessible_from
