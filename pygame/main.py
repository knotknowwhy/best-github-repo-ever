import pygame, pymunk, sys
from scripts.entity import PhysicsEntity

class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.screen.set_alpha(255)
        self.clock = pygame.Clock()
        self.space = pymunk.Space()
        self.space.gravity = (0, 700)

        self.player = PhysicsEntity(self, (50, 50), (23, 19))

        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, (0, 50), (800, 50), 5)
        floor_shape.friction = 0.62
        floor_shape.collision_type = 1

        self.movemant = [False, False]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: self.movement[0] = True
                    if event.key == pygame.K_d: self.movement[1] = True
                if event.key == pygame.KEYUP:
                    if event.key == pygame.K_a: self.movement[0] = False
                    if event.key == pygame.K_d: self.movement[1] = False
            


            self.screen.fill((150, 150, 150, 255))

            self.player.draw(self.screen)

            pygame.display.flip()
            self.space.step(1.0/60.0)
            self.clock.tick(60)

if __name__ == "__main__":
    Main().run()