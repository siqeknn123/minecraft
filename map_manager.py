class MapManager:
    def __init__(self):
        self.model = "models/block.egg"
        self.texture = "textures/custom1.png"
        self.colors = [
            (255, 0, 132, 0.6),
            (82, 255, 0, 0.85),
            (0, 13, 255, 0.85),
            (255, 242, 0, 0.6)
        ]
        self.add_land_node()
        self.add_block((1, 1, 1))

    def add_land_node(self):
        self.land = render.attachNewNode("Land")

    def clear_land_node(self):
        self.land.removeNode()
        self.add_land_node()

    def add_block(self, possition: tuple) -> None:
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))        
        self.block.setColor(self.colors[0])
        self.block.setPos(possition)
        self.block.reparentTo(self.land)