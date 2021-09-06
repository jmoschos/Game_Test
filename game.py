import os
import pygame
import time

class Game():
    def __init__(self):
        pygame.init()
        self.game_width, self.game_height = 480,270
        self.screen_width, self.screen_height = 960,540
        self.game_canvas = pygame.Surface((self.game_width,self.game_height))
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.running = True
        self.playing = True
        self.actions = {'left': False, "right": False, 'up': False, 'down': False, "A": False, "B": False, "Start": False}
        self.dt,self.prev_time = 0,0
        self.state_stack = []
        self.load_assets()     # doesn't do anything right now

    def get_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                if event.key == pygame.K_UP:
                    self.actions['up'] = True
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = True
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = True
                if event.key == pygame.K_a:
                    self.actions['A'] = True
                if event.key == pygame.K_b:
                    self.actions['B'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['Start'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                if event.key == pygame.K_UP:
                    self.actions['up'] = False
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = False
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = False
                if event.key == pygame.K_a:
                    self.actions['A'] = False
                if event.key == pygame.K_b:
                    self.actions['B'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['Start'] = False


    def update(self):
        pass

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprites_dir = os.path.join(self.assets_dir,"sprites")

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def render(self):
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.screen_width,self.screen_height)),(0,0))
        pygame.display.flip()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()




if __name__ == '__main__':
    g = Game()
    while g.running:
        g.game_loop()