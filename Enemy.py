import pygame
import json

class Enemy:
    def __init__(self, window: pygame.Surface, position: pygame.Vector2, type: str):
        self.window = window

        enemy = json.load(open("./Assets/Enemy/Enemy.json"))[type]

        self.speed = enemy["Speed"]
        self.jumpForce = enemy["JumpForce"]
        self.damage = enemy["Damage"]
        self.rect = pygame.Rect(position.x, position.y, enemy["Width"], enemy["Height"])
        self.sprite = pygame.transform.scale(pygame.image.load(enemy["Sprite"]).subsurface((22, 0, 10, 10)), self.rect.size)

        self.velocity = pygame.Vector2()
        self.gravityForce = 0.2
        self.isGround = False

    def draw(self, camera):
        self.window.blit(self.sprite, (self.rect.x - camera.position.x, self.rect.y - camera.position.y, self.rect.width, self.rect.height))

    def move(self, playerRect: pygame.Rect, walls: list):
        if self.rect.centerx < playerRect.centerx:
            self.velocity.x += self.speed
        elif self.rect.centerx > playerRect.centerx:
            self.velocity.x -= self.speed

        if not self.isGround:
            self.velocity.y += self.gravityForce
        elif self.isGround and playerRect.y + playerRect.h < self.rect.centery:
            self.velocity.y = -self.jumpForce

        self.rect.x += self.velocity.x
        for wall in walls:
            wall.collide_x(self)

        self.rect.y += self.velocity.y
        for wall in walls:
            wall.collide_y(self)

        self.velocity.x = 0

    def update(self, walls: list, camera, playerRect: pygame.Rect):
        self.draw(camera)
        self.move(playerRect=playerRect, walls=walls)
