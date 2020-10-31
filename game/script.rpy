# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Shrek")
define d=Character("Dave Mustaine")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")


init python:
    define.move_transitions("ease", 60.0)
    
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $renpy.sound.play("audio/thanos.mp3", loop=True)
    
    show run_animation at truecenter with flash
    
    "jeff"
    
    

    show shrek sad behind run_animation with easeinright
    
    hide run_animation


    e "WHAT ARE YOU DOING IN MY SWAMP!?"
    
    show shrek happy with dissolve
    #call prologue crashes the game, not sure why
    e "This is the part, where you run away!"
    
    "Shrek has told me to run away, what should I do?"
    
    show dave panning
    
    "Is that you dave mustaine?"
    
    show dave with flash
    
    "cool"
    
    d"Tell me son, what is it that you need?"
    #This begins a choice to continue the story
    menu:
        "What do I ask from Dave Mustaine?"
        
        "Wow you look strong let's have a guitar battle!":
            d"There is no time, shrek must be beat in a shred war"
            jump riff
            
        "I need you to beat Shreks legendary drop A guitar riffs!":
                d"Yes my child."
                hide dave
                jump riff
    
#This is the dialouge branch for asking Dave to fight Shrek
label riff:
    show dave at left
    show shrek worry at right with flash
    d"Hope you use D'addario NYXL strings, the only strings that can stay in tune for months on end and never break!"
    e"WHAT ARE YOU DOING IN MY PIT!?"
    "man, Dave is really pumping out some out of this world shreds, I could never even imagine seeing something this amazing."
    "Shrek has no chance at all!"
    hide dave with flash
    "WHAT!?"
    
    menu:
        "It's up to me, I must end shrek"
        
        "Do a roar":
                "ROAR!" 
                e"Oh no"
                hide shrek with hpunch
                "I did it, I defeated shrek"
                
        "Run":
            hide shrek with fade
            "I have escaped!"
            "But shrek is still out there, he could terrorise me with more Drop A riffs."
    

    # This ends the game.

    return
