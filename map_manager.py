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

    def add_land_node(self):
        self.land = render.attachNewNode("Land")

    def clear_land_node(self):
        self.land.removeNode()
        self.add_land_node()

    def set_color(self, z: int):
        if z <= 3:
            return self.colors[z]
        else:
            return self.colors[0]

    def add_block(self, possition: tuple) -> None:
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))     
        color = self.set_color(possition[2])   
        self.block.setColor(color)
        self.block.setPos(possition)
        self.block.reparentTo(self.land)

    def load_map(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line_lst = line.split(" ")
                for z in line_lst:
                    for z0 in range(int(z) + 1):
                        block = self.add_block((x, y, z0))
                    x += 1
                y += 1
        return x, y
