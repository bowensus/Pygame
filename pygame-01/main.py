from setting import *
import pygame, sys


######################
# SETTING THE SCREEN
######################

pygame.init()

clock = pygame.time.Clock()

screen_width = WIDTH
screen_height = HEIGHT
fps = FPS
game_font = pygame.font.Font("freesansbold.ttf", 32)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


#########################
# SETTING THE ELEMENTS
#########################

ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 120)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 120)

bg_color = pygame.Color("grey")
ele_color = pygame.Color("black")

# ball moving
ball_speed_x = 0
ball_speed_y = 0

def check_ball_direction():
  global ball_speed_x, ball_speed_y

  if ball.bottom >= screen_height or ball.y <= 0:
    ball_speed_y = -ball_speed_y
  if ball.right >= screen_width - 20 and player.y <= ball.centery <= player.bottom:
    ball_speed_x = -ball_speed_x
  if ball.left <= 20 and opponent.y <= ball.centery <= opponent.bottom:
    ball_speed_x = -ball_speed_x

def ball_moving():
  ball.x += ball_speed_x
  ball.y += ball_speed_y

# player moving
player_speed = 0
opponent_speed = 3.7

def character_moving(charactor, speed):
  charactor.y += speed
  if charactor.y <= 0:
    charactor.y = 0
  if charactor.bottom >= screen_height:
    charactor.bottom = screen_height

# oppenent moving
def oppenent_moving(speed):
  if opponent.y > ball.centery:
    opponent.y -= speed
  if opponent.bottom < ball.centery:
    opponent.y += speed
  if opponent.y <= 0:
    opponent.y += speed
  if opponent.bottom >= screen_height:
    opponent.y -= speed


######################
# SETTING THE GAME
######################

# score
player_score = 0
oppenent_score = 0

def update_score(score):
  score += 1
  return score

# restart
def reset_ball():
  ball.x = screen_width/2 - 10
  ball.y = screen_height/2 - 10

def check_next():
  global oppenent_score, player_score

  if ball.right >= screen_width and ball.centery < player.y:
    reset_ball()
    oppenent_score = update_score(oppenent_score)
  elif ball.right >= screen_width and ball.centery > player.bottom:
    reset_ball()
    oppenent_score = update_score(oppenent_score)
  if ball.left <= 0 and ball.centery < opponent.y:
    reset_ball()
    player_score = update_score(player_score)
  elif ball.left <= 0 and ball.centery > opponent.bottom:
    reset_ball()
    player_score = update_score(player_score)

# start the game
is_running = False

def start_running():
  global ball_speed_x, ball_speed_y
  if is_running:
    ball_speed_x = 4
    ball_speed_y = 4


######################
# RUNNING THE GAME
######################

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player_speed += 4
      if event.key == pygame.K_UP:
        player_speed -= 4
      if event.key == pygame.K_SPACE:
        is_running = True
        start_running()
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player_speed -= 4
      if event.key == pygame.K_UP:
        player_speed += 4

  # animation()
  check_ball_direction()
  ball_moving()
  character_moving(player, player_speed)
  oppenent_moving(opponent_speed)
  check_next()

  # drawing
  screen.fill(bg_color)
  pygame.draw.rect(screen, ele_color, player)
  pygame.draw.rect(screen, ele_color, opponent)
  pygame.draw.ellipse(screen, ele_color, ball)
  # drawing the line
  pygame.draw.aaline(screen, ele_color, (screen_width/2, 0), (screen_width/2, screen_height))
  
  player_text = game_font.render(f"Player Score: {player_score}", False, ele_color)
  screen.blit(player_text, (screen_width-250, 20))

  opponent_text = game_font.render(f"AI Score: {oppenent_score}", False, ele_color)
  screen.blit(opponent_text, (10, 20))

  # updating the window
  pygame.display.flip()
  clock.tick(fps)


  


