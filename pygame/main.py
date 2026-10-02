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

        self.movement = [False, False]
        self.jump = False

        self.font = pygame.font.SysFont("Arial", 24)
        self.font_img = self.font.render("Kraaa", antialias=False, color=(15, 15, 15))
        self.say_kraa = False

        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, (-50, 300), (850, 300), 10)
        floor_shape.friction = 0.99
        floor_shape.collision_type = 2
        self.space.add(floor_shape, floor_body)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: self.movement[0] = True
                    if event.key == pygame.K_d: self.movement[1] = True
                    if event.key == pygame.K_SPACE:self.jump = True
                if event.type == pygame.KEYUP:
                    self.say_kraa = False
                    if event.key == pygame.K_a: self.movement[0] = False
                    if event.key == pygame.K_d: self.movement[1] = False
                    if event.key == pygame.K_SPACE: self.jump = False

            self.player.update(self.movement, self.jump)

            if self.movement[0] or self.movement[1] or self.jump:
                self.say_kraa = True

            self.screen.fill((36, 137, 178))
            pygame.draw.rect(self.screen, (149, 86, 59), (0, 300, 800, 300))
            pygame.draw.rect(self.screen, (106, 190, 48), (0, 300, 800, 200))
            self.player.draw(self.screen)
            
            if self.say_kraa:
                self.screen.blit(self.font_img, (int(self.player.body.position.x) - 50, int(self.player.body.position.y)))
            
            pygame.display.flip()
            self.space.step(1.0/60.0)
            self.clock.tick(60)

if __name__ == "__main__":
    Main().run()