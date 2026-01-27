import pygame


class Player:
    def __init__(self, window: pygame.Surface):
        self.window = window

        self.rect = pygame.Rect(0, 200, 30, 60)

        self.speed = 5
        self.jumpForce = 7.5
        self.velocity = pygame.Vector2(0, 0)
        self.isGround = False

        self.gravityForce = 0.2

        self.direction = 0

    def draw(self, camera):
        pygame.draw.rect(self.window, (0, 255, 0), (self.rect.x - camera.position.x, self.rect.y - camera.position.y, self.rect.width, self.rect.height))

    def apply_gravity(self):
        if not self.isGround:
            self.velocity.y += self.gravityForce

    def jump(self):
        if self.isGround:
            self.velocity.y = -self.jumpForce
            self.isGround = False

    def move(self, camera, walls:list):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LSHIFT]:
            self.speed = 9
        else:
            self.speed = 5

        self.velocity.x = (key_state[pygame.K_d] - key_state[pygame.K_q]) * self.speed

        if self.velocity.x > 0:
            self.direction = 0
        elif self.velocity.x < 0:
            self.direction = 1

        self.rect.x += self.velocity.x
        for wall in walls:
            wall.collide_x(self)

        self.rect.y += self.velocity.y
        for wall in walls:
            wall.collide_y(self)

        camera.follow(self)

        self.velocity.x = 0

    def attack(self):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_z]:
            print("haut")
            self.velocity.y = 0
        elif key_state[pygame.K_s] and not self.isGround:
            print("down")
            self.velocity.y += 5
        else:
            if self.direction == 0:
                print("right")
                self.rect.x += 500
            elif self.direction == 1:
                print("left")
                self.rect.x -= 500

    def update(self, camera, walls):
        self.draw(camera=camera)
        self.move(camera=camera, walls=walls)
        self.apply_gravity()
        self.isGround = False


