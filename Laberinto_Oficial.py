#Laberinto
import pygame
import random

########  SPRITES #######################################################################################
class muro(pygame.sprite.Sprite):                                                                        #
    def __init__(self):                                                                                   #
        super().__init__()                                                                                # 
        self.image=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\ParedAmarilla.jpg").convert_alpha()                                 
        self.rect=self.image.get_rect()                                                                   #
class suelo(pygame.sprite.Sprite):                                                                        #
    def __init__(self):                                                                                   #
        super().__init__()                                                                                #
        self.image=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\Definitivo.png").convert_alpha()                                  
        self.rect=self.image.get_rect()                                                                   #
class PJ (pygame.sprite.Sprite):                                                                          #
    def __init__(self):                                                                                   #
        super().__init__()                                                                                #
        self.image=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\PJ_DS.png").convert_alpha()                                         
        self.rect=self.image.get_rect()                                                                   #                                                                            
class inicio(pygame.sprite.Sprite):                                                                       #
    def __init__(self):                                                                                   #
        super().__init__()                                                                                #
        self.image=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\InicioColor.jpg").convert_alpha()                                   
        self.rect=self.image.get_rect()                                                                   # 
class Final(pygame.sprite.Sprite):                                                                        #
    def __init__(self):                                                                                   #
        super().__init__()                                                                                #
        self.image=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\FinalColor.jpg").convert_alpha()                                    #
        self.rect=self.image.get_rect()                                                                   #
        self.rect=self.image.get_rect()                                                                   #
Logo=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\Logo.png")  
Menu=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\Menu.jpg")  
YouWin=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\Congrats.gif")                                                                    
Bosque=pygame.image.load("E:\AA-TEC\Primer semestre\Taller\Semana 15\Terminado\Fondo bosque.jpg")  #fondo de pantalla                                         
#########################################################################################################
def Congrats():
    ganar=True
    while ganar:
        clock.tick(60)
        if movil==ColiFinal:
            WIN.blit(YouWin,(n*80//22,m*80//2))


matrizUsuario=[]

##  COLICIONES  ############################################
def ParedesLaberinto(laberinto):                            #
    Listamuros=[]                                            #
    x=0                                                      #
    y=0
    print(laberinto)
    for fila in laberinto:                                   # 
        for pared in fila:                                   #
            if pared == True:                                #
                Listamuros.append(pygame.Rect(x,y,80,80))    #
            x+=80                                            #
        x=0                                                  #
        y+=80                                                # 
    return Listamuros                                       #
########## start colicion  #################################
def StartColicion():                                        #
    ListaStart=[]                                            #
    x=0                                                      #
    y=0                                                      #
    for fila in laberinto:                                   #
        for inicio in fila:                                  #
            if inicio=='I':                                  #
                ListaStart.append(pygame.Rect(x,y,80,80))    #
                
    return ListaStart                                       #
############################################################  
def n_matriz(matriz):
    filas=0
    for x in matriz:
        filas+=1
    return filas
def m_matriz(matriz):
    columnas=0
    for x in matriz:
        columnas+=1
    return columnas

def inicio_m(matrizUsuario):
    res =-1
    for x in matrizUsuario:
        res+=1
        for y in x:
            if y=="I":
                return res

def final_m(matrizUsuario):
    res =-1
    for x in matrizUsuario:
        res+=1
        for y in x:
            if y=="F":
                return res
## DIBUJA EL MAPA #################################
def dibujadorMuros(superficie,rectangulo):         #  
    pygame.draw.rect(superficie, VERDE, rectangulo) #
def dibujadorLaberinto(superficie, Listamuros):     # 
    for pared in Listamuros:                        # 
        dibujadorMuros(superficie, pared)          # 
###################################################
if matrizUsuario==[]:
    n = int(input("Inserte las filas: "))   #ancho                               
    m = int(input("Inserte las columnas: "))  #alto ramdom
    Inicio_n=random.randrange(n-1)
    Inicio_m=random.randrange(m-1)
    Final_n=random.randrange(n-1)
    Final_m=random.randrange(m-1)
else:
    n=m_matriz(matrizUsuario[0])
    m=n_matriz(matrizUsuario)

    Inicio_n=random.randrange(n-1)
    Inicio_m=inicio_m(matrizUsuario)
    print(inicio_m(matrizUsuario))
    Final_n=random.randrange(n-1)
    Final_m=final_m(matrizUsuario)

#colres
VERDE=(0,140,60)
Blanco=(255,255,255) 

#  parametros de la ventana   ##############################################################
WIDTH, HEIGHT=(n*80)+400,m*80 #variable para el tamano                                      #
FPS= 30                                                                                      #
WIN= pygame.display.set_mode((WIDTH,HEIGHT))  #variable que contiente la venntana            #
pygame.display.set_caption("Laberinto.io") #nombre de la ventana                             #
clock=pygame.time.Clock()                                                                   #
############################################################################################

#Funcion para el color de la ventana #####################################################                                                                      
#WIN.blit(suelo,(0,0))                                                                    #
#WIN.fill()                                                                                #
#pygame.display.update()  #funcion para actualizar y que se  van los cambios              #
##########################################################################################
def mostrar_ganaste():
    WIN.blit(Bosque,(0,0))
    WIN.blit(Logo,(n*80//2,m*80//2))
    
    print("hola")
    pygame.display.flip()
    waiting=True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting=False
##  LISTA DE SPRITES  ####################
mostrar_ganaste()
ganaste=False
lista_Sprite_Muro= pygame.sprite.Group()  #
muro=muro()                                #
lista_Sprite_Muro.add(muro)                #
lista_sprite_suelo=pygame.sprite.Group()   #
suelo=suelo()                              #
lista_sprite_suelo.add(suelo)              # 
lista_sprite_inicio=pygame.sprite.Group()  #
inicio=inicio()                            #
lista_sprite_inicio.add(inicio)            #
lista_sprite_final=pygame.sprite.Group()   #
Final=Final()                              #
lista_sprite_final.add(Final)              #
lista_arbol_sprite=pygame.sprite.Group()   #
PJ=PJ()                                    #
lista_arbol_sprite.add(PJ)  
##########################################

###  Generador de Matrices  ###################################
matriz=[]                                                      #
laberinto=[]                                                    #
def generador_matriz():                                         #
    global n                                                    #
    global m                                                    #

    global matriz                                               #
    matriz=[[TrueFalse() for j in range(n)] for i in range(m)]  #
    global Inicio_n
    global Inicio_m
    global Final_n
    global Final_m
    matriz[Inicio_m][0]="I"                                     #
    matriz[0][1]=False                                          #
    matriz[Final_m][-1]="F"                                     #
    matriz[-1][-2]=False                                        #
    return matriz                                               #
def TrueFalse():                                                #
    lista= random.choice([True, False])                         #
    return lista                                                #                                                                
laberinto= generador_matriz()                                   #                                            
###############################################################
if matrizUsuario==[]:
    listaMatriz= ParedesLaberinto(laberinto)
else:
    laberinto= matrizUsuario
    listaMatriz= ParedesLaberinto(laberinto)
print(laberinto)    

##  Variables para el movimiento  ###
vel=0                                # 
alt=0                                 #
ColiFinal=pygame.Rect(0,Final_m*80,80,80)
movil=pygame.Rect(0,Inicio_m*80,70,50) #
print(Inicio_m)
#^^^^Colicion del personaje^^^^^      #
Vel=5                                 #
x=0                                   #
y=0 
#####################################

########## Movimiento ############################
gameOver=False                                    #
ganaste=True
while not gameOver:
    clock.tick(60)                                 #
    for event in pygame.event.get():               # 
        if event.type==pygame.QUIT:                # 
            gameOver=True  
            Congrats()
        if event.type==pygame.KEYDOWN:             #   
            if event.key == pygame.K_LEFT:         #
                vel=-5                             #
            elif event.key == pygame.K_RIGHT:      #
                vel=+5                             #
            elif event.key == pygame.K_UP:         #
                alt=-5                             #
            elif event.key == pygame.K_DOWN:       #
                alt=+5                             #
        else:                                      #
            vel=0                                  #
            alt=0                                  #
    movil.x+=vel                                   #
    movil.y+=alt                                   #
    PJ.rect.x=movil.x                              #
    PJ.rect.y=movil.y                              #
    for pared in listaMatriz:                      #
        if movil.colliderect(pared):               #
            movil.x-=vel                           #
            movil.y-=alt
    if movil.colliderect(ColiFinal):
        ganaste=True
    if movil.left<0:                               #
        movil.left=0                               #
    elif movil.right>n*80:                         #
        movil.right=n*80                           #
    elif movil.top<0:                              #
        movil.top=0                                #
    elif movil.bottom>m*80:                        #
        movil.bottom=m*80                         #
### fondo y otras imagnes en pantalla ############
    WIN.blit(Bosque,[0,0])                       #
    WIN.blit(Logo, (n*80+50,100)) 
    
## Agrega sprites a la ventana  #################
    x=0                                          #
    y=0                                           #
    for fila in laberinto:                        #
        for pared in fila:                        #
            if pared==True:                       #
                muro.rect.x=x                     #
                muro.rect.y=y                     #
                lista_Sprite_Muro.add(muro)       #
                lista_Sprite_Muro.draw(WIN)       #
            elif pared=="I":                      #
                inicio.rect.x=x                   #
                inicio.rect.y=y                   #
                lista_sprite_inicio.add(inicio)   #
                lista_sprite_inicio.draw(WIN)     #
            elif pared=="F":                      #
                Final.rect.x=x                    #
                Final.rect.y=y                    #
                lista_sprite_final.add(Final)     # 
                lista_sprite_final.draw(WIN)      #
            else:                                 # 
                suelo.rect.x=x                    #
                suelo.rect.y=y                    #
                lista_sprite_suelo.add(suelo)     #
                lista_sprite_suelo.draw(WIN)      #
            x+=80                                 #
        x=0                                       #
        y+=80                                     #
    lista_arbol_sprite.draw(WIN)                  #
    #dibujadorMuros(WIN, listaMatriz)             #
    pygame.display.flip()                         #
pygame.quit()                                    #
#################################################
            
