screen cheatnavigation():
    modal True
    add "#000"
    text "{size=80}Joker's Cheat Mod" color "#0f0" xcenter 0.5 ypos 15

screen cheatmenu():
    modal True
    add "#000"
    add "JokerMod/Images/Cheat/CheatBG.jpg" alpha 0.60
    text "{size=60}Joker's Cheat Mod" color "#f00" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ypos 15 outlines [(2, "#000", 0, 3)]

    textbutton "{size=40}Return" text_selected_color "#0f0" text_idle_color "#ffffff" action Return() xalign 0.01 yalign 0.99

    vpgrid:
         xcenter 0.5
         ypos 150
         cols 4
         xspacing 60
         yspacing 50
         vbox:
             spacing 10
             text"{size=30}{color=#FF7070}[a]'s Love{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("amelie_love", 100)
                 text "{color=#ffffff}[amelie_love]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#FF7070}[a]'s Lust{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("amelie_lust", 100)
                 text "{color=#ffffff}[amelie_lust]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#F5C7FF}[k]'s Love{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("kylee_love", 100)
                 text "{color=#ffffff}[kylee_love]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#F5C7FF}[k]'s Lust{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("kylee_lust", 100)
                 text "{color=#ffffff}[kylee_lust]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#FFFFA6}[s]'s Love{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("stephanie_love", 100)
                 text "{color=#ffffff}[stephanie_love]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#FFFFA6}[s]'s Lust{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("stephanie_lust", 100)
                 text "{color=#ffffff}[stephanie_lust]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#9DE2FE}Mia's Love{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("mia_love", 100)
                 text "{color=#ffffff}[mia_love]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#9DE2FE}Mia's Lust{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("mia_lust", 100)
                 text "{color=#ffffff}[mia_lust]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#9DB4FE}[lauren]'s Lust{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("lauren_lust", 100)
                 text "{color=#ffffff}[lauren_lust]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]

         vbox:
             spacing 10
             text"{size=30}{color=#B5CCFF}[d]'s Love{/color=#f00}" font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]
             fixed:
                 xysize(250,40)
                 bar value VariableValue("davie_love", 100)
                 text "{color=#ffffff}[davie_love]{/color=#f00}" xcenter 0.5 ycenter 0.35 font "JokerMod/Bebas-Regular.otf" outlines [(2, "#000", 0, 2)]


    imagebutton:
        align(1.0,1.0)
        idle Transform("JokerMod/Images/Cheat/Patreon_Button.png", zoom=0.4)
        hover Transform("JokerMod/Images/Cheat/Patreon_Button_Hover.png", zoom=0.4)
        action OpenURL("https://www.patreon.com/JokerLeader")
    imagebutton:
        align(1.0,0.89)
        idle Transform("JokerMod/Images/Cheat/Coffee_Button.png", zoom=0.4)
        hover Transform("JokerMod/Images/Cheat/Coffee_Button_Hover.png", zoom=0.4)
        action OpenURL("https://www.buymeacoffee.com/JokerLeader")

    textbutton "{size=30}Change MC name{/size}" text_selected_color "#0f0" text_idle_color "#ffffff" xcenter 0.5 ypos 0.93 action [ui.callsinnewcontext("mcnamechange")]

label mcnamechange:
    scene black
    $ mc = renpy.input ("What is your name? (Default: John)")
    $ mc = y.strip()
    if mc == "":
        $ mc = "John"
    return
