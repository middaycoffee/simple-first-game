import pygame
import random

class Invasion:
    def __init__(self):
        pygame.init()

        self.load_images()

        self.scr_height = 600
        self.scr_width = 1200
        self.scr = pygame.display.set_mode((self.scr_width, self.scr_height))
        self.intro_font = pygame.font.SysFont("Arial", 80)
        self.intro_font2 = pygame.font.SysFont("Arial", 50)
        self.game_font = pygame.font.SysFont("Arial", 30)
        self.points = 0
        self.x = 100
        self.y = 100
        self.speed_robot = 4
        self.timer = 0
        self.timerm = 0
    


        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.coins = []
        self.monsters = []

        self.clock = pygame.time.Clock()
        self.intro()
    



    def load_images(self):
        self.images = {}
        self.masks = {}
        for name in ["coin", "door", "monster", "robot"]:
            self.images[name] = pygame.image.load(name + ".png")
            self.masks[name] = pygame.mask.from_surface(self.images[name])

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_up = True
                if event.key == pygame.K_DOWN:
                    self.move_down = True
                if event.key ==pygame.K_LEFT:
                    self.move_left = True
                if event.key ==pygame.K_RIGHT:
                    self.move_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.move_up = False
                if event.key == pygame.K_DOWN:
                    self.move_down = False
                if event.key ==pygame.K_LEFT:
                    self.move_left = False
                if event.key ==pygame.K_RIGHT:
                    self.move_right = False

    def update_robot(self):
        self.check_events()
        if self.move_up and self.y >= 3:
            self.y -= self.speed_robot
        if self.move_down and (self.y + self.images["robot"].get_height()) <= self.scr_height:
            self.y += self.speed_robot
        if self.move_left and self.x >= 0:
            self.x -= self.speed_robot
        if self.move_right and (self.x + self.images["robot"].get_width()) <= self.scr_width:
            self.x += self.speed_robot

    def check_collision_coin(self, coin):
        if coin[3].overlap(self.masks["robot"], (self.x - coin[1], self.y - coin[2])):
            return True
        return False

    def check_collision_monster(self, monster):
        if monster[3].overlap(self.masks["robot"], (self.x - monster[1], self.y - monster[2])):
            return True
        return False

    def spawn_coin(self):
        coin = self.images["coin"]
        coin_width = coin.get_rect()[2]
        coin_height = coin.get_rect()[3]
        self.coins.append((coin, random.randint(0, self.scr_width - coin_width), random.randint(0, self.scr_height - coin_height), self.masks["coin"]))

    def spawn_monster(self):
        monster = self.images["monster"]
        monster_width = monster.get_rect()[2]
        monster_height = monster.get_rect()[3]
        self.monsters.append([monster, self.scr_width, random.randint(0, self.scr_height - monster_height), self.masks["monster"]])

    def update_monster(self):
        for monster in self.monsters:
            monster[1] -= 4
            if self.check_collision_monster(monster):
                exit()
    

    def update_coin(self):
        for coin in self.coins: 
            if self.check_collision_coin(coin):
                self.coins.remove(coin)
                self.points += 1

    def intro(self):
        while True:
            self.scr.fill((200, 201, 130))
            text = self.intro_font.render("Press Enter to Start the Game!", True, (255, 0, 0))
            text1 = self.intro_font2.render("Instructions:", True, (0, 0, 0))
            text2 = self.game_font.render("Collect points while avoiding the monsters. Game will end if a monster gets you.", True, (0, 0, 0))

            self.scr.blit(text, (150, 50))
            self.scr.blit(text1, (150, 150))
            self.scr.blit(text2, (150, 200))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.main_loop()


    def draw_screen(self):
        self.scr.fill((200, 201, 130))
        self.scr.blit(self.images["robot"], (self.x, self.y))
        for c in self.coins:
            self.scr.blit(c[0], (c[1], c[2]))
        for m in self.monsters:
            self.scr.blit(m[0], (int(m[1]), int(m[2])))
        text = self.game_font.render(f"Points: {self.points}", True, (255, 0, 0))
        self.scr.blit(text, (1000, 50))
        pygame.display.flip()

    


    def main_loop(self):
        while True:
            self.timer += 1
            self.timerm += 1
            if self.timerm >= 80:
                self.spawn_monster()
                self.timerm = 0
            if self.timer >= 180:
                self.spawn_coin()
                self.timer = 0
            self.update_robot()
            self.update_monster()
            self.update_coin()
            self.draw_screen()
            
            self.clock.tick(60)


game = Invasion()