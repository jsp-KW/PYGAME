import pygame
import sys

pygame.init ()
pygame.display.set_caption ('점핑 공룡 게임')

max_width =800
max_height = 400

def main () :
    screen = pygame.display.set_mode ((max_width, max_height))
    fps = pygame.time.Clock()


    dino1 = pygame.image.load('images/dino1.png')
    dino2 = pygame.image.load('images/dino2.png')
    dino_height = dino1.get_size ()[1]
    dino_bottom = max_height - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_limit = 200
    

    leg_swap = True
    is_bottom = True
    is_go_up = False



    #Tree

    Tree = pygame.image.load('images/tree.png')
    tree_height = Tree.get_size()[1]
    tree_x = max_width
    tree_y = max_height-tree_height



    while True:
        screen.fill((255,255,255))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False


        #공룡 이동

        if is_go_up: #점프할때
            dino_y -=10.0
        elif not is_go_up and not is_bottom : #점프후 밑으로 내려갈때
            dino_y +=10.0

        
        if is_go_up and dino_y <=jump_limit:
            is_go_up = False
        
        if not is_bottom  and dino_y >= dino_bottom :
            is_bottom = True
            dino_y = dino_bottom
        

        #tree 이동

        tree_x  -=12.0

        if tree_x <=0 :
            tree_x = max_width

        screen.blit(Tree, (tree_x,tree_y))

        if  leg_swap :
            screen.blit(dino1,(dino_x,dino_y))
            leg_swap = False
        else:
            screen.blit(dino2,(dino_x, dino_y))
            leg_swap=True

        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__' :
    main ()