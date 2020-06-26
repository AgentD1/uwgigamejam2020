class TileType:
    def __init__(self, sprite, accessible_to, accessible_from):
        self.sprite = sprite
        self.accessible_to = accessible_to
        self.accessible_from = accessible_from
