import pygame
import map

HEIGHT, WIDTH = 600, 800
pygame.init()

scrn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("yaa test")

clk = pygame.time.Clock()

cp_st = map.sart_point

cp_st[1] = 22
# draw once
# for sec in map.map1:
#    for char in sec:
#        print(char)
offx = cp_st[0]
offy = cp_st[1]
print(cp_st[1])


scrn.fill((00, 00, 0))
for y in range(cp_st[1], cp_st[1] + 18):
    for x in range(cp_st[0], cp_st[0] + 20):
        ch = map.map1[y][x]

        print(ch, end="")
        if ch == "o":
            # print(f"x:{x}", end=" ")
            # print(f"y:{y - 20}", end=" ")
            tile = pygame.Surface((32, 32))
            tile.fill((100, 100, 199))
            scrn.blit(tile, ((x) * 32, (y - offy) * 32))
        elif ch == "x":
            tile = pygame.Surface((32, 32))
            tile.fill((255, 255, 255))
            scrn.blit(tile, ((x) * 32, (y - offy) * 32))
    #    li = map.map1[y]
    # print(li[1])
    print()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    clk.tick(60)
    pygame.display.flip()
