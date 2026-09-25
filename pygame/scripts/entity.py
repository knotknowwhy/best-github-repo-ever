import pygame, pymunk


class PhysicsEntity:
    def __init__(self, main, pos, size=(23, 19)):
        self.space = main.space

        self.body = pymunk.Body(mass=50, moment=10, body_type=pymunk.Body.DYNAMIC)
        self.shape = pymunk.Poly.create_box(self.body, size)

        self.space.add(self.body, self.shape)

        self.img = pygame.image.load("assets/crow.png").convert_alpha()
        self.img.set_colorkey((0, 0, 0))
        self.img = pygame.transform.scale(self.img, (115, 95))

    def draw(self, screen: pygame.Surface):
        screen.blit(self.img, (*self.body.position, *self.img.get_size()))