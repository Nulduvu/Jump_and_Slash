import pygame


class Wall:
    def __init__(self, window: pygame.Surface, rect: pygame.Rect):
        self.window = window
        self.rect = rect

    def draw(self, camera):
        pygame.draw.rect(self.window, (0, 0, 255), (self.rect.x - camera.position.x, self.rect.y - camera.position.y, self.rect.width, self.rect.height))

    def collide(self, entity):
        if entity.rect.y + entity.rect.h > self.rect.y and entity.rect.y < self.rect.y + self.rect.h:
            # left
            if self.rect.x <= entity.rect.x + entity.rect.w + entity.velocity.x <= self.rect.x + self.rect.w + entity.velocity.x:
                entity.rect.x = self.rect.x - entity.rect.w
            # right
            elif self.rect.x >= entity.rect.x - self.rect.w - entity.velocity.x >= self.rect.x - self.rect.w - entity.velocity.x:
                entity.rect.x = self.rect.x + self.rect.w

        if entity.rect.x + entity.rect.w > self.rect.x and entity.rect.x < self.rect.x + self.rect.w:
            # up
            if self.rect.y <= entity.rect.y + entity.rect.h + entity.velocity.y <= self.rect.y + self.rect.h + entity.velocity.y:
                entity.rect.y = self.rect.y - entity.rect.h
                entity.isGround = True
                entity.velocity.y = 0
            # down
            elif self.rect.y >= entity.rect.y - self.rect.h - entity.velocity.y >= self.rect.y - self.rect.h:
                print("touché")
                entity.rect.y = self.rect.y + self.rect.h
                if entity.velocity.y < 0:
                    entity.velocity.y = 0

    def update(self, camera):
        self.draw(camera=camera)
