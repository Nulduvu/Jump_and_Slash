from Player import Player
from Camera import Camera
from Enemy import Enemy
from Wall import Wall
import pygame
import json


class Window:
    def __init__(self):
        pygame.display.set_caption("Jump and Slash")
        self.window = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
        self.window.fill((255, 255, 255))

    def update(self):
        pygame.display.update()
        self.window.fill((255, 255, 255))
        pygame.time.Clock().tick(60)


def run(window: Window, player: Player, walls: list[Wall], camera: Camera, entity: list[Enemy]):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.attack()

        player.update(camera=camera, walls=walls)
        # camera.slide_to(pygame.Vector2(player.rect.centerx, player.rect.centery), 5)

        for wall in walls:
            wall.update(camera=camera)

        for e in entity:
            e.update(walls=walls, camera=camera, playerRect=player.rect)

        window.update()


if __name__ == '__main__':
    pygame.init()

    window = Window()
    camera = Camera(window=window.window)

    player = Player(window=window.window)

    walls = []
    entity = []
    level = json.load(open("./Assets/Levels/Level1.json"))

    for wall in level["Walls"]:
        walls.append(Wall(window=window.window, rect=pygame.Rect(wall[0], wall[1], wall[2], wall[3])))
    for enemy in level["Enemy"]:
        entity.append(Enemy(window=window.window, position=pygame.Vector2(enemy[0], enemy[1]), type=enemy[2]))

    run(window=window, player=player, walls=walls, camera=camera, entity=entity)
