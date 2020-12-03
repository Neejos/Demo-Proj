import pygame,sys,random
#Defining a function for the base floor to animate the floor as constantly moving object
def draw_floor():
 screen.blit(floor_surface,(floor_x_pos,800))
 screen.blit(floor_surface,(floor_x_pos+576,800))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos+400))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos+100))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes
def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 800:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)

def remove_pipes(pipes):
	for pipe in pipes:
		if pipe.centerx == -600:
			pipes.remove(pipe)
	return pipes
def check_collision(pipes):
    for pipe in pipes:
        if coro_rect.colliderect(pipe):
            death_sound.play() 
            return False
  

    if  coro_rect.bottom >= 950:
        return False
    return True

def rotate_corona(corona):
    #Rotozoom is used for thr rotation in pygame 
    new_coro = pygame.transform.rotozoom(corona,-coro_movement*3,1)
    return new_coro


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


pygame.mixer.pre_init(frequency = 48000,size=-16,channels=1,buffer = 1024)
pygame.init()
# themesong = pygame.mixer.Sound('sound/themesong.wav')
pygame.mixer.music.load('sound/themesong.wav')
pygame.mixer.music.play()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',30)
#Game variables 
gravity = 0.25
coro_movement = 0
game_active = True
score = 0
high_score = 0


#convert() changes it in a way to be easy for use in the python game and helps run the game at a consistent speed
bg_surface = pygame.image.load('assets/NewCity.png').convert()
#scale2X scales the background surface and adjusts the image
bg_surface = pygame.transform.scale2x(bg_surface)
floor_surface = pygame.image.load('assets/stone.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos=0
coro_surface = pygame.image.load('assets/virus.png').convert_alpha()
coro_surface = pygame.transform.scale2x(coro_surface)
coro_rect = coro_surface.get_rect(center = (100,512))
pipe_surface = pygame.image.load('assets/doctor.png').convert_alpha()
pipe_surface = pygame.transform.scale2x(pipe_surface)
# pipe_red = pygame.image.load('assets/women.png').convert_alpha()  
# pipe_red = pygame.transform.scale2x(pipe_red)
pipe_list = []
#Triggers event by timer
SPAWNPIPE = pygame.USEREVENT  
pygame.time.set_timer(SPAWNPIPE,2200)
pipe_height = [100,200,300]

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/Screen.png').convert_alpha())
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
                coro_movement = 0
                coro_movement -= 8
               
                # corona_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True 
                pipe_list.clear()
                coro_rect.center = (100,512)
                coro_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
           
    #blit puts one surface on  another
    screen.blit(bg_surface,(0,0))
    if game_active:
        #Corona
        coro_movement += gravity
        rotated_corona = rotate_corona(coro_surface)
        coro_rect.centery += coro_movement
        screen.blit(rotated_corona,(coro_rect))
        game_active =  check_collision(pipe_list)
        

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
           
            # score_sound.play()
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




