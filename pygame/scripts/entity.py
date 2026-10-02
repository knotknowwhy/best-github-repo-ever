import pygame, pymunk


class PhysicsEntity:
    def __init__(self, main, pos, size=(23, 19)):
        self.space = main.space
        self.size = size

        self.body = pymunk.Body(mass=3, moment=float('inf'), body_type=pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, self.size, radius=0.5)
        self.shape.friction = 0.99
        self.shape.collision_type = 1

        self.space.add(self.body, self.shape)

        self.img = pygame.image.load("assets/crow.png").convert_alpha()
        self.img.set_colorkey((0, 0, 0))
        self.img = pygame.transform.scale(self.img, (115, 95))

        self.jumps = 1

    def update(self, movement=[False, False], jump=False):
        self.body.velocity = ((movement[0] - movement[1]) * -250, self.body.velocity.y)
        if jump and self.jumps > 0:
            self.jumps -= 1
            self.body.velocity = (self.body.velocity.x, -400)
        self.space.on_collision(1, 2, begin=self.collision)
        if self.body.position.x > 800 - 115:
            self.body.position = (800 - 115, self.body.position.y)
        elif self.body.position.x < 0:
            self.body.position = (0, self.body.position.y)

    def draw(self, screen: pygame.Surface, dir):
        if dir == "left":
            screen.blit(self.img, (*self.body.position, *self.img.get_size()))
        elif dir == "right":
            screen.blit(pygame.transform.flip(self.img, True, False), (*self.body.position, *self.img.get_size()))
        
    def collision(self, arbiter, space, data):
        self.jumps = 1