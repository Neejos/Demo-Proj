import pygame,sys,random
#Defining a function for the base floor to animate the floor as constantly moving object
def draw_floor():
 screen.blit(floor_surface,(floor_x_pos,800))
 screen.blit(floor_surface,(floor_x_pos+576,800))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_red.get_rect(midbottom = (700,random_pipe_pos - 300))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface,pipe)
          
        else:
            flip_pipe = pygame.transform.flip(pipe_red,False,True)
            screen.blit(flip_pipe,pipe)
           

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if  bird_rect.bottom >= 950:
        return False
    return True

def rotate_corona(corona):
    #Rotozoom is used for thr rotation in pygame 
    new_bird = pygame.transform.rotozoom(corona,-bird_movement*3,1)
    return new_bird


def score_display(game_state):
	if game_state == 'main_game':
		score_surface = game_font.render(str(int(score)),True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,200))
		screen.blit(score_surface,score_rect)
	if game_state == 'game_over':
		score_surface = game_font.render(f'Score: {int(score)}' ,True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,200))
		screen.blit(score_surface,score_rect)

		high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
		high_score_rect = high_score_surface.get_rect(center = (288,700))
		screen.blit(high_score_surface,high_score_rect)

def update_score(score, high_score):
	if score > high_score:
		high_score = score
	return high_score
pygame.mixer.pre_init(frequency = 44100,size=16,channels=1,buffer = 512)
pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',30)
#Game variables 
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0


#convert() changes it in a way to be easy for use in the python game and helps run the game at a consistent speed
bg_surface = pygame.image.load('assets/Resize.png').convert()
#scale2X scales the background surface and adjusts the image
bg_surface = pygame.transform.scale2x(bg_surface)
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos=0
bird_surface = pygame.image.load('assets/coro.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))
pipe_surface = pygame.image.load('assets/mummy.png').convert_alpha()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_red = pygame.image.load('assets/mummy.png').convert_alpha()  
pipe_red = pygame.transform.scale2x(pipe_red)
pipe_list = []
#Triggers event by timer
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,2200)
pipe_height = [400,600,800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/NewMessage.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))

corona_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100

while True:
    #image of player 1
    #background image
    for event in pygame.event.get():
        #TO GET AN X BUTTON TO CLOSE THE SCREEN
        if event.type == pygame.QUIT:
            pygame.quit()
        #To make sure we shut down opur game completely
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8
                corona_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True 
                pipe_list.clear()
                bird_rect.center = (100,512)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
           
    #blit puts one surface on  another
    screen.blit(bg_surface,(0,0))
    if game_active:
        #Corona
        bird_movement += gravity
        rotated_corona = rotate_corona(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_corona,(bird_rect))
        game_active =  check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)




