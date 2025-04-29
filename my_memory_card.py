from pygame import *

img_back = "ctol.jpg"
img_rocket = "Без имени.png"
img_ball = "ball.png"

class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)
      #каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rest.y > 5:
      self.rest.y -= self.speed

  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rest.y > 5:
      self.rest.y -= self.speed

#создаём окошко
win_width = 700
win_height = 500
display.set_caption("ping_pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False

run = True 
racket1 = Player(img_rocket, 0, 200, 70, 150, 10)
racket2 = Player(img_rocket, 0, 500, 70, 150, 10)
while run:
   #событие нажатия на кнопку “Закрыть”
   for e in event.get():
       if e.type == QUIT:
           run = False

   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
       racket1.reset()

       display.update()

   time.delay(50)

