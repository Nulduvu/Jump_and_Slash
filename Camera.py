import pygame

class Camera:
    def __init__(self, window: pygame.Surface):
        self.window = window

        self.position = pygame.Vector2(0, 0)

        self.cameraSpeed = 5
        self.cameraOffset = 5
        self.cameraLimit = 20

    def follow(self, player):
        if player.velocity.x != 0:
            self.position.x += player.velocity.x * 2
        elif self.position.x < (player.rect.centerx - self.window.get_width() // 2) - self.cameraOffset:
            self.position.x += self.cameraSpeed
        elif self.position.x > (player.rect.centerx - self.window.get_width() // 2) + self.cameraOffset:
            self.position.x -= self.cameraSpeed

        if player.velocity.y != 0:
            self.position.y += player.velocity.y * 2
        elif self.position.y < (player.rect.centery - self.window.get_height() // 2) - self.cameraOffset:
            self.position.y += self.cameraSpeed
        elif self.position.y > (player.rect.centery - self.window.get_height() // 2) + self.cameraOffset:
            self.position.y -= self.cameraSpeed

        if self.position.x < player.rect.centerx - self.cameraLimit - self.window.get_width() // 2:
            self.position.x = player.rect.centerx - self.cameraLimit - self.window.get_width() // 2
        elif self.position.x > player.rect.centerx + self.cameraLimit - self.window.get_width() // 2:
            self.position.x = player.rect.centerx + self.cameraLimit - self.window.get_width() // 2

        if self.position.y < player.rect.centery - self.cameraLimit - self.window.get_height() // 2:
            self.position.y = player.rect.centery - self.cameraLimit - self.window.get_height() // 2
        elif self.position.y > player.rect.centery + self.cameraLimit - self.window.get_height() // 2:
            self.position.y = player.rect.centery + self.cameraLimit - self.window.get_height() // 2

    def slide_to(self, position: pygame.Vector2, speed: float):
        if self.position.x < (position.x - self.window.get_width() // 2) - 5:
            self.position.x += speed
        elif self.position.x > (position.x - self.window.get_width() // 2) + 5:
            self.position.x -= speed

        if self.position.y < (position.y - self.window.get_height() // 2) - 5:
            self.position.y += speed
        elif self.position.y > (position.y - self.window.get_height() // 2) + 5:
            self.position.y -= speed

    def go_at(self, position: pygame.Vector2):
        self.position = position