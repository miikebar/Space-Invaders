import pygame.math
from timer import Timer
from laser import Laser
from pygame.locals import *
from animated_sprite import AnimatedSprite

class Player(AnimatedSprite):
  def __init__(self, game):
    super().__init__("Lightning.png", 32, 4, 3, 100)
    
    self.game = game
    self.thrust = 1
    self.speed_max = 15
    self.speed_decay = .95
    self.movement_clamp = 10
    self.velocity = pygame.math.Vector2(0, 0)

  def update(self):
    super().update()

    self.move()

  def move(self):
    if self.game.input.key(K_LEFT):
      self.velocity.x -= self.thrust
    elif self.game.input.key(K_RIGHT):
      self.velocity.x += self.thrust
    else:
      self.velocity.x *= self.speed_decay

    speed = self.velocity.length()

    if speed > self.speed_max:
      self.velocity.x *= self.speed_max / speed
      self.velocity.y *= self.speed_max / speed
    elif (self.velocity.x > -.5 and self.velocity.x < 0) or (self.velocity.x < .5 and self.velocity.x > 0):
      self.velocity.x = 0

    if (
      self.rect.left - self.movement_clamp < 0 and self.velocity.x < 0 or
      self.rect.left > self.game.get_width() - self.rect.width - self.movement_clamp and self.velocity.x > 0
      ):
      self.velocity.x = 0

    self.rect.move_ip(self.velocity.x, self.velocity.y)