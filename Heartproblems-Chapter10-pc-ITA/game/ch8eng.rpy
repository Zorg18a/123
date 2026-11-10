label ch8at:
    stop music fadeout 2.0
    scene blackscreen
    with dissolve
    pause
label ch8s1:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
    if stephloving == "True":
        s "{i}{size=-3}[mc]..."
    else:
        jump ch8_74scene
    s "{i}{size=-3}[mc], wake up."
    s "{i}{size=-3}It's already 5 am, [mc]."
    play music scene3 fadein 2.0
    scene ch8_1- with dissolve
    mc "Uh, what?"
    mc "(I feel like I haven't slept at all.)"
    mc "Are you sure it's already five?"
    s "Yeah, in fact, it's five with ten seconds."
    mc "You sure are punctual..."
    s "Can I get on the bed with you?"
    mc "S-sure."
    pause
    scene ch8_2 with dissolve
    mc "Hey-"
    s "Tehe."
    scene ch8_3 with dissolve
    s "*Hmnch*"
    s "*Lhmnsh, ahmm*..."
    scene ch8_4 with dissolve 
    s "I couldn't sleep last night because I was thinking about you."
    mc "Oh, I-I see."
    mc "Did you... were you touching yourself?"
    scene ch8_2 with dissolve
    s "How do you know, you're a magician?"
    mc "By your face."
    s "You knew just by looking at my face? Hmm..."
    mc "And because you were touching yourself while you were waking me up."
    s "Hehe, that's true."
    s "But I didn't touch myself all night, just for a while and then I used the cell phone, and then I felt like touching myself again and I started touching myself, and then I got bored again but I felt like it again and..."
    s "What were we talking about? {w=0.5}ah, yeah, and then it was five o'clock and..."
    s "And I'm already here, hehe."
    mc "I see... do you touch yourself a lot, huh?"
    s "Only when I feel like it."
    mc "You feel like a lot of times..."
    scene ch8_4 with dissolve
    s "Yes, and right now I feel like it too, [mc]."
    s "Let's not waste any more time, okay?"
    s "I don't want us to be interrupted again."
    mc "We've got plenty of time."
    scene ch8_2 with dissolve
    s "Hehe."
    stop music fadeout 1.5
    pause
    scene ch8_5 with dissolve
    play music sexy3 fadein 1.5
    s "I'm already all soaked in here."
    s "My pussy needs your tongue, [mc]."
    s "I'm so wet and it's your fault."
    scene ch8_6 with dissolve
    mc "My fault?"
    s "Yes, whenever you're on my mind I get like this."
    mc "Do you always touch yourself thinking about me?"
    s "Yep."
    s "When I think about you doing things to me, it happens."
    mc "You get wet there..."
    s "Yeah."
    mc "Well, lie down on the bed and take off your clothes."
    s "Yes!"
    mc "{i}Keep your voice down!"
    s "{i}Sorry!"
    scene ch8_6-- with dissolve
    s "I'll just take off my shorts."
    mc "Just your shorts?"
    s "It's just... it's a little chilly."
    mc "As you wish."
    pause
    scene ch8_7 with dissolve
    pause
    mc "(Jesus...)"
    mc "(She's so beautiful...)"
    pause
    s "[mc], don't stare too much at me, it's embarrassing."
    mc "Are you embarrassed by me staring at you?"
    s "Yes, I know we've done it so many times, but..."
    s "It's just that, when you look at me with that face..."
    mc "(What face? Am I making a face and not realizing it?)"
    mc "Sorry."
    s "Don't be sorry, it's your face from when you see sexy things..."
    s "So it's okay if you see me with that face, that means you think I'm sexy."
    mc "Oh, well..."
    pause
    scene ch8_8- with dissolve
    mc "Spread your legs."
    s "Yeah..."
    pause
    scene ch8_10 with dissolve
    s "*Uhm*"
    s "H-today I'm very wet, I hope that doesn't bother you."
    mc "Of course not."
    s "*Hmm*"
    mc "Do you like it when I rub with my fingers like this?"
    s "Yes, *hmm*."
    pause
    scene ch8_11 with dissolve
    s "*Nhmm*"
    mc "God..."
    mc "What a nice..."
    mc "What a cute little pussy."
    s "*Hmn* haha, my pussy is all yours{image=redheart}."
    mc "(My cock just throbbed.)"
    pause
    scene ch8_12 with dissolve
    s "*Hah*..."
    mc "(My mouth is watering...)"
    mc "(It would be so easy to just jump on her and...)"
    mc "(God...)"
    pause
    scene ch8_9 with dissolve
    s "[mc], that feels good but..."
    s "I want you to use your tongue now, okay?"
    mc "Sure..."
    scene ch8_14 with dissolve
    s "*Uhh*, that feels good..."
    s "That feels so good."
    pause

init python:
    def ch8_8_sclng_1_(trans, st, at):  
        trans.set_child("ch8_8_scnlg{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value       
init python:
    def ch8_8_sclng_2_(trans, st, at):  
        trans.set_child("ch8_8_scnlg_2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

default last_sound = None
default random_number = 11
default frame_num = 1
default anim_speed = 0.055

screen animation_speed_settings8_pov1():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("after_8_scnlg") style "textbutton_choice"
        hbox:
            yalign 0.05
            xalign 0.99
            textbutton "Pov 2" action Jump("ch8_scnlgpov2") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen animation_speed_settings8_pov2():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("after_8_scnlg") style "textbutton_choice"
        hbox:
            yalign 0.05
            xalign 0.99
            textbutton "Pov 1" action Jump("ch8_scnlgpov1") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"

label ch8_8_scnlg_: 
    image ch8_8scnlg_1_:
        function ch8_8_sclng_1_ 
    image ch8_8scnlg_2_:
        function ch8_8_sclng_2_    
    scene ch8_8scnlg_1_ with dissolve       
    $ anim_speed = 0.07
    play voicefx "audio/wavs/s/smoansoft.ogg" loop
    s "*Uhhmm*"
    s "{i}It feels so gooood, [mc]{image=redheart}!"
    s "{i}Uhhh.."
    pause
    s "*Ouuhhh*"
    s "I-I'm...{w=0.5} I'm about to feel ''weird''."
    mc "Hm?"
    s "I'm going to..{w=0.7} do that thing."
    mc "(So fast?)"
    s "*Hm*"
    scene ch8_8scnlg_2_ with dissolve
    s "*Hmmng*"
    s "Right there, yeah, yeah."
    s "Yes, lick my pussy harder."
    $ anim_speed = 0.05
    s "*Uuhuhh, ah, ah!*"
    s "Harder, use your tongue harder, [mc]."
    pause
    jump ch8_scnlgpov1    
label ch8_scnlgpov2:
    scene ch8_8scnlg_2_ with dissolve
    call screen animation_speed_settings8_pov2 with dissolve
label ch8_scnlgpov1:
    scene ch8_8scnlg_1_ with dissolve
    call screen animation_speed_settings8_pov1 with dissolve       

label after_8_scnlg:  
    $ anim_speed = 0.012
    
    s "*Nghhh, hm, hm, hmmm!!*"
    mc "{size=-3}{i}Lower your voice!"
    pause
    image ch8_15image:
        "ch8_15" with hpunch 
        0.6
        "ch8_15" with hpunch 
        0.6
        "ch8_15" with hpunch 
        0.6
    scene ch8_15image with hpunch
    play voicefx "audio/wavs/s/s_softmoan_1.ogg"
    s "*Uuhhm!!!*{image=redheart}!"
    pause
    scene ch8_15- with dissolve
    s "Phew..."
    scene ch8_15-- with dissolve
    s "That was...{w=0.5} very good..."
    pause
    "..."
    pause
    mc "{w=0.5}?"
    s "..."
    pause
    mc "[s]."
    scene ch8_16 with dissolve
    pause
    s "*Fuu* That made me tired..."
    s "I didn't sleep, I guess that's why."
    s "I was afraid I wouldn't be able to wake up in time, really that's why I didn't sleep."
    mc "If you were five minutes late it didn't matter, but thank you for being on time."
    scene ch8_17 with dissolve
    pause
    s "..."
    s "You look very swollen..."
    mc "..."
    s "It got really big..."
    mc "Yes..."
    pause
    scene ch8_17 with dissolve
    mc "Erm, so are we done?"
    s "Yep..."
    pause
    s "What did you say?"
    mc "Well, since you're satisfied it's time to go to bed."
    scene ch8_19 with dissolve
    s "But it's still five o'clock, [mc]."
    s "We still have time to do more things."
    mc "So... What do you want to do now?"
    s "Hmm... {w=0.7}Shall we kiss?"
    pause
    mc "Sure..."
    scene ch8_20 with dissolve
    s "*Smnch*"
    pause
    scene ch8_21 with dissolve

    s "{i}Stick your dongue oud moh."
    mc "*Hmnsh*"
    pause
init python:
    def ch8_21_skis_(trans, st, at):  
        trans.set_child("ch8_21_skis_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
        
screen ch8_21_skis_settings():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("continuech8_21_skis_") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"
label ch8_skng1_:
    image ch8_21_skis_:
        function ch8_21_skis_
    $ anim_speed = 0.065        
    scene ch8_21_skis_ with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    s "*Nham, nhm, nham*"
    call screen ch8_21_skis_settings with dissolve
label continuech8_21_skis_:
    scene ch8_22- with dissolve
    stop sound fadeout 0.5
    s "*Bdah*"
    s "{i}Sloppy kiss{/i}{image=redheart}."
    pause
    scene ch8_23 with dissolve
    pause
    scene ch8_24 with dissolve
    s "I like kisses with tongue and lots and lots of saliva..."
    s "Do you like them?"
    mc "Yes, I like them too..."
    pause
    scene ch8_25 with dissolve
    pause
    s "It's pretty swollen."
    mc "Hey-"
    scene ch8_26 with dissolve
    mc "Uh..."
    s "It's always so hard..."
    pause
    scene ch8_24 with dissolve
    s "Is it okay if I touch?"
    mc "S-sure, you can touch if you want."
    mc "Just... touch."
    pause
    scene ch8_27 with dissolve
    s "I love you, [mc]."
    pause
    scene ch8_28 with dissolve
    s "I like you so, so, so much!"
    s "Who do you like more, [k] or me?"
    mc "Don't ask me that kind of question."
    mc "I love both of you."
    s "I'll make you love me more."
    pause
    scene ch8_29 with dissolve
    s "I love your kisses, [mc]."
    mc "You like my kisses?"
    s "Yup, I like them a lot."
    pause
    scene ch8_30 with dissolve
    s "And I also like your body..."
    s "Because you're very strong."
    s "I like your muscles."
    pause
    scene ch8_32 with dissolve
    s "That's why I'm going to cover you with kisses all over."
    s "Because I really like you, I like everything about you."
    pause
    image ch8_30_31_32_:
        "ch8_32" with dissolve
        1.5
        "ch8_30" with dissolve
        1.5
        "ch8_31" with dissolve
        1.5
        "ch8_30" with dissolve
        1.5
        repeat
    scene ch8_30_31_32_ with dissolve
    s "*Muah*, a little kiss on your chest."
    s "And another one, *muah*, on your belly too."
    mc "Hmm..."
    s "*Muah*, I'm gonna cover you in kisses all over{image=redheart}."
    pause
    image ch8_35_36_34:
        "ch8_34" with dissolve
        1.5
        "ch8_36" with dissolve
        1.5
        "ch8_35" with dissolve
        1.5
        "ch8_36" with dissolve
        1.5
        repeat
    scene ch8_35_36_34 with dissolve 
    mc "(I am being seduced...)"
    s "*Muha, muah, muah*"
    mc "(Her kisses are so tender.)"
    mc "(I've never had my body kissed so tenderly before.)"
    scene ch8_47---- with dissolve
    s "I want to kiss you on the mouth again."
    pause
    scene ch8_49 with dissolve
    s "Am I squishing you?"
    mc "It would take about ten of you for that."
    scene ch8_48 with dissolve
    s "Why? Because I'm short?"
    mc "You're my little one."
    s "Silly, you know I don't like being called that."
    mc "Haha, it's affectionate."
    s "I know."
    pause
    s "You have that face again."
    s "You really liked my kisses, didn't you?"
    mc "Yes."
    s "Well, there go more kisses."
    pause
    scene ch8_51 with dissolve
    s "*Smch*"
    pause
    scene ch8_50 with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    s "*Muah*"
    pause
    scene ch8_51 with dissolve
    s "*Hmm*"
    scene ch8_52 with dissolve
    pause
    scene ch8_47--- with dissolve
    s "What's that between my legs, hmm?"
    s "Is that your penis?"
    mc "I think it came out of my underpants."
    s "Bad penis."
    pause
    scene ch8_47_stjb_1_pov1_20 with dissolve
    stop sound fadeout 0.5
    s "This will teach him not to act on his own."
    s "I'm going to squeeze him with my legs as punishment."
    mc "Uh.."
    pause
    $ anim_speed = 0.065
    scene ch8_47_stjb_1_pov1 with dissolve
    play voicefx "audio/wavs/s/smoansoft.ogg" loop
    s "Bad... {w=1.25}penis..."
    mc "*Oh, hmm*..."
    image ch8_55-56:
        "ch8_56" with dissolve
        1.5
        "ch8_55" with dissolve
        1.5
        repeat
    scene ch8_55-56 with dissolve
    mc "Hmm, [s]..."
    s "You're a bad... {w=0.5}very... {w=0.58}bad... {w=0.58}penis."
    pause

init python:
    store.last_played_sound = None
    def ch8_47_stjb_2_pov1(trans, st, at):  
        trans.set_child("ch8_47_stjb_2_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fuckwet2.ogg", "audio/sex/fuckwet3.ogg", "audio/sex/fuckwet4.ogg", "audio/sex/fuckwet5.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voicefx(random_sound)()        
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    store.last_played_sound = None
    def ch8_47_stjb_2_pov2(trans, st, at):  
        trans.set_child("ch8_47_stjb_2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fuckwet2.ogg", "audio/sex/fuckwet3.ogg", "audio/sex/fuckwet4.ogg", "audio/sex/fuckwet5.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voicefx(random_sound)()       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
init python:
    store.last_played_sound = None
    def ch8_47_stjb_1_pov1(trans, st, at):  
        trans.set_child("ch8_47_stjb_1_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 28:
            sound_files = ["audio/sex/fuckwet2.ogg", "audio/sex/fuckwet3.ogg", "audio/sex/fuckwet4.ogg", "audio/sex/fuckwet5.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voicefx(random_sound)()       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

$ last_sound = None
$ random_number = 11
$ frame_num = 1  
screen animation_settings_ch8_47_stjb_1_pov1():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("after_anim_settings_stjb_1_pov1") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"

screen animation_settings_ch8_47_stjb_2_pov1():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continueafterch8_47_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_47_stjb_2_pov2label") style "textbutton_choice"    
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 

screen animation_settings_ch8_47_stjb_2_pov2():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continueafterch8_47_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_47_stjb_2_pov1label") style "textbutton_choice"    
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    


label ch8_55anim:
    image ch8_47_stjb_1_pov1:
        function ch8_47_stjb_1_pov1
    image ch8_47_stjb_2_pov1:
        function ch8_47_stjb_2_pov1
    image ch8_47_stjb_2_pov2:
        function ch8_47_stjb_2_pov2    
    scene ch8_47_stjb_1_pov1 with dissolve  
    mc "[s]..."
    s "Bad... {w=1.25}penis...{w=1.25} bad... {w=1.25}penis..."
    s "I'm going to punish him for a while longer..."
    s "Just to make sure he has.... {w=0.5}learned the lesson."
    mc "(So good...)"
    call screen animation_settings_ch8_47_stjb_1_pov1 with dissolve   
label after_anim_settings_stjb_1_pov1:    
    $ anim_speed = 0.02    
    s "Uh, [mc]."
    s "Your penis feels really good between my legs..."
    s "When it rubs against my vagina it feels really nice..."
    pause
    s "I-I'm getting tired already, [mc]."
    mc "Wait, just a little more."
    s "Yes."
    pause
    scene ch8_47_stjb_2_pov1 with dissolve
    s "Uh!, hehe..."
    s "Uhm, I like it when you squeeze me like that."
    mc "Do you like it when your [srelatmc] squeezes your little butt?"
    s "Yes, I like it very much."
    s "*Uh, hmm, hmm, hm, hmm*"
    scene ch8_47_stjb_2_pov2 with dissolve 
    s "I'm going to do that again..."
    s "I'm going to feel... Uh!,{w=0.5} pleasure."
    mc "*Hmng*, (Me too.)"
label ch8_47_stjb_2_pov1label:
    scene ch8_47_stjb_2_pov1 with dissolve
    call screen animation_settings_ch8_47_stjb_2_pov1 with dissolve
label ch8_47_stjb_2_pov2label:
    scene ch8_47_stjb_2_pov2 with dissolve 
    call screen animation_settings_ch8_47_stjb_2_pov2 with dissolve 
label continueafterch8_47_:
    $ anim_speed = 0.015      
    s "*Hmmn, hmmmg!*"
    s "*Ahmg!*" with hpunch
    s "Uh, hmm..." with hpunch    
    pause
    s "I think..."
    s "I think he's learned his lesson."
    mc "Just a little bit more..."
    s "My hips are tired already, [mc]."
    s "Stop, [mc]. I need to rest."
    pause
    stop sound fadeout 0.5
    scene ch8_37 with dissolve
    mc "[s], I still don't..."
    s "You've still got it swollen, I know, but my hips are tired already."
    mc "..."
    s "This time it didn't get flabby after rubbing, so..."
    s "What else can we do? hmm..."
    pause
    mc "(She want me to enjoy it too, so cute...)"
    pause
    s "Maybe..."
    pause
    scene ch8_37- with dissolve
    pause
    s "Uh... {w=0.5} maybe you need more kisses."
    mc "M-more kisses?"
    s "Yes, I think your penis needs more affection."
    scene ch8_39 with dissolve
    s "I-I'm going to give it some love, okay, [mc]?"
    mc "L-love?"
    s "Yes, may I?"
    mc "[s]-{p=0.5}{nw}"
    s "If you don't want to, that's fine!"
    s "I just want to see it up close, that's all, okay?"
    mc "[s]-{p=0.5}{nw}"
    s "[mc]!"
    pause
    s "[k] is your favorite, right?"
    s "You let [k] do whatever she wants to you..."
    s "It's unfair of you..."
    mc "This conversation again... I've told you it's not like that."
    s "So?"
    pause
    mc "(When she makes that face I just can't say no to her.)"
    mc "A-Alright..."
    mc "But get that idea out of your mind, I don't love [k] more than I love you, I've told you that before."
    s "Yes!"
    pause
    scene ch8_41 with dissolve
    pause
    mc "(After all we've done, this isn't that big of a deal, I guess.)"
    mc "(Who cares if she wants to give me a couple of kisses in.... {w=0.5}Ok, that's not okay at all.)"
    mc "No funny stuff, ok?"
    s "Yeah, I just want to see it and.... {w=0.5}see it."
    pause
    scene ch8_40 with dissolve
    s "Wow... it looks even bigger up close."
    s "It's too big."
    s "Have you been to the doctor to check it out?"
    mc "Why do you say that?"
    s "I think you're a little... deformed."
    mc "Deformed?"
    s "This isn't a normal size, is it?"
    mc "I don't think this qualifies as ''deformity''."
    s "Well, I think it does."
    s "It's thicker than my arm."
    pause
    s "I'm sorry I punished you."
    s "You just have to behave and there won't be any more punishments, okay?"
    mc "(She's talking to my penis...)"
init python:
    def ch8_45_std(trans, st, at):  
        trans.set_child("ch8_45_std_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
screen after_ch8_spmsj():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.018) style "textbutton_choice"        
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("after_ch8_spmsj") style "textbutton_choice"
        #hbox:
            #yalign 0.05
            #xalign 0.99
            #textbutton "Pov 2" action Jump("ch8_scnlgpov2") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
        
label ch8_45_stdas:
    image ch8_45_std:
        function ch8_45_std
    $ anim_speed = 0.065    
    scene ch8_45_std with dissolve
    mc "Uh... [s]."
    mc "W-what are you doing?"
    s "It's just a massage to make him feel better."
    s "I squeezed him too hard with my legs, and I think I hurt you..."
    s "I mean, I hurt him."
    pause
    mc "Don't worry, you didn't."
    mc "He...{w=0.5} liked it."
    s "Really?"
    mc "I assure you."
    pause
    s "Does this feel good?"
    pause
    mc "Are you talking to me or him?"
    s "B-both."
    mc "It feels really good."
    pause
    call screen after_ch8_spmsj   
label after_ch8_spmsj:
    $ anim_speed = 0.018
    s "Hmm, not working."
    pause
    scene ch8_41 with dissolve
    s "Oh..."
    scene ch8_42 with dissolve
    s "It's coming out this..."
    s "Is it your semen?"
    mc "N-no, it's the stuff that comes out before the white liquid comes out."
    s "The stuff that comes out before your milk?"
    mc "Yes, before my ''milk''."
    s "Hmm..."
    pause
    scene ch8_43 with dissolve
    mc "Hey..."
    pause
    scene ch8_44 with dissolve
    s "It's very sticky."
    pause
    scene ch8_57 with dissolve
    s "*Nam*."
    mc "What are you doing!"
    pause
    scene ch8_45 with dissolve
    s "It doesn't taste like anything."
    mc "You didn't have to do that..."
    s "I was curious to know what it tastes like."
    pause
    scene ch8_58 with dissolve
    s "Wow..."
    s "You have a lot of veins."
    s "It looks like you're straining."
    scene ch8_61 with dissolve
    pause
    s "And he's got this big vein in the middle."
    mc "Th-that's not a vein."
    s "Ah, that's right, that's where the urine goes through."
    s "Nice."
    pause
    scene ch8_59- with dissolve
    pause
    s "Uhm, [mc]."
    mc "Y-yes?"
    s "Will you let me kiss him?"
    s "Just a little kiss."
    mc "J-just a kiss..."
    pause
    scene ch8_59 with dissolve
    s "*Hmnch*"
    pause
    scene ch8_59- with dissolve
    play sound "audio/mouth/kiss_01.ogg"
    pause
    s "Maybe I should give you another..." 
    pause
    scene ch8_60 with dissolve
    s "*Smnch*"
    mc "W-We said..."
    pause
    pause
    image ch8_5959-60:
        "ch8_59-" with dissolve
        function atl_play_sound("audio/mouth/kiss_01.ogg")
        1.5
        "ch8_59" with dissolve
        1.5
        "ch8_59-" with dissolve
        function atl_play_sound("audio/mouth/kiss_02.ogg")
        1.5   
        "ch8_60" with dissolve
        1.5
    scene ch8_5959-60 with dissolve
    mc "We said just a kiss..."
    mc "(She's not listening...)"
    pause
    scene ch8_62 with dissolve
    s "*Smnch*"
    mc "Ah..."
    pause
    scene ch8_64 with dissolve
    pause
    scene ch8_64- with dissolve
    play sound "audio/mouth/kiss_01.ogg"
    s "*Muah*"
    pause
    s "The head deserves love too."
    pause
    image ch8_6464-:
        "ch8_64" with dissolve
        2.0
        "ch8_64" with dissolve
        1.5
        repeat
    scene ch8_6464- with dissolve
    s "*Mnch*"
    s "*Muah*"
    pause
    image ch8_6363--:
        "ch8_63" with dissolve
        2.0
        "ch8_63--" with dissolve
        1.5
        repeat
    scene ch8_6363-- with dissolve
    pause
    mc "(Oh, God...)"
    mc "(It feels so good...)"
    s "It's throbbing, [mc]."
    mc "Yeah, hmmhm, I know..."
    mc "It's because it feels so good."
    s "Is it because of my kisses?"
    mc "Yes.."
    s "Then I'll keep kissing it."
    s "Many, many, many, many kisses{image=redheart}."
    mc "(As long as it's just kisses it's okay...)"
    pause
    scene ch8_63-- with dissolve
    s "Although maybe... maybe just kisses isn't enough..."
    mc "What do you mean...?..."
    pause
    scene ch8_59- with dissolve
    pause
    scene ch8_59 with dissolve
    pause
    scene ch8_60 with dissolve
    pause
    scene ch8_58_slick_pov1_1 with dissolve
    s "*Dahh*..."
init python:
    def ch8_58_slick_pov1_(trans, st, at):  
        trans.set_child("ch8_58_slick_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
screen ch8_58_slick_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.045) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.03) style "textbutton_choice"        
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_58_slick_pov1_settings") style "textbutton_choice"
        #hbox:
            #yalign 0.05
            #xalign 0.99
            #textbutton "Pov 2" action Jump("ch8_scnlgpov2") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

label ch8_58_slick_pov1before:
    image ch8_58_slick_pov1_:
        function ch8_58_slick_pov1_
    $ anim_speed = 0.065
    scene ch8_58_slick_pov1_ with dissolve
    mc "[s]..."
    s "*Lham, ahm, nam*"
    mc "(Oh, God...)"
    s "Does it feel good when I run my tongue over it?"
    mc "Yes, very good..."
    mc "B-but... why are you doing it?"
    s "I want your penis to feel good."
    s "[k] did something like this that time and it deflated."
    call screen ch8_58_slick_pov1_settings with dissolve
label afterch8_58_slick_pov1_settings:    
    mc "Is... is that enough."
    s "Yes, that's enough licking here."
    pause
    scene ch8_58_slick_2_pov_2_1 with dissolve
    s "I forgot the little head."

init python:
    def ch8_58_slick_2_pov_2_(trans, st, at):  
        trans.set_child("ch8_58_slick_2_pov_2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_58_slick_2_pov_2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"        
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_58afterlick_") style "textbutton_choice"
        #hbox:
            #yalign 0.05
            #xalign 0.99
            #textbutton "Pov 2" action Jump("ch8_scnlgpov2") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

label ch8_58_slick_2_pov_2_label:
    image ch8_58_slick_2_pov_2_:
        function ch8_58_slick_2_pov_2_
    $ anim_speed = 0.035    
    scene ch8_58_slick_2_pov_2_ with dissolve
    mc "*Uh*.... *hmm*, o-hey..."
    mc "(I can't stop her, not at this point...)"
    mc "(It feels too good... I feel like I'm going to cum any minute.)"
    mc "(Be strong, [mc]!)"
    s "*Lah, lah, lah*"
    s "It's throbbing so much more..."
    s "That's where the little head starts is your weak spot, isn't it?"
    s "When I lick up and down it throbs quite a bit..." 
    mc "Yes... there, hmm."
    mc "That spot is very sensitive."
    call screen ch8_58_slick_2_pov_2_settings with dissolve
label ch8_58afterlick_:
    s "It's getting more and more swollen."
    s "And that clear stuff is spilling out all over your penis."
    s "It's on my tongue..."
    mc "Sorry, I can't control it."
    s "I don't mind."
    pause
    scene ch8_64 with dissolve
    "{w=0.5}{nw}"
    play sound "audio/mouth/kiss_01.ogg"
    scene ch8_64- with dissolve
    s "Still going out..."
    "..."
    pause
    scene ch8_64 with dissolve
    "{w=0.5}{nw}"
    scene ch8_64-- with dissolve
    mc "(Jesus...)"
    pause
    play sound "audio/wavs/bj_33.ogg"
    scene ch8_64- with dissolve
    s "It never ends..."
    s "Poor little thing..."
    pause
    s "[mc]."
    mc "Yes?"
    s "I think... I think I want to, I mean, he wants to get sucked."
    s "I'm going to suck it a little bit, okay?"
    s "To make it feel better."
    mc "Y-you don't have to do that, [s]..."
    s "I want to do it, [mc]."
    s "I want to know what it feels like...{w=0.5} to suck your penis."
    s "Can I suck it for you?"
    mc "..."
    s "Just the tip?"
    mc "... (What am I supposed to answer?)"
    mc "(I tell her no so she'll make a drama later and say I love [k] more than her... or I tell her yes and...)"
    mc "(What do I do?)"
    pause
    s "I'm going to do it, ok?...."
    pause
    scene ch8_64 with dissolve
    pause 0.5
    scene ch8_64-- with dissolve
    pause 0.5
    scene ch8_66 with dissolve
    mc "(Fuck...)"
    pause
    scene ch8_58_s_suck_pov1_1 with dissolve
    mc "(I can't let this happen, otherwise this will just keep escalating more and more and...)"
    scene ch8_67- with dissolve
    mc "[s], I can't-.... {w=0.5}{size=-5}we can't..."
    pause
    mc "(Who the hell am I kidding?)"
    mc "..."
    pause
    mc "You just want to make your [srelatmc] feel good, don't you?"
    s "U-hum."
    mc "You won't tell anyone ever, will you?"
    s "Uh-um."
    mc "O-ok..."
    pause
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_58_s_suck_pov1_(trans, st, at):  
        trans.set_child("ch8_58_s_suck_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_31.ogg", "audio/wavs/bj_34.ogg", "audio/wavs/bj_19.ogg", "audio/wavs/bj_36.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 45:
            sound_files = ["audio/wavs/bj_30.ogg", "audio/wavs/bj_13.ogg", "audio/wavs/bj_25.ogg", "audio/wavs/bj_28.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_58_s_suck_pov2_(trans, st, at):  
        trans.set_child("ch8_58_s_suck_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_31.ogg", "audio/wavs/bj_34.ogg", "audio/wavs/bj_19.ogg", "audio/wavs/bj_36.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 45:
            sound_files = ["audio/wavs/bj_30.ogg", "audio/wavs/bj_13.ogg", "audio/wavs/bj_25.ogg", "audio/wavs/bj_28.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
screen ch8_58_s_suck_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_58_s_suck_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_58_s_suck_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

screen ch8_58_s_suck_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.065) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_58_s_suck_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_58_s_suck_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"              

label ch8_58_s_suck_pov1_first:
    image ch8_58_s_suck_pov1_:
        function ch8_58_s_suck_pov1_
    image ch8_58_s_suck_pov2_:
        function ch8_58_s_suck_pov2_ 
    $ anim_speed = 0.065
    scene ch8_58_s_suck_pov1_ with dissolve
    pause
    mc "(God...)"
    mc "(Her little lips feel amazing.)"
    mc "*Hmm*..."
    mc "(She's sucking it so good...)"
    mc "(Even if she's sucking only the glans feels so damn good...)"
    pause
    mc "(Her saliva spills from the tip to the base.)"
    mc "(It's like my penis has her favorite flavor.)"
    pause
    scene ch8_67- with dissolve
    s "*Hehe*{i}, It's so big that the tip barely fits in my mouth"
    s "{i}I'm doing it right?"
    mc "Y-yes, you're doing great."
    pause
    scene ch8_58_s_suck_pov1_ with dissolve
    pause
    s "{i}Id feehls gooh?"
    mc "Very good..."
    pause
    mc "(She's sucking kind of hard, like she wants to get the stuffing out of me.)"
    mc "(I've never gotten a blowjob like this before...)"
    mc "(Maybe it's because of the ''forbidden'' but this feels so different than anything else.)"
    call screen ch8_58_s_suck_pov1_settings with dissolve
    pause
label ch8_58_s_suck_pov1_:
    scene ch8_58_s_suck_pov1_ with dissolve
    call screen ch8_58_s_suck_pov1_settings with dissolve
label ch8_58_s_suck_pov2_:
    scene ch8_58_s_suck_pov2_ with dissolve
    call screen ch8_58_s_suck_pov2_settings with dissolve   

label afterch8_58_s_suck_pov1_settings:
    mc "*Nhg, mhng*"
    mc "(Shit, I'm about to cum.)"
    mc "(But I won't do it in her mouth, that would be too much, even for her.)"
    mc "*Hngh!* [s], wait... wait a second."
    scene ch8_67- with dissolve
    mc "I'm going- {w=0.3}I'm going to cum now."
    s "{i}What?"
    mc "I'm going to cum now, *Nggh!!!*"
    scene ch8_68 with dissolve
    s "You're all red-"
    scene ch8_69 with cumming
    pause 0.0
    with flash
    mc "*Rgh!!!*"
    scene ch8_70 with dissolve
    pause
    s "Uh..."
    mc "Ah.{w=0.2}.{w=0.2}. {w=0.5}S-sorry!"
    s "Eh- {w=0.5}it's on my face..."
    mc "I-I didn't mean to do that!"
    mc "I'll get you something to clean you up."
    mc "(I really screwed up this time!)"
    scene ch8_71 with dissolve
    s "It finally came out!"
    mc "Huh?"
    s "That's because I did really well, right?"
    mc "Yeah, but-{p=0.25}{nw}"
    s "-Who does it better, [k] or me?"
    mc "Uh..."
    mc "(She doesn't even seem to care...)"
    mc "I've already told you not to ask me those kinds of questions."
    s "Obviously me."
    scene ch8_72 with dissolve
    s "I think I deserve a kiss now."
    mc "Ehh..."
    mc "B-better later."
    scene ch8_73 with dissolve
    s "Come give me a little kiss!"
    mc "At least let me wipe your face."
    s "Does your own semen disgust you?"
    mc "Actually, a little bit."
    s "Kiss me!"
    mc "I don't!"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blackscreen with Dissolve(2.0)
    pause
label ch8_74scene:
    scene ch8_318 with dissolve
    mc "*Yawn*..."
    if stephloving == "True":
        mc "(I fell asleep.)"
        mc "..."
        mc "(I can't believe she made me kiss her...)"
        mc "(I have dry cum on my legs...)"
    mc "I need a shower..."
    scene blackscreen with dissolve
    pause
    scene ch8_74 with dissolve
    play music scene1 fadein 1.0
    mc "..."
    mc "(I'm supposed to act like nothing that happened yesterday really happened, so that's what I'll do.)"
    pause
    scene ch8_75 with dissolve
    a "Oh, good morning, [mc]."
    mc "Good morning."
    a "Are you going to have breakfast?"
    a "I made bacon and eggs."
    mc "Of course, it looks delicious."
    pause
    a "..."
    mc "I was thinking that we could spend some time together, like yesterday."
    scene ch8_76 with dissolve
    a "Eh..."
    a "Like yesterday?"
    mc "Yes."
    mc "You and me having a drink outside, in the backyard."
    a "{size=-5}{i}Ah, you mean that. {p=0.25}{nw}"
    scene ch8_77 with dissolve
    a "Sure."
    a "In fact, I was thinking we could go buy the lights you mentioned yesterday."
    mc "Oh, right, the pendant lamps."
    mc "I know where they sell them. Shall we go later?"
    a "Sure."
    mc "Do you want me to help you with that?"
    a "With what, the fried eggs?"
    a "It's a tough task, but I think I can handle it on my own."
    mc "Haha, just trying to help."
    a "They'll be ready soon. Why don't you go wake up the girls instead?"
    mc "Sure."
    scene ch8_77_1 with fade
    pause
    mc "It's the [drelat] [d]."
    scene ch8_77_3 with dissolve
    d "Oh, hey."
    d "Good morning, [mc]."
    mc "Good morning."
    d "Hey, son, uh... I need the apartment keys, do you have them, right?"
    mc "Yes, do you need them?"
    d "Yes, please give them to me."
    mc "Sure, they're in my room. I'll get them for you."
    d "Thank you."
    scene blackscreen with dissolve
    pause
    scene ch8_77_5 with dissolve
    pause
    scene ch8_77_4 with fade
    d "Thank you, son."
    mc "Are you leaving?"
    d "I'm going to have breakfast somewhere, you know..."
    mc "Yeah... I know things aren't going very well between you and [arelat] [a]."
    d "Yes..."
    d "Hey, do you want to join me?"
    mc "[a] just served me my plate, sorry..."
    d "It's okay, don't worry."
    d "Tell the girls I'll be back later."
    mc "Sure."
    d "See you."
    scene ch8_77_1 with dissolve
    pause
    scene ch8_77_8 with dissolve
    k "Is he gone already?"
    mc "Were you listening?"
    k "Dad won't have breakfast with us?"
    mc "He said he'll have breakfast elsewhere."
    scene ch8_77_7 with dissolve
    k "I don't like this."
    pause
    k "What did you talk about?"
    mc "Nothing, he just asked for the apartment keys back."
    scene ch8_77_8 with dissolve
    k "He asked for the keys back?"
    mc "Yes, that's what I said."
    mc "He also mentioned he might be back late."
    pause
    scene ch8_77_9 with dissolve
    k "Wait... he might be back late?"
    k "We have at least a couple of hours without him at home..."
    mc "But I don't have the apartment keys."
    k "Why would we need those stupid apartment keys?"
    scene ch8_77_10 with dissolve
    a "Breakfast is served!"
    mc "I have to go wake up [s]."
    scene ch8_77_11 with dissolve
    k "We have to make the most of these hours."
    mc "You mean..."
    k "Obviously, dummy."
    mc "But, here?"
    scene ch8_77_10 with dissolve
    a "It's going to get cold!"
    mc "We're coming!"
    scene ch8_77_11 with dissolve
    mc "Let's talk about this after breakfast."
    k "Okay."
    scene blackscreen with dissolve
    pause
    scene ch8_78 with dissolve
    a "And all we saw were airplanes, right, [mc]?"
    mc "Yeah, it was very disappointing."
    scene ch8_79 with dissolve
    k "Why go out to see some stupid stars when you have the most beautiful star in the entire universe here at home?"
    scene ch8_80 with dissolve
    a "I heard that joke yesterday already."
    pause
    if stephloving == "True":
        scene ch8_82 with dissolve
        a "Sweetie, your food is going to get cold."
        a "Sweetie?"
        "..."
        pause
        k "What she's thinking about?"
        k "Look at her, she's even smiling, haha."
        k "Earth to [s]."
        a "[s], honey."
        scene ch8_83 with dissolve
        s "What?"
        a "You haven't taken a single bite of the bacon."
        s "Oh, sorry."
        scene ch8_84 with dissolve
        s "I couldn't sleep well last night, that's why I'm so tired."
        pause
        s "Right, [mc]?"
        mc "Yeah, I guess so, I-I don't know."
        mc "(Can you be any less obvious?!)"
        a "Eat quickly, and then you can go back to sleep."
        s "Okay."
        scene ch8_88 with dissolve
        s "Next time, I want to watch the meteor shower with you too, [mc]."
        mc "Of course."
        scene ch8_84 with dissolve
        k "Uh-huh, lost in thought, you say, but you heard everything."
        scene ch8_85 with dissolve
        s "Ugh... Of course I heard, I'm right here you silly."
        a "The next meteor shower is like in 5 years, honey."
        k "And by then, you'll have someone special to watch them with..."
        scene ch8_89 with dissolve
        s "[mc], that's a lie, I wouldn't trade you for anyone."
        mc "That's what they all say, haha."
        s "Maybe you think [k] would, but not me, never."
        s "I'm not like everyone else, and definitely not like [k]."
        k "What are you trying to say?!"
        scene ch8_87 with dissolve
        s "That you're a bitch!"
        a "[s]!!"
        k "Why so aggressive? Though it's true."
        a "[k]..."
    scene ch8_91 with dissolve
    k "Hey, [arelatks]."
    k "You and Dad..."
    k "Was there something that bothered you yesterday?"
    k "I saw you very uncomfortable all day, and then the yacht thing happened, and..."
    k "Is everything okay?"
    a "No, I..."
    k "What a question, obviously nothing is okay."
    a "I'm afraid not..."
    a "By the way, it's strange that he hasn't woken up yet."
    k "He just left."
    a "Oh, that explains it."
    a "And where did he go?"
    k "To have breakfast somewhere else, or at least that's what he said."
    a "Well, whatever."
    scene ch8_86 with dissolve
    a "I'm sorry for ruining your day yesterday."
    k "Don't worry about it."
    scene ch8_90 with dissolve
    k "You're right, [arelatks]."
    k "I wouldn't forgive him so easily either."
    scene ch8_91 with dissolve
    k "I'm on your side, okay, [arelatks]?"
    k "We all are."
    s "Yep."
    a "Thank you, guys... but he's still your father, dont hate him because of this."
    pause
    scene ch8_92 with dissolve
    k "Well, I'm done. Breakfast was really good, [arelatks]."
    pause
    scene ch8_93 with dissolve
    pause
    mc "({i}''Come..{w=0.5} with me..{w=0.5} upstairs..''{/i})"
    pause
    mc "I'm finished too, thanks [a], it was really good."
    stop music fadeout  1.5
    scene blackscreen with dissolve
    pause
label ch8k1:
    if _in_replay:
        show screen Replayexit
    scene ch8_94 with dissolve
    k "Quick!"
    mc "What, what's going on?"
    scene ch8_95 with vpunch
    mc "Ouch!, Hey, calm down!"
    k "Hurry up!!"
    pause
    scene ch8_96 with fade
    play music sexy1 fadein 1.0
    k "Mmmhmm."
    pause
    scene ch8_97 with dissolve
    k "I can't take it anymore, take everything off right now."
    scene ch8_98 with dissolve
    mc "Are we doing it here?"
    k "Yes, quickly, take off your clothes."
    pause
    scene ch8_99 with dissolve
    mc "They'll catch us."
    k "They won't."
    mc "Can you not moan?"
    k "We'll turn on the washing machine."
    mc "Clever."
    k "Take off your clothes now."
    pause
    scene ch8_103 with dissolve
    pause
    scene ch8_103 with dissolve
    k "Quick, we don't have all day!"
    pause
    scene ch8_104 with dissolve
    k "Hmm... *giggles*"
    mc "Did you miss my huge cock?"
    k "Yes."
    k "And it looks like your dick missed me too."
    mc "Definitely."
    mc "I missed those blowjobs with those slutty lips of yours."
    k "You want me to use my lips now?"
    mc "Oh, yeah."
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_105_kbj_1_pov1_(trans, st, at):
        trans.set_child("ch8_105_kbj_1_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_43.ogg", "audio/wavs/bj_45.ogg", "audio/wavs/bj_47.ogg", "audio/wavs/bj_49.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voicefx(random_sound)()        
        if store.frame_num == 45:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_54.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bjgags3.ogg", "audio/wavs/bjgags5.ogg", "audio/wavs/bjgags11.ogg"]
            sound_files2 = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_sound2 = renpy.random.choice([sound for sound in sound_files2 if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
            if random_chance > 0.1:
                store.last_played_sound3 = random_sound2
                atl_play_voicefx(random_sound2)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_105_kbj_1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.0094) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_105_kbj_1_pov1_settings") style "textbutton_choice"
        #hbox:
            #yalign 0.05
            #xalign 0.99
            #textbutton "Pov 2" action Jump("ch8_scnlgpov2") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label ch8_105_kbj_1_:
    image ch8_105_kbj_1_pov1:
        function ch8_105_kbj_1_pov1_
    $ anim_speed = 0.035    
    scene ch8_105_kbj_1_pov1 with dissolve
    mc "Oh, hmm.."
    mc "I love how you suck it so deep and without gagging."
    pause
    mc "You didn't seem to like sucking my cock before."
    mc "Now you love it, huh?"
    k "*Gugh, gug, gag, gag*, {i}Shudup."
    pause
    mc "Hmm, that, keep it up, keep sucking like that."
    pause
    call screen ch8_105_kbj_1_pov1_settings with dissolve
label afterch8_105_kbj_1_pov1_settings:
    mc "Oh, yeah... *ngh*."
    scene ch8_107 with dissolve
    k "Not yet, {i}I want you to fuck me!"
    k "We're short on time."
    mc "Get naked."
    k "Yes."
    scene ch8_108 with dissolve
    mc "Turn on the washing machine now."
    k "Good thinking."
    mc "And take everything off, including your blouse."
    pause
    scene ch8_108- with dissolve
    mc "Hmmm, what an ass."
    k "Consider yourself lucky to be able to touch it."
    mc "I definitely am."
    scene ch8_109 with dissolve
    k "Hmmm..."
    pause
    scene ch8_112 with dissolve
    k "*Uh, hmm*."
    pause
    scene ch8_113 with dissolve
    mc "You're all wet already."
    k "{i}Give it to me now, [mc]."
    mc "It's so sexy when you beg for my cock."
    k "You'd love that."
    pause
    scene ch8_110 with dissolve
    mc "You're so hot.."
    mc "You don't know how I miss your tits and this beautiful ass you have."
    pause
    scene ch8_114 with dissolve
    pause
    scene ch8_115 with dissolve
    k "*Ah*..."
    mc "Uh, I didn't remember you being so tight, *hmmm*."
    pause
    scene ch8_116 with dissolve
    mc "I'm going to fuck you so hard you're not going to know whether to cum or fall in love."
    k "Oh yeah? Well I want to see you try."
    mc "Do you want me to make you fall in love with me?"
    mc "Sorry, you're not my type."
    k "You idiot."
    k "Stop talking and fuck me hard."
init python:
    store.last_played_sound2 = None
    def ch8_kfuck1_pov1_(trans, st, at):  
        trans.set_child("ch8_kfuck1_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1 
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_sound(random_sound)() 
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_kfuck1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0105) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.00996) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_kfuck2_cum") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.01
        textbutton "Pose 2" action Jump("ch8_kfuck2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
############################################################################
init python:
    store.last_played_sound2 = None
    def ch8_kfuck2_pov1_(trans, st, at):  
        trans.set_child("ch8_kfuck2_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_sound(random_sound)() 
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_kfuck2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0105) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.0099) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_kfuck2_cum") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 2" action Jump("ch8_kfuck2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_kfuck2_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.01
        textbutton "Pose 1" action Jump("ch8_kfuck1_pov1_") style "textbutton_choice"

    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

####################################################################################
init python:
    store.last_played_sound2 = None
    def ch8_kfuck2_pov2_(trans, st, at):  
        trans.set_child("ch8_kfuck2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_sound(random_sound)() 
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_kfuck2_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0105) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.0099) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_kfuck2_cum") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 1" action Jump("ch8_kfuck2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_kfuck2_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.01
        textbutton "Pose 1" action Jump("ch8_kfuck1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
############################################################################################################
init python:
    store.last_played_sound2 = None
    def ch8_kfuck2_pov3_(trans, st, at):  
        trans.set_child("ch8_kfuck2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_sound(random_sound)() 
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_kfuck2_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0105) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.0099) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_kfuck2_cum") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 1" action Jump("ch8_kfuck2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_kfuck2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.01
        textbutton "Pose 1" action Jump("ch8_kfuck1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
############################################################################################################

label beforech8_kfuck1_pov1_:        
    image ch8_kfuck1_pov1__:
        function ch8_kfuck1_pov1_
    $ anim_speed = 0.025   
    scene ch8_kfuck1_pov1__ with dissolve

label afterch8_kfuck1_pov1_1:
    play voicefx "audio/wavs/k/kmoansoft.ogg" volume 0.4 loop
    $ anim_speed = 0.01
    k "Start slow."
    k "*Ah, hah, ah, aah*, slow!"
    $ anim_speed = 0.03
    pause
    k "Like that, just like that, *Ah, ah, ah, ah!"
    mc "How tight you are... hmhmm."
    mc "God, this pussy was begging for this."
    $ anim_speed = 0.01
    k "Ouch{w=0.5}, ![mc]!"
    mc "*Huh, huh, huh*, do you like it like this?"
    mc "Do you like it when I stick my dick deep inside you?"
    k "*Ahh, uh, hngh!"
    mc "I'll take that as a yes."
    k "*Ahh!!!, I love it!"
    k "Don't stop!"
    mc "Hmm, you're so tight."
    mc "I love this ass!"
    mc "I love watching your ass bounce with every thrust I give you."
    k "*Ah, ah, ah, ah, ayy, uhh!"
    pause
    scene ch8_kfuck2_pov1_4 with hpunch
    image ch8_kfuck2_pov1_:
        function ch8_kfuck2_pov1_
    mc "Over here and get that ass up."
    $ anim_speed = 0.015
    scene ch8_kfuck2_pov1_ with dissolve
    k "*Oh, ah, ah, ah, ah!"
    k "You're a little aggressive today."
    mc "It's just that we haven't had sex for a long time."
    k "Like two days."
    mc "Well, it felt like a month."
    k "Ah, ah, ah ah ayyy, aahh!"
    mc "You're moaning too loud, [k]."
    mc "If you keep moaning like that even an industrial washing machine won't be able to dull the sound."
    k "I-{w=0.5} Ahh{w=0.5}, I can't help it."
    k "Not if you fuck me that hard."
    mc "I can't stop myself."
    k "Then don't."
    k "Just keep penetrating me, penetrate me really hard!"
    pause
    image ch8_kfuck2_pov2_:
        function ch8_kfuck2_pov2_
    scene ch8_kfuck2_pov2_ with dissolve    
    mc "Did you ever think we'd be fucking like rabbits in the laundry room with the washing machine on so we wouldn't get caught?"
    k "Do I answer you truthfully?"
    mc "Me too."
    image ch8_kfuck2_pov3_:
        function ch8_kfuck2_pov3_
    $ anim_speed = 0.0105
    scene ch8_kfuck2_pov3_ with dissolve
    mc "What face do you think the [drelat] [d] would make if he caught us right now?"
    k "*Ah, hmmm! {w=0.5}Don't even mention it."
    k "If he {w=0.5}, *!Ah!*{w=0.5}, caught us again I'm sure he would send us to each end of the planet, at the very least."
    k "And I'd be committed to nun school."
    pause
    mc "Your ass looks exquisite from here, god.."
    mc "I-I think I'm going to cum already."
    k "*Don't even think about it!*"
    mc "I'll do it outside."
    k "No, dumbass{w=0.3}, *Ah, aah*{w=0.3}, I mean don't cum yet."
    k "Let's switch poses."
    mc "Yes."
    pause
    jump ch8_kfuck1_pov1_
label ch8_kfuck1_pov1_:
    scene ch8_kfuck1_pov1__ with dissolve
    call screen ch8_kfuck1_pov1_settings
label ch8_kfuck2_pov1_:
    scene ch8_kfuck2_pov1_ with dissolve
    call screen ch8_kfuck2_pov1_settings with dissolve
label ch8_kfuck2_pov2_:
    scene ch8_kfuck2_pov2_ with dissolve
    call screen ch8_kfuck2_pov2_settings with dissolve
label ch8_kfuck2_pov3_:
    scene ch8_kfuck2_pov3_ with dissolve
    call screen ch8_kfuck2_pov3_settings with dissolve

    $ anim_speed = 0.01
    k "*Ah, ah, ah, I'm close!"
    mc "Me too." 
    k "*Ah, ay, oh, ahh!*"
    scene ch8_115 with dissolution
    pause 0.5
    scene ch8_117 with run
    pause 0.0
    with flash
    mc "Ohh..."
    mc "Yes..."
    jump afterch8_117
label ch8_kfuck2_cum:
    $ anim_speed = 0.01
    k "*Ah, ah!* I'm close!"
    mc "Me too." 
    k "*Ah, uh, uh, ahh!*"
    scene ch8_118 with cumming
    pause 0.0
    with flash
    stop voicefx fadeout 0.5
    mc "Ohh..."
    mc "Yes..."
    pause
    stop music fadeout 1.5
    jump afterch8_117

label afterch8_117:
    scene blackscreen with dissolve
    pause 0.0
    scene ch8_119 with fade
    play music scene2 fadein 1.0
    k "I have to admit it, that was good."
    mc "Yeah, it was amazing."
    mc "Better than last time?"
    k "Hmm, I don't know."
    k "What are you doing later?"
    mc "Hmm, nothing."
    mc "Ah, I'm going with [arelat] [a] to go buy some stuff."
    k "Damn, you sure do have mom-itis, or in this case, [arelat]-itis."
    mc "Yeah, whatever, why do you ask?"
    k "You don't even make an effort to deny it..."
    k "No reason in particular."
    pause
    scene ch8_120 with dissolve
    k "You go out first, it'll be weird if we both come out at the same time all sweaty."
    mc "We have to do it again."
    k "Only if you behave yourself."
    mc "I really liked it."
    k "Me too."
    "..."
    mc "Maybe we'll have time for another round later, [drelat] [d] said he'd be back late."
    k "We'll see..."
    pause
    k "What, are you expecting a goodbye kiss or something?"
    k "Go away!"
    $ renpy.end_replay()
    scene blackscreen with dissolve
    pause
    scene ch8_121 with fade
    pause
    scene ch8_122 with dissolve
    mc "Reading?"
    a "Yes, I'm reading this fitness magazine."
    a "It has some stuff about yoga and diet that interest me."
    pause
    scene ch8_123 with dissolve
    mc "People always trying to have more and more."
    a "What are you talking about?"
    mc "About you, you're already beautiful, and yet you keep trying to look better and better."
    scene ch8_126 with dissolve
    a "And what about you? You exercise every day."
    mc "Because I need to, I haven't reached my limit like you have."
    a "Haha, yeah, right."
    a "Are you going to ask me for something, or why the compliment out of nowhere?"
    mc "Nah, just fulfilling my daily quota of compliments."
    a "Oh, well, *giggle*."
    scene ch8_124 with dissolve
    mc "You know I mean it."
    a "Yes, I know."
    pause
    mc "..."
    scene ch8_126 with dissolve
    a "You always say that I underestimate myself and all that, that I don't realize how pretty I am, but it seems like you underestimate yourself too."
    a "I think you should get out of the house more, have fun, meet people..."
    a "You know, do young people stuff, not spend the whole day with your [arelat], I find it strange that someone like you spends the whole day at home."
    a "Don't get me wrong, it's fine by me, but I think you should enjoy your youth more."
    pause
    mc "I am enjoying my youth, in my own way."
    mc "We've talked about this before, I don't enjoy those things as much."
    mc "Parties, drinking alcohol, and stuff like that are boring to be honest, at least for me they are."
    mc "[k] says I'm an old man in a young man's body when it comes to those things, haha."
    mc "I prefer to spend my time doing things that truly entertain me."
    mc "Besides, what's stopping me from doing ''young people'' stuff with my [arelat]?"
    a "W-what are you saying, [mc]?"
    a "Remember what we agreed on..."
    mc "Uh{w=0.3}- (Wait, what did she understand by ''young people'' stuff?)"
    mc "..."
    a "..."
    scene ch8_127 with dissolve
    a "I have... some things to do."
    a "I haven't cleaned my room in days, and I bet [d] hasn't either."
    mc "Sure."
    mc "I have things to do too."
    pause
    scene ch8_237 with dissolve
    mc "(She can't be that dirty-minded, can she?)"
    mc "..."
    pause
    stop music fadeout 2.0
    scene ch8_238 with dissolve
    pause
label ch8s2:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
    scene ch8_239 with dissolve
    mc "Hmm..."
    pause
    if stephloving != "True":
        jump afterssdk 
    scene ch8_240 with hpunch
    play music scene3
    mc "Oof!"
    s "[mc]!"
    mc "You scared me!"
    scene ch8_242 with dissolve
    s "[mc], I want it..."
    mc "Do you mean..."
    s "Yes."
    mc "Now?"
    s "Yes, now!"
    mc "[s], we just did it this morning."
    s "So what?"
    mc "Did you at least get any sleep?"
    s "I just woke up, and I already showered."
    mc "Everyone is awake, do you want us to get caught?"
    s "It'll be quick."
    mc "No, [s:.5]."
    s "[mc]!"
    s "Just five minutes."
    s "Come on, please, [mc]."
    mc "(This is becoming a problem...{w=0.6} Again!)"
    s "I'll suck you again."
    mc "No-!" with vpunch
    mc "{i}Don't say that just like that!"
    s "Please, [mc]."
    s "I'll be very, very quick."
    mc "(Don't look at me like that, please.)"
    mc "*Exhales*"
    pause
    mc "Will you be quiet?"
    s "Yes, very quiet."
    mc "Go to your room, I'll be there in a minute."
    s "Okay, I'll be waiting."
    scene ch8_241 with dissolve
    mc "And I'm not doing it because..."
    mc "Just go to your room."
    s "Yes!"
    stop music fadeout 1.5
    scene blackscreen with dissolve
    pause
    play music sexy3 fadein 2.0
    play voicefx "audio/wavs/s/smoansoft.ogg" fadein 2.0
    image ch8_243anim:
        "ch8_243" with dissolve
        1.0
        "ch8_244" with dissolve
        1.0
        repeat
    scene ch8_243anim with Dissolve(2.0)
    s "Hmmng, huh"
    s "Hmm, hmm, ahh"
    pause
    #animation
    s "Uh, hm, huh"
    s "Uh..."
    s "That feels so good..."
    pause
init python:
    def ch8_s_clngs_1_(trans, st, at):  
        trans.set_child("ch8_s_clngs_1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_s_clngs_1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterchoicesch8_s_clngs_1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 2" action Jump("ch8_s_clngs_2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_s_clngs_3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
############################################################################################################
init python:
    def ch8_s_clngs_2_(trans, st, at):  
        trans.set_child("ch8_s_clngs_2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_s_clngs_2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterchoicesch8_s_clngs_1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 1" action Jump("ch8_s_clngs_1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_s_clngs_3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
############################################################################################################
init python:
    def ch8_s_clngs_3_(trans, st, at):  
        trans.set_child("ch8_s_clngs_3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch8_s_clngs_3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterchoicesch8_s_clngs_1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 1" action Jump("ch8_s_clngs_1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_s_clngs_2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
############################################################################################################
label afterch8_s_clngs_1_code:
    image ch8_s_clngs_1_:
        function ch8_s_clngs_1_
    image ch8_s_clngs_2_:
        function ch8_s_clngs_2_
    image ch8_s_clngs_3_:
        function ch8_s_clngs_3_         
    $ anim_speed = 0.05
    scene ch8_s_clngs_3_ with dissolve
    s "*Uhhs, hmm, hm*"
    s "How come you know where to lick?"
    mc "..."
    s "When I sucked your dick I didn't really know what to do."
    s "Hmm...{w=0.3} but you always know where I'm going to feel good."
    mc "The experience."
    s "I want to have{w=0.3}, huh{w=0.3}, experience."
    s "I want to give you lots of pleasure just like you give me."
    mc "Erm..."
    mc "C-concentrate, [s]."
    s "Yes... *Uhm, uh*"
    pause
    scene ch8_s_clngs_1_ with dissolve
    s "Huhm...{w=0.3} I'm never going to get tired of this..."
    mc "T-this... we can't do it all the time, understand?"
    mc "Today is the exception because the [drelat][d] is not at home."
    mc "Don't expect every day to be like this one."
    s "We'll find a way, don't worry."
    mc "..."
    pause
    s "But we'll do it every morning without fail, you hear?"
    mc "(That sounded like a threat...)"
    scene ch8_s_clngs_2_ with dissolve
    s "Does [k] ask you to give her oral sex often?"
    mc "No."
    s "Huh{w=0.3}, doesn't she like it?"
    mc "We don't do it often because we're cautious and don't want to get caught."
    mc "You don't want to get caught either, right?"
    s "Of course{w=0.3}, Ahh{w=0.3}, no."
    mc "So we have to be careful."
    s "That's a shame..."
    pause
label ch8_s_clngs_1_:
    scene ch8_s_clngs_1_ with dissolve
    call screen ch8_s_clngs_1_settings with dissolve
label ch8_s_clngs_2_:
    scene ch8_s_clngs_2_ with dissolve
    call screen ch8_s_clngs_2_settings with dissolve
label ch8_s_clngs_3_:
    scene ch8_s_clngs_3_ with dissolve
    call screen ch8_s_clngs_3_settings with dissolve

label afterchoicesch8_s_clngs_1_:
    $ anim_speed = 0.01
    s "*Ah, unh*"
    s "I'm close, [mc]."
    s "Uhhhmmm!"
    with cumming
    play voicefx "audio/wavs/s/s_softmoan_1.ogg"
    pause 0.0
    with flash
    pause 0.0
    scene ch8_246 with dissolve
    s "Phew..."
    s "That... was amazing..."
    pause
    scene ch8_248 with dissolve
    s "Thank you, [mc]."
    mc "You're welcome, I have to go now."
    s "W-wait."
    s "I told you I'd suck you too."
    mc "Don't worry, I'm fine."
    scene ch8_249 with dissolve
    s "But what about this lump?"
    s "You're really bulging here."
    s "And quite hard..."
    mc "Erm, yeah but-"
    pause
    s "I'll take care of it."
    scene ch8_250 with dissolve
    s "Take off your pants."
    mc "Seriously, you don't need to."
    s "One little suck and that's it."
    scene ch8_251 with dissolve
    s "Don't tell me you don't want it too, [mc]."
    s "I'm going to suck you real hard to get that bad semen out that makes your penis so swollen."
    mc "That's not exactly how that works..."
    s "Come on, let me suck your penis little bit, I know you like it."
    s "We already did it once, [mc]."
    mc "Uh..."
    mc "{size=-5}{i}Fuck."
    mc "You like doing it, huh?"
    s "Yes, I do!"
    mc "Is there any special reason why you like it?"
    s "I don't know why, I just like it."
    s "I like to hold it in my mouth and taste it..."
    s "Even though it doesn't have any taste, but... well, it just makes me feel good."
    mc "(It's her womanly instincts, I guess.)"
    mc "Let's be quick, shall we?"
    s "Will you let me do it?"
    mc "Yes... {w=0.5} but it has to be quick."
    s "Got it!"
    scene ch8_252 with dissolve
    s "Take off your pants."
    s "Take them off now!"
    mc "I'm going, geez!"
    scene ch8_253 with dissolve
    s "Hmmm, *laugh*."
    s "How does this thing fit in your pants? I don't get it."
    pause
    scene ch8_254 with dissolve
    s "It's warm."
    pause
    scene ch8_253 with dissolve
    s "You have that face again, haha."
    s "I don't know why you refuse so much when you love it."
    pause

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_bj_2_pov1_(trans, st, at):  
        trans.set_child("ch8_s_bj_2_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 20:
            sound_files = ["audio/wavs/bj_65.ogg", "audio/wavs/bj_71.ogg", "audio/wavs/bj_63.ogg", "audio/wavs/bj_80.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 5:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_3.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.5:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_bj_2_pov2_(trans, st, at):  
        trans.set_child("ch8_s_bj_2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 20:
            sound_files = ["audio/wavs/bj_65.ogg", "audio/wavs/bj_71.ogg", "audio/wavs/bj_63.ogg", "audio/wavs/bj_80.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 5:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_3.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.5:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_bj_2_pov3_(trans, st, at):  
        trans.set_child("ch8_s_bj_2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 20:
            sound_files = ["audio/wavs/bj_65.ogg", "audio/wavs/bj_71.ogg", "audio/wavs/bj_63.ogg", "audio/wavs/bj_80.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 5:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_3.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.5:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_bj_2_cum_(trans, st, at):  
        trans.set_child("ch8_s_bj_2_cum_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating14.ogg", "audio/masturbating/cutmastrubating16.ogg", "audio/masturbating/cutmastrubating18.ogg", "audio/masturbating/cutmastrubating20.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating13.ogg", "audio/masturbating/cutmastrubating15.ogg", "audio/masturbating/cutmastrubating17.ogg", "audio/masturbating/cutmastrubating19.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
screen ch8_s_bj_2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_255cumming") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 2" action Jump("ch8_s_bj_2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_s_bj_3_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_s_bj_2_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_255cumming") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 1" action Jump("ch8_s_bj_2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_s_bj_3_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_s_bj_2_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_255cumming") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 1" action Jump("ch8_s_bj_2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_s_bj_2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_s_bj_2_cum_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_s_bj_2_cum_cumming") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label before_ch8_s_bj_2_:
    image ch8_s_bj_2_pov1_:
        function ch8_s_bj_2_pov1_
    image ch8_s_bj_2_pov2_:
        function ch8_s_bj_2_pov2_
    image ch8_s_bj_2_pov3_:
        function ch8_s_bj_2_pov3_
    image ch8_s_bj_2_cum_:
        function ch8_s_bj_2_cum_            
    scene ch8_s_bj_2_pov1_1 with dissolve  
    mc "(She put it in her mouth without a second thought...)"
    $ anim_speed = 0.05
    scene ch8_s_bj_2_pov1_ with dissolve
    s "*Suck, hmp, slurp*"
    mc "Oh, yeah..."
    mc "(Fuck, this feels too good.)"
    mc "(I can feel her little tongue frolicking around my glans.)"
    s "*Slurp, suck, suck*"
    pause
    mc "(She's supposed to be a beginner, but she sucks it like a pro.)"
    mc "(Things like sleeping, eating, drinking and oral sex no one has ever done wrong...)"
    s "*Shup, slurp, suck*"
    pause
    scene ch8_s_bj_2_pov3_ with dissolve
    s "{i}Don't even get half of it in my mouth..."
    pause
    mc "You like to suck it to make your [srelatmc] feel good, don't you?"
    s "Uh-hum{image=redheart}."
    mc "You're so- *hmm*{w=0.3}, cute."
    pause
    scene ch8_s_bj_2_pov2_ with dissolve
    s "{i}And you, what do you like best about giving me oral sex?"
    mc "..."
    mc "M-make you feel good is what I like best too..."
    s "{i}We're alike in that, hehe."
    pause
label ch8_s_bj_2_pov1_:
    scene ch8_s_bj_2_pov1_ with dissolve
    call screen ch8_s_bj_2_pov1_settings with dissolve
label ch8_s_bj_2_pov2_:
    scene ch8_s_bj_2_pov2_ with dissolve
    call screen ch8_s_bj_2_pov2_settings with dissolve
label ch8_s_bj_3_pov3_:
    scene ch8_s_bj_2_pov3_ with dissolve
    call screen ch8_s_bj_2_pov3_settings with dissolve        
label ch8_255cumming:
    scene ch8_s_bj_2_pov1_ with dissolve
    mc "Ohh, yeah..."
    mc "*Hmm*..."
    mc "*Hmm, hmng*"
    mc "It's coming- {p=0.3}{nw}"
    mc "{i}Semen is coming, [s]!"
    $ anim_speed = 0.015
    s "*Chup, shup, slurp*"
    mc "(She's starting to quickly stroke the tip of my penis with her tongue.)"
    mc "So good... Hmmg, almost there..."
    mc "*Hmng!*"
    scene ch8_s_bj_2_cum_ with vpunch
    $ anim_speed = 0.015
    mc "Oh, yes, *hmngh!*..."
    s "[mc], are you going to...?"
    mc "(Yes, I want to cover this angel face with my semen again!)"
    mc "*Hngh! *"
    call screen ch8_s_bj_2_cum_settings with dissolve
label ch8_s_bj_2_cum_cumming:        
    scene ch8_255 with cumming
    with flash
    mc "*Arghh!*"
    scene ch8_256 with dissolve
    mc "God..."
    pause
    s "*Hm.. uh...*"
    s "It's warm..."
    pause
    s "See? I told you it would be quick, Heh..."
    scene ch8_257 with dissolve
    mc "-Ah..."
    s "You did it on purpose this time didn't you? naughty..."
    mc "I-I didn't want to stain the carpet."
    s "A-ha."
    mc "Seriously..."
    mc "(God, I've done it again...)"
    mc "Can I get you something to clean you up?"
    s "I've got tissues in the drawer behind me."
    s "Did it feel good this time too?"
    mc "Yes, it felt really good."
    s "Well, now you know I can take care of that too."
    s "When you need to get the cum out come with me, I'm going to suck you real good to get it all out, okay?"
    mc "(She always says those things so lightly...)"
    mc "Ehh, well..."
    mc "I-I have to go take a shower."
    mc "Thank you for... this."
    s "Likewise."
    pause 
    $ renpy.end_replay()
label afterssdk:
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 2.0
    scene ch8_278 with fade
    pause
    mc "(I can't believe what's been going on lately.)"
    if stephloving == "True":
        mc "([s] gave me oral sex in the morning, then I fucked [k] and just a little while ago [s] just gave me another blowjob.)"
        mc "(Sex with [k] was fantastic.)"
        mc "(But I don't know how to feel about it with [s].)"
        mc "(At this point it's already ridiculous to say I don't like it, but I don't know, it's weird.)"
        "..."
        mc "([s] likes me a lot that worries me a little bit.)"
        mc "(And I'm giving in more and more and more to doing things with her.)"
    else:
        mc "(I fucked [k] so good and and [a] gave me a titjob last night.)"
        mc "(Sex with [k] was fantastic though... I couldn't remember her pussy feeling so thight and good.)"
    pause
    mc "(All the girls in this house are too sexy.)"
    mc "(Sometimes I think I'm living in a simulation.)"
    pause
    "..."
    mc "(How boring...)"
    mc "..."
    mc "(Stupid [k], she didn't tell me she was going out with [mia], I would have liked to go too.)"
    pause
    mc "(I haven't been studying or working for a month now, I feel like a parasite...)"
    mc "(I even feel a little ashamed now.)"
    mc "([drelat!c] [d] has never asked me to contribute to the house, in fact the last time I mentioned it to him he didn't like the idea.)"
    mc "(And [a] much less, she has always spoiled me a lot.)"
    mc "(But that was when I was studying.)"
    mc "..."
    pause
    mc "(What the heck did [a] even understand from what I said?)"
    mc "(In what world does 'doing young people stuff' have sexual connotation?)"
    pause
    mc "(Darn...)"
    mc "(I feel like [a] is trying to distance herself again.)"
    pause
    scene ch7_578 with cumming
    a "[mc], you're my [arelatmc]."
    pause
    mc "(How can I break that stupid barrier?)"
    mc "(I want her to see me as a man, not just her [arelatmc].)"
    mc "No matter what I do, I'll never stop being her [arelatmc]..."
    pause
    scene ch8_278 with flash
    pause
    mc "But..."
    mc "I can be a man..."
    mc "..."
    mc "Maybe if I start acting more mature..."
    pause
    scene ch8_279 with dissolve
    mc "I hope it's charged."
    pause
    scene ch8_280 with dissolve
    mc "I wonder if those job listings on the internet will actually work."
    mc "Computer technician... minimum requirements, some kind of vocational training, I don't have that..."
    mc "''Engineer in'' - Nah, it requires a degree."
    mc "''Senior administrator of something... 5 years of experience,'' yeah right."
    mc "Darn it, jobs that don't require a education pay considerably less than those that do... what a surprise."
    mc "''Forklift operator for receiving and dispatch'' - basic education level, this one interests me."
    mc "Heavy work, good physical shape without health problems, okay."
    mc "The pay isn't too bad."
    mc "''Register... create your cv'' I don't even know what a cv is."
    mc "Well, I'll send my cv to several and see what happens."
    pause
    stop music fadeout 2.0
    scene blackscreen with Dissolve(1.5)
    pause
    play music scene1 fadein 0.5
    scene ch8_258 with fade
    mc "Hey, [a], where are you going?"
    scene ch8_259 with dissolve
    a "I'm going for a jog."
    a "There's nothing to do at home, and I'm dying of boredom."
    a "Are you coming?"
    mc "Yeah, for sure."
    mc "I'm also bored to death."
    scene ch8_292 with fade
    mc "Whew, whew."
    mc "Aren't you hot in that oversized sweater?"
    a "Yeah, but I want to sweat as much as possible."
    mc "Again with that..."
    a "[mc], the other day I calculated my body mass index."
    mc "And?"
    a "I'm in the overweight range..."
    mc "What? Haha, no way."
    a "I've never been this heavy before."
    mc "[a], you don't even have a belly."
    a "That's what you think."
    mc "Well, it doesn't show."
    a "I have a little bit."
    a "But the body also stores fat in other places, not just the belly, in my case, it's in my legs."
    a "I understand that my physique isn't designed to be slim; I have wide hips and a large bust, and whether you like it or not, that's extra weight."
    a "I just want to lose a bit, that's all."
    a "I weigh 168, that eight pounds needs to go."
    mc "Just don't lose too much."
    scene ch8_293 with fade
    mc "We've never jogged around this block before."
    a "It's a good spot for jogging."
    mc "Yeah."
    mc "*Whew, whew, whew*"
    a "Tired?"
    mc "Honestly, yes."
    a "Don't tell me [arelat] [a] has better cardio than you."
    mc "Well, I woke up a bit tired today..."
    a "Are those excuses I'm hearing?"
    mc "Oh, yeah?!"
    a "Hey, not so fast, wait!"
    scene ch8_291 with fade
    a "Did you really order food?"
    mc "Running makes me hungry."
    a "What was the point of all this if you're going to regain all the calories you burned?"
    mc "It makes sense."
    a "I don't see any sense in it."
    mc "The point is that I just wanted to go jogging with my beautiful [arelat]."
    a "Ooh."
    mc "Exactly."
    a "You're a sweetheart."
    mc "Plus, it's part of the special diet my nutritionist gave me."
    mc "I need calories for the muscles and stuff."
    a "Oh, you mean ''this'' nutritionist?"
    mc "Ouch!, Stop it, quit poking my belly, hahaha."
    pause
    scene ch8_261 with fade
    a "We jogged quite a distance."
    mc "Yeah, too bad about the restaurant."
    a "Haha, you left them with no reservations."
    mc "The pizza and the frappé were amazing."
    mc "But I only had two slices, don't exaggerate."
    a "Speaking of food, I have to cook for the girls."
    a "Are you still hungry?"
    mc "No, I'm good."
    mc "Can we continue with the cooking lessons?"
    a "Oh, so you do want to learn how to cook?"
    a "The other day, you didn't even remember the basic steps."
    mc "Well... I got distracted."
    scene ch8_262 with dissolve
    a "R-right..."
    pause
    mc "I'll try not to get distracted this time."
    scene ch8_261 with dissolve
    a "You better, because there will be a written exam."
    mc "Haha, sure."
    a "Can I take a shower first?"
    mc "Sure."
    a "Great."
    scene ch8_261 with dissolve
    mc "I'm glad that you and I..."
    mc "I'm glad that we're doing well."
    a "There's no reason not to be."
    mc "True."
    "..."
    pause
    scene ch8_260 with dissolve
    a "Well, I'll go take a shower."
    pause
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 1.5
label ch8_kitchen263:
label ch8a1:
    if _in_replay:
        show screen Replayexit
        play music scene2 fadein 1.0
    scene ch8_263in with fade
    a "Did you already put the chicken to thaw in the refrigerator?"
    mc "Yeah, but isn't it faster to just leave it out?"
    a "No, at room temperature, chicken goes bad quickly."
    mc "I see."
    scene ch8_262-in with fade
    a "Another option is to submerge it in a bag in cold water."
    a "Chicken is very delicate in that regard; microorganisms reproduce rapidly on it."
    mc "I understand."
    pause
    scene ch8_262--- with dissolve
    pause
    scene ch8_262-- with dissolve
    mc "..."
    pause
    a "Are we going to buy the ceiling lamps?"
    scene ch8_262-in with dissolve
    mc "That was the plan."
    a "Then I'll hurry up; I don't want to go too late."
    mc "Sure."
    pause
    scene ch8_262-- with dissolve
    mc "..."
    pause
    mc "(Yesterday we said we'd forget about everything, but I can't.)"
    mc "(When I see her, I can't resist; she'll always attract me, no matter what she tells me.)"
    mc "(It's like asking me to stop drinking water; these are instincts that can't be controlled.)"
    pause
    mc "..."
    scene ch8_263---2 with dissolve
    a "Uh..."
    scene ch8_262- with dissolve
    mc "Y-you're quite the knife expert; you chop the veggies pretty fast."
    a "And I'm not even going as fast as I can."
    mc "Really?"
    a "Look and learn."
    pause
    image ch8_263--anim:
        "ch8_263---2" with dissolve
        1
        "ch8_263---1" with dissolve
        1
        repeat
    scene ch8_263--anim with dissolve
    mc "Uh..."
    a "Are you paying attention?"
    mc "Yes..."
    mc "I'm lucky; I'm being taught by a cooking expert."
    pause
    a "I'm not asking you to do anything; you must be bored."
    mc "I can learn by watching."
    a "Okay."
    mc "(Is she doing it on purpose?)"
    pause
    scene ch8_262-in with dissolve
    mc "You're not going to chop the carrots as well?"
    a "Um, yeah."
    pause
    image ch8_263anim:
        "ch8_263---" with dissolve
        1.0
        "ch8_263-----" with dissolve
        1.0
        repeat
    scene ch8_263anim with dissolve
    pause
    mc "Why are you stopping?"
    a "Huh?"
    a "I was thinking about something, sorry."
    pause
    mc "(Am I imagining things, or was chopping vegetables just an excuse to wiggle her butt against my bulge?)"
    mc "(I mean, she's not even chopping the veggies anymore, but she's still moving her butt...)"
    pause
    image ch8_263------anim:
        "ch8_263------" with dissolve
        1.0
        "ch8_263-------" with dissolve
        1.0
        repeat
    scene ch8_263------anim with dissolve
    mc "(Despite it all, she's still pretending that nothing is happening here.)"
    mc "(Well...)"
    pause
    scene ch8_263---------- with dissolve
    mc "(Let's keep pretending-)"
    pause
    scene ch8_263----------- with dissolve
    mc "(-That nothing is happening here...)"
    pause
    scene ch8_263---------- with dissolve
    pause
    scene ch8_263--------- with dissolve
    mc "(Hmm... how delightful.)"
    pause
    image ch8_263---------anim:
        "ch8_263-----------" with dissolve
        1.5
        "ch8_263----------" with dissolve
        1.5
        "ch8_263---------" with dissolve
        1.5
        repeat
    scene ch8_263---------anim with dissolve
    pause
    mc "(No complaints...)"
    mc "(I knew it; she wants this.)"
    mc "(I love pretending that nothing is happening here while I squeeze her buttocks with such lust.)"
    pause
    a "Has the chicken thawed yet?"
    mc "I don't know."
    mc "Should I check?"
    a "Let's wait a little longer."
    a "If it's still frozen, it won't cook well."
    mc "(She could simply ask me to check, but she doesn't because she doesn't want me to stop touching her.)"
    mc "(God...)"
    mc "(Under different circumstances, I'd have a raging hard-on, but I had quite an... ''active'' morning.)"
    mc "(Still, my body craves to fuck her; that's the effect [a] has on me.)"
    pause
    a "[mc], [s] could come..."
    mc "Hm, did you say something?"
    pause
    scene ch8_263-1in with dissolve
    a "[s] could come and see us..."
    mc "See us?"
    mc "I don't understand..."
    scene ch8_266 with dissolve
    a "[mc]..."
    pause
    scene ch8_263- with dissolve
    mc "I don't understand why that would be a problem."
    mc "I'm just learning to cook with my [arelat]."
    a "[mc]..."
    scene ch8_264 with dissolve
    mc "She's asleep."
    a "Oh, well..."
    scene ch8_267 with dissolve
    a "Hmm, I-in that case..." 
    mc "You smell delicious." 
    a "[mc]..." 
    mc "Is it a new shampoo?" 
    a "I'm using a different conditioner." 
    mc "It smells really good."
init python:
    def ch8_266_agroped_pov1_(trans, st, at):  
        trans.set_child("ch8_266_agroped_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
init python:
    def ch8_266_agroped_pov2_(trans, st, at):  
        trans.set_child("ch8_266_agroped_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
#
#
#
init python:
    def ch8_266_agroped_pov3_(trans, st, at):  
        trans.set_child("ch8_266_agroped_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
#
#
#
init python:
    def ch8_266_agroped_pov4_(trans, st, at):  
        trans.set_child("ch8_266_agroped_pov4_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
#
#
#
screen ch8_266_agroped_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_266_agroped_continue") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_266_agroped_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_266_agroped_pov3_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_266_agroped_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
#
#
#
#
screen ch8_266_agroped_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_266_agroped_continue") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_266_agroped_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_266_agroped_pov3_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_266_agroped_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
#
#
#
#
screen ch8_266_agroped_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_266_agroped_continue") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_266_agroped_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_266_agroped_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_266_agroped_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
#
#
#
#
screen ch8_266_agroped_pov4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_266_agroped_continue") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_266_agroped_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_266_agroped_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_266_agroped_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label ch8_266an:
    image ch8_266_agroped_pov1_:
        function ch8_266_agroped_pov1_
    image ch8_266_agroped_pov2_:
        function ch8_266_agroped_pov2_
    image ch8_266_agroped_pov3_:
        function ch8_266_agroped_pov3_
    image ch8_266_agroped_pov4_:
        function ch8_266_agroped_pov4_
    $ anim_speed = 0.06
    scene ch8_267- with dissolve
    a "I've never heard of someone who likes the smell of a conditioner so much, *giggles*."
    mc "Well, it's not really the conditioner, it's something else..."
    mc "Today you smell like...{w=0.4} I don't know, you smell so good that it makes me want to..."
    scene ch8_267-- with dissolve
    a "Oh..."
    image ch8_267-anim:
        "ch8_267-" with dissolve
        1.75
        "ch8_267--" with dissolve
        1.75
        repeat
    scene ch8_267-anim with dissolve
    a "[mc]..."
    a "Sweetheart, I have to cook."
    mc "Just a little longer..."
    mc "It's just...{w=0.4} you smell so good."
    a "Alright, just a little longer..."
    pause
    scene ch8_266_agroped_pov1_ with dissolve
    a "[mc], what are you...?"
    pause
    a "Sweetheart, don't you sometimes feel like you're being too affectionate?"
    mc "Well, it never hurts to show love for each other."
    mc "Besides, I hardly ever hug you."
    a "[mc], you hug me all the time, *giggles*."
    scene ch8_266_agroped_pov3_ with dissolve
    mc "Really?"
    a "Yes."
    pause
    mc "You've turned me into a spoiled boy, it's your fault."
    a "Yes *giggles*, it's probably my fault."
    a "You'll always be my spoiled little boy."
    mc "Well, now YOU are going to be my spoiled girl."
    a "*Giggles*"
    pause
    scene ch8_266_agroped_pov4_ with dissolve 
    a "Hmm..."
    a "That's enough hugs, sweetheart, we have to finish cooking."
    mc "But I'm enjoying... the hug..."
    mc "Can't we put aside the food for a moment?"
    a "[mc]..."
    pause
    scene ch8_266_agroped_pov2_ with dissolve
    a "Are you sure [s] is asleep?"
    mc "She is."
    pause
label ch8_266_agroped_pov1_:
    scene ch8_266_agroped_pov1_ with dissolve
    call screen ch8_266_agroped_pov1_settings with dissolve
label ch8_266_agroped_pov2_:
    scene ch8_266_agroped_pov2_ with dissolve
    call screen ch8_266_agroped_pov2_settings with dissolve
label ch8_266_agroped_pov3_:
    scene ch8_266_agroped_pov3_ with dissolve
    call screen ch8_266_agroped_pov3_settings with dissolve
label ch8_266_agroped_pov4_:
    scene ch8_266_agroped_pov4_ with dissolve
    call screen ch8_266_agroped_pov4_settings with dissolve   
label ch8_266_agroped_continue:
    $ anim_speed = 0.015
    a "[mc], wait."
    a "[mc], uh..."
    pause
    scene ch8_268 with dissolve
    a "[mc]!"
    scene ch8_269 with hpunch
    mc "I'm sorry, I won't do it again!"
    a "W-what?"
    mc "[a], put the knife down."
    scene ch8_270 with dissolve
    a "Ah, sorry! Haha."
    a "Do you really think I would hurt you, [mc]?"
    mc "I saw you slicing those vegetables and suddenly you lifted the knife like that looking at my eyes, don't blame me I got scared."
    a "Hahaha, nooo."
    scene ch8_276 with dissolve
    a "Let me cook now, [s] must be hungry."
    mc "I'll take the chicken out of the fridge."
    a "Nope, you, sir, are going to do something else because you distract me too much."
    mc "I'll help this time."
    a "Do you want me to lift the knife again?"
    mc "Okay, okay, I'm leaving."
    mc "But not without a good kiss first."
    scene ch8_277 with dissolve
    a "Alright, a kiss and that's it."
    pause
    scene ch8_272 with dissolve
    pause
    scene ch8_275 with dissolve 
    pause
    play sound "audio/wavs/sfx/kissing_1.ogg" volume 0.5 loop
    scene ch8_274 with dissolve
    a "*Mmm, hmm*"
    pause
    scene ch8_273 with dissolve 
    a "*Ahh, hmm*"
    pause

    scene ch8_275 with dissolve
    a "*Hmm* wait."
    pause
    stop sound fadeout 0.5
    scene ch8_272 with dissolve
    a "Hah... "
    a "You said a good kiss."
    mc "Yeah..."
    pause
    scene ch8_271 with dissolve 
    play sound "audio/mouth/french_kiss_05.ogg" volume 0.35
    $ renpy.pause(0.5, hard=True)
    scene ch8_272 with dissolve
    a "Alright, now go."
    a "I have to finish this."
    mc "See you later."
    $ renpy.end_replay()
    pause
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    scene ch8_281 with dissolve
    play music scene2 fadein 2.0
    k "[mc]."
    mc "*Zzz..*"
    pause
    scene blackscreen with dissolve
    k "[mc], wake up."
    pause
    k "{size=+5}[mc]!"
    scene ch8_283 with hpunch
    mc "Ah! What, what, what?"
    k "Hey, calm down, it's me."
    mc "Ugh! I'm still in the nightmare!"
    scene ch8_284 with hpunch
    mc "Ouch!"
    k "Idiot, me appearing in a dream would be like going to paradise for you."
    mc "Hahaha, more like hell."
    k "Oh, really?"
    k "Then I'm like a sexy little devil, I like that."
    mc "By the way, you left without me, I feel betrayed."
    scene ch8_283 with dissolve
    k "I was looking for you but couldn't find you."
    k "I thought you had left the house."
    mc "[k], I was in my room."
    k "Sorry I didn't search for you there."
    mc "I see, so that's how it is..."
    k "What?"
    mc "Nothing."
    k "HAHAHA."
    k "Are you sure you don't have a vagina?"
    mc "Well, I might have a vagina, but I don't betray, I'm real."
    k "Stop talking shit!"
    scene ch8_284 with dissolve
    k "Do you want me to apologize? Okay, I will."
    k "In my room... with the door locked."
    k "Dad hasn't come home yet."
    mc "Alright, I accept your apology but-"
    k "-Just shut up and come to my room with me."
    stop music fadeout 1.5
    scene blackscreen with dissolve
    pause
label ch8k2:
    if _in_replay:
        show screen Replayexit
    play music sexy1 fadein 1.5
    scene ch8_285 with dissolve
    mc "Turn up the tv more."
    k "It's already at maximum."
    mc "You better hold back your moans."
    pause
    scene ch8_286 with dissolve
    k "Can you imagine if every day could be like this?"
    k "Feeling horny and just going to the other's room and fucking like animals."
    mc "That would be awesome."
    mc "(I've already cum three times before and I'm still as hard as a rock.)"
    mc "(As if that's weird... any man would get hard with such an angel.)"
    k "Let's be quicker this time."
    k "We don't know if dad will come home early or not."
    k "Lucky that dad reconsidered and put the lock back on my room door."
    scene ch8_287 with dissolve
    k "*Uh... Oh!*"
init python:
    def ch8_k_sex_2_pov1_(trans, st, at):  
        trans.set_child("ch8_k_sex_2_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
#        
init python:
    def ch8_k_sex_2_pov2_(trans, st, at):  
        trans.set_child("ch8_k_sex_2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
#
init python:
    def ch8_k_sex_2_pov3_(trans, st, at):  
        trans.set_child("ch8_k_sex_2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
#
init python:
    store.last_played_sound = None
    def ch8_k_sex_3_pov1_(trans, st, at):  
        trans.set_child("ch8_k_sex_3_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 26:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
#
init python:
    store.last_played_sound = None
    def ch8_k_sex_3_pov2_(trans, st, at):  
        trans.set_child("ch8_k_sex_3_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 26:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
#
init python:
    store.last_played_sound = None
    def ch8_k_sex_3_pov3_(trans, st, at):  
        trans.set_child("ch8_k_sex_3_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 26:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value        
#
#
#
#              
screen ch8_k_sex_2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_k_sex_2_pov_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_k_sex_2_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 3" action Jump("ch8_k_sex_2_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch8_k_sex_2_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_k_sex_2_pov_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_k_sex_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 3" action Jump("ch8_k_sex_2_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch8_k_sex_2_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_k_sex_2_pov_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_k_sex_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 2" action Jump("ch8_k_sex_2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"        







screen ch8_k_sex_3_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"                  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_k_sex_3_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_k_sex_3_pov2_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 3" action Jump("ch8_k_sex_3_pov3_settings") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch8_k_sex_3_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_k_sex_3_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_k_sex_3_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 3" action Jump("ch8_k_sex_3_pov3_settings") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch8_k_sex_3_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_k_sex_3_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_k_sex_3_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.88
        textbutton "Pov 2" action Jump("ch8_k_sex_3_pov2_settings") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"        


label ch8_k_sex_2_p:
    $ anim_speed = 0.04
    image ch8_k_sex_2_pov1_:
        function ch8_k_sex_2_pov1_
    image ch8_k_sex_2_pov2_:
        function ch8_k_sex_2_pov2_
    image ch8_k_sex_2_pov3_:
        function ch8_k_sex_2_pov3_    
    image ch8_k_sex_3_pov1_:
        function ch8_k_sex_3_pov1_    
    scene ch8_k_sex_2_pov1_ with dissolve
    play voicefx "audio/wavs/k/kmoansoft.ogg" loop
    k "Oh, God!"
    mc "Shh..."
    k "-Sorry!, huh!"
    k "Uh, uhm.."
    k "Uh, ah, ah"
    mc "I love seeing you enjoy bouncing on my cock."
    k "We need to be,{w=0.4} huh, {w=0.4} quick."
    mc "Then keep jumping, make me cum fast."
    k "*Ahh, hng, hmm*"
    k "I want to fuck every day."
    k "We need to think of something."
    mc "What do you suggest?"
    k "I can't think of anything."
    scene ch8_k_sex_2_pov2_ with dissolve
    mc "Forget about it, it's almost time for his ''business trips'' again."
    k "Why do you say it like that?"
    mc "I-I don't know."
    k "You don't believe his story either, do you?"
    k "It's a bit strange that my dad goes on so many business trips."
    k "Think about it, why would he have to go on so many trips? Can't he send a representative or something?"
    scene ch8_k_sex_2_pov3_ with dissolve
    k "Oh, ahm, hgm..."
    k "His company isn't even that big, Ah, ah!"
    k "It's more like a small business, and I mean, it's doing well, but it's strange that he has so many trips."
    k "*Oh god...*"
    image ch8_k_sex_2_pov2_cmo:
        "ch8_k_sex_2_pov2_16"
        0.02
        "ch8_k_sex_2_pov2_17"
        0.02
        "ch8_k_sex_2_pov2_18"
        0.02
        "ch8_k_sex_2_pov2_19"
        0.02
        "ch8_k_sex_2_pov2_18"
        0.02
        "ch8_k_sex_2_pov2_17"
        0.02
        repeat
    image ch8_k_sex_2_pov1_cmo:
        "ch8_k_sex_2_pov1_16"
        0.02
        "ch8_k_sex_2_pov1_17"
        0.02
        "ch8_k_sex_2_pov1_18"
        0.02
        "ch8_k_sex_2_pov1_19"
        0.02
        "ch8_k_sex_2_pov1_18"
        0.02
        "ch8_k_sex_2_pov1_17"
        0.02
        repeat
    stop sound fadeout 0.5
    scene ch8_k_sex_2_pov2_cmo with cumming
    play voicefx "audio/wavs/k/kmoanhard.ogg" loop
    with flash
    k "*Uuhh... hmmmng!*"
    k "*Ngh...*"
    scene ch8_k_sex_2_pov1_cmo with dissolve
    k "*Hahmmhngh!"
    k "Oh my god!"
    pause
    stop sound fadeout 0.5
    scene ch8_k_sex_2_pov1_16 with dissolve
    mc "Wow... that was intense."
    k "Oh my god..."
    k "It's always intense when I do it with you..."
    play voicefx "audio/wavs/k/kmoansoft.ogg" loop
label ch8_k_sex_2_pov1_:
    scene ch8_k_sex_2_pov1_ with dissolve
    call screen ch8_k_sex_2_pov1_settings with dissolve   
label ch8_k_sex_2_pov2_:
    scene ch8_k_sex_2_pov2_ with dissolve
    call screen ch8_k_sex_2_pov2_settings with dissolve
label ch8_k_sex_2_pov3_:
    scene ch8_k_sex_2_pov3_ with dissolve
    call screen ch8_k_sex_2_pov3_settings with dissolve

label afterch8_k_sex_2_pov_settings:
    $ anim_speed = 0.035
    mc "I want to fuck you doggy style."
    k "Yeah, fuck me doggy style, make me your bitch."
    $ anim_speed = 0.035
    image ch8_k_sex_3_pov1_cmo:
        function ch8_k_sex_3_pov1_
    image ch8_k_sex_3_pov2_cmo:
        function ch8_k_sex_3_pov2_
    image ch8_k_sex_3_pov3_cmo:
        function ch8_k_sex_3_pov3_
    scene ch8_k_sex_3_pov1_cmo with dissolve
    k "*Ah, ah, ah, ah!* Oh, my god..."
    mc "Do you like it like this, Do you love being treated like my little bitch?"
    k "Yeah, I love it, *Ah, ah, ah!*"
    mc "Haah... you're so tight. *Uhh*"
    k "*Ah, ah, ah*"
    scene ch8_k_sex_3_pov2_cmo with dissolve
    k "*Ah, ah, ah*"
    k "It's weird that [s] isn't bothering us."
    mc "Don't summon her."
    k "*Hah, hah* I saw her at breakfast and then I didn't see her again all day."
    mc "She's sleeping."
    k "That's strange..."
    pause
    scene ch8_k_sex_3_pov3_cmo with dissolve
    k "*Hah, ahmm!*, I'm going to cum again."
    mc "*Hngh!*, I'm close too.."
    k "*Ah, ah!*, cum outside."
    $ anim_speed = 0.01
    pause
label ch8_k_sex_3_pov1_settings:
    scene ch8_k_sex_3_pov1_cmo with dissolve
    call screen ch8_k_sex_3_pov1_settings with dissolve
label ch8_k_sex_3_pov2_settings:
    scene ch8_k_sex_3_pov2_cmo with dissolve
    call screen ch8_k_sex_3_pov2_settings with dissolve
label ch8_k_sex_3_pov3_settings:
    scene ch8_k_sex_3_pov3_cmo with dissolve
    call screen ch8_k_sex_3_pov3_settings with dissolve

label afterch8_k_sex_3_pov1_settings:
    k "*Ngh!*, I'm going to cum now."
    k "*Ah, ah, ah!* Do it outside, remember."
    stop voicefx fadeout 0.5
    $ anim_speed = 0.01
    scene ch8_288 with cumming
    with flash
    mc "*Argh!*"
    scene ch8_289 with dissolve
    mc "Whew..."
    k "Hah... god, that was good..."
    k "Remember... dad is coming, you should go."
    mc "Right."
    $ renpy.end_replay()
    pause
    scene ch8_290 with dissolve
    mc "Do you want me to lower the volume on the monitor?"
    k "..."
    mc "(She fell asleep...)"
    mc "I'll lock the door just in case..."
    k "..."
    mc "I'm so thirsty, I'll go get a glass of water."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    scene ch8_294 with dissolve
    play music scene1 fadein 1.5
    a "[mc], where were you?"
    mc "I was...{w=0.4} outside."
    a "I was looking for you."
    a "I'm bored..."
    a "Do you want to come with me to the supermarket?"
    mc "Of course."
    scene ch8_298 with dissolve
    mc "Unless you think I'm too annoying."
    a "What? No, why do you say that?"
    mc "Well, someone thought I was annoying when I tried to help in the kitchen."
    a "I didn't say annoying, I said distracting."
    mc "At the end of the day, it's the same thing."
    a "No, sir."
    scene ch8_295 with dissolve
    a "A distraction can be a good thing, like something you enjoy so much that you put other things aside."
    a "And that's what you are, my distraction."
    mc "I see... I love being your distraction then."
    a "*Giggles*"
    mc "(Wow.)"
    image ch8_296anim:
        "ch8_296" with dissolve
        1.5
        "ch8_297" with dissolve
        1.5
        repeat
    scene ch8_296anim with dissolve
    pause
    mc "(Was that some kind of flirting or am I imagining things again?)"
    mc "(Maybe it's silly to be surprised that she's flirting when in the kitchen I rubbed my bulge against her ass and she allowed it.)"
    mc "(But this is very unusual for her.)"
    a "So, what do you say, will you come with me?"
    scene ch8_299 with dissolve
    mc "Sure, of course."
    mc "Let's go to Walmarket, they sell what we're looking for."
    a "The ceiling lamps?"
    mc "Yes, I saw they had them the other day."
    a "Alright, I'll go change, I don't want to go in these clothes."
    mc "You look perfect just like that."
    a "You always think I look perfect no matter what."
    mc "Obviously."
    a "*Giggles* I'll go change."
    mc "Me too."
    scene blackscreen with dissolve
    pause
    scene ch8_129 with dissolve
    mc "Are you ready?"
    a "Yes, let's go."
    show ch8_300in with dissolve:
        zoom 0.75
        xalign 0.5
        yalign 0.0
    mc "You look beautiful."
    show ch8_300in:
        zoom 0.75
        xalign 0.5
        yalign 0.0
        ease 3 yalign 0.35 zoom 0.9
    a "I wanted to look pretty today."
    mc "Nice necklace."
    a "It's an amethyst, [d] gave it to me..."
    mc "Oh, it's nice..."
    pause
    a "Although this blouse has a weird cut."
    show ch8_300in:
        yalign 0.35 zoom 0.9
        ease 1 zoom 0.75 xalign 0.5 yalign 0.0
    mc "Weird cut?"
    a "Yes, the cut."
    show ch8_301in with dissolve:
        yalign 0.0 xalign 0.5 zoom 1.0
    a "It has this kind of ''v'' shape tail."
    show ch8_301in:
        yalign 0.0 xalign 0.5 zoom 1.0
        ease 3 yalign 1.0 
        ease 3 yalign 0.5 zoom 1.15
    pause 3.0
    mc "Oh, I see now..."
    pause
    mc "I think it's cute..."
    mc "(She's doing it on purpose...)"
    mc "Its a nice rear."
    mc "(Why the hell did I say that?)"
    a "Ahem, well, you also look very handsome."
    show ch8_300in with dissolve:
        zoom 0.75
        xalign 0.5
        yalign 0.0
    a "Shall we go now?"
    mc "Let's go."
    scene ch8_130 with dissolve
    a "Should we take a taxi?"
    mc "Is there something wrong with the car?"
    a "[d] took it, and I don't want to use his fancy car."
    mc "I don't mind taking a taxi."
    stop music fadeout 2.0
    scene blackscreen with Dissolve(2.0)
    pause
    play music scene2 fadein 1.5
    scene ch8_134 with dissolve
    a "Look at this lantern, [mc], how beautiful."
    mc "It's beautiful."
    a "I really like it... but it wouldn't fit well in the backyard, it's more for the front area."
    mc "Let's buy it, it could look good."
    a "Meh, I'm not sure."
    mc "It could look good on the balcony, you need some lighting there."
    a "Yeah, it could be... we'll decide later."
    pause
    scene ch8_135 with dissolve
    mc "Look [a], here's what we were looking for."
    a "Oh!"
    scene ch8_135- with dissolve
    a "Yes, I love it!"
    a "But can we see them lit up?"
    scene ch8_135-- with dissolve
    a "They are connected."
    a "Here's the switch."
    scene ch8_136 with dissolve
    a "They're beautiful, [mc]!"
    mc "So, are we taking these?"
    a "Yes, I love them."
    a "Uh, but they're a bit expensive..."
    mc "I'll buy them."
    a "Money is not a problem, [mc]."
    mc "(Now that I remember, I don't even have a penny left...)"
    a "Should we ask the shopkeeper to give them to us or what?"
    mc "(I wish I could always buy her whatever she wants with my money.)"
    mc "(I need to find a job as soon as possible...)"
    mc "(Tomorrow morning, I'll hit the streets to look for a job, I don't care if it's at Burger Prince or McDonald's.)"
    mc "I think these are display models, I'll ask the shopkeeper."
    pause
    scene ch8_131 with fade
    mc "Should I put the bulbs here at the back?"
    a "No, there's no space left, they'll break."
    "{size=+5}{color=#FFE800}Taxi Driver{/size}{/color}: You can put them inside the taxi without any problem, ma'am."
    a "Thank you."
    scene ch8_132 with dissolve
    a "Finally, we bought them."
    mc "Yes."
    a "What will be our new project now?"
    mc "We'll find something new to do."
    mc "Well, we have to finish this first."
    a "Right."
    show ch8_132in:
        zoom 0.75 xalign 0.5
        ease 1.5 zoom 1.2 xalign 0.5 yalign 0.6    
    mc "(Damn, her boobs look great from here...)"
    pause
    a "Well, let's go now to install them and enjoy an evening sipping tea with the beautiful lighting these bulbs provide."
    show ch8_132in:
        zoom 1.2 xalign 0.5 xalign 0.5
        ease 1 zoom 0.75  xalign 0.5
    mc "Your plan sounds fabulous, but you make installing them sound so easy, haha."
    mc "I still don't even have a clear idea of how I'm going to do it."
    scene ch8_133 with dissolve
    a "You're a smart guy, I know you can do it."
    a "Plus, I'll help you."
    show ch8_133in: 
        zoom 0.75 xalign 0.5 yalign 0.0 
        ease 2 zoom 1.2 xalign 0.5 yalign 1.0
 
    mc "You're right, between the two of us, we'll surely do it quickly..." 
    mc "(Although if I have that ass close, I don't know if I'll be able to concentrate...)" 
    pause 
    scene blackscreen with dissolve 
    pause 
    scene ch8_137 with dissolve 
    mc "(I thought it would just be unscrewing and breaking the roof a bit, but it's more difficult than that...)" 
    mc "(I'll have to break the ceiling and patch it up.)" 
    mc "(What does scare me a little is all the wiring stuff, I've seen on YouTube how it's done, but I'm nervous, I don't want to mess it up.)" 
    a "Are you sure you don't need help?" 
    scene ch8_138 with dissolve 
    mc "Yes, don't worry." 
    a "Don't be stubborn, let me help you, I have nothing to do and I'm bored alone." 
    a "Besides, this was a project between the two of us, as far as I remember." 
    mc "You're right." 
    scene ch8_139- with dissolve 
    a "So, what do we need to do first?" 
    mc "Well..."
    scene ch8_139 with dissolve
    mc "First, we gotta get rid of that light fixture over there."
    a "It's easy."
    mc "Yeah, it is."
    mc "What I was thinking is that the default fixtures look ugly with those supports they come with."
    mc "I think we can use pot hangers instead."
    mc "Those metal rods are hollow, we can run the wires through them so they won't be visible from the outside."
    a "What about the flower pots?"
    mc "We can screw the pot strings directly into the ceiling with some concrete screws and anchors."
    mc "They're small pots, so I don't think there will be any issue with the weight."
    a "Do we need to remove the light fixture completely?"
    scene ch8_139- with dissolve
    mc "Yeah, we gotta remove it all, unless you want a cable running across the entire wall."
    a "No, that would look bad."
    a "Let's get to work then."
    scene ch8_141 with dissolve
    pause 
    scene ch8_142 with dissolve
    pause 
    scene ch8_143--- with dissolve
    pause 
    scene blackscreen with dissolve
    pause
label ch8a2:
    if _in_replay:
        show screen Replayexit
    scene ch8_145 with dissolve
    a "Sweetie, it looks beautiful!"
    a "Painting the rods black was a fantastic idea."
    mc "I did my best."
    scene ch8_146 with dissolve
    a "And it turned out perfect, honey."
    mc "Thanks."
    pause
    scene ch8_147 with dissolve
    a "Another achievement."
    mc "Yeah."
    mc "It took us a while, but we did it."
    scene ch8_148 with dissolve
    a "Took us? I literally didn't help you at all this time."
    mc "Your company was more than enough."
    mc "There was a moment when it got stressful, and having you there helped."
    scene ch8_149 with dissolve
    a "Aww, baby."
    a "I get happy when we do things together, things like this makes me feel I'm productive."
    mc "Yeah."
    a "What do you want for dinner? We're having whatever you say tonight."
    mc "Hmmm, anything is fine."
    a "Come on, ask for something, whatever you want."
    mc "Hmm, I don't really have a craving for anything."
    mc "Can I ask for something else?"
    a "If it's within my posibilities, you can ask for it."
    mc "A kiss?"
    a "Just a kiss?"
    scene ch8_151 with dissolve
    stop music fadeout 2.0
    mc "I don't just want a kiss, [a]."
    mc "I want... {w=0.4} a nice kiss."
    a "A nice kiss..."
    a "O-of course, you deserve a nice kiss."
    play music sexy3 fadein 2.0
    scene ch8_152 with dissolve
    pause
    scene ch8_153 with dissolve
    a "Hmm..."
    pause
    scene ch8_153- with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    a "Hahm... smnch"
    image ch8_153anim:
        "ch8_153" with dissolve
        2
        "ch8_153-" with dissolve
        2
        repeat
    scene ch8_153anim with dissolve
    a "Smnchm, ahlm, mnha"
    pause
    image ch8_153---anim:
        "ch8_153---" with dissolve
        2
        "ch8_153----" with dissolve
        2
        repeat
    scene ch8_153---anim with dissolve
    a "Smnch, snch, smnch"
    mc "(The sensation of her tongue entwined with mine is exhilarating...)"
    pause
    scene ch8_153--1 with dissolve
    mc "(I can't just kiss her and not touch her delicious breasts.)"
    mc "(The temptation is too strong... it would be a sin not to do it.)"
    pause
    scene ch8_153--2 with dissolve
    pause
    mc "(She isn't saying anything...)"
    mc "(I guess that's a green light to continue.)"
    pause
    scene ch8_153--3 with dissolve
    a "Oh... Smnch"
    mc "(How delightful...)"
    mc "(And her hand... it seems I'm not the only one tempted to touch.)"
    mc "(She wants to feel my bulge...)"
    scene ch8_153--5 with dissolve
    mc "Oh..."
    mc "(That's right, feel it...)"
    mc "(feel with your hand the desire I have to make you mine.)"
    scene ch8_153--4 with dissolve
    mc "Oh... (She's squeezing it...)"
    mc "(She wants to feel my cock again in her hands.)"
    image ch8_153--4anim:
        "ch8_153--5" with dissolve
        1.75
        "ch8_153--4" with dissolve
        1.75
        repeat
    scene ch8_153--4anim with dissolve
    mc "(God...)"
    mc "(It feels so good.)"
    pause
    mc "(Should I say something?)"
    mc "(Maybe show some signs of pleasure to turn her on more...)"
    mc "..."
    mc "[a], your hand... feels good."
    a "Smnch, A-ah, really?"
    mc "Mnch, yes... I love how you touch me."
    pause
    mc "You have beautiful breasts."
    mc "Can I see them?"
    a "No{w=0.4}, mnch{w=0.4}, not here, honey{w=0.4}, lmhnch{w=0.4}, someone might see..."
    mc "Mmhmm, No one's going to see us."
    a "No, [mc]..."
    pause
    stop sound fadeout 0.5
    scene ch8_154- with hpunch
    a "Wait, [mc]."
    a "[d] will be here soon..."
    a "And I have to make dinner."
    mc "(Excuses...)"
    mc "[a], we were having a good time."
    a "Yes, but... it's better if I go."
    mc "(I really can't make any progress...)"
    mc "(Every time I think the timing is right, she always ends up regretting it and leaving.)"
    scene ch8_155 with dissolve
    mc "-[a]!."
    scene ch8_156 with dissolve
    pause
    a "[d] is about to arrive, and if he sees us like this..."
    mc "Uh..."
    mc "Y-yeah, you're right."
    pause
    scene ch8_157 with dissolve
    a "We got carried away."
    mc "Yeah..."
    mc "I'm sorry, I was just so excited that I..."
    a "-I know, me too..."
    a "It was... it was both of our faults."
    "..."
    pause
    scene ch8_159 with dissolve
    a "*Hmnch, hmmn, mnch*"
    pause
    scene ch8_160 with dissolve
    a "*smnch, ahlmm, mnch*"
    pause
    scene ch8_161 with dissolve
    a "*Hmnch, hmmn, mnch*"
    pause
    scene ch8_162 with dissolve
    pause
    mc "(This time the excuse was different... it's progress.)"
    pause
    scene ch8_163 with dissolve
    pause
    scene ch8_166 with dissolve
    pause
    scene ch8_168 with dissolve
    a "[mc], remember, [d]..."
    mc "We'll hear the car."
    a "Right..."
    scene ch8_167 with dissolve
    pause
    a "And what about the girls?"
    scene ch8_165 with dissolve
    a "How would we explain this to the girls?"
    mc "Yeah, it would be difficult."
    pause
    scene ch8_167 with dissolve
    a "Well..."
    a "It's better if we go inside."
    a "Plus, I have to make dinner too, by the way, you haven't told me what you want for dinner."
    mc "I asked for a kiss, and I already got that."
    scene ch8_165 with dissolve
    a "Right *giggles*, I almost forgot."
    a "Well, let's go inside now."
    mc "Yeah."
    stop music fadeout 5.0
    scene ch8_169 with dissolve
    pause
    a "..."
    a "Erm..."
    pause
    a "[mc]."
    mc "Yes?"
    a "I-I almost forgot."
    scene ch8_170 with dissolve
    a "I want to show you where I want to place the lantern we bought."
    mc "Now?"
    a "Y-yes, but you don't have to install it right away..."
    scene ch8_171 with dissolve
    mc "I wouldn't mind doing it."
    a "I just want you to see where I want it and tell me if you can do it or not."
    a "Asking you to install it now would be exploitative."
    mc "No, haha, not at all."
    a "Let's go, and I'll let you rest."
    scene blackscreen with dissolve
    pause
    scene blackscreen with dissolve
    pause
    scene ch8_172 with dissolve
    mc "Oh, I see."
    mc "Yes, it's practically the same as what we did downstairs."
    mc "It'll just be replacing it."
    scene ch8_173 with dissolve
    mc "Yeah, I can do it."
    a "Great."
    a "Well, let's go inside already, I'm freezing."
    scene blackscreen with dissolve
    pause
    scene ch8_174 with dissolve
    a "I miss my bed..."
    scene ch8_175 with dissolve
    a "Uh, these heels are killing me."
    mc "Let me help you."
    play music sexy2 fadein 3.0
    scene ch8_176 with dissolve
    pause
    mc "I don't know how women can walk on these things all day."
    a "It's the sacrifice you have to make to be pretty."
    scene ch8_177 with dissolve
    mc "Those are things I'll never understand about women."
    a "Well, I really like them."
    mc "Indeed, women look great in heels."
    mc "They have a certain something that makes them look different."
    scene ch8_178 with dissolve
    a "See?"
    mc "That doesn't mean they're comfortable."
    pause
    scene ch8_180 with dissolve
    a "What are you doing, [mc]?"
    mc "A massage, feeling like it?"
    a "Yeah, sure."
    pause
    a "It's a bit selfish of me to let you give me a massage when you were the one working."
    mc "I was wearing sneakers, plus I'm not tired."
    a "Okay."
    scene ch8_181 with dissolve
    a "Oh... hmhmm, I needed this."
    a "You're good..."
    mc "Thank you."
    pause
    scene ch8_183 with dissolve
    a "[mc]?"
    mc "A kiss to make the soreness go away."
    a "Hmm..."
    mc "You have pretty feet..."
    a "Thanks, no one has ever complimented my feet before."
    mc "Don't lie."
    a "Seriously."
    mc "Well, you have beautiful feet."
    a "*Giggles*"
    pause
    scene ch8_184 with dissolve
    mc "(They really are beautiful, even exciting in a way.)"
    pause
    scene ch8_185 with dissolve
    mc "Hmmm..."
    a "Oh..."
    pause
    scene ch8_186 with dissolve
    pause
    scene ch8_187 with dissolve
    a "Oh, [mc]..."
    pause
    scene ch8_186 with dissolve
    mc "([a] is beautiful from head to toe, literally.)"
    mc "(This is turning me on...)"
    scene ch8_189 with dissolve
    pause
    a "..."
    pause
    scene ch8_190 with dissolve
    mc "Oh..."
    pause
    scene ch8_188 with dissolve
    mc "(And I think I'm not the only one.)"
    pause
    scene ch8_190 with dissolve
    pause
    mc "(Was that not an accident, or was it?)"
    scene ch8_191 with dissolve
    mc "(There's my answer.)"
    mc "(It's the first time she's taken the initiative...)"
    pause
    scene ch8_192 with dissolve
    pause
    scene ch8_194 with dissolve
    pause
    image ch8_194anim:
        "ch8_192" with dissolve
        1.6
        "ch8_194" with dissolve
        1.6 
        repeat
    scene ch8_194anim with dissolve
    mc "(God...)"
    pause
    image ch8_193anim:
        "ch8_193" with dissolve
        1.6
        "ch8_191" with dissolve
        1.6
        repeat
    scene ch8_193anim with dissolve
    mc "Oh..."
    mc "Hmm..."
    a "Does it feel good?{w=0.4}{nw}"
    a "I mean, it feels good..."
    a "It wasn't a question, it was a statement."
    a "The massage feels good..."
    pause
    scene ch8_195 with dissolve
    a "T-thank you, I'm good now, sweetie."
    mc "A-are you sure, don't you want me to massage a little more?"
    a "No, thanks."
    scene ch8_196 with dissolve
    mc "*Gulp* (I didn't know my bulge was so noticeable...)"
    pause
    a "Do you want me to give you a massage now?"
    scene ch8_197 with dissolve
    mc "M-me? I mean, you?"
    mc "(Why the hell am I getting nervous?)"
    mc "(I'm taken by surprise by [a] taking the initiative.)"
    a "Yes, me, *giggles*"
    scene ch8_198 with dissolve
    a "You've been holding those lights up with your arms raised for a long time; your muscles must be tense."
    mc "(Yeah, especially the one on my crotch.)"
    image ch8_199anim:
        "ch8_199" with dissolve
        1.6
        "ch8_199-" with dissolve
        1.6
        repeat
    scene ch8_199anim with dissolve
    a "You're tense; relax your shoulders."
    a "Wow, I think you've grown a bit..."
    a "Your shoulders are bigger; exercise really does wonders."
    mc "Yeah, I changed my routine a bit and have been focusing more on my shoulders."
    a "Hmm... It's definitely working."
    a "Oh, my poor baby, with your new routine and this, you must have wrecked shoulders."
    scene ch8_200 with dissolve
    a "*Muah*"
    pause
    scene ch8_199anim with dissolve
    a "Lie down on the bed."
    pause
    scene ch8_202 with dissolve
    a "Hmm.."
    pause
    scene ch8_203 with dissolve
    mc "..."
    pause
    a "I love you so much, [mc]."
    scene ch8_202 with dissolve
    mc "I love you too."
    a "Hmhmm..."
    a "My spoiled young man..."
    mc "No, you're my spoiled girl."
    scene ch8_204 with dissolve
    a "*giggles*, I think we're both spoiled by each other."
    mc "Yeah... {w=0.5}But you more than me."
    scene ch8_205 with dissolve
    pause
    scene ch8_204 with dissolve
    a "That's not true."
    mc "I gave you a foot massage."
    a "Doesn't my shoulder massage count?"
    mc "A foot massage is worth more."
    a "I cook for you."
    mc "I clean the car."
    a "I clean the living room and the house in general."
    mc "I sweep the backyard and front yard."
    a "I wash your underwear, sometimes."
    mc "Hmm.."
    pause
    mc "Alright, you win."
    a "*Giggle*"
    scene ch8_205 with dissolve
    pause
    scene ch8_206 with dissolve
    pause
    scene ch8_206- with dissolve
    pause
    image ch8_206--anim:
        "ch8_206-" with dissolve
        1.6
        "ch8_206--" with dissolve
        1.6
        repeat
    scene ch8_206--anim with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    a "*Mmhm, mmmhm*"
    pause
    scene ch8_206--- with dissolve
    pause
    scene ch8_206---- with dissolve
    pause 1.5
    scene ch8_206--- with dissolve
    pause
    scene ch8_216 with dissolve
    mc "..."
    pause
    scene ch8_217 with dissolve
    pause
    image ch7_217anim:
        "ch8_218" with dissolve
        1.6
        "ch8_217" with dissolve
        1.6
        repeat
    scene ch7_217anim with dissolve
    mc "Oh... [a]."
    a "..."
    pause
    stop sound fadeout 0.5
    scene ch8_221 with dissolve
    a "You have a huge...{w=0.4} boner."
    mc "Yeah, I think all of this got me a little excited."
    image ch8_220anim:
        "ch8_220" with dissolve
        1.6
        "ch8_219" with dissolve
        1.6
        repeat
    scene ch8_220anim with dissolve
    a "You sure did..."
    mc "(Looks like [a] is slowly losing her shyness.)"
    pause
    scene ch8_210 with dissolve
    pause
    scene ch8_211 with dissolve
    mc "(While we're at it, I'm gonna touch too.)"
    pause
    scene ch8_212 with dissolve
    mc "(What an ass, god...)"
    pause
    scene ch8_214 with dissolve
    mc "(I'm too horny.)"
    mc "(I hope she doesn't mind if...)"
    pause
    scene ch8_213 with dissolve
    a "Oh."
    pause
    scene ch8_214 with dissolve
    a "..."
    mc "(Not a word, that's the green light.)"
    pause
    image ch8_213anim:
        "ch8_213" with dissolve
        1.7
        "ch8_214" with dissolve
        1.7
        repeat
    scene ch8_213anim with dissolve
    mc "(These leggings are so thin that I can feel her vagina through them.)"
    mc "(I can't believe it.)"
    mc "(It's incredible that she lets me touch her so lewdly.)"
    mc "(This is too damn hot.)"
    pause
    scene ch8_225 with dissolve
    pause
    scene ch8_226- with dissolve
    a "Oh..."
    a "Baby..."
    pause
    mc "Is it okay if I get a little carried away?"
    scene ch8_222 with dissolve
    a "..."
    mc "Just a little bit?"
    a "Just a little bit..."
    a "..."
    a "O-okay..."
    scene ch8_230- with dissolve
    a "Oh... [mc].."
    a "..."
    pause
    scene ch8_231 with dissolve
    a "That's what you meant..."
    mc "(You're not escaping this time.)"
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    scene ch8_230 with dissolve
    a "Hm!"
    mc "*Hmnch*"
    a "*Hmnch, nsch*"
    pause

init python:
    def c8at1p2_(trans, st, at):  
        trans.set_child("c8at1p2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value            
init python:
    def c8at1p1_(trans, st, at):  
        trans.set_child("c8at1p1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value          
screen c8at1p1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterchoicec8at1p21_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("c8at1p2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    
screen c8at1p2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.06) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterchoicec8at1p21_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("c8at1p1_") style "textbutton_choice"    
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    

label beforec8at1p1_:
    image c8at1p2_:
        function c8at1p2_
    image c8at1p1_:
        function c8at1p1_    
    $ anim_speed = 0.05
    scene c8at1p2_ with dissolve
    a "*Hmm*, [mc]..."
    a "Ohmm, *lmahl, lahl*"
    pause
    mc "I love you, [a]."
    a "Baby..."
    pause
    a "This is too much, [mc]..."
    mc "It's not."
    pause
    scene c8at1p1_ with dissolve
    mc "We did more yesterday."
    a "Nothing happened yesterday."
    mc "(Right, we promised not to talk about it again.)"
    pause

label c8at1p2_:
    scene c8at1p2_ with dissolve
    call screen c8at1p2_settings with dissolve
label c8at1p1_:
    scene c8at1p1_ with dissolve
    call screen c8at1p1_settings with dissolve    
label afterchoicec8at1p21_:
    stop sound fadeout 0.5
    scene ch8_232 with dissolve
    a "I think that's enough..."
    pause
    scene ch8_233 with dissolve
    a "..."
    pause
    scene ch8_236 with dissolve
    a "But you're still hard..."
    mc "Yeah..."
    a "[mc], yesterday... do you remember what we agreed on?"
    mc "Nothing happened yesterday."
    mc "And nothing's happening today either."
    a "..."
    a "O-okay."
    pause
    show ch8_237-in with flash:
        zoom 0.9
        yalign 1.0 xalign 0.5
        ease 7 yalign 0.0 xalign 0.5
        ease 3.5 zoom 0.65
    mc "Oh..."
    mc "Wow, [a]..."
    mc "(What a beauty!)"
    mc "(I feel like I'm gonna cum just from looking at her...)"
    a "Erm...{w=0.4} Aren't you gonna say anything?"
    mc "Uh..."
    mc "Sorry, you caught me off guard, wow..."
    mc "I just wasn't expecting this at all."
    show ch8_237-in:
        yalign 0.0 xalign 0.5 zoom 0.65
        ease 7 zoom 0.5
    a "You have that huge...{w=0.4} and I...{w=0.4} well..."
    a "I-I'm gonna make you lose that erection... {w=0.4}unless you don't want me to, of course."
    mc "Of course I want to!"
    mc "There's no way I wouldn't want to!" 
    a "*Giggle*"
    a "I know how much you love these, so I'm gonna use them."
    a "Get comfortable, baby."
    mc "(God...)"
    pause
    scene ch8_237--- with fade
    mc "(God...)"
    mc "[a], this is so sudden."
    a "You've had this erection since you finished installing the lights, I can't let you go like this."
    a "Plus, I... I also..."
    scene ch8_a_titjob1_pov1_15 with dissolve
    a "Erm..."
    pause
    scene ch8_237--- with dissolve
    a "Remember, this will remain a secret, ok?"
    mc "I know, [a]."
    a "Good."
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_a_titjob1_pov1_(trans, st, at):  
        trans.set_child("ch8_a_titjob1_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/masturbating/cutmastrubating14.ogg", "audio/masturbating/cutmastrubating16.ogg", "audio/masturbating/cutmastrubating18.ogg", "audio/masturbating/cutmastrubating20.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 10:
            sound_files = ["audio/masturbating/cutmastrubating13.ogg", "audio/masturbating/cutmastrubating15.ogg", "audio/masturbating/cutmastrubating17.ogg", "audio/masturbating/cutmastrubating19.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_a_titjob1_pov2_(trans, st, at):  
        trans.set_child("ch8_a_titjob1_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/masturbating/cutmastrubating14.ogg", "audio/masturbating/cutmastrubating16.ogg", "audio/masturbating/cutmastrubating18.ogg", "audio/masturbating/cutmastrubating20.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 10:
            sound_files = ["audio/masturbating/cutmastrubating13.ogg", "audio/masturbating/cutmastrubating15.ogg", "audio/masturbating/cutmastrubating17.ogg", "audio/masturbating/cutmastrubating19.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value     

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_a_titjob1_pov3_(trans, st, at):  
        trans.set_child("ch8_a_titjob1_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/masturbating/cutmastrubating14.ogg", "audio/masturbating/cutmastrubating16.ogg", "audio/masturbating/cutmastrubating18.ogg", "audio/masturbating/cutmastrubating20.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 10:
            sound_files = ["audio/masturbating/cutmastrubating13.ogg", "audio/masturbating/cutmastrubating15.ogg", "audio/masturbating/cutmastrubating17.ogg", "audio/masturbating/cutmastrubating19.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value     
        
screen ch8_a_titjob1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterlabelch8_a_titjob1_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_a_titjob1_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_a_titjob1_pov3_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_a_titjob1_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterlabelch8_a_titjob1_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_a_titjob1_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_a_titjob1_pov3_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_a_titjob1_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterlabelch8_a_titjob1_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_a_titjob1_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_a_titjob1_pov2_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  


label beforech8_a_titjob1_pov1:
    image ch8_a_titjob1_pov1_:
        function ch8_a_titjob1_pov1_
    image ch8_a_titjob1_pov2_:
        function ch8_a_titjob1_pov2_
    image ch8_a_titjob1_pov3_:
        function ch8_a_titjob1_pov3_
    $ anim_speed = 0.05    
    scene ch8_a_titjob1_pov1_ with dissolve
    mc "Oh, [a], I love your boobs, I've never seen anything like them."
    a "Thanks."
    mc "They're big but still firm... are they fake?"
    a "*Giggle*, do you really think so?"
    mc "Come on, you must be blind if you can't see it for yourself."
    mc "You have dream boobs."
    a "Oh, thanks... "
    scene ch8_a_titjob1_pov2_ with dissolve
    a "Actually... {w=0.4}they're one of my favorite things about my body."
    mc "What are the other things?"
    a "*Giggle*, stop it, [mc]."
    pause
    a "And no, they're not fake."
    mc "Wow... God really does have favorites."
    mc "(Like me right now.)"
    scene ch8_a_titjob1_pov3_ with dissolve
    a "I-I didn't know a penis could be this big."
    mc "Yeah, my penis is big."
    a "Very big..."
    a "..."
    pause
    scene ch8_a_titjob1_pov1_ with dissolve
    a "Er, enough talk *giggle*."
    $ anim_speed = 0.035
    a "Focus on finishing, baby."
    a "Let it out."
    mc "Oh, yeah... *hmm*."
    pause
    jump ch8_a_titjob1_pov1_

label ch8_a_titjob1_pov1_:
    scene ch8_a_titjob1_pov1_ with dissolve
    call screen ch8_a_titjob1_pov1_settings with dissolve

label ch8_a_titjob1_pov2_:
    scene ch8_a_titjob1_pov2_ with dissolve
    call screen ch8_a_titjob1_pov2_settings with dissolve    

label ch8_a_titjob1_pov3_:
    scene ch8_a_titjob1_pov3_ with dissolve
    call screen ch8_a_titjob1_pov3_settings with dissolve

label afterlabelch8_a_titjob1_pov:
    scene ch8_a_titjob1_pov1_ with dissolve
    $ anim_speed = 0.01
    mc "*Hngh* Almost there..."
    a "That's it, baby, let it flow..."
    a "So you feel good and relaxed..."
    a "It's the least a hardworking [arelatmc] like you, who takes such good care of their [arelat], deserves..."
    mc "*Oh.. hmngh!*"
    mc "*Hmnghh!* Here it comes, *Ngh!*"
    pause
    play sound "audio/carengine.mp3" volume 0.5
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1.0
    scene ch8_237----in with dissolve
    stop music fadeout 1.5
    a "Ah!"
    a "Was that... {w=0.4}was that a car?"
    mc "I think so."
    scene ch8_237-----in  with vpunch
    play music doing fadein 3.0
    a "[d]!"
    a "Quick, get dressed!"
    mc "(Damn it, not now.)"
    a "Hurry!"
    scene ch8_237------in with dissolve
    a "Let's go quickly."
    mc "Okay."
    a "And this..."
    mc "Not a word about this."
    a "..."
    a "See you at dinner."
    mc "I don't think I can stay awake until dinner, I'm exhausted."
    a "Are you feeling sick?"
    mc "I'm just tired, today was a pretty hectic day for me."
    a "I'll leave something in the fridge in case you wake up later, okay?"
    mc "No need, I'll probably sleep until tomorrow."
    a "Rest well, honey."
    $ renpy.end_replay()
    pause
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    scene ch8_302 with dissolve
    mc "Uh, I'm so sleepy..."
    mc "(I came like a damn rabbit today, that's probably why I'm so tired.)"
    pause
    mc "(Uhh, but my balls hurt a little...)"
    mc "(Damn it, why did [drelat] [d] have to show up now?)"
    mc "(I would have loved to cover those tits with my cum again..)"
    mc "(There will surely be another opportunity with [a]... I hope.)"
    pause
    if stephloving != "True":
        jump ch8_after2s
label ch8s3:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
    scene blackscreen with dissolve
    "Zzz..."
    pause
    s "[mc]."
    play music scene3 fadein 1.5
    scene ch8_303 with Dissolve(2.0)
    mc "Huh?"
    mc "Is it already morning?"
    s "No, it's nine o'clock."
    s "Are you going to sleep already?"
    mc "Yes, that's what I was doing."
    s "Oh, okay..."
    s "I came for... you know."
    s "Well, also because you didn't eat dinner."
    s "Are you okay?"
    mc "Yeah, just a little tired."
    s "I see..."
    s "Everyone is upstairs watching a show and I wanted to take advantage of coming here with you."
    mc "[s], I'm really tired right now."
    s "I see..."
    s "I'll be back at five o'clock."
    mc "(No way, tonight I want to sleep well.)"
    mc "(I'll do it quickly and then go to sleep.)"
    mc "Come in, and lock the door behind you."
    s "Okay."
    scene ch8_306 with fade
    s "*Mmm, lhmhmm...*"
    s "*Blah*"
    s "Hehe, don't squeeze so hard, silly."
    scene ch8_304 with dissolve
    mc "Sorry, it's just that you have a very squeezable butt."
    scene ch8_305 with dissolve
    s "Ooh, *giggle*"
    image ch8_305anim:
        "ch8_304" with dissolve
        1.65
        "ch8_305" with dissolve
        1.65
        repeat
    scene ch8_305anim with dissolve
    s "[mc], I want you to lick me there now."
    s "We don't have much time."
    mc "Get on top of me."
    scene blackscreen with fade
    s "Like this?"
    mc "The other way around."
    s "Like this?"
    mc "Exactly, perfect."
    scene ch8_307 with dissolve
    mc "Such a delicious butt."
    s "*Giggle* You love it."
    mc "Yeah."

init python:
    def ch8_s_cnlngs_2_pov1_(trans, st, at):  
        trans.set_child("ch8_s_cnlngs_2_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_69_pov1_(trans, st, at):  
        trans.set_child("ch8_s_69_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_65.ogg", "audio/wavs/bj_71.ogg", "audio/wavs/bj_63.ogg", "audio/wavs/bj_80.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 10:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_3.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 1.0:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)() 
        return store.anim_speed  
    def update_anim_speed(value):
        store.anim_speed = value          

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_69_pov2_(trans, st, at):  
        trans.set_child("ch8_s_69_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_65.ogg", "audio/wavs/bj_71.ogg", "audio/wavs/bj_63.ogg", "audio/wavs/bj_80.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 10:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_3.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_s_69_pov3_(trans, st, at):  
        trans.set_child("ch8_s_69_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_65.ogg", "audio/wavs/bj_71.ogg", "audio/wavs/bj_63.ogg", "audio/wavs/bj_80.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 10:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 1:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/s/sbjmoan_3.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/s/sbjmoan_4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         

screen ch8_s_cnlngs_2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterchoicec8at1p21_") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
 

screen ch8_s_69_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_s_cnlngs_2_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_s_69_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_s_69_pov3_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
    
screen ch8_s_69_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_s_cnlngs_2_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_s_69_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_s_69_pov3_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
    
screen ch8_s_69_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_s_cnlngs_2_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_s_69_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_s_69_pov2_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  


label afterch8s69:
    image ch8_s_cnlngs_2_pov1_:
        function ch8_s_cnlngs_2_pov1_
    image ch8_s_69_pov1_:
        function ch8_s_69_pov1_
    image ch8_s_69_pov2_:
        function ch8_s_69_pov2_
    image ch8_s_69_pov3_:
        function ch8_s_69_pov3_      
    
    scene ch8_309 with dissolve
    pause
    scene ch8_308 with dissolve
    pause
    $ anim_speed = 0.05
    scene ch8_s_cnlngs_2_pov1_ with dissolve
    play voicefx "audio/wavs/s/smoansoft.ogg" loop
    s "Yes, like that."
    s "Hmhmm..."
    pause
label afterch8_s_cnlngs_2_pov1_:
    stop sound fadeout 0.5
    scene ch8_310 with dissolve
    s "I'm going to give you oral sex too."
    s "I'm going to suck you with so much love."
    scene ch8_s_69_pov1_ with dissolve
    s "*Gag, gag, gulp*"
    mc "Oh, yeah... that feels so good."
    mc "Make sure to circle the head with your tongue."
    s "*Moans*, *Slurp, suck, slurp*"
    mc "(Is it just me or is she getting better and better at this?)"
    s "*Slurp, suck, gulp, moan*"
    pause
    scene ch8_s_69_pov2_ with dissolve
    s "*Moans*, *Slurp, slurp*"
    s "Mhmmh..."
    s "*Slurp, gulp, moan*"
    s "I love sucking you off while you suck me."
    s "It's{w=0.4} *Moans*{w=0.4}, so much more exciting this way."
    mc "It's called sixty-nine."
    s "Oh, *Slurp, slurp* I didn't know that."
    mc "(I can't believe it... I'm teaching sexual positions to my little [srelat]...)"
    pause
    scene ch8_s_69_pov3_ with dissolve
    s "*Moans* [mc], that feels so good..."
    s "*I'm going to feel good soon...*Uhh*, *Grunts*."
    s "Uff... that feels so good."

label ch8_s_69_pov1_:
    scene ch8_s_69_pov1_ with dissolve
    call screen ch8_s_69_pov1_settings
label ch8_s_69_pov2_:
    scene ch8_s_69_pov2_ with dissolve
    call screen ch8_s_69_pov2_settings
label ch8_s_69_pov3_:
    scene ch8_s_69_pov3_ with dissolve
    call screen ch8_s_69_pov3_settings

label afterch8_s_cnlngs_2_pov:
    scene ch8_s_69_pov1_ with dissolve
    mc "*Argh* *Hnghhh!!!*"
    scene ch8_312 with cumming
    with flash
    play sound "audio/mouth/swallow_03.ogg"
    mc "Hah..hahh..."
    mc "God..."
    pause
    image ch8_313anim:
        "ch8_314" with dissolve
        1.7
        "ch8_313" with dissolve
        1.7
        repeat
    scene ch8_313anim with dissolve
    mc "Oh... {w=0.4}hey.."
    s "*Slurp, slurp, slurp*"
    mc "[s], s-stop... *Ahh*.."
    s "*Slurp*"
    scene ch8_312 with dissolve
    s "*Buhg..* I thought I drooled..."
    s "But it's your semen..."
    image ch8_313imagen:
        "ch8_313" with dissolve
        1.0
        "ch8_314" with dissolve
        1.0
        "ch8_315" with dissolve
    scene ch8_313imagen with dissolve    
    s "Huh... you came in my mouth."
    mc "I did warn you."
    s "Huh..."
    s "Uh.. okay."
    scene ch8_316 with dissolve
    s "I swallowed a little bit."
    mc "Really?"
    s "It's okay."
    with fade
    mc "Uh.. I'm falling asleep..."
    with fade
    scene ch8_317 with fade
    s "Well, I'm leaving now."
    s "Sweet dreams."
    $ renpy.end_replay()
label ch8_after2s:
    stop music fadeout 2.0
    with fade
    scene blackscreen with Dissolve(2.0)
    "Zzz..."
    pause
    scene ch8_318 with Dissolve(2.0)
    pause
    scene ch8_319 with dissolve
    if stephloving == "True":
        mc "(Uh... I have so much eye gunk that I can barely open my eyes.)"
        mc "(It's not eye gunk... I forgot to wash my face after giving [s] oral sex...)"
        mc "(I need to take a shower right now.)"
    pause
    scene blackscreen with dissolve
    pause
label ch8a3:
    if _in_replay:
        show screen Replayexit
    scene ch8_320in with dissolve
    play music scene1 fadein 1.0
    pause
    mc "Good morning."
    show ch8_321-in with dissolve:
        xalign 0.5 yalign 0.0
    a "Good morning, honey."
    show ch8_321-in:
        xalign 0.5 yalign 0.0
        ease 3 yalign 1.0
        ease 3 yalign 0.7
    a "Did you sleep well?"
    mc "Extremely well."
    scene ch8_323 with dissolve
    mc "And you, did you sleep well?"
    a "Yeah."
    a "You woke up early today."
    mc "Yesterday I went to bed early, I was a bit tired, you know."
    a "Yeah..."
    a "Are you looking for something or..."
    mc "No."
    a "I'm about to make breakfast, what do you want me to prepare for you?"
    scene ch8_324 with dissolve
    a "Yesterday you didn't want to choose dinner, so you can use the wildcard for breakfast."
    mc "{i}I didn't choose dinner because I traded it for a kiss, remember?"
    a "{i}Kisses are free."
    scene ch8_324- with dissolve
    play sound "audio/mouth/french_kiss_06.ogg"
    a "*Muah*"
    scene ch8_325 with dissolve
    mc "{i}But, I didn't just receive a kiss yesterday."
    a "{i}I don't remember that..."
    mc "Right... we don't remember it."
    mc "Hmm..."
    mc "{i}Seems like there's a glitch in the system."
    scene ch8_325- with dissolve
    mc "{i}What if for some reason I ask for that thing we don't remember again, will I still keep the wildcard for tomorrow?"
    a "{i}Ohh, sneaky."
    a "{i}Maybe we should reconsider the rules of this."
    scene ch8_325-- with dissolve
    mc "{i}But first, I'm going to ask for the same as yesterday."
    a "{i}I'm pretty sure yesterday you only asked for a kiss."
    mc "{i}Exactly, that's what I was talking about."
    mc "{i}Or do you have something else in mind?"
    a "*Giggles*, no."
    scene ch8_327-- with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    a "*Hmnch, hmm.*"
    pause
    image ch8_326anim:
        "ch8_326" with dissolve
        1.6
        "ch8_327" with dissolve
        1.6
        repeat
    scene ch8_326anim with dissolve
    a "*Hmnh*{w=0.4}, *Hmnch, hmuah*"
    pause
    scene ch8_325-- with dissolve
    pause
    stop sound fadeout 0.5
    a "{i}[mc]?"
    mc "Yes?"
    a "{i}Your hand."
    mc "{i}What about my hand?"
    scene ch8_325_1 with dissolve
    a "{i}I think your hand is a bit lost from my waist."
    mc "{i}It's not."
    mc "{i}My hand never searched for your waist."
    scene ch8_325--- with dissolve
    a "{i}Oh... You naughty boy."
    mc "{i}Does it bother you?"
    a "{i}You can leave it there for now."
    mc "{i}Hmm... maybe I'll move it."
    a "{i}Now that I give you permission, you don't want to anymore?"
    mc "{i}That's just how I am, I like going against the flow."
    scene ch8_325--2 with dissolve
    a "Ah, [mc]..."
    pause
    scene ch8_325--3--- with dissolve
    pause
    a "{i}[mc], what do you think you're doing?"
    mc "{i}Sorry, I can't resist your charms."
    scene ch8_325--4 with dissolve
    a "Oh!"
    mc "Hmm..."
    pause
    scene ch8_325--3--- with dissolve
    a "{i}You, sir, think you can do whatever you want without consequences?"
    mc "{i}I'll accept those consequences."
    a "{i}And also, cynical..."
    a "{i}I hope you're doing glute exercises at the gym."
    mc "Why should I do glute exercises at the gym? Haha."
    a "{i}Because you're earning yourself some good spankings."
    mc "*Laughs*, well, just so you know, I do glute exercises and it offends me that you haven't noticed."
    a "*Laughs*"
    mc "{i}But of course, having these..."
    image ch8_325anim:
        "ch8_325--4" with dissolve
        3
        "ch8_325--3---" with dissolve
        3
        repeat
    scene ch8_325anim with dissolve
    a "{i}[mc], that's not how you treat your [arelat]..."
    a "{i}That behind is going to be very red if you keep it up."
    mc "{i}Am I squeezing too hard?"
    a "{i}I mean yours, silly."
    mc "*Laughs*"
    a "*Laughs*"
    mc "(I never thought I'd be able to do this.)"
    mc "(I love this version of [a], the one that's not so shy, and doesn't get self-conscious about everything.)"
    pause
    scene ch8_326- with dissolve
    a "{i}Stop, [mc], someone could walk into the kitchen at any moment."
    mc "{i}You're right..."
    mc "{i}But first I want to see that behind turn red like you said."
    scene ch8_326-- with dissolve
    a "{i}Enough! *giggles*, go do something else while breakfast is ready."
    mc "{i}My kiss first."
    a "{i}I already gave you one."
    mc "{i}You said they were free."
    $ renpy.end_replay()
    d "Good morning."
    play music scene2 
    scene ch8_329 with hpunch
    mc "G-good morning, [drelat] [d]!"
    mc "(Did he see us!?)"
    d "No, no, keep talking, I just came for a glass of water."
    d "*Exhales*"
    pause
    scene ch8_332 with fade
    pause
    mc "Uh, [drelat] [d]."
    scene ch8_333 with dissolve
    mc "I'm going to install a lantern on the balcony."
    d "Oh, really?"
    mc "Yeah, I just want to know if you have any problems with that, you know, because of the noise and all that."
    d "Of course not."
    d "Can you do it? Don't you need any help?"
    mc "Don't worry, I can handle it on my own."
    d "It's no trouble, [mc], let me help you."
    mc "No, really, I'm good."
    d "Are you sure?"
    mc "Yes, don't worry about it."
    d "Hey, are you coming with us later?"
    d "I'm taking the girls out to eat and have some fun."
    mc "Are we all going?"
    d "I wish, but... you know who's not coming."
    mc "Sorry, I'll be doing what I mentioned you."
    d "[mc], don't tell me you too..."
    pause
    scene ch8_332 with dissolve
    d "Well, if you need any help I'm here."
    d "And if I'm not here, it means we already left, hehe."
    mc "Thanks, [drelat] [d], I appreciate it."
    mc "..."
    scene ch8_334 with fade
    mc "[a], do you remember where we left the toolbox by any chance?"
    a "Are you going to install it now?"
    mc "Yes, I actually enjoy doing things like this."
    a "That's good."
    scene ch8_336 with dissolve
    a "Do you want me to help you?"
    mc "It's not necessary."
    a "I put the tools in the garage."
    mc "Thanks, I'll go get them."
    mc "Has [drelat] [d] left yet?"
    a "Not yet."
    mc "Are you going with them?"
    scene ch8_335 with dissolve
    a "They said they were going out for a walk, but... I don't feel like it."
    a "Are you going?"
    mc "Nope, I'd rather stay and finish this up."
    scene ch8_336 with dissolve
    mc "By the way, please tell the girls not to turn on the electricity."
    a "Sure thing, don't worry."
    mc "Thanks."
    scene blackscreen with dissolve
    pause
    scene ch8_338 with Dissolve(1.5)
    mc "It wasn't as easy as I thought it would be, but I think I'll finish in another fifteen minutes or so."
    pause
    scene ch8_339 with dissolve
    mc "Phew... It's so hot today, I'm roasting!"
    mc "I'm going to take off my shirt."
    pause
label ch8a4:
    if _in_replay:
        show screen Replayexit
        play music scene2 fadein 1.0
    scene ch8_340 with fade
    pause
    a "..."
    pause
    scene ch8_341 with dissolve
    a "Are you almost done?"
    mc "Oh, hey, [a]. Yeah, I'm almost finished."
    show ch8_342in with dissolve:
        zoom 0.75 
    a "Is it hot today, huh?"
    mc "Yeah, it's too hot."
    show ch8_342in with dissolve:
        subpixel True
        zoom 0.75 xalign 0.5 yalign 0.0
        ease 4 zoom 1.25 yalign 0.1 xalign 0.5
    mc "(Wow, that bra is too tight.)"
    mc "Are you going to do yoga?"
    a "Yes, I want to take advantage of [d]'s absence and do it here."
    a "You know, it's not the same doing it inside without sunlight."
    a "Do you mind?"
    mc "Not at all, I'm almost done."
    a "You can join me if you want when you finish."
    mc "Sure, I will."
    scene ch8_345 with dissolve
    mc "Great, now I have an incentive to finish this quickly."
    a "I'm glad you see doing yoga with me as an incentive."
    mc "I love doing yoga with you."
    scene ch8_343 with dissolve
    a "Then hurry up."
    mc "Okay."
    show ch8_344in with dissolve:
        xalign 0.5 yalign 0.05 zoom 0.75
    a "I can wait for you if you want."
    mc "Yeah, I'm almost done with this."
    show ch8_344in:
        xalign 0.5 yalign 0.05 zoom 0.75
        ease 6 yalign 1.0 zoom 0.875
        ease 3 yalign 0.5 zoom 1.0
    mc "(Those leggings are too sexy.)"
    mc "(They are very thin and perfectly shape her figure, it's like she's not wearing anything...)"
    mc "(I have to hurry up.)"
    pause
    stop music fadeout 2.0
    scene ch8_345 with fade
    pause
    mc "(Done.)"   
    show ch8_347in with dissolve:
        zoom 0.75 xalign 0.5 yalign 0.0
    pause
    show ch8_347in:
        zoom 0.75 xalign 0.5 yalign 0.0
        ease 5 zoom 1.5 yalign 0.4 xalign 0.5
    mc "(It's a bit strange that she wants to do yoga right now.)"
    mc "(And with that sports bra she looks very provocative.)"
    mc "(Wait, have I not seen [k] wear that bra before?)"
    show ch8_346in with dissolve:
        zoom 1.5 xalign 0.5 yalign 0.4    
    a "Are you done?"
    show ch8_346in:
        zoom 1.5 xalign 0.5 yalign 0.4
        ease 0.5 zoom 0.75
    mc "Uh, yeah."
    a "Come on, honey, I'm waiting for you."
    play music sexy1 fadein 2.0
    scene ch8_348 with dissolve
    mc "Okay, I'm here now."
    mc "You have no patience."
    a "I just don't want to start without you."
    mc "So, what's first, stretching?"
    a "That's right, first we're going to do some stretching."
    scene ch8_349 with dissolve
    mc "Hey, [a], a question..."
    mc "Is this sports bra [k]'s?"
    a "...{w=0.5} no."
    mc "Are you sure?"
    a "..."
    a "You caught me."
    a "I was looking for something cool and it was the only thing I found clean in the freshly washed laundry basket."
    mc "I knew it."
    a "Don't tell [k]."
    scene ch8_350 with dissolve
    mc "Don't worry, I won't."
    a "It's a little tight on me..."
    mc "Yeah..."
    a "Does it look bad on me?"
    mc "Not at all, it looks incredible on you."
    mc "A little tight, yes..."
    scene ch8_351 with dissolve
    mc "But what can you do when you have breasts like these..."
    a "[mc]..."
    pause
    a "It's hard for me to find clothes that fit because of these."
    mc "I can imagine..."
    scene ch8_359 with dissolve
    a "They're a real problem."
    a "Sometimes my back hurts and I strongly suspect these two."
    mc "Are they heavy?"
    a "Check for yourself..."
    scene ch8_360 with dissolve
    mc "Hmm... yeah, they're kind of heavy."
    a "Now imagine carrying this all the time."
    mc "It must be a little tough."
    a "It is."
    mc "How can something so beautiful be so problematic?"
    a "*Giggle*, I don't know."
    pause
    scene ch8_352 with dissolve
    a "Enough of talking about my breasts."
    image ch8_354anim:
        "ch8_354" with dissolve
        2.0
        "ch8_353" with dissolve
        2.0
        repeat
    scene ch8_354 with dissolve
    mc "Aww, I liked that conversation topic."
    a "*Giggle*, we'll save it for another time."
    pause
    scene ch8_356 with dissolve
    pause
    scene ch8_358 with dissolve
    a "Oh..."
    mc "Hmm..."
    image ch8_357anim:
        "ch8_357" with dissolve
        1.75
        "ch8_358" with dissolve
        1.75
        repeat
    scene ch8_357anim with dissolve
    mc "Oh..."
    mc "(She's grinding her huge ass against my crotch.)"
    mc "(So delicious.)"
    pause
    scene ch8_355 with dissolve
    a "Let's do some yoga or..."
    mc "This could perfectly be yoga."
    scene ch8_354anim with dissolve
    a "This?"
    a "What would you call this position?"
    mc "Hmm... the loving embrace."
    a "*Giggle*, I like it."
    pause
    scene ch8_361 with dissolve
    a "Okay, enough of weird poses, I want to do real yoga now."
    mc "[a], I know I said I would do yoga with you but I'm terrible at it."
    mc "Can I help you with your routine instead?"
    a "Sure, whatever you want."
    mc "Plus, I enjoy being an assistant more."
    mc "Because I can be close to you... making physical contact..."
    scene ch8_362 with dissolve
    a "Sure, do what you like best."
    a "Well, shall we start?"
    mc "Sure."
    scene ch8_363 with fade
    pause
    scene ch8_365 with dissolve
    a "Hold my leg firmly there."
    scene ch8_364 with fade
    a "Perfect."
    pause
    scene ch8_366 with dissolve
    mc "I remember this was a pose that was difficult for you because of balance."
    a "Yes, hold me up."
    scene ch8_367 with dissolve
    mc "Like this?"
    a "Higher up."
    scene ch8_369 with dissolve
    scene ch8_369 with dissolve
    mc "Higher..."
    pause
    scene ch8_368 with dissolve
    pause
    scene ch8_371 with dissolve
    mc "Like this?"
    a "Yes."
    scene ch8_370 with dissolve
    pause
    a "Perfect, hold me there for a second."
    a "Let go."
    scene ch8_369 with dissolve
    mc "That's it, you got it."
    pause
    scene ch8_372 with dissolve
    a "It's hard to keep the balance."
    mc "Yeah."
    a "Can I tell you a secret?"
    mc "Hm?"
    a "I'm a fraud at this yoga thing."
    mc "What do you mean?"
    a "I have no idea, I try to copy the poses I see on youtube and besides the ''sun salutation'' and one or two others, none of them come out well."
    scene ch8_373 with dissolve
    mc "But you did this one well."
    scene ch8_374 with dissolve
    mc "You just need a little more practice and you'll get it."
    a "Do you think so?"
    scene ch8_375 with dissolve
    mc "Sure I do."
    mc "But you should start with the basics first."
    scene ch8_374 with dissolve
    a "Sweetie, I've been in the basic level for too long and I just can't seem to improve."
    scene ch8_375 with dissolve
    a "I think I need an instructor."
    scene ch8_374 with dissolve
    mc "I can be your instructor."
    a "[mc], you don't know anything about yoga either."
    scene ch8_375 with dissolve
    mc "In a football game, when have you seen the coach play on the field or in boxing, a coach fight in the ring?"
    mc "I just need to see the pose and support you in what you need."
    scene ch8_374 with dissolve
    mc "Besides, the truth is I do have some idea about yoga, I just pretended not to because..."
    mc "I preferred to watch you do it."
    scene ch8_375 with dissolve
    a "Oh, really?"
    a "Show me a simple pose I can do."
    mc "Sure."
    scene ch8_378 with dissolve
    mc "Stand like this and... look forward."
    a "Like this?"
    mc "Perfect."
    mc "(My dick is between her legs...)"
    mc "This one is called.. um.. ''cat bull'' or something like that."
    mc "The name isn't important."
    mc "A-actually, it's for two people."
    scene ch8_379 with dissolve
    a "Really?"
    a "Hmm..."
    a "This pose doesn't sound familiar to me."
    scene ch8_377 with dissolve
    a "But if the instructor says so, I believe him."
    mc "Exactly, just listen to your instructor [mc]."
    a "Okay, what now, instructor?"
    mc "Alright, uhh..."
    pause
    scene ch8_379 with dissolve
    mc "Let's see..."
    scene ch8_380 with dissolve
    mc "I have to put my hands on your waist."
    a "Okay..."
    scene ch8_ayoga_1_pov2_1 with dissolve
    mc "You have lovely hips, ma'am."
    a "T-thanks."
    mc "(Damn, this is too hot, I've never been this close to her vagina before.)"
    mc "(I wonder if she doesn't feel it or if she doesn't care.)"
    mc "(It's impossible for her not to feel it, she's allowing me to do it, she likes it.)"

init python:
    def ch8_ayoga_1_pov1_(trans, st, at):  
        trans.set_child("ch8_ayoga_1_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         

init python:
    def ch8_ayoga_1_pov2_(trans, st, at):  
        trans.set_child("ch8_ayoga_1_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         

init python:
    def ch8_ayoga_1_pov3_(trans, st, at):  
        trans.set_child("ch8_ayoga_1_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         

screen ch8_ayoga_1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_1_pov1_settings") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_ayoga_1_pov2_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_ayoga_1_pov3_settings") style "textbutton_choice"        
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

screen ch8_ayoga_1_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_1_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_ayoga_1_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_ayoga_1_pov3_settings") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"       

screen ch8_ayoga_1_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_1_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_ayoga_1_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_ayoga_1_pov2_settings") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label beforech8_ayoga_1_pov3_:
    image ch8_ayoga_1_pov1_:
        function ch8_ayoga_1_pov1_
    image ch8_ayoga_1_pov2_:
        function ch8_ayoga_1_pov2_
    image ch8_ayoga_1_pov3_:
        function ch8_ayoga_1_pov3_    
    $ anim_speed = 0.05
    scene ch8_ayoga_1_pov3_1 with dissolve
    mc "And now... erm..."
    mc "We stay like this for a while, still."
    pause
    a "This is a bit tiring if I have to stay completely still."
    mc "It'll only be a moment."
    a "Okay."
    pause
    mc "We can move a little if you want..."
    mc "How about if..."
    mc "(Having her like this doggy style is too much for me, I can't resist.)"
    mc "(I hope she doesn't get mad.)"
    pause
    scene ch8_ayoga_1_pov3_ with dissolve
    a "Oh..."
    pause
    mc "(She's moving too!)"
    mc "(And in a very sexy way...)"
    mc "(Wow...)"
    pause
    a "[mc]?"
    mc "Yes?"
    a "..."
    mc "Is something wrong?"
    pause
    scene ch8_ayoga_1_pov1_ with dissolve
    a "Um... I suppose this is also part of the pose."
    mc "Of course."
    a "This pose is a bit... 'different'."
    mc "I invented it, it's a combination of other poses."
    a "Ah, I see."
    a "And what are those poses?"
    mc "Er... {w=0.4} ones I learned."
    a "Can you tell me which ones or do you not remember them?"
    mc "Are you trying to say I don't know what I'm doing?"
    a "No, not at all. *laughter*"
    a "I'm going to trust my instructor and his yoga innovations."
    mc "Thank you."
    pause
    scene ch8_ayoga_1_pov2_ with dissolve
    mc "How about it, do you feel how your body relaxes?"
    a "I wouldn't say it 'relaxes' me."
    mc "Any effect is a sign that the pose is being done correctly."
    mc "(Such sensual hip movements, god...)"
    mc "(What a temptation, I'd love to take my penis out of my shorts and just fuck her right here, I don't care if the neighbors see us.)"
    pause
    a "Instructor [mc], am I doing it right?"
    mc "(She wants me to rate her hips movements.)"
    mc "You're doing it perfect."
    a "Oh, thank you."


label ch8_ayoga_1_pov1_settings:
    scene ch8_ayoga_1_pov1_ with dissolve
    call screen ch8_ayoga_1_pov1_settings with dissolve

label ch8_ayoga_1_pov2_settings:
    scene ch8_ayoga_1_pov2_ with dissolve
    call screen ch8_ayoga_1_pov2_settings with dissolve

label ch8_ayoga_1_pov3_settings:
    scene ch8_ayoga_1_pov3_ with dissolve
    call screen ch8_ayoga_1_pov3_settings with dissolve

label afterch8_ayoga_1_pov1_settings:
    mc "(God, the neighbors could see us.)"
    mc "(It's weird that she doesn't mind.)"
    mc "(Maybe she's enjoying it so much she can't think about that.)"
    scene ch8_382 with dissolve
    mc "(I can't take it anymore.)"
    pause
    scene ch8_383 with dissolve
    a "..."
    mc "(Much better.)"
    pause
    scene ch8_384 with dissolve
    a "Are we done with the pose yet?"
    a "Can I suggest one now?"
    mc "Sure."
    scene ch8_385 with dissolve
    a "This is one of the few poses I do well."
    mc "(Shit, my penis is exposed.)"
    scene ch8_388 with dissolve
    a "But it's a normal pose."
    a "I trust that you can adapt it for two people."
    mc "Of course, in yoga there are no strict rules, poses can always be modified for greater comfort or enjoyment of the person."
    scene ch8_387 with dissolve
    a "I didn't expect you to know so much about yoga, [mc]."
    mc "Neither did I."
    a "*Laughter*"
    pause
    scene ch8_389 with dissolve
    mc "You have beautiful hips."
    a "Thank you, but you already said that before."
    mc "Oh, did I?"
    a "*Giggle* Yes, you said it a moment ago."
    mc "Sorry, I forgot."
    pause
    scene ch8_389- with dissolve
    mc "It's just... I'm amazed at how beautiful...{w=0.4} your hips are."
    a "They're stay-at-home mom hips with two kids."
    mc "Well, they're perfect."
    pause
    scene ch8_390 with dissolve
    a "Do you really think so?"
    mc "Of course."
    mc "Only a mother could have 'hips' like these."
    pause
    scene ch8_391 with dissolve
    a "*Sigh* I-instructor?"
    mc "(What a delicious ass.)"
    pause
    image ch8_393anim:
        "ch8_392" with dissolve
        1.75
        "ch8_389-" with dissolve
        1.75
        "ch8_390" with dissolve
        1.75
        repeat
    scene ch8_393anim with dissolve
    a "Anyone could think that after two children one becomes less attractive."
    a "I'm glad there are people who find beauty in women like us."
    mc "I don't find beauty in women LIKE you, I find beauty in YOU."
    a "You just boosted my self-esteem like you have no idea."
    pause
    scene ch8_393 with dissolve
    mc "(She didn't mind when I put my penis between her legs earlier...)"
    pause
    scene ch8_ayoga_2_pov3_14 with dissolve
    pause
    mc "(Look how my cock wraps around her ass... God.)"
    a "I see you were able to adapt the pose well."
    a "Before we were joking, but you're really a good instructor, [mc]."
    mc "I'm trying."

init python:
    def ch8_ayoga_2_pov1_(trans, st, at):  
        trans.set_child("ch8_ayoga_2_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value     

init python:
    def ch8_ayoga_2_pov2_(trans, st, at):  
        trans.set_child("ch8_ayoga_2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value


init python:
    def ch8_ayoga_2_pov3_(trans, st, at):  
        trans.set_child("ch8_ayoga_2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value           

init python:
    def ch8_ayoga_2_pov4_(trans, st, at):  
        trans.set_child("ch8_ayoga_2_pov4_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

init python:
    def ch8_ayoga_2_pov5_(trans, st, at):  
        trans.set_child("ch8_ayoga_2_pov5_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   







screen ch8_ayoga_2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_2_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch8_ayoga_2_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch8_ayoga_2_pov3_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch8_ayoga_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch8_ayoga_2_pov5_") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      

screen ch8_ayoga_2_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_2_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_ayoga_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch8_ayoga_2_pov3_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch8_ayoga_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch8_ayoga_2_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      

screen ch8_ayoga_2_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_2_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_ayoga_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch8_ayoga_2_pov2_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch8_ayoga_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch8_ayoga_2_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      

screen ch8_ayoga_2_pov4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_2_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_ayoga_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch8_ayoga_2_pov2_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch8_ayoga_2_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch8_ayoga_2_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      

screen ch8_ayoga_2_pov5_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_ayoga_2_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_ayoga_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch8_ayoga_2_pov2_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch8_ayoga_2_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch8_ayoga_2_pov4_") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      


label beforech8_ayoga_2_pov3_:
    image ch8_ayoga_2_pov1_:
        function ch8_ayoga_2_pov1_
    image ch8_ayoga_2_pov2_:
        function ch8_ayoga_2_pov2_
    image ch8_ayoga_2_pov3_:
        function ch8_ayoga_2_pov3_
    image ch8_ayoga_2_pov4_:
        function ch8_ayoga_2_pov4_
    image ch8_ayoga_2_pov5_:
        function ch8_ayoga_2_pov5_
    $ anim_speed = 0.05
    scene ch8_ayoga_2_pov3_ with dissolve
    a "Um..."
    a "..."
    pause
    a "Maybe you don't really know the basics of yoga or anything like that, but..."
    a "Uhm... At the end of the day, it's about enjoying yourself and feeling good."
    mc "And if it feels good?"
    a "Exactly, that's what I mean."
    mc "DOES THIS feel good?"
    a "Yes..."
    pause
    scene ch8_ayoga_2_pov1_ with dissolve
    "*crack*"
    mc "Was that your back?"
    a "Yes, uh..."
    a "I think this is helping my spine."
    pause
    scene ch8_ayoga_2_pov2_ with dissolve
    mc "(I must be dreaming.)"
    mc "(This is better than any fantasy I've ever had.)"
    mc "(How could someone change so much overnight?)"
    mc "(I guess after the titjob she gave me last night, this is nothing.)"
    pause
    scene ch8_ayoga_2_pov5_ with dissolve
    a "Do we change poses or...?"
    pause
    mc "Just a little longer."
    a "*Giggle*, I figured."
    pause
    mc "What do you mean you figured?"
    a "I just figured it out."
    mc "Hmm..."
    a "I assumed you were enjoying doing this pose, am I wrong?"
    mc "No, you're right."
    mc "I'm enjoying it... A LOT."
    pause
    jump ch8_ayoga_2_pov3_

label ch8_ayoga_2_pov1_:
    scene ch8_ayoga_2_pov1_ with dissolve
    call screen ch8_ayoga_2_pov1_settings with dissolve

label ch8_ayoga_2_pov2_:
    scene ch8_ayoga_2_pov2_ with dissolve
    call screen ch8_ayoga_2_pov2_settings with dissolve

label ch8_ayoga_2_pov3_:
    scene ch8_ayoga_2_pov3_ with dissolve
    call screen ch8_ayoga_2_pov3_settings with dissolve

label ch8_ayoga_2_pov4_:
    scene ch8_ayoga_2_pov4_ with dissolve
    call screen ch8_ayoga_2_pov4_settings with dissolve

label ch8_ayoga_2_pov5_:
    scene ch8_ayoga_2_pov5_ with dissolve
    call screen ch8_ayoga_2_pov5_settings with dissolve

    scene ch8_ayoga_2_pov4_ with dissolve
    mc "(She knows I'm rubbing my dick on her fat and juicy ass, and she enjoys it.)"
    mc "(She loves to seduce me...)"
    mc "(Feeling desired drives her crazy.)"
    mc "(And that makes me want her even more... it's a vicious circle.)"
    pause

label afterch8_ayoga_2_pov4_:
    a "I think we've had enough of this pose."
    scene ch8_395 with dissolve
    mc "Uh..."
    scene ch8_397 with dissolve
    a "What is it, [mc]...?"
    a "Oh, god... [mc]..."
    a "I didn't know you had it out."
    mc "..."
    a "And, erm... I didn't know that... uh..."
    pause
    scene ch8_396 with dissolve
    a "..."
    mc "..."
    pause
    a "What are we doing?"
    a "C-cover yourself, [mc]."
    pause
    scene ch8_396- with hpunch
    stop music fadeout 3.0
    a "A neighbor could see you, cover yourself now! Don't you have any shame?!"
    pause
    scene ch8_399 with dissolve
    mc "..."
    a "That was... I have no words to describe it."
    pause
    scene ch8_400 with dissolve
    a "Uhm..."
    a "..."
    pause
    scene ch8_401 with dissolve
    a "Erm..."
    a "I didn't like that at all."
    a "And I don't want you to do it again, got it?"
    mc "I'm sorry, I thought... {w=0.4} Yeah, I got it."
    a "L-let's just go inside."
    mc "(I'm an idiot...)"
    mc "(It's obvious she won't like it if we do it outdoors in front of everyone.)"
    mc "(Once again, I screwed up...)"
    a "Let's go inside, [mc]."
    mc "Yeah."
    scene ch8_402 with dissolve
    mc "Sorry, [a], that was really stupid of me."
    a "I-it's okay... let's just forget about it."
    mc "Yeah..."
    mc "I didn't want to ruin the yoga."
    scene ch8_403 with dissolve
    a "Let's just forget about it, [mc]."
    mc "Yeah, it's just that I don't like to make you uncomfortable or angry."
    mc "Seriously, I'm sorry, I crossed the line."
    a "I'm not angry, honey."
    a "And maybe you did cross the line but... well... it doesn't matter."
    mc "Okay..."
    mc "So... I'm gonna go to my room."
    scene ch8_404 with dissolve
    a "You're leaving?"
    a "I-if you want to go, it's fine."
    mc "I thought it would be better if I left but..."
    a "..."
    pause
    play music sexy3 fadein 2.0 
    scene ch8_405 with dissolve
    a "I was thinking of continue here, in the room."
    a "But if you're tired or bored and want to leave, that's okay."
    mc "N-no."
    a "..."
    scene ch8_406 with dissolve
    mc "Of course I want to continue, [a]."
    scene ch8_407 with dissolve
    mc "But... continue with what?"
    a "..."
    mc "What do you mean by continue?"
    a "..."
    pause
    scene ch8_408- with dissolve
    a "I'm sorry for yelling at you outside."
    a "I shouldn't have done that."
    mc "I deserved it, what I did was really stupid."
    a "I'm glad you understand."
    scene ch8_408 with dissolve
    a "..."
    a "And... did it come out on its own or...?"
    mc "S-something like that."
    mc "It was really tight in my underwear and it just came out."
    a "I see..."
    a "Something that big must be hard to hide."
    mc "It is, but only when it's erect."
    scene ch8_409 with dissolve
    a "And... can I know what caused your erection?"
    mc "You mean which part of you caused it?"
    scene ch8_410 with dissolve
    a "I understand that it was me who got you like this..."
    mc "Obviously it was you [a]."
    mc "When you posed like that, you looked so sexy..."
    mc "And when we were doing that pose and our bodies were rubbing against each other, it was just too much."
    mc "By that point, I couldn't control myself anymore."
    scene ch8_411 with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    mc "And my instincts took over."
    a "*Hmnch, smnch*"
    pause
    stop sound fadeout 0.5
    scene ch8_412 with dissolve
    mc "Look, [a]."
    a "Oh..."
    mc "Look how big and hard I get because of you."
    scene ch8_413 with dissolve
    a "So big... and hard..."
    mc "Only you can make me this hard, [a]."
    a "..."
    pause
    scene ch8_414 with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop
    pause
    a "I can't believe we're doing this, [mc]."
    mc "Let's just go with the flow."
    pause
    scene ch8_415 with dissolve
    a "*Hmnch, smlmh*{w=0.4}, Remember the limits."
    mc "I know."
    pause
    stop sound fadeout 0.5
    scene ch8_416 with dissolve
    mc "Hmm, you have beautiful boobs."
    pause
    scene ch8_417 with dissolve
    a "Uhm..."
    image ch8_417anim:
        "ch8_416" with dissolve
        1.75
        "ch8_417" with dissolve
        1.75
        repeat
    scene ch8_417anim with dissolve
    mc "Hmm, so delicious..."
    a "Don't suck too hard, honey. My boobs are sensitive."
    a "*Uh..*"
    pause
    scene ch8_418 with dissolve
    pause
    scene ch8_419 with dissolve
    pause
    scene ch8_420 with dissolve
    a "*Uhh..*"
    mc "Do you like it when I suck your boobs, [a]?"
    a "Don't ask me those questions, [mc]."
    a "I'm still your [arelat]."
    scene ch8_421 with dissolve
    mc "I know, I just want you to enjoy this too."
    mc "I love your waist..."
    scene ch8_422 with dissolve
    mc "Hmm.."
    mc "The curve of your hips..."
    scene ch8_423 with dissolve
    mc "Your legs drive me crazy..."
    mc "But my favorite part..."
    scene ch8_424 with dissolve
    mc "Is your ass..."
    a "[mc]..."
    pause
    scene ch8_424--- with dissolve
    mc "Hmm, god..."
    a "Don't put your hand there, [mc]."
    pause
    scene ch8_425 with dissolve
    a "No, honey..."
    mc "God, I lose control when I see you like this."
    a "Try to control yourself."
    mc "It's hard."
    pause
    a "And..."
    a "What do you like the most?"
    mc "About what?"
    a "Well..."
    a "I don't have a firm or toned butt."
    a "What do you like about me?"
    mc "That's exactly what I like, [a]."
    mc "I love it when you walk and your butt wiggles from side to side."
    mc "And when you bend over, it has the perfect shape."
    mc "You have a big butt with that delicious touch of softness that drives me crazy."
    a "Wow..."
    a "I guess everyone has their own concept of beauty."
    scene ch8_428 with dissolve
    a "Ah!"
    pause
    image ch8_428anim:
        "ch8_429" with dissolve 
        1.75
        "ch8_428" with dissolve
        1.75
        repeat
    scene ch8_428anim with dissolve
    a "[mc], no, baby."
    mc "Hmm..."
    mc "[a], putting my face between your cheeks has been my dream forever."
    mc "Can I do it just this once?"
    a "..."
    pause
    scene ch8_427 with dissolve
    a "Just that, don't try anything else."
    mc "Yes, just that."
    pause 
    mc "Didn't [drelat] [d] used to tell you how attractive and sexy you are?"
    a "It's been a long time since he used to..."
    a "A long time and many pounds ago. *giggle*"
    a "I think he stopped liking me when I gained weight."
    a "When my second pregnancy came, everything went downhill."
    pause
    image ch8_430anim:
        "ch8_430" with dissolve
        1.75
        "ch8_431" with dissolve 
        1.75
        repeat
    scene ch8_430anim with dissolve
    mc "(Her scent...)"
    mc "(She smells exquisite) *Sniff*"
    mc "Hmm..."
    a "[mc], that's enough, honey."
    pause
    scene ch8_a_yoga_pov1_15 with dissolve
    mc "Who in their right mind wouldn't want a wife fractionally as sexy as you?"
    mc "If I were [drelat] [d], I would make you mine every day."
    a "[mc]..." 
    a "Don't say those things, I'm your [arelat]."
    mc "You say that as if someone could hear us."
    mc "It's just you and me, [a]."
    mc "We can be honest."
    pause
    a "It's not about whether someone can hear us or not."
    a "You're my [arelatmc], [mc]. Hearing you talk to me like that gives me goosebumps."
    mc "Sorry, I thought you liked it."
    a "I like it when you compliment me."
    a "But I couldn't get used to hearing you talk to me in that tone."
    mc "I understand."
    a "You have to remember the boundaries."
    mc "Yeah..."
    pause
    scene ch8_432-in with dissolve
    pause
    scene ch8_432--in with dissolve
    a "[mc]..."
    mc "Hmm..."
    pause
    scene ch8_432---in with dissolve
    a "W-what are you doing, honey?"
    mc "You have legs that are too sexy, it makes me want to..."
    pause

init python:
    store.last_played_sound2 = None
    def ch8_a_yoga_pov1_(trans, st, at):  
        trans.set_child("ch8_a_yoga_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked2.ogg", "audio/sex/fuck_naked1.ogg", "audio/sex/fuck_naked6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    store.last_played_sound2 = None
    def ch8_a_yoga_pov2_(trans, st, at):  
        trans.set_child("ch8_a_yoga_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked2.ogg", "audio/sex/fuck_naked1.ogg", "audio/sex/fuck_naked6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

init python:
    store.last_played_sound2 = None
    def ch8_a_yoga_pov3_(trans, st, at):  
        trans.set_child("ch8_a_yoga_pov3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked2.ogg", "audio/sex/fuck_naked1.ogg", "audio/sex/fuck_naked6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

init python:
    store.last_played_sound2 = None
    def ch8_a_yoga_pov4_(trans, st, at):  
        trans.set_child("ch8_a_yoga_pov4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 30:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked2.ogg", "audio/sex/fuck_naked1.ogg", "audio/sex/fuck_naked6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

screen ch8_a_yoga_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"     
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"        
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_a_yoga_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_a_yoga_pov2_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_a_yoga_pov3_settings") style "textbutton_choice"     
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_a_yoga_pov4_settings") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_a_yoga_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"      
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"       
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_a_yoga_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_a_yoga_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_a_yoga_pov3_settings") style "textbutton_choice"     
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_a_yoga_pov4_settings") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_a_yoga_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"   
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_a_yoga_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_a_yoga_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_a_yoga_pov2_settings") style "textbutton_choice"     
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_a_yoga_pov4_settings") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_a_yoga_pov4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_a_yoga_pov1_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_a_yoga_pov1_settings") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_a_yoga_pov2_settings") style "textbutton_choice"     
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_a_yoga_pov3_settings") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"


label beforech8_a_yoga_pov:
    image ch8_a_yoga_pov1_:
        function ch8_a_yoga_pov1_
    image ch8_a_yoga_pov2_:
        function ch8_a_yoga_pov2_
    image ch8_a_yoga_pov3_:
        function ch8_a_yoga_pov3_
    image ch8_a_yoga_pov4_:
        function ch8_a_yoga_pov4_
    $ anim_speed = 0.035
    scene ch8_a_yoga_pov1_ with dissolve
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.5
    a "Uh..."
    a "[mc], c-calm down..."
    mc "I can't, [a]."
    mc "You're too hot."
    a "Oh... god."
    pause
    $ anim_speed = 0.015
    mc "Oh, yes..."
    a "*Huh, uh, hmm*"
    a "Baby, calm down."
    mc "Uh, this feels so good, hmm..."
    pause
    a "D-does this feel good?"
    mc "It feels really good, [a]..."
    mc "I'm just rubbing between your legs and it feels incredible."
    mc "Hmmm... I love it..."
    mc "The sensation of your legs squeezing my penis is almost like we're-"
    a "-Don't say it."
    pause
    mc "[a], can you squeeze a little more?"
    a "Squeeze a little?"
    mc "Yes, with your legs."
    a "Uhm.. alright..."
    a "Like this?"
    mc "Yeah, just like that."
    scene ch8_a_yoga_pov2_ with dissolve
    a "Oh, [mc]..."
    a "You're being a little rough."
    mc "Hmm, this feels so good."
    pause
    scene ch8_a_yoga_pov4_ with dissolve
    mc "Oh, [arelat] [a], I love this."
    a "I'm glad..."
    mc "Can we do this again another day?"
    a "I don't know..."
    a "We have to be careful, [mc]."
    mc "Obviously in a safe place without the risk of being caught."
    a "In that case..."
    a "Maybe we can..."
    mc "Thank you, [a]."
    a "..."
    pause
    scene ch8_a_yoga_pov3_ with dissolve
    pause
    mc "Can I cum on your legs?"
    a "Yes..."
    mc "Oh, yes..."
    a "Are you close?"
    mc "Almost there."
    pause
    jump ch8_a_yoga_pov1_settings

label ch8_a_yoga_pov1_settings:
    scene ch8_a_yoga_pov1_ with dissolve
    call screen ch8_a_yoga_pov1_settings with dissolve

label ch8_a_yoga_pov2_settings:
    scene ch8_a_yoga_pov2_ with dissolve
    call screen ch8_a_yoga_pov2_settings with dissolve

label ch8_a_yoga_pov3_settings:
    scene ch8_a_yoga_pov3_ with dissolve
    call screen ch8_a_yoga_pov3_settings with dissolve

label ch8_a_yoga_pov4_settings:
    scene ch8_a_yoga_pov4_ with dissolve
    call screen ch8_a_yoga_pov4_settings with dissolve

label afterch8_a_yoga_pov1_settings:
    $ anim_speed = 0.01
    mc "Hmm, this feels good.."
    a "*Uh, uh, uh*"
    a "Are you about to finish, baby?"
    mc "Yeah, almost there..."
    a "*Uh.. hmm..*"
    pause
    mc "Do you like it when it rubs against your vagina?"
    a "Don't ask me that, [mc]."
    mc "I just want to know."
    mc "From the sounds you're making, I'd say yes."
    a "..."
    a "I'm not a robot, [mc]."
    a "Obviously, I feel things."
    a "B-but I already told you not to talk to me like that, I don't like such sexual conversations."
    mc "I-I want both of us to have a good time."
    $ anim_speed = 0.011
    pause 0.5
    $ anim_speed = 0.015
    pause 0.5
    $ anim_speed = 0.025
    pause 0.5
    $ anim_speed = 0.035
    a "Are you done yet?"
    mc "N-no..."
    scene ch8_435 with dissolve
    pause
    mc "I just want to make sure you enjoy it too."
    a "No, [mc]."
    pause
    scene ch8_436 with dissolve
    a "[mc]..."
    image ch8_437anim:
        "ch8_437" with Dissolve(0.5)
        1.0
        "ch8_436" with Dissolve(0.5)
        1.0
        repeat
    scene ch8_437anim with dissolve
    mc "(She's so hot...)"
    mc "(And wet... seems like she was enjoying it after all.)"
    a "No, baby."
    a "This is going too far, honey."
    mc "[a], just enjoy it."
    mc "We'll forget about this anyway."
    a "But... *Ah, hmm*"
    a "Oh, God *Uhh.. hmmm*"
    a "This is{w=0.4}, *Hmm*{w=0.4}, too inappropriate, [mc]."
    pause
    scene ch8_438 with dissolve
    a "That's enough, [mc]."
    a "Now let me make you feel good."
    stop voicefx fadeout 0.5
    scene ch8_439 with dissolve
    a "*Ahlmm, mnch*"
    pause
    scene ch8_440 with dissolve
    a "*Hmmnch*"
    pause
    scene ch8_441 with vpunch
    a "Ow! Sorry..."
    mc "What's wrong, [arelat] [a]?"
    mc "Didn't you like it?"
    a "It's not that..."
    a "You crossed the line."
    a "Y-you can't touch me like that, [mc]."
    scene ch8_442 with dissolve
    mc "But you've touched me before."
    mc "I thought it was only fair if I did it too."
    a "..."
    pause
    scene ch8_443 with dissolve
    a "Baby, we can't go that far."
    mc "I'm tired of all these limits and rules, [arelat] [a]."
    a "It's either that or nothing, [mc]."
    mc "..."
    pause
    scene ch8_444 with dissolve
    pause
    scene ch8_445 with dissolve
    a "You'll have to settle for this, honey."
    a "If you want this to work, you have to follow the rules."
    pause
    mc "Okay..."
    a "Remember, we're still [arelat] and [arelatmc]."
    mc "Yeah."
    a "Did we not finish something yesterday?"
    a "Do you want me to use my breasts like yesterday?"
    mc "Yes, I'd love that."
    a "Okay."
    pause
    scene ch8_446 with dissolve
    pause
    scene ch8_447 with dissolve

    pause
    $ anim_speed = 0.05
    scene ch8_a_titjob1_pov1_ with dissolve
    mc "Oh, yeah..."
    a "Enjoy it, baby."
    a "This time you have to cum or I'll feel bad."
    mc "Yeah... ah..."
    a "Do you want me to do it faster, slower? You tell me."
    mc "A little faster, [a]."
    $ anim_speed = 0.045
    pause 0.5
    $ anim_speed = 0.040
    pause 0.5
    $ anim_speed = 0.035
    a "Like this?"
    mc "Yeah, just like that."
    pause
    a "We had to stop almost when you were about to finish yesterday."
    mc "It was painful."
    a "Oh, my poor baby."
    a "But this time I'll make sure you cum."
    a "So enjoy it as much as you can and cum quickly, I don't want us to be interrupted again."
    mc "Yeah... I definitely will..."
    mc "God, [a]..."
    mc "*Hah.. hngh*"
    a "That's it, honey, cum now."
    a "Come on these breasts that you love so much."
    mc "I love this new version of you, [a]."
    mc "I never thought I'd hear you say those words to me."
    a "Shhh..."
    pause
    a "Things change."
    a "It's just that... you're so good to me and give me all the attention I need..."
    a "How could a [arelat] not spoil a [arelatmc] like you?"
    mc "Oh, [a]... *Hngh!* I love you so much!"
    mc "Faster, [a]."
    $ anim_speed = 0.03
    pause 0.5
    $ anim_speed = 0.025
    pause 0.5
    $ anim_speed = 0.02
    pause 0.5
    $ anim_speed = 0.015
    a "I love you too, baby."
    a "My favorite [arelatmc]..."
    a "That's it, honey."
    a "Come on my breasts, the ones you love so much."
    menu:
        "Cum on her tits":
            jump afterchoicech8_446
        "Cum between her legs":
            jump ch8_400thight_cumm
        "[JGR]Mod: Cum on Both":
            jump jokerbothcumchoices

label afterchoicech8_446:
    $ anim_speed = 0.014
    pause 0.5
    $ anim_speed = 0.013
    pause 0.5
    $ anim_speed = 0.012
    pause 0.5
    $ anim_speed = 0.011
    pause 0.5
    $ anim_speed = 0.01
    mc "*hngh!*, fuck, so sexy!"
    mc "Ah, a-ah, [a]..."
    a "Do it, baby."
    pause
    mc "*Hmnh*, *ah, hmmm!*"
    scene ch8_452-in with cumming
    with flash
    mc "*Nghh!*"
    pause
    scene ch8_452--in with dissolve
    mc "*Hahh...*"
    pause
    scene ch8_452---in with dissolve
    a "Wow, [mc]..."
    a "You let out so much..."
    pause
    scene ch8_452----in with dissolve
    a "Look at this mess, *giggle*."
    a "How am I going to clean all of this?"
    pause
    scene ch8_452---in with dissolve
    a "Oh my god..."
    a "..."
    pause
    mc "Uhh... should I bring some tissue?"
    scene ch8_452----in with dissolve
    a "If it's not too much trouble."
    a "I don't want to spill it on the carpet."
    mc "Uff... I'll be right back."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    jump ch8_455label

screen ch8_a_titjob1_pov1_settings2():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"            
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterlabelch8_a_titjob1_pov") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("c8at1p1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("c8at1p1_") style "textbutton_choice"      
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

    
label ch8_400thight_cumm:
    mc "Wait, [a]."
    mc "I want to cum between your legs."
    a "Okay."
    pause
    $ anim_speed = 0.015
    scene ch8_a_yoga_pov1_ with fade
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.5
    mc "*Hngh!*, damn, so sexy!"
    mc "Ah, a-ah, [a]..."
    a "Are you close, sweetie?"
    mc "Yeah, *Hngh!*"
    $ anim_speed = 0.014
    pause 0.5
    $ anim_speed = 0.013
    pause 0.5
    $ anim_speed = 0.012
    pause 0.5
    $ anim_speed = 0.011
    pause 0.5
    $ anim_speed = 0.007
    a "That's it, cum baby."
    a "Come on my legs."
    mc "*Hmnnghh!*, *ah, argh!*"
    scene ch8_451 with cumming
    with flash
    stop voicefx fadeout 0.5
    mc "*Hmngh!*, Uuff..."
    a "Oh... so much cum..."
    mc "Uff... that was good..."
    scene ch8_452 with dissolve
    mc "Hmh!"
    a "*Hmnch, hmhmm*"
    pause
    stop music fadeout 5.0
    scene blackscreen with Dissolve(2.0)
    pause
    jump ch8_455label

label jokerbothcumchoices:
    $ anim_speed = 0.014
    pause 0.5
    $ anim_speed = 0.013
    pause 0.5
    $ anim_speed = 0.012
    pause 0.5
    $ anim_speed = 0.011
    pause 0.5
    $ anim_speed = 0.01
    mc "*hngh!*, fuck, so sexy!"
    mc "Ah, a-ah, [a]..."
    a "Shhh, just focus on coming, baby."
    pause
    mc "*Hmnh*, *ah, hmmm!*"
    scene ch8_452-in with cumming
    with flash
    mc "*Nghh!*"
    pause
    scene ch8_452--in with dissolve
    mc "*Hahh...*"
    pause
    scene ch8_452---in with dissolve
    a "Wow, [mc]..."
    a "You let out so much..."
    pause
    scene ch8_452----in with dissolve
    a "Look at this mess, *giggle*."
    a "How am I going to clean all of this?"
    pause
    scene ch8_452---in with dissolve
    a "Oh my god..."
    a "..."
    pause
    mc "Uhh... should I bring some tissue?"
    scene ch8_452----in with dissolve
    a "If it's not too much trouble."
    a "I don't want to spill it on the carpet."
    mc "Uff... I'll be right back."
    scene blackscreen with dissolve

    mc "Wait, [a]."
    mc "I want to cum between your legs."
    a "Okay."
    pause
    $ anim_speed = 0.015
    scene ch8_a_yoga_pov1_ with fade
    mc "*Hngh!*, damn, so sexy!"
    mc "Ah, a-ah, [a]..."
    a "Are you close, [mc]?"
    mc "Yeah, *Hngh!*"
    $ anim_speed = 0.014
    pause 0.5
    $ anim_speed = 0.013
    pause 0.5
    $ anim_speed = 0.012
    pause 0.5
    $ anim_speed = 0.011
    pause 0.5
    $ anim_speed = 0.01
    a "That's it, cum baby."
    a "Come on my legs."
    mc "*Hmnnghh!*, *ah, argh!*"
    scene ch8_451 with cumming
    with flash
    mc "*Hmngh!*, Uuff..."
    a "Oh... so much cum..."
    mc "Uff... that was good..."
    pause
    scene ch8_452 with dissolve
    a "Are you satisfied now, baby?"
    mc "For the moment, yes."
    pause
    scene blackscreen with dissolve
    pause
    jump ch8_455label

label ch8_455label:
    $ renpy.end_replay()
    scene ch8_454 with dissolve
    a "What we just did..."
    mc "I know, not a word."
    a "..."
    a "N-no, I don't mean that..."
    pause
    scene ch8_456 with dissolve
    a "Do you want to shower first or me?"
    mc "Shower?"
    scene ch8_455 with dissolve
    a "We just did yoga and, we sweat a lot..."
    a "And you still don't plan to shower?"
    mc "But I showered in the morning."
    scene ch8_458 with dissolve
    a "I'll go shower and then you can do it."
    mc "Is that an order?"
    a "It's a mandatory suggestion."
    pause
    scene ch8_459 with dissolve
    mc "(What a way to walk... who knows when I'll see her in underwear again.)"
    mc "What a beauty."
    pause
    scene ch8_460 with dissolve
    a "Did you say something?"
    mc "I was thinking out loud."
    a "Did I hear you say 'what a beauty'?"
    mc "Ah, yes. I was admiring your walking in my mind."
    scene ch8_461 with dissolve
    a "Thank you, tell that to your mind."
    mc "You're welcome."
    pause
    scene ch8_462 with dissolve
    a "Do you want to go to the patio later?"
    a "It's so hot inside the house."
    mc "Sure."
    a "And you're going to shower, you heard me?"
    mc "Yes, [arelat] [a]."
    a "*Giggle*"
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 1.5
    scene ch8_462-in with dissolve
    pause
    a "*Laughter*"
    a "No, I'm at home."
    a "My [arelatmc] and I renovated the backyard, do you want to see?"
    "Oh... it looks nice."
    mc "(I think she's video calling someone.)"
    a "Hey, how's that going? Did everything turn out okay?"
    "Yeah, look."
    a "Wow."
    a "Are you recovered yet?"
    "Not completely, I think I'll heal in one or two weeks."
    "[a], how about that toy I recommended to you?"
    "Much better than a man, right?"
    scene ch8_462--in with dissolve
    a "[lauren]!"
    lauren "What?"
    a "You're on speaker!"
    lauren "Oh, [a], it's normal. Everyone masturbates, even your daughters, don't act like saints."
    a "[lauren]!"
    scene ch8_462---in with dissolve
    mc "(Shit!)"
    scene ch8_462----in with hpunch
    pause
    a "You're lucky they're not home today."
    "Unintelligible."
    a "My [arelatmc] is with me."
    a "Yes, he stayed to keep me company."
    "Unintelligible."
    a "Yes, I tried it."
    a "I'll just say that you were right, *giggle*."
    a "But I thought it would calm me down, you know... {i}the cravings{/i}{w=0.4}{i} for sex{/i}{w=0.4}."
    a "{i}I feel like a pre-university student.{/i} *Laughter*"
    a "Oh no! Hahaha."
    mc "(I think they're talking about some kind of sex toy.)"
    mc "(I never imagined that [a] would use those things.)"
    a "Take care, kisses."
    a "Bye." 
    pause
    scene ch8_462----- with fade
    mc  "It's nice and cool here."
    a "Yes, the weather here is very pleasant."
    a  "You showered, right?"
    mc  "Yes, [a]."
    a  "*Laughs*"
    scene ch8_464 with dissolve
    a  "You're wearing the same clothes again."
    mc  "It's not dirty, I just put it on this morning."
    a  "Hmm... did you take a shower, you're not lying to me, right?"
    mc  "I did shower."
    a  "..."
    mc  "What?"
    a  "*Laughs*"
    a  "I'm just kidding, I know you showered. I can smell my conditioner from here."
    scene ch8_467 with dissolve
    pause
    a  "It's so beautiful."
    mc  "And to think I didn't even take a shower."
    a  "*Giggles*, I'm talking about the patio, silly."
    a  "You did a great job too."
    a  "And you learned all this in just one afternoon."
    mc  "YouTube has everything described in detail."
    a  "You're being modest."
    scene ch8_466 with dissolve
    a  "Have you ever thought about pursuing a trade like this?"
    a  "You're good at these things."
    mc  "No, never."
    mc  "To learn these things well, you need someone to teach you."
    mc  "I don't know anyone."
    a  "You could work as an assistant bricklayer, that's how everyone starts."
    mc  "Yes, that's a good idea. You learn while making money."
    scene ch8_468 with dissolve
    pause
    a  "The house is so peaceful when it's just you and me."
    mc  "Yes."
    mc  "There's so much peace."
    a  "Yes."
    pause
    a  "What's next? What's the next goal?"
    pause
    scene ch8_465 with dissolve
    a  "Do we remodel the kitchen?"
    mc  "Do you want to replace the furniture?"
    a  "Not just the furniture, I want to rearrange everything."
    mc  "Even the sink?"
    a  "Yes."
    a  "Or do you feel incapable?"
    mc  "No, of course not."
    mc  "It shouldn't be too difficult."
    scene ch8_483 with dissolve
    mc  "Anything for my spoiled [arelat]."
    a  "*Giggles*"
    a  "Speaking of the kitchen, you still have the food wildcard."
    mc  "That's right."
    scene ch8_484 with dissolve
    a  "-No asking for kisses."
    mc  "Aww..."
    a  "Because they're free."
    mc  "Yay!"
    a  "But they're all gone."
    mc  "Aww..."
    a  "*Laughs*"
    a  "Ask for something to eat."
    mc  "What's on the menu?"
    a  "You can choose between chicken with vegetables, hmm... spaghetti, meatballs or we can also order takeout."
    scene ch8_485 with dissolve
    mc  "I'm craving some juicy and delicious legs... {w=0.4} hmmm..."
    mc  "-Of chicken."
    a  "[mc]!"
    scene ch8_486 with dissolve
    a  "Are you saying I have chicken legs? *Giggles*"
    mc  "Juicy and delicious ones."
    a  "*Laughs*, stop it, [mc]."
    pause
    scene ch8_487 with dissolve
    a  "Do you know what I'm craving?"
    mc  "*Laughs*, what?"
    a  "A big and juicy..."
    a  "Sausa-..."
    scene ch8_487-in with dissolve
    a  "..."
    pause
    "*Beep, beep*"
    scene ch8_469 with dissolve
    mc  "They're calling me."
    pause
    scene ch8_470 with dissolve
    mc  "Yes, hello?"
    mc  "Yes, this is [mc]."
    "..."
    pause
    scene ch8_471 with dissolve
    mc  "Tomorrow?"
    mc  "Yes, of course, at eight. I'll be there."
    a  "Who was that?"
    mc  "Just a copy job."
    mc  "Perfect."
    mc  "Thanks."
    scene ch8_472 with dissolve
    a  "Who was it?"
    mc  "[a], I think I got a job."
    a  "A job?"
    mc  "Yesterday, I sent my resumes to several companies online, and one of them wants to hire me."
    scene ch8_473 with dissolve
    a  "Really?"
    mc  "Yes, they called me in for an interview tomorrow morning."
    a  "That's great news."
    scene ch8_474 with dissolve
    a  "Congratulations, honey."
    mc  "Thanks."
    scene ch8_481 with dissolve
    mc  "Now I'll have money to buy gifts and spoil my [arelat]."
    a  "Aww.."
    pause
    scene ch8_477 with dissolve
    a  "I hope that's not the only reason you got the job."
    mc  "Well, keep hoping."
    scene ch8_478
    a  "Honey..."
    a  "You're not serious."
    mc  "I am serious. I want to have money to take you out and treat you and the girls."
    scene ch8_477 with dissolve
    a  "Aww, you're so sweet, you know that?"
    mc  "Yes, I know."
    scene ch8_476- with dissolve
    a  "You don't have to do that, [mc]."
    a  "If you just want to start being self-taught, that's okay."
    mc  "I don't want to be self-taught."
    show ch8_482--- with dissolve:
        zoom 0.75 
    pause
    show ch8_482----------- with dissolve: 
        zoom 0.75
    mc  "I want to keep being taken care of by you."
    scene ch8_476- with Dissolve(0.5)
    pause 0.25
    scene ch8_476 with dissolve
    a "Oh..."
    pause
    scene ch8_479 with dissolve
    a "You're getting used to holding me like that."
    scene ch8_477 with dissolve
    a "I'm going to make launch."
    mc "Can I help-{w=0.5}{nw}"
    a "Nope, you're going to wait until I finish cooking."
    scene ch8_480 with dissolve
    a "I'm going to make the most delicious chicken you've ever tasted."
    mc "Hmm... my mouth is watering."
    a "*Giggles*"
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 1.5
    scene ch8_488 with dissolve
    k "Hey."
    mc "Hey."
    mc "Did you have fun?"
    s "It sucked."
    scene ch8_489 with dissolve
    d "We'll go next day."
    s "I wanted to go today."
    scene ch8_490 with dissolve
    d "[s:.5], don't be like that."
    s "Why did you take us to the beach if you weren't going to let us swim?"
    d "[s], the sun was already setting."
    d "We didn't even have swimsuits."
    s "I don't want to talk to you."
    scene ch8_491 with dissolve
    d "Uhh..."
    d "Why you had to inherit my temperament?"
    scene ch8_492 with dissolve
    d "I'm exhausted..."
    k "We walked too much."
    mc "Where did you go?"
    k "Dad took us to eat at a restaurant near the beach...{w=0.4} again."
    d "I thought you guys liked seafood."
    k "And then he took us to see the formula one race."
    d "That was fun, you can't deny it."
    k "Yeah..."
    k "Then we went to the beach, but only walked along the shore and [s] wanted to swim."
    k "But dad didn't let her and she went crazy."
    s "No, you're crazy!"
    scene ch8_493 with dissolve
    k "Shut up."
    k "Ugh... she was nagging all day..."
    k "Uh?"
    pause
label ch8k3:
    if _in_replay:
        show screen Replayexit
        play music scene2 fadein 1.0
    scene ch8_494 with dissolve 
    k "..."
    pause
    scene ch8_495 with dissolve
    mc "What...?"
    k "..."
    pause
    scene ch8_496 with dissolve
    pause
    scene ch8_497 with dissolve
    pause
    image ch8_499ainm:
        "ch8_499" with Dissolve(0.5)
        1.75
        "ch8_500" with Dissolve(0.5)
        1.75
        repeat
    scene ch8_499ainm with dissolve
    mc "{i}[k]."
    k "{i}Shut up."
    pause
    scene ch8_501 with dissolve
    k "{i}I wanted to come back as soon as possible too."
    k "{i}I want to have sex, [mc]."
    k "{i}What if we sneak off somewhere and do it?"
    mc "Are you crazy?"
    scene ch8_502 with dissolve
    k "{i}Let's go outside, we'll do it outside behind a tree."
    mc "{i}You're crazy, the neighbors have cameras."
    k "{i}Then let's go to my room."
    k "{i}We'll leave the window open so you can jump out if dad comes."
    mc "{i}No way, I'm not daring enough."
    k "{i}Coward."
    if _in_replay:
        $ stephloving = "True"
    if stephloving != "True":
        mc "{i}You're insane."
        mc "{i}[s] is coming."
        scene ch8_493 with hpunch
        d "Come here."
        $ renpy.end_replay()
        jump ch8aftersfight
    scene ch8_504 with hpunch
    s "{i}What are you doing?"
    k "{i}No, what are you doing?"
    s "{i}I'm stopping you from doing something stupid."
    s "{i}Dad is right there, you dumb."
    s "{i}Plus... he's not yours."
    k "{i}Hm? Are you jealous?"
    s "{i}So what if I am?"
    k "{i}Does it make you jealous that I'm his favorite?"
    s "{i}You're not his favorite."
    k "{i}He didn't tell you?"
    s "{i}Tell me what?"
    k "{i}We're dating."
    scene ch8_505 with dissolve
    mc "[k], what the hell?!"
    s "{i}What? It's not true."
    s "{i}Right?"
    mc "Don't mind her, she's crazy."
    s "Am I your favorite?"
    mc "Yes, you're my favorite."
    scene ch8_506 with dissolve
    s "*Ha-ha*, I'm his favorite, {i}and you're not his girlfriend, liar."
    k "{i}If I wasn't his girlfriend, could I do this?"
    scene ch8_507 with dissolve
    mc "[k]!"
    s "Ah!"
    play music doing
    scene ch8_508 with hpunch
    k "*Ouch!" with hpunch
    s "You're such a...!" with hpunch
    scene ch8_509- with hpunch
    s "You!...{w=0.4} You're a!...{w=0.5} A bitch!" with hpunch
    mc "Stop it, [s], stop!"
    s "This will teach you to respect me!" with hpunch
    s "Bitch!" with hpunch
    scene ch8_510 with dissolve
    mc "Relax, she just wanted to tease you."
    s "Ugh... stupid, idiotic, bitch!"
    scene ch8_511 with dissolve
    d "Hey, hey, what's going on here?"
    s "Ugh!!"
    s "Take me to the beach!" with vpunch
    d "We can't go to the beach now, it's nighttime, [s]."
    s "*Ugh!*" with vpunch
    d "Calm down, you're going to burst a vein. We'll go tomorrow."
    scene ch8_512 with dissolve
    s "Really?"
    d "Better on Friday."
    scene ch8_513 with dissolve
    s "Ugh! I never get what I want."
    d "Come on, calm down. Come sit with me."
    $ renpy.end_replay()
    k "Thanks for caring about me."
    mc "{i}Shut up."
label ch8aftersfight:
    scene ch8_514 with dissolve
    d "Remember how you wanted me to take you shopping?"
    d "I'll buy you all the clothes you want tomorrow."
    s "The 'whatever you want' is never true..."
    s "Dinner is ready by the way."
    if stephloving == "True":
        scene ch8_515 with dissolve
        k "Great, she almost killed me and she's the one who gets a reward."
        d "I'll take you shopping too."
        d "But don't act innocent, I'm sure you started all of this."
        stop music fadeout 1.5
        play music scene2 fadein 1.5
    scene ch8_516 with dissolve
    if stephloving == "True":
        a "What happened here?"
        d "Nothing, honey. The girls had a little fight that we already resolved."
        k "She almost killed me."
    else:
        a "Dinner is ready."
        s "Yeah, I already told them."
        a "Speaking of telling."
    scene ch8_517 with dissolve
    a "Honey, did you tell them yet?"
    mc "What thing?"
    if stephloving == "True":
        k "Hello? Did you hear the part where I said I almost died?"
    scene ch8_518 with dissolve
    a "About your job."
    mc "Oh, right."
    scene ch8_519 with dissolve
    k "You have a job?"
    mc "Yeah, well, I sent some emails online and they called me today for an interview tomorrow."
    k "Great, I hope you buy me something with your first paycheck."
    s "You damn..."
    k "Congratulations, [mc]."
    scene ch8_520 with dissolve
    s "Dad, aren't you going to congratulate [mc]?"
    s "Dad...?"
    d "What? Oh yeah, of course, of course."
    scene ch8_521 with dissolve
    d "I'm very happy for you."
    d "So that's why you didn't come with us, you were waiting for that call."
    mc "Uh... yeah."
    d "I'm really happy for you, [mc]."
    d "Looks like we'll be two men of the house now."
    d "I mean, not that you weren't before... You know what I mean."
    mc "I know what you mean, don't worry."
    mc "I'm glad I can contribute to the household now."
    d "Well said, [mc]."
    scene ch8_522 with dissolve
    d "How about we order some food and watch a movie upstairs to celebrate?"
    s "Yes!"
    scene ch8_523 with dissolve
    s "Will you buy me things with your money?"
    mc "Yes, of course."
    k "Me too, right?"
    a "And me."
    mc "All of you, even the [drelat] [d]."
    "*Laughter*"
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 1.5
    scene ch8_524 with dissolve
    s "What movie will we watch?"
    d "[mc], what do you think?"
    mc "You guys choose."
    scene ch8_525 with dissolve
    k "How about an action movie?"
    mc "Sure..."
    scene ch8_527 with dissolve
    s "Excuse me."
    k "Ugh..."
    scene ch8_528 with dissolve
    s "I'll sit next to [mc]."
    s "I want to watch a horror movie."
    mc "S-sure, we'll watch whatever you guys want."
    d "Not a horror movie, honey. I don't want to see you traumatized like last time."
    s "It won't happen again, I promise."
    d "No, honey."
    scene ch8_529 with dissolve
    s "*Ugh!*"
    d "Okay, where's [a]?"
    d "She said she was coming, right?"
    mc "Yeah, she said she was on her way."
    scene ch8_530 with dissolve
    mc "(Oh wow...)"
    d "[a]..."
    scene ch8_531 with dissolve
    a "Did you guys choose the movie?"
    d "No, not yet."
    s "We're going to watch a horror movie."
    scene ch8_532 with dissolve
    k "Wow..."
    k "Mom, I've never seen you wear that before."
    a "I had it stored somewhere and I felt like wearing it."
    s "It's really tight on you, [arelatks]."
    a "Do you think so?"
    a "I've put on some weight these last few months and I don't think it fits me like it used to."
    s "It looks like your breasts are going to burst out of it any second."
    s "I like it, it looks really good on you."
    a "T-thank you..."
    scene ch8_534 with dissolve
    pause
    image ch8_535inanim:
        "ch8_535in"
        zoom 0.75
        ease 3 xalign 0.7 yalign 0.5
        ease 3 xalign 0.6 yalign 1.0
        ease 3 xalign 0.0
        repeat
    scene ch8_535inanim with dissolve
    mc "(I've never seen [a] dress like that, not even for sleeping.)"
    mc "([s] is right, those boobs are about to burst out of that pajama.)"
    pause
    scene ch8_534 with dissolve
    mc "{i}You look cute."
    scene ch8_533 with dissolve
    a "{i}Thanks, you look cute too. *giggles*"
    pause
    scene ch8_534 with dissolve
    s "I'm going to put on this movie."
    k "Not a horror movie, [s]."
    s "I'll put on whatever I want, you don't boss me around."
    k "Just don't come to my room later saying you're scared to sleep alone."
    s "I'll go with [mc]."
    d "Just put on a movie already, please."
    pause
label ch8a5:
    if _in_replay:
        show screen Replayexit
    stop music fadeout 4.0
    scene ch8_536 with Fade(2.0,2.0,2.0)
    pause
    mc "(I'm falling asleep.)"
    mc "(They don't make good horror movies anymore...)"
    scene ch8_537 with dissolve
    pause
    mc "(Good thing I have something to keep me awake.)"
    pause
    scene ch8_539 with dissolve
    pause
    play music sexy2 fadein 4.0
    scene ch8_540 with dissolve
    pause
    scene ch8_538 with dissolve
    pause
    scene ch8_541 with dissolve
    s "Uh.. uhh.."
    scene ch8_542 with dissolve
    k "I told you to put on something else."
    scene ch8_543 with dissolve
    s "Shut up, I'm not scared."
    scene ch8_542 with dissolve
    k "You're literally trembling."
    s "I'm cold."
    scene ch8_541 with dissolve
    k "Yeah, sure."
    pause
    scene ch8_540 with dissolve
    pause
    scene ch8_544 with dissolve
    pause
    scene ch8_545 with dissolve
    pause
    mc "(I really want to grab those boobs...)"
    scene ch8_544 with dissolve
    mc "(We're in the dark, I don't think anyone will notice.)"
    pause
    scene ch8_547-------------------- with dissolve
    a "..."
    scene ch8_549 with dissolve
    mc "(Not a single word...)"
    mc "(I love how careless she is now.)"
    image ch8_548anim:
        "ch8_548----------------------" with Dissolve(0.5)
        2.0
        "ch8_549" with Dissolve(0.5)
        2.0
        repeat
    scene ch8_548anim with dissolve
    pause
    mc "(I can't believe these boobs aren't fake.)"
    mc "(I don't think I'll find any other woman with boobs like these.)"
    mc "(Well, maybe [k]'s are a little similar, but I think hers are firmer.)"
    mc "([a]'s are bigger, although a bit more saggy.)"
    mc "(Of course, they're the boobs of a mother of two daughters.)"
    mc "(Still, I don't see that as a bad thing, I like that they're a bit soft.)"
    a "{i}[mc]."
    scene ch8_550 with dissolve
    a "{i}No, [mc]."
    scene ch8_546- with dissolve
    pause
    scene ch8_546 with dissolve
    a "{i}Stay there."
    pause
    scene ch8_546-- with dissolve
    pause
    scene ch8_550 with dissolve
    a "{i}Don't be reckless, honey."
    mc "{i}You look too sexy in that pijama."
    scene ch8_551 with dissolve
    a "{i}Thank you."
    mc "{i}Did you wear it for me?"
    scene ch8_552 with dissolve
    a "{i}I wore it to sleep comfortably tonight."
    mc "{i}I see..."
    scene ch8_552 with dissolve
    a "{i}Not everything is about you, [mc]."
    mc "{i}Yeah, sure."
    image ch8_553anim:
        "ch8_553" with Dissolve(0.5)
        2.0
        "ch8_554" with Dissolve(0.5)
        2.0
        repeat
    scene ch8_553anim with dissolve
    mc "{i}I'll pretend I believe you."
    pause
    scene ch8_555 with dissolve
    a "{i}Oh..."
    pause
    scene ch8_556 with dissolve
    a "..."
    pause
    scene ch8_557 with dissolve
    a "..."
    pause
    scene ch8_562 with dissolve
    mc "{i}Hm?"
    a "..."
    pause
    scene ch8_561 with dissolve
    a "..."
    scene ch8_559 with dissolve
    pause 0.4
    scene ch8_561 with dissolve
    pause
    mc "(She wants to touch but she doesn't dare.)"
    scene ch8_562 with dissolve
    mc "{i}You can touch, [arelat] [a]..."
    a "..."
    pause
    scene ch8_561 with dissolve
    pause 0.4
    scene ch8_559 with dissolve
    pause
    scene ch8_559- with dissolve
    pause 0.5
    scene ch8_561 with dissolve
    a "{i}Alright..."
    scene ch8_563 with dissolve
    mc "{i}Play more, [a]."
    a "{i}No, baby."
    mc "{i}Just a little bit."
    a "{i}No, [mc]."
    mc "{i}No one's watching."
    a "..."
    scene ch8_562 with dissolve
    a "{i}No, [mc], it's too obvious."
    a "{i}Actually, you should try to hide it."
    scene ch8_564 with dissolve
    mc "{i}Does it still show now?"
    a "{i}No, it is fine now."
    a "..."
    pause  
    play music something
    scene ch8_565 with hpunch
    s "Waaaaaahh!"
    scene ch8_566 with dissolve
    k "*Laughs* That was a good screamer."
    k "Stupid movie, it actually scared me a little too."
    $ renpy.end_replay()
label ch8s4:
    if _in_replay:
        show screen Replayexit
        play music something
        scene ch8_565 with hpunch
        s "Waaaaaahh!"
        scene ch8_566 with dissolve
        k "*Laughs* That was a good screamer."
        k "Stupid movie, it actually scared me a little too."
        $ stephloving = "True"
    d "We should put on something else."
    s "N-no, I like this one."
    d "But, honey, you're not even watching it anymore."
    s "I'm listening to it."
    d "..."
    if stephloving != "True":
        jump ch8aftersbjh
    stop music fadeout 0.5
    scene ch8_568 with dissolve
    pause
    play music scene3 fadein 3.0
    scene ch8_569- with Dissolve(2.0)
    pause
    s "{i}Wow..."
    pause
    scene ch8_566 with dissolve
    mc "[s]..."
    s "Do you mind if I stay here?"
    mc "No, but..."
    scene ch8_568 with dissolve
    pause
    scene ch8_570 with Dissolve(2.0)
    s "*Giggle...*"
    mc "U-umm..."
    scene ch8_569 with dissolve
    pause
    scene ch8_571 with dissolve
    mc "(What the hell is she doing?)"
    mc "[s]."
    s "Shh..."
    $ anim_speed = 0.035
    scene ch8_s_dicklick_pov1_ with dissolve
    mc "(Oh my god...)"
    mc "(We're all here, including [drelat] [d], if we get caught I'm dead, no, worse than dead.)"
    mc "(The [drelat] will send me straight to hell.)"
    s "*Lahl, lha*"
    pause
    scene ch8_572 with dissolve
    s "*Hmchu*" 
    mc "(This girl doesn't care about anything.)"

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_s_bj_6_pov1_(trans, st, at):  
        trans.set_child("ch8_s_bj_6_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 5:
            sound_files = ["audio/wavs/bj_31.ogg", "audio/wavs/bj_34.ogg", "audio/wavs/bj_19.ogg", "audio/wavs/bj_36.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_30.ogg", "audio/wavs/bj_13.ogg", "audio/wavs/bj_25.ogg", "audio/wavs/bj_28.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_s_bj_6_pov2_(trans, st, at):  
        trans.set_child("ch8_s_bj_6_pov2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 5:
            sound_files = ["audio/wavs/bj_31.ogg", "audio/wavs/bj_34.ogg", "audio/wavs/bj_19.ogg", "audio/wavs/bj_36.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 25:
            sound_files = ["audio/wavs/bj_30.ogg", "audio/wavs/bj_13.ogg", "audio/wavs/bj_25.ogg", "audio/wavs/bj_28.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_s_dicklick_pov1_(trans, st, at):  
        trans.set_child("ch8_s_dicklick_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/wavs/bj_24.ogg", "audio/wavs/bj_23.ogg", "audio/wavs/bj_24.ogg", "audio/wavs/bj_19.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 


screen ch8_s_bj_6_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_s_bj_6_pov1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_s_bj_6_pov2_") style "textbutton_choice"     
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Lick" action Jump("ch8_s_dicklick_pov1_") style "textbutton_choice"     
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"


screen ch8_s_bj_6_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_s_bj_6_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_s_bj_6_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Lick" action Jump("ch8_s_dicklick_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"


screen ch8_s_dicklick_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_s_bj_6_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_s_bj_6_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_s_bj_6_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"


label beforech8_s_bj_6_pov2_:    
    image ch8_s_bj_6_pov1_:
        function ch8_s_bj_6_pov1_
    image ch8_s_bj_6_pov2_:
        function ch8_s_bj_6_pov2_
    image ch8_s_dicklick_pov1_:
        function ch8_s_dicklick_pov1_
    $ anim_speed = 0.055
    scene ch8_s_bj_6_pov1_ with dissolve
    mc "(Shit... this can't be happening, I have to stop this.)"
mc "{i}Stop, [s]."
s "{i}*Slurp, slurp, smnch*"
mc "{i}Stop, [s]!"
s "*Chup, schup*"
mc "{i}Don't pretend you can't hear me."
mc "{i}Stop..."
s "*Hmph!*" with hpunch
mc "Ouch!"
scene ch8_566 with dissolve
a "[s], what are you doing?"
mc "I got a cramp, that's all..."
a "[s], you're not letting [mc] enjoy the movie."
s "*Plop*, I'm not doing anything."
mc "I-it's fine, [a], she's, {w=0.4}*Hmm*{w=0.4}, not bothering me."
scene ch8_575 with dissolve
pause 0.25
scene ch8_s_bj_6_pov2_ with Dissolve(2.0)
s "*Chup, suck, hmph*"
mc "Uhmm... (Fuck, I'm close.)"
mc "(Is she trying to make me ejaculate?)"
mc "(I hope not, for God's sake.)"
mc "(I can't walk around all covered in cum, they'll notice.)"

label ch8_s_bj_6_pov1_:
    scene ch8_s_bj_6_pov1_ with dissolve
    call screen ch8_s_bj_6_pov1_settings with dissolve

label ch8_s_bj_6_pov2_:
    scene ch8_s_bj_6_pov2_ with dissolve
    call screen ch8_s_bj_6_pov2_settings with dissolve

label ch8_s_dicklick_pov1_:
    scene ch8_s_dicklick_pov1_ with dissolve
    call screen ch8_s_dicklick_pov1_settings with dissolve

label afterch8_s_bj_6_pov1_:
    $ anim_speed = 0.015
    scene ch8_s_bj_6_pov2_ with dissolve
    s "*slurp, slurp, slurp*, *Hmnhh!*"
    mc "(She's moving too much.)"
    mc "(God, I'm so close already.)"
    mc "*Hngh!* (I have to hold it!)"
    pause
    image ch8_581anim_:
        "ch8_581" with Dissolve(0.1)
        0.25
        "ch8_582" with Dissolve(0.1)
        0.25
        repeat
    scene ch8_581anim_ with dissolve
    s "*Huh, huh, hungh*"
    mc "(Finally stopped.)"
    mc "(She's coming.)"
    d "[s], stop shaking so much, it's not that big a deal."
    with cumming
    scene ch8_581 with flash
    s "*Hmngh!* Uhh..."
    pause
    scene ch8_583 with dissolve
    d "This is the last time we watch this kind of movie, got it?"
    scene ch8_584 with dissolve
    s "Huuhh...."
    k "*Laughs*, what happened to you?"
    s "N-nothing, shut up."
    scene ch8_585 with dissolve
    s "I'm going to my room now, I don't want to watch this movie anymore."
    d "[s], did you wet yourself?"
    s "What...?"
    s "Oh... y-yes, I think so."
    a "Oh, baby. We won't watch this kind of movie again."
    d "Don't worry, honey, it happens to all of us."
    k "*Pfff*"
    d "Shut up, [k]!"
    a "Now go to the bathroom, take a shower and go to bed, okay, baby?"
    s "Okay."
    mc "(That's not urine...)"
    pause
    scene ch8_586 with dissolve
    s "Well, I'm leaving now."
    s "Good night."
    mc "(God...)"
    $ renpy.end_replay()
    pause
    stop music fadeout 4.0
    scene blackscreen with dissolve
    pause
    scene ch8_587 with dissolve
    d "The movie's over."
    d "I liked spending time together."
    pause
label ch8a6:
    if _in_replay:
        show screen Replayexit
        scene ch8_587 with dissolve
    d "Well..."
    scene ch8_588 with dissolve
    d "[mc] seems to have fallen asleep...{w=0.4} Huh?"
    a "I'll wake him up."
    d "Uh... yeah, okay."
    d "Good night, honey."
    a "{w=1.0}Good night."
    pause
label ch8aftersbjh:
    stop music fadeout 2.0
    scene blackscreen with Dissolve(2.0)
    pause
    a "[mc], wake up."
    scene ch8_590 with dissolve
    mc "Uh..." with Fade(1.0,0.5,1.0)
    scene ch8_589 with dissolve
    play music sexy3 fadein 5.0
    a "You fell asleep."
    mc "Everyone's left already?"
    a "For a while now."
    mc "The movie instead of scaring me it lulled me to sleep."
    a "Yeah, the movie was pretty bad."
    a "But to be fair, that happens with every movie you watch."
    mc "True."
    mc "So, do I have to go now?"
    scene ch8_592 with dissolve
    a "No, you can stay a little longer if you want."
    scene ch8_591 with dissolve
    pause
    mc "You look stuning in this pijama, [a]."
    scene ch8_593 with dissolve
    a "It's custom-made."
    a "[d] gave it to me as a gift months ago."
    a "He bought it to appease me."
    scene ch8_592 with dissolve
    a "I really never wore it until today."
    pause
    a "And yes, I put it on for you today."
    a "So that...{w=0.4} you can see how it looks on me."
    mc "Well, you already know my opinion."
    scene ch8_591 with dissolve
    mc "It fits you perfectly."
    a "The seamstress who made it is a genius."
    image ch8_594anim:
        "ch8_594" with Dissolve(0.5)
        1.75
        "ch8_595" with Dissolve(0.5)
        1.75
        repeat
    scene ch8_594 with dissolve
    a "You fell asleep with that erection and it never went down..."
    scene ch8_592 with dissolve
    mc "How do you know?"
    scene ch8_593 with dissolve
    a "Uh... Can't you see it?"
    scene ch8_594anim with dissolve
    a "It's still so erect..."
    pause
    scene ch8_596 with dissolve
    a "..."
    scene ch8_594 with dissolve
    pause
    scene ch8_596 with dissolve
    pause 0.25
    scene ch8_596- with dissolve
    a "Oh, god..."
    a "It's so hard..."
    pause
    scene ch8_592 with dissolve
    a "I think I'm crossing a line, *he-he*."
    mc "It's okay, [a]."
    scene ch8_593 with dissolve
    a "N-no, this is not right."
    mc "[a], I don't mind at all."
    pause
    mc "Do you want to see it?"
    a "..."
    mc "(I'll take that as a 'yes')"
    scene ch8_599 with dissolve
    a "[mc]..."
    pause
    scene ch8_600 with dissolve
    a "I-it's so big."
    pause
    scene ch8_601 with dissolve
    a "It looks like it's going to burst..."
    image ch8_601anim:
        "ch8_600" with Dissolve(0.5)
        1.75
        "ch8_601" with Dissolve(0.5)
        1.75
        repeat
    mc "Oh... that feels good."
    a "..."
    pause
    scene ch8_602 with dissolve
    pause
    scene ch8_603 with dissolve
    a "It reaches up to your chest..."
    pause
    image ch8_602anim:
        "ch8_602" with Dissolve(0.5)
        1.0
        "ch8_603" with Dissolve(0.5)
        1.0
        repeat
    a "Oh my god..."
    pause
    image ch8_604anim:
        "ch8_605" with Dissolve(0.3)
        1.5
        "ch8_604" with Dissolve(0.3)
        1.5
        repeat
    scene ch8_604anim with dissolve
    a "..."
    a "The head is pretty large too..."
    pause
    scene ch8_606 with dissolve
    a "I'm sorry."
    mc "Why are you apologizing?"
    a "I did it again."
    mc "You have my permission to touch me whenever you want."
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.4
    scene ch8_609 with dissolve
    pause
    scene ch8_610 with dissolve
    a "*Ahl.. hmlh*."
    pause
    scene ch8_611 with dissolve
    mc "I can't take it anymore, [a]."
    a "*Hmm.. mnch*"
    pause
    stop sound fadeout 0.5
    scene ch8_612 with dissolve
    a "Are you going to take off your clothes?"
    mc "Yes."
    pause
    scene ch8_613 with dissolve
    mc "I feel like I'm going to explode, look at me."
    a "Y-yes, it's very swollen..."
    pause
    a "J-just remember the boundaries."
    scene ch8_614 with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.4
    mc "Don't talk to me about boundaries now, [a]."
    pause
    scene ch8_614--- with dissolve
    a "Oh, [mc]..."
    mc "Hmm, you're wearing perfume."
    mc "Did you know this was going to happen?"
    a "Ah..."
    scene ch8_614---- with dissolve
    mc "Of course you did, you put on this sexy pajama for me after all."
    mc "Hmm... so delicious."
    pause
    scene ch8_614- with dissolve
    a "*Umsh, hmn*"
    pause
    scene ch8_614-- with dissolve
    pause
    stop sound fadeout 0.5
    show ch8_616-in with dissolve:
        xalign 0.5 yalign 1.0
        ease 5 yalign 0.1
    mc "God..."
    pause
    show ch8_616-in with dissolve:
        xalign 0.5 yalign 0.0
        ease 5 yalign 1.0    
    mc "[a], I want to do something."
    a "...."
    scene ch8_617- with dissolve
    a "Oh..."
    mc "I want to feel my penis wrapped in them again..."
    scene ch8_618 with dissolve
    a "Uh, sure..."
    a "We've done this before, right?"
    mc "Twice."
    a "Twice... *Heh..*"
    a "W-well..."

init python:
    def ch8_atj_2_pov1_(trans, st, at):  
        trans.set_child("ch8_atj_2_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_atj_2_pov2_(trans, st, at):  
        trans.set_child("ch8_atj_2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_atj_2_pov3_(trans, st, at):  
        trans.set_child("ch8_atj_2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   




init python:
    def ch8_atj_3_pov1_(trans, st, at):  
        trans.set_child("ch8_atj_3_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_atj_3_pov2_(trans, st, at):  
        trans.set_child("ch8_atj_3_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_atj_3_pov3_(trans, st, at):  
        trans.set_child("ch8_atj_3_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   






screen ch8_atj_2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech8_atj_2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_atj_2_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_atj_2_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_atj_2_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech8_atj_2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_atj_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_atj_2_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_atj_2_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech8_atj_2_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_atj_2_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_atj_2_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"


screen ch8_atj_3_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_atj_3_pov3_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_atj_3_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_atj_3_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_atj_3_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_atj_3_pov3_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_atj_3_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_atj_3_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_atj_3_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.013) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_atj_3_pov3_settings") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_atj_3_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_atj_3_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"


label afterch8_atj_2_pov1_:
    image ch8_atj_2_pov1_:
        function ch8_atj_2_pov1_
    image ch8_atj_2_pov2_:
        function ch8_atj_2_pov2_
    image ch8_atj_2_pov3_:
        function ch8_atj_2_pov3_

    image ch8_atj_3_pov1_:
        function ch8_atj_3_pov1_
    image ch8_atj_3_pov2_:
        function ch8_atj_3_pov2_
    image ch8_atj_3_pov3_:
        function ch8_atj_3_pov3_
    $ anim_speed = 0.05
    scene ch8_atj_2_pov1_ with dissolve
    scene ch8_atj_2_pov1_ with dissolve

    mc "Oh... this is the best."
    mc "So, you never wore this pajama for [drelat] [d]?"
    a "Only once, but yeah..."
    pause
    a "There was no reaction."
    pause
    mc "That's insane."
    mc "I wouldn't have lasted a day without seeing you wear it at night."
    mc "With my first paycheck, I'll buy you something nice too."
    a "Buy something for yourself first."
    mc "Trust me, I'll enjoy it more than you will."
    mc "It'll really be a gift for me."
    a "Well, in that case... *giggles*."
    scene ch8_atj_2_pov2_ with dissolve
    pause
    a "I'll let you buy me one then."
    mc "The one I want?"
    a "Yes, the one you want."
    mc "Really?"
    a "Yes."
    a "You can treat me like your mannequin, *giggles*."
    a "Or will it literally be a gift for you and you'll wear it?"
    mc "*Laughs*, yes, that's what I meant."
    a "*Laughs*"
    mc "Hmm....{w=0.4} Although I'm not sure if a neckline like this would look as good on me as it does on you."
    a "I'm sure it will, *giggles*."
    mc "Let me doubt it."
    a "*Laughs*"
    scene ch8_atj_2_pov3_ with dissolve
    mc "*Hmm..*"
    mc "The seamstress did a great job."
    a "She measured me very carefully before making it."
    a "But I chose the design."
    mc "It's a very sexy design."
    a "..."
    a "I wanted to look sexy..."
    mc "You succeeded."
    mc "But he just didn't want to see it."
    a "..."

    label ch8_atj_2_pov1_:

    scene ch8_atj_2_pov1_ with dissolve
    call screen ch8_atj_2_pov1_settings with dissolve

    label ch8_atj_2_pov2_:

    scene ch8_atj_2_pov2_ with dissolve
    call screen ch8_atj_2_pov2_settings with dissolve

    label ch8_atj_2_pov3_:

    scene ch8_atj_2_pov3_ with dissolve
    call screen ch8_atj_2_pov3_settings with dissolve

    label beforech8_atj_2_pov1_:

    a "{i}I don't want you to stain the pajama, okay?"
    a "{i}Remember that [d] gave it to me."
    mc "Hmm...{w=0.4}, don't worry."
    a "Okay."
    $ anim_speed = 0.011
    mc "Hngh...{w=0.4}, god..."
    a "Remember what I told you, [mc]."
    mc "Yes.."
    pause
    mc "*Ah..*"
    a "It's better if I take it off."
    scene ch8_619 with dissolve
    mc "You don't have to take it off completely."
    mc "I'm constantly amazed by how beautiful you are, [a]."
    scene ch8_620 with dissolve
    mc "God, you have beautiful breasts, [a]."
    pause
    scene ch8_621 with dissolve
    mc "Let me move these aside..."
    pause
    scene ch8_622 with dissolve
    mc "Jesus..."
    pause
    scene ch8_623 with dissolve
    a "Hmm..."
    mc "Fuck..."
    pause
    scene ch8_624 with dissolve
    a "Oh..."
    pause
    scene ch8_625 with dissolve
    a "*Ah...*"
    pause
    scene ch8_626 with dissolve
    a "*Uhmm...*"
    pause
    scene ch8_626- with dissolve
    mc "They're so delicious."
    a "Thank you."
    mc "I wish I could eat you whole every day."
    pause
    $ anim_speed = 0.035
    scene ch8_atj_3_pov1_ with dissolve
    mc "Oh, yes..."
    mc "[a], I love you."
    a "I love you too, honey."
    a "Hurry up and cum, you have important things to do tomorrow."
    mc "I'm going to enjoy every second I can."
    mc "I don't care if I have to go to that interview without sleeping."
    scene ch8_atj_3_pov2_ with dissolve
    a "No, baby. You need to rest, tomorrow will be a long day."
    mc "Oh, [a]..."
    mc "There couldn't be a better way to celebrate my new job than this."
    mc "With you, kissing and then rubbing my penis between your beautiful breasts."
    pause
    scene ch8_atj_3_pov3_ with dissolve
    a "That's true, we're celebrating your new job."
    a "..."
    pause
    a "In that case...you can stay a little longer."
    mc "Thank you!"
    pause
label ch8_atj_3_pov1_:
    scene ch8_atj_3_pov1_ with dissolve
    call screen ch8_atj_3_pov1_settings
label ch8_atj_3_pov2_:
    scene ch8_atj_3_pov2_ with dissolve
    call screen ch8_atj_3_pov2_settings
label ch8_atj_3_pov3_:
    scene ch8_atj_3_pov3_ with dissolve
    call screen ch8_atj_3_pov3_settings

label afterch8_atj_3_pov3_settings:
    mc "Take everything off, [a], this time I want to see you naked."
    a "N-naked?"
    mc "Yes... I want to appreciate your whole body in the nude."
    a "{i}{size=-5}Naked..."
    a "Not naked, but I can take off my pajamas."
    a "Is that okay?"
    mc "Yes, sure, whatever makes you more comfortable.."
    mc "I just want to see your figure better."
    a "Alright."
    scene ch8_626--inin with dissolve
    mc "Wow..."
    mc "What a delicious woman."
    scene ch8_626--- with dissolve
    mc "Those breasts..."
    a "*Giggle*, do you like them?"
    mc "I love them."
    pause
    scene ch8_626---- with dissolve
    mc "[a], can you stand up?"
    a "Do you want me to stand?"
    mc "Yes, to appreciate your body better."
    scene ch8_626----- with dissolve
    a "Okay, but I'll only take off my pajamas, got it?"
    mc "Yes, that's what we agreed on."
    a "Alright..."
    scene ch8_628 with dissolve
    a "So you want me to take off my pajamas?"
    mc "Yes."
    a "Hmm... I don't see you very eager for me to do it..."
    mc "Yes, please!, *laugh*"
    a "*Giggle*, okay."
    scene ch8_629 with dissolve
    mc "Oh, wow..."
    a "You've seen me like this before."
    mc "And I'm still blown away by your beauty."
    a "Oh, *giggle*."
    scene ch8_630 with dissolve
    mc "Hmmm, you're so hot, god..."
    pause
    scene ch8_631 with dissolve
    mc "*Munch*, are you going to take off the bottom part too?"
    a "If you want me to..."
    mc "Of course I want to."
    scene ch8_632 with dissolve
    mc "Can I take it off for you?"
    a "Hmm... okay."
    scene ch8_634 with dissolve
    mc "Your beauty is truly out of this world, [a]."
    mc "It's incomparable to anything I've ever seen."
    a "*Giggle*, stop it, [mc], you're making me blush."
    scene ch8_636 with dissolve
    pause
    scene ch8_635_series_30 with dissolve
    mc "Hmmm, what a piece of woman..."
    jump ch8_635_series_30

label ch8_635_series_24:
    scene ch8_635_series_24 with Dissolve(0.1) 
    call screen arrow_buttons24  
label ch8_635_series_25:
    scene ch8_635_series_25 with Dissolve(0.1)  
    call screen arrow_buttons25     
label ch8_635_series_26:
    scene ch8_635_series_26 with Dissolve(0.1)  
    call screen arrow_buttons26     
label ch8_635_series_27:
    scene ch8_635_series_27 with Dissolve(0.1)  
    call screen arrow_buttons27     
label ch8_635_series_28:
    scene ch8_635_series_28 with Dissolve(0.1)  
    call screen arrow_buttons28     
label ch8_635_series_29:
    scene ch8_635_series_29 with Dissolve(0.1)  
    call screen arrow_buttons29     
label ch8_635_series_30:
    scene ch8_635_series_30 with Dissolve(0.1)  
    call screen arrow_buttons30     

screen arrow_buttons24:
        textbutton "{image=left_arrow}" action Jump("ch8_635_series_25") xalign 0.0 yalign 1.0
        textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice" 
screen arrow_buttons25:       
    textbutton "{image=left_arrow}" action Jump("ch8_635_series_26") xalign 0.01 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch8_635_series_24") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice"
screen arrow_buttons26:
    textbutton "{image=left_arrow}" action Jump("ch8_635_series_27") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch8_635_series_25") xalign 1.0 yalign 1.0
    textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice" 
screen arrow_buttons27:
    textbutton "{image=left_arrow}" action Jump("ch8_635_series_28") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch8_635_series_26") xalign 1.0 yalign 1.0
    textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice" 
screen arrow_buttons28:
    textbutton "{image=left_arrow}" action Jump("ch8_635_series_29") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch8_635_series_27") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice"
screen arrow_buttons29:
    textbutton "{image=left_arrow}" action Jump("ch8_635_series_30") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch8_635_series_28") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice"
screen arrow_buttons30:
    textbutton "{image=right_arrow}" action Jump("ch8_635_series_29") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch8_arrowbuttons635") xalign 0.99 yalign 0.05 style "textbutton_choice"
      
label ch8_arrowbuttons635:
    scene ch8_640 with dissolve
    mc "What a figure..."
    mc "I'm fascinated by your body."
    a "I have a bit of a belly."
    mc "Lies."
    a "I suck in my belly a bit so it doesn't show, *giggle*."
    scene ch8_641 with dissolve
    mc "*Hmm*, are you talking about this belly?"
    a "Oh, *giggle*."
    pause
    scene ch8_639 with dissolve
    mc "God..."
    pause
    mc "I can't believe those breasts are all mine now."
    a "*Laughs*, what?"
    scene ch8_638 with dissolve
    a "When did I say they're all yours?"
    mc "T-they're not?"
    a "..."
    a "Only thirty percent, I keep the rest, *giggle*."
    mc "Aww, that's not fair."
    mc "Can't you give me a bit more percentage?"
    a "Fifty percent, take it or leave it."
    scene ch8_637 with dissolve
    mc "Hmm... I'll accept the fifty percent."
    mc "-For now."
    a "*Giggle*"
    pause
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.35
    scene ch8_642 with dissolve
    a "*Mmmhmm, mmmnch*"
    pause
    scene ch8_643 with dissolve
    mc "And how will it work, one breast is mine?"
    a "*Giggle*, it was just a joke, [mc]."
    a "*Hmnch, mmmnch*"
    mc "I see, so they're all mine one hundred percent."
    a "Stop it, you swindler."
    image ch8_645anim:
        "ch8_645" with Dissolve(0.25)
        1.0
        "ch8_646" with Dissolve(0.25)
        1.0
        repeat
    scene ch8_644 with dissolve
    mc "*Hmmhm*{w=0.4}, your tits taste so good, [a]."
    a "*Hmmhnch, mmm*"
    pause
    scene ch8_645anim with dissolve
    a "*Hmnch*{w=0.4}, [mc], you're so...{w=0.4} wonderful."
    mc "Thanks{w=0.4}, *hmmhm*, nobody's ever told me I'm wonderful before."
    a "You're such a wonderful boy."
    pause
    scene ch8_647- with dissolve
    pause
    mc "(I want her to enjoy too.)"
    pause
    scene ch8_648- with dissolve
    a "[mc]{w=0.4}, *Hmnch*{w=0.4}, no..."
    pause
    scene ch8_650 with dissolve
    a "N-no, baby."
    mc "Just a little bit."
    a "..."
    pause
    scene ch8_651 with dissolve
    a "*Ahh, mmm*"
    pause
    scene ch8_652 with dissolve
    a "*Hmmnch, hmnhm*"
    pause
    image ch8_652anim:
        "ch8_653" with Dissolve(0.5)
        1.5
        "ch8_654" with Dissolve(0.5)
        1.5
        repeat
    scene ch8_652anim with dissolve
    a "We can't, [mc]."
    mc "Of course we can."
    a "We have to{w=0.4}, *hmnch*{w=0.4}, set boundaries."
    mc "We'll do that after pleasing you."
    mc "After hearing you moan in pleasure..."
    a "No-{w=0.4}*Hmuahl*{w=0.4}, don't say those things."
    mc "It's what I desire the most, [a]."
    mc "I want my sweet [arelat] to enjoy to the fullest."
    pause
    scene ch8_654- with dissolve
    pause
    scene ch8_654-- with dissolve
    a "No..."
    pause
    scene ch8_654--- with dissolve
    a "Uh..."
    pause
    stop sound fadeout 0.5
    scene ch8_657 with dissolve
    a "Baby..."
    mc "Just relax."
    scene ch8_659 with dissolve
    a "Uh... baby."
    a "Isn't this too much?"
    pause
    scene ch8_660 with dissolve
    a "Ah..."
    mc "Let yourself be loved, [a]."
    scene ch8_656 with dissolve
    a "No, baby... T-this is escalating too much."
    mc "It's not, you've already masturbated me several times."
    a "Yes, but..."
    scene ch8_655 with dissolve
    mc "It's exactly the same, [a]."
    mc "Let me take care of you."
    mc "If I don't, I'll feel bad about myself."
    a "[mc]..."
    pause
    a "O-okay... if you want it that much then, I can't say no."
    scene ch8_661 with dissolve
    mc "You're so wet..."
    a "*Uhh..*"
    mc "How long has it been since someone touched you, [a]?"
    a "..."
    pause
    scene ch8_662 with dissolve
    play voicefx "audio/wavs/a/amoansoft.ogg" loop
    a "Ah... ahhh..."
    a "Mhmhmm..."    
    image ch8_663anim:
        "ch8_663" with Dissolve(0.5)
        1.5
        "ch8_664" with Dissolve(0.5)
        1.5
        repeat
    scene ch8_663anim with dissolve
    a "*Uhh, ahh*"
    mc "That's it, enjoy yourself, [a]."
    a "*Uh, mmmhmm, ah*"
    a "I love you, [mc], I love you so much."
    mc "I love you too, [a]."
    mc "I love my [arelat] so much."
    a "Oh god, [mc]."
    scene ch8_664- with dissolve
    a "*Hmnhmm*"
    $ anim_speed = 1.
    image ch8_665anim:
        "ch8_665" with Dissolve(0.5)
        pause(anim_speed)
        "ch8_666" with Dissolve(0.5)
        pause(anim_speed)
        repeat
    scene ch8_665anim with dissolve
    a "*Ah, ahm!*"
    a "Oh, god,{w=0.4}, [mc]!"
    mc "Does it feel good?"
    a "Ahh, *hmhm*{w=0.4}, Yes, baby, it feels really good."
    a "Oh my God{w=0.4}, *Huhmmh!*."
    $ anim_speed = 0.6
    a "*Oh, ahhmm!*, Keep going, baby, keep going!"
    a "*Ahhmmm!*"
    scene ch8_667 with cumming
    play voicefx "audio/wavs/a/amoanhard_2.ogg"
    a "*Aah!"
    scene ch8_668 with cumming
    play voicefx "audio/wavs/a/amoanhard_1.ogg"
    a "*Ahhh!, Hmmnhm!" with flash
    pause
    scene ch8_669 with dissolve
    pause
    a "Oh my god."
    mc "Wow, [a]..."
    scene ch8_670 with dissolve
    mc "You came so fast."
    a "I-I don't know what happened, I..."
    mc "That was too sexy."
    scene ch8_672 with dissolve
    pause
    scene ch8_671 with dissolve
    a "I don't remember having such an intense orgasm before..."
    mc "I'm glad I could make you feel good."
    a "Thank you, baby."
    mc "Anytime, just let me know when you want it again."
    scene ch8_673 with dissolve
    a "Well... I think it's time for you to go to your room."
    mc "Yeah..."
    a "Because you have to wake up early tomorrow."
    mc "..."
    scene ch8_674 with dissolve
    a "..."
    a "Y-you're still hard..."
    a "..."
    a "Do you want me to..."
    a "We can do something."
    scene ch8_674- with dissolve
    a "Let's do this..."
    mc "Oh..."
    a "Put it between my legs."
    scene ch8_674-- with dissolve
    mc "*Hmm..*"
    pause
    scene ch8_675 with dissolve
    mc "Hmm, [a], I thought you forgot about me."
    a "I would never forget about my handsome [arelatmc]."
    mc "I'm so lucky to have you."
    a "We're both lucky, dear."
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_676_atjb_pov3_(trans, st, at):  
        trans.set_child("ch8_676_atjb_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 31:
            store.frame_num = 2
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound 
            atl_play_voice(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_676_atjb_pov1_(trans, st, at):  
        trans.set_child("ch8_676_atjb_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 31:
            store.frame_num = 2
 
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound 
            atl_play_voice(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_676_atjb_pov2_(trans, st, at):  
        trans.set_child("ch8_676_atjb_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 31:
            store.frame_num = 2
 
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound 
            atl_play_voice(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_acum_thjb_pov1_(trans, st, at):  
        trans.set_child("ch8_acum_thjb_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 31:
            store.frame_num = 2
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound 
            atl_play_voice(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   

screen ch8_676_atjb_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.011) style "textbutton_choice"           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_676_atjb_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_676_atjb_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_676_atjb_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_676_atjb_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.011) style "textbutton_choice"               
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_676_atjb_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_676_atjb_pov1_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_676_atjb_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_676_atjb_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.011) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_676_atjb_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_676_atjb_pov2_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_676_atjb_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_acum_thjb_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.011) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_acum_thjb_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
    

label beforech8_676_atjb_pov1_:
    image ch8_676_atjb_pov1_:
        function ch8_676_atjb_pov1_  
    image ch8_676_atjb_pov2_:
        function ch8_676_atjb_pov2_   
    image ch8_676_atjb_pov3_:
        function ch8_676_atjb_pov3_   
    image ch8_acum_thjb_pov1_:
        function ch8_acum_thjb_pov1_
    $ anim_speed = 0.035
    scene ch8_676_atjb_pov3_ with dissolve
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.5
    mc "Hmm, this feels so good."
    mc "I love your legs, [a]."
    mc "You have the sexiest legs in the world."
    a "What do you like more, my breasts or my legs?"
    mc "Wow..."
    mc "That's a very difficult question."
    a "I ask because maybe you prefer me to use my breasts."
    mc "Hmm, your breasts are amazing but your legs deserve some love too."
    pause
    a "So you like my legs more?"
    mc "Every corner of your body I like, it's hard to decide."
    a "*Giggle*"
    $ anim_speed = 0.015
    mc "*Hmngh*"
    mc "Yes, hmmm..."
    pause
    a "Are you close, baby?"
    mc "Not yet, but it feels really good."
    pause
    scene ch8_676_atjb_pov2_ with dissolve
    a "It's getting late."
    a "Although, if you don't mind, neither do I."
    mc "I don't mind at all."
    mc "I'd rather be late for work than{w=0.4}, *Hmngh*{w=0.4}, waste this moment."
    a "*Uhm, uh*"
    a "I won't allow you to be irresponsible."
    mc "I'll be punctual, I promise."
    a "You better be, or you can forget about doing these things with your [arelat]."
    mc "I better arrive early then."
    a "*Giggle*, just kidding."
    pause
    mc "*Hmm*, oh yes..."
    mc "Your body is so soft, [a]... when I see your curves bouncing with my thrusts it makes me turn into an animal."
    mc "And feeling your fluids mixed with mine is a sensation... *hmmm* that has no comparison."
    pause
    mc "I want to repeat this every day."
    mc "All the time."
    scene ch8_676_atjb_pov1_ with dissolve
    pause
    a "Every day is too much."
    mc "Of course not."
    mc "On the contrary, I need more hours in the day to be fully satisfied by you."
    a "We have to be careful, baby."
    mc "I know."
    mc "We will be."
    a "..."
    pause
    a "We'll see..."
    $ anim_speed = 0.013
    mc "*Uhh, argh*, almost there..."
    a "Give it to me hard, baby, give it all to me."
    mc "Y-yes... yes... *Hngh!*"

label ch8_676_atjb_pov3_:
    scene ch8_676_atjb_pov3_ with dissolve
    call screen ch8_676_atjb_pov3_settings
label ch8_676_atjb_pov2_:
    scene ch8_676_atjb_pov2_ with dissolve
    call screen ch8_676_atjb_pov2_settings
label ch8_676_atjb_pov1_:
    scene ch8_676_atjb_pov1_ with dissolve
    call screen ch8_676_atjb_pov1_settings

label afterch8_676_atjb_pov3_:
    scene ch8_676_atjb_pov3_ with dissolve
    $ anim_speed = 0.011
    mc "*Ungh!*"
    mc "[a], I'm going to..."
    a "Yes, baby, give it to me."
    a "Take it all out, honey, don't leave a single drop inside."
    scene ch8_acum_thjb_pov1_ with dissolve
    $ anim_speed = 0.015
    mc "*Hmmngh, nghh, argh!*"
    a "*Ah, uh, hm*, that's it, honey."
    a "Let it out on your [arelat]'s legs."
    call screen ch8_acum_thjb_pov1_settings
label afterch8_acum_thjb_pov1_:
    $ anim_speed = 0.011
    mc "[a], *hmngh!*" with cumming
    a "*Ah, ah, ahm, uh!*"
    stop voicefx fadeout 0.5
    scene ch8_678- with flash
    mc "*Aaargh!*" with flash
    scene ch8_678-- with dissolve
    mc "Uff... uff..."
    mc "Wow, [a]..."
    a "Honey, you stained the couch."
    mc "Oh, sorry... I couldn't think straight."
    mc "I'll clean it up now."
    a "I'll do it honey, don't worry."
    mc "Ufff... I'm exhausted."
    $ renpy.end_replay()
    pause
    scene ch8_679 with dissolve
    mc "[a], I want to repeat this every day."
    a "..."
    pause
    a "Maybe."
    scene ch8_680 with dissolve
    a "Now go to your room, you have something important to do in the morning."
    mc "First tell me how much you liked what we did."
    a "No, baby..."
    mc "I know you loved it."
    a "And why do you ask...?"
    mc "Heh, I just like hearing it from your mouth."
    a "Go to bed now, mister."
    a "You have to rest for tomorrow."
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    scene ch8_681 with dissolve
    mc "I'm going to take all this trash out."
    a "Thank you."
    pause
    scene ch8_682 with dissolve
    a "..."
label ch8stasda:
    scene ch8_682 with dissolve
    mc "It was amazing, [a]."
    scene ch8_683 with dissolve
    mc "I love that everything is like this now."
    pause
    scene ch8_682 with dissolve
    a "Yeah..."
    pause
    mc "What's wrong?"
    pause
    a "I don't know if this is good for us, [mc]."
    scene ch8_683 with dissolve
    a "I know it's a little late to...{w=0.4} think about it again, but..."
    scene ch8_682 with dissolve
    a "It just doesn't feel right."
    mc "It will only be bad if you don't like it."
    pause
    mc "Hm?"
    scene ch8_683 with dissolve
    a "Yeah..."
    a "Now go to sleep, you gluttonous man."
    a "I saw you devouring an entire box of pizza."
    mc "It's my diet."
    a "Yeah, sure..."
    mc "*Laughs*"
    scene ch8_684 with dissolve
    a "Good night, honey, rest well."
    mc "Good night, [a]."
    scene blackscreen with dissolve
    pause
    scene ch8_685 with dissolve
    mc "(Sleeping after a good release is the best.)"
    mc "(I can't believe [a] is finally opening up to me.)"
    mc "(Although it seems like she still has doubts...)"
    pause
    mc "(Little by little...)"
    scene blackscreen with dissolve
    pause
    scene ch8_686 with Fade(1.0,1.0,1.0)
    mc "Uh..." with Fade(0.2,0.2,0.2)
    mc "What time is it?"
    play music scene2
    with hpunch
    mc "Aah! what the hell happened with the alarm?" 
    mc "This fucking phone!"
    scene ch8_687 with fade
    a "[mc], aren't you going to have breakfast?"
    mc "*Glup* I'm running late."
    scene ch8_688 with dissolve
    a "[mc], you can't leave without having breakfast."
    a "Should I warm up some leftovers from dinner?"
    scene ch8_689- with dissolve
    mc "I'm running late!"
    a "Oh!"
    scene ch8_690 with dissolve
    a "At least buy something at the store."
    mc "I think there's a cafeteria at work."
    scene ch8_691 with dissolve
    mc "Goodbye, I love you!"
    a "Take care!"
    a "And good luck at work!"
    a "I-I love you too!"
    a "*Exhales*"
    pause
    scene blackscreen with dissolve

    pause

    scene ch8_699 with dissolve
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} And lunch break is at ten and one o'clock depending on the sector you're working in, but with me it's at that time."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} You can come here or go wherever you want, you'll have thirty minutes and then you'll have to go back to your posts."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} Any questions?"
    scene ch8_698 with dissolve
    "Sorry, where can I check the bus routes again?"
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} There's a big sign in human resources where you can check that out."
    "Thank you."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} Alright, I'll leave for now while the urine tests finish. You can go to the bathroom and do whatever you want."
    scene ch8_700 with dissolve
    pause
    mc "(Ugh, waiting again...)"
    "*Beep*"
label ch8hasd:
    scene ch8_701 with dissolve
    call phone_start from _call_phone_startch812
    call message_start("[k]", "Hey, did you get the job?") from _call_message_startch8
    call reply_message("I'm still in the process. I just finished a general knowledge test and a drug test, though.") from _call_reply_messagech81
    call reply_message("I had to pee in a cup.") from _call_reply_messagech8
    call message("[k]", "You better get that job. I'm tired of always eating burgers when we go out.") from _call_messagech8
    call reply_message("Last time we went out, you had {image=eggplant32}{image=eggplant32}") from _call_reply_message_1ch8
    call message("[k]", "{image=face-with-tongue}{image=face-with-tongue}") from _call_message_1ch8
    call message("[k]", "Idiot.") from _call_message_1ch82321
    call message("[k]", "What are you doing?") from _call_message_1ch82
    call reply_message("Nothing, we're all just waiting.") from _call_reply_message_2ch8
    call reply_message("We've been waiting since morning. We do something and then we have to wait again.") from _call_reply_message_2ch8235
    call reply_message("I'm dying of boredom. What about you?") from _call_reply_message_2ch82
    call message("[k]", "Nothing, I'm in the living room, bored as well.") from _call_message_2ch81313131
    call message("[k]", "{i}{size=-5}Typing...") from _call_message_3ch815144
    call message_img("[k]", " ", "images/scenes/ch8_kpic1.jpg") from _call_message_imgch8
    mc "(Oh.)"
    call reply_message("{image=nauseated-face}") from _call_reply_message_7ch8
    call message("[k]", "Idiot, I'm never sending you anything again.") from _call_message_6ch8
    call reply_message("Joke, I loved it{image=smiling-face-with-heart-eyespng32}{image=smiling-face-with-heart-eyespng32}.") from _call_reply_message_7ch8159
    call reply_message("Are you in the living room?") from _call_reply_message_7ch815900
    call message("[k]", "Yep.") from _call_message_6ch81555101
    call reply_message("You're crazy.") from _call_reply_message_7ch81590
    call message("[k]", "It's just me in the living room and mom's in the kitchen.") from _call_message_6ch815551013577
    call reply_message("Can you send me another one?{image=pleading-face32}{image=pleading-face32}") from _call_reply_message_7ch81599
    call message("[k]", "No.") from _call_message_6ch8155588
    call reply_message("{image=pleading-face}{image=pleading-face}{image=pleading-face}") from _call_reply_message_7ch815995
    call message("[k]", "Deal with it. Also, dad's coming.") from _call_message_6ch81555
    call message("[k]", "I miss you{nw}") from _call_message_6ch81555144
    call message("[k]", "{i}{size=-5}{color=#f3f3f3}This message was deleted") from _call_message_6ch8155514421477
    call message("[k]", "I piss you*") from _call_message_6ch81555144214
    call reply_message("I miss you too{image=smiling-face-with-hearts32}") from _call_reply_message_7ch815995744
    call message("[k]", "You read it!! HAHASASHJAJ") from _call_message_6ch81555144214455
    call message("[k]", "It was the autocorrector's fault") from _call_message_6ch8155514421445574
    call reply_message("I have to go, the instructor is back.") from _call_reply_message_7ch8159957
    call message("[k]", "Good luck.") from _call_message_6ch8155514421445574ASDASD
    call phone_end from _call_phone_endch8
    scene blackscreen with dissolve
    pause
    scene ch8_703 with dissolve
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} And when the trailers arrive, the forklift drivers will do the rest."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} Any more questions?"
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} Great."
    scene ch8_702 with dissolve
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} It's hard work but there are opportunities for growth."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} We're a new warehouse and we're short-staffed in almost all areas, so if you put in effort and learn, you could get a promotion."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} It's up to you."
    scene ch8_703 with dissolve
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} That's all for today. It's almost time to leave."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} You'll be leaving on the morning schedule today, and tomorrow you'll start on the second schedule."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} By the way, today is also a paid day, so you'll receive your full paycheck on payday."
    "{size=+10}{color=#82C200}Instructor:{/color}{/size} Have a good afternoon, see you tomorrow."
    scene blackscreen with dissolve
    pause
    scene ch8_692 with dissolve
    pause
    scene ch8_693 with dissolve
    d "Hey, [mc], how did it go?"
    scene ch8_694 with dissolve
    mc "Good, today we saw some slides on a projector and they gave us a tour of the place."
    mc "I only worked half a day."
    d "I see, so tomorrow the real work begins."
    mc "Yes, tomorrow I'll start working later."
    d "Really?"
    mc "I'll work from seven in the morning to seven in the evening, but then I'll have three days off."
    d "That's a lot of hours."
    mc "Yes, but I prefer having three days off instead of two."
    d "Have you met your boss yet?"
    mc "Yes."
    d "And how was it?"
    mc "I don't know, he didn't seem like a bad person."
    scene ch8_695 with dissolve
    d "One advice, don't let anyone boss you around."
    d "Your dignity comes before anything else."
    d "When I was a laborer in my first job, those who let themselves be manipulated never got anywhere."
    d "Of course you have to work hard, but always show character, autonomy, and leadership. Those are the things that owners look for."
    scene ch8_696 with dissolve
    mc "Thank you for the advice."
    scene ch8_697 with dissolve
    a "[mc], how did it go?"
    a "Did you get the job?"
    mc "Yes, there wasn't even an interview. The hardest part was the drug test."
    a "Drug test?"
    d "Yes, it's something that companies usually do."
    a "I see."
    a "You must be hungry, do you want me to prepare something to eat?"
    mc "Yes, please."
    scene ch8_696 with dissolve
    d "Hey, and..."
    d "If for any reason you don't want to work there anymore because they treat you badly or anything, even if you're just tired, don't worry."
    d "I don't need you to work."
    d "Soon we'll have what we always dreamed of."
    d "As long as I'm here, no one will need to work unless they want to, of course."
    mc "Thank you [drelat] [d], but I'm ashamed of not contributing anything."
    scene ch8_694 with dissolve
    d "That attitude makes me proud."
    d "Still, you know."
    mc "Thank you [drelat] [d], really."
    mc "(Wow...)"
    mc "(This is the man whose wife I'm sleeping with.)"
    mc "(I feel a little bad...)"
    d "And how's the work environment?"
    mc "I don't know yet, we haven't really worked yet. I've only interacted with the new ones."
    mc "I'm going to the kitchen, I'm starving."
    d "Yes, enjoy your meal."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
label ch8a7:
    if _in_replay:
        show screen Replayexit
    play music scene1 fadein 1.5
    scene ch8_704 with fade
    mc "It smells delicious."
    a "It's almost ready."
    pause
    scene ch8_709 with dissolve
    a "You're not here to distract me, right?"
    mc "Distract you? Me?"
    scene ch8_704 with dissolve
    pause 0.2
    scene ch8_705 with dissolve
    mc "I just came to see what I'm going to eat."
    a "I'm reheating the food from earlier, it's ravioli."
    a "Do you want this or something else?"
    scene ch8_706 with dissolve
    mc "Hmm, I feel like something with a little more meat..."
    a "[mc]..."
    pause
    scene ch8_709 with dissolve
    pause 0.2
    scene ch8_708 with dissolve
    a "You said you weren't here to distract me."
    mc "I missed you during work..."
    a "Not now, [mc]."
    mc "{i}Just one kiss."
    scene ch8_712 with dissolve
    pause
    scene ch8_713 with dissolve
    a "Alright, go to the table."
    mc "Lately you smell really good."
    a "[mc]!" with hpunch
    scene ch8_709 with dissolve
    mc "Ok, ok, I'm going already."
    scene ch8_714 with fade
    mc "It looks delicious."
    a "Try it."
    scene ch8_715 with dissolve
    mc "Yup, it tastes just as good as it looks, very tasty."
    mc "{i}Like you."
    a "[mc], stop it."
    a "Well, I'm going now, I'll go clean up my ''room'', it's a mess."
    mc "Hey, I was thinking about coming to your room later."
    a "Hmm..."
    a "Sure."
    mc "Great."
    $ renpy.end_replay()
    pause
    scene ch8_716 with dissolve
    mc "(God...)"
    mc "(That ass has to be mine tonight too.)"
    mc "(I'll visit her tonight, I have nothing to lose by trying.)"
    pause
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
label ch8a8:
    if _in_replay:
        show screen Replayexit
    play music scene2 fadein 1.5
    scene ch8_717 with dissolve
    mc "[a], can I come in?"
    a "Yes."
    scene ch8_718 with dissolve
    mc "Making your bed?"
    a "Yes, my ''bed''."
    scene ch8_719 with dissolve
    a "So, how was your first day at work?"
    mc "We didn't do much today. They gave us a general explanation of everything and showed us around the facilities. We only worked half a day. In the end, we moved some barrels, but that's it."
    a "Barrels?"
    mc "Yes, my job basically consists of moving barrels. The forklift operator brings them, and we move and secure them in groups."
    a "Sounds like hard work."
    mc "Yes, it really is."
    a "You must be tired."
    mc "Yes, but I'll get used to it."
    scene ch8_723 with dissolve
    a "Oh, my poor baby."
    a "Come here with [arelat] [a]."
    scene ch8_724-in with dissolve
    mc "*Laughs* Stop treating me like a child, [a]."
    a "You'll always be my baby, [mc]."
    scene ch8_725-in with dissolve
    a "Even when you're 50 years old, you'll still be my baby."
    mc "But I have a job now."
    scene ch8_727 with dissolve
    a "I don't care."
    mc "That's not fair."
    a "That's life, baby."
    mc "Ouch, that hurts a little."
    scene ch8_728 with dissolve
    a "Did you hurt yourself at work?"
    mc "It was due to bad technique when moving the barrels. I was pressing them against me to lift them instead of just rolling them slowly."
    image ch8_729anim:
        "ch8_729-in" with Dissolve(0.5)
        1.0
        "ch8_730-in" with Dissolve(0.5)
        1.0
        repeat
    scene ch8_729anim with dissolve
    a "Does it hurt here?"
    mc "Yes, right there."
    mc "But it doesn't really hurt, it's just like..."
    a "Pain?"
    mc "Yeah, *laughs*"
    mc "It doesn't hurt that much."
    scene ch8_728 with dissolve
    a "*Sighs*, Even though I try deny it, my boy is already a man."
    mc "Yes, I think you've lost your boy, but look on the bright side. Now you have your man."
    scene ch8_727 with dissolve
    a "Oh..."
    a "That's true, I hadn't thought about it that way."
    scene ch8_728 with dissolve
    a "But I'll still be in denial."
    scene ch8_726 with dissolve
    mc "(Although looking at these breasts makes me want to be breastfed like a baby.)"
    mc "There's a theory that says men never stop being children; we just become more obedient."
    a "I support that theory."
    pause
    scene ch8_731 with dissolve
    a "Do you want me to apply ointment?"
    mc "It's not necessary. Just the massage is making me feel better."
    a "At least let me check it."
    scene ch8_732 with dissolve
    pause
    scene ch8_733 with dissolve
    a "I don't want you to go to work injured."
    mc "I'm not injured, just a little sore."
    stop music fadeout 2.0
    scene ch8_736 with dissolve
    a "{i}{size=-5}Oh..."
    pause
    play music sexy3 fadein 2.0
    a "I-I'm going to check it to be sure."
    scene ch8_735 with dissolve
    pause
    scene ch8_737 with dissolve
    pause
    a "..."
    scene ch8_738 with dissolve
    pause
    scene ch8_740 with dissolve
    a "..."
    pause
    mc "Hmm..."
    scene ch8_742 with dissolve
    a "Ahem..."
    pause
    scene ch8_739 with dissolve
    a "..."
    pause
    scene ch8_741 with dissolve
    a "..."
    image ch8_738anim:
        "ch8_738" with Dissolve(0.3)
        1.5
        "ch8_740" with Dissolve(0.3)
        1.5
        repeat
    scene ch8_738anim with dissolve
    pause
    mc "Hmm..."
    a "..."
    pause
    scene ch8_734 with dissolve
    pause
    scene ch8_744 with dissolve
    mc "*Hmmn*"
    a "Ah..."
    pause
    scene ch8_743 with dissolve
    a "Ahem, I need to lift your shirt."
    pause
    image ch8_745anim:
        "ch8_745" with Dissolve(0.3)
        1.25
        "ch8_746" with Dissolve(0.3)
        1.25
        repeat
    scene ch8_745anim with dissolve
    a "It doesn't seem like you have anything wrong."
    a "Just these defined abs..."
    mc "I told you."
    mc "But the massage feels good..."
    pause
    scene ch8_749 with dissolve
    a "How do you get abs like these?"
    a "They're rock-solid, wow..."
    mc "(And soon something else will be rock-solid too.)"
    scene ch8_750 with dissolve
    a "Oh..."
    a "..."
    pause
    scene ch8_751 with dissolve
    a "[mc]..."
    mc "*Hmph, smph*"
    pause
    scene ch8_752 with dissolve
    mc "*Smph, hmmm*"
    a "*Oh, hmm*, dear..."
    pause
    scene ch8_753 with dissolve
    pause 0.5
    scene ch8_752 with dissolve
    a "Hmm..."
    pause
    scene ch8_753 with dissolve
    pause
    scene ch8_752 with dissolve
    a "Uh..."
    pause
    scene ch8_754 with dissolve
    mc "Hmm, [a]."
    pause
    scene ch8_755 with dissolve
    mc "I love your breasts, [a]."
    mc "I need to see them naked."
    pause
    scene ch8_756 with dissolve
    mc "Hmm..."
    pause
    scene ch8_759 with dissolve
    mc "It's only fair if I show you something too."
    a "What are you going to show me?"
    scene ch8_757 with dissolve
    a "Oh!..."
    pause
    a "You have an erection..."
    mc "Yeah..."
    a "..."
    a "Do you want me to...?"
    mc "If you want to..."
    scene ch8_758 with dissolve
    mc "(She almost didn't hesitate to grab it.)"
    pause

init python:
    store.last_played_sound = None
    def ch8_ahj_pov1_(trans, st, at):  
        trans.set_child("ch8_ahj_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    store.last_played_sound = None
    def ch8_ahj_pov2_(trans, st, at):  
        trans.set_child("ch8_ahj_pov2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    store.last_played_sound = None
    def ch8_ahj_pov3_(trans, st, at):  
        trans.set_child("ch8_ahj_pov3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    store.last_played_sound = None
    def ch8_ahj_pov4_(trans, st, at):  
        trans.set_child("ch8_ahj_pov4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value     
screen ch8_ahj_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
     
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("labelafterch8_ahj_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_ahj_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_ahj_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_ahj_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_ahj_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
           
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("labelafterch8_ahj_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_ahj_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_ahj_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_ahj_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_ahj_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"  
      
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("labelafterch8_ahj_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_ahj_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_ahj_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_ahj_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_ahj_pov4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"             
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("labelafterch8_ahj_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_ahj_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_ahj_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_ahj_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"




label beforech8_ahj_pov4:
    image ch8_ahj_pov1_:
        function ch8_ahj_pov1_
    image ch8_ahj_pov2_:
        function ch8_ahj_pov2_
    image ch8_ahj_pov3_:
        function ch8_ahj_pov3_
    image ch8_ahj_pov4_:
        function ch8_ahj_pov4_
    $ anim_speed = 0.06
    scene ch8_ahj_pov1_ with dissolve
    pause
    mc "Wow, [a]..."
    a "..."
    a "You'll feel better if I take care of this huge erection for you."
    mc "Yeah, I'll definitely feel better if you do that..."
    a "..."
    mc "*Uhm*, That feels good..."
    scene ch8_ahj_pov4_ with dissolve
    pause
    a "Y-you're very...{w=0.4} virile..."
    mc "*Hmnch*{w=0.4}, What do you mean?"
    a "..."
    a "You get erections very easily."
    mc "Yeah..."
    mc "But that's partly because of you."
    image ch8_759anim:
        "ch8_759" with Dissolve(0.2)
        1.0
        "ch8_760" with Dissolve(0.2)
        1.0
        repeat
    scene ch8_759anim with dissolve
    a "Is it because you find me very attractive?"
    mc "You already know that, I don't know why you're asking me."
    mc "But I'll tell you as many times as you want."
    mc "You're too sexy, [a], I find you much more than just attractive."
    mc "When I see you, all I can feel is desire..."
    a "Oh... thank you."
    pause
    scene ch8_ahj_pov3_ with dissolve
    pause
    a "{i}Oh my God, you're so big..."
    a "..."
    a "{i}{size=-5}So thick..."
    a "You must have made many girls happy..."
    a "{i}{size=-5}God, what am I saying?"
    mc "It's not like that."
    mc "I've only had a few girlfriends in my life."
    a "Sorry, that was an inappropriate question, heh..."
    pause
    scene ch8_ahj_pov2_ with dissolve
    pause
    a "{i}*Ah..*, Don't suck so hard, baby."
    pause
    mc "It's been a while since you called me baby."
    a "Yeah... you stopped liking it when I called you that in front of your high school friends."
    mc "Yes, *laughs*."
    a "..."
    a "{i}Are you close yet, honey?"
    mc "Not yet."

label ch8_ahj_pov1_:
    scene ch8_ahj_pov1_ with dissolve
    call screen ch8_ahj_pov1_settings with dissolve
label ch8_ahj_pov2_:
    scene ch8_ahj_pov2_ with dissolve
    call screen ch8_ahj_pov2_settings with dissolve
label ch8_ahj_pov3_:
    scene ch8_ahj_pov3_ with dissolve
    call screen ch8_ahj_pov3_settings with dissolve
label ch8_ahj_pov4_:
    scene ch8_ahj_pov4_ with dissolve
    call screen ch8_ahj_pov4_settings with dissolve

label labelafterch8_ahj_pov3_:
    stop music fadeout 2.0
    scene ch8_759anim with dissolve
    mc "[a], I don't want to cum just by this."
    mc "I can't waste this alone time with you."
    a "What do you want to do?"
    play music sexy3 fadein 1.5
    scene ch8_720 with dissolve
    mc "I'd like to repeat what we did last night."
    mc "I really liked it."
    mc "You did too, right?"
    a "Y-yeah..."
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.5
    scene ch8_721 with dissolve
    a "*Hmnch*"
    pause
    stop sound fadeout 0.5
    scene ch8_722 with dissolve
    a "We're not going any further than that."
    mc "I know."
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.5
    scene ch8_762 with fade
    pause
    scene ch8_763 with dissolve
    mc "Take off your blouse."
    a "*Hmnch, hmm*"
    pause
    scene ch8_764 with dissolve
    mc "Take it all off."
    mc "I want to see your naked body."
    pause
    scene ch8_765 with dissolve
    a "No, {w=0.4}*Hmnch*{w=0.4}, leave the panties on."
    pause
    scene ch8_766 with dissolve
    a "Ah... *Hmnch, mlmh*"
    pause
    image ch8_765anim:
        "ch8_766" with Dissolve(0.5)
        1.0
        "ch8_767" with Dissolve(0.5)
        1.0
        repeat
    scene ch8_765anim with dissolve
    a "*Hmnch* Oh, [mc]."
    mc "*Hmnch*"
    pause
    scene ch8_773 with dissolve
    pause
    stop sound fadeout 0.5
    scene ch8_772 with dissolve
    a "*Haah...*"
    scene ch8_774 with dissolve
    a "Oh, [mc], what are we doing?"
    a "Is it too late to back out?"
    mc "It is."
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.5
    scene ch8_773 with dissolve
    pause
    scene ch8_768 with dissolve
    a "I can't believe we're doing this again."
    mc "We can't help it, [arelat] [a]."
    scene ch8_769 with dissolve
    a "[mc]..."
    a "..."
    pause
    scene ch8_771 with dissolve
    mc "*Hmm..*"
    pause
    stop sound fadeout 0.5
    scene ch8_774 with dissolve
    a "[mc], I didn't said you can do that..."
    mc "Sorry, I just..."
    a "I'll let it slide this time."
    scene ch8_775 with dissolve
    a "Hmm..."
    scene ch8_771 with dissolve
    pause 0.2
    scene ch8_770 with dissolve
    pause
    scene ch8_770- with dissolve
    a "*Uh!*, naughty..."
    mc "God... your ass is so perfect, [arelat] [a]."
    mc "I was dying to squeeze your bare butt again, you have no idea."
    pause
    scene ch8_776 with dissolve
    a "I could imagine it."
    a "You never miss an opportunity to look at my behind whenever you can."
    a "And lately you've been a bit... touchy-feely."
    mc "[arelat!cl] [a], if you talk to me like that..."
    scene ch8_775 with dissolve
    a "Ah..."
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.1
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_athjob_1_pov1_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value      
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_athjob_1_pov2_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value       
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_athjob_1_pov3_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value      
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_athjob_1_pov4_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_athjob_1_pov5_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.last_played_sound4 = None
    def ch8_athjob_1_pov6_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov6_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.last_played_sound4 = None
    def ch8_athjob_1_pov7_(trans, st, at):  
        trans.set_child("ch8_athjob_1_pov7_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         
screen ch8_athjob_1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 5" action Jump("ch8_athjob_1_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 6" action Jump("ch8_athjob_1_pov6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 7" action Jump("ch8_athjob_1_pov7_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_athjob_1_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 5" action Jump("ch8_athjob_1_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 6" action Jump("ch8_athjob_1_pov6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 7" action Jump("ch8_athjob_1_pov7_") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_athjob_1_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 5" action Jump("ch8_athjob_1_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 6" action Jump("ch8_athjob_1_pov6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 7" action Jump("ch8_athjob_1_pov7_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_athjob_1_pov4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 5" action Jump("ch8_athjob_1_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 6" action Jump("ch8_athjob_1_pov6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 7" action Jump("ch8_athjob_1_pov7_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_athjob_1_pov5_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 6" action Jump("ch8_athjob_1_pov6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 7" action Jump("ch8_athjob_1_pov7_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_athjob_1_pov6_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch8_athjob_1_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 7" action Jump("ch8_athjob_1_pov7_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_athjob_1_pov7_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch8_athjob_1_pov5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch8_athjob_1_pov6_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label beforech8_athjob_1_pov1_:
    image ch8_athjob_1_pov1_:
        function ch8_athjob_1_pov1_
    image ch8_athjob_1_pov2_:
        function ch8_athjob_1_pov2_
    image ch8_athjob_1_pov3_:
        function ch8_athjob_1_pov3_
    image ch8_athjob_1_pov4_:
        function ch8_athjob_1_pov4_
    image ch8_athjob_1_pov5_:
        function ch8_athjob_1_pov5_
    image ch8_athjob_1_pov6_:
        function ch8_athjob_1_pov6_
    image ch8_athjob_1_pov7_:
        function ch8_athjob_1_pov7_
    $ anim_speed = 0.05
    scene ch8_athjob_1_pov5_ with dissolve 
    a "[mc]..."
    mc "Don't ask me to control myself if you talk to me so sexy, [a]."
    a "*Hmnch, smnch*{w=0.4}, so it's my fault again?"
    mc "You know how I am, I can't resist you, especially if you provoke me." 
    mc "Yeah, squeeze me tight with your legs, [a]."
    a "Like this?"
    mc "Yeah.."
    pause
    scene ch8_athjob_1_pov7_ with dissolve
    mc "Hmhm, [a]..."
    mc "You're so wet down there."
    a "A-am I?"
    mc "Yeah..."
    a "..."
    mc "You're so sexy, [a]."
    mc "To feel your naked body rubbing against mine is an experience like no other."
    a "Oh, dear..."
    pause
    a "Thanks..."
    pause
    scene ch8_athjob_1_pov1_ with dissolve
    a "You understand we can't do this all the time, right?"
    mc "Why not?"
    a "I'm your [arelat], [mc]."
    mc "But you want it too, [a]."
    a "That doesn't matter..."
    pause
    scene ch8_athjob_1_pov3_ with dissolve
    a "*Hmnch*, baby, your penis... it feels..."
    mc "Tell me how much you like this, [a]."
    a "[mc]..."
    a "W-we cannot get carried away."
    $ anim_speed = 0.035
    a "*Uh, hmm, hmm.*"
    pause
    scene ch8_athjob_1_pov2_ with dissolve
    a "Darling{w=0.4}, *hmm..*{w=0.4}, this is dangerous."
    mc "It can't be heard from outside, calm down."
    a "*Uh*{w=0.4}, It's not that.."
    mc "Relax, nobody is going to discover us."
    a "No, no... I mean us, your penis is too close..."
    a "You're too close to...{w=0.5} me."
    scene ch8_athjob_1_pov4_ with dissolve
    mc "*lahmmn*{w=0.4}, I won't do anything you don't want, [a]."
    a "*Huh*, Okay..."
    mc "(The Ol' Reliable.)"
    a "Just don't forget I'm your [arelat]."
    mc "Yeah."
    mc "My beautiful and sexy [arelat]."
    a "..."
    pause
    scene ch8_athjob_1_pov6_ with dissolve
    a "I know you don't care that I'm your [arelat] but..."
    a "Huh, huh{w=0.4}, but I do care, a-and I care a lot."
    mc "(She says that when we're both rubbing each other's naked bodies...)"
    pause
label ch8_athjob_1_pov1_:
    scene ch8_athjob_1_pov1_ with dissolve
    call screen ch8_athjob_1_pov1_settings with dissolve
label ch8_athjob_1_pov2_:
    scene ch8_athjob_1_pov2_ with dissolve
    call screen ch8_athjob_1_pov2_settings with dissolve
label ch8_athjob_1_pov3_:
    scene ch8_athjob_1_pov3_ with dissolve
    call screen ch8_athjob_1_pov3_settings with dissolve
label ch8_athjob_1_pov4_:
    scene ch8_athjob_1_pov4_ with dissolve
    call screen ch8_athjob_1_pov4_settings with dissolve
label ch8_athjob_1_pov5_:
    scene ch8_athjob_1_pov5_ with dissolve
    call screen ch8_athjob_1_pov5_settings with dissolve
label ch8_athjob_1_pov6_:
    scene ch8_athjob_1_pov6_ with dissolve
    call screen ch8_athjob_1_pov6_settings with dissolve
label ch8_athjob_1_pov7_:
    scene ch8_athjob_1_pov7_ with dissolve
    call screen ch8_athjob_1_pov7_settings with dissolve


label afterch8_athjob_1_pov1_label:
    $ anim_speed = 0.01
    a "*Uh, huh, huh*, baby, we're making too much noise."
    mc "I can't stop...{w=0.4} I'm going to cum, *Hmh*...{w=0.4} *Ngh*."
    a "That's it, baby..."
    a "Let it out, honey..."
    mc "*Hah*, [a]...{w=0.4} N-no{w=0.4}, *hngh!..."
    $ anim_speed = 0.015
    pause 0.5
    $ anim_speed = 0.025
    pause 0.5
    $ anim_speed = 0.035
    mc "Huh, [a]..."
    mc "I don't want it to end yet."
    pause

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aprub_pov1_(trans, st, at):  
        trans.set_child("ch8_aprub_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
    
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aprub_pov2_(trans, st, at):  
        trans.set_child("ch8_aprub_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
    
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aprub_pov3_(trans, st, at):  
        trans.set_child("ch8_aprub_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 28:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking7.ogg", "audio/sex/fucking4.ogg", "audio/sex/fucking8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 8:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 23:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)() 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
    

screen ch8_aprub_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

screen ch8_aprub_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

screen ch8_aprub_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"    
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.012) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_athjob_1_pov1_label") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch8_athjob_1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_athjob_1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_athjob_1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_athjob_1_pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label labelbeforech8_aprub_pov1_:
    image ch8_aprub_pov1_:
        function ch8_aprub_pov1_
    image ch8_aprub_pov2_:
        function ch8_aprub_pov2_
    image ch8_aprub_pov3_:
        function ch8_aprub_pov3_
    
    scene ch8_aprub_pov2_ with dissolve
    a "*Hmmnch, uh, uh,* [mc].."
    mc "Are you enjoying it, [a]?"
    pause
    a "Yeah..."
    pause
    mc "Tell me how much, [a]."
    a "..."
    pause
    scene ch8_aprub_pov1_ with dissolve
    a "*Huh, ah, uh*"
    mc "*Hngh*, [a], I love you so much."
    a "I love you too, honey."
    pause
    $ anim_speed = 0.02
    scene ch8_aprub_pov3_ with dissolve
    pause
    mc "*Hah, ngh!*, I'm close."
    a "Cum for me, baby, don't hold back..."
    $ anim_speed = 0.012
    mc "Y-yes, *ahh..*"
    mc "*Huh.. hnghm!*"
    a "*Hah, ah!*, baby..."
    mc "Do you like it fast?"
    a "Yes, baby, keep doing it fast."
    scene ch8_793 with dissolve
    pause 0.5
    scene ch8_792 with cumming
    mc "Argh!!" with flash
    pause
    scene ch8_793 with dissolve
    pause
    image ch8_777anim_:
        "ch8_777" with Dissolve(0.3)
        0.4
        "ch8_778" with Dissolve(0.3)
        0.4
        repeat
    scene ch8_777anim_ with dissolve
    mc "(I just exploded between her legs.)"
    mc "(I can feel her vagina all wet...)"
    pause
    mc "I knew sooner or later you would be mine, [a]."
    a "N-no{w=0.4}, *mmlhm*{w=0.4}, I'm not yours, [mc]"
    a "I'm still your [arelat]."
    mc "*Hngh!!*{w=0.4}, if you weren't your [arelatmc], you would have been mine for a long time."
    stop sound fadeout 0.5
    stop music fadeout 0.5
    play sound "audio/knockdoor.mp3" volume 0.5 fadein 0.5
    scene ch8_779 with dissolve
    a "*Sigh*"
    a "{i}Did you hear that?"
    mc "{i}Hear what?"
    a "{i}Someone knocked on the door."
    scene ch8_780
    d "[a], I was thinking it's a bit unfair that you always sleep on the couch."
    scene ch8_781 with dissolve
    d "I'll sleep-...{w=0.4} uh... {w=1.0}Huh?!"
    scene blackscreen with Dissolve(2.5)
    mc "(Shit!)"
    pause
    play music something
    scene ch8_782 with Dissolve(0.1)
    d "You should put the lock on the door if you're going to...{w=0.4} do that."
    d "Can I come in?"
    a "No!{w=1.0} no..." with hpunch
    a "Close the door."
    d "I just want to talk."
    a "I have nothing to talk to you about, now leave."
    show ch8_783 with dissolve:
        xalign 0.5 yalign 1.0
        ease 10 zoom 0.75
    d "Good night, [a]."
    d "I look forward to the day you want to fix things."
    a "Go away, [d]."
    d "..."
    show ch8_783-- with dissolve:
        zoom 0.75
    pause
    scene ch8_784 with fade
    mc "{i}Is he gone already?"
    a "God, [mc]..."
    pause
    scene ch8_785 with dissolve
    a "Jesus, what would have happened if he saw us doing that?"
    a "Go to your room {w=0.5}{nw}"
    a "No, wait for a while, he might see you leaving."
    a "But what if he decides to look for you right now and can't find you anywhere?"
    mc "Relax, [a]."
    mc "You're being a bit extreme."
    mc "If he doesn't find me at home, he'll think I went to some party or something."
    scene ch8_786 with dissolve
    a "My heart almost came out of my chest, [mc]."
    mc "Mine too."
    mc "How could we forget to lock the door?"
    a "I don't know, my mind was a bit foggy..."
    mc "We'll be more careful next time."
    a "[mc], there won't be a next time."
    stop music fadeout 3.0
    scene ch8_787 with dissolve
    mc "No, no, [a]."
    mc "You can't be serious, can you?"
    mc "You can't, [a]..."
    a "Maybe this is a sign that we need to stop, [mc]."
    mc "No, it is not, [a]."
    mc "We just..."
    play music sexy1 fadein 3.0
    scene ch8_790 with dissolve
    a "[mc]..."
    pause
    scene ch8_791 with dissolve
    a "[mc], wait."
    pause
    scene ch8_794 with dissolve
    mc "[a], hmmm... I want to devour you whole body."
    a "[d] just almost caught us, [mc]!"
    mc "(And that made me horny even more...)"
    pause
    scene ch8_795 with dissolve
    mc "I desire you like nobody else..."
    a "No, dear."
    mc "Just let yourself be loved, [a]."
    scene ch8_796 with dissolve
    mc "How beautiful..."
    pause
    scene ch8_797 with dissolve
    a "No, [mc]..."
    a "..."
    pause
    mc "You need it, [a]."
    mc "Let me do it."
    a "You're my [arelatmc]..."
    mc "You deserve someone to take care of these desires."
    mc "Let me be that person, [a]."
    scene ch8_798 with dissolve
    mc "I'll satisfy your needs as a woman from now on."
    a "The boundaries, [mc]..."
    scene ch8_800 with dissolve
    a "Oh, [mc], *ah..*, no..."
    a "Remember{w=0.4}, *Ah*{w=0.4}, the boundaries..."
    scene ch8_801 with dissolve
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.5
    a "*Oh, god... *hah, ah*, [mc]..."
    pause
    scene ch8_802 with dissolve
    a "*Hmm, ah...*"
    pause

init python:
    def ch8_acun1_pov1_(trans, st, at):  
        trans.set_child("ch8_acun1_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    def ch8_acun1_pov2_(trans, st, at):  
        trans.set_child("ch8_acun1_pov2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value         
init python:
    def ch8_acun1_pov3_(trans, st, at):  
        trans.set_child("ch8_acun1_pov3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

screen ch8_acun1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_acun1_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_acun1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_acun1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_acun1_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_acun1_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_acun1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_acun1_pov3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_acun1_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_acun1_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_acun1_pov1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_acun1_pov2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"






label beforech8_acun1_pov1_1:
    image ch8_acun1_pov1_:
        function ch8_acun1_pov1_
    image ch8_acun1_pov2_:
        function ch8_acun1_pov2_
    image ch8_acun1_pov3_:
        function ch8_acun1_pov3_
    image ch8_806anim:
        "ch8_806" with Dissolve(0.2)
        0.75
        "ch8_807" with Dissolve(0.2)
        0.75
        repeat
    $ anim_speed = 0.05
    scene ch8_acun1_pov1_ with dissolve
    a "*Ah, hmm*{w=0.4}, remember the limits, [mc]..."
    a "*Oh.. hmmhmm, ahh*"
    pause
    scene ch8_806anim with dissolve
    mc "(It feels so delicious and soft...)"
    mc "(She even shaved...)"
    pause
    mc "(She probably did it because she knew this could happen.)"
    mc "('Remember the limits', 'this can't happen', she's talking to herself, not to me.)"
    scene ch8_acun1_pov2_ with dissolve
    $ anim_speed = 0.035
    mc "(Because even though I'm her [arelatmc], she melts for me.)"
    a "*Ah, hmhmm*"
    a "*Hmmhm, uhh*, baby, I'm going to..."
    a "*Hmmhm*, oh god..."
    mc "Do it, [a]."
    pause
    scene ch8_acun1_pov3_ with dissolve
    a "Oh, god... *Hmmhhmm*"
    a "Darling, this is so wrong..."
    $ anim_speed = 0.015
    a "[mc]!..."
    a "Oh, god... *Hmmhm*, *Ahh*"

label afterch8_acun1_pov1_:
    a "-[mc]!"
    stop voicefx fadeout 0.5
    play voicefx "audio/wavs/a/amoanhard_1.ogg" volume 0.5
    scene ch8_805 with cumming
    a "*Hmnhmm!" with flash
    scene ch8_804 with dissolve
    a "*Uhhmmmhm!"
    pause
    scene ch8_805 with dissolve
    a "Uh...{w=0.4} [mc]...{w=1.0} that was..."
    pause
    scene ch8_809 with dissolve
    a "Uhh... uh..."
    pause
    scene ch8_808 with dissolve
    a "Oh, god..."
    a "Huh..."
    pause
    scene ch8_810 with dissolve
    mc "You came hard again."
    a "Y-yeah.."
    a "I had forgotten how good that felt."
    a "Ermm..."
    pause
    play sound "audio/wavs/sfx/kissing_1.ogg" volume 0.5
    scene ch8_811 with dissolve
    pause
    stop sound fadeout 0.5
    scene ch8_812 with dissolve
    mc "Good night."
    a "..."
    scene ch8_813 with dissolve
    pause
    scene ch8_812 with dissolve
    a "..."
    pause
    play sound "audio/wavs/sfx/kissing_1.ogg" volume 0.5
    scene ch8_811 with dissolve
    a "*Smnch*"
    scene ch8_813 with dissolve
    stop sound fadeout 0.5
    a "Go to your room now, you have work tomorrow."
    a "I don't want you to be late because of me."
    mc "Good night, [a]."
    a "Rest well, dear."
    $ renpy.end_replay()
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    scene ch8_814 with Dissolve(2.0)
    scene blackscreen with dissolve
    scene ch8_814 with dissolve
    mc "Shit, I'm late again."
    play music scene1 fadein 1.0
    scene ch8_816 with dissolve
    a "Good morning."
    mc "Good morning, [a]."
    a "Do you have time for breakfast?"
    mc "No, I'm late again."
    a "It's barely six o'clock."
    mc "I start at seven and I have to get there early."
    scene ch8_817 with dissolve
    a "Do you want me to drive you there?"
    mc "No need, I'll wait for the bus."
label ch8a9:
    if _in_replay:
        show screen Replayexit
        scene ch8_817 with dissolve
        play music scene1 fadein 1.0
    a "Don't tell me you're just going to eat that apple."
    mc "I'll eat something there."
    scene ch8_818 with dissolve
    a "Luckily for you, your [arelat] [a] prepared something for you to take."
    mc "Oh, thank you."
    scene ch8_819 with dissolve
    mc "..."
    pause
    scene ch8_819- with dissolve
    mc "Thanks."
    mc "..."
    pause
    scene ch8_820 with dissolve
    a "Hey! Don't you forget something?"
    mc "Uh, did I forget something?"
    scene ch8_821 with dissolve
    a "Don't you feel like something's missing?"
    mc "Uh..."
    pause
    a "My good morning kiss?"
    scene ch8_822 with dissolve
    play voicefx "audio/wavs/sfx/kissing_1.ogg" volume 0.15 loop
    mc "Right, how could I forget!"
    mc "I can't leave without giving my beautiful [arelat] [a] a good morning kiss."
    scene ch8_823 with dissolve
    a "*Hmnhmm*"
    pause
    image ch8_824anim:
        "ch8_825" with Dissolve(0.5)
        1.0
        "ch8_824" with Dissolve(0.5)
        1.0
        repeat
    scene ch8_824 with dissolve
    a "Hmmnch*"
    scene ch8_824anim with dissolve
    mc "*Hmnh!*, [a]."
    a "*Mhmh, hmhhm*"
    pause
    scene ch8_826 with dissolve
    pause
    scene ch8_827 with dissolve
    pause
    scene ch8_828 with dissolve
    a "*Hmnhmm*, *giggle*, wait [mc]."
    pause
    stop voicefx fadeout 0.5
    scene ch8_830 with dissolve
    mc "[a], I wasn't expecting that."
    a "Hmm..."
    scene ch8_831 with dissolve
    a "You'll be late."
    mc "Ah, I need to go!"
    scene ch8_832 with dissolve
    mc "See you later, love you!"
    a "Take care."
    scene ch8_833 with dissolve
    a "I love you too!"
    pause
    a "Eh!"
    a "You forgot your lunch!"
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 1.5
    scene ch8_834 with dissolve
    noah "Does that one leak too?"
    mc "Yeah."
    scene ch8_835 with dissolve
    noah "Uhh, my fucking back..."
    noah "This shit should be done by the forklift drivers, not us."
    noah "Do you mind if I go to the bathroom?"
    mc "No, don't worry."
    mc "Besides, it's break time in a minute."
    scene ch8_836 with dissolve
    mc "Uh... (How boring...)"
    stop music fadeout 1.5
    "*Beep, beep*"
    play music scene1 fadein 1.0
label ch8_phonemsg_a2:
    call phone_start from _call_phone_startch8
    call message_start("[a]", "Honey, you forgot your lunch.") from _call_message_startch8_a2_
    call reply_message("No wonder I felt like I was forgetting something on my way to work.") from _call_reply_messagecha2_1
    call message_img("[a]", " ", "images/scenes/ch8_apic2in_phone.jpg") from _call_message_imgch8pollo
    call reply_message("Oh...") from _call_reply_messagecha2_2
    call reply_message("It looks very appetizing{image=pleading-face32}{image=pleading-face32}") from _call_reply_messagecha2_3
    call message("[a]", "How do you know? The lunchbox wasn't even open in the picture.") from _call_messagech8_a2_1
    call reply_message("{image=kissing-face-with-closed-eyes}{image=kissing-face-with-closed-eyes}{image=kissing-face-with-closed-eyes}") from _call_reply_messagecha2_4
    call message("[a]", "You naughty boy...{image=face-with-hand-over-mouth32}{image=face-with-hand-over-mouth32}") from _call_messagech8_a2_5
    call message("[a]","{i}{size=-5}Typing...") from _call_messagech8_a2_6
    call message_img("[a]", "A picture without the lid{image=face-blowing-a-kiss32}{image=face-blowing-a-kiss32}", "images/scenes/ch8_apic4in_phone.jpg") from _call_message_imgch8pollo2
    $ renpy.pause(0.5, hard=True)
    call message("[a]","{i}{size=-5}{color=#f3f3f3}This message was deleted.") from _call_messagech8_a2_7
    mc "(What was that? I didn't get to see it.)"
    mc "(Did she send me a picture of the lunchbox?)"
    call reply_message("What was that?") from _call_reply_messagecha2_5
    call message("[a]","Nothing, honey, I sent something by mistake{image=face-with-hand-over-mouth32}{image=face-with-hand-over-mouth32}") from _call_messagech8_a2_8
    call message("[a]","Well, I'll let you work, you must be busy.") from _call_messagech8_a2_9
    call reply_message("It's almost my break time, I'll message you in a bit.") from _call_reply_messagecha2_6
    call message("[a]","Okay baby {image=face-blowing-a-kiss32}{image=face-blowing-a-kiss32}") from _call_messagech8_a2_10
    mc "(What did she send a moment ago?)"
    mc "(Wait, it might have been saved in the gallery...)"
    call phone_end from _call_phone_endch8_a2_
    show ch8_apic4in with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 0.5
        ease 3 yalign 1.0
        ease 3 yalign 0.7 zoom 0.42
    mc "Whoa..."
    mc "(Did she really send me this?)"
    mc "([a] has changed a lot since that day on the yacht...)"
    mc "(I'm going to save it.)"
    noah "Talking to your girlfriend?"
    play music scene2
    scene ch8_837 with hpunch
    mc "Y-yeah, something like that, haha."
    noah "It's break time, buddy."
    noah "Shall we go to the cafeteria or what?"
    mc "Let's go."
    $ renpy.end_replay()
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 2.0
    scene ch8_838 with dissolve
    s "I don't like seafood."
    d "They make all kinds of dishes at that restaurant, not just seafood."
    s "The restaurants you take us to are always so boring."
    s "Why don't we ever do what I like?"
    k "You only like pizza."
    s "Pizza is good."
    k "To be fair, [s] has a point."
    k "You always take us to places that only you like."
    scene ch8_841 with dissolve
    d "[mc], it's great that you're here, can you decide where we'll go please?"
    mc "Are we going out?"
    scene ch8_839 with dissolve
    k "What do you prefer, pizza or restaurant near the beach?"
    scene ch8_840 with dissolve
    s "You prefer pizza, right!?"
    mc "Uh..."
    scene ch8_841 with dissolve
    mc "Pizza or restaurant?"
    mc "I actually prefer tacos."
    d "Oh, no..."
    k "Ushh..."
    mc "Just kidding."
    scene ch8_840 with dissolve
    mc "Erm..."
    mc "I'm a little tired of pizza."
    scene ch8_842 with dissolve
    s "No, [mc]..."
    scene ch8_843 with dissolve
    mc "I'll take you out for pizza another day, okay?"
    s "No."
    mc "No?"
    s "Take me to the fair, remember you promised?"
    s "And now you have money, you have no excuse."
    mc "Right, I'll take you."
    s "Just me, right?"
    s "[k] won't come with us."
    mc "Yes, it'll just be you and me."
    s "Promise me."
    mc "I promise."
    s "Promise me you'll promise."
    mc "Yes, [s:.5], I promise."
    scene ch8_844 with dissolve
    d "Great, tonight we'll celebrate your first payment at your first job."
    d "And what better way than you paying for dinner."
    mc "Huh? Sure..."
    d "Just kidding."
    d "You're off tomorrow, right?"
    s "[mc].{w=0.4}{nw}"
    mc "Yeah, I'm not working tomorrow, until Monday."
    d "Great."
    d "They serve some amazing cocktails and-"
    scene ch8_845 with dissolve
    a "[mc], are you hungry?"
    d "We're going out to dinner, don't you remember?"
    d "You said you'd come... to celebrate with us."
    scene ch8_846 with dissolve
    d "We're going as a family."
    a "..."
    s "[mc]...{w=0.4}{nw}"
    a "Okay..."
    scene ch8_847 with dissolve
    a "Have you already chosen where we're going?"
    d "Yes, it's a restaurant with outdoor seating."
    d "You're going to love it."
    a "Alright, I'll go change."
    s "[mc], it hurts..."
    scene ch8_848 with dissolve
    s "Aww..."
    scene ch8_849 with hpunch
    mc "Sorry!"
    s "Silly..."
    k "*Laughs*"
    mc "Sorry, [s:.5]!"
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    scene ch8_850 with dissolve
    pause
    play music scene2 fadein 2.0
    scene ch8_851 with hpunch
    s "Why didn't you open the door for me today?"
    mc "What?"
    s "I knocked on your door and you didn't come out."
    mc "When?"
    s "You know, don't play dumb, I knocked on your door today at 5 am, like we agreed."
    mc "I didn't say we would do it every day."
    scene ch8_852 with dissolve
    s "I said yes..."
    mc "I have a job now, I don't have that much time."
    s "And then I went into your room and you were sleeping."
    mc "Did I leave the door unlocked?"
    s "Yes."
    s "It's not the same when you're asleep, you know?"
    mc "What do you mean?"
    scene ch8_853 with dissolve    
    s "Nothing."
    s "T-tell me when we'll do it again."
    mc "Hmm... come to my room tomorrow morning."
    mc "And if I'm sleeping, please wake me up..."
    s "I didn't do anything to you while you were sleeping..."
    mc "Nobody said you did..."
    pause
    scene ch8_854 with dissolve
    s "So today, I mean, tomorrow morning again?"
    mc "Yes. (It's better to keep her happy...)"
    mc "(Plus, I had fun with her the other day...)"
    mc "{i}No!" with hpunch
    s "No what?"
    mc "Nothing, I'm going to get ready for the dinner."
    stop music fadeout 1.5
    scene blackscreen with dissolve
    pause
    scene ch8_855 with dissolve
    d "Ready, son?"
    mc "Yes, and [arelat] [a]?"
    d "We'll wait for her in the car."
    scene ch8_857 with dissolve
    play music sexy3 fadein 2.0
    a "Sorry for the delay."
    mc "..."
    d "..."
    k "Wow, [arelatks], you look beautiful."
    a "Thank you, honey."
    show ch8_858in with dissolve:
        xalign 0.5 yalign 0.0
        ease 3 yalign 1.0
        ease 6 yalign 0.0
    pause
    mc "(Hard not to fall in love... she's beautiful.)"
    pause
    mc "(I think she's waiting for a compliment from me.)"
    mc "You look gorgeous, [arelat] [a]!"
    scene ch8_860 with dissolve
    a "Thank you, honey."
    a "You look handsome too..."
    pause
    scene ch8_859 with dissolve
    k "Nice heels, [arelatks]."
    k "Are they new?"
    a "No, I had them stored away."
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    scene ch8_862 with dissolve
    play music scene1 fadein 2.0
    a "Thank you, honey."
    s "Nice place."
    k "Yeah, it's pretty."
    s "And I like the music."
    d "See, [s]?"
    d "Try listening to me before getting upset next time."
    pause
    scene ch8_863 with Fade(1.0,1.0,1.0)
    d "Because what's really important is hard work and intelligence."
    d "A piece of paper doesn't define your ability."
    d "Hard work and intelligence far surpass a university degree."
    d "And I see that in [mc]."
    scene ch8_863- with dissolve
    d "I know that in that company you're in, you'll go far."
    d "You remind me a lot of myself when I was your age, seeking to be someone in life and my own autonomy, good times.."
    d "Well done, son."
    mc "Thank you, [drelat] [d]."
    pause
    d "By the way, what do you do in that company?"
    mc "We produce motor oil."
    mc "I'm in the warehouse area, moving and arranging barrels all day."
    mc "We check the integrity of the containers and secure them in groups."
    d "It must be tiring."
    mc "Yes, but you get used to it."
    d "That's good, that's good."
    scene ch8_863-- with dissolve
    s "And how much do they pay you?"
    d "That's not something you ask, [s]."
    mc "Enough to take my beautiful [srelat] to the fair."
    s "How many times a week?"
    mc "Uh..."
    s "Will you buy me a car?"
    mc "Uh... well..."
    show ch8_864in with dissolve:
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 10 zoom 0.65 yalign 0.05
    d "The day you work you will buy one."
    s "No, I won't work, too lazy for that."
    d "What? I didn't raise a lazy daughter."
    s "You give money to [arelatks]."
    s "Why can't [mc] give me money too?"
    mc "(She looks really beautiful today...)"
    d "[a] is my wife."
    s "W-well, then [mc] and I..."
    d "What?!"
    s "That we are [srelat]s! What's the difference?"
    d "That's very different."
    show ch8_865in with dissolve:
        zoom 0.98 yalign 0.05 xalign 0.5
    d "As a husband, it's my duty to bring food, money, and everything else that is needed."
    d "Because we have an unbreakable bond that ties us all together, which is you guys."
    scene ch8_866 with dissolve
    d "What's mine is my beloved wife's because she is the heart of the family."
    a "..."
    pause
    scene ch8_867 with dissolve
    d "And that's why everything of mine is hers too."
    s "Yeah, yeah, we get it..."
    scene ch8_866 with dissolve
    d "Everything is for my beautiful, beautiful wife."
    scene ch8_868 with dissolve
    pause
    scene ch8_869 with dissolve
    pause
    scene ch8_870 with dissolve
    mc "You look absolutely stunning today, [a], [drelat] [d] is right."
    mc "Is that eyeshadow new?"
    a "My eyeshadow?"
    a "No, I had it before. I just wanted to try a brighter color today."
    mc "Well, it looks incredible on you."
    mc "I don't know if it's that or the lip gloss, but you look absolutely beautiful, like an angel."
    a "Oh..."
    scene ch8_871 with dissolve
    a "[mc], thank you so much."
    mc "Erm..."
    mc "Isn't that right, [drelat] [d]?"
    scene ch8_872- with dissolve
    d "Definitely, when I saw you coming down the stairs, you took my breath away, [a]."
    a "Thank you."
    pause
    scene ch8_872 with dissolve
    d "[a], I'm very happy that you came with us."
    d "I want to take this opportunity to tell you in front of everyone that..."
    d "I-i'm learning from my mistakes, I'm changing."
    d "Those things you believe about me...{w=0.4} it's totally my fault that you believe those things."
    d "I've neglected not only you as my wife but also my daughters and [mc]."
    d "You believe those things because of my apparent indifference towards you guys, my family."
    d "But I want to tell you that you guys never leave my mind even for a second, I always have you in mind wherever I go-{nw}"
    a "Stop, [d]."
    a "I think we should talk about these things at home."
    scene ch8_870 with dissolve
    a "We're celebrating [mc]'s job."
    d "Right, right..."
    d "Sorry, [mc]."
    scene ch8_877 with dissolve
    mc "No worries." 
    image ch8_878anim:
        "ch8_878" with Dissolve(0.5)
        1.5
        "ch8_879" with Dissolve(0.5)
        1.5
        repeat
    scene ch8_878anim with dissolve
    mc "[drelat!c] [d], you are very lucky to have a wife like [arelat] [a]."
    d "Of course."
    d "Don't ever doubt that, [mc]."
    d "She's my treasure."
    mc "Yeah."
    mc "She deserves to be treated like a treasure."
    mc "A secret treasure..."
    scene ch8_871 with dissolve
    d "She's my life."
    pause
    scene ch8_881 with dissolve
    pause
    scene ch8_878anim with dissolve
    pause 0.5
    scene ch8_880 with dissolve
    a "{i}{size=-5}Honey..."
    pause
    scene ch8_873 with dissolve
    d "[a], the other day on the yacht... I know it didn't go well, but..."
    d "I really wanted to dance with you, my love."
    image ch8_873anim:
        "ch8_873"
        3.0
        "ch8_874" with dissolve
    scene ch8_873anim with dissolve
    d "Would you grant me-"
    d "Uh..."
    a "..."
    scene ch8_882 with vpunch
    mc "[a], would you like to dance?"
    a "Uh?"
    mc "(What the hell am I doing?)"
    pause
    mc "W-would you like to dance with me?"
    a "S-sure.."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 1.0
    image ch8_883anim:
        "ch8_883" with Dissolve(0.5)
        1.5
        "ch8_884" with Dissolve(0.5)
        1.5
        repeat
    scene ch8_883anim with dissolve
    a "{i}What was that, [mc]?"
    mc "{i}I don't know..."
    pause
    mc "{i}The atmosphere was a bit heavy."
    mc "{i}I didn't think of anything else."
    a "{i}So that's why."
    mc "..."
    pause
    image ch8_885anim:
        "ch8_885" with Dissolve(0.5)
        1.5
        "ch8_886" with Dissolve(0.5)
        1.5
        repeat
    scene ch8_885anim with dissolve
    mc "{i}No."
    mc "{i}I felt jealous."
    mc "{i}I didn't want to see you dance with [drelat] [d]."
    a "{i}[mc]..."
    pause
    a "{i}I'm your [arelat], [mc]."
    mc "{i}And I love you."
    a "{i}You have to love me as your [arelat], and nothing else."
    mc "{i}I know, but..."
    pause
    mc "{i}I don't want him to sweet-talk you with that garbage he said."
    scene ch8_887 with dissolve
    a "{i}It's normal to want to take care of your [arelat]."
    a "{i}But I'm not naive."
    a "{i}Even so, it's sweet that you asked me to dance with you."
    pause
label ch8a10:
    if _in_replay:
        scene ch8_887 with dissolve
        show screen Replayexit
        play music scene2 fadein 1.0
    mc "{i}You look beautiful today, [arelat] [a]."
    mc "{i}This dress looks stunning on you."
    a "{i}Thank you."
    scene ch8_890 with dissolve
    pause
    scene ch8_892 with dissolve
    pause
    scene ch8_887 with dissolve
    pause 0.5
    scene ch8_887- with dissolve
    a "[mc]..."
    mc "{i}No one is watching us."
    scene ch8_892 with dissolve
    mc "{i}I can't resist your charms, [a], you know that."
    pause
    scene ch8_893 with dissolve
    pause
    scene ch8_894 with dissolve
    a "{i}[mc]!"
    mc "{i}No one is watching."
    a "{i}It doesn't matter, I don't like it."
    pause
    scene ch8_897 with dissolve
    a "{i}[mc], have you lost your mind?"
    mc "{i}Sorry."
    mc "(She turns me on too much, like a high school kid.)"
    scene ch8_896 with dissolve
    mc "{i}It's just, you look so damn beautiful today that I-"
    a "{i}I think we might be going a bit overboard with the compliments *giggle*."
    mc "{i}I thought you liked compliments."
    a "{i}Of course I do."
    a "{i}But you're making me addicted to them."
    pause
    scene ch8_898 with dissolve
    a "Do you know where the restroom is?"
    mc "It's inside."
    a "Will you come with me?"
    mc "Sure."
    pause
    scene ch8_899 with dissolve
    d "Where are you going?"
    mc "I'm accompanying [a] to the restroom."
    d "Oh, okay."
    d "I'm going to order some good alcohol, [mc]."
    d "To toast for your new job, of course, hahaha."
    mc "Yeah, we'll right back."
    pause
    scene ch8_900 with fade
    a "I'll be back in a second."
    a "..."
    mc "(I can't wait to get home...)"
    scene ch8_901 with dissolve
    mc "(To make her mine as far as the limits allow...)"
    pause
    mc "(Fuck, I'm so horny right now.)"
    mc "(Literally I can't...)"
    mc "(I can't wait!)"
    pause
    scene ch8_902 with dissolve
    mc "[a]..."
    a "Yeah?"
    a "What's the matter, honey?"
    mc "..."
    play music sexy1 fadein 1.0
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.4
    scene ch8_903- with dissolve
    a "*Hmmhm*"
    pause
    scene ch8_903 with dissolve
    stop sound fadeout 0.5
    a "{i}[mc]..."
    pause
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.4
    scene ch8_904 with hpunch
    a "*Hmh!"
    pause
    image ch8_903anim:
        "ch8_903--" with Dissolve(0.5)
        1.5
        "ch8_903-" with Dissolve(0.5)
        1.5
        repeat
    scene ch8_903anim with dissolve
    a "{i}Wait until we get home, honey."
    mc "{i}I can't."
    mc "{i}You look too beautiful, [a], I want you to be mine right here and now."
    a "{i}No{w=0.4}, *hmnch*."
    pause
    stop sound fadeout 0.5
    scene ch8_905 with dissolve
    mc "{i}I need to see them, [a]."
    pause
    scene ch8_906 with dissolve
    a "{i}[mc], this is crazy."

init python:
    def ch8_anipl_pov1_(trans, st, at):  
        trans.set_child("ch8_anipl_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_atit_pov1_(trans, st, at):  
        trans.set_child("ch8_atit_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
screen ch8_anipl_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Breasts" action Jump("ch8_atit_pov1_settings") style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_anipl_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_atit_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Nipples" action Jump("ch8_anipl_pov1_settings") style "textbutton_choice"               
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_anipl_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label beforech8_atit_pov1_:
    image ch8_anipl_pov1_:
        function ch8_anipl_pov1_
    image ch8_atit_pov1_:
        function ch8_atit_pov1_
    $ anim_speed = 0.035
    scene ch8_atit_pov1_ with dissolve
    a "{i}Oh, baby... Can't you wait until we get home?"
    mc "{i}You're too hot, [a]... I want you so much it hurts."
    mc "{i}No one will discover us here, [a]."
    a "{i}But why take such a risk, [mc]?"
    a "{i}You need to stop, honey."
    pause
    scene ch8_906 with dissolve
    pause
    scene ch8_907 with dissolve
    mc "{i}Such a beautiful nipples..."
    pause
    scene ch8_908 with dissolve
    a "{i}*Uh..*"
    scene ch8_anipl_pov1_ with dissolve
    a "{i}[mc], remember don't pull so hard."
    mc "{i}Is this good?"
    a "{i}Yes but..."
    a "{i}..."
    pause
    label ch8_atit_pov1_settings:
    scene ch8_atit_pov1_ with dissolve
    call screen ch8_atit_pov1_settings with dissolve
    label ch8_anipl_pov1_settings:
    scene ch8_anipl_pov1_ with dissolve
    call screen ch8_anipl_pov1_settings with dissolve
    label afterch8_anipl_pov1_:
    scene ch8_909 with dissolve
    mc "Hmm..."
    pause
    scene ch8_910 with dissolve
    a "{i}[mc], that's enough."
    mc "{i}No, [a], I need more of you..."
    a "{i}But, dear..."
    scene ch8_911 with dissolve
    a "{i}[mc], wait until we get home, it'll only be a couple of hours."
    mc "{i}We don't have to wait, if we're quiet we can do it here."
    pause
    scene ch8_912 with dissolve
    a "{i}[mc], this is crazy!"
    mc "{i}[a], you drive me completely crazy."
    mc "{i}With that makeup and this short dress, I can't resist you, you look like a goddess."
    a "{i}Oh, baby..."
    scene ch8_913 with dissolve
    mc "{i}I desire you, [arelat] [a]."
    a "{i}[mc], we have to be very careful, If we don't go back soon, they might suspect."
    mc "{i}No one would imagine that we're doing this, don't worry."
    scene ch8_914 with dissolve
    a "{i}[mc]!"
    a "{i}[mc], not here, listen to me.."
    pause
    $ anim_speed = 1.0
    image ch8_915anim:
        "ch8_915" with Dissolve(0.4)
        pause (anim_speed)
        "ch8_916" with Dissolve(0.4)
        pause (anim_speed)
        repeat
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.2
    scene ch8_915anim with dissolve
    a "{i}*Hmmhm, ahmhm*{w=0.4} No, [mc]."
    a "{i}*Uhhm*{w=0.4} No, baby..."
    pause
    image ch8_917anim:
        "ch8_917" with Dissolve(0.4)
        pause (anim_speed)
        "ch8_918" with Dissolve(0.4)
        pause (anim_speed)
        repeat
    a "{i}*Uh, hahmm*"
    pause
    a "{i}*Uhhm*{w=0.4}We have to go back, [mc]."
    mc "{i}I can't let you go like this, [a]."
    mc "{i}I have to finish what I started."
    a "{i}*Hmm*, I can't believe this is happening."
    image ch8_920anim:
        "ch8_920" with Dissolve(0.4)
        pause (anim_speed)
        "ch8_921" with Dissolve(0.4)
        pause (anim_speed)
        repeat
    scene ch8_920anim with dissolve
    mc "{i}(Neither can I.)"
    mc "{i}(This is incredible.)"
    a "{i}Oh, baby..."
    mc "(I think she's about to cum.)"
    $ anim_speed = 1.0
    a "{i}Stop, baby{w=0.4}, *hmmhm!*{w=0.4}, you have to stop."
    mc "{i}Stop me then, [a]."
    scene ch8_915anim with dissolve
    mc "{i}If you don't like it, then stop me..."
    $ anim_speed = 0.75
    pause
    a "*Hmhmm, uhh*"
    a "Stop...{w=0.4} *Ahh, hmm, ahh*."
    scene ch8_917anim with dissolve
    a "{i}*Ah, ahh, ah*"
    a "{i}Oh, [mc], *Ah, ahh, ah*"
    pause
    scene ch8_919 with dissolve
    mc "{i}I need to take it out, it hurts inside my pants."
    pause
    scene ch8_922 with dissolve
    mc "{i}I can't take it anymore, [a]..."
    a "{i}[mc], we've been here for too long."
    a "{i}They'll start suspecting of us."
    pause
    scene ch8_923 with dissolve
    mc "{i}Hmm, God..."
    mc "{i}(Look at that ass, oh my god...)"
    a "{i}Don't try anything extreme, I'm serious..."
    stop voicefx fadeout 0.5
    play sound "audio/knockdoor.mp3" fadein 1.0 volume 0.4
    "*Knock*"
    scene ch8_925 with dissolve
    a "Uh, Yeah?"
    a "I mean, occupied!"
    k "Sorry."
    scene ch8_926 with dissolve
    a "{i}{size=-3}That was [k]."
    mc "{i}{size=-3}Don't worry, let's just wait for her to leave."
    a "{i}{size=-3}[mc], I told you this was dangerous."
    pause
    scene ch8_927 with dissolve
    mc "{i}{size=-3}I like danger."
    a "{i}{size=-3}[mc], move away, didn't you hear? [k] is just a few steps away from us."
    scene ch8_928 with dissolve
    a "{i}{size=-3}Now!"
    pause
    scene ch8_929 with dissolve
    pause
    a "{i}{size=-3}Let's not do any more crazy things..."
    scene ch8_930 with dissolve
    pause
    a "{i}{size=-3}When she leave, you go first and..."
    scene ch8_931 with dissolve
    a "..."
    pause
    a "{i}{size=-3}Y-you go first and..."
    mc "{i}{size=-3}Look at me, [a]."
    mc "{i}{size=-3}My body craves more of you..."
    pause
    scene ch8_932 with dissolve:
        xalign 0.5 yalign 0.5 zoom 0.75
    a "{i}{size=-3}[mc]..."
    a "{i}{size=-3}..."
    pause
    scene ch8_933 with dissolve
    pause
    scene ch8_932 with dissolve:
        xalign 0.5 yalign 0.5 zoom 0.75
    pause
    scene ch8_934 with dissolve:
        xalign 0.5 yalign 0.5 zoom 0.75
    pause
    scene ch8_938-1 with dissolve
    a "{i}{size=-3}Honey..."
    a "{i}{size=-3}..."
    pause
    scene ch8_937 with dissolve
    a "{i}{size=-3}..."
    pause
    scene ch8_938 with dissolve
    a "{i}{size=-3}..."
    pause
    scene ch8_938-1 with dissolve
    a "*Ahem*{i}{size=-3} let's wait and...{w=0.4} you'll leave when [k] does, ok?"
    mc "{i}{size=-3}[a]..."
    pause
    scene ch8_938-2 with dissolve
    a "{i}{size=-3}What are you...?"
    mc "{i}{size=-3}I can't take it anymore, [a]."
    pause
    scene ch8_938-3 with dissolve
    a "{size=-3}{i}[mc]{w=0.4} ..."
    pause
    scene ch8_938-4in with dissolve
    a "Uh..."
    pause
    scene ch8_938-5in with dissolve
    a "{i}{size=-3}No..."
    pause
    scene ch8_938-4in with dissolve
    a "{i}{size=-3}[mc]..."
    pause
    scene ch8_938-5in with dissolve
    a "..."
    pause
    scene ch8_938-4in with dissolve
    pause
    scene ch8_938-6in with dissolve
    a "{i}{size=-3}*Muah*, dear..."
    pause
    scene ch8_938-8in with dissolve
    a "..."
    pause
    scene ch8_938-7in with dissolve
    a "{i}{size=-3}*Hmh*"
    pause
    scene ch8_938-8in with dissolve
    pause
    scene ch8_938-7in with dissolve
    a "{i}{size=-3}*Humh*"
    pause
    scene ch8_938-6in with dissolve
    pause
    scene ch8_938-10in with dissolve
    mc "{i}{size=-3}Oh..."
    pause
    mc "(This is really happening... [a] is giving me oral sex on her own.)"
    mc "(Her lips are so soft...)"
    scene ch8_938-11in with dissolve
    a "..."
    pause
    scene ch8_938-12in with dissolve
    a "{i}{size=-3}*Ahem*..."
    a "{i}{size=-3}I think [k] just left."
    mc "{i}{size=-3}[a]..."
    scene ch8_938-12in with dissolve
    a "{i}You have to leave, [mc]."
    mc "{i}[arelat!cl] [a], your lips-{w=0.5}{nw}"
    scene ch8_938-13in with dissolve
    a "{i}I'm not going to repeat myself..."
    mc "{i}Okay but..."
    a "{i}Wait until we get home."
    mc "(It's better to listen to her, it would be terrible to make her angry now that we're finally getting somewhere.)"
    mc "{i}Okay..." 
    a "Go now, honey, or they'll get suspicious."
    mc "Okay, I'll wait until home then."
    a "..."
    $ renpy.end_replay()
    stop music fadeout 4.0
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 2.0
    scene ch8_939 with dissolve
    d "Did you have fun?"
    s "Yes, Dad, but you shouldn't have had so much to drink."
    d "I'm not drunk."
    scene ch8_940 with dissolve
    d "If I were drunk, could I do this?"
    d "Hey, don't record me!"
    s "*Chuckles*"
    pause
    mc "(I can't wait to be alone with [a] again.)"
    mc "(I'm sure she feels the same way.)"
    mc "(She hasn't stopped looking at me since we got in the car.)"
    mc "(Too bad I couldn't sit next to her.)"
    scene ch8_942 with dissolve
    mc "{size=-3}{i}So, I'll see you in a while?"
    a "{i}{size=-3}Y-yes."
    pause
    scene ch8_942 with dissolve
    a "{i}{size=-3}Make sure no one sees you..."
    mc "{i}{size=-3}I know."
    a "{i}{size=-3}Good."
    scene ch8_941 with dissolve
    a "{i}{size=-3}I-I'll be waiting for you..."
    pause
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 2.0
    scene ch8_943 with dissolve
    mc "(What is she doing here?)"
    pause
label ch8a11:
    if _in_replay:
        show screen Replayexit
        play music scene2 fadein 1.0
    scene ch8_944 with dissolve
    mc "[arelat!cl] [a]."
    a "You came quick."
    mc "Are you waiting for something?"
    a "I want to change into something comfortable before going to bed but [d] is still in the room."
    mc "I see."
    scene ch8_944- with dissolve
    a "{i}{size=-3}I told you to come when no one could see you."
    mc "Why?"
    a "You know why..."
    pause
    scene ch8_944-- with dissolve
    mc "{i}{size=-3}What's wrong with saying goodnight to my [arelat]?"
    a "{i}{size=-3}Nothing, there's nothing wrong with it."
    scene ch8_944--- with dissolve
    mc "{i}{size=-3}So?"
    a "{i}{size=-3}I think you're right."
    d "[a]."
    scene ch8_946 with dissolve
    d "I'll be sleeping on the couch tonight."
    d "So... the room is all yours."
    a "It's okay, [d]."
    d "No."
    d "This house, even though I bought it, belongs to you more than it does to me."
    a "I'm used to the couch, [d], don't worry about it."
    d "I think it's unfair that you can't sleep in your own bed, don't you think?"
    mc "(Shit, [drelat] [d] had to ruin it...)"
    scene ch8_947 with dissolve
    a "[d], seriously, it's okay."
    d "No, [a], unless you want us to sleep together again..."
    a "..."
    mc "(I think [drelat] [d] is consumed by guilt.)"
    mc "(He's realizing that he can't neglect [a] because finding another woman like her is practically impossible.)"
    mc "(But he realized too late, [a] is mine now.)"
    d "Goodnight."
    scene ch8_948 with fade
    mc "So, you'll be sleeping in your room tonight."
    a "Yes."
    mc "So then..."
    a "Hm?"
    scene ch8_949 with dissolve
    pause
    a "Aren't you coming?"
    mc "To your room?"
    a "Y-{w=0.4}yeah."
    mc "Sure."
    pause
    stop music fadeout 3.0
    scene ch8_950 with Fade(1.5,0.0,1.5)
    pause
    mc "(Finally alone...)"
    mc "(I thought she wouldn't want to do it here, but thinking logically it's better than on the couch.)"
    mc "(No one will disturb us here and if someone knocks the door I can quickly go to the balcony.)"
    mc "(Thanks [drelat] [d].)"
    a "[mc]?"
    mc "I'm locking the door."
    "*Click*"
    pause
    play music sexy2 fadein 3.0
    play voicefx "audio/wavs/sfx/kissing_1.ogg" fadein 1.5 loop volume 0.5
    scene ch8_951- with dissolve
    a "*Hmnhmm*"
    pause
    stop voicefx fadeout 0.5
    scene ch8_951 with dissolve
    a "*Ah..* Straight to kissing?"
    mc "Why wait?"
    play voicefx "audio/wavs/sfx/kissing_1.ogg" fadein 1.5 loop volume 0.5
    scene ch8_951- with dissolve
    mc "I don't want to waste the night with words."
    a "*Hmmhmm*"
    pause
    scene ch8_952 with dissolve
    mc "Take everything off, [a]."
    mc "I want to see you as God made you."
    pause
    scene ch8_953 with dissolve
    pause
    scene ch8_954 with dissolve
    mc "[a], how I adore you!"
    a "*Giggles*"
    pause
    scene ch8_957 with dissolve
    mc "When I see you naked my senses start going crazy."
    a "*Hmmm..*"
    mc "You put on the same perfume as last time."
    a "You said you liked it."
    mc "Yes, I love it."
    mc "Hmm, [a], you have no idea how desperate I was to get home."
    mc "Every minute was torture."
    a "Don't be exaggerated, honey."
    mc "[a], I don't think you realize how much I adore you yet."
    scene ch8_960 with dissolve
    mc "*Hah..* I want to devour you whole, [a]."
    mc "I want to run my tongue all over your body."
    a "Oh, my god..."
    scene ch8_961 with dissolve
    mc "*Hmm..* Your ass drives me crazy, [a]."
    a "Oh..."
    pause
    a "L-let's not go overboard..."
    scene ch8_962 with dissolve
    mc "I never thought that one day having only two arms would be so frustrating."
    mc "I wish I had more hands so I could touch your whole body at once."
    a "*Giggles*, Relax, take your time."
    scene ch8_959 with dissolve
    mc "*Hmhm* You taste so good.."
    pause
    scene ch8_958 with dissolve
    mc "*Sucking sounds*"
    a "*Ah, hmmhm...*"
    pause
    scene ch8_959 with dissolve
    mc "*Hmmahm*"
    pause
    scene ch8_963 with dissolve
    a "*Hmhmmh, hmch*"
    pause
    stop voicefx fadeout 0.5
    scene ch8_964 with dissolve
    a "Ah... Oh, baby."
    a "I was also anxious for us to get home and for you to kiss me as passionately as you do."
    mc "You have no idea how passionately I'm going to kiss you now, [a]."
    mc "Lie down on the bed."
    pause
    scene ch8_955 with dissolve
    pause
    a "..."
    show ch8_956 with dissolve:
        xalign 0.0 yalign 1.0 
        ease 10 yalign 0.0
    mc "Wow..."
    mc "(Her beauty never ceases to amaze me.)"
    mc "(She truly looks like a goddess.)"
    mc "(Such loveliness cannot leave anyone indifferent, not even me, her [arelatmc].)"
    pause
    scene ch8_966 with dissolve
    a "[mc]..."
    pause
    scene ch8_968 with dissolve
    mc "Hmm, you have such exquisite legs, [a]..."
    a "*Hmhm*"
    pause
    scene ch8_967 with dissolve
    mc "(Damn... What a view.)"    
    pause
    mc "Wow..."
    mc "You truly are a goddes..."
    a "Thank you."
    scene ch8_969 with dissolve
    a "Remember the limits, ok?"
    mc "I don't know where those limits you speak of are, [a]."
    mc "Those limits were different yesterday, and the day before that they were different."
    a "There are certain things we can never do under any circumstances."
    a "Things that [arelat] and [arelatmc] should never do."
    pause
    image ch8_970anim:
        "ch8_970" with Dissolve(0.4)
        1.5
        "ch8_971" with Dissolve(0.4)
        1.5
        repeat
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.6
    scene ch8_970anim with dissolve
    mc "I don't know where those limits are, [a]..."
    a "*Ahh, hmmhm*"
    mc "This isn't something a [arelatmc] should be doing to his [arelat], but we're doing it."
    a "*Ahh, hmhhmm*."
    pause
    scene ch8_972 with dissolve
    mc "Hmmm..."
    pause
    scene ch8_973 with dissolve
    a "Oh... hmmhm.."
    pause

init python:
    def ch8_974_acl_1_pov1_(trans, st, at):  
        trans.set_child("ch8_974_acl_1_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_974_acl_1_pov2_(trans, st, at):  
        trans.set_child("ch8_974_acl_1_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 31:
            store.frame_num = 2
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_974_acl_1_pov3_(trans, st, at):  
        trans.set_child("ch8_974_acl_1_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
screen ch8_974_acl_1_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_974_acl_1_pov2_settings") style "textbutton_choice"      
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_974_acl_1_pov3_settings") style "textbutton_choice"               
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_974_acl_1_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_974_acl_1_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_974_acl_1_pov1_settings") style "textbutton_choice"      
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_974_acl_1_pov3_settings") style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_974_acl_1_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_974_acl_1_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_974_acl_1_pov1_settings") style "textbutton_choice"      
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_974_acl_1_pov2_settings") style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_974_acl_1_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label beforech8_974_acl_1_pov3_:
    image ch8_974_acl_1_pov1_:
        function ch8_974_acl_1_pov1_
    image ch8_974_acl_1_pov2_:
        function ch8_974_acl_1_pov2_
    image ch8_974_acl_1_pov3_:
        function ch8_974_acl_1_pov3_
    $ anim_speed = 0.05
    scene ch8_974_acl_1_pov1_ with dissolve
    a "*Ahh*{w=0.5}, That feels so good, baby..."
    a "*Hmhm, ahh*"
    mc "Hmm... *slup, chup*"
    $ anim_speed = 0.035
    mc "(I love how she writhes in pleasure when I roll my tongue on her clit.)"
    a "*Uuh, hmmhm*"
    pause
    scene ch8_974_acl_1_pov2_ with dissolve
    a "Oh, [mc]{w=0.4}*Hmhmm*{w=0.4}, you're so good..."
    a "You're making me feel things I haven't felt in a long time."
    a "*Ahh*, baby... yes, keep going, honey."
    $ anim_speed = 0.015
    mc "(I forgot how premature she is.)"
    mc "(It must be because of the lack of real sex.)"
    a "*Hahh*, oh, dear..."
    pause
    scene ch8_974_acl_1_pov3_ with dissolve
    a "*Ahh, ahmhhm!*{w=0.4}, honey{w=0.4}, *Hahh, ahhmhm, uhmm*{w=0.4}, you're so good..."
    a "*Ahh*{w=0.4}, I missed being touched by a man so much."
    a "Even if it's you..."
    pause
    a "No..."
    a "It's because it's you, baby..."
    a "That's why it feels so good{w=0.4}, *Ah, ahmmhaah!*{w=0.4}, because it's my beloved [arelatmc] who's pleasing me."
    a "I love you so much, baby,{w=0.4}*Ahh, hmmhm!*{w=0.4} You have no idea."
    call screen ch8_974_acl_1_pov3_settings with dissolve
    image ch8_974_acl_1_pov3_cumm:
        "ch8_974_acl_1_pov3_9"
        0.025
        "ch8_974_acl_1_pov3_10"
        0.025
        "ch8_974_acl_1_pov3_11"
        0.025
        "ch8_974_acl_1_pov3_12"
        0.025
        "ch8_974_acl_1_pov3_11"
        0.025
        "ch8_974_acl_1_pov3_10"
        0.025
        repeat
label ch8_974_acl_1_pov1_settings:
    scene ch8_974_acl_1_pov1_ with dissolve
    call screen ch8_974_acl_1_pov1_settings with dissolve
label ch8_974_acl_1_pov2_settings:
    scene ch8_974_acl_1_pov2_ with dissolve
    call screen ch8_974_acl_1_pov2_settings with dissolve
label ch8_974_acl_1_pov3_settings:
    scene ch8_974_acl_1_pov3_ with dissolve
    call screen ch8_974_acl_1_pov3_settings with dissolve
    
label afterch8_974_acl_1_pov2_:
    scene ch8_974_acl_1_pov3_cumm with cumming
    with flash
    play voicefx "audio/wavs/a/amoanhard_2.ogg"
    a "*Hngh, hmmngh, ahhh!!" 
    scene ch8_974_acl_1_pov3_10 with dissolve
    a "Uuuff... Oh, God..."
    pause
    scene ch8_969 with dissolve
    mc "(Too bad, there was no squirt this time...)"
    mc "I love it when you have such intense orgasms, [a]."
    mc "When you moan with so much pleasure, it really turns me on."
    a "Oh, dear..."
    pause

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_asy_pov1_(trans, st, at):  
        trans.set_child("ch8_asy_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking8.ogg", "audio/sex/fucking2.ogg", "audio/sex/fucking6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()   
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_asy_pov2_(trans, st, at):  
        trans.set_child("ch8_asy_pov2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking8.ogg", "audio/sex/fucking2.ogg", "audio/sex/fucking6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_asy_pov3_(trans, st, at):  
        trans.set_child("ch8_asy_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 25:
            sound_files = ["audio/sex/fucking1.ogg", "audio/sex/fucking8.ogg", "audio/sex/fucking2.ogg", "audio/sex/fucking6.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)() 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

screen ch8_asy_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.013) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_asy_pov2_") style "textbutton_choice"      
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_asy_pov3_") style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_asy_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch8_asy_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.013) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_asy_pov1_") style "textbutton_choice"      
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_asy_pov3_") style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_asy_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    
screen ch8_asy_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.013) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_asy_pov1_") style "textbutton_choice"      
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_asy_pov2_") style "textbutton_choice"          
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_asy_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    

label beforech8_asy_pov1_:
    image ch8_asy_pov1_:
        function ch8_asy_pov1_
    image ch8_asy_pov2_:
        function ch8_asy_pov2_
    image ch8_asy_pov3_:
        function ch8_asy_pov3_   
    $ anim_speed = 0.05
    scene ch8_967 with dissolve
    pause
    scene ch8_977 with dissolve
    mc "Hmm..."
    a "No, [mc]..."
    scene ch8_975 with dissolve
    a "Remember what I told you at the beginning."
    mc "I'm not going to put it in, I just want to rub."
    a "Just...{w=0.4} rub."
    pause
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.5
    scene ch8_asy_pov2_ with dissolve
    mc "Yes, I just want to feel the friction between your vagina and my cock..."
    mc "Hmmhm, [a]... this feels really good."
    a "Hmhmmm..."
    mc "*Uh, uh*, do you like it?"
    a "Yes, baby, it feels good..."
    $ anim_speed = 0.035
    pause
    scene ch8_asy_pov3_ with dissolve
    mc "*Uhm, hmm, hmg*{w=0.4}, your vagina is so yummy{w=0.4}, [a]."
    mc "So swollen... hmmm, delicious."
    a "*Mhh, hmmhm*{w=0.4}, Thank you, baby..."
    a "Your...{w=0.4} dick{w=0.4} is beautiful too..."
    a "*Uh, uh, uh*{w=0.4}, Your big, thick and gorgeous dick..."
    $ anim_speed = 0.013
    mc "*Hm, hmg, hng!* God, {w=0.4}*Ah!*{w=0.4}"
    pause
    scene ch8_asy_pov1_ with dissolve
    mc "*Hngh!*(I can't cum yet)"
    jump ch8_asy_pov1_

label ch8_asy_pov1_:
    scene ch8_asy_pov1_ with dissolve
    call screen ch8_asy_pov1_settings with dissolve
label ch8_asy_pov2_:
    scene ch8_asy_pov2_ with dissolve
    call screen ch8_asy_pov2_settings with dissolve
label ch8_asy_pov3_:
    scene ch8_asy_pov3_ with dissolve
    call screen ch8_asy_pov3_settings with dissolve




label afterch8_asy_pov1_:
    scene ch8_975 with dissolve
    a "Why did you stop?"
    mc "I was about to cum, *uff...*"
    scene ch8_976 with dissolve
    mc "(What I wouldn't give to be inside her for at least a minute...)"
    pause
    jump beforech8_976

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_a_dr_pov1_(trans, st, at): 
        trans.set_child("ch8_a_dr_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_voice(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

screen ch8_a_dr_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.014) style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_a_dr_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

label beforech8_976:
    image ch8_a_dr_pov1_:
        function ch8_a_dr_pov1_
    $ anim_speed = 0.05
    scene ch8_a_dr_pov1_ with dissolve
    mc "*Uhh*, (Your vagina is so delicious, my god!)"
    a "Honey... *Hmmm*"
    mc "(It's getting wetter and wetter...)"
    mc "(Maybe if I keep going, I can convince her to have sex...)"
    $ anim_speed = 0.035
    pause
    mc "Do you like it when I rub my penis on your clitoris?"
    a "*Hmmm...* Yes, baby, it feels so good..."
    call screen ch8_a_dr_pov1_settings with dissolve


label afterch8_a_dr_pov1_:
    image ch8_976anim:
        "ch8_976" with Dissolve(0.4)
        1.0
        "ch8_977" with Dissolve(0.4)
        1.0
        repeat
    scene ch8_976anim with dissolve
    a "No, [mc]..."
    mc "Just a little bit, the tip."
    a "No, [mc], not that."
    a "We can do many things but definitely not that, baby."
    a "*Ah.. uh.. hmmhm*"
    mc "Just a little bit, [a]."
    a "*Ah, hmhmm*"
    pause
    stop voicefx fadeout 0.5
    scene ch8_978 with dissolve
    a "I said no, [mc]."
    a "And if that was your only goal, it's better that you go to your room..."
    pause
    scene ch8_980 with dissolve
    mc "No, no, of course not."
    mc "But you're just so irresistible, [a]..."
    a "That's not an excuse, honey."
    mc "I know, but it's hard to resist."
    mc "When I'm so close to you, smelling your perfume and tasting your body, it becomes impossible not to try something more."
    a "You know the rules, baby..."
    a "If you want this to work, you have to follow them."
    scene ch8_979 with dissolve
    mc "I want this to work, I'll do and stop doing anything you ask of me."
    mc "But try to put yourself in my shoes, I like you excessively."
    mc "When you think I'm crossing the line, just tell me and I swear I'll stop instantly."
    mc "But I can't promise I won't try something more again..."
    a "[mc]..."
    a "O-okay..." 
    mc "Lie down on the bed, [a]."
    a "W-why?"
    mc "I want to keep eating you out like you like it..."
    a "J-just try not to get too excited again, okay?"
    mc "I will."
    scene ch8_986 with dissolve
    a "Don't... go too far."
    mc "I won't."
    pause
    scene ch8_987 with dissolve
    mc "(Wow, what an ass...)"
    mc "There's no angle in which you're not beautiful, [a]..."
    a "T-thank you..."
    pause
    scene ch8_997 with dissolve
    mc "(Her anus is so pink... so delicious!)"
    mc "(But she told me not to go too far.)"
    mc "(I won't pressure her, she must already think we're doing too much.)"
    pause

init python:
    def ch8_988_acl_1_(trans, st, at):  
        trans.set_child("ch8_988_acl_1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    def ch8_988_acl_2_(trans, st, at):  
        trans.set_child("ch8_988_acl_2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
    
init python:
    def ch8_988_acl_3_(trans, st, at):  
        trans.set_child("ch8_988_acl_3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    def ch8_988_acl_4_(trans, st, at):  
        trans.set_child("ch8_988_acl_4_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        # Call atl_play_sound function inside var_speed function
        #if store.frame_num == 65:
        #    sound_files = ["audio/bj/bj_b_01.ogg", "audio/bj/bj_b_02.ogg", "audio/bj/bj_b_03.ogg"]
        #    random_sound = renpy.random.choice(sound_files)
        #    atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
screen ch8_988_acl_1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.014) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_988_acl_2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_988_acl_3_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_988_acl_1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_988_acl_2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.014) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_988_acl_1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_988_acl_3_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_988_acl_1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_988_acl_3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.014) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_988_acl_1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_988_acl_2_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_988_acl_1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_988_acl_4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_988_acl_4_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
label beforech8_988_acl_1_:
    image ch8_988_acl_1_:
        function ch8_988_acl_1_
    image ch8_988_acl_2_:
        function ch8_988_acl_2_
    image ch8_988_acl_3_:
        function ch8_988_acl_3_
    image ch8_988_acl_4_:
        function ch8_988_acl_4_   
    scene ch8_996 with dissolve
    a "*Oh!*"
    pause
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.5
    scene ch8_988_acl_1_ with dissolve
    a "*Uhmhm* Baby..."
    mc "*Hmnch, slmh* You taste so delicious, [a]."
    mc "*Hmhmm* I could do this all night."
    a "*Uhhmmh, ahh*"
    pause
    scene ch8_988_acl_2_ with dissolve
    a "Oh, baby, that feels so good..."
    a "*Uhmhm*, I didn't know I needed this so much..."
    mc "I'll give you oral sex anytime you want, [a]."
    mc "You just have to ask and I'll gladly lick this delicious vagina you have, *hmnch*."
    a "Oh, dear.. Ahh.."
    scene ch8_988_acl_3_ with dissolve
    a "*Huhnm!*{w=0.4}, that feels so good, baby..."
    a "That's it, honey, keep using your tongue like that{w=0.4}, *Ahh*."
    mc "Hmm, you taste so delicious, [a]."
    a "Oh, my God, I'm so lucky to have such a loving [arelatmc] with his [arelat]..."
    call screen ch8_988_acl_3_settings with dissolve
label ch8_988_acl_1_:
    scene ch8_988_acl_1_ with dissolve
    call screen ch8_988_acl_1_settings with dissolve
label ch8_988_acl_2_:
    scene ch8_988_acl_2_ with dissolve
    call screen ch8_988_acl_2_settings with dissolve
label ch8_988_acl_3_:
    scene ch8_988_acl_3_ with dissolve
    call screen ch8_988_acl_3_settings with dissolve

label afterch8_988_acl_1_:
    $ anim_speed = 0.013
    scene ch8_988_acl_4_ with dissolve
    a "Oh, honey!"
    a "*Hmhm*{w=0.4}, -baby!"
    a "*Nghmmhm, mhmm!*"
    pause
    call screen ch8_988_acl_4_settings with dissolve

label ch8_988_acl_4_:
    image ch8_988_acl_4_cumm:
        "ch8_988_acl_4_10"
        0.012
        "ch8_988_acl_4_11"
        0.012
        "ch8_988_acl_4_12"
        0.012
        "ch8_988_acl_4_13"
        0.012
        "ch8_988_acl_4_14"
        0.012
        "ch8_988_acl_4_15"
        0.012
        "ch8_988_acl_4_16"
        0.012
        "ch8_988_acl_4_15"
        0.012
        "ch8_988_acl_4_14"
        0.012
        "ch8_988_acl_4_13"
        0.012
        "ch8_988_acl_4_12"
        0.012
        "ch8_988_acl_4_11"
        0.012
        
        repeat
    scene ch8_988_acl_4_cumm with cumming
    play voicefx "audio/wavs/a/amoanhard_1.ogg" volume 0.8
    a "*Ahhhmhh!*" with flash
    scene ch8_1002 with Dissolve(2.0)
    a "*Uhhh...*"
    pause
    scene ch8_996 with dissolve
    pause
    scene ch8_995 with dissolve
    a "*Uhhh*, baby..."
    pause
    scene ch8_985 with dissolve
    a "Uh, [mc]..."
    pause
    show ch8_983-in with dissolve:
        xalign 0.5 yalign 0.0 zoom 0.75
    a "[mc], that was..."
    show ch8_983-in:
        xalign 0.5 yalign 0.0 zoom 0.75
        ease 5 yalign 1.0
        ease 2 yalign 0.6
        ease 2 yalign 1.0
    mc "Hmm, [a], you know how much I like this part of you."
    mc "I had always dreamed of doing this someday..."
    a "Doing what, honey?"
    show ch8_983--in with dissolve:
        xalign 0.5 zoom 0.75 yalign 1.0
    mc "Hmm, rubbing my dick between this delicious ass cheeks..."
    show ch8_983-in with dissolve:
        xalign 0.5 zoom 0.75 yalign 1.0
    mc "God..."
    scene ch8_983---- with dissolve
    a "Oh..."
    a "What are you waiting for?"
    scene ch8_983----- with dissolve
    a "It's your reward for being such a good [arelatmc]."
    mc "[a], I fucking love you."
    scene ch8_983---- with dissolve
    mc "Mhmm, so good..."
    scene ch8_aj_2_pov1_1 with dissolve
    a "After how good you made me feel, I can't say no to you."
    a "I have to reward you with something."
    mc "Thank you, [a]."

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aj_2_pov1_(trans, st, at):  
        trans.set_child("ch8_aj_2_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound = random_sound
            atl_play_voice(random_sound)() 
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aj_2_pov2_(trans, st, at):  
        trans.set_child("ch8_aj_2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_voice(random_sound)() 
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aj_2_pov3_(trans, st, at):  
        trans.set_child("ch8_aj_2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_voice(random_sound)() 
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    def ch8_aj_2_pov4_(trans, st, at):  
        trans.set_child("ch8_aj_2_pov4_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound 
            atl_play_voice(random_sound)() 
        if store.frame_num == 25:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

screen ch8_aj_2_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch8_aj_2_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_aj_2_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_aj_2_pov4_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_aj_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_aj_2_pov2_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_aj_2_pov1_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch8_aj_2_pov3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_aj_2_pov4_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_aj_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_aj_2_pov3_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_aj_2_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_aj_2_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch8_aj_2_pov4_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_aj_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_aj_2_pov4_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch8_aj_2_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_aj_2_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_aj_2_pov3_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_aj_2_pov4_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

label beforech8_aj_2_pov1_1:
    image ch8_aj_2_pov1_:
        function ch8_aj_2_pov1_
    image ch8_aj_2_pov2_:
        function ch8_aj_2_pov2_   
    image ch8_aj_2_pov3_:
        function ch8_aj_2_pov3_   
    image ch8_aj_2_pov4_:
        function ch8_aj_2_pov4_   
    $ anim_speed = 0.035
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.2
    scene ch8_aj_2_pov1_ with dissolve
    a "Oh!"
    mc "*Hmmhm*, God, [a]... this is better than I ever imagined."
    a "You like it, dear?"
    mc "Yes{w=0.4}, *Hmh*{w=0.4}, seeing those bouncing buttocks is super exciting."
    a "..."
    pause
    a "The fact that you find me so attractive makes me feel like a woman again.."
    a "It boosts my self-esteem like you have no idea."
    scene ch8_aj_2_pov2_ with dissolve
    a "You don't know how much you've helped me regain my self-esteem."
    a "It's been a while since I felt that attractive..."
    a "Maybe never."
    mc "*Hmm*, that can't be true."
    a "It's not that I saw myself as an ugly woman, I just... I don't know... stopped feeling pretty."
    mc "You had a distorted perception of yourself."
    a "Yes."
    a "When [d] stopped being interested in me, it made me depressed."
    a "You know, years went by and then [d] did what he did..."
    $ anim_speed = 0.022
    mc "*Hmmh!*"
    mc "I still can't understand [drelat] [d]."
    mc "I can't wrap my head around how someone could get tired of a woman like you."
    mc "But I'm glad it happened, because now you're all mine."
    pause
    a "I think I'm much happier now."
    a "Spending time with you..."
    pause
    a "Although..."
    mc "Hm?"
    a "Nothing."
    pause
    scene ch8_aj_2_pov3_ with dissolve
    mc "Plus, you haven't lost an ounce of beauty, [a]."
    mc "On the contrary, over the years you've become more and more beautiful."
    a "Do you really think so?"
    mc "It's a fact..."
    mc "[a], you're like a fine wine."
    a "Are you calling me old?"
    mc "*Hmm*{w=0.4}, you definitely have good self-esteem now."
    a "*Giggle*, it's all your fault."
    mc "*Hmhm*, what have I created..."
    a "*Giggle*"
    $ anim_speed = 0.013
    a "Oh!.."
    mc "Hmm, [a]."
    scene ch8_aj_2_pov4_ with dissolve
    a "Are you close, baby?"
    mc "*Hmmhngh!*{w=0.4}, almost there.."
    mc "*Hmgh!*{w=0.4}, This is like a dream."

label ch8_aj_2_pov1_:
    scene ch8_aj_2_pov1_ with dissolve
    call screen ch8_aj_2_pov1_settings with dissolve
label ch8_aj_2_pov2_:
    scene ch8_aj_2_pov2_ with dissolve
    call screen ch8_aj_2_pov2_settings with dissolve
label ch8_aj_2_pov3_:
    scene ch8_aj_2_pov3_ with dissolve
    call screen ch8_aj_2_pov3_settings with dissolve
label ch8_aj_2_pov4_:
    scene ch8_aj_2_pov4_ with dissolve
    call screen ch8_aj_2_pov4_settings with dissolve

label afterch8_aj_2_pov4_:
    scene ch8_aj_2_pov4_ with dissolve
    $ anim_speed = 0.01
    a "That's it, baby, let it out on my back."
    a "I don't want you to hold back anything, honey."
    mc "Hmhgh!, [a], I would like to..."
    stop voicefx fadeout 0.5
    $ anim_speed = 0.015
    pause 0.1
    $ anim_speed = 0.02
    pause 0.1
    $ anim_speed = 0.03
    pause 0.1
    $ anim_speed = 0.04
    pause 0.1
    $ anim_speed = 0.05
    pause 0.1
    $ anim_speed = 0.08
    pause 0.1
    $ anim_speed = 0.1
    pause 0.1
    $ anim_speed = 0.15
    pause 0.1
    $ anim_speed = 0.2
    pause 0.1
    $ anim_speed = 0.3
    pause 0.1
    $ anim_speed = 1000
    pause 0.1
    mc "Uff, I still don't want to do it, [a]."
    mc "I want to keep enjoying this."
    a "Ok, baby, you can take your time if you want."
    mc "[a], we've talked about how I make you feel like a woman and all that..."
    play voicefx "audio/wavs/a/amoansoft.ogg" loop volume 0.15
    scene ch8_993 with dissolve
    a "Y-yes..."
    mc "My most cherished dream is for you to make me feel like a man..."
    a "W-what do you mean by that?"
    mc "Yes, [a]... I want to be your man."
    a "[mc], th-this..."
    pause
    scene ch8_990 with dissolve
    mc "I want to make you mine, [a]."
    a "N-no, baby..."
    mc "Just this once."
    scene ch8_991 with dissolve
    a "Honey, you know the rules."
    mc "[a], how long has it been since you've been made love to?"
    image ch8_991anim:
        "ch8_992" with Dissolve(0.4)
        2.0
        "ch8_991" with Dissolve(0.4)
        2.0
        repeat
    scene ch8_991anim with dissolve
    a "[mc], don't do it, baby..."
    mc "Wouldn't you like to feel the love of a man again?"
    a "Honey, we can't, please understand, baby."
    mc "No one will know..."
    a "But I will."
    a "Honey, you're my [arelatmc]."
    image ch8_993anim:
        "ch8_993" with Dissolve(0.4)
        2.0
        "ch8_994" with Dissolve(0.4)
        2.0
        repeat
    scene ch8_993anim with dissolve
    mc "I'm your [arelatmc] but I'm also a man."
    a "Honey, please understand."
    mc "[a], I'm inches away from making you mine, you just have to say yes."
    a "Baby..."
    mc "No one will know, I swear it'll be our secret."
    a "[mc], don't ask me that."
    stop voicefx fadeout 0.5
    scene ch8_998 with dissolve
    a "[mc]..."
    pause
    scene ch8_1000 with dissolve
    a "T-this feeling you have..."
    a "These desires for me..."
    mc "They're not just desires, [a]..."
    scene ch8_1000- with dissolve
    a "Yes, they're just that, ''desires'', [mc]."
    a "You're young and virile."
    a "Y-your hormones are going crazy right now."
    scene ch8_1000 with dissolve
    pause
    scene ch8_999 with dissolve
    a "You're confusing love with physical attraction..."
    pause
    a "Maybe it's because you've never been with a woman with my...{w=0.4} proportions before?"
    mc "No, [a]-"
    scene ch8_999- with dissolve
    a "-*Shhh!*, that's how it is, you may not think so but I'm right."
    pause
    scene ch8_1004 with dissolve
    a "If we give in to all of this, things won't turn out well."
    a "Do you understand, right?"
    mc "I don't understand [a]..."
    a "Honey..."
    mc "But I don't really care about having sex or not, I just want to make you happy."
    a "..."
    scene ch8_1000- with dissolve
    pause
    a "I also want you to be happy, baby..."
    a "Lie down, honey."
    a "N-now I'll take care of this...{w=0.4} matter."
    pause
    scene ch8_1005 with fade
    a "*Sigh*..."
    a "Oh, baby, look at this erection..."

init python:
    store.last_played_sound3 = None
    store.last_played_sound2 = None
    def ch8_1000_ahj_pov1_(trans, st, at):  
        trans.set_child("ch8_1000_ahj_pov1_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
 
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            store.last_played_sound3 = random_sound  
            atl_play_voice(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value      

screen ch8_1000_ahj_pov1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_1000_ahj_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

    

label beforech8_1000_ahj_pov1_:
    image ch8_1000_ahj_pov1_:
        function ch8_1000_ahj_pov1_
    scene ch8_1000_ahj_pov1_1 with dissolve
    a "..."
    pause
    $ anim_speed = 0.05
    scene ch8_1000_ahj_pov1_ with dissolve
    pause
    a "I'm sorry we can't do much more."
    mc "I understand, [a]."
    mc "I know the mere thought of you and me doing more than we should gives you chills."
    a "..."
    pause
    a "Obviously, I don't feel any rejection towards you."
    a "You're handsome, athletic, loving... and I can go on."
    a "I don't think there's any woman who would reject spending a night with you..."
    mc "Only you."
    pause
    a "Y-yes, only me..."
    a "[mc]..."
    pause
    a "I wish things were different..."
    pause
    $ anim_speed = 0.015
    mc "*Hmmhm*"
    mc "If I weren't your [arelatmc], would things be different?"
    a "L-like that, baby?"
    mc "Answer me, [a]."
    a "..."
    a "Yes..."
    mc "That comforts me a little."
    a "Let's not talk about that please."
    call screen ch8_1000_ahj_pov1_settings with dissolve

label afterch8_1000_ahj_pov1_:
    $ anim_speed = 0.02
    pause 0.5
    $ anim_speed = 0.025
    pause 0.5
    $ anim_speed = 0.03
    pause 0.5
    $ anim_speed = 0.035
    pause 0.5
    $ anim_speed = 0.04
    pause 0.5
    $ anim_speed = 0.045
    pause 0.5
    $ anim_speed = 0.05
    a "Y-you don't seem to enjoy it much..."
    mc "I do, it's just that after everything we've already done, it doesn't give me the same thrill anymore."
    pause
    scene ch8_1009 with dissolve
    a "I didn't expect you to finish with just that anyway..."
    a "..."
    image ch8_1010anim:
        "ch8_1010" with Dissolve(0.3)
        2.0
        "ch8_1011" with Dissolve(0.3)
        2.0
        repeat
    scene ch8_1010anim with dissolve
    a "Oh, baby, you have it so hard, it must even hurt..."
    mc "Hmm... (I can see the desire in her eyes.)"
    mc "It's very hard but..."
    a "Very hard, yeah..."
    mc "But it doesn't really hurt."
    a "I-I see..."
    scene ch8_1011- with dissolve
    a "You have a beautiful penis, honey..."
    image ch8_1013anim:
        "ch8_1012" with Dissolve(0.3)
        1.0
        "ch8_1013" with Dissolve(0.3)
        1.0
    scene ch8_1013anim with dissolve
    pause 1.5
    play sound "audio/mouth/french_kiss_02.ogg" volume 0.25
    scene ch8_1011- with dissolve
    a "So long and thick..."
    a "..."
    scene ch8_1013anim with dissolve
    pause 2
    play sound "audio/mouth/french_kiss_06.ogg" volume 0.25
    scene ch8_1011- with dissolve
    a "Oh, baby..."
    a "You're not the only one who has to hold back..."
    mc "*Hmm*, well let's not hold back then."
    scene ch8_1014 with dissolve
    a "I-I said that out loud..."
    mc "[a], you seem more nervous than usual."
    a "It's just... I want to make you cum, baby, but..."
    a "I'm not sure if I should do what I have in mind."
    a "I guess you're right that the line between what we can do and what we can't is a bit blurry."
    a "..."
    scene ch8_1015 with dissolve
    a "You made me enjoy myself so much earlier, honey..."
    a "I think it's only fair that I take care of you in the same way, right?"
    a "This will remain our secret, okay, honey?"
    mc "Of course, [a]."
    mc "No one will never know."
    scene ch8_1011- with dissolve
    a "..."
    pause
    mc "(Damn it, [a], don't just stare...)"
    scene ch8_1013anim with dissolve
    play sound "audio/mouth/french_kiss_02.ogg" volume 0.2
    mc "Oh, [a], every kiss you give me makes me melt..."
    play sound "audio/mouth/french_kiss_06.ogg" volume 0.2
    pause
    scene ch8_1016 with dissolve
    play sound "audio/mouth/french_kiss_04.ogg" volume 0.2
    a "*Giggle, Hmmhm*, then I'll keep kissing you..."
    mc "*Hmm*..."
    scene ch8_1017 with dissolve
    a "Hah... {i}{size=-5}what a big and throbbing penis..."
    pause
    scene ch8_1018 with dissolve
    a "You're so big, [mc]..."
    pause
    scene ch8_1016 with dissolve
    play sound "audio/mouth/french_kiss_02.ogg" volume 0.2
    a "*Hmnch*..."
    scene ch8_1017 with dissolve
    a "*Smnch...*"
    pause
    scene ch8_1024 with dissolve
    play sound "audio/mouth/french_kiss_07.ogg" volume 0.2
    a "*Hmhm..*"
    pause
    scene ch8_1025 with dissolve
    a "*Hmahh...*"
    pause
    scene ch8_1026 with dissolve
    mc "Oh, [a]..."
    a "Hmm, my handsome [arelatmc]..."
    play sound "audio/mouth/french_kiss_06.ogg" volume 0.2
    scene ch8_1024 with dissolve
    a "*Hmnch, hmnch, hmnch*"
    scene ch8_1025
    a "*Hmlahh...*"
    scene ch8_1026 with dissolve
    a "{i}{size=-5}So big and hard..."
    a "{i}{size=-5}And what a manly scent..."
    scene ch8_1027 with dissolve
    play sound "audio/mouth/french_kiss_04.ogg" volume 0.2
    a "*Hmhmm...* Do you want kisses on these too?"
    mc "Yes, [a]... *hmmh*"
    pause
    scene ch8_1028in with dissolve
    a "*Ahl..*"
    mc "Oh..."
    pause
    scene ch8_1029in with dissolve
    a "*Mnch*"
    mc "*A-ah...*"
    pause
    play sound "audio/mouth/french_kiss_07.ogg" volume 0.2
    scene ch8_1026 with dissolve
    a "*Hah...*"
    pause
    scene ch8_1019 with dissolve
    a "Hmmhm..."
    scene ch8_1020 with dissolve
    play sound "audio/mouth/french_kiss_02.ogg" volume 0.2
    a "*Hmhmm...*"
    scene ch8_1021 with dissolve
    a "*Mmhlm..*"
    image ch8_1020anim:
        "ch8_1020" with Dissolve(0.3)
        1.5
        "ch8_1021" with Dissolve(0.3)
        1.5
        repeat
    scene ch8_1020anim with dissolve
    play sound "audio/wavs/sfx/kissing_1.ogg" loop volume 0.2
    a "*Hmhah, hmlahmm...*"
    mc "So good, oh my god..."
    pause
    stop sound fadeout 0.5
    scene ch8_1022- with dissolve
    mc "(God, her way of looking at me... it's the look of a mature woman in need of dick, this is too hot!)"
    mc "( [a] could literally make me cum just by looking at me.)"
    pause
    a "What's wrong baby, why the serious face?"
    scene ch8_1022-- with dissolve
    mc "It just feels really good, I'm enjoying it a lot."
    a "That's good, honey."
    pause

init python:
    store.last_played_sound3 = None
    store.last_played_sound2 = None
    def ch8_alick_1_(trans, st, at):  
        trans.set_child("ch8_alick_1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
        if store.frame_num == 5:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()  
        if store.frame_num == 20:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()
        if store.frame_num == 12:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()  
        if store.frame_num == 27:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()                     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
screen ch8_alick_1_settings():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_alick_1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  


label beforech8_alick_1_1:
    $ anim_speed = 0.05
    image ch8_alick_1_:
        function ch8_alick_1_
    scene ch8_alick_1_ with dissolve
    a "*Lahlhh*"
    a "That's it, honey."
    a "Let your [arelat] [a] take care of these needs."
    mc "A-ah, [a], that feels so good..."
    mc "*Hmhmm*..."
    call screen ch8_alick_1_settings with dissolve
label afterch8_alick_1_:
    scene ch8_1022-- with dissolve
    a "This huge erection doesn't seem to want to go away, honey."
    mc "*Hmngh...* (That was close! One more second and I would've cum.)"
    mc "(I think she noticed and stopped so I wouldn't.)"
    a "We will have to take other measures..."
    a "It's been a while since I've done this, I hope I do it right."
    play sound "audio/wavs/bj_13.ogg"
    scene ch8_1022 with dissolve
    a "*Hmhmp*"
    mc "Ahh..."
    pause
    scene ch8_abj_pov1_17 with dissolve
    mc "Oh, wow, [a], this..."
    a "Shhh..."
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.stop_animation_at_frame_55 = False
    def ch8_abj_pov1_(trans, st, at):
        if store.stop_animation_at_frame_55 and store.frame_num == 55:
            return None
        trans.set_child("ch8_abj_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 57:
            store.frame_num = 1
        if store.frame_num == 53:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 17:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_50.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 1:
            sound_files = ["audio/wavs/a/abjmoan_4.ogg", "audio/wavs/a/abjmoan_17.ogg", "audio/wavs/a/abjmoan_11.ogg", "audio/wavs/a/abjmoan_12.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_abj_pov2_(trans, st, at):  
        trans.set_child("ch8_abj_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        if store.frame_num == 53:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 17:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_50.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 1:
            sound_files = ["audio/wavs/a/abjmoan_4.ogg", "audio/wavs/a/abjmoan_17.ogg", "audio/wavs/a/abjmoan_11.ogg", "audio/wavs/a/abjmoan_12.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_abj_pov3_(trans, st, at):  
        trans.set_child("ch8_abj_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        if store.frame_num == 53:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 17:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_50.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 1:
            sound_files = ["audio/wavs/a/abjmoan_4.ogg", "audio/wavs/a/abjmoan_17.ogg", "audio/wavs/a/abjmoan_11.ogg", "audio/wavs/a/abjmoan_12.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
screen ch8_abj_pov1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch8_abj_pov2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_abj_pov3_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_abj_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_abj_pov2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_abj_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch8_abj_pov3_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_abj_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch8_abj_pov3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch8_abj_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_abj_pov2_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch8_abj_pov1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
label beforech8_abj_pov1_1:
    image ch8_abj_pov1_:
        function ch8_abj_pov1_
    image ch8_abj_pov2_:
        function ch8_abj_pov2_
    image ch8_abj_pov3_:
        function ch8_abj_pov3_
    $ anim_speed = 0.05
    scene ch8_abj_pov1_ with Dissolve(0.3)
    a "*Slurp, slurp, slurp*"
    mc "Wow, [a]..."
    mc "Oh God... hmmhmm."
    mc "(She's sucking me hard... I can feel her tongue swirling around my glans with each suck.)"
    mc "(I'm going to cum very soon.)"
    mc "(A moment ago I was a little down because I couldn't fuck her, but now...) *Hmngh*."
    mc "(Not now!)"
    pause
    a "*Hmph, slurp, slurp*"
    scene ch8_1022-- with dissolve
    a "*Hah*, am I doing it right, honey?"
    mc "V-very well, [a]!, I was{w=0.4}, *Hmnh*{w=0.4}, about to cum."
    a "So soon, baby?"
    a "Hold on a little longer, honey."
    mc "Do you want me to hold on longer?"
    a "Y-yes, so you can... enjoy it more."
    mc "I-I'll try..."
    mc "(Tell me it's because you want to keep sucking it, [a], you don't have to pretend.)"
    scene ch8_1011- with dissolve
    a "I've never sucked one so big..."
    a "Well... [d] is the only one I've been with..."
    mc "And..."
    mc "Which one do you like more?"
    scene ch8_1014 with dissolve
    a "W-what do you mean?"
    mc "Between [d] and me, which do you prefer?..."
    a "..."
    scene ch8_1013anim with dissolve
    a "Don't ask me that, [mc]."
    pause
    scene ch8_1022-- with dissolve
    a "No one can find out about this, honey, okay?"
    a "Tomorrow we'll wake up and nothing will change between us."
    mc "No one will know about this, [a], you can trust me."
    a "I know, baby."
    a "I know I can always trust you."
    scene ch8_abj_pov1_ with dissolve
    a "*Slurp, schup, glug*"
    mc "Oh, god... this feels so good."
    mc "You suck it so well, [a], *hmngh*..."
    mc "You look beautiful sucking my cock."
    $ anim_speed = 0.03
    a " Hmmhm, *slurp, smnch, chup* "
    pause
    scene ch8_abj_pov2_ with dissolve
    a "Hmmhm, *slurp, slurp, slurp*"
    mc "Yes, keep going like that, hmmm..."
    a "*Slurp, slurp*, {i}Am I doing it right?"
    mc "Very well, hmhmm... excellently well, [a]."
    pause
    scene ch8_abj_pov3_ with dissolve
    a "Hmhmm... *slurp, slurp, chup*"
    mc "Hmmh, this is like a dream."
    mc "I'm in paradise right now..."
    a "*Slurp, slurp, smnch*"
    pause
    scene ch8_abj_pov1_ with dissolve
    call screen ch8_abj_pov1_ with dissolve

label ch8_abj_pov1_:
    scene ch8_abj_pov1_ with dissolve
    call screen ch8_abj_pov1_ with dissolve    
label ch8_abj_pov2_:
    scene ch8_abj_pov2_ with dissolve
    call screen ch8_abj_pov2_ with dissolve    
label ch8_abj_pov3_:
    scene ch8_abj_pov3_ with dissolve
    call screen ch8_abj_pov3_ with dissolve    




label afterch8_abj_pov1_:
    scene ch8_abj_pov1_ with dissolve
    $ store.stop_animation_at_frame_55 = True
    jump beforech8_abj2_pov2_



init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch8_abj2_pov1_(trans, st, at):  
        trans.set_child("ch8_abj2_pov1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
        if store.frame_num == 56:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()        
        if store.frame_num == 19:
            sound_files = ["audio/wavs/bj_63.ogg", "audio/wavs/bj_65.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 55:
            sound_files = ["audio/wavs/bjgags3.ogg", "audio/wavs/bjgags5.ogg", "audio/wavs/bjgags11.ogg"]
            sound_files2 = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_sound2 = renpy.random.choice([sound for sound in sound_files2 if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
            if random_chance > 0.1:
                store.last_played_sound3 = random_sound2
                atl_play_voicefx(random_sound2)()

        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_abj2_pov2_(trans, st, at):  
        trans.set_child("ch8_abj2_pov2_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
 
        if store.frame_num == 56:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()        
        if store.frame_num == 19:
            sound_files = ["audio/wavs/bj_63.ogg", "audio/wavs/bj_65.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 55:
            sound_files = ["audio/wavs/bjgags3.ogg", "audio/wavs/bjgags5.ogg", "audio/wavs/bjgags11.ogg"]
            sound_files2 = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_sound2 = renpy.random.choice([sound for sound in sound_files2 if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
            if random_chance > 0.1:
                store.last_played_sound3 = random_sound2
                atl_play_voicefx(random_sound2)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch8_abj2_pov3_(trans, st, at):  
        trans.set_child("ch8_abj2_pov3_{}".format(store.frame_num))

        store.frame_num += 1
        if store.frame_num > 60:
            store.frame_num = 1
 
        if store.frame_num == 56:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_voice(random_sound)()        
        if store.frame_num == 19:
            sound_files = ["audio/wavs/bj_63.ogg", "audio/wavs/bj_65.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 55:
            sound_files = ["audio/wavs/bjgags3.ogg", "audio/wavs/bjgags5.ogg", "audio/wavs/bjgags11.ogg"]
            sound_files2 = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_sound2 = renpy.random.choice([sound for sound in sound_files2 if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
            if random_chance > 0.1:
                store.last_played_sound3 = random_sound2
                atl_play_voicefx(random_sound2)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value    
screen ch8_abj2_pov1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch8_abj2_pov2_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_abj2_pov1_cumm") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

screen ch8_abj2_pov2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.5
        textbutton "Faster" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch8_abj2_pov1_") style "textbutton_choice"  

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch8_abj2_pov1_cumm") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  


label beforech8_abj2_pov2_:
    image ch8_abj2_pov1_:
        function ch8_abj2_pov1_
    image ch8_abj2_pov2_:
        function ch8_abj2_pov2_
    image ch8_abj2_pov3_:
        function ch8_abj2_pov3_
    $ anim_speed = 0.035
    scene ch8_abj2_pov1_ with dissolve
    pause 2.0
    a "*Gurg!* {w=0.5}{nw}"
    scene ch8_1023 with dissolve
    play voicefx "audio/wavs/a/abjmoanbreath.ogg" volume 0.5
    a "*Bah*"
    scene ch8_1014 with dissolve
    a "Sorry, I don't have much experience in this."
    a "I wanted to go deep but you're too big."
    mc "You can try again if you want."
    a "I'm going to make those unpleasant sounds if I choke, is that okay?"
    mc "That would turn me on even more..."
    scene ch8_1022- with dissolve
    a "Hmm, do you like it when I choke on your-"
    mc "I love it."
    a "You're so bad..."
    scene ch8_abj_pov1_38 with dissolve
    pause
    scene ch8_abj_pov1_45 with dissolve
    pause
    scene ch8_abj_pov1_58 with dissolve
    play sound "audio/wavs/bj_5.ogg" 
    pause
    scene ch8_abj2_pov1_38 with dissolve
    play sound "audio/wavs/bj_1.ogg" 
    pause
    scene ch8_abj2_pov1_52 with dissolve
    play sound "audio/wavs/bj_15.ogg" 
    pause
    play voicefx "audio/wavs/bj_5.ogg"
    $ renpy.pause(0.5, hard=True)
    play sound "audio/wavs/bjgags3.ogg" 
    scene ch8_abj2_pov1_1 with dissolve
    a "Ghug!"
    pause
    $ frame_num = 1
    scene ch8_abj2_pov1_
    a "*Slurg, slurp, gug*"
    mc "Hmhmm..."
    mc "You suck it so well, [a]..."
    a "Hmhm..."
    $ anim_speed = 0.02
    mc "Ah, [a]{w=0.4}, *hmngh!*{w=0.4}, I'm very close.."
    a "Hmm... *gug, slurp, slurp*"
    pause
    scene ch8_abj2_pov2_ with dissolve
    a "Hmmhmaah, *gugh, slurgp, slurgp*"
    mc "Oh, yeah...{w=0.4} *Hmhng!*."
    a "*Gagh, gugh, slurgp*"
    pause
    call screen ch8_abj2_pov2_ with dissolve

label ch8_abj2_pov1_:
    scene ch8_abj2_pov1_ with dissolve
    call screen ch8_abj2_pov1_ with dissolve
label ch8_abj2_pov2_:
    scene ch8_abj2_pov2_ with dissolve
    call screen ch8_abj2_pov2_ with dissolve

label ch8_abj2_pov1_cumm:
    $ anim_speed = 0.01
    mc "*!Hngh!*{w=0.4}, i-it's coming."
    mc "[a]..."
    mc "*Mnghh!*, (She doesn't hear me...)"   
    $ anim_speed = 0.01
    mc "*Hmngh!*"
    scene ch8_abj2_pov1_ with dissolve
    mc "*Hmnghmmhm!*"
    scene ch8_1037 with dissolve
    play voicefx "audio/wavs/bjgags8.ogg"
    a "*Gugh!*"
    scene ch8_1038 with dissolve
    play voicefx "audio/wavs/bj_7.ogg"
    play sound "audio/mouth/swallow_03.ogg"
    a "Blrgh?"
    scene ch8_1039 with dissolve
    play sound "audio/wavs/bj_63.ogg"
    a "Hmm..."
    scene ch8_1040 with cumming
    play voicefx "audio/wavs/bj_1.ogg"
    mc "*Hmgh!*"
    scene ch8_1039 with dissolve
    play sound "audio/wavs/bj_65.ogg"
    pause
    scene ch8_1040 with dissolve
    play sound "audio/wavs/bj_3.ogg"
    mc "*Nghh*"
    scene ch8_1039 with dissolve
    play sound "audio/wavs/bj_67.ogg"
    pause
    scene ch8_1040 with dissolve
    play sound "audio/wavs/bj_5.ogg"
    mc "*Nghh*"
    pause 0.5
    scene ch8_1041 with cumming
    play sound "audio/wavs/a/abjmoanbreath.ogg"
    mc "*Arghhh!*" with flash
    pause
    scene ch8_1041- with dissolve
    mc "(Shit, she swallowed some, I heard it!... I hope she's not mad about this.)"
    a "..."
    pause
    scene ch8_1042 with dissolve
    a "*Huh...*"
    mc "(Fuck, I came so much in her mouth...)"
    mc "(Please don't be mad!)"
    pause
    mc "S-sorry, [a], it felt so good that I couldn't control it."
    scene ch8_1043 with dissolve
    a "D-don't worry, honey."
    a "That was the goal after all."
    a "-I mean making you cum, not..."
    mc "I got it."
    a "O-okay, erm..."
    a "You're satisfied now, honey?"
    mc "More than satisfied, I could not explain how good I feel now."
    a "I-I'm glad for you..."
    a "So..."
    a "I'll clean this up."
    $ renpy.end_replay()
    pause
    scene ch8_1043- with dissolve
    mc "(I can't believe this happened.)"
    mc "(I came in her mouth and I think she liked it.)"
    mc "(Or at least I didn't see any expression of disgust on her face.)"
    a "Do you want some tissues too, honey?"
    mc "Yes, please, I'll go get them, [a]."
    a "Don't worry, I should have some in my makeup drawer."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    scene ch8_1044 with dissolve
    mc "Well, I'll let you sleep now."
    a "I'll remove my makeup and take a shower first."
    mc "I'll shower tomorrow morning, right now I'm too tired."
    a "You worked today, of course you're going to be tired."
    mc "Yes."
    mc "I really enjoyed this, [a]."
    a "Me too, honey."
    mc "Goodnight."
    a "Goodnight, rest well."
    mc "..."
    pause
    a "What's wrong?"
    mc "Aren't you forgetting something?"
    a "Hmmm..."
    pause
    play music sexy3 fadein 2.0
    scene ch8_1045 with dissolve
    a "*Mmuah*, {i}you're such a spoiled boy, *giggles*."
    image ch8_end:
        "chapterendend" with Dissolve(1.5)
        1.0
    scene ch8_end with Fade(1.0,0.5,0.5)
    $ renpy.pause(0.5, hard = "True")     
    scene chapterend with Dissolve(2.0)
    call screen chapter8end with Dissolve(2.0)










    








    


