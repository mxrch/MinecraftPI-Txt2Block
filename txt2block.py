# On importe les librairies de Minecraft Pi
import mcpi.minecraft as minecraft
import mcpi.block as block
 
mc = minecraft.Minecraft.create()

#Fonctions
 
def ecrire():
    #On définit la fonction qui va écrire le texte
    x, y, z = mc.player.getPos() #On stocke la position du joueur dans les variables x y z
    bloc = int(input("Quel bloc voulez-vous utiliser ? Veuillez entrer son id : ")) #On demande à l'utilisateur quel bloc utiliser puis on sauvegarde son id dans la variable "bloc"
    texte = input("Que voulez vous ecrire ? ")
    mc.postToChat("Vous avez choisi : " + texte + " Avec le bloc id " + str(bloc))
    x = x-10
    z = z-16
    for lettre in texte:
        #On définit les lettres
        #Après chaque lettre on incrémente x de 6 pour pouvoir espacer les lettres
        if lettre == "A" or lettre == "a":
            mc.setBlocks(x+1,y,z,x+1,y+5,z,bloc)
            mc.setBlocks(x+5,y,z,x+5,y+5,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+2,y+3,z,x+4,y+3,z,bloc)
            x+=6
        elif lettre == "B" or lettre == "b":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+3,z,x+4,y+3,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+5,y+1,z,x+5,y+2,z,bloc)
            mc.setBlocks(x+5,y+4,z,x+5,y+5,z,bloc)
            x+=6
        elif lettre == "C" or lettre == "c":
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+1,y+1,z,x+1,y+5,z,bloc)
            mc.setBlock(x+5,y+5,z,bloc)
            mc.setBlock(x+5,y+1,z,bloc)
            x+=6
        elif lettre == "D" or lettre == "d":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+5,y+1,z,x+5,y+5,z,bloc)
            x+=6
        elif lettre == "E" or lettre == "e":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y,z,x+5,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+1,y+3,z,x+4,y+3,z,bloc)
            x+=6
        elif lettre == "F" or lettre == "f":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+1,y+3,z,x+4,y+3,z,bloc)
            x+=6
        elif lettre == "G" or lettre == "g":
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+1,y+1,z,x+1,y+5,z,bloc)
            mc.setBlock(x+5,y+5,z,bloc)
            mc.setBlock(x+5,y+1,z,bloc)
            mc.setBlocks(x+4,y+2,z,x+5,y+2,z,bloc)
            x+=6
        elif lettre == "H" or lettre == "h":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+2,y+3,z,x+4,y+3,z,bloc)
            x+=6
        elif lettre == "I" or lettre == "i":
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+3,y+1,z,x+3,y+5,z,bloc)
            x+=6
        elif lettre == "J" or lettre == "j":
            mc.setBlock(x+1,y+1,z,bloc)
            mc.setBlocks(x+2,y,z,x+3,y,z,bloc)
            mc.setBlocks(x+4,y+1,z,x+4,y+5,z,bloc)
            mc.setBlocks(x+3,y+6,z,x+5,y+6,z,bloc)
            x+=6
        elif lettre == "K" or lettre == "k":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlock(x+2,y+3,z,bloc)
            mc.setBlock(x+3,y+4,z,bloc)
            mc.setBlock(x+3,y+2,z,bloc)
            mc.setBlock(x+4,y+5,z,bloc)
            mc.setBlock(x+4,y+1,z,bloc)
            mc.setBlock(x+5,y+6,z,bloc)
            mc.setBlock(x+5,y,z,bloc)
            x+=6
        elif lettre == "L" or lettre == "l":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y,z,x+5,y,z,bloc)
            x+=6
        elif lettre == "M" or lettre == "m":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+3,y+3,z,x+3,y+4,z,bloc)
            mc.setBlock(x+2,y+5,z,bloc)
            mc.setBlock(x+4,y+5,z,bloc)
            x+=6
        elif lettre == "N" or lettre == "n":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y,z,x+5,y+6,z,bloc)
            mc.setBlock(x+2,y+4,z,bloc)
            mc.setBlock(x+3,y+3,z,bloc)
            mc.setBlock(x+4,y+2,z,bloc)
            x+=6
        elif lettre == "O" or lettre == "o":
            mc.setBlocks(x+1,y+1,z,x+1,y+5,z,bloc)
            mc.setBlocks(x+5,y+1,z,x+5,y+5,z,bloc)
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            x+=6
        elif lettre == "P" or lettre == "p":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+1,y+3,z,x+4,y+3,z,bloc)
            mc.setBlocks(x+5,y+4,z,x+5,y+5,z,bloc)
            x+=6
        elif lettre == "Q" or lettre == "q":
            mc.setBlocks(x+1,y+1,z,x+1,y+5,z,bloc)
            mc.setBlocks(x+5,y+2,z,x+5,y+5,z,bloc)
            mc.setBlocks(x+2,y,z,x+3,y,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlock(x+3,y+2,z,bloc)
            mc.setBlock(x+4,y+1,z,bloc)
            mc.setBlock(x+5,y,z,bloc)
            x+=6
        elif lettre == "R" or lettre == "r":
            mc.setBlocks(x+1,y,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+4,y+6,z,bloc)
            mc.setBlocks(x+1,y+3,z,x+4,y+3,z,bloc)
            mc.setBlocks(x+5,y+4,z,x+5,y+5,z,bloc)
            mc.setBlock(x+3,y+2,z,bloc)
            mc.setBlock(x+4,y+1,z,bloc)
            mc.setBlock(x+5,y,z,bloc)
            x+=6
        elif lettre == "S" or lettre == "s":
            mc.setBlocks(x+1,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+2,y+3,z,x+4,y+3,z,bloc)
            mc.setBlocks(x+2,y+6,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+5,y+1,z,x+5,y+2,z,bloc)
            mc.setBlocks(x+1,y+4,z,x+1,y+5,z,bloc)
            x+=6
        elif lettre == "T" or lettre == "t":
            mc.setBlocks(x+1,y+6,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+3,y,z,x+3,y+5,z,bloc)
            x+=6
        elif lettre == "U" or lettre == "u":
            mc.setBlocks(x+2,y,z,x+4,y,z,bloc)
            mc.setBlocks(x+1,y+1,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y+1,z,x+5,y+6,z,bloc)
            x+=6
        elif lettre == "V" or lettre == "v":
            mc.setBlocks(x+1,y+3,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y+3,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+2,y+1,z,x+2,y+2,z,bloc)
            mc.setBlocks(x+4,y+1,z,x+4,y+2,z,bloc)
            mc.setBlock(x+3,y,z,bloc)
            x+=6
        elif lettre == "W" or lettre == "w":
            mc.setBlocks(x+3,y+1,z,x+3,y+3,z,bloc)
            mc.setBlocks(x+1,y+1,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y+1,z,x+5,y+6,z,bloc)
            mc.setBlock(x+2,y,z,bloc)
            mc.setBlock(x+4,y,z,bloc)
            x+=6
        elif lettre == "X" or lettre == "x":
            mc.setBlocks(x+1,y,z,x+1,y+1,z,bloc)
            mc.setBlocks(x+1,y+5,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y,z,x+5,y+1,z,bloc)
            mc.setBlocks(x+5,y+5,z,x+5,y+6,z,bloc)
            mc.setBlock(x+2,y+2,z,bloc)
            mc.setBlock(x+4,y+2,z,bloc)
            mc.setBlock(x+3,y+3,z,bloc)
            mc.setBlock(x+2,y+4,z,bloc)
            mc.setBlock(x+4,y+4,z,bloc)
            x+=6
        elif lettre == "Y" or lettre == "y":
            mc.setBlocks(x+3,y,z,x+3,y+3,z,bloc)
            mc.setBlocks(x+1,y+5,z,x+1,y+6,z,bloc)
            mc.setBlocks(x+5,y+5,z,x+5,y+6,z,bloc)
            mc.setBlock(x+2,y+4,z,bloc)
            mc.setBlock(x+4,y+4,z,bloc)
            x+=6
        elif lettre == "Z" or lettre == "z":
            mc.setBlocks(x+1,y+6,z,x+5,y+6,z,bloc)
            mc.setBlocks(x+1,y,z,x+5,y,z,bloc)
            mc.setBlock(x+1,y+1,z,bloc)
            mc.setBlock(x+2,y+2,z,bloc)
            mc.setBlock(x+3,y+3,z,bloc)
            mc.setBlock(x+4,y+4,z,bloc)
            mc.setBlock(x+5,y+5,z,bloc)
            x+=6
        elif lettre == " ":
            x+=6
        else :
            print("Veuillez ne pas mettre d'accents ou d'autres caracteres que des lettres")

ecrire()
