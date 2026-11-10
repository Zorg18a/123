label ch10at:
    $ disable_even_frames()
    stop background fadeout 0.5
    stop music fadeout 0.5
    stop sound
    scene blackscreen with dissolve
    pause
    a "Sweetie, take your [drelat] to his room, please. I’ll take [s]."
    pause
    a "Wake up, we’re home now."
    a "I can’t carry you, you’re too heavy already."
    s "{i}Yawn..." # said sleepily
    a "Come on, get up."
    s "Where’s [mc]?"
    a "I’m taking him to his room."
    k "[drelatks!cl], wake up."
    d "Yeah, yeah, I’m up, *hic*." # drunk
    k "Help me get him up."
    mc "Uhm... Zzz..."
    pause
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    a "[mc], wake up, honey."
    a "[mc]."
    play music scene1 fadein 2.0
    scene ch10_1 with Dissolve(2.0)
    mc "What...?" # said sleepily
    a "We’re home."
    mc "Oh... yeah..." # said sleepily
    a "Here, let me help you."
    scene ch10_2 with dissolve
    a "Lean on me, [mc]."
    d "[k], you’re gonna make me fall!"
    camera:
        subpixel False
        zoom 1.0
        xalign 0.5
        yalign 0.5
    scene blackscreen with dissolve
    pause
    scene ch10_3 with dissolve:
        zoom 0.75
    k "Don’t let go of him, [mia]."
    a "Do you need help?"
    d "N-no need, I can walk on my own."
    d "O-or better yet, just leave me on the couch."
    k "Nope, we’re taking you to your room."
    d "Take me to the downstairs bathroom, I wanna wash my face."
    a "[s] is showering there. You have to go upstairs."
    k "You heard her, we gotta take the stairs."
    mia "Hold on tight, Mr. [d]."
    scene ch10_4 with dissolve:
        zoom 0.75
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    a "You should go wash your face too, at least. Sleeping with all that salt isn’t good for your skin or your hair."
    mc "Uh..." #said drunkenly
    d "Girls, slow down. *hic*"
    a "Come on, let’s go upstairs. Wash your head and then straight to your room."
    mc "Yeah..."
    scene ch10_5 with dissolve:
        zoom 0.75
    a "No, no, [mc]. You need to turn around. You won’t make it up the stairs walking backwards."
    mc "Uh..."
    a "Don’t worry, I’ve got you from behind."
    scene ch10_6 with dissolve:
        zoom 0.75
    d "Girls, help [mc], I’m fine."
    k "[arelatks!cl] is taking care of him."
    camera:
        subpixel False
        zoom 1.0
        xalign 0.5
        yalign 0.5
label ch10a1:
    if _in_replay:
        play music scene1 fadein 2.0
    scene ch10_7 with dissolve:
        zoom 0.75
    d "Ouch, [k]!, *hic*. L-let go of me right now!"
    k "I need to get your head under the faucet!"
    scene ch10_8-- with dissolve
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    a "Come in, [mc]."
    mc "Okay."
    scene ch10_9 with vpunch:
        zoom 0.75
    mc "Whoa!"
    scene ch10_10 with dissolve:
        zoom 0.75
    a "[mc]!"
    mc "The floor’s slippery..."
    a "That’s why I hate when you drink. You don’t know your limits."
    a "Just sit down."
    mc "Uhm... On the floor?"
    a "Yes, on the floor."
    scene ch10_11 with dissolve
    mc "Alright..."
    mia "[mc] is totally wasted, haha."
    mia "I think he’s gonna need someone to give him a shower." #looking at k joking around
    k "Yeah, haha."
    mia "..."
    k "{size=-6}Who, me?"
    k "Shut up."
    #k looks at mia clearly bothered by the comment
    scene ch10_13 with dissolve
    a "[mia]’s right, [mc]."
    mia "Aww, he still needs his [arelat] to take care of him."
    play background "audio/shower.ogg" fadein 0.2 loop volume 0.75
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_12 with hpunch
    mc "Haah! It’s freezing! *hic*" #A opens the cold water
    stop background fadeout 0.5
    a "Oops! Wrong knob, heh..."
    image ch10_14anim:
        "ch10_14" with dissolve
        3.0
        "ch10_15" with dissolve
        1.0
        repeat
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_14anim with dissolve
    a "*Hmph!*"
    a "Who tightened the hot water so much?"
    d "I did, honey. It drips if we don’t close it tight."
    a "*Hmngh*"
    scene ch10_15- with dissolve
    mc "Let me help you."
    a "Careful, [mc]."
    scene ch10_16 with dissolve
    mc "I’m not thaaat drunk... {w=0.5}*hic*"
    a "Yes, you are."
    scene ch10_17 with dissolve
    pause
    show ch10_17 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    mc "*Hmnghh!*"
    a "You’re not gonna make it. Let me try one more time."
    play background "audio/shower.ogg" fadein 0.2 loop volume 0.2
    scene ch10_17 with hpunch
    a "Haah! Close it!" #water
    a "[mc]!"
    stop background fadeout 0.5
    scene ch10_18 with dissolve:
        subpixel True
        xalign 0.5 yalign 1.0 zoom 1.0
        ease 4 yalign 0.0 zoom 0.75
    $ renpy.pause(4.0, hard=True)
    mc "Oh... Haha."
    mc "At least you got the hot water. *hic*"
    scene ch10_18- with vpunch
    mc "Whoa!" 
    a "[mc]!"
    a "Lean on the wall, I’ll go get something for you to sit on."
    scene ch10_19 with dissolve
    d "A-alright, *hic*, enough! You’re just messing around..."
    k "Hahaha, I was helping you."
    
    scene ch10_20 with dissolve
    mia "Was he really mad?"
    k "Nah, the old man’s just sleepy."
    d "I’m still in my forties!"
    a "[k], that man is going to hurt himself. Go help him."
    k "Are you two gonna take long?"
    a "[mc] needs to take a shower. Go use the downstairs bathroom."
    k "Let’s go."
    scene ch10_21 with dissolve
    pause
    scene ch10_22 with vpunch
    a "Oww!"
    mc "[arelat!cl] [a]!"
    scene ch10_22-- with dissolve
    mc "Wha... *hic*, what happened?"
    a "Honey, help me up."
    camera:
        xalign 0.5 yalign 0.5 zoom 1.0
    scene ch10_22---
    a "The girls left the floor all wet."
    mc "Are you okay?"
    a "Yeah, it was just the fall."
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_23 with dissolve
    mc "Up you go."
    a "Thanks, [mc]."
    scene ch10_24 with dissolve:
        subpixel True
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 3 zoom 1.02
        ease 3 zoom 1.0
        repeat
    a "Hahaha."
    mc "Are you sure you didn’t drink too?"
    a "Maybe I did and just forgot..."
    scene ch10_25 with vpunch
    mc "Whoa!"
    a "Careful! Hahaha."
    mc "I’m slipping!"
    a "[mc], get up! Hahaha."
    mc "*Hic* I can’t!"
    "Hahaha."
    scene ch10_24 with dissolve
    mc "You’re soaked."
    a "Yeah, and it’s your fault! You’re soaked too."
    mc "Also your fault."
    scene ch10_26 with dissolve
    a "Oh my god, I’m such a klutz. And it’s freezing in here."
    a "I better take off this skirt or I’m gonna catch a cold."
    scene ch10_27 with dissolve:
        subpixel True
        xalign 0.5 zoom 0.75
        ease 6 yalign 1.0
        ease 6 yalign 0.0    
        repeat
    a "When you take your clothes off, leave them here on the floor so I can throw everything in the wash together." #removes her skirt
    mc "Okay."
    scene ch10_28 with dissolve
    a "Alright, alright, let’s get in the shower before we crack a tile with our butts."
    scene ch10_29 with dissolve
    pause
    a "Huh?"
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_30 with dissolve
    mc "Hm?"
    a "Uhm... no, it’s just that..."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_31:
        zoom 0.5
    a "Whaaat?!"
    pause
    mc "Whaaat?!"
    scene ch10_32 with dissolve:
        zoom 0.5
    pause
    scene ch10_33 with hpunch
    a "No!"
    a "[mc]!"
    mc "What?"
    scene ch10_33_1 with dissolve
    a "Oh god, how could you all let me walk around the beach like this?!"
    a "How embarrassing!"
    #A looks at mirror
    a "{i}I-It looks like I’m wearing a thong!"
    mc "That’s not true!"
    mc "Your thong looks amazing on you!"
    scene ch10_33_2 with hpunch
    a "{i}Shhh! I-it’s not a thong."
    scene ch10_33_1 with dissolve
    a "God, [d] was right, I should’ve listened to him..."
    mc "Then why’d you put on a thong?!"
    scene ch10_33_2 with hpunch
    a "{i}Lower your voice! It’s not a thong!"
    scene ch10_33_1 with dissolve
    a "[s] was rushing me, and I only looked at the top part."
    mc "I like it."
    scene ch10_34 with dissolve
    a "Come on, into the shower."
    pause
    stop music fadeout 1.5
    scene blackscreen with dissolve
    pause
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    play music sexy3 fadein 1.5
    play background "audio/shower.ogg" fadein 1.5 loop volume 0.2
    scene ch10_34- with Dissolve(1.5)
    mc "*Hic*, I can do it, go to bed."
    a "No, [mc]. I’m not leaving you alone like this."
    a "Besides, I want to shower too, and if I let you do it alone, either you won’t manage or you’ll take forever."
    pause
    a "Or... are you feeling shy?"
    scene ch10_35
    a "Don’t tell me you’re shy in front of your [arelat]."
    a "Hmm?"
    a "Don’t worry, I like looking after my spoiled [arelatmc] sometimes."
    pause
    a "[mc]?"
    mc "Huh, whah...?"
    a "I said{w=0.5} -never mind..."
    a "[mc], don’t drink so much. I don't like seeing you like this, it just makes me...{w=0.5} sad."
    mc "It was [drelat] [d]'s idea..."
    pause
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_36
    mc "Are you mad?"
    a "No, I just really don’t like seeing you this drunk. You remind me of..."
    pause
    mc "Of who?"
    a "Of your [drelat] [d]."
    a "You both get just as silly when you drink."
    pause
    mc "Sorry."
    scene ch10_37 with dissolve
    a "It’s okay. You’re an independent man now, you have a job... So, what I think doesn’t really matter."
    pause
    a "Wash behind your ears."
    mc "Yeah..."
    scene ch10_38 with dissolve
    a "Here."
    a "To rinse the sand off."
    scene ch10_39-- with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 0.5
        parallel:
            ease 5 zoom 1.0
        parallel:
            ease 3 yalign 1.0
    pause
    mc "[arelat!cl] [a], that bikini looks amazing on you..."
    a "Thanks..."
    pause
    "..."
    scene ch10_39--- with dissolve:
        subpixel True
        xalign 0.5 yalign 1.0 zoom 1.0
    pause
    a "And...?"
    a "Is that all?"
    show ch10_39--- with nothing:
        subpixel True
        xalign 0.5 yalign 1.0 zoom 1.0
        ease 2 yalign 0.0 zoom 0.95

    mc "Whuh..?"
    a "I thought you wanted to say something else."
    show ch10_39--- with nothing:
        subpixel True
        ease 5 zoom 0.5
    mc "Uhm..."
    mc "Nope... *hic*"
    pause
    a "Making me walk around like this on the beach... I won’t forget, okay?"
    mc "What, why? *hic*"
    a "Yeah, pretend you don’t see the problem..."
    show ch10_39--- with nothing:
        subpixel True
        pause 1.5
        parallel:
            ease 2 yalign 1.0
        parallel:
            ease 5 zoom 1.0
    a "Look how tight the bottom is on me..."
    a "It barely covers anything, just a little triangle..."
    mc "Yeah, I see..."
    mc "But the real issue isn’t the bikini. It’s that you’ve got a big butt, [arelat] [a]."
    mc "Not that it’s a problem, but..."
    pause
    a "[mc], what are you staring at, hmm?"
    show ch10_39--- with nothing:
        subpixel True
        ease 5 yalign 0.0
    pause 1.0
    mc "It’s just...{w=1.0} I can’t help it. You’ve got a great ass."
    a "[mc], did you really just say that?"
    mc "Uh, I meant it respectfully. *hic*"
    a "*Giggle*{w=0.75}{nw}"
    scene ch10_40 with dissolve
    pause
    mc "{i}(She’s leaving...)" with dissolve
    mc "(That sucks, I was just starting to enjoy it...)" with dissolve
    scene ch10_41 with dissolve
    pause
    mc "{i}(My hair... it’s all stiff from the sea salt.)" with dissolve
    mc "{i}(It’s so tangled. I need some shampoo.) {/i}*Hic*" with dissolve
    scene ch10_39- with dissolve
    mc "(I feel like I’m gonna fall, I can’t keep my balance.)" with dissolve
    mc "(My stomach’s not feeling too great either.)" with dissolve
    scene ch10_41 with dissolve
    mc "(Ouch, shampoo’s getting in my eyes.)" with dissolve
    scene blackscreen with dissolve
    mc "(I’m so sleepy...)" with dissolve
    pause
    mc "(I need to be careful or...{w=0.5} or I might...{w=0.5} I might fall asleep..)" with dissolve
    a "Are you using conditioner?{w=1.0}{nw}"
    scene ch10_42 with hpunch
    mc "{size=+5}Ah!"
    a "What’s wrong? Don’t yell."
    mc "I thought you’d left."
    a "N-no, I just went to make sure the door was locked..."
    scene ch10_43 with dissolve
    a "I told you I was going to help you."
    pause
    mc "I don’t really feel drunk anymore."
    a "Uh-huh..."
    a "You just dozed off and earlier you slipped."
    a "If I hadn’t been here, you could’ve cracked your head open..."
    mc "It’s just that the floor was really slippery."
    a "Sure it was..."
    mc "You slipped too."
    a "But I slipped 'cause I’m clumsy, *giggle*."
    pause
    a "Hand me the body wash."
    mc "The what?"
    a "Never mind."
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_44-
    a "I don't want you slipping again."
    pause
    scene ch10_45_1 with vpunch
    a "Oh!"
    pause
    a "T-the floor really is a bit slippery, heh..."
    mc "(Her body... it’s as soft and squeezable as always...)" with dissolve
    scene ch10_46 with dissolve
    a "Thanks for catching me, sweetheart."
    mc "*Lmch*... Don’t mention it." #mc can’t resist giving her body a little lick while soaping her
    pause
    scene ch10_47 with dissolve
    pause
    scene ch10_48 with dissolve
    mc "Hmm..."
    a "..."
    pause
    scene ch10_49 with dissolve
    a "You’re gonna make me fall, [mc]."
    a "Look how much sand you still have on your back..."
    pause
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_50 with dissolve
    mc "Are you going to shower me?"
    a "That’s what we’re doing."
    mc "Oh, okay."
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_50-
    mc "Did you say you’re gonna shower too?"
    a "After I’m done with you."
    mc "Can you give me some soap?"
    pause
    scene ch10_52--
    a "Uhm... [mc]?"
    mc "It’s important to save water, [arelat] [a]."
    a "That’s true..."
    scene ch10_52- with dissolve
    mc "*Lahm*, I wanna help you too... wash your body, *lmh*..."
    scene ch10_50-- with dissolve
    mc "*Smch*, hmm.."
    image ch10_52anim:
        "ch10_52--" with dissolve
        1.0
        "ch10_52-" with dissolve
        1.0
        "ch10_50--" with dissolve
        1.0
        repeat
    scene ch10_52anim with dissolve
    mc "Hmmh..."   
    a "[mc], are you...?"
    a "Are you kissing me?"
    mc "Yeah, *hmch*."
    a "*Giggle*{w=0.5}{nw}"
    a "You little rascal..."
    pause
    mc "*Hmch*, [arelat] [a]..."
    mc "*Hmmf*... your ass is just...{w=0.5} wow."
    a "Ahem..."
    pause
    a "{i}{size=-5}K-keep your voice down when you say things like that..." #she says it because they’re showering while everyone sleeps.
    pause
    mc "Right... you’re married..."
    a "*Giggle*{w=0.5}{nw}"
    pause
    mc "{size=-3}{i}I love touching your legs, squeezing them and kissing them... they’re so sexy..."
    a "Shhh... Okay, let’s stop that now,"
    a "Remember, you’re drunk."
    scene ch10_54_3
    pause
    a "You’ve got a nice back..."
    pause
    a "Toned..."
    scene ch10_54_2
    a "Very manly..."
    pause
    scene ch10_54_1
    a "Sit up straight or you'll fall back."
    mc "Yeah, *mnch*."
    image ch10_54anim:
        "ch10_54_3" with dissolve
        1.0
        "ch10_54_2" with dissolve
        1.0
        "ch10_54_1" with dissolve
        1.0
        repeat
    scene ch10_54anim with dissolve
    pause
    mc "*Hmch*"
    mc "*Lhm, smnch*"
    mc "Kisses are one hundred percent necessary *hic*, I mean it..."
    a "{size=-5}*Giggle*{w=0.5}{nw}"
    pause
    a "It feels nice..."
    a "Like a massage."
    pause
    mc "Are you sleeping in your room tonight?" 
    a "I heard the girls took your [drelat] there, so I don’t think I will."
    mc "I see..."
    a "Mhm..."
    pause
    mc "Why don’t you sleep with me tonight, [arelat] [a]?"
    a "Shh..."
    pause
    mc "Seriously, my bed is way more comfortable than the couch."
    a "I’m sure it is..."
    mc "So?"
    a "I’m fine, sweetheart, maybe another day..."
    mc "My bed’s always open for you, anytime."
    mc "My bed and me, *hic*."
    scene ch10_55 with dissolve
    a "Thanks, it’s good to know..."
    a "You can come sleep with me on the couch if you want."
    mc "S-*hic*, sure..."
    pause
    a "Maybe tomorrow?"
    a "You’re way too drunk tonight."
    mc "As you command, my queen..."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_56
    a "*Giggle*{w=0.5}{nw}"
    pause
    a "I’m laughing, but that doesn’t mean I like seeing you like this." #referring to seeing him drunk
    mc "Uh, yeah..."
    a "I’m not mad because it was with your [drelat] and we where there."
    a "Just make sure it doesn’t become a habit."
    mc "Yes, [arelat] [a]...{w=0.5} {i}uh..."
    a "Look at all this sand..."
    pause
    scene blackscreen with Dissolve(1.5)
    a "Are you asleep?"
    mc "Hnh..."
    a "It’s okay, just don’t fall over."
    image ch10_56anim:
        "ch10_56---" with dissolve
        1.0
        "ch10_56-----" with dissolve
        1.0
        repeat
    scene ch10_56anim with dissolve
    mc "What?"
    a "You’re falling asleep."
    pause
    scene ch10_57 with dissolve
    mc "I’m so sleepy, and the warm water… I’m getting really comfy..."
    mc "Your hands… this feels nice… really relaxing..."
    pause
    scene ch10_58 with dissolve
    mc "..."
    pause
    scene ch10_59 with dissolve #mc can't stop looking at Amelie's tits in that bikini while she washes his body.
    a "..."
    mc "You should take your top off too."
    pause
    scene ch10_57 with dissolve
    mc "It’s soaking wet, you’re gonna catch a cold."
    a "Uhm...{w=0.5} yeah, you’re right."
    a "I was just thinking the same thing."
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_61
    pause
    a "Did [d] say he was going to shower?"
    mc "I don’t think so."
    a "He said he was going to bed, right?"
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_62
    pause
    mc "They look great..."
    mc "Your face is beautiful, and your body’s a perfect ten."
    a "And you’re a very charming young man."
    mc "[arelat!cl] [a], if you wanted to, you could have the whole world at your feet, *hic*."
    a "Sweetheart, I can’t even get a discount at the grocery store."
    scene ch10_63 with dissolve
    mc "Where’s the soap?"
    a "It’s behind you."
    pause
    scene ch10_64 with dissolve
    a "Ah, it’s for me..."
    scene ch10_65 with dissolve
    mc "You wash me, and I’ll wash you."
    image ch10_65anim:
        "ch10_64" with dissolve
        1.0
        "ch10_65" with dissolve
        1.0
        repeat
    image ch10_67anim:
        "ch10_66" with dissolve
        1.25
        "ch10_67" with dissolve
        1.25
        repeat
    scene ch10_65anim with dissolve
    a "Alright, sounds like a fair deal."
    pause
    a "Why did you and your [drelat] have to start drinking?"
    mc "I don’t know, it was his idea."
    mc "Rum was my dad’s favorite."
    mc "At least that’s what [drelat] [d] said. I didn’t really feel like it."
    a "Oh... In that case, it’s okay."
    pause
    a "Hey, what were you guys singing?"
    mc "{i}{size=+10}''In the quiet of the night, I sit alooone!!''" with hpunch
    a "Shh... {i}I asked what song it was, not for you to sing it."
    mc "Oh..."
    a "Silly boy..."
    pause
    mc "It’s a song that my [drelat] [d] and I heard the other day in the garage while I was helping him with his car."
    a "That man..."
    pause
    a "Your [drelat] [d] doesn’t even know what he wants..."
    scene ch10_66 with dissolve
    mc "Your skin is so soft..."
    scene ch10_67 with dissolve
    pause
    scene ch10_66 with dissolve
    a "*Giggle*"
    pause
    scene ch10_65anim with dissolve 
    mc "What’s wrong?"
    a "{i}{size=-3}Took you long enough..."
    mc "Took me long enough for what?"
    pause
    a "Oh, [mc]... I’ll say it again, don’t drink like that anymore, you can’t handle alcohol at all."
    scene ch10_67 with dissolve
    mc "You know what else I can’t handle?"
    a "*Giggle*{w=0.8}{nw}"
    pause
    mc "[arelat!cl] [a], you looked really beautiful on the beach today..."
    a "Just today?"
    scene ch10_66 with dissolve
    mc "N-no, you’re beautiful always, it’s just that...{w=0.5} *hic*...{w=0.5} today you look even more stunning."
    scene ch10_67anim with dissolve
    mc "I mean... you’re really beautiful."
    mc "You’re more beautiful than...{w=0.5} the most beautiful woman ever, uh..."
    mc "You’re like a really pretty flower that’s...{w=0.5} really pretty and..."
    pause
    mc "I can’t think of anything else..."
    scene ch10_65anim with dissolve
    a "{size=-4}*Giggle*{w=0.5}{nw}"
    mc "I’m way too drunk, [arelat] [a]..."
    a "Yeah, I can tell..." 
    pause
    a "You turn into a poet when you’re drunk."
    mc "You are poetry."
    a "Oh..."
    pause
    a "I actually liked that one..."
    pause
    mc "Everything’s spinning..."
    pause
    mc "[arelat!cl] [a], your bra..."
    a "You want me to take it off?"
    scene ch10_67 with dissolve
    mc "Yes."
    scene ch10_67- with dissolve
    a "Alright then..."
    pause
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_68 with dissolve
    mc "I still need to wash these two..." #referring to Amelie’s tits
    pause
    scene ch10_69 with dissolve
    mc "Wow..."
    pause
    a "I’m getting cold, sweetheart..."
    mc "I was just admiring your... *hic*, sorry."
    mc "I’ll keep going now."
    scene ch10_71_4__ with dissolve
    pause
    mc "These tits are out of this world..."
    pause
    mc "Now I'm going to wash them lustfully... if that’s okay with you."
    a "*Giggle*{w=0.5}{nw}"
    scene ch10_70_2 with dissolve
    a "Lu-lustfully? O-okay..."
    mc "Hmm... wow..."
    pause
    scene ch10_70 with dissolve
    mc "Oh... hmm..."
    pause
    image ch10_70anim:
        "ch10_71_4__" with dissolve
        1.1
        "ch10_70_2" with dissolve
        1.1
        "ch10_70" with dissolve
        1.1
        repeat
    scene ch10_70anim with dissolve
    mc "They’re so soft and warm... just how I like them..."
    a "*Giggle*{w=0.5}{nw}"
    pause
    a "Don’t squeeze too hard, sweetheart."
    pause
    mc "I’d never hurt you, *hic*..."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_71_2- with dissolve
    mc "Quite the opposite..."
    scene ch10_71_4_ with dissolve
    mc "All I can think about is how to make you happy."
    scene ch10_71_3 with dissolve
    a "Aww..."
    image ch10_71anim:
        "ch10_71_2-" with dissolve
        1.5
        "ch10_71_4_" with dissolve
        1.5
        "ch10_71_3" with dissolve
        1.5
        repeat
    scene ch10_71anim with dissolve
    pause
    a "Even drunk, you can say things like that..."
    mc "I always say dumb things when I’m drunk."
    a "Those aren’t dumb things, [mc]..."
    pause
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_75_1- #mc starts sucking on her breasts.
    a "..."
    pause
    scene ch10_75_2- with dissolve
    a "Hey..."
    a "You’re licking the soap."
    pause
    scene ch10_75_3- with dissolve
    mc "*Smnch, mhmp*"
    pause
    image ch10_75anim:
        "ch10_75_2-" with dissolve
        0.8
        "ch10_75_3-" with dissolve
        0.8
        "ch10_75_2-" with dissolve
        0.8
        "ch10_75_3-" with dissolve
        0.8
        "ch10_75_2-" with dissolve
        0.8
        "ch10_75_3-" with dissolve
        0.8
        "ch10_75_1-" with dissolve
        0.8
        repeat
    scene ch10_75anim with dissolve
    play soundfx "audio/kissing_1.ogg" fadein 0.5 loop volume 0.5
    $ renpy.music.set_audio_filter("voicefx", [reverb_bathroom_af, af.Highpass(1000)])
    $ renpy.music.set_audio_filter("voicefx2", [reverb_bathroom_af, af.Highpass(1500)])
    a "You’re so drunk you don’t even notice the taste."
    pause
    mc "They taste good."
    a "*Uh*..."
    scene ch10_76_1 with dissolve
    pause
    scene ch10_76_2 with dissolve
    a "*Hm..*"
    pause
    scene ch10_76_3 with dissolve
    pause
    scene ch10_76_4 with dissolve
    a "Uh, [mc]..."
    pause
    image ch10_76anim:
        "ch10_76_1" with dissolve
        1.0
        "ch10_76_2" with dissolve
        1.0
        "ch10_76_1" with dissolve
        1.0
        "ch10_76_2" with dissolve
        1.0
        #
        "ch10_76_3" with dissolve
        1.0
        "ch10_76_4" with dissolve
        1.0
        "ch10_76_3" with dissolve
        1.0
        "ch10_76_4" with dissolve
        1.0
        "ch10_76_3" with dissolve
        1.0
        "ch10_76_4" with dissolve
        1.0
        repeat
    scene ch10_76anim with dissolve
    a "Hmm..."
    a "..."
    pause
    mc "So delicious..."
    a "Uh, [mc]..."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_72
    a "You look like a hungry baby..."
    scene ch10_73 with dissolve
    mc "*Hmmch*" 
    scene ch10_73- with dissolve
    mc "[arelat!cl] [a]..."
    a "Yes, sweetheart?"
    scene ch10_73-- with dissolve
    a "Don’t suck too hard or you’ll leave a mark."
    image ch10_72fpanim:
        "ch10_72" with dissolve
        1.0
        "ch10_73" with dissolve
        1.0
        "ch10_72" with dissolve
        1.0
        "ch10_73" with dissolve
        1.0
        "ch10_72" with dissolve
        1.0
        "ch10_73" with dissolve
        1.0
        #
        "ch10_73-" with dissolve
        1.0
        "ch10_73--" with dissolve
        1.0
        "ch10_73-" with dissolve
        1.0
        "ch10_73--" with dissolve
        1.0
        "ch10_73-" with dissolve
        1.0
        "ch10_73--" with dissolve
        1.0
        repeat
    scene ch10_72fpanim with dissolve
    mc "Hmh..."
    a "Are you biting?"
    mc "Just a little... I love your delicious pink nipples..."
    pause
    mc "Uh...?" 
    stop soundfx fadeout 0.5
    scene ch10_77 with dissolve
    pause
    scene ch10_78 with dissolve
    a "Uhm..."
    pause
    scene ch10_79 with dissolve
    a "Let me take off your shorts, honey. They must be full of sand."
    scene ch10_79:
        pause 1.0
        xalign 0.5 yalign 0.5
        ease 2 zoom 1.1
        ease 2 zoom 1.0
    a "Lift your butt a little... there you go." #she makes mc lift himself slightly to remove his shorts
    pause
    scene ch10_80 with dissolve
    mc "Oh, my underwear came off too, *hic*."
    a "How else are you gonna get the sand off your butt if you're still wearing them?"
    mc "That’s...{w=0.5} true..."
    scene ch10_80 with fade
    a "You're falling asleep again."
    mc "Huh...?"
    a "I said you’re nodding off."
    mc "No, I..."
    scene blackscreen with dissolve
    scene ch10_81 with fade
    scene blackscreen with Dissolve(2.0)
    pause
    "..."
    a "[mc], sweetheart..."
    a "Are you asleep...?"
    pause
    scene ch10_81 with dissolve
    pause
    scene blackscreen with dissolve
    pause
    scene ch10_81 with dissolve
    pause
    scene ch10_82 with dissolve
    pause
    scene ch10_83 with dissolve
    pause
    scene ch10_84 with dissolve
    pause
    scene ch10_84-
    pause
    image ch10_84anim:
        "ch10_82" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        "ch10_82" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        "ch10_83" with dissolve
        1.0
        "ch10_84" with dissolve
        1.0
        repeat
    scene ch10_84anim with dissolve
    mc "(She’s...{w=0.5} she’s washing my penis...)" with dissolve #with his eyes half-closed, he can see Amelie washing his groin and flaccid penis; in parentheses indicates a thought.
    pause
    mc "(This would usually get me rock hard...)" with dissolve
    mc "(Must be the alcohol...)"
    pause
    mc "(It tickles.)" with dissolve
    mc "(It almost feels like she’s jerking me off... I must have a ton of sand there.)" with dissolve
    pause
    scene ch10_85 with dissolve
    pause
    scene ch10_86 with dissolve
    pause
    play voicefx "audio/showershot.ogg" volume 0.6
    scene ch10_87 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    pause 7
    stop voicefx fadeout 1.5
    scene ch10_88intel with dissolve
    mc "Hah... *Cough, cough*, water went up my nose."
    a "Erm, s-sorry sweetheart! I-I thought you were asleep, heh..."
    a "Heh... Erm, you’re all done now, I’ll go get a towel."
    scene ch10_89intel with dissolve
    mc "You're not done yet."
    a "Huh?"
    a "Oh, right, erm... I’ll shower after you’re out." #she said nervously
    scene ch10_90-intel with dissolve
    mc "We agreed I was gonna do it."
    scene ch10_91intel with dissolve
    a "O-okay..."
    pause
    scene ch10_89intel with dissolve
    pause
    image ch10_92anim:
        "ch10_90-intel" with dissolve
        1.25
        "ch10_91intel" with dissolve
        1.25
        "ch10_89intel" with dissolve
        1.25
        repeat
    scene ch10_92anim
    a "M-make sure you clean me really well, okay? Heh..."
    mc "Of course..."
    mc "I’ve got my ways..."
    pause
    mc "What was that just now...?"
    mc "Were you touching me while I was asleep?"
    a "M-me?"
    a "..."
    pause
    a "Leaving sand down there isn’t good... it’ll irritate you."
    mc "Hmm..."
    pause
    mc "I see what you’re doing..."
    mc "I know you like teasing me, [arelat] [a]."
    mc "Because you know I like you."
    mc "And even if you say you don’t, I know you like me... Yeah, you totally do."
    mc "If you didn’t, then why do you let me touch you, huh? Heh..."
    pause
    a "O-once we’re done, you’re going straight to bed, got it?"
    mc "Yeah...{w=0.5} I mean, no."
    mc "I don’t wanna sleep, I wanna keep touching you, even if you won’t let me fuck you, at least I’m having a great time."
    a "{i}{size=-3}Shhh... stop it, [mc]."
    mc "This ass *hic* belongs to me now."
    menu:
        "Bury your face":
            camera:
                subpixel False
                zoom 1.0 xalign 0.5 xalign 0.5
            scene ch10_93
            mc "Now I get what you’re after, [arelat] [a]."
            a "Huh?"
    scene ch10_94 with dissolve
    a "[mc]..."
    mc "These, uhm, are in the way..."
    pause
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_95
    mc "Muah..."
    mc "This is what you want, isn’t it?"
    mc "You shouldn’t-*hic*{w=0.5}, feel shy about asking for it. I’ll gladly do it."
    pause
    scene ch10_98 with dissolve
    mc "Phew..."
    a "..."
    pause
    image ch10_99z:
        subpixel True
        "ch10_99nvidia"
        zoom 1.0 xalign 0.5
        ease 0.5 zoom 1.005
        ease 0.5 zoom 1.01
        ease 0.5 zoom 1.005
        ease 0.5 zoom 1.0
        repeat
    scene ch10_99z:
        subpixel True
        yalign 0.0 xalign 0.5
        ease 0.5 yalign 1.0
        ease 0.5 yalign 0.0
        ease 0.5 yalign 1.0
        ease 0.5 yalign 0.0
        repeat
    $ renpy.music.set_audio_filter("voicefx2", reverb_bathroom_af)
    $ renpy.music.set_audio_filter("sound", reverb_bathroom_af)
    $ renpy.music.set_audio_filter("soundfx", reverb_bathroom_af)
    play sound kissing2 volume 1.0 fadein 0.5 loop
    mc "*Hmphm... lhm...*"
    play voicefx2 amoansoft loop volume 0.75
    a "*Uh..*"
    pause
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    play sound kissing2 volume 0.5 fadein 0.5 loop
    $ anim_speed = 0.033
    scene ch10_99pov4_
    a "*Hmh, uh...*"
    mc "*Smnch* You know how much I love eating your pussy. Why don’t you just ask me for it?"
    a "*uh* {size=-3}{i}B-because it’s not right... and stop talking so loud..."
    pause
    scene ch10_99pov2_
    play sound kissing2 volume 0.5 fadein 0.5 loop
    play voicefx2 amoansoft loop volume 0.45
    mc "{size=-3}{i}It always ends up like this anyway..."
    mc "*Hmch, mhahl*"
    a "*Uh*"
    mc "{size=-3}{i}So... do you want me to keep going?"
    mc "*Hmch* {size=-3}{i}If you don’t answer, I’m gonna -*hic*, stop..."
    a "..."
    pause
    a "*Uhm, uh...* {i}{size=-3}Y-yes, sweetheart, don’t stop..."
    scene ch10_99pov1_
    play sound kissing2 volume 0.5 fadein 0.5 loop
    play voicefx2 amoansoft loop volume 0.7
    mc "*Hm..*"
    a "{i}{size=-3}Uh... uh..."
    mc "I wasn’t gonna stop anyway... *chup, shlp*"
    a "{i}{size=-3}*Hm*, Oh my... *aah*"
init python:
    def ch10_99pov1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_99pov1_{}".format(store.frame_num))
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    def ch10_99pov2_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_99pov2_{}".format(store.frame_num))
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value
init python:
    def ch10_99pov3_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_99pov3_{}".format(store.frame_num))
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value
init python:
    def ch10_99pov4_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_99pov4_{}".format(store.frame_num))
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value
screen ch10_99pov1_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch10_99pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch10_99pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch10_99pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_99_pov") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_99pov2_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch10_99pov1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch10_99pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch10_99pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_99_pov") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_99pov3_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch10_99pov1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch10_99pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch10_99pov4_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_99_pov") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_99pov4_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch10_99pov1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch10_99pov3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch10_99pov2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_99_pov") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 

label ch10_99pov1_:
    $ current_pov = 4
    scene ch10_99pov1_
    call screen ch10_99pov1_ with dissolve
label ch10_99pov2_:
    $ current_pov = 2
    scene ch10_99pov2_
    call screen ch10_99pov2_ with dissolve
label ch10_99pov3_:
    $ current_pov = 3
    scene ch10_99pov3_
    call screen ch10_99pov3_ with dissolve
label ch10_99pov4_:
    $ current_pov = 1
    scene ch10_99pov4_
    call screen ch10_99pov4_ with dissolve

label ch10_99pov:
    image ch10_99pov1_:
        function ch10_99pov1_
    image ch10_99pov2_:
        function ch10_99pov2_
    image ch10_99pov3_:
        function ch10_99pov3_
    image ch10_99pov4_:
        function ch10_99pov4_
    $ anim_speed = 0.035
    scene ch10_99pov1_
    call screen ch10_99pov1_
    pause

label afterch10_99_pov:
    if current_pov != 3:
        scene ch10_99pov3_
    pause
    a "{i}{size=-3}Sweetheart, those sounds... *ah*"
    a "{i}{size=-3}You’re making a lot of noise..."
    a "*Uh, uhmm*"
    a "{i}{size=-3}I can even hear the echo of your sucking..."
    image ch10_101anim:
        "ch10_101" with dissolve
        1.5
        "ch10_102" with dissolve
        1.5
        repeat
    scene ch10_101anim:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.0
        ease 1 zoom 1.01 xalign 0.5
        ease 1 zoom 1.0 xalign 0.5
        repeat
    a "Ahh... uhhm.."
    mc "Your legs are starting to tremble..."
    a "Uhm.. hmmm... Y-yes.."
    pause
    scene ch10_103
    a "Eh.. hmmh.. [mc]..."
    menu:
        "Use your tongue": #in her anus
            "{nw}"
    scene ch10_103:
        subpixel True
        xalign 0.5 yalign 0.5
        ease 0.35 zoom 1.02
        ease 0.25 zoom 1.01
    pause 0.75
    stop voicefx fadeout 0.5
    stop voicefx2 fadeout 0.5
    stop sound fadeout 0.5
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_104 with hpunch
    play voicefx2 "audio/character/a/hard/a_moan_hard_7.wav" volume 0.5
    a "Ah!"
    pause
    scene ch10_105
    a "N-no, not there, [mc]..."
    mc "No one’s ever done that to you?"
    a "N-no, of course not..."
    mc "I lose control when I touch your body... makes me wanna lick every inch of you..."
    a "I know, honey..."
    scene ch10_106 with dissolve
    a "I-I feel that way too sometimes..."
    mc "*Hic* Really?"
    a "..."
    play sound kissing loop volume 0.7
    play soundfx kissing2 loop volume 0.4
    scene ch10_107 with dissolve
    a "*Hmn... smnch...*"
    scene ch10_107- 
    pause
    image ch10_107anim:
        "ch10_107" with dissolve
        1.0
        "ch10_107-" with dissolve
        1.0
        repeat
    scene ch10_107anim
    a "*Lmah...* {i}{size=-3}Yes..."
    pause
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_106-
    a "*Hmnh... hlm...*"
    scene ch10_106--
    a "*Hmn.. malh...*"
    image ch10_106anim:
        "ch10_106-" with dissolve
        1.0
        "ch10_106--" with dissolve
        1.0
        repeat
    scene ch10_106anim
    a "*Smnch... lahn...*"
    pause
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_107anim
    mc "*Hmnch*, [arelat] [a], you’re sticking your tongue down my throat..."
    a "*Lahm... nsh...*"
    mc "(I’m getting dizzy...)" with dissolve
    pause
    stop sound fadeout 0.25
    scene ch10_108
    mc "[arelat!cl] [a]..."
    mc "(She’s kissing my neck... is that her tongue?)"
    pause
    scene ch10_109
    a "*Smnch...*"
    pause
    scene ch10_110
    pause
    scene ch10_111
    a "*Mchs...*"
    pause
    scene ch10_112
    a "*Mlh...*"
    pause
    scene ch10_113
    a "*Lahm...*"
    mc "Oh..."
    pause




    stop soundfx fadeout 0.5
    scene ch10_114
    a "..."
    pause
    scene ch10_115
    pause
    scene ch10_114
    mc "Uh..."
    image ch10_114anim:
        "ch10_114" with Dissolve(0.5)
        1.0
        "ch10_115" with Dissolve(0.5)
        0.5
        "ch10_114" with Dissolve(0.5)
        0.85
        "ch10_115" with Dissolve(0.5)
        0.5
        "ch10_114" with Dissolve(0.5)
        3.0
        "ch10_115" with Dissolve(0.5)
        0.5
        "ch10_114" with Dissolve(0.5)
        0.75
        "ch10_115" with Dissolve(0.5)
        0.5
        "ch10_114" with Dissolve(0.5)
        2.0
        "ch10_115" with Dissolve(0.5)
        0.5
        repeat
    scene ch10_114anim #amelie begins kissing his naked body, running her tongue across his torso
    pause
    mc "(I can’t get hard...)" with dissolve
    pause
    mc "I-I don’t *hic*{w=0.5} know what’s wrong with me..."
    play sound kissing2 fadein 0.25 loop volume 0.4
    scene ch10_113
    a "*Lhm...*"
    scene ch10_112
    a "*Lmhm...*"
    scene ch10_111
    a "*Hmch...* {i}It’s okay, you drank a lot..."
    scene ch10_116
    pause
    a "{i}Just let me... kiss it a little..."
    a "*Hmnch...*"
    scene ch10_117
    a "*Lah...*"
    pause
    scene ch10_118 
    a "*Hmmh...*"
    pause
    image ch10_118anim:
        "ch10_117" with dissolve
        1.25
        "ch10_116" with dissolve
        1.25
        "ch10_117" with dissolve
        1.25
        "ch10_118" with dissolve
        1.25
        repeat
    scene ch10_118anim
    a "*Hmsh.*"
    mc "Uh..."
    pause
    scene ch10_119
    a "*Hm... mmch...*"
    pause
    mc "I must be dreaming..."
    scene ch10_120
    a "*Lah...*"
    pause
    scene ch10_121
    a "*Llh... lhmm...*"
    pause
    scene ch10_118anim
    a "*Hmm...*"
    pause

init python:
    store.frame_num = 1
    store.anim_speed = 0.1
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.start_time = 0.0
    store.last_anim_speed = store.anim_speed

    def ch10_120asb1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_120asb1_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_120asb2_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_120asb2_{}".format(store.frame_num))
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value

screen ch10_120asb1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch10_120asb2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1"  style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_120aafter") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_120asb2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch10_120asb1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_120aafter") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 



screen ch10_120asd1_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_120asd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_120asd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_120bfore") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_120asd2_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_120asd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_120asd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_120bfore") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_120asd3_:
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
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_120asd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_120asd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_120bfore") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 


init python:
    store.frame_num = 1
    store.anim_speed = 0.1
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.start_time = 0.0
    store.last_anim_speed = store.anim_speed
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True

    def ch10_120asd1_(trans, st, at):
        if store.current_active_animation != "ch10_120asd1_":
            store.current_active_animation = "ch10_120asd1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_120asd1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_120asd1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_120asd2_(trans, st, at):
        if store.current_active_animation != "ch10_120asd2_":
            store.current_active_animation = "ch10_120asd2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_120asd2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_120asd2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 3.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_120asd3_(trans, st, at):
        if store.current_active_animation != "ch10_120asd3_":
            store.current_active_animation = "ch10_120asd3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_120asd3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_120asd3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 3.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value






label ch10_120anim:
    image ch10_120asb1:
        function ch10_120asb1_
    image ch10_120asb2:
        function ch10_120asb2_
    image ch10_120asd1:
        function ch10_120asd1_
    image ch10_120asd2:
        function ch10_120asd2_
    image ch10_120asd3:
        function ch10_120asd3_
    $ anim_speed = 0.02
    $ renpy.music.set_audio_filter("sound", [reverb_bathroom_af, af.Highpass(1000)])
    scene ch10_120asb1
    mc "Oh, wow..."
    a "*Hmch... hmmh...*"
    pause
    mc "Yeah... *hic*."
    mc "I like it..."
    mc "Uh... that feels so good, [arelat] [a]... *hic*"
    a "*Schm-muah, hmm*..."
    mc "*Uh*... {i}{size=-3}I can feel your tongue playing with my balls... Uh..."
    mc "{size=-3}That’s gotta get me hard any second now..."
    a "*Hch, mlh...*"
    pause
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_120asb2 
    mc "Oh... [arelat] [a]..."
    mc "Is this{w=0.5}, *hic*{w=0.5}, why you stayed here with me?"
    a "*H-hmm... smonch...*"
    a "Shh... *Hmsh, mnch...*"
    mc "Uh..."
    a "*Mch, mauh* {i}{size=-3}Don’f talk, honey..."
    pause
    $ anim_speed = 0.02
label ch10_120asb1_:
    $ current_pov = 1
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_120asb1
    call screen ch10_120asb1_ with dissolve
label ch10_120asb2_:
    $ current_pov = 2
    camera:
        subpixel False
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_120asb2
    call screen ch10_120asb2_ with dissolve  
label ch10_120aafter:
    camera:
        subpixel True
        ease 1.0 zoom 1.005 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    if current_pov != 1:
        scene ch10_120asb1
    mc "[arelat!cl] [a], uh..."
    a "*Hmh-hm... smch...*"
    pause
    scene ch10_121
    a "*Lhm... hmm..*"
    scene ch10_119
    a "Mnch...*"
    scene ch10_120
    a "*Muah... Hmh..*"
    scene ch10_122-
    a "*lhmm....*"
    scene ch10_122
    a "*Smnch...*"
    image ch10_122-_anim:
        "ch10_122-" with Dissolve(0.5)
        1.0
        "ch10_122" with Dissolve(0.75)
        1.2
        "ch10_122-" with Dissolve(0.75)
        1.2
        "ch10_120" with Dissolve(0.75)
        1.2
        "ch10_119" with Dissolve(0.75)
        1.2
        "ch10_121" with Dissolve(0.75)
        1.2
        "ch10_118" with Dissolve(0.75)
        1.2
        "ch10_117" with Dissolve(0.75)
        1.2
        "ch10_116" with Dissolve(0.75)
        1.2
        "ch10_117" with Dissolve(0.75)
        1.2
        "ch10_118" with Dissolve(0.75)
        1.2
        "ch10_121" with Dissolve(0.75)
        1.2
        "ch10_119" with Dissolve(0.75)
        1.2
        "ch10_120" with Dissolve(0.75)
        1.2
        "ch10_122" with Dissolve(0.5)
        1.2
        repeat
    scene ch10_122-_anim
    pause
    mc "Uh, yeah..."
    a "*Hmm, smnch... chup...*"
    pause
    a "*Mnch... schp...* {i}{size=-3}Is it working?"
    mc "Working? *hic*"
    a "I mean, *smnch, lhmm...*{w=0.5} if you’re enjoying it..."
    mc "*Hmmh...* Yeah, I like it..."
    pause
    a "{i}{size=-3}D-do you want me to suck it now? {/i}{/size}*Smonch.. hmch...*"
    mc "Yes..."
    a "*Smnch...* {size=-3}{i}Good..."
    $ anim_speed = 0.033
    stop voicefx2 fadeout 0.5
    stop voicefx fadeout 0.5
    scene ch10_120asd1
    mc "Oh..."
    mc "This is definitely gonna... hmm..."
    a "*Slrp, smnch...*"
    pause
    mc "Uh... yeah... {size=-3}{i}That’s gonna get me nice and hard for you, [arelat] [a]..."
    a "*Slch*, {i}hm-hmm..."
    pause
    mc "Keep using your tongue like before..."
    a "*slurp, smch*..."
    mc "*Uh*, yeah...{w=0.5} just like that, uh..."
    pause
    scene ch10_120asd2
    mc "*Hic*, this is amazing..."
    mc "Usually I have to beg to get this..."
    mc "Hope it keeps going like this, uh..."
    mc "You like it?... *uh*, do you like my cock in your mouth, [arelat] [a]?"
    mc "Does that turn you on?"
    mc "You don’t have to answer, *hic*, I already know it does..."
    a "*slurp* {i}{size=-3}You’re talking too much..."
    pause
    mc "Take it all in you mouth, [arelat] [a]..."
    mc "More... you’re almost at the base..."
    scene ch10_120asd3
    a "{size=-3}{i}Even soft *shup*, it’s still big..."
    mc "You really think this is big?"
    pause
    mc "You’ve only been with [drelat] [d], right? *hic*"
    mc "Uh... is [drelat] [d]’s smaller than this?"
    a "{i}Shh..."
    a "{i}Don’t talk like that, [mc]... *slurp*, I don’t like it..."
    a "{i}Better focus on this... *chup, slurp*."
    pause
    call screen ch10_120asd1_ with dissolve
    label ch10_120asd1_:
        scene ch10_120asd1
        call screen ch10_120asd1_ with dissolve  
    label ch10_120asd2_:
        scene ch10_120asd2 
        call screen ch10_120asd2_ with dissolve   
    label ch10_120asd3_:
        scene ch10_120asd3 
        call screen ch10_120asd3_ with dissolve  







init python:
    def ch8_abj2_pov1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 60 + 1
        if store.frame_num > 60:
            store.frame_num = 1
        trans.set_child("ch8_abj2_pov1_{}".format(store.frame_num))
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

init python:
    def ch10_120ased1_(trans, st, at):
        if store.current_active_animation != "ch10_120ased1_":
            store.current_active_animation = "ch10_120ased1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame > 40:
            new_frame = 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_120ased1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_120ased1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_53.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_42.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg", "audio/wavs/bj_71.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='voicefx')
                if store.anim_speed < 0.02:
                    if random_chance < 0.75:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                elif store.anim_speed >= 0.03:
                    if random_chance < 0.1:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                elif store.anim_speed >= 0.02:
                    if random_chance < 0.4:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_120ased2_(trans, st, at):
        if store.current_active_animation != "ch10_120ased2_":
            store.current_active_animation = "ch10_120ased2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame > 40:
            new_frame = 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_120ased2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_120ased2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_53.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_42.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg", "audio/wavs/bj_71.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='voicefx')
                if store.anim_speed < 0.02:
                    if random_chance < 0.75:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                        atl_play_voicefx(random_sound)()
                        store.sound_played_this_cycle = True
                elif store.anim_speed >= 0.03:
                    if random_chance < 0.1:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                        
                        store.sound_played_this_cycle = True
                elif store.anim_speed >= 0.02:
                    if random_chance < 0.4:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                        
                        store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_120ased3_(trans, st, at):
        if store.current_active_animation != "ch10_120ased3_":
            store.current_active_animation = "ch10_120ased3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame > 40:
            new_frame = 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_120ased3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_120ased3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_53.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_42.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg", "audio/wavs/bj_71.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
               
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='voicefx')
                if store.anim_speed < 0.02:
                    if random_chance < 0.75:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                   
                        store.sound_played_this_cycle = True
                elif store.anim_speed >= 0.03:
                    if random_chance < 0.1:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                    
                        store.sound_played_this_cycle = True
                elif store.anim_speed >= 0.02:
                    if random_chance < 0.4:
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                     
                        store.sound_played_this_cycle = True
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value

screen ch10_120ased1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Show("random_speed", min_speed=0.035, max_speed=0.045)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Show("random_speed", min_speed=0.02, max_speed=0.03)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.014), Show("random_speed", min_speed=0.013, max_speed=0.018)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.025), Function(disable_even_frames), Show("random_speed", min_speed=0.013, max_speed=0.045)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_120ased3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_120ased2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch120ased") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_120ased2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Show("random_speed", min_speed=0.035, max_speed=0.045)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Show("random_speed", min_speed=0.02, max_speed=0.03)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.014), Show("random_speed", min_speed=0.013, max_speed=0.018)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.025), Function(disable_even_frames), Show("random_speed", min_speed=0.014, max_speed=0.045)] style "textbutton_choice" 
    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_120ased3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_120ased1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch120ased") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_120ased3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Show("random_speed", min_speed=0.035, max_speed=0.045)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Show("random_speed", min_speed=0.02, max_speed=0.03)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.014), Show("random_speed", min_speed=0.013, max_speed=0.018)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.025), Function(disable_even_frames), Show("random_speed", min_speed=0.014, max_speed=0.045)] style "textbutton_choice" 
    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_120ased2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_120ased1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch120ased") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label ch10_120bfore:
    image ch10_123anim:
        "ch10_123_1" with dissolve
        0.5
        "ch10_123_2" with dissolve
        0.5
        "ch10_123_3" with dissolve
        0.5
        "ch10_123_4" with dissolve
        0.5
        repeat
    show ch10_123anim
    a "*Slrp, hmm...*"
    pause
    mc "It’s getting hard, I can feel it..."
    a "*Smch, slrp, sch...*"
    mc "Oh... the echo... yeah, I can hear it..."
    pause
    image ch10_120ased1_:
        function ch10_120ased1_
    image ch10_120ased2_:
        function ch10_120ased2_
    image ch10_120ased3_:
        function ch10_120ased3_
    scene ch10_124
    a "Hm.."
    scene ch10_125
    a "-Hmm..."
    $ renpy.music.set_audio_filter("voicefx", [reverb_bathroom_af, af.Highpass(500)], replace=True)
    scene ch10_120ased1_
    mc "Uh, yeah..."
    a "*Slrp, slrp, suck...*"
    mc "Oh, [arelat] [a]..."
    pause
    mc "You like it nice and *hic*...{w=0.5} hard, huh?... hehe..."
    a "Hmh... *slrp, chuck, guh*"
    pause
    mc "Although... I did like when you could suck almost the whole thing when it was soft..."
    a "-Hmm... *Slrp, suck, smnch...*"
    scene ch10_126
    a "Sweetheart, it’s too big... I can’t go that deep..."
    mc "Practice makes perfect, [arelat] [a]."
    a "{i}{size=-3}Yeah..."
    mc "Tell me, who’s bigger, me or [drelat] [d]?"
    a "{i}{size=-3}Don’t ask me that..."
    mc "Say it, [arelat] [a]... we won’t tell anyone."
    pause
    a "{i}{size=-3}Y-you, sweetheart..."
    mc "Uh... When I know you want me, it gets even harder than usual."
    a "{i}{size=-3}Yeah, it’s throbbing a little..."
    mc "Keep sucking, [arelat] [a], or it’ll go soft again..."
    scene ch10_120ased1_
    mc "Uh, yeah... Good girl."
    pause
    mc "You’re the best [arelat] anyone could ask for."
    scene ch10_120ased2_
    $ volumedown()
    pause
    mc "*Uh...*, that feels so good..."
    mc "This blowjob feels even better, I think you’ve gotten better at it, [arelat] [a]..."
    a "*hmm-hm*"
    mc "If you weren’t my [arelat], *uh*{w=0.5}, I’d marry you."
    mc "Actually, I’m lying... {w=1.0}I don’t care that you’re my [arelat]."
    pause
    scene ch10_120ased3_
    $ volumedown()
    pause
    mc "Someday you’ll be my woman..."
    mc "I’ll give you everything, way more than [drelat] [d] ever has, *hic*."
    mc "And I don’t mean money..."
    a "*Slurp, slorp, chup* {i}{size=-3}[mc], that’s enough..."
    mc "N-no, I’ll have money too, *hic* {w=0.5}, so much we won’t even know how to spend it."
    mc "But more than anything... I’ll give you love. Because that’s *hic*{w=0.5}, the most important thing... in life..."
    a "Shhh, {i}{size=-3}Quiet now or I’ll stop..."
    call screen ch10_120ased3_ with dissolve
define ch10120_ased1 = "False"
label ch10_120ased1_:
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    $ ch10120_ased1 = "True"
    scene ch10_120ased1_
    
    call screen ch10_120ased1_ with dissolve
label ch10_120ased2_:
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    $ ch10120_ased1 = "False"
    scene ch10_120ased2_
    
    call screen ch10_120ased2_ with dissolve    
label ch10_120ased3_:
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    $ ch10120_ased1 = "False"
    scene ch10_120ased3_
    
    call screen ch10_120ased3_ with dissolve

label afterch120ased:
    if ch10120_ased1 == "False":
        camera:
            subpixel True
            zoom 1.005 
            xalign 0.5 
            yalign 0.5
            parallel:
                align (0.5, 0.5)
                around (0.501, 0.5)
                linear 3.0 counterclockwise circles 1
                around (0.499, 0.5)
                linear 3.0 clockwise circles 1
                repeat
        scene ch10_120ased1_
        
    mc "[a], I wish you'd let me fuck you... Hmmh..."
    a "*slurp, suck...*"
    mc "I can think of a thousand ways to make love to you..."
    a "Hm.. *Slurp, slurp, slmch...*"
    mc "{i}{size=-3}Let me fuck you..."
    a "*slurp* Hm-hmh..."
    mc "I know you want to..."
    mc "[drelat] [d] stopped giving you the attention you need a long time ago."
    mc "Or maybe, *hic*{w=0.5}, he just doesn't make you feel anything anymore..."
    mc "That’s why you’re here, right? You just have to let me..."
    a "Hmm... *smlrp, suck...*"
    pause
    scene ch10_126
    a "*Buah...*"
    a "Do you want to do it between my legs?"
    mc "Between your legs?"
    mc "Let me fuck you, [arelat] [a]... *hic* I’m going crazy, I dream about being inside you every night."
    scene ch10_127
    a "[mc]..."
    a "Honey, you already know that’s not happening."
    a "They’d never forgive me..."
    mc "Who wouldn’t?"
    a "Well, your..."
    a "[mc], we just can’t. That’s it. Simple as that."
    a "It’s already crazy that we’re doing this...{w=0.5} again..."
    pause
    "..."
    scene ch10_128 
    a "And what’s wrong with my legs, huh?"
    a "Don’t you like them?"
    mc "Why settle for just that?"
    scene ch10_129
    a "Just that?"
    a "Are my legs ''just that'' to you?"
    mc "No, I love your legs, I just, {w=0.5}{nw}"
    a "-Put it between them."
    mc "I didn’t mean I don’t like them{w=0.5}{nw}"
    a "Between my legs. Now." with hpunch
    camera:
        zoom 1.00
        xalign 0.5 
        yalign 0.5
    scene ch10_130 
    mc "Uh... you’re so wet..."
    a "Yeah... you like it?"
    mc "I love it..."
    a "I know how much you love doing this..."
    a "Deeper, sweetheart..."
    scene ch10_131
    a "That’s it, just like that..." 
    mc "Hmm..."
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_128
    a "I’m going to squeeze it tight, just how you like it."
    a "Unless... you want me to take you to bed now?"
    mc "N-no, {w=0.5} *hic* let’s keep going. I love doing it with your legs."
    a "Good... I’m glad you like it."
    pause
    scene ch10_107anim
    play sound kissing fadein 0.5 volume 0.1 loop
    pause
    jump ch10_130athj3_

label ch10_athj1_:
    $ current_pov = 1
    scene ch10_130athj1_ with nothing
    call screen ch10_130_athj_ with nothing
label ch10_athj2_:
    $ current_pov = 2
    scene ch10_130athj2_ with nothing
    call screen ch10_130_athj_ with nothing
label ch10_athj3_:
    $ current_pov = 3
    scene ch10_130athj3_ with nothing
    call screen ch10_130_athj_ with nothing
label ch10_athj4_:
    $ current_pov = 4
    scene ch10_130athj4_ with nothing
    call screen ch10_130_athj_ with nothing
label ch10_athj5_:
    $ current_pov = 5
    scene ch10_130athj5_ with nothing
    call screen ch10_130_athj_ with nothing

init python:
    store.frame_num = 1
    store.anim_speed = 0.1
    store.last_played_sound = None
    store.last_played_sound1 = None      
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.start_time = 0.0
    store.last_anim_speed = store.anim_speed
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True

    def get_masturbating_sounds():
        return [
            "audio/masturbating/cutmastrubating6.ogg",
            "audio/masturbating/cutmastrubating7.ogg",
            "audio/masturbating/cutmastrubating8.ogg",
            "audio/masturbating/cutmastrubating9.ogg"
        ]

    def get_fuck_sounds():
        return [
            "audio/sex/fuck_naked5.ogg",
            "audio/sex/fuck_naked11.ogg",
            "audio/sex/fuck_naked10.ogg",
            "audio/sex/fuck_naked8.ogg"
        ]

    def ch10_130athj1_(trans, st, at):
        if store.current_active_animation != "ch10_130athj1_":
            store.current_active_animation = "ch10_130athj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130athj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130athj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 30 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_fuck_sounds() if s != store.last_played_sound1])
                store.last_played_sound1 = sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.6 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.09 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_130athj2_(trans, st, at):
        if store.current_active_animation != "ch10_130athj2_":
            store.current_active_animation = "ch10_130athj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130athj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130athj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 30 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_fuck_sounds() if s != store.last_played_sound1])
                store.last_played_sound1 = sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.5 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.25 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.05 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_130athj3_(trans, st, at):
        if store.current_active_animation != "ch10_130athj3_":
            store.current_active_animation = "ch10_130athj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130athj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130athj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 30 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_fuck_sounds() if s != store.last_played_sound1])
                store.last_played_sound1 = sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.75 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.35 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_130athj4_(trans, st, at):
        if store.current_active_animation != "ch10_130athj4_":
            store.current_active_animation = "ch10_130athj4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130athj4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130athj4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 30 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_fuck_sounds() if s != store.last_played_sound1])
                store.last_played_sound1 = sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.8 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.45 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.15 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_130athj5_(trans, st, at):
        if store.current_active_animation != "ch10_130athj5_":
            store.current_active_animation = "ch10_130athj5_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130athj5_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130athj5_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 30 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_fuck_sounds() if s != store.last_played_sound1])
                store.last_played_sound1 = sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.8 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.45 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.15 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(sound, channel='sound')
                    store.sound_played_this_cycle = True
        return store.anim_speed
screen ch10_130_athj_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.023), Show("random_speed", min_speed=0.02, max_speed=0.027), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Show("random_speed", min_speed=0.013, max_speed=0.018), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Show("random_speed", min_speed=0.008, max_speed=0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.008, max_speed=0.027)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 5:
            textbutton "Pov 5" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 5" action [SetVariable("current_pov", 5), Jump("ch10_athj5_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 4:
            textbutton "Pov 4" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 4" action [SetVariable("current_pov", 4), Jump("ch10_athj4_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [SetVariable("current_pov", 3), Jump("ch10_athj3_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_athj2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_athj1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("ch10_afeterch10_130athj3_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
image ch10_130athj1_:
    function ch10_130athj1_

image ch10_130athj2_:
    function ch10_130athj2_

image ch10_130athj3_:
    function ch10_130athj3_

image ch10_130athj4_:
    function ch10_130athj4_

image ch10_130athj5_:
    function ch10_130athj5_

# Pantalla para alternar modo de frames pares
screen toggle_even_frames_screen():
    textbutton "Toggle Even Frames" action Function(toggle_even_frames) xalign 0.95 yalign 0.05
define af = renpy.audio.filter
define reverb_church_hall_af = [af.Reverb(resonance=0.7, dampening=200, dry=0.7, delay_subchannel=0.001)]
define reverb_bathroom_af = (af.Reverb(resonance=0.5, dampening=6000, wet=0.3, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410]))
label ch10_130athj3_:
    #$ renpy.music.set_audio_filter("sound", reverb_church_hall_af, replace=True)
    play voicefx2 amoansoft volume 1.0 loop
    $ renpy.music.set_audio_filter("voicefx2", [reverb_bathroom_af, af.Lowpass(400), af.Highpass(1500)])
    $ renpy.music.set_audio_filter("voicefx", [reverb_bathroom_af, af.Highpass(1500)])
    $ renpy.music.set_audio_filter("sound", [af.Highpass(1800), af.Reverb(resonance=0.5, dampening=6000, wet=0.5, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])])
    $ renpy.music.set_audio_filter("soundfx", [af.Highpass(1800), af.Reverb(resonance=0.5, dampening=6000, wet=0.5, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])])
    $ renpy.music.set_audio_filter("sound_fx", [af.Highpass(1800), af.Reverb(resonance=0.5, dampening=6000, wet=0.5, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])])
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_130athj3_ with dissolve
    $ hide_anim_speed()
    show screen random_anim_speed with nothing
    a "*Hmmh, smnch...* {i}Yes, honey, like that... *hmmh...*"
    mc "*Hah*, [arelat] [a]... your body makes me melt."
    pause
    a "*Hmh, smnch...* {i}Push it deeper..."
    $ hide_anim_speed()
    hide screen random_anim_speed with nothing
    show screen random_anim_speed_fast with nothing
    $ anim_speed = 0.0125
    pause
    a "*Hm, hmch, hm...* {i}J-just like that... yes, baby, *huh*..."
    mc "*Hah*..."
    pause
    a "*Huh*... {i}Oh..."
    a "{i}D-doesn’t that feel good? {/i}*uh-huh*"
    pause
    a "*Huh* {i}Hmm?"
    mc "*Huh, smch* {i}W-what...?"
    a "*Giggle* {i}Nothing{/i} *mch*{w=0.5}, {i}just keep going..."
    pause
    a "*Hmh, hah*..."
    hide screen random_anim_speed_fast with nothing
    show screen random_anim_speed_slow with nothing
    mc "*Hah*..."
    $ anim_speed = 0.027
    mc "*Hmnh* W-wait, [arelat] [a]..."
    a "*Huh*... {i}Tired already?"
    mc "{i}I-I almost came… *smch*"
    a "{i}Not yet, sweetheart -I’m not done with you..."
    scene ch10_130athj2_
    pause
    mc "{i}I like you so much, [arelat] [a]... *hic*.{/i} *Uh... hmm...*"
    a "*Huh*...?"
    mc "{i}I know you do too... you’re crazy about me, *smnch*...{/i}"
    a "*Giggle*{w=0.5}{nw}"
    a "{i}And you’re drunk and crazy.{/i}"
    mc "{i}That's [drelat] [d]'s fault.{/i}"
    mc "...{w=0.5} No, wait..."
    mc "N-no, *huh*, I didn’t mean I’m crazy for [drelat] [d]-"
    a "*Giggle*{w=0.5}{nw}"
    mc "{i}Everything’s fine with him, but *mahl*{w=0.5}... the one thing about him that drives me crazy...{w=0.5} is my [arelat] [a]...{/i}"
    hide screen random_anim_speed_slow with nothing
    show screen random_anim_speed_fast with nothing
    $ anim_speed = 0.014

    a "*Mnch*, {i}Uh, [mc]..."
    pause
    scene ch10_130athj1_
    mc "{i}Move your hips, *mch*."
    mc "Uh... yeah, that’s how I like it..."
    mc "{i}Squeeze it tighter..."
    a "*Hmch*, {i}{size=-3}Like this?"
    a "*Hah, hah*..."
    a "[mc]..."
    a "*Uh, uhm*..."
    scene ch10_130athj5_
    mc "{i}It slides so well..."
    mc "{i}You’re so wet..."
    a "*Uh, hmmh*..."
    pause
    scene ch10_130athj4_
    mc "*Uh* -[arelat!cl] [a], your body’s so soft and comforting..."
    mc "I’m gonna cum soon."
    a "*Huh, uh*, keep going baby, don’t stop now..."
    $ current_pov = 4
    call screen ch10_130_athj_ with dissolve

label ch10_afeterch10_130athj3_:
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_107anim
    pause 0.1
    $ audio_fade()
    play sound kissing fadein 1.0 volume 1.0 loop
    play soundfx kissing2 fadein 0.5 volume 0.5 loop
    stop voicefx2 fadeout 0.1
    a "*Hmnch... mnch...*"
    scene ch10_128 with dissolve
    $ stop_sounds()
    a "Why did you stop?"
    mc "Turn around..."
    a "You want to do it from behind?"
    mc "Yeah..."
    scene ch10_132
    a "Like this?"
    mc "Uh, yeah..."
    a "B-between my legs, [mc]..."
    pause
    hide screen random_anim_speed_fast
    hide screen random_anim_speed_slow
    hide screen random_anim_speed
    $ hide_anim_speed()
     
    jump ch10_2500at



init python:
    def ch10_130_athjb0_(trans, st, at):
        if store.current_active_animation != "ch10_130_athjb0_":
            store.current_active_animation = "ch10_130_athjb0_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_athjb0_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_athjb0_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 20 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slaprev_1.ogg", "audio/slaps/slaprev_2.ogg", "audio/slaps/slaprev_3.ogg", "audio/slaps/slaprev_4.ogg", "audio/slaps/slaprev_5.ogg", "audio/slaps/slaprev_6.ogg", "audio/slaps/slaprev_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.6 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
    
    def ch10_130_athjb2_(trans, st, at):
        if store.current_active_animation != "ch10_130_athjb2_":
            store.current_active_animation = "ch10_130_athjb2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_athjb2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_athjb2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 20 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slaprev_1.ogg", "audio/slaps/slaprev_2.ogg", "audio/slaps/slaprev_3.ogg", "audio/slaps/slaprev_4.ogg", "audio/slaps/slaprev_5.ogg", "audio/slaps/slaprev_6.ogg", "audio/slaps/slaprev_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.45 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.25 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.09 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
    
    def ch10_130_athjb3_(trans, st, at):
        if store.current_active_animation != "ch10_130_athjb3_":
            store.current_active_animation = "ch10_130_athjb3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_athjb3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_athjb3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 20 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slaprev_1.ogg", "audio/slaps/slaprev_2.ogg", "audio/slaps/slaprev_3.ogg", "audio/slaps/slaprev_4.ogg", "audio/slaps/slaprev_5.ogg", "audio/slaps/slaprev_6.ogg", "audio/slaps/slaprev_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.17 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.075 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
    
    def ch10_130_athjb4_(trans, st, at):
        if store.current_active_animation != "ch10_130_athjb4_":
            store.current_active_animation = "ch10_130_athjb4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_athjb4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_athjb4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 20 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slaprev_1.ogg", "audio/slaps/slaprev_2.ogg", "audio/slaps/slaprev_3.ogg", "audio/slaps/slaprev_4.ogg", "audio/slaps/slaprev_5.ogg", "audio/slaps/slaprev_6.ogg", "audio/slaps/slaprev_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.4 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.25 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.075 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
    
    def ch10_130_athjb5_(trans, st, at):
        if store.current_active_animation != "ch10_130_athjb5_":
            store.current_active_animation = "ch10_130_athjb5_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_athjb5_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_athjb5_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 20 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slaprev_1.ogg", "audio/slaps/slaprev_2.ogg", "audio/slaps/slaprev_3.ogg", "audio/slaps/slaprev_4.ogg", "audio/slaps/slaprev_5.ogg", "audio/slaps/slaprev_6.ogg", "audio/slaps/slaprev_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed < 0.015:
                    final_volume = max(0.04, 0.25 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.015 < 0.023:
                    final_volume = max(0.04, 0.13 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                elif anim_speed >= 0.023:
                    final_volume = max(0.04, 0.05 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

screen ch10_130_athjb0_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.023), Show("random_speed", min_speed=0.02, max_speed=0.027), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Show("random_speed", min_speed=0.013, max_speed=0.018), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Show("random_speed", min_speed=0.008, max_speed=0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.008, max_speed=0.027)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch10_130_athjb5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch10_130_athjb4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch10_130_athjb3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch10_130_athjb2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_afterathjb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_130_athjb2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.023), Show("random_speed", min_speed=0.02, max_speed=0.027), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Show("random_speed", min_speed=0.013, max_speed=0.018), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Show("random_speed", min_speed=0.008, max_speed=0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.008, max_speed=0.027)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch10_130_athjb5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch10_130_athjb4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch10_130_athjb3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch10_130_athjb0_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_afterathjb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_130_athjb3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.023), Show("random_speed", min_speed=0.02, max_speed=0.027), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Show("random_speed", min_speed=0.013, max_speed=0.018), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Show("random_speed", min_speed=0.008, max_speed=0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.008, max_speed=0.027)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch10_130_athjb5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch10_130_athjb4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch10_130_athjb2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch10_130_athjb0_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_afterathjb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_130_athjb4_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.023), Show("random_speed", min_speed=0.02, max_speed=0.027), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Show("random_speed", min_speed=0.013, max_speed=0.018), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Show("random_speed", min_speed=0.008, max_speed=0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.008, max_speed=0.027)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch10_130_athjb5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch10_130_athjb3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch10_130_athjb2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch10_130_athjb0_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_afterathjb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_130_athjb5_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.023), Show("random_speed", min_speed=0.02, max_speed=0.027), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Show("random_speed", min_speed=0.013, max_speed=0.018), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Show("random_speed", min_speed=0.008, max_speed=0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.008, max_speed=0.027)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5"  style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch10_130_athjb4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch10_130_athjb3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch10_130_athjb2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch10_130_athjb0_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10_afterathjb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 

image ch10_130_athjb0_:
    function ch10_130_athjb0_
image ch10_130_athjb2_:
    function ch10_130_athjb2_
image ch10_130_athjb3_:
    function ch10_130_athjb3_
image ch10_130_athjb4_:
    function ch10_130_athjb4_
image ch10_130_athjb5_:
    function ch10_130_athjb5_

label ch10_130_athjb0_:
    $ current_pov = 1
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_130_athjb0_ with nothing
    call screen ch10_130_athjb0_ 
label ch10_130_athjb2_:
    $ current_pov = 2
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    scene ch10_130_athjb2_ with nothing
    call screen ch10_130_athjb2_ 
label ch10_130_athjb3_:
    $ current_pov = 3
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    scene ch10_130_athjb3_ with nothing
    call screen ch10_130_athjb3_
label ch10_130_athjb4_:
    $ current_pov = 4
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    scene ch10_130_athjb4_ with nothing
    call screen ch10_130_athjb4_
label ch10_130_athjb5_:
    $ current_pov = 5
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    scene ch10_130_athjb5_ with nothing
    call screen ch10_130_athjb5_ 
label ch10_2500at:
    $ renpy.music.set_audio_filter("sound", None)
    show screen random_speed(0.009, 0.015)
    play voicefx2 amoansoft volume 0.5 loop
    $ renpy.music.set_audio_filter("voicefx2", [af.Highpass(500), af.Reverb(resonance=0.5, dampening=9000, wet=0.5, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])])
    $ renpy.music.set_audio_filter("voicefx", [reverb_bathroom_af, af.Highpass(1500)])
    $ renpy.music.set_audio_filter("soundfx3", [reverb_bathroom_af, af.Highpass(300)])
    $ renpy.music.set_audio_filter("sound", [af.Highpass(1000), af.Reverb(resonance=0.5, dampening=9000, wet=0.35, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])], replace=True)
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_130_athjb0_
    mc "*Hmmgh..* {i}Oh god, this ass... *mnh*..."
    mc "Your butt jiggles so much, *hic*... I love it."
    a "*Huh, uh*."
    pause
    show ch10_133- with dissolve:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.2 zoom 1.005
        ease 0.3 zoom 1.0
        repeat
    mc "Kiss me, [arelat] [a]."
    a "Come closer, honey..."
    pause
    image ch10_134anim:
        "ch10_134" with Dissolve(0.1)
        0.2
        "ch10_135" with Dissolve(0.1)
        0.3
        repeat
    show ch10_134 with dissolve:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.2 zoom 1.005
        ease 0.3 zoom 1.0
        repeat
    pause 0.1
    play soundfx3 kissing2 volume 0.5 loop fadein 0.5
    mc "Wrap your tongue around mine..."
    a "*Lahm, hmua*..."
    pause
    camera:
        zoom 1.00
        xalign 0.5 
        yalign 0.5
    $ renpy.music.set_audio_filter("soundfx3", [reverb_bathroom_af, af.Highpass(1500)], replace=True)
    play soundfx3 kissing2 volume 0.15 loop fadein 0.5
    scene ch10_130_athjb2_
    a "*Huh, luahl*...{w=0.5} {i}So noisy..."
    mc "You should be proud, *hic*."
    $ hide_anim_speed()
    a "*Huh*, {i}I-I guess... {w=0.5}S-slow down a bit, honey, you’ll wake everyone..."
    $ anim_speed = 0.015
    pause 0.5
    show screen random_speed(0.02, 0.03)
    mc "*Hah.. huh...* [arelat!cl] [a], I’m in love with you..."
    pause
    mc "Tell me you love me, [arelat] [a]."
    a "*Hah*{w=0.5} I love you, honey..."
    mc "Now say it like you mean it, *uh*{w=0.5}, tell me you’ll be mine."
    mc "Say it right now, *hic*..."
    a "..."
    pause
    a "*Huh* {i}[mc], you’re drunk *huh*{w=0.5}, you don’t know what you’re saying."
    pause
    a "*Muahl*... {i}{size=-3}If you want, you can go a little faster, baby..."
    $ hide_anim_speed()
    show screen random_speed(0.009, 0.011)
    $ anim_speed = 0.01
    pause
    mc "*Huh* You’re more… passionate than usual today, [arelat] [a]."
    a "*Mah, hah* {i}P-passionate?{/i}"
    mc "*Uh* Yeah…"
    a "*Hmn*…"
    mc "All this… bringing me here *hic*{w=0.5}, showering me…"
    scene ch10_130_athjb3_
    mc "You don’t need an excuse to spend -*huh*{w=0.5} some quality time with me."
    mc "You just have to say so… *uh*."
    a "*Hmmh*… {i}I wasn’t-{/i}"
    pause
    a "{i}A-alright, honey…{/i} *smnch*."
    pause
    mc "*Hic*... You’re such a reserved woman when it comes to this."
    mc "It’s not just your body I love, [arelat] [a] *huh*{w=0.5}, it’s that way you are... it drives me crazy."
    mc "You’re *hic*{w=0.5} the perfect woman for me."
    a "*Huh, lahm* {i}[mc], what did we say about talking too much...?"
    pause
    mc "Even if you won’t let me fuck you, *hngh*..."
    show screen random_speed(0.008, 0.01)
    $ anim_speed=0.008
    mc "Just give me a sign, and I’ll gladly make you moan with pleasure!"
    a "{i}Shhh, honey, lower your voice..."
    mc "Your ass slapping against my hips is louder than my voice..."
    a "{i}I-it’s true, we’re being loud, *oh*..."
    mc "{i}Let’s make a scene, [arelat] [a]."
    a "*Uh, hmm, huh...*"
    show screen random_speed(0.007, 0.009)
    $ anim_speed = 0.007
    mc "*Hmngh!* Let’s make a scene- I want everyone in this house to know you’re mine now!"
    a "*Oh, hah, ah*..."
    pause
    scene ch10_130_athjb4_ 
    a "*Huh* {i}[mc], *huh*{w=0.5}, I’m telling you to stop saying those things..."
    a "*Uh, hmh, huh* {i}I-if anyone finds out, we’ll never do any of this again, *huh*."
    a "*Huh, uh* {i}So get those ideas out of that head..."
    pause
    scene ch10_130_athjb5_ 
    mc "So... should I slow down? *hmgh* We’re being kinda loud."
    a "{i}It’s fine... *huh*, I locked the door."
    a "*Hah, hah, huh* {i}D-don't stop now..."
    $ current_pov = 5
    hide screen random_anim_speed_slow with nothing
    hide screen random_anim_speed_fast with nothing
    hide screen random_anim_speed_normal with nothing
    hide screen random_anim_speed with nothing
    $ hide_anim_speed()
    call screen ch10_130_athjb5_ with dissolve






label ch10_afterathjb:
    if current_pov != 2:
        scene ch10_130_athjb2_
    pause 0.1
    hide screen random_anim_speed_slow with nothing
    hide screen random_anim_speed_fast with nothing
    hide screen random_anim_speed_normal with nothing
    hide screen random_anim_speed with nothing
    hide screen random_speed with nothing
    $ anim_speed = 0.008
    pause 1.0
    a "*Uh, uh, uhm...* {i}K-keep giving it to me like that, honey..."
    mc "*Hah* [arelat!cl] [a], m-my legs are shaking..."
    a "*Uh, huh* {i}A-are you close?"
    $ anim_speed = 0.007
    mc "*Hmmngh!*"
    a "*Ah, ah...* {i}Just like that, baby, yes, *uh, huh*..."
    mc "*hmmh!* *haah!*"
    a "J-just don’t lean on me."
    pause
    stop voicefx fadeout 0.2
    stop voicefx2 fadeout 0.2
    stop soundfx fadeout 0.2
    stop soundfx3 fadeout 0.2
    stop sound fadeout 0.2
    pause 0.5 
    play voicefx2 "audio/character/a/acum/a_acum_10.wav" volume 0.3
    scene ch10_136 with hpunch
    a "Aah!" 
    scene blackscreen with nothing
    mc "Hah!" with vpunch
    a "Honey, are you okay?!"
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_140 with Dissolve(2.0)
    mc "Uh..."
    mc "M-my legs gave out, *hic*..."
    a "[mc], I-I fell on top of you."
    mc "Thank God for that..."
    a "Are you really okay?"
    mc "Uh... Of course I am..."
    pause
    scene ch10_139
    pause
    a "{i}Oh, honey..." 
    a "..."
    pause
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    scene ch10_130_agd0_2 
    a "Uh..."
    pause
    a "{i}C-can we stay like this for a moment? *Uh*."
    mc "Why? Are you okay?"
    a "{i}Yeah, just...{w=0.5}"
    pause
    image ch10_130agdanim:
        "ch10_130_agd0_2" with dissolve
        0.3
        "ch10_130_agd0_3" with dissolve
        0.3
        "ch10_130_agd0_4" with dissolve
        0.3
        "ch10_130_agd0_2" with dissolve
        2.0
        "ch10_130_agd0_2" with dissolve
        0.3
        "ch10_130_agd0_3" with dissolve
        0.3
        "ch10_130_agd0_4" with dissolve
        0.3
        "ch10_130_agd0_2" with dissolve
        2.0
        "ch10_130_agd0_2" with dissolve
        0.3
        "ch10_130_agd0_3" with dissolve
        0.3
        "ch10_130_agd0_4" with dissolve
        0.3
        "ch10_130_agd0_2" with dissolve
        0.3
        "ch10_130_agd0_2" with dissolve
        0.3
        "ch10_130_agd0_3" with dissolve
        0.3
        "ch10_130_agd0_4" with dissolve
        0.3
        "ch10_130_agd0_2" with dissolve
        0.3
        repeat
    scene ch10_130agdanim
    a "{i}I-I just need to catch my breath a bit, that’s all..."
    pause
    mc "{i}[arelat!cl] [a]-...?"
    a "Sweetheart, I..."
    a "..."
    pause
    jump afterch10_agd0



init python:
    def ch10_130_agd0_(trans, st, at):
        if store.current_active_animation != "ch10_130_agd0_":
            store.current_active_animation = "ch10_130_agd0_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_agd0_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_agd0_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                               "audio/masturbating/cutmastrubating7.ogg",
                               "audio/masturbating/cutmastrubating8.ogg",
                               "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_130_agd1_(trans, st, at):
        if store.current_active_animation != "ch10_130_agd1_":
            store.current_active_animation = "ch10_130_agd1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_agd1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_agd1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                               "audio/masturbating/cutmastrubating7.ogg",
                               "audio/masturbating/cutmastrubating8.ogg",
                               "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_130_agdc_(trans, st, at):
        if store.current_active_animation != "ch10_130_agdc_":
            store.current_active_animation = "ch10_130_agdc_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_130_agdc_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_130_agdc_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                               "audio/masturbating/cutmastrubating7.ogg",
                               "audio/masturbating/cutmastrubating8.ogg",
                               "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

image ch10_130_agd0_:
    function ch10_130_agd0_
image ch10_130_agd1_:
    function ch10_130_agd1_
image ch10_130_agdc_:
    function ch10_130_agdc_

screen ch10_130_agd_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Hide("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Hide("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Hide("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_130_agd1_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_130_agd0_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("beforech10_130")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  




label ch10_130_agd0_:
    $ current_pov = 1
    scene ch10_130_agd0_ with nothing
    call screen ch10_130_agd_ 
label ch10_130_agd1_:
    $ current_pov = 2
    scene ch10_130_agd1_ with nothing
    call screen ch10_130_agd_ 





label afterch10_agd0:
    $ hide_anim_speed()
    $ anim_speed = 0.02
    show screen random_anim_speed_normal with nothing
    $ renpy.music.set_audio_filter("voicefx2", None)
    $ renpy.music.set_audio_filter("voicefx", None)
    $ renpy.music.set_audio_filter("voicefx2", [af.Reverb(resonance=0.5, dampening=9000, wet=0.3, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])])
    $ renpy.music.set_audio_filter("voicefx", [af.Reverb(resonance=0.5, dampening=9000, wet=0.3, dry=1.0, delay_multiplier=1.0, delay_times=[0.0253, 0.0269, 0.029, 0.0307, 0.0322, 0.0338, 0.0353, 0.0367], delay_subchannel=0.001, allpass_frequences=[5250, 8560, 12410, 15410])])
    play voicefx2 amoansoft volume 0.15 loop 
    pause 0.5
    scene ch10_130_agd0_ with dissolve
    mc "Uh? -oh..."
    mc "Oh, [arelat] [a]..."
    pause
    mc "{i}Yeah, keep moving like that...{/i} *Hmmh...*"
    mc "Bouncing on me... {w=0.75}That’s so sexy... *hic*"
    a "{i}Do you like it?"
    mc "Yeah, *uh*..."
    a "{i}T-then I’ll keep going..."
    mc "Put it in..."
    a "{i}S-stop... *Hm*..."
    a "{i}Don’t insist on that, [mc]... *huh*..."
    a "..."
    a "{i}{size=-3}I-I want to too..."
    pause
    a "*Uhm, hmm, hngh...* Believe me, I do too..."
    hide screen random_anim_speed_normal with nothing
    show screen random_anim_speed_slow2 with nothing
    a "I’d love to..."
    pause
    a "*Hah, hah*... {i}Uuh, you’re so hard, honey..."
    a "*Ah, ah* {i}Y-you have a...{w=0.5} beautiful cock."
    pause
    $ current_pov = 2
    scene ch10_130_agd1_
    a "*Uh, hah*"
    mc "You’re moaning..."
    a "*Hmm, ah* {i}I can’t hold it in..."
    mc "*Hmh* If you move like that, I won’t be able to hold it either."
    a "*Aaah...* Yes, baby, do it... Cum for me, honey, don’t hold back..."
    mc "Huh [arelat!cl] [a]...  you’re like... s-super hot... like, stupid hot... even when you’re just... being you..."
    mc "But when you do it on purpose? Shit I can’t even think straight..."
    $ hide_anim_speed()
    call screen ch10_130_agd_ with dissolve
label beforech10_130: 
    $ hide_anim_speed()
    $ anim_speed = 0.015
    a "*Hah, ahhmh!*"
    mc "Are you close?"
    a "Y-yes *hah, ah*{w=0.5} {i}yes, honey!"
    pause
    $ anim_speed = 0.05
    if current_pov != 1:
        scene ch10_130_agd0_
    $ anim_speed = 0.015
    mc "*Hic* {i}That’s it, keep massaging my cock with your pussy, don’t stop- *uh*..."
    mc "{i}I want your scent on me till tomorrow..."
    a "*huh* Yes, baby..."
    mc "{i}Tell me, [arelat] [a], I want to know how much you’re enjoying this."
    a "{i}A-a lot, honey... *huh*."
    pause
    mc "{i}What’s the matter? Can’t quite get there?"
    mc "{i}Need a little help?"
    a "*Huh... I... hmm...*"
    pause
    stop voicefx fadeout 0.5
    play voicefx2 amoan1 fadein 0.5 volume 0.3 loop 
    $ disable_even_frames()
    scene ch10_130_agdc_ with vpunch
    $ anim_speed = 0.02
    a "*Haah*, [mc]!"
    mc "Do it, [arelat] [a]. I want to hear you moan..."
    mc "That’s it, keep moaning. Let [drelat] [d] hear, for the last time, the moans of pleasure from his ex-wife!"
    a "*Haah, aah, haah!* Oh my...{w=0.5} God!"
    pause
    stop voicefx2 fadeout 1.0
    play voicefx2 "audio/wavs/a/amoanhard_2.ogg"
    scene ch10_137 with hpunch
    $ renpy.pause(0.5, hard=True)
    image ch10_130cummings2:
        "ch10_137_2" with dissolve
        0.2
        "ch10_137_1" with dissolve
        0.2
        "ch10_137_2" with dissolve
        0.2
        "ch10_137_1" with dissolve
        0.2
        "ch10_137_2" with dissolve
        0.2
        "ch10_137_3" with cumming
    scene ch10_130cummings2
    $ renpy.pause(2.3, hard=True)
    play voicefx "audio/character/a/acum/a_acum_11.wav"
    a "Aaaah!" with cumming
    scene ch10_137_2
    $ renpy.pause(1.0, hard=True)
    image ch10_138anim:
        "ch10_138_2-1" with dissolve
        1.0
        "ch10_138_2-2" with dissolve
        0.1
        "ch10_138_2-1" with dissolve
        0.1
        "ch10_138_2-2" with dissolve
        0.1
        "ch10_138_2-1" with dissolve
        0.1
        "ch10_138_2-2" with dissolve
        0.1
        #
        "ch10_138_2-1" with dissolve
        1.0
        "ch10_138_2-2" with dissolve
        0.1
        "ch10_138_2-1" with dissolve
        0.1
        "ch10_138_2-2" with dissolve
        0.1
        "ch10_138_2-1" with dissolve
        0.1
        "ch10_138_2-2" with dissolve
        0.1
        #
        "ch10_138_2-1" with dissolve
        1.0
        "ch10_138_2-2" with dissolve
        0.1
        "ch10_138_2-1" with dissolve
        1.0
        repeat
    scene ch10_138anim
    a "*Uuh* Oh...{w=0.5} my God..."
    pause
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_139
    mc "That was so damn sexy, [arelat] [a]..."
    a "{i}Uh..."
    a "{i}{size=-3}D-did I make too much noise?"
    a "{i}{size=-3}Do you think anyone heard us?"
    mc "{i}Nah-*hic*{w=0.5}, just you."
    a "{i}{size=-3}Let’s stay quiet for a while... *huh*..."
    pause
    scene ch10_140
    a "{i}Honey, I don’t know how you do it... I-I’ve never..."
    a "{i}I’ve n-never had reactions like that from... you know."
    mc "{i}You’re welcome."
    scene ch10_139
    pause
    mc "{i}You even squirted and everything... wow."
    a "{i}Y-yeah..."
    mc "{i}I’m glad you enjoyed it... You deserve nothing less, [arelat] [a]."
    a "{i}Thank you, sweetheart..."
    a "Uhm..."
    pause
    scene ch10_140
    a "[mc]..."
    a "N-now it’s your turn."
    mc "{i}Yeah? *hic*"
    a "{i}Yeah..."
    scene ch10_141
    a "So, what should we do about that erection?"
    a "Want to use my legs again? Or maybe you'd rather have my mouth..."
    $ hide_anim_speed()

    default mod_d69_ch10eng_entrambe1 = False

    menu:
        "Legs":
            mc "[arelat!cl] [a], can I use your sexy legs?"
            a "A-alright. Let me help you up."
            jump ch10_140_clegs
        "Blowjob":
            mc "[arelat!cl] [a], can I get a blowjob?"
            a "O-okay... but you’ll have to get up first, honey. Think you can manage?"
            mc "For a blowjob from you, I could float, [arelat] [a]... *hic*."
            a "*Giggle*{w=0.7}{nw}"
            jump ch10_140_cmouth
        "[JGR]Mod_ Both":
            $ mod_d69_ch10eng_entrambe1 = True
            jump ch10_140_clegs


label ch10_140_clegs:
    camera:
        zoom 1.0
        xalign 0.5 
        yalign 0.5
    $ hide_anim_speed()
    show screen random_speed(0.007, 0.009)
    scene ch10_130athj4_
    mc "*Hmngh!*"
    a "{i}Let it all out, honey. *uhm...*"
    camera:
        subpixel True
        parallel:
            pause 0.1
            ease 0.03 xoffset 12
            ease 0.03 xoffset -12
            ease 0.03 xoffset 10
            ease 0.03 xoffset -10
            ease 0.03 xoffset 8
            ease 0.03 xoffset -8
            ease 0.03 xoffset 6
            ease 0.03 xoffset -6
            ease 0.03 xoffset 5
            ease 0.03 xoffset -5
            ease 0.03 xoffset 4
            ease 0.03 xoffset -4
            ease 0.03 xoffset 3
            ease 0.03 xoffset -3
            ease 0.03 xoffset 2
            ease 0.03 xoffset -2
            ease 0.03 xoffset 1
            ease 0.03 xoffset -1
            ease 0.03 xoffset 0
        parallel:
            pause 0.1
            ease 0.03 yoffset -10
            ease 0.03 yoffset 10
            ease 0.03 yoffset -8
            ease 0.03 yoffset 8
            ease 0.03 yoffset -7
            ease 0.03 yoffset 7
            ease 0.03 yoffset -6
            ease 0.03 yoffset 6
            ease 0.03 yoffset -5
            ease 0.03 yoffset 5
            ease 0.03 yoffset -4
            ease 0.03 yoffset 4
            ease 0.03 yoffset -3
            ease 0.03 yoffset 3
            ease 0.03 yoffset -2
            ease 0.03 yoffset 2
            ease 0.03 yoffset -1
            ease 0.03 yoffset 1
            ease 0.03 yoffset 0
    scene ch10_142_1 with nothing
    mc "*Argh!*{w=0.5}{nw}"
    scene ch10_142_2
    pause 0.5
    camera:
        subpixel True
        parallel:
            pause 0.1
            ease 0.03 xoffset -12
            ease 0.03 xoffset 12
            ease 0.03 xoffset -10
            ease 0.03 xoffset 10
            ease 0.03 xoffset -8
            ease 0.03 xoffset 8
            ease 0.03 xoffset -6
            ease 0.03 xoffset 6
            ease 0.03 xoffset -5
            ease 0.03 xoffset 5
            ease 0.03 xoffset -4
            ease 0.03 xoffset 4
            ease 0.03 xoffset -3
            ease 0.03 xoffset 3
            ease 0.03 xoffset -2
            ease 0.03 xoffset 2
            ease 0.03 xoffset -1
            ease 0.03 xoffset 1
            ease 0.03 xoffset 0
        parallel:
            pause 0.1
            ease 0.03 yoffset 10
            ease 0.03 yoffset -10
            ease 0.03 yoffset 8
            ease 0.03 yoffset -8
            ease 0.03 yoffset 7
            ease 0.03 yoffset -7
            ease 0.03 yoffset 6
            ease 0.03 yoffset -6
            ease 0.03 yoffset 5
            ease 0.03 yoffset -5
            ease 0.03 yoffset 4
            ease 0.03 yoffset -4
            ease 0.03 yoffset 3
            ease 0.03 yoffset -3
            ease 0.03 yoffset 2
            ease 0.03 yoffset -2
            ease 0.03 yoffset 1
            ease 0.03 yoffset -1
            ease 0.03 yoffset 0
    scene ch10_142_3 with nothing
    mc "!hmmgh!{w=0.5}{nw}"

    scene ch10_142_2
    pause 0.5


    camera:
        subpixel True
        parallel:
            pause 0.1
            ease 0.03 xoffset 12
            ease 0.03 xoffset -12
            ease 0.03 xoffset 10
            ease 0.03 xoffset -10
            ease 0.03 xoffset 8
            ease 0.03 xoffset -8
            ease 0.03 xoffset 6
            ease 0.03 xoffset -6
            ease 0.03 xoffset 5
            ease 0.03 xoffset -5
            ease 0.03 xoffset 4
            ease 0.03 xoffset -4
            ease 0.03 xoffset 3
            ease 0.03 xoffset -3
            ease 0.03 xoffset 2
            ease 0.03 xoffset -2
            ease 0.03 xoffset 1
            ease 0.03 xoffset -1
            ease 0.03 xoffset 0
        parallel:
            pause 0.1
            ease 0.03 yoffset -10
            ease 0.03 yoffset 10
            ease 0.03 yoffset -8
            ease 0.03 yoffset 8
            ease 0.03 yoffset -7
            ease 0.03 yoffset 7
            ease 0.03 yoffset -6
            ease 0.03 yoffset 6
            ease 0.03 yoffset -5
            ease 0.03 yoffset 5
            ease 0.03 yoffset -4
            ease 0.03 yoffset 4
            ease 0.03 yoffset -3
            ease 0.03 yoffset 3
            ease 0.03 yoffset -2
            ease 0.03 yoffset 2
            ease 0.03 yoffset -1
            ease 0.03 yoffset 1
            ease 0.03 yoffset 0
    scene ch10_142_1 with nothing
    mc "*Argh!*{w=0.5}{nw}"
    scene ch10_142_2
    pause 0.5
    scene ch10_142_2
    pause 0.5
    scene ch10_142_1
    pause 0.5
    scene ch10_142_4
    mc "Uh.... hmmh..."
    pause
    a "{i}You let out a lot..."
    a "{i}You must’ve been holding that in all day..."
    mc "Uh... not exactly..."
    pause
    mc "Turn around."
    a "Hm? What for?"
    scene ch10_130_athjb2_
    a "Honey... how much more do you have in there?"
    mc "*Hmmngh!*, *hmngh!*..."
    pause
    scene ch10_130_athjb0_
    mc "*Mhg!*{w=0.5}{nw}"
    camera:
        subpixel True
        parallel:
            pause 0.1
            ease 0.03 xoffset -12
            ease 0.03 xoffset 12
            ease 0.03 xoffset -10
            ease 0.03 xoffset 10
            ease 0.03 xoffset -8
            ease 0.03 xoffset 8
            ease 0.03 xoffset -6
            ease 0.03 xoffset 6
            ease 0.03 xoffset -5
            ease 0.03 xoffset 5
            ease 0.03 xoffset -4
            ease 0.03 xoffset 4
            ease 0.03 xoffset -3
            ease 0.03 xoffset 3
            ease 0.03 xoffset -2
            ease 0.03 xoffset 2
            ease 0.03 xoffset -1
            ease 0.03 xoffset 1
            ease 0.03 xoffset 0
        parallel:
            pause 0.1
            ease 0.03 yoffset 10
            ease 0.03 yoffset -10
            ease 0.03 yoffset 8
            ease 0.03 yoffset -8
            ease 0.03 yoffset 7
            ease 0.03 yoffset -7
            ease 0.03 yoffset 6
            ease 0.03 yoffset -6
            ease 0.03 yoffset 5
            ease 0.03 yoffset -5
            ease 0.03 yoffset 4
            ease 0.03 yoffset -4
            ease 0.03 yoffset 3
            ease 0.03 yoffset -3
            ease 0.03 yoffset 2
            ease 0.03 yoffset -2
            ease 0.03 yoffset 1
            ease 0.03 yoffset -1
            ease 0.03 yoffset 0
    scene ch10_144_1 
    pause 1.0
    scene ch10_144_2
    pause
    mc "*Hah*..."
    scene ch10_130_athjb2_
    pause 1.0
    camera:
        subpixel True
        parallel:
            pause 0.1
            ease 0.03 xoffset -12
            ease 0.03 xoffset 12
            ease 0.03 xoffset -10
            ease 0.03 xoffset 10
            ease 0.03 xoffset -8
            ease 0.03 xoffset 8
            ease 0.03 xoffset -6
            ease 0.03 xoffset 6
            ease 0.03 xoffset -5
            ease 0.03 xoffset 5
            ease 0.03 xoffset -4
            ease 0.03 xoffset 4
            ease 0.03 xoffset -3
            ease 0.03 xoffset 3
            ease 0.03 xoffset -2
            ease 0.03 xoffset 2
            ease 0.03 xoffset -1
            ease 0.03 xoffset 1
            ease 0.03 xoffset 0
        parallel:
            pause 0.1
            ease 0.03 yoffset 10
            ease 0.03 yoffset -10
            ease 0.03 yoffset 8
            ease 0.03 yoffset -8
            ease 0.03 yoffset 7
            ease 0.03 yoffset -7
            ease 0.03 yoffset 6
            ease 0.03 yoffset -6
            ease 0.03 yoffset 5
            ease 0.03 yoffset -5
            ease 0.03 yoffset 4
            ease 0.03 yoffset -4
            ease 0.03 yoffset 3
            ease 0.03 yoffset -3
            ease 0.03 yoffset 2
            ease 0.03 yoffset -2
            ease 0.03 yoffset 1
            ease 0.03 yoffset -1
            ease 0.03 yoffset 0
    scene ch10_143_1 with Dissolve(0.2)
    mc "Hmgh!{w=1.0}{nw}"
    scene ch10_143_2 
    pause 1.0
    camera:
        subpixel True
        parallel:
            pause 0.1
            ease 0.03 xoffset -12
            ease 0.03 xoffset 12
            ease 0.03 xoffset -10
            ease 0.03 xoffset 10
            ease 0.03 xoffset -8
            ease 0.03 xoffset 8
            ease 0.03 xoffset -6
            ease 0.03 xoffset 6
            ease 0.03 xoffset -5
            ease 0.03 xoffset 5
            ease 0.03 xoffset -4
            ease 0.03 xoffset 4
            ease 0.03 xoffset -3
            ease 0.03 xoffset 3
            ease 0.03 xoffset -2
            ease 0.03 xoffset 2
            ease 0.03 xoffset -1
            ease 0.03 xoffset 1
            ease 0.03 xoffset 0
        parallel:
            pause 0.1
            ease 0.03 yoffset 10
            ease 0.03 yoffset -10
            ease 0.03 yoffset 8
            ease 0.03 yoffset -8
            ease 0.03 yoffset 7
            ease 0.03 yoffset -7
            ease 0.03 yoffset 6
            ease 0.03 yoffset -6
            ease 0.03 yoffset 5
            ease 0.03 yoffset -5
            ease 0.03 yoffset 4
            ease 0.03 yoffset -4
            ease 0.03 yoffset 3
            ease 0.03 yoffset -3
            ease 0.03 yoffset 2
            ease 0.03 yoffset -2
            ease 0.03 yoffset 1
            ease 0.03 yoffset -1
            ease 0.03 yoffset 0
    scene ch10_143_3 with Dissolve(0.2)
    mc "*Argh!*{w=1.0}{nw}"
    scene ch10_143_4 with Dissolve(1.5)
    mc "*Oh*.. *huh*..."
    pause
    a "Oh, [mc]..."
    a "*Muah* Did you get it all out?"
    mc "Yeah... *smch*"   
    pause
    a "*mnch*... {w=0.5}I’ll get a towel, lean against the wall."
    scene ch10_147 with vpunch
    a "{i}{size=-5}[mc]!"
    a "{i}{size=-3}Just look at you... Y-you’re never drinking a single drop of alcohol around me again. You heard me?"
    mc "{i}{size=-3}Yes, [arelat] [a]..."
    pause
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop voicefx fadeout 2.0
    stop voicefx2 fadeout 2.0
    stop background fadeout 2.0
    scene blackscreen with Dissolve(2.0)
    pause

    if mod_d69_ch10eng_entrambe1:
        jump ch10_140_cmouth

    jump ch10nxtd



label ch10_140_cmouth:
    hide screen random_anim_speed_normal2 with nothing
    hide screen random_anim_speed_normal with nothing
    hide screen random_anim_speed_slow with nothing
    $ anim_speed = 0.015
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_120ased1_
    a "*Slurp, slurp*"
    pause
    mc "*Hmm, uhh* A-almost..."
    a "*Slurp, hm-mmh*"
    mc "Do you want me to cum, [arelat] [a]? *hic*"
    a "*Slurp, slurp* {i}Hm-hmm..."
    mc "N-not yet... I want to keep going... *hngh*"
    a "{i}{size=-3}Mmm, we’ve b-been in the sh-wer a lo’ time, mmm... *slurp, slurp*..."
    mc "*Uhmh* [arelat!cl] [a]..."
    a "*Slurp, ch-chup* {i}{size=-3}C’m for me, b’mby... you m-need to m-let it out, mmm..."
    mc "*Hngh* {i}You want it now?"
    a "*Slurp, sl-slurp* {i}{size=-3}Mmh... juss l-let it out, d-don’t h-hold it..."
    mc "*Oh, uh*... {i}{size=-3}If you’re asking for it -I’ll gladly give you my cum, [arelat] [a]."
    mc "Here it comes, *hmgh*-I'm cumming..."
    a "*Slurp, slurp* Hm-hmm..."
    scene ch10_145_1 with hpunch
    play voicefx "audio/wavs/bj_6.ogg"
    mc "*Hmngh!*{w=1.0}{nw}"
    scene ch10_145_2
    play voicefx "audio/wavs/bj_15.ogg"
    play sound "audio/mouth/swallow_03.ogg"
    pause 1.0
    scene ch10_145_3
    play sound "audio/wavs/bj_63.ogg"
    pause 1.0
    scene ch10_145_4
    play voicefx "audio/wavs/bj_14.ogg"
    pause 0.5
    scene ch10_145_4-
    play sound "audio/mouth/swallow_02.ogg"
    pause 1.0
    scene ch10_145_5- with vpunch
    mc "*Mghh!* {w=1.0}{nw}"
    scene ch10_145_6-
    a "Hmn..."
    mc "*Uh.. huh...*"
    mc "Wow... *hic*"
    pause
    scene ch10_145_8-:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.0
        ease 3 zoom 1.01
        ease 3 zoom 1.0
        repeat
    mc "Uh... That was amazing..."
    scene ch10_145_9:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.0
        ease 3 zoom 1.01
        ease 3 zoom 1.0
        repeat
    a "*Buh*..."
    mc "(My legs are giving out...)" with dissolve
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_146 
    a "{i}{size=-3}Honey, g-give me a signal next time..."
    mc "Huh..."
    scene ch10_147 with vpunch
    a "[mc]!"
    a "{i}{size=-3}Just look at you... Y-you’re never drinking a single drop of alcohol around me again. You heard me?"
    mc "{i}{size=-3}Yes, [arelat] [a]..."
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop voicefx fadeout 2.0
    stop voicefx2 fadeout 2.0
    stop background fadeout 2.0
    scene blackscreen with Dissolve(2.0)
    pause
    jump ch10nxtd

label ch10nxtd:
    $ renpy.end_replay()
    $ renpy.music.set_audio_filter("music", None)
    $ renpy.music.set_audio_filter("sound", None)
    $ renpy.music.set_audio_filter("sound_fx", None)
    $ renpy.music.set_audio_filter("voicefx", None)
    $ renpy.music.set_audio_filter("voicefx2", None)
    $ renpy.music.set_audio_filter("background", None)
    $ clear_audiofx()
    stop sound fadeout 1.0
    stop voicefx fadeout 1.0
    stop music fadeout 1.0
    scene blackscreen #mc wakes up in his room, barely piecing together what happened yesterday.
    pause
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_148 with Dissolve(2.0)
    mc "Uh..."
    mc "(I don’t even know how I got back to my room.)" with dissolve
    s "[mc]!" 
    play music scene2 fadein 3.0
    s "*Knock knock* [mc]-wake up!"
    mc "Mm-coming..."
    scene ch10_150 with fade
    mc "Yeah?"
    s "We made tacos!"
    mc "Oh, really?"
    s "I helped, too. We used my recipe-so it’s basically like I made them."
    mc "Oh... are they good?"
    s "You bet-obviously good!"
    mc "Alright, I’ll be there in a sec."
    if stephloving == "True":
        scene ch10_151 
        s "{i}{size=-3}But first let’s kiss a little, okay?"
        mc "{i}{size=-3}Didn’t you say they’re waiting for us?"
        s "{i}{size=-3}Who cares..."
        pause
        scene ch10_153
        s "{i}{size=-3}[mc], can we do ''that thing'' real quick?"
        mc "{i}{size=-3}They're waiting for us for breakfast."
        s "{i}{size=-3}That’s why I said real quick, dummy..."
        mc "{i}{size=-3}Besides, my head kinda hurts..."
        mc "*Smch* {i}{size=-3}Later, okay?"
        s "{i}{size=-3}Alright... *mch*."
        pause
        scene ch10_154
        s "Don’t forget we’re going to the fair today."
        mc "Yeah yeah, I remember, I remember..."
        s "{i}{size=-3}Don’t spank me!"
        mc "(I’d forgotten...)" with dissolve
    scene blackscreen 
    pause
    scene ch10_155
    s "[mc]."
    mc "Morning."
    scene ch10_156
    s "I’ll go get your plate!"
    mc "Thanks."
    scene ch10_157 
    mc "Did [mia] stay the night?"
    k "Yeah. How’s the hangover?"
    mc "So-so. You?"
    k "What do you mean 'you?'"
    k "You and [drelatks] were the only ones drinking last night."
    mc "Sorry, force of habit."
    k "Force of habit?"
    k "Shut up, I barely even drink..."
    mia "Oh, you drink? Shocking news..."
    scene ch10_158
    s "Ta-daa!"
    mc "Mmm! They look great!"
    scene ch10_159
    s "I made them all by myself.{w=1.0} Well, [arelatks] helped a little..."
    mc "Mmm, my mouth’s watering!"
    s "They’re vegan tacos!"
    mc "Uh... No meat?"
    s "Yep, one hundred percent healthy!"
    s "The salsa was made by [mia] and [k]."
    s "{i}{size=-4}I don’t recommend using too much..."
    k "What’s wrong with the salsa?"
    s "It’s too spicy."
    k "It is not."
    scene ch10_159-
    mia "{i}{size=-3}I think she’s having another one of those jealous episodes, like at the beach."
    k "Yeah, probably."
    s "Huh? J-jealous of what?"
    s "Y-you do know [mc] is my [srelatmc], right?"
    scene ch10_160
    mc "Good morning."
    a "Good morning, honey."
    mc "How did you sleep?"
    a "Very well. And you?"
    scene ch10_161
    mc "Slept great. Wish I could sleep like that every night."
    a "{i}{size=-3}*Giggle*{w=1.0}{nw}"
    a "Same here."
    image ch10_160mem:
        "ch10_71_3"
        0.3
        "ch10_71_2-"
        0.3
        "ch10_71_4_"
        0.3
        "ch10_75_2-"
        0.3
        "ch10_75_3-"
        0.3
        "ch10_75_1-"
        0.3
        "ch10_101"
        0.3
        "ch10_137"
        0.3
    scene ch10_160mem with flash
    "{nw}"
    scene ch10_161 with flash
    pause
    s "Are they good?"
    mc "Uh, yeah..."
    scene ch10_162
    mc "Mmm! Yeah! The salsa's kinda spicy, but it adds a great flavor. You’re a good cook, [s]."
    s "Hehe..."
    scene ch10_163
    s "You already finished them?"
    mc "Told you, they were really good."
    s "Going for more?"
    mc "Yeah."
    s "You’re such a glutton."
    mc "It’s part of my health diet."
    s "If you say so..."
label ch10a2:
    if _in_replay:
        play music scene2 fadein 3.0
    scene ch10_164 with fade
    mc "Hey."
    a "Hey, sweetheart. Looking for something?"
    mc "{i}[arelat!cl] [a], that was really good."
    a "You think so?"
    mc "{i}Can we go for seconds?"
    a "Uhm... seconds?"
    scene ch10_165
    mc "Can’t we?"
    a "Uhm...{w=0.5} {i}{size=-3}Y-yeah, maybe we could... another day..."
    a "{i}But... we’d have to be completely alone and-{w=0.7}{nw}"
    scene ch10_166
    mc "Great, can you make me two more?"
    a "Huh?"
    mc "They’re tasty but kinda small. Two didn’t fill me up."
    scene ch10_167
    a "O-oh... you meant the tacos."
    mc "Hm?"
    scene ch10_169
    a "Y-yeah, of course, take as many as you want from that plate."
    mc "Were they for you?"
    a "No, they were for your [drelat] [d], but I’ll make him some more."
    mc "Oh, alright."
    mc "[s] told me she made them."
    a "She found the recipe and prepped them, but I cooked the filling."
    a "[s] was dead set on making them vegan. No idea why she decided to go vegan today."
    a "Did you really like them?"
    mc "Yeah, they were good."
    scene ch10_168
    a "Wait, do you want me to add meat?"
    mc "Oh, yes, please."
    mc "Your meat always tastes great..."
    scene ch10_170 #he gives her a big handful of ass while no one’s looking, hidden in the kitchen while the others are in the living room
    pause
    scene ch10_171
    a "We have beef and chicken in the fridge."
    image ch10_171anim:
        "ch10_170" with dissolve
        2.0
        "ch10_171" with dissolve
        2.0
        repeat
    scene ch10_171anim
    mc "Hmm, I like both."
    a "Do you want me to make you some of each?"
    scene ch10_172
    mc "Really?"
    a "Yes, think of it as a little gift for your first week at work."
    scene ch10_173
    mc "Thank you so much."
    image ch10_173anim:
        "ch10_173" with dissolve
        2.0
        "ch10_174" with dissolve
        2.0
        repeat
    scene ch10_173anim 
    pause
    mc "I liked the gift you gave me yesterday too..."
    a "..."
    a "{i}{size=-3}You actually remember? You were so drunk..."
    mc "Of course I remember. How could I forget something like that?"
    scene ch10_175
    pause
    scene ch10_176
    pause
    image ch10_175anim:
        "ch10_175" with dissolve
        1.5
        "ch10_176" with dissolve
        1.5
        repeat
    scene ch10_175anim
    mc "{i}{size=-3}You were amazing..."
    mc "{i}{size=-3}I can still feel the texture of your wet skin in the palms of my hands..."
    a "{i}I’ll get them ready now, honey. Go sit down..."
    scene ch10_183
    a "{i}{size=-3}[mc]..."
    mc "Just thinking about what we did got me like this, [arelat] [a]." #mc shows her his morning erection through his shorts, the large outline of his penis clearly visible
    scene ch10_184
    a "..."
    scene ch10_178
    pause
    scene ch10_179
    a "..."
    image ch10_179anim:
        "ch10_178" with Dissolve(0.5)
        1.0
        "ch10_179" with Dissolve(0.5)
        1.5
        "ch10_178" with Dissolve(0.5)
        2.0
        "ch10_179" with Dissolve(0.5)
        1.0
        "ch10_178" with Dissolve(0.5)
        1.0
        "ch10_179" with Dissolve(0.5)
        1.0
        "ch10_178" with Dissolve(0.5)
        2.0
        "ch10_179" with Dissolve(0.5)
        1.5
        "ch10_178" with Dissolve(0.5)
        1.0
        "ch10_179" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_179anim
    pause
    mc "{i}{size=-3}I even dreamed about you..."
    a "[mc]..."
    mc "{i}{size=-3}It wasn’t anything sexual!"
    mc "{i}{size=-3}The sexual part already happened yesterday in the shower..."
    a "{i}{size=-3}[mc]..."
    a "..."
    pause
    scene ch10_180 with Dissolve(0.5)
    a "..."
    pause
    scene ch10_181 with Dissolve(0.5)
    a "{i}{size=-3}I just didn’t want you to be upset with me about the beach..."
    mc "{i}Something happened at the beach?"
    a "{i}{size=-3}Well... I thought maybe you were a little frustrated..."
    scene ch10_184 with dissolve
    a "{i}{size=-3}And..."
    pause
    scene ch10_183 with dissolve
    a "{i}{size=-3}Sweetheart, the girls are going to see that if you don’t hide it..."
    a "{i}{size=-3}And with no shirt on, you’ve got no way to cover it..."
    scene ch10_185
    mc "{i}{size=-3}Then how about we go to your room?"
    scene ch10_186
    a "{i}{size=-3}But your [drelat] [d] is sleeping in there..."
    scene ch10_186
    mc "{i}{size=-3}Then let’s go to the living room..."
    a "{i}{size=-3}[mc], you’re insane..."
    image ch10_185anim:
        "ch10_186" with Dissolve(0.5)
        1.0
        "ch10_187" with Dissolve(0.5)
        1.5
        "ch10_186" with Dissolve(0.5)
        2.0
        "ch10_187" with Dissolve(0.5)
        1.0
        "ch10_186" with Dissolve(0.5)
        1.0
        "ch10_187" with Dissolve(0.5)
        1.0
        "ch10_186" with Dissolve(0.5)
        2.0
        "ch10_187" with Dissolve(0.5)
        1.5
        "ch10_186" with Dissolve(0.5)
        1.0
        "ch10_187" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_185anim
    a "{i}{size=-3}How can you still be in the mood? It hasn’t even been half a day..."
    mc "Blame it on your beauty."
    scene ch10_188-
    a "{i}{size=-3}O-okay, okay, that’s enough!"
    a "{i}{size=-3}Don’t you remember the beach?"
    a "{i}{size=-3}We were fooling around, and that woman almost caught us."
    mc "{i}{size=-3}Here we have doors with locks..."
    a "{i}{size=-3}... {w=0.5}N-no."
    mc "{i}{size=-3}Come on, [arelat] [a]..."
    scene ch10_184
    mc "I can’t go out there like this."
    a "..."
    scene ch10_188--
    a "Then go eat your tacos at the table until you cool off."
    mc "..."
    pause
    scene ch10_189
    a "{i}{size=-3}Tonight..."
    scene ch10_190
    pause
    scene ch10_188--
    mc "{i}{size=-3}Now you’ve just made it last twice as long..."
    a "*Giggle* {i}{size=-3}Sorry..."
    mc "{i}{size=-3}It's okay. Not your fault you're this hot."
    a "*Giggle* {i}{size=-3}You silly boy..."
    stop music fadeout 1.5
    scene blackscreen with fade
    $ renpy.end_replay()
    pause
    play music scene1 fadein 0.5
    scene ch10_191
    s "[mc], you said you were getting more tacos."
    mc "Phew, yeah, they were really good..."
    s "Y-you already ate them?!"
    s "Your butt’s gonna get big like mine."
    k "Want me to lend you some clothes or are we going to your house?"
    mia "Let’s go to mine, please. I don’t think giraffe-girl clothes will fit me."
    if stephloving == "True": 
        scene ch10_195
        s "{i}{size=-3}[mc], let’s go to your room now."
        mc "{i}What?"
        s "{i}{size=-3}Let’s go to your room so we can, you know..."
        mc "{i}{size=-3}Shh... We can’t do that all the time..."
        mc "(Actually...)" with dissolve
        mc "(There wouldn’t be much of a problem if we locked the door and kept quiet, we’ve done it before...)" with dissolve
    scene ch10_194
    k "[s], are you coming?"
    s "Where?"
    s "Oh, right!"
    mia "You got ready this morning just for that, did you already forget?"
    scene ch10_193
    mc "You guys going somewhere?"
    k "We’re going shopping."
    mc "Ah, have fun."
    mia "Not coming?"
    mc "Afraid not."
    mia "Why?"
    k "I’ll explain later, come on."
    scene ch10_196
    d "Morning."
    mia "Good morning, Mr. [d]."
    d "Things got a little wild yesterday, hehe. Hope I didn’t embarrass you."
    d "You or myself..."
    mia "Don’t worry, my mom is way worse."
    d "Did you guys eat already?"
    scene ch10_197
    s "We made homemade tacos for [mc]!"
    d "Tacos, hmm..."
    s "I’ll make you some right now."
    d "Yes, sweetheart, please."
    scene ch10_198
    d "Well, at least I wasn’t the only one who got carried away yesterday."
    d "I know a few others who were suspiciously alone on the beach, surrounded by a bunch of empty beer bottles..."
    scene ch10_199
    mia "Uh?"
    scene ch10_200
    mia "What are you talking about, Mr. [d]? Haha..."
    d "Haha, forget it. I didn’t see anything."
    scene ch10_201
    d "Are the tacos good?"
    mc "I’m about to explode."
    d "{i}{size=-3}Tacos... and for breakfast too. Jesus Christ..."
    scene ch10_202
    d "Honey, are you in the kitchen?"
    a "Yes?"
    d "Make me some coffee."
    scene ch10_203
    mia "[mc], come outside with me."
    mc "Why? Sure."
    scene ch10_204
    mc "What’s up?"
    mia "I’ll tell outside."
    stop music fadeout 1.0
    scene blackscreen
    pause
    play music scene2 fadein 0.5
    scene ch10_205_ with fade
    pause
    mia "You don’t smoke, right?"
    mc "Only when I drink."
    pause
    scene ch10_206
    mc "So..."
    mia "I don’t know. [k] told me to bring you with me. "
    mc "I wonder what she wants."
    pause
    mia "I like your place. It’s full of trees and all that."
    mia "It’s peaceful..."
    if miatell > 2:
        mc "The beach was fun."
        scene ch10_208
        mia "Yeah."
        mia "Especially when that old lady showed up."
        mia "That reminds me..."
        scene ch10_209 with hpunch
        mia "Ugh! Why didn’t you let me hit her?"
        mc "Did you want to get arrested?"
        scene ch10_208
        mia "And when you told her that lie about me being pregnant, haha."
        mia "And the money thing, haha, that was a good one."
        mc "I was nervous."
        scene ch10_208-
        mia "It was smart, you kept us out of trouble."
        mc "Yeah, trouble you were ready to jump into."
        scene ch10_206
        mia "Totally, haha. Sorry, I just can’t stand Karens."
        pause
        mia "I invited you to a party the other day, and you totally brushed me off."
        mc "Really? When?"
        mia "Don’t play dumb..."
        scene ch10_207
        mia "You haven’t talked to me since then."
        mc "I’ve been busy."
        mia "Sure, with [k]."
        mc "I could be busy with you too."
        scene ch10_208-
        mia "You think you can handle both of us?"
        mc "And two more..."
        scene ch10_206
        mia "Hahaha- Big talker..."
        pause
        mia "By the way, I’m in an open relationship with [dereck]."
        mia "I’m not a slut, if that’s what you’re thinking."
        mc "I’m kind of a slut too, it’s fine."
        mia "Well I’m not."
        pause
        scene ch10_208
        mia "Okay... maybe a little."
        "Hahaha."
        pause
        mc "So what’s that kind of relationship like?"
        scene ch10_208-
        mia "An open relationship?"
        mia "Well, we can sleep with other people and still be together. That simple."
        mc "Nice."
        pause
        mia "You could totally have something like that with [k]."
        mia "Actually... isn’t that kind of what you already have?"
        mc "What are you talking about? Are you crazy?"
        scene ch10_208
        mia "You know what's actually crazy? You fucking your [krelat]."
        mia "Now that’s crazy."
        pause
        mc "Yeah..."
        pause
        scene ch10_208-
        mia "But it’s fine!"
        mia "I’ve got it! We should have a relationship with the three of us."
        mc "The three of us together?"
        mc "Haha, that’d be even crazier."
        pause

    scene ch10_210
    mc "*Ouch*"
    k "What are you two doing!?"
    mc "Was the butt pinch really necessary?"
    scene ch10_211
    k "Couldn’t you pick a less suspicious place?"
    mia "I didn’t want your parents to catch me smoking."
    mia "Anyway, we’re here now. What you wanna tell us?"
    k "Right."
    scene ch10_212
    k "I came up with an idea to get [drelatks] to stop being mad about, you know..."
    mia "[k], no need to talk in code in front of me. Your [drelatks] is mad because he caught you two fucking."
    k "You're going to be [mia]’s boyfriend."
    scene ch10_213 with hpunch
    mia "What!?"
    k "[drelatks!cl] thinks you two have something. We need to take advantage of that."
    mc "And who told you that?"
    k "It’s obvious."
    k "Remember the other day, when I ran off because [drelatks] was coming and you two stayed behind?"
    k "He probably saw you together, alone, and thought... well, the obvious."
    k "Or at least what seemed obvious."
    k "Please..."
    scene ch10_214
    mia "By the way, that was one hell of a fuck I witnessed."
    scene ch10_215
    mia "You two fuck like porn stars, heh..."
    scene ch10_214
    k "So? Are you helping me or not?"
    mia "[k], I don’t know... your [drelatks] knows I have a boyfriend."
    k "I’m not saying be actual boyfriend and girlfriend! Just act sweet around him, it doesn’t have to be real."
    scene ch10_216
    k "Besides, cheating exists... and he knows that better than anyone."
    k "I just want things to go back to normal, guys..."
    pause
    mia "Fine, let’s do it."
    mc "Are you serious?"
    mia "Look at those puppy eyes, how could you say no to that?"
    mc "Uh... is this really necessary, [k]?"
    k "Yes, [mc], it is."
    k "You’re not even a little ashamed?"
    mc "Well...{w=0.5} not that much."
    mc "He’ll get over it."
    k "[mc]..."
    mc "Maybe I should just get a real girlfriend instead."
    scene ch10_217
    "..."
    pause
    mc "(Though now that I think about it... there wouldn’t really be any consequences, unless [dereck] breaks my nose if he finds out.)" with dissolve
    mc "(Actually, [dereck] might not even be mad. They’re in an open relationship, and this wouldn’t even be real...)" with dissolve
    if stephloving == "True":
        s "[mc]!"
        s "[mc], where are you?!"
    else:
        a "[mc], you didn’t wash your plate!"
    scene ch10_218---
    mc "I’m being summoned."
    k "Come on, [mc]... It won’t kill you."
    mc "I’ll think about it."
    pause

    stop music fadeout 1.0
    scene blackscreen 
    pause
    if stephloving == "True":
        jump ch10s1
    else:
        jump ch10_243afss
label ch10s1:
    scene ch10_219:
        zoom 0.75
    play music scene3 fadein 0.5
    s "[mc]."
    mc "You called me?"
    scene ch10_220:
        zoom 0.75
    s "{i}[drelatks!cl] went back to sleep..."
    mc "Oh yeah?"
    s "Yeah..."
    scene ch10_221 with dissolve:
        zoom 0.75
    s "Wanna go to your room?"
    mc "Hmm..."
    scene ch10_222 with vpunch:
        zoom 0.75
    mc "Let’s go."
    s "Eek!"
    stop music fadeout 1.0
    scene ch10_223_ with fade
    play music sexy3 fadein 0.5
    s "*Giggle*"
    pause
    scene ch10_223-
    mc "What’s up with you, hm?"
    s "I’m excited, *giggle*."
    mc "Really in the mood?"
    s "Yeah, are you?"
    mc "{i}Me too."
    play sound kissing volume 0.3 loop fadein 0.1
    play voicefx2 kissing2 volume 0.1 loop fadein 0.1
    scene ch10_226_1
    mc "Hmm..."
    image ch10_226anim:
        "ch10_226_1" with Dissolve(0.5)
        0.65
        "ch10_226_2" with Dissolve(0.5)
        1.0
        "ch10_226_1" with Dissolve(0.5)
        1.0
        "ch10_226_2" with Dissolve(0.5)
        1.0
        "ch10_226_1" with Dissolve(0.5)
        1.0
        
        "ch10_226_3" with Dissolve(0.5)
        0.65
        "ch10_226_4" with Dissolve(0.5)
        0.65
        "ch10_226_3" with Dissolve(0.5)
        0.65
        "ch10_226_4" with Dissolve(0.5)
        0.65
        repeat
    scene ch10_226anim
    play voicefx2 kissing2 fadein 0.5 loop volume 0.2
    s "*Hamh, mch*..."
    s "*Lahl*..."
    pause
    stop voicefx fadeout 0.05
    stop voicefx2 fadeout 0.05
    $ stop_sounds(0.5)
    scene ch10_227
    mc "{i}{size=-3}Take off your shorts. I wanna eat that horny little pussy."
    s "{i}{size=-3}You take them off."
    scene ch10_228
    mc "{i}{size=-3}Let’s see..."
    s "{i}{size=-3}Hurry, [mc]."
    mc "{i}{size=-3}I’m on it, relax..."
    scene ch10_229
    mc "{i}{size=-3}First, let’s move these out of the way."
    s "*Giggle*"
    pause
    scene ch10_230
    mc "Hmm... {i}{size=-3}That looks delicious..."
    mc "{i}{size=-3}You’ve got a cute little pussy."
    s "Thanks..."
    s "{i}{size=-3}[mc], don't just stare at it."
    scene ch10_231_1
    mc "*Msh*..."
    play voicefx smoansoft volume 0.25 loop
    play voicefx2 kissing2 volume 0.1 loop
    scene ch10_231_2
    s "*Huh*..."
    image ch10_231anim:
        "ch10_231_1" with Dissolve(0.5)
        1.0
        "ch10_231_2" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_231anim
    s "*Huh* {i}{size=-3}When you use your whole tongue... I really like that..."
    mc "*Hmsh* {i}{size=-3}Good..."
    s "{i}{size=-3}Yes, like that."
    mc "*Chup* {i}{size=-3}Mmm, such a tasty little pussy..."
    s "*Huh*... {i}{size=-3}That thing you’re doing -*huh*... feels good."
    pause
    s "{i}{size=-3}B-but don’t stop what you were doing before."
    pause
    s "{i}{size=-3}You have to suck it with your whole mouth, [mc], just like before."
    scene ch10_232_1
    mc "*Hmh* {i}{size=-3}Like this?"
    scene ch10_232_2
    s "*Huh* {i}{size=-3}Yeah, but keep doing the other thing too."
    image ch10_232anim:
        "ch10_232_1" with Dissolve(0.5)
        1.0
        "ch10_232_2" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_232anim
    s "*huh* {i}{size=-3}Yes, lick it a little and then swirl your tongue around it."
    mc "{i}{size=-3}You’re getting a little demanding..."
    pause
    s "{i}{size=-3}Almost there..."
    scene ch10_233_1
    pause
    scene ch10_233_2
    mc "*slch* {i}{size=-3}Are you about to feel it?"
    image ch10_233animcm:
        "ch10_233_1" with Dissolve(0.1)
        0.15
        "ch10_233_2" with Dissolve(0.1)
        0.15
        "ch10_233_1" with Dissolve(0.1)
        1.0
        "ch10_233_2" with Dissolve(0.1)
        0.15
        "ch10_233_1" with Dissolve(0.1)
        0.15
        "ch10_233_2" with Dissolve(0.1)
        1.0
        "ch10_233_1" with Dissolve(0.1)
        2.0
        "ch10_233_2" with Dissolve(0.1)
        1.0
        repeat
    scene ch10_233animcm
    s "*Hmnnn, huh, hmm*..."
    pause
    image ch10_234anim:
        "ch10_233_3" with Dissolve(0.25)
        1.0
        "ch10_233_4" with Dissolve(0.25)
        1.0
        repeat
    stop voicefx fadeout 0.2
    stop voicefx2 fadeout 0.2
    scene ch10_234anim
    pause
    s "*Huh, huh, huh* {i}{size=-3}That was so good..."
    s "{i}S-see? I told you I’d be quick..."
    mc "Yeah."
    mc "{i}Now will you do me?"
    s "Yeah... just need a quick breather... *phew*..."
    pause
    scene ch10_234-
    pause
    s "Alright, [mc]."
    s "{i}{size=-3}Pull your dick out! Come on, do it now!"
    mc "Whoa, you’re really fired up, huh?"
    mc "Here it is, come get it."
    scene ch10_235 
    s "{i}There you are..."
    s "{i}{size=-3}Wow, you’re really hard..."
    mc "{i}{size=-3}I’m gonna need a really good suck..."
    s "{i}{size=-3}I’ll suck it really good."
    scene ch10_236
    s "*Ub*..."
    mc "Oh yeah..."
    mc "Ahh, is this how you wanted me to use my tongue on you?"
    s "U-huh..."
    scene ch10_236-
    mc "Noted."
    jump afterch10_235sbj1_











init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1

    def ch10_235sbj1_(trans, st, at):
        if store.current_active_animation != "ch10_235sbj1_":
            store.current_active_animation = "ch10_235sbj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_235sbj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_235sbj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.25 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_235sbj2_(trans, st, at):
        if store.current_active_animation != "ch10_235sbj2_":
            store.current_active_animation = "ch10_235sbj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_235sbj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_235sbj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.25 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 2.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value


screen ch10_235sbj1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.03)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.02)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.016)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.016), Show("random_speed", min_speed=0.016, max_speed=0.03)]  style "textbutton_choice" 
    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_235sbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_235sbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10sbj") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_235sbj2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.03)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.02)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.016)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.016), Show("random_speed", min_speed=0.016, max_speed=0.03)]  style "textbutton_choice" 
    
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_235sbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_235sbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10sbj") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_235sbj3_:
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_235sbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_235sbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10sbj") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
image ch10_235sbj1_:
    function ch10_235sbj1_
image ch10_235sbj2_:
    function ch10_235sbj2_

label ch10_235sbj1_:
    if anim_speed == 0.25:
        $ anim_speed = 0.02
    elif anim_speed == 0.5:
        $ anim_speed = 0.03
    elif anim_speed == 0.15:
        $ anim_speed = 0.016
    scene ch10_235sbj1_
    call screen ch10_235sbj1_  
label ch10_235sbj2_:
    if anim_speed == 0.25:
        $ anim_speed = 0.02
    elif anim_speed == 0.5:
        $ anim_speed = 0.03
    elif anim_speed == 0.15:
        $ anim_speed = 0.016
    scene ch10_235sbj2_
    call screen ch10_235sbj2_  
label ch10_235sbj3_:
    if anim_speed == 0.2:
        $ anim_speed = 0.25
    elif anim_speed == 0.03:
        $ anim_speed = 0.5
    elif anim_speed == 0.016:
        $ anim_speed = 0.15
    else:
        $ anim_speed = 0.25
    show ch10_237anim with dissolve
    call screen ch10_235sbj3_  


label afterch10_235sbj1_:
    $ hide_anim_speed()
    $ disable_even_frames()
    $ clear_audiofx()
    $ anim_speed = 0.02
    scene ch10_235sbj1_
    mc "{i}{size=-3}Uh, that feels so good..."
    mc "(I can feel her tongue circling the edge of my tip... it feels amazing.)" with dissolve
    pause
    mc "*Hmm* {i}{size=-3} You really like sucking just the tip, huh?"
    s "*Chup, shlp* {i}{size=-3}Yehh, I li’ke it..."
    pause
    scene ch10_235sbj2_
    mc "The girls were talking about going shopping or something. Are you going with them?"
    s "*Chup, chup* {i}{size=-3}Yesh, I wan’na buy clothez for the date."
    mc "The date?"
    mc "Ah, right... you mean the fair."
    s "*Slurp, suck* {i}{size=-3}Wan’na look pretty..."
    mc "You wanna look pretty for me?"
    s "*Slurp* {i}{size=-3}Yesh..."
    $ anim_speed = 0.25
    image ch10_237anim:
        "ch10_237_1" with Dissolve(0.1)
        anim_speed
        "ch10_237_2" with Dissolve(0.1)
        anim_speed
        "ch10_237_3" with Dissolve(0.1)
        anim_speed
        "ch10_237_4" with Dissolve(0.1)
        anim_speed
        repeat
    #scene ch10_235
    show ch10_237anim
    mc "I’m sure you’re gonna look gorgeous. No doubt about it."
    pause
    mc "{i}{size=-3}And when we get back... you gonna wanna do sexy stuff again?"
    s "{i}{size=-3}Yesh, I’ll wanna do sexyy shtuff..."
    mc "{i}{size=-3}But not too late, I don’t wanna mess up my sleep schedule."
    call screen ch10_235sbj3_ with dissolve
label afterch10sbj:
    image ch10_238anim:
        "ch10_238_1" with Dissolve(0.25)
        0.5
        "ch10_238_2" with Dissolve(0.25)
        0.5
        "ch10_238_3" with Dissolve(0.25)
        0.5
        "ch10_238_4" with Dissolve(0.25)
        0.5
        repeat
    show ch10_238anim with dissolve
    pause
    image ch10_239anim:
        "ch10_239_1" with Dissolve(0.25)
        0.6
        "ch10_239_2" with Dissolve(0.25)
        0.6
        "ch10_239_3" with Dissolve(0.25)
        0.6
        "ch10_239_4" with Dissolve(0.25)
        0.6
        repeat
    image ch10_239animslap:
        "ch10_239_2--" with Dissolve(0.25)
        pause 0.25
        "ch10_239_2_-" with Dissolve(0.25)
        1.0
    show ch10_239anim with dissolve
    mc "{i}{size=-3}Let’s not forget this cute round little butt..."
    pause
    show ch10_239animslap with dissolve
    play soundfx "audio/smack1.ogg" 
    pause 0.1
    play voicefx "audio/wavs/s/sbjmoan_4.ogg" volume 2.0 fadein 0.1
    s "*Ah* {w=0.5}{nw}" with hpunch
    hide ch10_239animslap with nothing
    show ch10_239anim with dissolve
    s "*Slurp, chup* {i}{size=-3}You spanked me, *giggle*."
    mc "{i}{size=-3}I couldn’t help it... that little butt is just asking for it."
    show ch10_239animslap with dissolve
    play voicefx2 "audio/smack1.ogg" 
    pause 0.1
    play voicefx "audio/wavs/s/sbjmoan_1.ogg" volume 2.0 fadein 0.1
    s "*Ah* {w=0.5}{nw}" with hpunch
    hide ch10_239animslap with nothing
    show ch10_239anim with dissolve
    pause
    scene ch10_240
    mc "{i}{size=-3}Now I wanna rub it against your cute little ass. I need you to get my dick nice and wet, okay?"
    s "*chup* {i}{size=-3}‘Kay."
    scene ch10_240_1
    mc "{i}{size=-3}Good... stick your tongue out, let it flow..."
    scene ch10_240_2
    mc "{i}{size=-3}You gotta get it soaked so it slides real nice."
    scene ch10_240_3
    s "*Blah*"
    image ch10_240anim:
        "ch10_240_1" with Dissolve(0.5)
        1.0
        "ch10_240_2" with Dissolve(0.5)
        1.0
        "ch10_240_3" with Dissolve(0.5)
        1.0
        repeat
    play sound kissing2 fadein 0.1 loop volume 0.25
    scene ch10_240anim
    s "*Blah* {i}{size=-3}Should I put lots of spit on it?..."
    mc "Yeah, lots... even if it drips everywhere, that’s fine."
    pause
    mc "Uh... that’s good, [s], that’s enough."
    stop voicefx fadeout 0.1
    $ stop_sounds(0.5)
    scene ch10_241saj3_1
    s "{i}{size=-3}Why do you like rubbing it there?"
    mc "{i}{size=-3}Because it feels really good."
    s "{i}{size=-3}Is it ‘cause you imagine you’re having sex with me?"
    scene ch10_141saj1_206_1
    mc "{i}{size=-3}Uhm... {w=0.5}Something like that..."
    $ anim_speed = 0.02
    jump ch10_241bfrsthj








init python:
    def ch10_141saj1_(trans, st, at):
        if store.current_active_animation != "ch10_141saj1_":
            store.current_active_animation = "ch10_141saj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_141saj1_206_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_141saj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 18 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_241saj2_(trans, st, at):
        if store.current_active_animation != "ch10_241saj2_":
            store.current_active_animation = "ch10_241saj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_241saj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_241saj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 18 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_241saj3_(trans, st, at):
        if store.current_active_animation != "ch10_241saj3_":
            store.current_active_animation = "ch10_241saj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_241saj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_241saj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 18 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed


screen ch10_141saj1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.02), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Show("random_speed", min_speed=0.01, max_speed=0.03)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_241saj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_241saj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10afteranim241") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_241saj2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.02), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_anim_speed")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_241saj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_141saj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10afteranim241") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_241saj3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.02), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Hide("random_anim_speed"), SetVariable("anim_speed", 0.01), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_anim_speed")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_241saj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_141saj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch10afteranim241") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
default last_anim = "False"
label ch10_141saj1_:
    $ last_anim = "True"
    scene ch10_141saj1_
    call screen ch10_141saj1_ with dissolve

label ch10_241saj3_:
    $ last_anim = "False"
    scene ch10_241saj3_
    call screen ch10_241saj3_ with dissolve

label ch10_241saj2_:
    $ last_anim = "False"
    scene ch10_241saj2_
    call screen ch10_241saj2_ with dissolve

image ch10_241saj3_:
    function ch10_241saj3_
image ch10_241saj2_:
    function ch10_241saj2_
image ch10_141saj1_:
    function ch10_141saj1_


label ch10_241bfrsthj:
    $ hide_anim_speed()
    show screen random_speed(0.02, 0.03)
    $ anim_speed = 0.02
    scene ch10_141saj1_
    pause
    mc "{i}{size=-3}Mmm... such a pretty little butt..."
    s "*Giggle*{w=0.65}{nw}"
    s "{i}{size=-3}It feels funny..."
    pause
    s "Uh... {i}{size=-3}but I like it too."
    scene ch10_241saj2_
    pause
    s "[mc]."
    mc "Yeah?"
    s "{i}{size=-3}Are we ever going to have real sex?"
    mc "{i}{size=-3}Uh... sex?"
    pause
    s "{i}{size=-3}I wonder what it feels like..."
    s "{i}{size=-3}If you wanna do it, uhm... we could try, if you want..."
    mc "{i}{size=-3}I'm okay... I like doing this."
    s "{i}{size=-3}Why don’t you want to?"
    mc "{i}{size=-3}It’s not that I don’t want to, but..."
    mc "{i}{size=-3}What if it hurts?"
    s "{i}{size=-3}Does sex hurt?"
    mc "{i}{size=-3}They say the first time it does."
    s "{i}{size=-3}Why?"
    mc "{i}{size=-3}The body has to get used to it."
    scene ch10_241saj3_
    pause
    s "{i}{size=-3}Even if you go really slow?"
    mc "{i}{size=-3}Some people say it didn’t hurt, but..."
    s "{i}{size=-3}I’m really curious, [mc]..."
    pause
    s "{i}{size=-3}Can you just put it in... a little?"
    mc "{i}{size=-3}[s]..."
    mc "{i}{size=-3}Your first time should be really special, with a person your age that you really like."
    s "{i}{size=-3}Why?"
    mc "{i}{size=-3}Well, because... {w=0.5}that’s how it should be."
    mc "{i}{size=-3}You only lose your virginity once."
    s "{i}{size=-3}I have virginity?"
    mc "{i}{size=-3}Being a virgin means you’ve never had sex with anyone."
    s "{i}{size=-3}Oh."
    mc "{i}{size=-3}Besides, we shouldn't do that, you're my [srelat], remember?"
    s "{i}{size=-3}Would that be really bad?"
    mc "{i}{size=-3}Uhm... yeah, I-I think so..."
    s "{i}{size=-3}To me, you’re the most special person there is."
    mc "{i}{size=-3}Aww. And you’re the most special girl to me."
    show screen random_speed(0.01, 0.013)
    $ renpy.pause(0.75, hard=True)
    s "*Huh, hm*..."
    pause
    s "{i}{size=-3}But you do it with [k]..."
    mc "*huh* {i}{size=-3}Have you seen us?"
    s "{i}{size=-3}No, but -*huh*{w=0.5}, I’m sure you do."
    s "{i}{size=-3}The other day I heard weird noises coming from [k]’s room, and you were in there with her."
    mc "{i}{size=-3}We weren’t doing anything, we were... {w=0.5}arguing, like always."
    s "{i}{size=-3}Liar..."
    pause
    s "{i}{size=-3}Did you take [k]’s virginity?"
    mc "{i}{size=-3}I don’t think so. {w=0.5}I-I mean..."
    s "{i}{size=-3}Hmm..."
    s "{i}{size=-3}Do you think the other guy who took [k]’s virginity was more special than you?"
    mc "{i}{size=-3}I don’t know..."
    s "{i}{size=-3}I don’t think so. That’s why she doesn’t have a boyfriend anymore. She realized you’re better."
    mc "{i}{size=-3}You think so?"
    s "{i}{size=-3}Yeah."
    pause
    mc "{i}{size=-3}You’re such a sweet girl, you know that?"
    s "{i}{size=-3}If you say so..."
    mc "{i}{size=-3}Well, you are. You’re my favorite. My beautiful little princess."
    s "{i}{size=-3}{i}Hmm... {/i}thanks."
    $ hide_anim_speed()
    call screen ch10_241saj3_ with dissolve
label ch10afteranim241:
    if last_anim == "False":
        scene ch10_141saj1_
    $ hide_anim_speed()
    mc "*Uh* {i}{size=-3}I-it’s coming..."
    s "*Huh* {i}The cum?"
    mc "Yeah, *hmngh!*..."
    pause
    scene ch10_240_5 with flash
    mc "*Hmng*"
    scene ch10_242 with cumming
    mc "*Ah*..."
    scene ch10_241
    pause
    mc "Uh..."
    s "My shirt..."
    mc "Phew...  "
    k "[s], we’re leaving!"
    s "{i}T-they're calling me!"
    s "{size=+10}I’m coooming!"
    mc "{i}Let me clean you up first."
    scene ch10_243 with fade
    s "Bye, love you!"
    mc "Love you too."
    scene ch10_244
    s "I love you more!"
    pause
    mc "(I did it again... and I don’t even feel bad. Not a bit.)" with dissolve
    mc "(I actually feel happy.)" with dissolve
    pause
    mc "(Maybe... {w=0.5}maybe I’m starting to really like [s]...)" with dissolve
    pause
label ch10_243afss:
    stop music fadeout 1.0
    scene blackscreen with dissolve
    $ renpy.end_replay()
    pause
    play music scene2 fadein 1.0
    scene ch10_mcgym with Dissolve(1.0)
    mc "*Hngh!* Twelve!"
    mc "*Hmph!* One more..."
    mc "*Ngh* Nope."
    scene ch10_mcgym-
    mc "(I needed this, I hadn’t worked out all week.)" with dissolve
    mc "(I wonder what my [arelat] [a] is doing?)" with dissolve
    mc "(Might be a good idea to go check on her...)" with dissolve
    pause
    scene ch10_245
    pause
    d "[a], I’m glad you came with us to the beach yesterday."
    d "It was a good day, well... except for the end, heh."
    d "Opening that bottle was a bad idea."
    mc "(Looks like they’re chatting...)" with dissolve
    d "It was a gift from [k]’s friend, we didn’t want to be rude."
    d "It’s good for us to go out as a family more often, don’t you think?"
    d "Especially now that I’ve taken this mini vacation."
    d "I’ll be back in three or four weeks... {w=0.5}It was hard to get these days off, but I managed."
    d "I want us to be together, like the family we are!"
    d "Hehe... erm..."
    a "Sounds good to me."
    d "Yeah..."
    d "What are you doing?"
    a "I’m going to clean, erm...{w=0.5} the oven."
    a "I’m a little busy, so..."
    d "Are you cooking something good today?"
    a "Maybe."
    d "Oh, okay."
    pause
    d "Well then..."
    scene ch10_246
    d "I guess I’ll stop bothering you, dear. Uhm, I’m gonna... watch some football."
    scene ch10_247
    d "Hey, [mc], I think we overdid it yesterday."
    mc "Yeah, we drank a lot."
    scene ch10_248
    pause 0.65
    d "{i}{size=-3}Oh my god..." #said touching his forehead with both hands 
    scene ch10_249
    pause
    mc "Something wrong?"
    scene ch10_250
    d "N-no, well..."
    d "Nah, just this damn headache I can’t shake."
    mc "You should take some ibuprofen."
    scene ch10_249
    d "Yeah..."
    scene ch10_250
    d "Hey, [mc]."
    d "How’s life treating you?"
    mc "Good. And you?"
    d "You know, {i}{size=-5}bad with my family...{/i} but everything else is alright, heh."
    pause
    d "Man, I’m craving a beer, might help this damn hangover."
    d "Wanna have one in the patio?"
    mc "Uh, sure, why not."
    scene ch10_251- with fade
    d "You guys really did a good job with all this."
    d "Was it your idea or [a]’s?"
    mc "It was [arelat] [a]’s idea. I just helped set it all up."
    scene ch10_252
    d "[mc], this looks really well done."
    mc "I watched a few videos on how to set it all up."
    d "Glad you’re not wasting your time. Learning this kind of stuff is useful."
    pause
    scene ch10_253
    d "So, how’s the girlfriend?"
    mc "Girlfriend? Uhm...{w=0.5} not great, I don’t have one."
    d "You don’t sound too sure about that."
    scene ch10_254
    d "Haha, sounds like we’re in the same boat when it comes to love."
    mc "Why do you say that?"
    d "Come on, don’t play dumb. I saw you two at the beach."
    mc "Ah, I think I know what you mean."
    d "Yeah."
    pause
    scene ch10_253
    d "That girl, [mia], she has a boyfriend, doesn’t she?"
    mc "Y-yeah..."
    pause
    mc "Not much to say, love’s complicated."
    scene ch10_254
    d "Haha, ain’t that the truth!"
    pause
    scene ch10_253
    pause 0.5
    scene ch10_255
    d "I really like here."
    scene ch10_256
    d "Hey, that grill."
    d "I bought it, but we hardly ever use it. It’s just sitting there rusting."
    d "I think there’s charcoal in the garage... {w=0.5}Wanna grill something?"
    mc "Sure."
    scene ch10_254
    d "I’ll grab the meat. Be right back."
    scene blackscreen 
    pause 0.5
    scene ch10_251 with fade
    d "Things are wild nowadays. You just open one of those dating apps and boom."
    d "Back then, it was a lot harder."
    mc "It has downsides too. Sometimes the girl doesn’t even look like her picture."
    mc "And sometimes... it’s not even a girl."
    d "Ha! Don’t tell me that actually happened to you!"
    mc "No, but I’ve heard stories, haha."
    scene ch10_257
    d "Here, wave this so the coals catch."
    mc "Back then it was letters, right?"
    scene ch10_258
    d "Letters, my ass. We had to hustle."
    d "You had to show up, be confident, impress the girls face to face."
    d "Those were the days... Wish I could be your age again."
    scene ch10_259
    d "That’s why I say, enjoy life. You can leave love for later."
    d "This girl, [mia]... I don’t see her as someone to get serious with."
    scene ch10_258
    d "You’re young. You’ve got plenty of time to mess up."
    scene ch10_260
    d "*Cough, cough...* What did you put in there, [mc]?"
    mc "A piece of cardboard, like you said. *Cough, cough*"
    d "That’s plastic, [mc]. *Cough* Help me move this thing, way too much smoke."
    stop music fadeout 0.7
label ch10a3:
    scene blackscreen
    pause 0.7
    play music scene1 fadein 0.5
    scene ch10_261
    a "Is something burning?"
    d "No, love, it’s just a barbecue attempt. We’re grilling some burgers too."
    a "I thought the place was on fire, are you grilling meat or tires?"
    d "We had a little mishap earlier."
    d "Come on, give it a try."
    a "No, I..."
    d "[mc] and I made it together."
    mc "We need an opinion."
    d "Give her that one over there, it’s cooked well."
    scene ch10_262
    pause
    scene ch10_263
    pause
    a "This is the one that was cooked well?"
    mc "Why do you ask? Is it raw?"
    a "It’s... {w=0.5}fine."
    d "Score?"
    a "I’d give it... a seven?"
    scene ch10_264
    mc "What?"
    a "It’s raw on the inside and burned on the outside."
    mc "Think you could do better?"
    a "Is that a serious question?"
    mc "Is it really that bad?"
    a "Give me that..."
    scene ch10_265
    a "Did you put barbecue sauce on the chicken?"
    d "Uh, yeah... y-yeah, you can do that, right?"
    d "We just wanted something to go with the beers."
    a "Of course you can."
    d "Heh, watch and learn from the pro, [mc]."
    scene ch10_266
    d "Now this is a barbecue."
    pause
    "..."
    pause
    d "We were just talking about how love and relationships used to be way harder."
    d "Kids today have it easy."
    d "Now there are even long-distance relationships. Back in our day, that was a real issue."
    d "Letters took days to arrive, right honey?"
    scene ch10_267
    a "You never sent me any letters, [d]..."
    d "I know, love... I’m just talking about how things used to be."
    a "And there were phones too, we’re not that old."
    d "R-right, that’s why I didn’t send you letters, hehe..."
    d "But they weren’t like today’s. That’s what I meant."
    pause
    mc "Technology evolves, [drelat] [d]. Worry when everything gets harder instead."
    scene ch10_266
    d "Yeah, yeah, you’re right about that."
    scene ch10_268
    pause
    a "Give me some space, honey, or that meat’s gonna burn."
    scene ch10_269
    pause
    mc "..."
    a "So... why were you two talking about that anyway?"
    d "About what, relationships?"
    a "Yes."
    scene ch10_270
    d "Oh, no reason, dear. [mc] and I were just chatting."
    d "I was giving him some love advice."
    a "You?"
    scene ch10_271
    d "Erm..."
    pause
    "..."
    pause
    d "I’ll go get the plates. Be right back..."
    scene ch10_272
    pause
    mc "That looks good."
    a "Don’t start."
    scene ch10_275
    mc "What?"
    a "{i}{size=-3}Every time I’m cooking, you do the same thing. You start praising the food and then...{w=0.5} praising other things."
    scene ch10_272
    mc "Guess I’m getting too predictable."
    a "*Giggle*{w=0.5}{nw}"
    pause
    a "So? Do you have a girlfriend and didn’t tell me?"
    scene ch10_274
    mc "Girlfriend? N-no."
    a "Weren’t you two just talking about that a minute ago?"
    scene ch10_276
    d "Hehe, [mc]’s not a little boy anymore, love. We have to face it, this bird’s ready to fly."
    mc "I don’t wanna fly. I wanna stay in the nest."
    d "Haha! We’ll see about that!"
    a "One plate, please."
    d "Me first! Hehe."
    scene ch10_277
    d "Mmm... now this is something else!"
    pause
    scene ch10_278
    d "Uhmm, delicious."
    pause
    a "So... is it true about the girlfriend or not?"
    scene ch10_275
    mc "No, [drelat] [d] was just messing around."
    a "..."
    a "{i}{size=-3}Is she at least cute?"
    mc "No, I don't-..."
    scene ch10_280
    mc "..."
    pause
    mc "{i}{size=-3}I mean, yeah... yeah, she’s pretty."
    a "{i}{size=-3}Oh... really?"
    scene ch10_278
    mc "{i}{size=-3}Yeah... and she's really sexy too."
    scene ch10_279
    pause
    scene ch10_280_1 #mc starts touching her butt discreetly, making sure Davie doesn’t see.
    mc "{i}{size=-3}She’s got an amazing body and a face that damn, I melt just thinking about her."
    scene ch10_280_2
    pause 0.75
    scene ch10_280_2-
    pause 1.0
    scene ch10_280_2
    a "Oh..."
    image ch10_280anim:
        "ch10_280_2" with Dissolve(0.5)
        1.5
        "ch10_280_1" with Dissolve(0.5)
        1.5
        repeat
    mc "Her name’s Jessica."
    a "Huh?"
    scene ch10_275
    mc "{i}{size=-5}Just kidding. I don’t have a girlfriend."
    a "{i}{size=-3}You’re such a liar."
    scene ch10_278
    mc "(I’m already turned on...)" with dissolve
    mc "(What the hell’s wrong with me? I can’t be horny all day...)" with dissolve
    mc "(But look at that ass...)" with dissolve
    scene ch10_279
    mc "([drelat!cl] [d] is still focused on his food...)" with dissolve
    pause
    scene ch10_279_1
    pause
    scene ch10_279_2
    pause
    a "..."
    image ch10_279anim:
        "ch10_279_2" with Dissolve(0.5)
        1.5
        "ch10_279_1" with Dissolve(0.5)
        1.5
        repeat
    scene ch10_279anim
    pause
    a "Do you want your burger medium or well done?"
    mc "Medium is well done."
    a "I don’t get how you can like meat like that..."
    mc "That’s when it tastes best."
    mc "(When she just lets me touch her like this without saying anything... it really turns me on like crazy.)" with dissolve
    image ch10_279nim2:
        "ch10_279_3" with Dissolve(0.5)
        1.5
        "ch10_279_4" with Dissolve(0.5)
        1.5
        "ch10_279_3" with Dissolve(0.5)
        1.5
        "ch10_279_4" with Dissolve(0.5)
        1.5
        "ch10_279_3" with Dissolve(0.5)
        1.5

        "ch10_279_2" with Dissolve(0.5)
        1.5
        "ch10_279_1" with Dissolve(0.5)
        1.5
        "ch10_279_2" with Dissolve(0.5)
        1.5
        "ch10_279_1" with Dissolve(0.5)
        1.5
        "ch10_279_2" with Dissolve(0.5)
        1.5
        repeat
    scene ch10_279nim2
    a "Ew, no thanks. But I’ll cook it like you... {w=0.5}-however you prefer it."
    a "To each their own."
    d "Hmm. [mc]’s right, love."
    scene ch10_279
    d "Meat should be cooked medium. Anything else is nonsense."
    a "If you say so."
    scene ch10_279nim2
    pause
    image ch10_280animfp:
        "ch10_280_2" with Dissolve(0.5)
        1.5
        "ch10_280_2-" with Dissolve(0.5)
        1.5
        "ch10_280_2" with Dissolve(0.5)
        1.5
        "ch10_280_2-" with Dissolve(0.5)
        1.5
        "ch10_280_3" with Dissolve(0.5)
        1.5
        "ch10_280_4" with Dissolve(0.5)
        1.5
        "ch10_280_3" with Dissolve(0.5)
        1.5
        "ch10_280_4" with Dissolve(0.5)
        1.5
        "ch10_280_3" with Dissolve(0.5)
        1.5
        "ch10_280_2-" with Dissolve(0.5)
        1.5
        repeat
    scene ch10_280animfp
    d "See, love, medium doneness is the best because it keeps the cut juicy while getting a nice sear on the outside."
    d "That pink you’re seeing doesn’t mean it’s raw, it's just perfectly cooked, and no, it won’t hurt you."
    a "Well, to me it’s still raw."
    scene ch10_280_5
    a "..."
    pause
    scene ch10_280animfp #mc continues squeezing Amelie's butt
    a "{i}{size=-3}No..."
    scene ch10_282
    a "{i}{size=-3}[mc]..."
    scene ch10_281_2
    pause
    scene ch10_281_1
    pause
    scene ch10_281_3
    pause
    scene ch10_281_4
    pause
    image ch10_281_anim:
        "ch10_281_2" with Dissolve(0.35)
        1.5
        "ch10_281_1" with Dissolve(0.35)
        1.5
        "ch10_281_2" with Dissolve(0.35)
        1.5
        "ch10_281_1" with Dissolve(0.35)
        1.5
        "ch10_281_3" with Dissolve(0.35)
        1.5
        "ch10_281_4" with Dissolve(0.35)
        1.5
        "ch10_281_3" with Dissolve(0.35)
        1.5
        "ch10_281_4" with Dissolve(0.35)
        1.5
        "ch10_281_3" with Dissolve(0.35)
        1.5
        repeat

    scene ch10_281_anim
    d "I’ll take my burger medium too, love."
    a "Y-yes."
    a "..."
    pause
    a "{i}{size=-3}Stop it..."
    scene ch10_282
    a "{i}{size=-3}Don’t be silly, your [drelat] is right there."
    scene ch10_284
    pause
    mc "{i}{size=-3}He’s not looking..."
    scene ch10_282
    mc "{i}{size=-3}Come inside with me..."
    a "{i}{size=-3}Just like that?"
    mc "{i}{size=-3}Why not?"
    pause
    mc "{i}{size=-3}[arelat!cl] [a], I can’t resist you..."
    d "How are those burgers coming along?"
    scene ch10_283
    a "A-almost ready, dear."
    a "Medium, right?"
    d "Yes, honey."
    scene ch10_286-
    d "Be right back, I’ll get the lettuce and tomato."
    a "Okay, thanks, honey."
    pause
    d "No problem, love."
    pause
    scene ch10_288
    a "{i}{size=-3}[mc]..."
    mc "Come on, follow me."
    scene ch10_289
    a "{i}{size=-3}W-what? Where?"
    mc "{i}{size=-3}Just come with me..."
    scene ch10_290_1
    a "Oh..."
    mc "{i}{size=-3}I need to touch these tits..."
    scene ch10_290_2
    mc "{i}{size=-3}I need you..."
    scene ch10_290_3
    a "{i}{size=-3}Don’t go crazy, [mc]..."
    image ch10_290anim:
        "ch10_290_1" with Dissolve(0.4)
        1.5
        "ch10_290_2" with Dissolve(0.4)
        1.5
        "ch10_290_3" with Dissolve(0.4)
        1.5
    scene ch10_290anim
    mc "{i}{size=-3}He’ll take a while washing the veggies..."
    a "{i}{size=-3}[mc]..."
    pause
    scene ch10_291_2
    a "{i}{size=-3}This obsession of yours is starting to worry me..."
    scene ch10_291_1
    mc "{i}{size=-3}Mmm, so perfect..."
    scene ch10_291_2
    pause
    scene ch10_292
    a "{i}{size=-3}[mc], seriously, what’s wrong with you?"
    mc "{i}{size=-3}[arelat!cl] [a], what’s wrong is that you’re irresistible."
    scene ch10_294
    a "{i}{size=-3}[mc]..."
    pause
    scene ch10_293_1
    a "{i}{size=-3}The burgers are going to burn."
    scene ch10_293_2
    a "{i}{size=-3}[mc]..."
    scene ch10_293_2-
    pause
    image ch10_293_2-anim:
        "ch10_293_2" with Dissolve(0.3)
        1.75
        "ch10_293_2-" with Dissolve(0.3)
        1.75
        repeat
    scene ch10_293_2-anim
    a "{i}{size=-3}[mc], you’re so clingy..."
    mc "{i}{size=-3}[arelat!cl] [a], are you wet already?"
    a "{i}{size=-3}W-what?.."
    pause
    image ch10_293_3anim:
        "ch10_293_3" with Dissolve(0.3)
        1.75
        "ch10_293_4" with Dissolve(0.3)
        1.75
        repeat
    scene ch10_293_3anim
    pause
    a "{i}{size=-3}Honey, this really isn’t okay."
    pause
    image ch10_293_5anim:
        "ch10_293_5" with Dissolve(0.3)
        1.75
        "ch10_293_6" with Dissolve(0.3)
        1.75
        repeat
    scene ch10_293_5anim
    a "..."
    pause
    scene ch10_293_3anim
    pause
    scene ch10_294
    a "{i}{size=-3}That’s enough!"
    a "{i}{size=-3}I don’t like it when you do that, [mc]."
    a "{i}{size=-3}You’re getting used to touching me whenever you want, and that’s not okay."
    mc "{i}{size=-3}But you like it."
    a "{i}{size=-3}No, I don’t."
    scene ch10_295
    mc "{i}{size=-3}..."
    a "{i}{size=-3}Uhm..."
    pause
    scene ch10_295--
    a "{i}{size=-3}That’s not..."
    a "..."
    pause
    play sound kissing fadein 0.1 loop volume 0.5 
    play soundfx kissing2 fadein 0.1 loop volume 0.15 
    scene ch10_296
    a "*Mch*"
    scene ch10_297
    a "*Hm* {i}{size=-3}[mc]..."
    image ch10_296anim:
        "ch10_296" with Dissolve(0.3)
        1.75
        "ch10_297" with Dissolve(0.3)
        1.75
        repeat
    scene ch10_296anim
    a "*Hmm, smch*"
    pause
    $ stop_sounds(0.5)
    scene ch10_299
    a "{i}{size=-3}H-hey..."
    scene ch10_298
    
    scene ch10_299-
    mc "{i}{size=-3}[arelat!cl] [a], come with me..."
    a "{i}{size=-3}Where to?"
    mc "{i}{size=-3}Somewhere we won’t be seen..."
    play sound kissing volume 0.05 loop
    play soundfx kissing2 volume 0.1 loop
    stop music fadeout 1.5
    play music sexy1 fadein 1.5
    scene ch10_304_2
    a "*Hmm, mch* {i}{size=-3}No..."
    scene ch10_304_1
    a "*Mhh* {i}{size=-3}[mc]... *mch*"
    image ch10_304_1anim:
        "ch10_304_2" with Dissolve(0.3)
        1.5
        "ch10_304_1" with Dissolve(0.3)
        1.5
        repeat
    scene ch10_304_1anim
    a "{i}{size=-3}[mc], your [drelat]... *hm*"
    mc "{i}{size=-3}Let’s go inside..."
    a "{i}{size=-3}We can’t, we’re supposed to be watching the meat... *smoch*"
    mc "{i}{size=-3}I’ve got a better piece of meat right here for you to watch..."
    pause
    image ch10_303_1anim:
        "ch10_303_1" with Dissolve(0.3)
        2.0
        "ch10_303_2" with Dissolve(0.3)
        0.75
        "ch10_303_1" with Dissolve(0.3)
        1.5
        "ch10_303_2" with Dissolve(0.3)
        1.0
        "ch10_303_1" with Dissolve(0.3)
        2.0
        "ch10_303_2" with Dissolve(0.3)
        0.65
        "ch10_303_1" with Dissolve(0.3)
        0.65
        "ch10_303_2" with Dissolve(0.3)
        0.65
        repeat
    image ch10_301_1anim:
        "ch10_301_1" with Dissolve(0.3)
        2.0
        "ch10_301_2" with Dissolve(0.3)
        0.75
        "ch10_301_1" with Dissolve(0.3)
        1.5
        "ch10_301_2" with Dissolve(0.3)
        1.0
        "ch10_301_1" with Dissolve(0.3)
        2.0
        "ch10_301_2" with Dissolve(0.3)
        0.65
        "ch10_301_1" with Dissolve(0.3)
        0.65
        "ch10_301_2" with Dissolve(0.3)
        0.65
        repeat
    a "*Mch, mualh...* {i}{size=-3}S-stop it, [mc]..." #asking him to stop, but without real resistance, because she likes it.
    pause
    scene ch10_308
    pause
    scene ch10_309
    pause
    stop sound
    stop soundfx
    scene ch10_305
    a "{i}{size=-3}Sweetheart, not now."
    scene ch10_306- with vpunch
    mc "{i}{size=-3}You drive me crazy."
    image ch10_305kiss:
        "ch10_309" with Dissolve(0.3)
        1.0
        "ch10_308" with Dissolve(0.3)
        1.0
        repeat
    scene ch10_305kiss
    a "*Smch, mch* {i}{size=-3}[mc]..."
    play sound kissing volume 0.05 loop
    play soundfx kissing2 volume 0.1 loop
    pause
    scene ch10_304_1anim
    a "*Hmch*{i}{size=-3} I said no, [mc]..."
    pause

    scene ch10_303_1
    a "*Hm, mch*..."
    scene ch10_303_2
    mc "{i}{size=-3}Uh, your body..."
    a "*Hnh*"
    scene ch10_303_1anim
    mc "(I just can’t resist her anymore. I simply can’t.)" with dissolve
    a "*Hmch, Muah...*"
    pause
    scene ch10_301_1
    a "*smch*..."
    pause
    scene ch10_301_2
    a "*Mmh*"
    pause
    scene ch10_301_1anim
    pause
    mc "(This situation really reminds me of my first kiss. It was behind the school building, hiding from the principal...)" with dissolve
    scene ch10_302_3
    mc "(Although this kiss...)" with dissolve
    pause
    scene ch10_302_3s
    a "*Smnch...*"
    mc "(This kiss feels way more special to me.)"
    call screen ch10_302_3s with dissolve
    pause
    


transform transparent_button:
    alpha 0.4
    zoom 0.7
screen ch10_302_1:
    imagebutton:
        idle "right_arrow_idle"         
        hover "right_arrow_hover"  
        action Jump("ch10_302_2")
        xalign 1.0                     
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Squeeze" action Jump("ch10_302_1s") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_2:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_1")
        xalign 0.0
        yalign 1.0
        at transparent_button
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_3")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Squeeze" action Jump("ch10_302_2s") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_3:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_2")
        xalign 0.0
        yalign 1.0
        at transparent_button
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_4")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Squeeze" action Jump("ch10_302_3s") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_4:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_3")
        xalign 0.0
        yalign 1.0
        at transparent_button
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_5")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Squeeze" action Jump("ch10_302_4s") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_5:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_4")
        xalign 0.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Squeeze" action Jump("ch10_302_5s") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_1s:
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_2s")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Soltar" action Jump("ch10_302_1") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_2s:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_1s")
        xalign 0.0
        yalign 1.0
        at transparent_button
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_3s")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Soltar" action Jump("ch10_302_2") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_3s:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_2s")
        xalign 0.0
        yalign 1.0
        at transparent_button
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_4s")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Soltar" action Jump("ch10_302_3") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_4s:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_3s")
        xalign 0.0
        yalign 1.0
        at transparent_button
    imagebutton:
        idle "right_arrow_idle"
        hover "right_arrow_hover"
        action Jump("ch10_302_5s")
        xalign 1.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Soltar" action Jump("ch10_302_4") xalign 0.05 yalign 0.4 style "textbutton_choice"

screen ch10_302_5s:
    imagebutton:
        idle "left_arrow_idle"
        hover "left_arrow_hover"
        action Jump("ch10_302_4s")
        xalign 0.0
        yalign 1.0
        at transparent_button
    textbutton "Continuar" action Jump("afterch10_302s") xalign 0.99 yalign 0.05 style "textbutton_choice"
    textbutton "Soltar" action Jump("ch10_302_5") xalign 0.05 yalign 0.4 style "textbutton_choice"



label ch10_302_1:
    scene ch10_302_1 with Dissolve(0.2)
    call screen ch10_302_1 with dissolve

label ch10_302_2:
    scene ch10_302_2 with Dissolve(0.2)
    call screen ch10_302_2 with dissolve

label ch10_302_3:
    scene ch10_302_3 with Dissolve(0.2)
    call screen ch10_302_3 with dissolve

label ch10_302_4:
    scene ch10_302_4 with Dissolve(0.2)
    call screen ch10_302_4 with dissolve

label ch10_302_5:
    scene ch10_302_5 with Dissolve(0.2)
    call screen ch10_302_5 with dissolve
label ch10_302_1s:
    scene ch10_302_1s with Dissolve(0.2) 
    call screen ch10_302_1s with dissolve

label ch10_302_2s:
    scene ch10_302_2s with Dissolve(0.2)  
    call screen ch10_302_2s with dissolve    

label ch10_302_3s:
    scene ch10_302_3s with Dissolve(0.2)  
    call screen ch10_302_3s with dissolve    

label ch10_302_4s:
    scene ch10_302_4s with Dissolve(0.2)  
    call screen ch10_302_4s with dissolve    

label ch10_302_5s:
    scene ch10_302_5s with Dissolve(0.2)  
    call screen ch10_302_5s with dissolve



label afterch10_302s:
    scene ch10_300
    a "*Mmh, smch*"
    pause
    scene ch10_300_4
    pause
    scene ch10_300_3
    pause
    scene ch10_300_4
    pause
    scene ch10_300_1
    pause
    scene ch10_300_2
    a "*Mlah*"
    image ch10_300ainm:
        "ch10_300_4" with Dissolve(0.3)
        0.75
        "ch10_300_3" with Dissolve(0.3)
        0.75
        "ch10_300_4" with Dissolve(0.3)
        0.75
        
        "ch10_300" with Dissolve(0.3)
        0.75
        "ch10_300_1" with Dissolve(0.3)
        0.75
        "ch10_300_2" with Dissolve(0.3)
        0.75
        "ch10_300_1" with Dissolve(0.3)
        0.75
        "ch10_300_2" with Dissolve(0.3)
        0.75
        repeat
    scene ch10_300ainm
    a "*Smch, mualh*..."
    a "*Smch* {i}{size=-3}If your [drelat] caught us like this..."
    mc "{i}{size=-3}He’d have to open the door first, *hmm*{w=0.5}, we’d hear it..."
    pause
    scene ch10_309
    pause 1.0
    stop sound
    stop soundfx
    scene ch10_306-
    a "{size=-3}W-wait, [mc]..."
    scene ch10_303_5
    mc "{i}{size=-3}[arelat!cl] [a]..."
    scene ch10_303_6
    a "..."
    pause
    scene ch10_303_7
    pause
    scene ch10_303_8
    a "{i}{size=-3}I just went to flip the meat..."
    play sound kissing volume 0.05 loop
    play soundfx kissing2 volume 0.1 loop
    scene ch10_303_9
    a "*Smoch* {i}{size=-3}Sweetheart, not here..."
    pause
    scene ch10_303_1anim
    a "*Mahl, smonch*"
    pause
    scene ch10_305kiss
    a "*Muah, lmch*"
    pause
    scene ch10_310
    pause
    scene ch10_310_2
    mc "*Hmh* {i}{size=-3}Having your body so close to mine feels so good..."
    a "*Smonch* {i}[mc]..."
    scene ch10_310_1
    a "{i}{size=-3}Even after last night, you’re still like this so early in the morning..."
    pause
    image ch10_310anim:
        "ch10_310_2" with Dissolve(0.5)
        1.5
        "ch10_310_1" with Dissolve(0.5)
        1.5
        repeat
    scene ch10_310anim
    a "{i}{size=-3}You’re not taking anything weird, are you? *muah*"
    mc "{i}{size=-3}It’s you... watching you walk is my aphrodisiac."
    a "*smch, lhmm* {i}{size=-3}You say the silliest things, [mc], really..."
    mc "{i}{size=-3}What’s worse is that it’s true."
    a "*Hmch* {i}{size=-3}Stop exaggerating..."
    pause
    scene ch10_311
    stop sound
    stop soundfx
    mc "{i}{size=-3}You call this exaggerating?"
    a "{i}{size=-3}[mc], no..."
    pause
    scene ch10_318_0
    a "..."
    mc "{i}{size=-3}Tell me, [arelat] [a], does this feel like exaggerating to you?"
    a "{i}{size=-3}No..."
    scene ch10_318_0-
    pause
    a "..."
    scene ch10_318_0
    pause 0.5
    scene ch10_317
    a "{i}{size=-3}[mc], you have no shame..."
    mc "{i}{size=-3}Touch it again, [arelat] [a]..."
    scene ch10_317_0
    a "{i}{size=-3}[mc], why does it have to be here and now?"
    mc "{i}{size=-3}[drelat!cl] [d]’s probably still washing the lettuce."
    mc "{i}{size=-3}Just a little..."
    a "{i}{size=-3}Oh, [mc]..."
    a "..."
    scene ch10_318_0
    pause 0.5
    scene ch10_318_0-
    pause
    a "{i}{size=-3}Sweetheart, you can’t get like this just because I’m near you."
    scene ch10_318_1
    pause
    a "{i}{size=-3}You’re hard as a rock..."
    scene ch10_318_2
    pause
    image ch10_318animation:
        "ch10_318_1" with Dissolve(0.3)
        1.5
        "ch10_318_2" with Dissolve(0.3)
        1.5
        repeat
    scene ch10_318animation
    a "{i}{size=-3}Look how swollen it is, my god..."
    a "{i}{size=-3}Poor thing... You really need to stop thinking so much about..."
    mc "{i}{size=-3}About you?"
    image ch10_317_1anim:
        "ch10_317_1" with Dissolve(0.2)
        1.5
        "ch10_317_2" with Dissolve(0.2)
        1.5
        repeat
    scene ch10_317_1anim
    a "{i}{size=-3}Y-you need to work on that, [mc]."
    a "{i}{size=-3}Or I won’t even be able to hug you without this happening."
    mc "{i}{size=-3}I know the solution."
    a "{i}{size=-3}..."
    pause
    a "{i}{size=-3}You know we can’t."
    mc "{i}{size=-3}Yeah... I’m done begging."
    a "{i}{size=-3}W-well, good."
    pause
    mc "{i}{size=-3}Faster, [arelat] [a]..."
    image ch10_316anim:
        "ch10_316_2" with Dissolve(0.2)
        0.35
        "ch10_316_1" with Dissolve(0.2)
        0.35
        repeat
    scene ch10_316anim
    pause
    a "{i}{size=-3}If [d] comes out, you run back inside, got it?"
    mc "{i}{size=-3}Yeah... *Uh*{w=0.5}, that feels good..."
    pause
    mc "{i}{size=-3}It’s these hips, they’re to blame for everything."
    a "{i}{size=-3}Right... everything’s always my fault."
    pause
    a "{i}{size=-3}You’re young and full of hormones. That’s the problem."
    mc "{i}{size=-3}Are you kidding? Your curves could wake the dead."
    a "{i}{size=-3}If you didn’t have those 'reactions,' none of this would happen."
    mc "{i}{size=-3}So what do you suggest, I blindfold myself?"
    a "{i}{size=-3}Maybe we should try that."
    pause
    scene ch10_315_1
    a "{i}{size=-3}[mc], your [drelat] could come back any second..."
    scene ch10_315_2
    mc "{i}{size=-3}But it’s starting to feel so good..."
    image ch10_315anim:
        "ch10_315_1" with Dissolve(0.2)
        0.35
        "ch10_315_2" with Dissolve(0.2)
        0.35
        repeat
    scene ch10_315anim
    a "{i}{size=-3}Making me do something like this here..."
    pause
    a "{i}{size=-3}If [d] comes out, we stopping, got it?"
    mc "*Uh, hmm* {i}{size=-3}Yeah, uh..."
    a "{i}{size=-3}Were you working out?"
    mc "{i}{size=-3}Yeah. Do I smell?"
    a "{i}{size=-3}You do."
    mc "{i}{size=-3}Sorry. I don’t like showering right after working out."
    a "{i}{size=-3}No, no, I like it..."
    pause
    image ch10_314animated:
        "ch10_313" with Dissolve(0.2)
        0.35
        "ch10_314" with Dissolve(0.2)
        0.35
        repeat
    scene ch10_314animated
    mc "{i}{size=-3}You like it?"
    a "{i}{size=-3}I like that you work out..."
    pause
    a "{i}{size=-3}That must be it. The workout got your hormones going or something."
    mc "{i}{size=-3}That could be true too."
    pause
    mc "{i}{size=-3}But you like it too. Don’t deny it."
    a "{i}{size=-3}Like what?"
    mc "{i}{size=-3}This..."
    mc "{i}{size=-3}Doing these things in secret with me..."
    a "..."
    pause
    scene ch10_314-
    mc "{i}{size=-3}I want to feel you too, [arelat] [a]..."
    a "{i}{size=-3}[mc]..."
    pause
    scene ch10_319_5
    mc "{i}{size=-3}So warm..."
    a "{i}{size=-3}[mc]..."
    scene ch10_319_6
    mc "{i}{size=-3}You’re dripping..."
    image ch10_319_5anim:
        "ch10_319_5" with Dissolve(0.3)
        1.0
        "ch10_319_6" with Dissolve(0.3)
        1.0
        repeat
    a "{i}{size=-3}Don’t put them in, [mc]..."
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 2.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 2.0 clockwise circles 1
            repeat
        parallel:
            ease 1.3 zoom 1.005
            ease 1.3 zoom 1.01
            repeat
    scene ch10_319_5anim
    a "*Uh*"
    pause
    a "*Hmh* {i}{size=-3}I told you no, [mc]... you never listen."
    mc "{i}{size=-3}I’m listening, but you’re not telling the truth."
    mc "{i}{size=-3}I know you love this just as much as I do."
    pause
    scene ch10_320_1
    a "{i}{size=-3}We can’t be doing this, [mc]..."
    a "{i}{size=-3}We’re insane..."
    mc "{i}{size=-3}We’re just turned on, [arelat] [a]."
    play sound kissing volume 0.35 loop
    play soundfx kissing2 volume 0.3 loop
    scene ch10_320_2
    a "*Muah*"
    scene ch10_320_3
    a "*Smch*"
    image ch10_320anim:
        "ch10_320_2" with Dissolve(0.3)
        1.25
        "ch10_320_3" with Dissolve(0.3)
        1.25
        repeat
    $ renpy.music.set_audio_filter("voicefx", af.Lowpass(400), replace=True)
    play voicefx amoansoft fadein 1.5 volume 0.5
    scene ch10_320anim
    mc "*Hmh* {i}{size=-3}You and I are the sanest people in this house..."
    stop sound
    stop soundfx 
    $ renpy.music.set_audio_filter("voicefx", None, replace=True)
    play voicefx "audio/character/a/soft/a_moan_soft_2.wav" volume 0.3 fadein 0.2
    scene ch10_320_4
    a "*Hah*..."
    mc "{i}{size=-3}See? I’m right. Your mouth always says no, but it doesn’t mean anything."
    mc "{i}{size=-3}I always know what you really want."
    $ renpy.music.set_audio_filter("voicefx", af.Lowpass(10000), replace=True)
    play voicefx amoansoft volume 0.2 loop
    camera:
        xalign 0.5 yalign 0.5 zoom 1.0
    scene ch10_319_3
    pause
    scene ch10_319_4
    pause
    image ch10_319anim:
        "ch10_319_3" with Dissolve(0.3)
        0.7
        "ch10_319_4" with Dissolve(0.3)
        0.7
        repeat
    scene ch10_319anim
    a "*Uh* {i}{size=-3}Honey, your fingers..."
    mc "{i}{size=-3}Am I being too rough?"
    a "*Uh, hm* {i}{size=-3}N-no..."
    pause
    mc "{i}{size=-3}You like it like this?"
    a "*Hm*.. {i}{size=-3}Yes..."
    image ch10_319_1anim:
        "ch10_319_1" with Dissolve(0.3)
        1.0
        "ch10_319_2" with Dissolve(0.3)
        1.0
        repeat
    a "*Hmm, uh* {i}{size=-3}I’m gonna soak my clothes..."
    mc "{i}{size=-3}You’ll change in a moment..."
    a "*Huh, hmh*"
    pause
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 1.5 counterclockwise circles 1
            around (0.499, 0.5)
            linear 1.5 clockwise circles 1
            repeat
        parallel:
            ease 0.5 zoom 1.005
            ease 0.5 zoom 1.01
            repeat
    scene ch10_319_5anim
    a "*Uh, huh*"
    pause
    a "*Huh* [mc]..."
    scene ch10_320_1
    mc "{i}{size=-3}Tell me..."
    a "{i}{size=-3}When [d] comes back, *huh*...{w=0.5} we’ll go inside..."
    mc "{i}{size=-3}Yeah..."
    $ renpy.music.set_audio_filter("voicefx", af.Lowpass(400), replace=True)
    play voicefx amoansoft fadein 1.5 volume 0.5
    play sound kissing volume 0.3 loop
    play soundfx kissing2 volume 0.25 loop
    scene ch10_320anim
    a "*Hm, muah*..."
    pause
    d "How are those burgers coming along?"
    stop soundfx
    stop sound
    stop voicefx
    stop voice
    camera:
        ease 0.1 xalign 0.5 yalign 0.5 zoom 1.0
    $ renpy.music.set_audio_filter("voicefx", None, replace=True)
    scene ch10_320_5 with hpunch
    d "What the hell!? They left the meat unattended."
    d "{size=+3}Honey, why’d you leave the grill!?"
    d "[mc], is that you? What are you doing over there?"
    mc "(Shit, he saw me.)" with dissolve
    mc "Erm... w-we were cleaning up."
    if _in_replay:
        scene blackscreen
        pause 0.5
        $ renpy.end_replay()
    scene ch10_321
    d "Cleaning what!? Look what happened to the meat!"
    scene ch10_322
    mc "We were cleaning the hallway because... {w=0.5} uhm... {w=0.5} we wanted to move the grill."
    scene ch10_323-
    pause 0.5
    mc "Ouh..."
    d "Those were the last burgers, there’s no more. *cough*"
    d "Where did your [arelat] [a] go?"
    scene ch10_324
    mc "S-she's..."
    mc "She went to the bathroom..."
    d "Alright, come help me move this before the smoke gets inside the house."
    stop music fadeout 1.5
    scene blackscreen 
    pause
    play music scene2 fadein 1.5
    scene ch10_325
    d "Yeah, this spot’s good."
    d "I’m going to get more meat. You keep fanning the coals."
    mc "Sure."
    scene ch10_326
    pause
    scene ch10_327
    mc "(That was close.)" with dissolve
    mc "(It was really stupid to do that… There was no need to take such a risk.)" with dissolve
    mc "(But even so, [a] was very responsive... If [drelat] [d] had taken just a little longer, who knows how far we would’ve gone.)" with dissolve
    pause
    scene ch10_328
    mc "(I’m hard again...)" with dissolve
    mc "(What’s [arelat] [a] doing? She said we should go back inside once [drelat] [d] got here...)" with dissolve
    scene ch10_329
    mc "(Shit, the coals are dying down.)" with dissolve
    pause
    d "All I found were these cheap steaks your [arelat] [a] picked up at the supermarket."
    scene ch10_330
    mc "Yeah, uh..."
    pause
    scene ch10_324-
    d "Damn, I forgot the potatoes."
    d "[mc], go grab some potatoes and aluminum from the kitchen."
    scene ch10_331
    d "And butter. Potatoes without butter just don’t hit the same."
    pause
    d "[mc]."
    scene ch10_324-
    mc "[drelat!cl] [d], I need to use the bathroom real quick."
    d "Go on, son. I’ll take care of this."
    mc "Thanks."
    stop music fadeout 1.5
    scene blackscreen
    pause
    scene ch10_332
    pause
    scene ch10_333
    pause
label ch10a4:
    play music sexy2 fadein 1.5
    scene ch10_335 #Amelie looking out the window, like she’s waiting for mc.
    mc "Looking for someone?"
    a "[mc], you scared me."
    scene ch10_336
    a "Uh, {i}[mc]..."
    mc "You said once [drelat] [d] came back, we’d go inside."
    mc "I’m here now, [arelat] [a]."
    mc "Were you waiting for me?"
    a "{i}Uh..."
    play sound kissing volume 0.5 loop
    play soundfx kissing2 volume 0.3 loop
    scene ch10_338
    a "*Uh, hmm*"
    scene ch10_339
    a "*Smch*"
    image ch10_338anim:
        "ch10_338" with Dissolve(0.5)
        1.0
        "ch10_339" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_338anim
    pause
    stop soundfx
    stop sound
    scene ch10_337
    a "{i}Wait, did you just leave your [drelat] out there?"
    mc "{i}I told him I was going to the bathroom."
    a "{i}And what if he comes looking for you?"
    mc "{i}It’s fine. I locked the door."
    play sound kissing volume 0.5 loop
    play soundfx kissing2 volume 0.3 loop
    scene ch10_338anim 
    mc "*Hmch* {i}[drelat] [d] made me help him move the grill. There was way too much smoke."
    mc "{i}The burgers got burned."
    a "*Uhm, smch*..."
    pause
    scene ch10_340
    pause
    scene ch10_341
    a "*Muahl*"
    scene ch10_342
    pause
    scene ch10_343
    pause
    scene ch10_340
    a "*Hmm*"
    scene ch10_341
    pause
    scene ch10_344
    a "*Hmch*"
    scene ch10_344-
    pause
    image ch10_344anim:
        "ch10_344" with dissolve
        0.7
        "ch10_344-" with dissolve
        0.7
        "ch10_344" with dissolve
        0.7
        "ch10_344-" with dissolve
        0.7

        "ch10_340" with dissolve
        0.7
        "ch10_341" with dissolve
        0.7    
        "ch10_342" with dissolve
        0.7     
        "ch10_343" with dissolve
        0.7        
        "ch10_340" with dissolve
        0.7
        "ch10_341" with dissolve
        0.7
        "ch10_342" with dissolve
        0.7  

        "ch10_344" with dissolve
        0.7
        "ch10_344-" with dissolve
        0.7
        "ch10_344" with dissolve
        0.7
        "ch10_344-" with dissolve
        0.7

        "ch10_341" with dissolve
        0.7    
        "ch10_342" with dissolve
        0.7     
        "ch10_343" with dissolve
        0.7

        repeat
    scene ch10_344anim
    a "*Hmnh, muah*..."
    mc "*Uhm, mh* {i}[arelat!cl] [a]..."
    mc "*Hmh* {i}Did you wait long?"
    a "*Hmch* {i}{size=-3}N-no, not really... *hmh*"
    scene ch10_337
    stop sound
    stop soundfx
    a "{i}Did the meat really burn?"
    mc "{i}Yeah, it turned to charcoal."
    scene ch10_345
    pause
    mc "{i}Let’s move away from here."
    a "{i}[mc], he could’ve seen us..."
    scene ch10_347
    mc "{i}You can’t really see from there."
    mc "{i}[arelat!cl] [a], I’ve spent all morning thinking about your bare breasts..."
    pause
    scene ch10_346
    mc "{i}Can I?"
    a "{i}If you want to..."
    pause
    scene ch10_347
    $ renpy.pause(1.0, hard=True)
    scene ch10_347-
    mc "{i}God, missed them..."
    a "{i}You saw them yesterday."
    scene ch10_347--
    mc "{i}Hmm..."
    pause
    mc "{i}Yesterday’s kind of blurry in my head."
    a "{i}See? That’s what happens when you drink so much. If you hadn’t, you’d remember clearly."
    mc "{i}I remember a lot from yesterday... You were so sexy."
    scene ch10_348
    mc "{i}The only thing I don’t remember is how it all started."
    play soundfx kissing2 volume 0.3 loop
    scene ch10_349
    mc "*Chup* {i}You were helping me shower and suddenly you were kissing me, then giving me a blowjob..."
    image ch10_349anim:
        "ch10_348" with dissolve
        1.0
        "ch10_349" with dissolve
        1.0
        repeat
    play sound kissing2 volume 0.2 loop
    scene ch10_349anim
    mc "{i}Was I being too pushy?"
    a "*Hm* {i}Pushy how, sweetheart?"
    mc "{i}I mean... doing all that."
    mc "{i}Both of us naked, showering... and I was drunk..."
    mc "{i}I must’ve been annoying."
    pause
    a "{i}N-no, no... It just... kinda happened, like it always does..."
    scene ch10_350
    mc "*Hmh* {i}Uh, I love your tits..."
    scene ch10_351
    a "*Uh*"
    image ch10_350anim:
        "ch10_350" with dissolve
        1.0
        "ch10_351" with dissolve
        1.0
        repeat
    scene ch10_350anim
    mc "*Hmm* {i}This is bringing back even more memories from yesterday..."
    a "*Uh*..."
    pause
    $ stop_sounds(0.5)
    scene ch10_352
    mc "{i}Now I’m going for the main course."
    a "{i}Honey, you really need to stop comparing me to food."
    scene ch10_353
    mc "{i}Why? Eating is the greatest pleasure of all."
    scene ch10_354-
    mc "Oh... {i}[arelat] [a], you look so delicious..."
    pause
    mc "{i}You’re so wet..."
    a "{i}Well, after all those kisses and touches..."
    scene ch10_352
    mc "{i}If just a little teasing gets you like this, it only makes me think how unsatisfied you are..."
    mc "{i}Let’s make love, [arelat] [a]..."
    a "{i}[mc]..."
    pause
    a "{i}Y-you better finish what you started..."
    mc "{i}As you wish."
    jump ch10_400rsm



init python:
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1
    
    def ch10_355acn0_(trans, st, at):
        if store.current_active_animation != "ch10_355acn0_":
            store.current_active_animation = "ch10_355acn0_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_355acn4_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_355acn1_(trans, st, at):
        if store.current_active_animation != "ch10_355acn1_":
            store.current_active_animation = "ch10_355acn1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_355acn1_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_355acn2_(trans, st, at):
        if store.current_active_animation != "ch10_355acn2_":
            store.current_active_animation = "ch10_355acn2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_355acn5_{}".format(store.frame_num))
        return store.anim_speed
init python:
    def reset_animation_counters():
        for anim_name in anim_frame_counters:
            anim_frame_counters[anim_name] = 1



screen ch10_355acn0_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.045), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.025), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.012), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", min_speed=0.015, max_speed=0.045)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_355acn2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_355acn1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_355") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_355acn1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.05), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.02), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", min_speed=0.02, max_speed=0.05)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_355acn2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_355acn0_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_355") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_355acn2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.045), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.025), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.012), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", min_speed=0.015, max_speed=0.045)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_355acn1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_355acn0_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_355") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 

image ch10_355acn0_:
    function ch10_355acn0_
image ch10_355acn1_:
    function ch10_355acn1_
image ch10_355acn2_:
    function ch10_355acn2_

label ch10_355acn0_:
    $ last_anim = "False"
    scene ch10_355acn0_
    call screen ch10_355acn0_ with dissolve
label ch10_355acn1_:
    $ disable_even_frames()
    $ hide_anim_speed()
    $ last_anim = "False"
    $ hide_anim_speed
    $ anim_speed = 0.025
    scene ch10_355acn1_
    call screen ch10_355acn1_ with dissolve
label ch10_355acn2_:
    $ last_anim = "True"
    scene ch10_355acn2_
    call screen ch10_355acn2_ with dissolve

label ch10_400rsm:
    pause 0.1
    $ hide_anim_speed()
    show screen random_speed(0.025, 0.045)
    play voicefx2 amoansoft volume 0.35 loop
    play soundfx3 kissing2 volume 0.2 loop
    scene ch10_355acn1_
    a "*hmm...*" #oral sex scene, mc to amelie
    mc "*Hm, hmf* {i}Delicious..."
    a "*Uh, huh* {i}Uh, sweetheart, what’s gotten into you today? You’ve been... desperate."
    mc "*Smch* {i}What we did out in the patio was so hot."
    a "{i}That was so irresponsible... *Uh, uh*"
    a "{i}[mc], you’ve been chasing me around all morning..."
    mc "{i}This is how it should be, [arelat] [a]."
    mc "{i}From now on, what’ll be weird is if I don’t."
    a "{i}You're my [arelatmc]... -*huh*{w=0.5} you shouldn’t be like that..."
    mc "{i}It can’t be that bad if we both enjoy it."
    a "{i}T-that’s not right... {w=0.5}You should resist it, not go looking for it..."
    pause
    scene ch10_355acn0_
    pause
    mc "{i}[arelat!cl] [a], do you like it like this?"
    mc "{i}I’m really focusing on your clit this time, your body’s reacting differently."
    a "*Uh* {i}Yes, honey..."
    a "{i}It feels amazing... *huh*"
    mc "I have this feeling you come harder when I give it more attention."
    a "*Hm, ah..* {i}Why do you want that..?"
    mc "{i}I like knowing I left you completely satisfied."
    a "*Uh..* {i}I always make a mess, sweetie..."
    mc "{i}That’s what I like the most. Seeing you lose control turns me on even more. When you squirt it's just, {i}wow..."
    a "*Huh, uh, hm* {i}{size=-3}Oh, [mc]... you’re nothing like your-..."
    pause

    scene ch10_355acn2_
    show screen random_speed(0.02, 0.02)
    a "*Hah, uh* Uh, [mc]..."
    mc "{i}[arelat!cl] [a], m-my hair."
    a "*Huh, uuhm* {size=-3}{i}Oh my god..."
    mc "*hm* {i}Wouldn’t you rather lie down in bed?"
    a "*Uh* {i}N-no... {size=-3}from here I can see if your [drelat] is still there. {/i}*uh*"
    pause
    call screen ch10_355acn2_ with dissolve


label afterch10_355:
    show screen random_speed(0.011, 0.012)
    if last_anim == "False":
        scene ch10_355acn2_
    a "{i}[mc]... to think you like me this much..."
    a "*Uh, mh* {i}My handsome, charming [arelatmc]... *uh, huh*"
    d "The meat’s almost ready!"
    $ stop_sounds(0.5)
    scene ch10_356
    d "Honey!"
    mc "{i}Is he talking to you?"
    scene ch10_357
    a "W-what?"
    d "Is something wrong, honey?"
    d "You left and all the meat got burned."
    d "Even [mc] didn’t realize, said you had him cleaning the hallway or something."
    scene ch10_358
    a "Uh! I'm okay, dear! -I..."
    a "I went to answer a call, honey. You know WhatsUpp never works well from there."
    d "Yeah, happens to me too."
    scene ch10_359
    a "Did all the meat really burn? Want me to get more?"
    d "Yes, love. But don’t worry, there was more in the fridge."
    scene ch10_360
    a "{i}{size=-3}[mc]..."
    d "I’ve got company data on my plan, I'll get you a data plan too, so you don’t have to keep worrying about paying it every time."
    a "Thank you, dear."
    scene ch10_358-
    mc "..."
    pause
    scene ch10_358--
    a "{i}{size=-3}Your [drelat] [d] is waiting for us."
    mc "{i}He can wait a little longer..."
    mc "{i}It’s fine, it’s not like he’s gonna come looking for us."
    a "{i}[mc], what..."
    scene ch10_360
    a "{i}[mc], he’s going to see you..."
    mc "{i}It's fine."
    mc "{i}Look, he’s back at the grill again."
    scene ch10_361
    a "{i}Are you sure he can’t see you?"
    mc "{i}Yeah."
    a "{i}Just don’t lean out too far."
    mc "{i}He won’t see me, I promise."
    scene ch10_362
    pause
    mc "{i}{size=-3}Uh, [arelat] [a], standing like that, hmm..."
    mc "{i}Wouldn’t you rather go to the bed?"
    a "{i}[mc], if your [drelat] decides to come inside, we won’t even notice."
    mc "{i}Why would he suspect anything? I just came here to have a little chat with my [arelat]..."
    scene ch10_363
    a "{i}Well, yeah, th-that’s true but..."
    a "{i}Still..."
    mc "{i}So... you wanna keep going like this?"
    a "If you really can’t help yourself..."
    mc "{i}Obviously I can’t..."
    scene ch10_364
    mc "{i}[arelat!cl] [a], you’re soaking wet."
    mc "{i}Your juices are dripping down your legs..."
    mc "{i}It’s almost slipping in on its own..."
    scene ch10_365
    a "{i}Not inside..."
    mc "{i}Just the tip..."
    a "{i}No..."
    mc "{i}All this teasing... it’s almost painful for me..."
    scene ch10_366
    a "{i}We’ve talked about this so many times already."
    a "{i}A-and you always end up enjoying it anyway."
    $ hide_anim_speed()
    play soundfx3 "audio/slaps/slap_8.ogg" volume 0.5 
    scene ch10_367 with hpunch
    a "Uh!...{w=1.0}{nw}"
    mc "Hnmh... Of course I end up enjoying it."
    jump afterch10_367

init python:
    def ch10_366athj2_(trans, st, at):
        if store.current_active_animation != "ch10_366athj2_":
            store.current_active_animation = "ch10_366athj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_366athj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_366athj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 34 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_366athj1_(trans, st, at):
        if store.current_active_animation != "ch10_366athj1_":
            store.current_active_animation = "ch10_366athj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_366athj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_366athj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 34 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_366athj3_(trans, st, at):
        if store.current_active_animation != "ch10_366athj3_":
            store.current_active_animation = "ch10_366athj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_366athj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_366athj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 34 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
image ch10_366athj2_:
    function ch10_366athj2_

image ch10_366athj1_:
    function ch10_366athj1_


image ch10_366athj3_:
    function ch10_366athj3_
    
screen scrollable_ch10_366athj1_():
    default ypos = 0.0
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        yinitial 1.0
        add "ch10_366athj1_"

screen scrollable_ch10_366athj1_2():
    default ypos = 0.0
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        yinitial 1.0
        add "ch10_366athj1_"


screen ch10_366athj2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", max_speed=0.009, min_speed=0.03)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_366athj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_366athj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("affterch10_366") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_366athj3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", max_speed=0.009, min_speed=0.03)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_366athj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_366athj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("affterch10_366") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_366athj1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.015), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.009), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", max_speed=0.009, min_speed=0.03)] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_366athj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_366athj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("affterch10_366") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action Hide("ch10_366athj1_") style "textbutton_choice" 


define ch10_366athj2__ = "False"
define ch10_366athj1__ = "True"
define ch10_366athj3__ = "False"
label ch10_366athj2_:
    $ current_pov = 2
    $ ch10_366athj2__ = "True"
    $ ch10_366athj1__ = "False"
    $ ch10_366athj3__ = "False"
    hide screen scrollable_ch10_366athj1_ with nothing
    hide screen scrollable_ch10_366athj1_2 with nothing
    scene ch10_366athj2_ with nothing
    call screen ch10_366athj2_ 

label ch10_366athj1_:
    $ current_pov = 1
    $ button_visiblech9_95 = False
    hide screen scrollable_ch10_366athj1_ with nothing
    hide screen scrollable_ch10_366athj1_2 with nothing
    scene ch10_366athj1_1 with nothing
    show screen scrollable_ch10_366athj1_2 with nothing
    $ ch10_366athj2__ = "False"
    $ ch10_366athj1__ = "True"
    $ ch10_366athj3__ = "False"
    call screen ch10_366athj1_ 

label ch10_366athj3_:
    $ current_pov = 3
    $ ch10_366athj2__ = "False"
    $ ch10_366athj1__ = "False"
    $ ch10_366athj3__ = "True"
    hide screen scrollable_ch10_366athj1_ with nothing
    hide screen scrollable_ch10_366athj1_2 with nothing
    scene ch10_366athj3_ with nothing
    call screen ch10_366athj3_ 



label afterch10_367:
    $ button_visiblech9_95 = True
    $ hide_anim_speed()
    show screen random_anim_speed_fast with nothing
    $ anim_speed = 0.05
    scene ch10_366athj2_
    $ anim_speed = 0.014
    mc "*Hmn* With how gorgeous you are, it’s impossible not to."
    a "*Oh, uh*..."
    mc "*Hmm* {i}Uh, [arelat] [a]... You're so damn hot..."
    mc "*Uh* {i}My cock glides deliciously between the juices of your pussy..."
    a "*Huh*"
    pause
    mc "{i}Am I being too rough?"
    pause
    mc "{i}[arelat!cl] [a], am I going too hard?"
    a "*Huh* {i}Y-yeah..."
    mc "{i}Let me keep going like this for a bit, it feels amazing..."
    a "{i}O-okay... *huh*{w=0.5}"
    a "*Uh, huh* {i}You can go at whatever pace you want, honey..."
    pause
    play voicefx amoansoft volume 0.2 loop
    scene ch10_366athj3_ with Dissolve(0.5)
    $ anim_speed = 0.014
    pause
    mc "{i}Is [drelat] [d] still there?"
    a "{i}No{w=0.5}, I-I don’t know... *uh*"
    mc "*Hmh* {i}I thought we stayed here to keep an eye on him."
    a "*Huh* {i}Yeah..."
    a "Huh..."
    mc "{i}Do you like it, [arelat] [a]?"
    mc "{i}*Hngh* Am I going too fast? Do you like it like this?"
    a "Yes, baby *hah*{w=0.5}, keep going."
    a "*Huh* Do it however you like..."
    pause
    mc "{i}[arelat!cl] [a], is [drelat] [d] still there?"
    scene ch10_366athj3_1 with nothing
    show screen scrollable_ch10_366athj1_ with Dissolve(0.5)
    a "*{i}What?...{/i} *huh, huh*"
    a "-{i}He’s still there... {w=0.5}looks like he’s on the phone."
    a "{i}I-I had already forgotten...{/i} *huh, uh*"
    mc "{i}Oh yeah... *hmh*"
    mc "{i}Watching your hips bounce against me... *hah*{w=0.5} -you have no idea how much it turns me on seeing them shake like that..."
    a "{i}Oh baby, *huh*..."
    pause
    $ arrow_alpha = 0.0
    $ button_visiblech9_95 = False
    $ ch10_366athj1__ = "False"
    $ ch10_366athj3__ = "False"
    $ ch10_366athj2__ = "True"
    scene ch10_366athj1_1 with nothing
    hide screen scrollable_ch10_366athj1_ 
    scene ch10_366athj2_
    call screen ch10_366athj2_ with dissolve
    jump affterch10_366
    


label affterch10_366:    
     
    $ hide_anim_speed()
    $ anim_speed = 0.013
    hide screen scrollable_ch10_366athj1_ with nothing
    hide screen scrollable_ch10_366athj1_2 with nothing
    if ch10_366athj2__ == "True":
        scene ch10_366athj2_1 with nothing
    if ch10_366athj3__ == "True":
        scene ch10_366athj3_1 with nothing
    if ch10_366athj1__ == "True":
        scene ch10_366athj1_1 with nothing
    show screen scrollable_ch10_366athj1_ with dissolve
    a "*Huh, uhh* {i}A-are you close, honey?"
    mc "{i}Not yet. I want you to finish first..."
    a "*Huh, hmm* {i}You don’t have to, baby, just hurry, please..."
    mc "*Hngh* {i}I’m not gonna leave you hanging."
    mc "(I said that but I don’t know how much longer I can last, I'm so turned on...)" with dissolve
    mc "*Hngh* (I’m about to cum... I need to do something to make her finish before I do.)" with dissolve
    pause
    hide screen scrollable_ch10_366athj1_ with nothing
    scene ch10_370 with vpunch
    stop voicefx fadeout 0.1
    mc "Uhh, [arelat] [a], you’re soaking like a fountain..."
    a "{i}Honey... w-why did you stop? *hm*..."
    mc "I’m gonna make you feel good first. I’m not leaving until you come."
    a "{i}[mc], that’s not necessary..."
    mc "(I have to make her cum so hard she won’t be able to hold back from wanting sex with me...)" with dissolve
    play voicefx "audio/wavs/a/abjmoan_8.ogg" volume 0.2
    scene ch10_372
    a "*Ah*..."
    mc "{i}You’re burning up inside... of course it’s necessary."
    scene ch10_371
    play voicefx "audio/wavs/a/abjmoan_9.ogg" volume 0.2
    a "*Ah, uhmm*..."
    play voicefx amoansoft loop volume 0.2 fadein 1.5
    scene ch10_372animfast
    mc "(I’ve never seen a woman get this wet...)" with dissolve
    a "*Uhm, hmm* {i}Honey, your [drelat]..."
    mc "{i}Shhh, don’t worry. I’ll make it quick..."
    image ch10_372animfast:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        xalign 0.5 yalign 0.5
        parallel:
            "ch10_372" with Dissolve(0.5)
            ease 0.75 xalign 0.5 yalign 0.5 zoom 1.01
            "ch10_371" with Dissolve(0.5)
            ease 0.75 xalign 0.5 yalign 0.5 zoom 1.005
            repeat
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat


init python:
    def ch10_366afngr1_(trans, st, at):
        if store.current_active_animation != "ch10_366afngr1_":
            store.current_active_animation = "ch10_366afngr1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_366afngr1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_366afngr1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed



screen ch10_366afngr1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.03), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.02), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [Function(hide_anim_speed), SetVariable("anim_speed", 0.012), Function(disable_even_frames)]  style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Function(disable_even_frames), Show("random_speed", max_speed=0.012, min_speed=0.03)] style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch10_366afngr1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 


image ch10_366afngr1_:
    function ch10_366afngr1_

label beforech10_366afngr1_1:
    play voicefx amoanmid loop volume 0.2 fadein 1.5
    scene ch10_366afngr1_
    $ anim_speed = 0.025
    a "*Ah, uhh* {i}God, [mc]..." 
    pause
    a "{i}Uh, [mc]... *huh, uh*"
    mc "{i}[arelat!cl] [a], you’re moaning so damn good... I’ve never heard you like this before."
    mc "{i}When I press my fingers right here I can feel how your body reacts... You like it like that?"
    a "*huh, ah* {i}Yes, baby, like that..."
    call screen ch10_366afngr1_ with dissolve

label afterch10_366afngr1_:

    $ anim_speed = 0.015
    a "*Huh, ah* [mc], *ah*..."
    pause
    a "{i}That you know how I like it... *huh*{w=0.5} That a [arelatmc] knows how to please his [arelat]..."
    a "{i}Honey, we’re hopeless... {/i}*hah, hm*"
    mc "{i}Yeah... all we can do is enjoy each other now, [arelat] [a]."
    a "{i}*uh, huh*"
    mc "{i}I’m glad you finally understand me."
    a "{i}*Oh, uhh*... I-I’m close, baby..."
    a "{i}Oh, honey..."
    show screen random_speed(min_speed = 0.01, max_speed = 0.008)
    mc "{i}Do it, [arelat] [a], I wanna see you dripping with pleasure already..."
    a "*Uuh, haah*"
    play voicefx "audio/wavs/a/amoanhard_2.ogg" volume 0.35
    scene ch10_373_1s
    a "*Aah, hmmah!*{w=0.5}{nw}"
    scene ch10_373_1  
    pause 1.0
    scene ch10_373_2s 
    play voicefx "audio/wavs/a/amoanhard_1.ogg" volume 0.35
    pause 0.5
    scene ch10_373_2 
    pause 0.25
    scene ch10_373_2s
    pause 0.5
    scene ch10_373_1s
    pause 0.5
    scene ch10_376_2--_
    pause 0.5
    scene ch10_376_2-_
    pause 0.5
    image ch10_376anim:
        "ch10_376_2--" with Dissolve(0.3)
        0.3
        "ch10_376_2-" with Dissolve(0.3)
        0.3
        "ch10_376_2--" with Dissolve(0.3)
        1.0
        "ch10_376_2-" with Dissolve(0.3)
        0.3
        "ch10_376_2--" with Dissolve(0.3)
        0.3
        "ch10_376_2-" with Dissolve(0.3)
        0.3
        "ch10_376_2-" with Dissolve(0.3)
        0.3
        "ch10_376_2--" with Dissolve(0.3)
        0.3
        "ch10_376_2--" with Dissolve(0.3)
        1.0
        repeat 3
    image ch10_376anim2:
        "ch10_376_2--" with Dissolve(0.3)
        2.0
        "ch10_376_2-" with Dissolve(0.3)
        0.3
        "ch10_376_2--" with Dissolve(0.3)
        0.3
        "ch10_376_2-" with Dissolve(0.3)
        0.3
        "ch10_376_2--" with Dissolve(0.3)
        5.0
        repeat
    scene ch10_376anim
    a "*Huh... hmh*"
    mc "{i}Wow, [arelat] [a]..."
    scene ch10_376anim2
    a "*Huh, uhmm* Oh my God..."
    a "{i}I-I got the carpet wet..."
    pause
    scene ch10_369
    mc "{i}That was insanely sexy..."
    play soundfx3 "audio/slaps/slap_1.ogg" volume 0.4
    scene ch10_368_1 with vpunch
    a "*Uh*"
    image ch10_368_anim:
        "ch10_368_1" with Dissolve(0.2)
        0.3
        "ch10_368_2" with Dissolve(0.2)
        0.3
        "ch10_368_3" with Dissolve(0.2)
        0.3
        "ch10_368_4" with Dissolve(0.2)
        0.3
        repeat
    jump beforescrollable_ch10_368anim
screen scrollable_ch10_368anim():
    default ypos = 0.0
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        yinitial 1.0
        add "ch10_368_anim"

init python:
    def play_bj_sound(sound_file):
        renpy.sound.play(sound_file, channel="sound")  
init python:
    def play_random_bj_sound(trans, st, at):
        sound_files = ["audio/wavs/bj_42.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_48.ogg"]
        random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
        store.last_played_sound2 = random_sound
        renpy.sound.play(random_sound, channel="sound")
        return 0
label beforescrollable_ch10_368anim:    
    show screen scrollable_ch10_368anim
    pause
    mc "Uh..." 
    mc "{i}[arelat!cl] [a], if your goal is to drive me crazy with desire... you're doing it..."
    a "{i}I want you to...{w=0.5} enjoy this time."
    pause
    mc "{i}Hmm, you’re soaking my cock."
    mc "{i}Watching you come like that was -*ngh*{w=0.5}, so damn hot."
    a "{i}How embarrassing... you seeing me like that... {/i}*uh*"
    scene ch10_368_1 with nothing
    hide screen scrollable_ch10_368anim with nothing
    scene ch10_376_3-_-
    mc "N-no, don’t say that, *huh*{w=0.5}, I liked it."
    mc "Seeing you lose control... That turned me on even more..."
    mc "{i}Being able to make such a gorgeous woman climax -*uh*{w=0.5}, it’s a privilege..."
    a "{i}Oh, [mc]... Do you really mean that?"
    mc "{i}I love it. Everything about you drives me crazy, *Huh*..."
    a "{i}Well, if you say you like it, I believe you."
    scene ch10_376_3 with hpunch
    a "*Uh*..."
    mc "[arelat!cl] [a]..."
    mc "[arelat!cl] [a], I want to do it... I want it so bad..."
    mc "*Hmgh* I-I feel like I’m gonna explode if I don’t..."
    a "{i}Do what, [mc]?"
    mc "{i}Fuck you!... {w=0.65}I want to fuck you, [arelat] [a]." with hpunch
    a "{i}[mc], that’s not..."
    mc "{i}Just once, be mine just once."
    a "{i}Stop it, [mc]."
    mc "{i}I can’t take it anymore, I've been holding back for days. You’re driving me insane."
    a "[mc]..."
    mc "{i}Just... *ngh*, just once." with hpunch
    scene ch10_376_3--
    a "{i}[mc], no, stop..."
    mc "{i}This teasing... it’s too much. I can’t hold back anymore..."
    a "{i}I said no, [mc]."
    scene ch10_376_3---
    a "No."
    a "I said no, [mc]..."
    mc "If you don’t want this, then push me away."
    scene ch10_376_3----
    a "No..."
    mc "You want it too. Let’s stop pretending."
    a "{i}You know it’s not about that, [mc]."
    mc "{i}Then what is it about?"
    a "{i}You know, [mc]. It’s not right."
    mc "Let’s go to the bedroom..."
    a "{i}N-no, [mc], calm down."
    mc "You say that, but you’re not stopping me. You’re just giving me the same monologue as always..."
    mc "Do you want me to make the first move? Is that it?"
    scene ch10_376_3--------2
    a "{i}[mc]..."
    mc "{i}If it’s just fear of getting caught, then let’s go somewhere more private..."
    mc "{i}Okay, how about we tell [drelat] [d] we’re just going out to buy some more meat, then sneak off to a motel? Sound good?"
    a "{i}Stop saying nonsense, [mc]..."
    mc "{i}It’s not nonsense. You want it too."
    scene ch10_376_3_-
    mc "{i}I know you want it just as much as I."
    a "{i}[mc]..."
    pause
    scene ch10_376_4-
    mc "{i}[arelat!cl] [a], I’m starting to believe we’ll never actually do it."
    a "{i}I-if that’s still what you’re trying to get..."
    a "{i}T-then you better go. Because it’s not going to happen."
    mc "{i}But [arelat!cl] [a]..."
    pause
    mc "{i}Really?..."
    a "{i}Let me go, [mc]..."
    scene ch10_376_3_-
    a "{i}I said let go of me."
    scene ch10_376_4---4 with hpunch
    mc "Whoa!"
    scene ch10_376_5- with vpunch
    a "I-I’m sorry, honey. I didn’t mean to push you that hard."
    scene ch10_376_6 with cumming
    mc "I’m not a kid anymore, [arelat] [a]..." with dissolve
    a "{i}You’re just embarrassed ‘cause your friends are around, is that it?"
    scene ch10_376_5- with flash
    pause 0.1
    scene ch10_376_6-
    pause
    mc "S-sorry...{w=1.0} I don’t know what came over me."
    a "Don’t worry, honey. -I know..."
    scene ch10_376_7
    mc "I better head back before [drelat] [d] gets suspicious."
    a "..."
    pause
    scene ch10_376_8
    a "[mc]... {w=1.0}it wasn’t that big a deal, okay?"
    a "You just had a weak moment, that’s all."
    mc "Yeah... I guess."
    a "..."
    pause
    mc "Alright... I’m going now."
    a "W-wait..."
    scene ch10_376_9
    a "Honey, I know it seems absurd after everything we’ve already done..."
    a "It’s just... I’m sorry, [mc]. I just can’t."
    a "I’ll use my mouth. You like that too, right?"
    mc "..."
    scene ch10_380_1
    pause
    a "Are you upset?"
    mc "No. It was just the frustration in the moment. I’m fine."
    scene ch10_380_2
    pause 0.6
    play soundfx3 "audio/mouth/kiss_01.ogg" volume 0.25
    pause 0.05
    scene ch10_380_1
    a "I know how frustrating it is. I understand."
    scene ch10_380_2
    pause 0.6
    play soundfx3 "audio/mouth/kiss_02.ogg" volume 0.2
    pause 0.05
    scene ch10_380_1
    mc "Are we really never going to do it?"
    mc "What needs to happen?"
    a "[mc]..."
    image ch10_380anin:
        "ch10_380_2" with dissolve
        2.0
        "ch10_380_1" with dissolve
        3.0
        "ch10_380_2" with dissolve
        1.0
        "ch10_380_1" with dissolve
        2.0
        "ch10_380_2" with dissolve
        0.75
        "ch10_380_1" with dissolve
        3.0
        "ch10_380_2" with dissolve
        0.75
        "ch10_380_1" with dissolve
        2.0
        repeat
    scene ch10_380anin
    a "{i}I’m going to make sure you enjoy this, okay?" 
    $ clear_audiofx()
    scene ch10_378 
    play sound "audio/wavs/bj_42.ogg" volume 1.0
    mc "Uh..."
    scene ch10_379
    play sound "audio/wavs/bj_44.ogg" volume 1.0
    a "*Smch*"
    scene ch10_379-
    play sound "audio/wavs/bj_46.ogg" volume 1.0
    pause
    scene ch10_380
    play sound "audio/wavs/bj_48.ogg" volume 1.0
    pause
    scene ch10_380-
    play sound "audio/wavs/bj_50.ogg" volume 1.0
    pause
    image ch10_379_bg_animation:
        "ch10_379" with Dissolve(0.3)
        pause 0.7
        "ch10_379-" with Dissolve(0.3)
        pause 0.7
        "ch10_380" with Dissolve(0.3)
        pause 0.7
        "ch10_380-" with Dissolve(0.3)
        pause 0.7
        repeat
    scene ch10_379_bg_animation
    play soundfx kissing2 volume 0.7 loop
    mc "Uh, wow..."
    a "{i}{size=-3}You ga’e me sho mush p’leash’re jush’ now... {/i}{/size}*mschup*"
    a "*Chup, shluph* {i}{size=-3}I’sh m’ doody to... *mmh*... re’tur’ the fav’r..."
    a "{i}{size=-3}I d’t wan-u to be mad at me..."
    mc "{i}I-I’m not mad, huh..."
    mc "{i}Just a little frustrated, but it’s gone now..."
    a "*Smch, smonch* {i}{size=-3}Thas’ good, shweetie... I cou’n’ bear it if you were..."
    show ch10_376_6-- with cumming
    a "[mc], why didn’t you tell me it was bleeding?"
    mc "I didn’t want to scare you, [arelat] [a]..."
    hide ch10_376_6-- with flash 
    pause
    mc "{i}(Damn... what a way to suck me off...)" with dissolve
    mc "{i}(She’s massaging my tip with her tongue in such a clumsy and lewd way...)" with dissolve
    mc "{i}(To think my [arelat] [a] would be capable of) {/i}-*uh*{w=0.5} (something like this...)" with dissolve
    pause
    mc "{i}I could never be mad at you, [arelat] [a]."
    mc "{i}You’ve always been so good to me... more than I deserve."
    a "*Shlrp, smoch* {i}{size=-3}And I alw’ys will be."
    a "*chup, shlrp* {i}{size=-3}B’cuz I’m your [arelat]..."
    pause
    stop soundfx fadeout 0.1
    scene ch10_380anin
    a "{i}Sweetie, your [drelat]..."
    scene ch10_379_bg_animation
    play soundfx kissing2 volume 0.7 loop
    pause 1.0
    image ch10_380window:
        "ch10_380--" with Dissolve(0.25)
        1.0
        "ch10_380---" with Dissolve(0.25)
        1.0
        repeat
    scene ch10_380window
    pause 0.5
    mc "He’s still there, grilling the meat."
    a "*Muah, smch* {i}He mush’ be waitin’ for ush... we nee’ t’ hurry up..."
    scene ch10_380---- 
    pause 0.5
    camera:
        ease 0.5 zoom 1.1 xalign 0.0 yalign 0.5
    mc "(Shit!)" with dissolve
    pause 0.5
    camera:
        ease 2.0 zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_380-----
    pause 0.5
    mc "{i}{size=-3}Hey..."
    pause 0.5
    a "*slush, sluph* {i}{size=-3}What’sh wrong?"
    scene ch10_381 with Dissolve(0.5)
    $ stop_sounds(0.5)
    mc "N-nothing. Let’s move over here instead."
    scene ch10_382
    a "{i}Keep watching, [mc]."
    mc "I can still see him from here."
    $ hide_anim_speed()
    $ disable_even_frames()
    $ anim_speed = 0.02
    scene ch10_383
    pause 0.5
    a "You’re throbbing..."
    mc "Yeah..."
    a "You must be close... {w=0.5}I’m gonna suck a little more, okay?"
    a "You... {w=0.5}just enjoy it, okay?"
    mc "Oh I will..."
    a "G-good..."
    scene ch10_378asd1_
    a "*Slurp, slurp*"
    mc "{i}[arelat!cl] [a]... {w=0.5}Uh..."
    mc "{i}Uh, [arelat] [a], I’m gonna cum real soon if you keep sucking me like this..."
    a "{i}Hmm... *Slurp, shlrp*"
    mc "(She’s putting so much effort into this blowjob...)" with dissolve   
    mc "(She’s caressing and exploring my glans with her tongue...)" with dissolve
    mc "(This is her way of making it up to me for not letting me fuck her...)" with dissolve
    mc "(Fucking her? Impossible. But a blowjob this lewd? -no problem!)" with dissolve
    mc "(I won’t pressure her anymore for now. She always gives me long, amazing blowjobs most girls wouldn’t...)" with dissolve
    pause
    a "{i}Hmmm..."
    a "{i}Hmm-hm... *slurp, slurp*"
    mc "{i}Oh, [arelat] [a], it feels incredible..."
    scene ch10_378asd2_
    pause
    a "*Chup, slurp* {i}{size=-3}Hmm... Your [drelat]..."
    a "*Slorp, shlurp* {i}{size=-3}What’sh your [drelat] doing now?..."
    mc "{i}Looks like he’s talking on the phone. He hasn’t moved from there."
    pause 0.5
    $ anim_speed = 0.015
    mc "Uh..."
    a "*shlurp, schup* {i}{size=-3}D-Don’ hol’ back... huneh... c-cum for me shweethea'..."
    mc "{i}Uh, almost there... {w=0.5}Just keep sucking me like that, [arelat] [a], uh..."
    a "*Slurp, chup, slfsh*"
    $ hide_anim_speed()
    scene ch10_378asd3_ as bg
    pause
    mc "{i}Oh, yeah..."
    a "{i}*Gugh, gugh*"
    mc "(At first I was guiding her head, but now she’s going deeper all on her own...)" with dissolve
    mc "{i}Uh, [arelat] [a], your blowjobs are the best..."
    $ hide_anim_speed()
    $ ch10_3781p = 3
    a "*Slurp, gug* {i}{size=-3}Hmm-hn..."
    call screen ch10_378asd3_ with dissolve

    
    







    








init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1

    def ch10_378asd1_(trans, st, at):
        if store.current_active_animation != "ch10_378asd1_":
            store.current_active_animation = "ch10_378asd1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_378asd1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_378asd1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.015:
                    if random_chance < 0.3:
                        final_volume = max(0.1, 0.1 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                elif anim_speed <= 0.015:
                    if random_chance < 0.8:
                        final_volume = max(0.1, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"
                ]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.8 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_378asd2_(trans, st, at):
        if store.current_active_animation != "ch10_378asd2_":
            store.current_active_animation = "ch10_378asd2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_378asd2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_378asd2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.015:
                    if random_chance < 0.3:
                        final_volume = max(0.1, 0.1 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                elif anim_speed <= 0.015:
                    if random_chance < 0.8:
                        final_volume = max(0.1, 0.4 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"
                ]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_378asd3_(trans, st, at):
        if store.current_active_animation != "ch10_378asd3_":
            store.current_active_animation = "ch10_378asd3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_378asd3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_378asd3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.015:
                    if random_chance < 0.3:
                        final_volume = max(0.1, 0.1 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                elif anim_speed <= 0.015:
                    if random_chance < 0.8:
                        final_volume = max(0.1, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                        store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"
                ]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.8 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value
screen ch10_378asd1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.035), Function(hide_anim_speed)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", min_speed=0.015, max_speed=0.04)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_378asd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_378asd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_378asdcont"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_378asd2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.035), Function(hide_anim_speed)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", min_speed=0.015, max_speed=0.04)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_378asd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_378asd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_378asdcont"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_378asd3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.035), Function(hide_anim_speed)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", min_speed=0.015, max_speed=0.04)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_378asd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_378asd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_378asdcont"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 

default ch10_3781p = 0


label ch10_378asd1_:
    $ ch10_3781p = 1
    scene ch10_378asd1_ as bg
    call screen ch10_378asd1_ with dissolve
label ch10_378asd2_:
    $ ch10_3781p = 2
    scene ch10_378asd2_ as bg
    call screen ch10_378asd2_ with dissolve
label ch10_378asd3_:
    $ ch10_3781p = 3
    scene ch10_378asd3_ as bg
    call screen ch10_378asd3_ with dissolve





image ch10_378asd1_:
    function ch10_378asd1_
image ch10_378asd2_:
    function ch10_378asd2_
image ch10_378asd3_:
    function ch10_378asd3_





label ch10_378asdcont:   
    pause 0.5
    show screen random_speed(0.013, 0.015)
    mc "Uh, a-almost..."
    show screen random_speed(0.01, 0.013)
    pause 0.5
    mc "*Uh, hmm*..." 
    $ hide_anim_speed()
    $ anim_speed = 0.011
    if ch10_3781p != 1:
        scene ch10_378asd1_ at Shake((0.5, 1.0, 0.5, 1.0), 9999.0, dist=3) with dissolve
    else:
        show bg at Shake((0.5, 1.0, 0.5, 1.0), 9999.0, dist=3) with dissolve
    mc "Oh..."
    mc "{i}Hah, hmmh...{w=0.5} [persistent.Amrelation[0].upper()]-[arelat] [a]..." 
    a "*Gug, gug, slurp!*"
    mc "*Hmnh!*"
    mc "*Ghah* I'm cumming..."
    scene ch10_383 at Shake((0.5, 1.0, 0.5, 1.0), 9999.0, dist=3) with dissolve
    hide ch10_378asd1_ with nothing
    mc "*Hmmngh!* {i}I'm cumming!!..." 
    scene ch10_384 at Shake((0.5, 1.0, 0.5, 1.0), 9999.0, dist=3) with dissolve
    a "Ah..."
    scene ch10_385
    pause 1.0
    scene ch10_386
    pause 0.75
    scene ch10_387-
    mc "Uh...{w=0.5}{nw}"
    scene ch10_388-
    pause 0.75
    scene ch10_389-
    mc "Hah...{w=0.5}{nw}"
    scene ch10_389--
    pause
    mc "Phew, uh..."
    a "{i}{size=-2}-Uh..."
    pause
    a "Oh, [mc]..."
    mc "Uh... I came a lot."
    scene ch10_389-----a
    pause 0.75
    a "{i}You really did..."
    a "{i}A-alright..."
    a "Now go back to your [drelat], I’ll wash my face and come down with you, okay?"
    mc "Yeah..."
    mc "Thanks, [arelat] [a], really."
    a "You’re welcome..."
    scene ch10_390____
    mc "Phew... Alright, I’m heading out."
    a "{i}Wait, can you bring me a tissue? I-I can’t see anything..."
    stop music fadeout 2.0
    scene blackscreen with Dissolve(1.5)
    $ renpy.end_replay()
    pause
    play music scene2 fadein 1.5
    scene ch10_393
    d "Did those tacos mess you up? You were in the bathroom for a while."
    mc "I-I’m not sure... Yeah maybe they did."
    mc "How's the barbecue?"
    d "That crap’s useless. I’ll buy some quality meat later."
    mc "Was it that bad?"
    d "Yeah, it got burned. Damn thing."
    d "It was garbage anyway. When I use good meat, my burgers come out amazing, you'll see."
    scene ch10_391
    s "[drelatks!cl], have you seen a pink wallet by any chance?"
    d "A wallet?"
    d "[s], I thought you were with the girls."
    s "We came back because I forgot the money, heh..."
    d "I haven’t seen any wallet."
    s "[mc], have you seen it?"
    mc "No. Did you check the bathroom? You always leave your phone in there."
    s "Oh, maybe there is."
    d "All that instagran and TikTo is rotting your brains... Do you remember where you were last before you left?"
    s "Ah! I know!"
    scene ch10_393
    d "Hey, what about your [arelat] [a]? Where is she?"
    mc "Uhm..."
    mc "She spilled something on the carpet so she’s cleaning it up."
    d "Oh, alright."
    scene ch10_392
    s "Oh, I almost forgot! [mc], [mia] says she wants to know if you’re coming."
    mc "[mia]?"
    s "Yeah."
    mc "Uh..."
    mc "I’m having a beer with my [drelat] [d]. I’ll join you girls another time, okay?"
    s "Come on..."
    s "[drelatks!cl], can he come with us?"
    d "He should take her out properly some other day."
    s "But we’re going out today."
    d "You are?"
    s "Yeah, [mc] and I are going to the fair."
    d "Oh, no, sweetie. I meant [mc] and [mia]."
    s "Huh?"
    mc "You girls have fun."
    s "Alright then..."
    scene ch10_393
    d "He-heh, as long as the boyfriend doesn’t find out..."
    mc "Yeah..."
    d "If you ever need advice about these ''topics'', don’t hesitate to ask me."
    d "Believe it or not, I used to be really good with women back in the day...{w=0.5}{size=-3}{i} well, I still am, haha."
    mc "Haha, I don’t doubt it, [drelat] [d]."
    mc "Did you ever go out with someone else’s girl?"
    d "If I told you... Ah, those were the days."
    d "But back then, cheating wasn’t as accepted. Usually someone just stole your girlfriend, haha."
    mc "Sounds like you stole a few."
    d "‘Stole’ sounds harsh. I’d say I ‘won’ them. I’ve always been a winner, always."
    d "Don’t tell your [arelat], haha."
    mc "Ha-ha..."
    scene ch10_394
    a "[mc], why don’t you go with the girls?"
    d "Hi, love. Uhm..."
    mc "I'm having a beer with my [drelat] [d]."
    mc "I, uhm... wanted to stay."
    scene ch10_395
    a "You’re not going because you don’t want to, or is there another reason?"
    d "Huh?"
    d "Oh, right, right..."
    d "I had asked your [arelat] [a] not to let you and [k] go out together, as punishment for what happened last time..."
    d "But, well..."
    a "Yeah, I think that’s punishment enough."
    scene ch10_396
    a "I’ve noticed you and [k] barely talk now, this isn’t what we wanted either."
    a "Punishment is one thing, but completely cutting each other off is something else."
    mc "Uhm..."
    mc "N-no, we’re fine."
    d "What I didn’t want was for you two to go out partying, that’s all."
    mc "She hangs out with [mia] more now, that’s why we don’t talk much anymore."
    a "If that’s the case, then alright."
    a "I just worry that you’re always at home, and now that you’re working, you should go unwind a bit with the girls at least, [mc]."
    mc "Uhm..."
    scene ch10_397
    d "Son, could you grab me a beer?"
    mc "Sure."
    stop music fadeout 1.0
    scene blackscreen 
    pause
    scene ch10_398 with dissolve
    play music scene1 fadein 1.0
    mc "(That was weird...)"
    mc "(I’ve got a bad feeling...)" with dissolve
    scene ch10_399
    d "{i}Your [arelat] told me you barely speak to [k], says it’s because of me."
    mc "...{w=0.5} *gulp*..."
    scene ch10_400
    d "Listen..."
    d "Your [arelat] don’t talk to me, and well..."
    d "You’re the only one I’ve really spent time with in this house since I got here."
    d "I don’t want things to get even more tense than they already are."
    d "Just hear me out, [mc], I promise I won’t bring it up again."
    scene ch10_401
    mc "I’m listening, [drelat] [d]."
    d "..."
    pause
    stop music fadeout 2.0
    scene ch10_402 with Dissolve(2.0)
    d "Has anything like that happened again?"
    pause
    mc "L-like what?"
    d "You and [k]."
    mc "(Are you serious?! It’s obvious what he means!)" with dissolve
    mc "Erm..."
    mc "(That look... I feel like he can read my thoughts...)" with dissolve
    mc "(What is this pressure? I can barely breathe...)" with dissolve
    pause
    mc "N-no..."
    mc "Of course not."
    "..."
    pause
    play music scene1 fadein 1.0
    scene ch10_403
    d "Good."
    d "Listen, I don’t want you two to stop talking forever either."
    d "You and [k] going out together is still off the table. No matter what your [arelat] says, you and I both know what really happened."
    d "So go ahead, go with the girls, I've got no problem with it. [a] told them to wait for you."
    d "You’d actually be doing me a favor by going. {i}I’m trying to score points, and this kind of thing helps."
    d "You know, I want peace."
    d "I’d really like to think what happened was just a mistake, and not something I need to worry about happening again when I’m not home."
    d "Because honestly, just remembering it puts me in a really bad mood."
    d "You’re my [drelatmc], [mc]. You’re very important to everyone in this house, and I want you to keep living here as long as you want, got it?"
    mc "Y-yeah, I understand."
    d "You’re a good person. I know you won’t let me down."
    scene ch10_404
    d "Ah, one more thing."
    d "[s] tells me{w=0.5} —EVERYTHING."
    d "Just so you know. That goes for [k] too, not just you."
    mc "... {w=0.5}O-of course."
    d "Have fun."
    pause
    mc "(Did [s] tell him something?)" with dissolve
    mc "(Would she?)" with dissolve
    mc "(No... I don’t think so. He would’ve said something. Actually, he wouldn’t be letting me go with them if she had.)" with dissolve
    mc "(That makes me feel a little better... but damn...)" with dissolve
    mc "(That was terrifying...)" with dissolve
    stop music fadeout 1.0
    scene blackscreen
    pause
    play music scene2 fadein 1.0
    scene ch10_404-
    s "I told [arelatks] to convince [drelatks]."
    mc "Really?"
    s "Uh-huh."
    mc "Thanks, [s]."
    s "[drelatks!cl] wasn’t going to let you come with us, right? That’s why you said you didn’t want to go."
    mc "Something like that."
    scene ch10_405 with fade
    s "Yes I told him!"
    mia "No way."
    scene ch10_406
    s "Right, [mc]?"
    mc "Told him what?"
    s "That [mia] wanted you to come with us."
    mia "And what did he say?"
    s "He accepted."
    mia "But why do I have to be his girlfriend?!"
    k "You already agreed! Just play along."
    scene ch10_405
    s "Yeah, otherwise [drelatks] is going to keep doubting us."
    mc "You’re still on that nonsense?"
    mc "Wait—[s] knows?!"
    scene ch10_406
    s "Yup."
    mia "Mr. [d] already knows I have a boyfriend, I told him myself!"
    k "It’s already been decided. Don’t back out now."
    k "{i}{size=-3}It’s not like you really care, c'mon..."
    mia "Just promise you’re not gonna lose your mind with jealousy."
    k "Jealous? Me?"
    mia "Yes, you!"
    k "Shut up—I won’t."
    scene ch10_407
    mia "Hahaha—{w=0.5}{nw}"
    mia "-Ha..."
    s "Why would she be jealous? You're just his fake girlfriend… or am I missing something?"
    mia "Eh..."
    scene ch10_408
    mia "[mc], your [srelat]..."
    s "W-wait! I left the money in [arelatks]’s room!"
    k "Oh my god..."
label ch10k1:
    if _in_replay:
        play music scene2 fadein 1.0
    stop music fadeout 1.0
    scene blackscreen 
    if _in_replay:
        pause 0.5
    else:
        pause
    play music scene1 fadein 1.0
    scene ch10_409
    mc "(They’ve been here for like an hour and I haven’t seen them try on a single thing...)" with dissolve
    mc "(I should’ve insisted on staying home. Would’ve spared myself the [drelat] [d] threats too...)" with dissolve
    pause
    scene ch10_410 
    s "Which one was the one I liked? Was it this one?"
    mia "Look at this, it’s on sale."
    s "I don’t like the color."
    pause
    scene ch10_411
    mc "Find anything you like?"
    k "Not yet."
    scene ch10_412
    k "Oh, look at that dress!"
    scene ch10_413:
        subpixel True
        yalign 1.0 xalign 0.5
        ease 5 yalign 0.0
        ease 10 zoom 0.75
    k "Uhm... but I’m looking for something more evening-like."
    pause
    scene ch10_419
    mc "Still not finding what you’re looking for?"
    k "[mia]'s the one shopping. I’m just browsing."
    mc "I’ve never seen you walk into a clothing store and walk out empty-handed."
    k "I like this dress, but I already have a bunch like it..."
    mc "This blue one? Take it. I’ll buy it for you."
    scene ch10_414
    k "Nah, are you serious?"
    mc "Yeah, of course. That’s what I work for."
    scene ch10_416 with hpunch
    mc "I like keeping my bitches happy."
    scene ch10_415
    k "You say that like you have any."
    image ch10_415ani:
        "ch10_416" with Dissolve(0.5)
        1.0
        "ch10_415" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_415ani
    pause
    scene ch10_417
    mc "Oh? So you’re not my bitch?"
    scene ch10_418
    k "Are you buying me the dress or not?"
    image ch10_417animm:
        "ch10_417" with Dissolve(0.5)
        1.0
        "ch10_418" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_417animm
    mc "I already told you yes."
    k "Buy me two."
    mc "Alright, I’ll buy you two."
    scene ch10_419
    k "{i}Yes, I’m your bitch..."
    mc "Oh..."
    scene ch10_417animm
    mc "{i}Only two dresses? You’re cheap..."
    k "I’m going to shove both dresses up your ass."
    mc "Whoa, relax, I’m kidding."
    scene ch10_450
    mc "But being my bitch isn’t just about saying you are..."
    scene ch10_451
    k "Stop it, dumbass, there’s the clerk."
    scene ch10_452
    mc "You’re no fun..."
    if stephloving == "True":
        pause
        scene ch10_453
        pause
        scene ch10_454
        pause
        scene ch10_456
        pause
        scene ch10_455
        mc "{i}Say you're my bitch again." 
        scene ch10_456
        s "What?"
        scene ch10_457
        mc "Eh, hey..."
        scene ch10_458
        s "{i}I’m your bitch."
        scene ch10_459
        mc "Oops..."
        s "Why do you want me to say that, huh?"
        scene ch10_460
        mia "Come see this, [s]!"
        s "Coming!"
        scene ch10_461
        s "Is it on sale?"
        mia "Yeah, wow it’s {i}Vouis Luiton."
        pause
    scene ch10_462
    mc "(I’m dying of boredom...)" with dissolve
    mc "(If at least there were men’s clothes, everything here is for women.)" with dissolve
    pause
    scene ch10_463
    mc "(The lingerie section...)" with dissolve
    mc "(Is that a leopard-print bra?)" with dissolve
    scene ch10_464
    mc "(Could be a funny joke for [k]...)" with dissolve
    mc "(Yeah... a joke...)" with dissolve
    mc "(But I need to know her size. She’s got pretty big tits...)" with dissolve
    pause
    scene ch10_420 with fade
    k "You said three dresses, right?"
    mc "I said two."
    mc "Hey, can you turn this way for a second?"
    scene ch10_421
    mc "Hmm, yeah, you’d need a big cup size."
    scene ch10_424
    k "Seriously?"
    mc "Remember you’re my bitch?"
    k "...{w=1.0} That’s it?"
    scene ch10_425
    mc "Yup. That’s all."
    k "{i}H-hey, where are you going?"
    scene ch10_426
    k "{i}That’s it? You’re leaving without doing anything?"
    mc "Uh, what?"
    scene ch10_427 with vpunch
    mc "Ow!"
    mc "H-hey, that’s what they’re for, but you ask first..."
    k "{i}Teasing me and then ignoring me? Are you messing with me?"
    mc "What?"
    scene ch10_429
    k "Walking around the house shirtless, all sweaty... you think I don’t notice?"
    mc "I wasn’t trying to seduce you. I-it’s not my fault I’m this handsome..."
    k "{i}Quit pretending, I know you do it to turn me on!" with vpunch
    scene ch10_430-
    s "What are you doing to [mc]?"
    k "Uh..."
    scene ch10_431
    k "N-nothing, we weren’t doing anything... hehe..."
    s "Are those the jealousy fits they were talking about?"
    k "What?"
    s "Chill out, for god’s sake, plus, the clerk’s a guy."
    k "It’s not like that, I was just...{w=0.5} checking the fit on his pants, that’s all."
    mia "[s], look! This is the dress I told you about!"
    scene ch10_432
    s "Really!?"
    mia "Yeah, come on, I want to see how it looks on you."
    scene ch10_433
    s "I’m watching you..."
    k "Yeah yeah, get going."
    scene ch10_434
    pause
    k "She always shows up at the worst possible time, I don’t know how she does it."
    scene ch10_435
    mc "By the way, what the hell was that?"
    k "Haha, that... I don’t know."
    k "[drelatks!cl] makes it impossible at home. Here I feel a little more free..."
    scene ch10_435--
    mc "Is my favorite bitch all worked up? Is that it?"
    mc "{i}Why didn’t you tell me?"
    k "You don’t seem too interested when we’re at home..."
    mc "I’m scared [drelat] [d] will catch us again."
    k "Yeah... me too."
    $ audio_fade()
    play voicefx2 kissing volume 0.35 loop
    play voicefx3 kissing2 volume 0.3 loop
    scene ch10_435---
    pause
    scene ch10_435----
    pause
    image ch10_435anim:
        "ch10_435---" with dissolve
        1.0
        "ch10_435----" with dissolve
        1.0
        repeat
    scene ch10_435anim
    k "Hm-hmm..."
    pause
    mc "{i}When you’re in the mood, just say the word."
    k "*Smch*{i} You never come looking for me."
    mc "{i}I forgot, you’re a woman. I always have to be the one who makes the move."
    $ stop_sounds()
    play soundfx2 kissing volume 0.1 loop
    play soundfx3 kissing2 volume 0.07 loop
    scene ch10_436-
    k "{i}Idiot... {/i}*hm-smch*"
    k "{i}Today I’m the one coming after you. *smch*"
    scene ch10_436--
    mc "{i}Every chance we get, I try to spend time with you."
    image ch10_437anim:
        "ch10_436-" with Dissolve(0.2)
        1.0
        "ch10_436--"with Dissolve(0.2)
        1.0
        repeat
    scene ch10_437anim
    k "{i}That’s not true..."
    mc "{i}We did it yesterday."
    k "{i}That doesn’t count."
    scene ch10_436---
    mc "{i}Wanna do it now?"
    scene ch10_436----
    k "{i}Where?"
    image ch10_437-anim:
        "ch10_436---" with Dissolve(0.2)
        1.0
        "ch10_436----"with Dissolve(0.2)
        1.0
        repeat
    scene ch10_437-anim
    mc "{i}In the car..."
    k "*smonch, muah* {i}Three dresses..."
    mc "{i}Yeah, as many as you want..."
    k "*Smch, hmm*"
    mc "{i}The clerk’s gonna see us... Let’s go to the car now."
    k "{i}We’re going to [mia]’s place after this..."
    mc "{i}You mean hours from now, after you’re all done shopping?"
    k "{i}Well yeah."
    scene ch10_437
    mc "{i}I can’t wait that long."
    k "{i}Me neither."
    mc "{i}W-wait, here comes the clerk..."
    $ stop_sounds(0.5)
    scene ch10_436
    pause
    mc "{i}So what now? Are we doing the car?"
    k "{i}I think I have a better idea..."
    mc "{i}Oh yeah?"
    scene ch10_435-----
    k "Meet me in the fitting rooms in a bit..."
    if _in_replay:
        scene blackscreen
        pause 0.5
        $ renpy.end_replay()
    pause
    scene ch10_435------:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 30 zoom 1.0 
    pause
    mc "(I just came a couple hours ago from a blowjob from my [arelat] [a], but nothing beats real sex...)"
    mc "(Not to mention [k] is just as gorgeous as her [arelatks]...)" with dissolve
    mc "(She said to meet her in a bit... In the meantime, I’ll buy 'that' so she can try it on right there...)" with dissolve
    scene ch10_463 with fade
    pause
    scene ch10_464
    pause
    scene ch10_465
    mc "(They’re about this size...)" with dissolve
    mc "(Should’ve asked her bra size...)" with dissolve
    scene ch10_466
    mc "(They’re not even gonna fit...)" with dissolve
    mc "(I don’t think these would even fit [s]...)" with dissolve
    pause
    scene ch10_467
    mc "(Is that sleepwear or lingerie?)" with dissolve
    mc "(Probably both.)" with dissolve
    scene ch10_468
    mc "..."
    pause
    mc "(This one might fit her...)" with dissolve
    mc "(Bras stretch, right?)" with dissolve
    scene ch10_469
    mc "(Hmm, maybe it will fit. I think so. Maybe a little tight, but that’d make it even better...)" with dissolve
    mc "(Fuck it, I make money now. I can treat myself.)" with dissolve
    "Need help with something?{w=0.7}{nw}"
    scene ch10_470 with hpunch
    mc "W-woah! Y-yes, {w=0.5}I-I mean, no!"
    "I’m going to have to ask you to leave the store."
    mc "N-no, I... I wasn’t.. I'm not a weirdo."
    scene ch10_471
    mc "I’m just looking for something cute for my girlfriend, but I don’t really know her size."
    "Ah, you should’ve said that. Sorry, I saw what you were doing and thought you were some creep."
    "Tell me what size you need and I’ll help you out."
    mc "Uhm..."
    "Just show me, like, with your hands."
    scene ch10_472
    mc "S-she’s around this size..."
    "Ah... got it."
    "That’s a large cup. Alright."
    scene ch10_473
    "Come with me. I’ve got what you’re looking for over here. Are you looking for lingerie, a bikini, or something themed? Satin, spandex, cotton? We’ve got a bit of everything."
    mc "Uh, yeah..."
    scene blackscreen 
    pause 0.5
    scene ch10_474 with fade
    mc "(That was so embarrassing... I don’t even know what the hell I ended up buying. That guy's really good at selling.)" with dissolve
    $ renpy.pause(hard=False)
    s "How do I look, [mc]?"
    mc "Hm?"
    scene ch10_475_1
    mc "Oh, [s]! I didn’t see you there."
    mc "That dress is beautiful!"
    s "You like it?"
    mc "Yeah, I like it a lot. You look gorgeous."
    scene ch10_475_2
    s "You really like it?"
    mc "Yes, of course! I love how it looks on you."
    s "I’m wearing this one for the date today..."
    s "I also picked out more clothes."
    mc "Really?"
    s "A few sets..."
    s "Wanna see them all?"
    mc "Yeah, show me."
    s "Okay, I’ll be right back."
    pause
    scene ch10_475_----
label ch10_phonemsg:
    call phone_start from _call_phone_startch10
    call reply_message("Hey") from _call_message_startch10_1
    call message("[k]", "Hold on, there are some people in here.") from _call_message_startch10_21
    call message("[k]", "I’ll let you know.") from _call_message_startch10_2315
    call message_img("[k]", "", "images/scenes/ch10/ch10_kpphone.jpg") from _call_message_startch10_8
    call reply_message("😳😳😍") from _call_message_startch10_223
    call phone_end from _call_phone_endch10_a2_ 
    scene ch10_475_3 with vpunch
    s "[mc!cl], do you like this one?"
    mc "Nice pants, I like them."
    scene ch10_475_4
    s "What about this one? Do you like it?"
    mc "I like it a lot."
    scene ch10_475_5
    mc "So cute!"
    scene ch10_475_6
    mc "Beautiful!"
    scene ch10_475_8
    mc "I love it!"
    scene ch10_475_7
    mc "Oh, so formal!"
    s "I wanted to look a little more grown-up, heh..."
    scene ch10_475_9
    mia "And me?"
    s "..."
    mia "What? I’m the girlfriend."
    s "Fake girlfriend!"
    scene ch10_475_10
    s "I’m gonna go try on more clothes."
    mc "Sure, I’ll wait here."
    s "I might take a bit, okay?"
    mc "Yeah, no problem."
label ch10k2:
    if _in_replay:
        play music scene2 fadein 1.0
    scene ch10_475_11
    s "[mia], can you help me pick out more clothes?"
    mia "Of course!"
    mia "Are you coming with us?"
    s "No, I’m going to... I’ve got a thing."
    scene ch10_475_----
    call phone_start from _call_phone_startch101
    call message("[k]", "Come now") from _call_message_startch10_213
    call reply_message("Are we really doing it here?") from _call_message_startch10_22
    call message("[k]", "I want you to see a dress... I need your opinion😛") from _call_message_startch10_2
    call reply_message("On my way") from _call_message_startch10_22321
    call phone_end from _call_phone_endch10_a2_5
    scene blackscreen
    stop music fadeout 1.0
    pause
    scene ch10_475-
    pause
    mc "{i}[k]?"
    pause
    scene ch10_477:
        subpixel True
        xalign 0.5 yalign 1.0
        ease 6 yalign 0.0
    play music sexy1
    k "What do you think of this dress?"
    mc "Oh..."
    mc "I like it.."
    scene ch10_478
    mc "Uh, yeah, I definitely like it."
    mc "Really brings out your..."
    mc "Big tits."
    k "Well, I’ll take the credit."
    mc "More like theirs."
    scene ch10_479
    k "I wanted your opinion, not on how it looks, on the price... It's kinda expensive."
    mc "I’ll buy it. Doesn’t matter."
    scene ch10_480
    k "*Mmh* {i}Wait..."
    scene ch10_481
    k "It’s two hundred."
    mc "{i}I said I don’t care..."
    play soundfx2 kissing volume 0.2 loop fadein 0.5
    play soundfx3 kissing2 volume 0.2 loop fadein 0.5
    scene ch10_482
    k "*Smch* {i}Hmm..."
    scene ch10_483
    mc "{i}Anything for my personal bitch."
    image ch10_483anim:
        "ch10_482" with dissolve
        1.0
        "ch10_483" with dissolve
        1.0
        repeat
    scene ch10_483anim
    k "*Smnch* {i}Hmm... I’ll just take this one."
    mc "{i}You can grab another one if you want."
    k "{i}This is the only one I really liked."
    $ stop_sounds()
    scene ch10_484
    mc "{i}Turn around."
    k "{i}[mc], I heard someone come into the other fitting rooms, let’s not make too much noise."
    scene ch10_484---
    mc "So just this dress?"
    k "{i}Yeah... {w=0.5}-But I want a purse..."
    mc "{i}How much is it?"
    k "{i}Another hundred, okay?"
    scene ch10_484--
    mc "{i}Yeah, sure."
    mc "{i}You’ve got amazing tits."
    k "{i}Guess your paycheck's not too bad, huh?"
    mc "{i}Enough to spoil myself."
    scene ch10_487
    k "{i}Wait, you’re gonna ruin the dress."
    mc "{i}Take it off."
    scene ch10_488
    mc "{i}Take it all off."
    k "{i}Are we seriously doing it here?"
    mc "{i}What do you mean? This was your idea."
    k "{i}I didn’t think you’d actually go for it."
    mc "{i}You chickening out?"
    pause
    k "{i}I want shoes too..."
    k "{i}Kidding! Kidding! Come back here..."
    k "{i}Don’t put it all in..."
    mc "{i}Is my dick too much for you?"
    k "{i}It’s too big, you’ll make me moan..."
    show screen random_speed(0.02, 0.03)
    play voicefx2 kmoansoft volume 0.1 loop
    $ renpy.music.set_audio_filter("voicefx2", af.Lowpass(2000))
    scene ch10_489kf1_
    k "*Huh, huh* {i}Yeah, like that... keep it slow..."
    mc "{i}I love how you moan slowly... you sound like such an adorable little bitch."
    k "{i}*Hah, hah*"
    mc "{i}Uhh, I missed this pussy, oh... you’re squeezing me like crazy..."
    k "{i}Keep buying me cute things and you’ll get more of this."
    mc "{i}I don’t need to buy you anything, you’ll come crawling for my dick anyway."
    mc "{i}You’re already my personal bitch."
    k "{i}Keep saying that and I won’t even let you touch a single hair."
    mc "{i}Alright, alright..."
    mc "{i}I’ll keep buying you nice things, but not because of this."
    k "{i}Then why?"
    mc "{i}Well... because of love."
    k "{i}Love?"
    mc "{i}What?"
    k "{i}You’re pathetic..."
    mc "{i}-Because of the love you have for my dick. It’s amazing how much you enjoy it."
    k "{i}You’re such an idiot..."
    show screen random_speed(0.018, 0.023)
    k "{i}Ah... {/i}*huh, huh*"
    scene ch10_489kf2_
    mc "{i}Would it really be that pathetic if I did it out of love?"
    k "*huh* {i}[mc], don’t make it weird."
    mc "{i}Haha, I’m just messing with you."
    pause
    mc "{i}Hey, different topic, are you going out with [mia] today?"
    k "{i}Yeah, we’re going dancing."
    k "{i}Does it bother you?"
    mc "{i}No, of course not."
    pause
    mc "{i}Would it bother you if I did the same?"
    k "*huh* {i}No, not really."
    pause
    k "{i}Are you sure it doesn’t bother you?"
    mc "{i}Well, I won’t lie, it’d sting a little seeing you with someone else wearing the dress I bought you..."
    k "{i}I’m just going to keep [mia] company."
    k "{i}{size=-3}I think she’s having boyfriend problems. She just doesn’t want to tell me."
    mc "{i}Ah."
    k "{i}I’m going with her and then I’ll come back."
    k "{i}Really."
    mc "{i}Yeah, it’s fine. You can do whatever you want. I don’t mind."
    k "{i}I know."
    k "{i}Same goes for you."
    pause
    scene ch10_489kf3_
    mc "{i}I still think we’d make a great couple."
    k "{i}What? Shut up. Stop saying stuff like that..."
    mc "{i}What? Do I make you feel things?"
    k "{i}It’s weird."
    mc "{i}Well, I think it’s hot..."
    k "*Huh, oh*"
    mc "*Hmh* {i}Damn, [k], you’re sucking me in..."
    k "*Hah, uh*"
    mc "{i}Can I cum inside?"
    k "{i}Today?.. I-I don’t know..."
    mc "{i}I’ll buy you the pills."
    k "{i}..."
    k "{i}F-fine, okay."
    $ anim_speed = 0.014
    show screen random_speed(0.013, 0.018)
    mc "{i}That’s why you’re my favorite bitch."
    pause
    k "{i}*hah, oh, uhm...*"
    mc "{i}Oh..."
    mc "{i}You’re moaning loud."
    k "{i}I-I couldn’t help it..."
    mc "{i}Did you come?"
    k "{i}Yeah..."
    scene ch10_489kf1_
    pause
    mc "(I don’t think even 3 minutes passed, she came fast...)" with dissolve
    mc "(Now I need to hurry and finish too.)" with dissolve
    $ ch10_489pov = 1
    call screen ch10_489kf1_ with dissolve

init python:
    def ch10_489kf1_(trans, st, at):
        if store.current_active_animation != "ch10_489kf1_":
            store.current_active_animation = "ch10_489kf1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_489kf1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_489kf1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.6 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.01, 0.05 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_489kf2_(trans, st, at):
        if store.current_active_animation != "ch10_489kf2_":
            store.current_active_animation = "ch10_489kf2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_489kf2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_489kf2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.01, 0.05 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.2 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_489kf3_(trans, st, at):
        if store.current_active_animation != "ch10_489kf3_":
            store.current_active_animation = "ch10_489kf3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_489kf3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_489kf3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.25 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.01, 0.05 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

screen ch10_489kf1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_489kf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_489kf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10ch10_489kf1_1"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_489kf2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_489kf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_489kf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10ch10_489kf1_1"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_489kf3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_489kf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_489kf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10ch10_489kf1_1"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 

image ch10_489kf1_:
    function ch10_489kf1_
image ch10_489kf2_:
    function ch10_489kf2_
image ch10_489kf3_:
    function ch10_489kf3_
define ch10_489pov = 0
label ch10_489kf1_:
    $ ch10_489pov = 1
    scene ch10_489kf1_
    call screen ch10_489kf1_ with nothing
label ch10_489kf2_:
    $ ch10_489pov = 2
    scene ch10_489kf2_
    call screen ch10_489kf2_ with nothing
label ch10_489kf3_:
    $ ch10_489pov = 3
    scene ch10_489kf3_
    call screen ch10_489kf3_ with nothing

label afterch10ch10_489kf1_1:
    if ch10_489pov != 1:
        scene ch10_489kf1_
    show screen random_speed(min_speed = 0.01, max_speed = 0.009)
    $ anim_speed = 0.01
    mia "[mc]?"
    mia "No, he’s not here."
    k "{i}*hah, hah*{/i} I think they’re looking for you..."
    mc "{i}Yeah, shut up."
    pause
    s "He’s probably in there with [k]..."
    pause 0.5
    camera:
        subpixel True
        ease 0.5 zoom 1.1 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 1.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 1.0 clockwise circles 1
            repeat
        parallel:
            ease 0.5 xalign 0.4
            ease 0.5 xalign 0.5
    pause 0.5
    show ch10_489 with dissolve
    mia "I don’t think so, must be someone else."
    s "I bet you it’s them."
    mia "Nah, you think?"
    scene ch10_489_-- with hpunch
    s "I’m pretty sure!"
    s "..."
    camera:
        ease 0.5 xalign 0.5 yalign 0.5 zoom 1.0
    $ stop_sounds(0.5)
    scene ch10_489_---
    if _in_replay:
        pause
    $ renpy.end_replay()
    k "{i}That little rat!"
    k "{i}And I told her we wouldn’t do it again, now she’s gonna be all over me about it..."
    mc "{i}Shit..."
    k "{i}It’s fine, we’re heading to [mia]’s house after this anyway..."
    mc "{i}And?"
    k "{i}Which means we’ll have more time to..."
    mc "{i}Yes!"
    mc "{i}I mean, yeah, sure..."
    k "{i}I-it’s a nice dress you’re buying me..."
    mc "{i}Yeah, it is."
    pause
    mc "{i}Wait, what are we gonna do about [s]?"
    k "{i}Ugh... I don’t know. Try to keep her happy, I guess?"
    mc "Yeah."
    pause
    scene ch10_491
    mc "{i}So you’ll stay my bitch a little longer. I like that."
    mc "{i}Hm?"
    scene ch10_488
    mc "{i}Haha, are you blushing ‘cause I called you my bitch?"
    k "{i}That was cringe..."
    stop music fadeout 1.0
    scene blackscreen 
    pause
    play music scene1 fadein 1.0
    scene ch10_492
    k "What’s that?"
    mc "Uh, this... {w=0.5}it’s a gift."
    k "Hey, why don’t you buy something for [s] too?"
    mc "Why don’t you go to hell?"
    k "Haha, it’s to make sure she doesn’t tell [drelatks] anything."
    mc "You buy it then."
    k "Ugh, stingy..."
    mc "Don’t worry, I was gonna buy her something anyway. Don’t think you’re that special."
    k "Aww, you’re so sweet..."
    mc "I know."
    stop music fadeout 1.0
    scene blackscreen
    pause 1.0
    play music scene2 fadein 1.0
    scene ch10_475_1- with fade
    mc "Hey..."
    mc "What are you doing?"
    s "Looking at the purses..."
    mc "Oh..."
    pause
    mc "You like any of them?"
    s "Yeah, I like a few."
    mc "Want me to buy you one?"
    scene ch10_475_1--
    s "I don’t want anything."
    mc "Huh?"
    mc "Really?"
    pause
    mc "What about a dress?"
    s "No."
    mc "You sure?"
    s "Yes, I’m sure!"
    mc "Alright!..."
    pause
    mc "We’re going to the fair today."
    mc "You still wanna go? Because I really want to go with you..."
    s "You know the clerk noticed, right?"
    mc "What?"
    s "He was gonna call security."
    mc "Security? Why?!"
    s "{i}{size=-3}''Why?''{/i} Don’t play dumb! you know why."
    s "The clerk heard you doing ''that'' and sent me to tell you to stop or he’d call a guard."
    mc "Uh... really?"
    pause
    mc "And you... came to warn us?"
    pause
    s "Just go already, he might think I’m just like you and [k]."
    mc "Alright, alright..."
    s "..."
    scene ch10_474 with fade
    pause
    s "[mc], are you asleep?"
    scene ch10_475_1--- with fade
    mc "Huh?"
    mc "Are we leaving already?"
    s "I *do* want you to buy me something!" with hpunch
    mc "O-oh... yeah?"
    s "The girls and I want to buy purses..."
    mc "Purses for all of you?"
    s "We’re short a hundred bucks..."
    mc "A hundred?"
    mc "Yeah, it’s fine, I’ll cover it."
    s "A-actually it’s three hundred..."
    s "We’re three hundred short, yeah..."
    mc "T-three hundred?"
    mc "Three hundred..."
    mc "{i}{size=-3}That’s almost half a paycheck..."
    mc "I mean, sure, don’t worry, anything for my little [srelat]."
    scene ch10_475_1----
    s "See? Told you he’d say yes."
    mia "Buying purses for all of us, even me..."
    mc "It’s nothing."
    mia "What are you talking about? Not even my real boyfriend gives me gifts."
    mc "It’s nothing, really."
    scene ch10_475_1-----
    s "B-but you two are fake dating, don’t forget that, okay?"
    mia "I remember, don’t worry."
    "Thanks, and next time go get a motel, alright?"
    k "Huh?..."
    "I’m kidding, but seriously, I’d really appreciate it if you didn’t do that again..."
    mc "S-sorry..."
    "Thanks for shopping here —have a great day..."
    scene ch10_492-
    mia "Let’s go to my house, please. I wanna shower."
    k "Sure... Yeah, whatever you want."
    mc "So, you’re going out later?"
    mia "Yeah, we’re going out partying later."
    s "You’re not going, [mc]."
    s "You and I are going to the fair today..."
    mc "That's right."
    mia "Oof, jealous much?"
    s "Yeah—and?"
    mia "Nothing. At least you’re honest about it, unlike some people..."
    k "[mia], it’s not funny anymore."
    mia "Buzzkill..."
label ch10k3:
    stop music fadeout 2.0
    scene blackscreen
    pause
    play music scene1 fadein 1.0
    scene ch10_493
    s "Nice living room."
    mia "Thanks."
    mia "I’m gonna take a shower."
    scene ch10_494
    s "What’s this? It smells weird..."
    scene ch10_495
    mia "*Ahem!* That’s [dereck]’s, hehe..."
    scene ch10_496
    s "[mia], can I use your bathroom?"
    mia "Of course, I’ll show you where it is."
    pause
    scene ch10_497
    pause
    mc "Come here."
    k "What?"
    mc "Come here, bitch."
    scene ch10_498
    k "Hey, did [drelatks] say anything to you for coming?"
    mc "Funny you ask... you were right."
    scene ch10_499
    k "What happened?"
    scene ch10_500
    mc "Basically, he said he’s tired of worrying that we might... you know, do it again."
    mc "He was really serious about it."
    mc "First we were having a beer and then everything turned dark..."
    scene ch10_506
    k "Right? He’s all chill one second and then just flips like that. It’s so awkward."
    mc "Awkward? I’d say terrifying..."
    scene ch10_505
    k "Yeah, totally."
    mc "And he said [s] tells him *everything*."
    k "Yeah, he told me the same thing."
    k "Don’t worry, she won’t say anything."
    k "[mia] and I will make sure she keeps her mouth shut."
    scene ch10_507
    mc "What? Don’t go putting ideas in her head."
    k "Would you rather say nothing and risk her blurting something out later?"
    k "It’s better to be sure."
    mc "I guess you’ve got a point."
    scene ch10_505
    k "She’s terrified they’ll kick you out of the house again, haha."
    k "So she’ll keep quiet."
    mc "Really?"
    scene ch10_502
    k "Yeah, don’t stress. We just have to avoid pissing her off."
    mc "God help us then."
    k "We’ll be fine."
    image ch10_502anim:
        "ch10_503" with dissolve
        1.5
        "ch10_504" with dissolve
        1.5
        repeat
    play soundfx2 kissing volume 0.2 loop
    play soundfx3 kissing2 volume 0.2 loop
    scene ch10_502anim   
    mc "You sound awfully confident."
    k "*Mch* {i}If it’s about you, she’ll do anything. She’ll keep the secret for sure."
    mc "*smch* {i}If you say so."
    scene ch10_507
    k "At least now you’ve got a job."
    mc "And?"
    k "If you get kicked out, you can live on your own now. *smonch*"
    scene ch10_508
    mc "Yeah, sure..."
    pause
    $ stop_sounds()
    k "By the way..."
    scene ch10_501
    k "[mia] said we could do whatever we want..."
    k "And we’re alone with no one watching..."
    k "We hardly ever get a moment like this at home."
    mc "That's what I was thinking."
    k "[mia] takes forever to get ready... wanna sneak into her room with me?"
    play music sexy2 fadein 0.5
    scene ch10_509 with fade
    k "Take your clothes off."
    mc "This is [mia]’s mom’s room."
    k "Yeah, she’s on a trip."
    mc "I know."
    $ predict_ch10_513kbj1_()
    scene ch10_510
    k "Finally, a real moment alone."
    mc "Yeah..."
    scene ch10_511
    mc "Think we’ve got time for a blowjob?"
    k "[mia] always takes forever to get dressed."
    mc "What about [s]?"
    k "You locked the door."
    mc "Good. Then start sucking, bitch..."
    $ disable_even_frames()
    $ predict_ch10_513kbj2_()
    $ predict_ch10_513kbj3_()
    scene ch10_513kbj1_
    jump afterch10_513kbj1_1



init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1

    def ch10_513kbj3_(trans, st, at):
        if store.current_active_animation != "ch10_513kbj3_":
            store.current_active_animation = "ch10_513kbj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 39 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_513kbj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_513kbj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 6.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 23 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bjgags3.ogg", "audio/wavs/bjgags4.ogg", "audio/wavs/bjgags7.ogg", "audio/wavs/bjgags8.ogg", "audio/wavs/bjgags10.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.35 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 13 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_513kbj1_(trans, st, at):
        if store.current_active_animation != "ch10_513kbj1_":
            store.current_active_animation = "ch10_513kbj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 39 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_513kbj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_513kbj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.01 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_513kbj2_(trans, st, at):
        if store.current_active_animation != "ch10_513kbj2_":
            store.current_active_animation = "ch10_513kbj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 39 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_513kbj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_513kbj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.01 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_513kbj4_(trans, st, at):
        if store.current_active_animation != "ch10_513kbj4_":
            store.current_active_animation = "ch10_513kbj4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_513kbj4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_513kbj4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 8 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 13 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value

init python:
    def predict_ch10_513kbj1_():
        """Predice todos los frames de la animación"""
        for i in range(1, 40):
            renpy.start_predict("ch10_513kbj1_{}".format(i))
init python:
    def predict_ch10_513kbj3_():
        """Predice todos los frames de la animación"""
        for i in range(1, 40):
            renpy.start_predict("ch10_513kbj3_{}".format(i))
init python:
    def predict_ch10_513kbj2_():
        """Predice todos los frames de la animación"""
        for i in range(1, 40):
            renpy.start_predict("ch10_513kbj2_{}".format(i))
init python:
    def predict_ch10_513kbj4_():
        """Predice todos los frames de la animación"""
        for i in range(1, 40):
            renpy.start_predict("ch10_513kbj4_{}".format(i))

screen ch10_513kbj1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.035), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.035), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.3
        xalign 0.99
        textbutton "Shaft" action Jump("ch10_513shaft") style "textbutton_choice"
    hbox:
        yalign 0.15
        xalign 0.99
        textbutton "Deepthroat" action Jump("ch10_513kbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action [SetVariable("anim_speed", anim_speed * 2), Function(hide_anim_speed), Jump("ch10_513kbj4_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_513kbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_513kbj1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_513kbj2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.035), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.035), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action [SetVariable("anim_speed", anim_speed * 2), Function(hide_anim_speed), Jump("ch10_513kbj4_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_513kbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_513kbj1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_513kbj4_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.060), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.024), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.04), Show("random_speed", max_speed=0.024, min_speed=0.060), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action [SetVariable("anim_speed", anim_speed / 2), Function(hide_anim_speed), Jump("ch10_513kbj2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action [SetVariable("anim_speed", anim_speed / 2), Function(hide_anim_speed), Jump("ch10_513kbj1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_513kbj1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_513kbj3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.035), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.035), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.3
        xalign 0.99
        textbutton "Blowjob" action Jump("ch10_513kbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_513kbj1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_513kbjshaft_:
    hbox:
        yalign 0.3
        xalign 0.99
        textbutton "Blowjob" action Jump("ch10_513kbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Function(stop_sounds, 0.5), Jump("afterch10_513kbj1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label ch10_513kbj1_:
    $ ch10_513kbj1 = 1
    scene ch10_513kbj1_ with Dissolve(0.3) 
    call screen ch10_513kbj1_
label ch10_513kbj2_:
    $ ch10_513kbj1 = 2
    scene ch10_513kbj2_ with Dissolve(0.3)   
    call screen ch10_513kbj2_
label ch10_513shaft:
    $ ch10_513kbj1 = 3
    scene ch10_513anima with Dissolve(0.3) 
    call screen ch10_513kbjshaft_
label ch10_513kbj3_:
    $ ch10_513kbj1 = 5
    $ dialogsch10_513 = [
        "Wanna give me some deep throat?",
        "I’m gonna use your throat again...",
        "Suck it all the way down again.",
        "Take it all, bitch..."
    ]
    mc "[renpy.random.choice(dialogsch10_513)]"
    $ dialogsch10_513k = [
        "*slurp, slurp* {i}{size=-3}Mmph, see? It’sh not that hard to ashk nicely firsht.",
        "*slurp, mmmph* {i}{size=-3}But I’ll shtop shucking if you get tosh rough...",
        "*chup, slurph* {i}{size=-3}That dam dressh endid up coshting me a lot...",
        "*shlurp, chup* {i}{size=-3}Hmmmh..."
    ]
    k "[renpy.random.choice(dialogsch10_513k)]"
    $ ch10_513kbj1 = 4
    $ anim_speed = 0.015
    scene ch10_513kbj3_ with Dissolve(0.3) 
    call screen ch10_513kbj3_
label ch10_513kbj4_:
    $ ch10_513kbj1 = 6
    scene ch10_513kbj4_ with Dissolve(0.3) 
    call screen ch10_513kbj4_

image ch10_513kbj4_:
    function ch10_513kbj4_
image ch10_513kbj1_:
    function ch10_513kbj1_
image ch10_513kbj3_:
    function ch10_513kbj3_
image ch10_513kbj2_:
    function ch10_513kbj2_
label afterch10_513kbj1_1:
    $ hide_anim_speed()
    show screen random_speed(0.02, 0.035)
    mc "Mmm... that feels amazing."
    mc "Yeah, just like that... keep looking into my eyes..."
    pause
    mc "You’re getting really good at this..."
    k "*Slurp, chup*"
    mc "Thought you didn’t like doing this before."
    mc "But now... looks like you’re really into it."


    mc "You're already my little bitch... my [krelat] personal cock-sucking piece of ass, just for me."
    pause
    scene ch10_513kbj2_
    k "*slurp* {i}{size=-3}Only fo' you?... geep dream'n..."
    k "*chup, shlp* {i}{size=-3}Buh' if you keep buyin' me nice stuff..."
    mc "Uh?"
    mc "So you're saying if I keep buying you things, you'll be my exclusive bitch?"
    mc "Damn... you really do play the bitch role perfectly."
    scene ch10_513_1
    k "*mua* {i}{size=-1}Wha' role?"
    scene ch10_513_2
    mc "Haha, wow..."
    image ch10_513anima:
        "ch10_513_1" with dissolve
        1.5
        "ch10_513_2" with dissolve
        1.5
        repeat
    scene ch10_513anima
    play soundfx3 kissing2 volume 0.25 loop
    mc "Lick my balls when you go down, like that..."
    pause
    mc "And who’s buying me stuff, huh?"
    k "*chup, shlup* {i}{size=-3}I’ll pay you if you wash the dishes o' my days..."
    mc "Ha-ha..."
    pause
    $ predict_ch10_513kbj4_()
    mc "You think [mia] will be pissed that we’re fucking in her mom’s bedroom?"
    k "*smch* {i}{size=-1}Nah..."
    k "{i}{size=-3}I ah'ked her for permission befo' we go' here.{/i}{/size} *smonch*"
    mc "You planned it all?"
    mc "Nicely done, bitch..."
    pause
    mc "{i}Suck it again..."
    $ stop_sounds()
    scene ch10_513kbj1_

default ch10_513kbj1 = 0
label afterch10_513kbj2_:
    if ch10_513kbj1 != 1:
        scene ch10_513kbj1_
    $ hide_anim_speed()
     
    $ anim_speed = 0.017
    k "*Slurp, shuck, chup*"
    mc "Oh, yeah... just like that..."
    pause
    mc "Are you touching yourself?"
    $ anim_speed = 0.03
    scene ch10_513kbj4_ 
    mc "You're enjoying this, aren't you, you little slut?"
    k "{i}Hmm... {/i}*Slurp, slurp*"
    mc "{i}Would've been a shame if you didn’t enjoy sucking with those perfect little slut lips..."
    k "*Slurp, slorpt* {i}{size=-3}Stop callin' me a slu' al-ready, u’re ove-doin' it."
    mc "{i}Such a killjoy..."
    $ anim_speed = 0.017
    scene ch10_513kbj1_
    pause
    mc "Uh, so good..."
    mc "Take it deeper, [k]."
    mc "I know you can go deeper than that..."
    scene ch10_513kbj3_
    $ anim_speed = 0.015
    mc "*hngh* There you go, all the way in... {w=1.5}{nw}"
    play voicefx "audio/character/k/hard/k_moan_hard_2.wav" volume 0.75
    scene ch10_515 with vpunch
    k "Hah! *cough, cough*"
    k "Idiot! *cough*"
    k "*cough* You idiot..."
    scene ch10_513kbj1_ with vpunch
    $ anim_speed = 0.017
    mc "Shhh! If you can still insult me, you can keep sucking..."
    k "*Slurp, chup, shlup* {i}{size=-2}Hmm..."
    call screen ch10_513kbj1_ with dissolve

label afterch10_513kbj1_:
    $ hide_anim_speed()
    $ anim_speed = 0.011
    if ch10_513kbj1 != 4:
        scene ch10_513kbj3_ with Dissolve(0.2)
        $ anim_speed = 0.011
    mc "*Hmnh* {i}Take it all! Uh..."
    k "*Gug, guh, gug*"
    scene ch10_515-- at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    play soundfx3 ["audio/wavs/bjgags3.ogg", "audio/bj/bj_b_04.ogg", "audio/wavs/bjgags4.ogg", "<silence 3.0>", "audio/bj/bj_b_05.ogg", "audio/wavs/bjgags8.ogg", "audio/bj/bj_b_09.ogg", "<silence 2.0>", "audio/wavs/bjgags10.ogg", "<silence 3.0>", "audio/bj/bj_b_02.ogg"] loop volume 0.5 
    mc "Argh... Yeah, all the way in..."
    k "*Glugh, -plrff*..."
    pause
    $ stop_sounds()
    scene ch10_515 with vpunch
    play voicefx "audio/character/k/hard/k_moan_hard_6.wav" volume 0.75
    k "*Cough, cough!* Hah..."
    scene ch10_516
    mc "What a good little bitch..."
    mc "Was that just my imagination, or did you actually come just from sucking my cock?"
    k "*Huh*..."
    mc "How's that pussy feeling? Ready to be fucked all the way in?"
    k "{i}Yeah... take me already, hah..."
    mc "I'm gonna give you a fuck you'll never forget."
    scene ch10_517
    k "Time's up."
    k "You've always been the submissive one between us, so stop pretending you're in charge."
    mc "But you said you'd be my bitch."
    k "And I was."
    play soundfx3 kissing volume 0.1
    play soundfx2 kissing2 volume 0.1
    scene ch10_518
    k "Did you really think a dress and a purse would make me your bitch forever?"
    mc "What is this now, a subscription plan?"
    k "*giggle* Exactly."
    image ch10_519anim:
        "ch10_519" with dissolve
        1.5
        "ch10_520" with dissolve
        1.5
        repeat
    $ stop_sounds(0.0)
    play soundfx3 kissing volume 0.2 loop
    play soundfx2 kissing2 volume 0.2 loop
    scene ch10_519anim
    k "Hmm... *smonch, muah*"
    mc "That wasn’t in the contract..."
    k "*smonch* Well, that’s what you get for skipping the fine print..."
    $ stop_sounds(0.5)
    scene ch10_521
    play soundfx3 "audio/mouth/saliva_04.ogg" volume 0.2
    k "Open that mouth... good boy."
    mc "Aah..."
    scene ch10_522
    pause
    scene ch10_523
    play soundfx3 kissing volume 0.1 loop
    play soundfx2 kissing2 volume 0.1 loop
    k "Hnm.. *smch, mch*"
    pause
    scene ch10_519anim
    k "*Smch* {i}{size=-2}Come on, put it in already..."
    $ stop_sounds()
    scene ch10_524_1
    $ stop_sounds()
    k "Ah-ah..."
    mc "{i}Uhh, [k]..."
    mc "Sit down on it... take it all in."
    scene ch10_518kfm4_1
    k "Uh, unh..."
    $ clear_audiofx()
    play voicefx kmoansoft volume 0.2 loop
    scene ch10_518kfm4_ with Dissolve(0.2)
    $ anim_speed = 0.015
    k "*Ah, uh, uh*"
    mc "Oh..."
    mc "Yeah, ride this cock just like that..."
    mc "*Hngh, ah*"
    mc "Damn, [k]..."
    mc "*Hmnh* You're just too damn hot..."
    pause
    k "*Ah, ah* {i}Oh God..."
    k "{i}You like it like this?"
    mc "Yeah, keep bouncing just like that..."
    k "God... you're stretching me out so deep..."
    scene ch10_518kfm3_
    mc "Yeah... you love how deep I’m filling you, don’t you?"
    k "Y-yeah. *uh, uh*"
    mc "(Girls usually complain about how long I am... they say it hurts when I go all in.)" with dissolve
    mc "(But she doesn’t even flinch, despite having one of the tightest, most delicious pussies I’ve ever been inside.)" with dissolve
    scene ch10_518kfm1_
    pause
    mc "You're moaning pretty loud, [k]."
    k "S-so let them hear... who cares..."
    mc "R-right, good point. They already know anyway."
    k "Yeah, it doesn’t matter now."
    k "*Ah, hah, ah*"
    mc "Let’s enjoy this while we can. Might be weeks before we can do it again."
    k "*Ah, huh* {i}That’s true..."
    scene ch10_518kfm2_
    pause
    k "{i}Though... we could always sneak back here if we can't hold out..."
    mc "You think [mia] would care?"
    k "*Hah, hah* {i}N-nah, she’s chill about it."
    mc "{i}But [s] would have to come with us. [drelat!cl] [d] doesn’t let us go out alone anymore."
    k "*Hah* {i}Then we bring her too."
    k "{i}She can hang out with [mia] while you and I... get busy in here."
    mc "Wow, you planned all that just for more sex with me?"
    k "*Hah, ah, ah* {i}Idiot..."
    call screen ch10_518kfm2_ with dissolve




init python:
    def ch10_518kfm4_(trans, st, at):
        if store.current_active_animation != "ch10_518kfm4_":
            store.current_active_animation = "ch10_518kfm4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kfm4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kfm4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.6 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                if anim_speed > 0.02:
                    final_volume = max(0.005, 0.02 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.02 > 0.0125:
                    final_volume = max(0.005, 0.06 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.0125:
                    final_volume = max(0.1, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.6 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_518kfm3_(trans, st, at):
        if store.current_active_animation != "ch10_518kfm3_":
            store.current_active_animation = "ch10_518kfm3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kfm3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kfm3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.6 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.02:
                    final_volume = max(0.005, 0.02 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.02 > 0.0125:
                    final_volume = max(0.005, 0.06 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.0125:
                    final_volume = max(0.1, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_518kfm2_(trans, st, at):
        if store.current_active_animation != "ch10_518kfm2_":
            store.current_active_animation = "ch10_518kfm2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kfm2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kfm2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.6 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.02:
                    final_volume = max(0.005, 0.02 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.02 > 0.0125:
                    final_volume = max(0.005, 0.06 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.0125:
                    final_volume = max(0.1, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_518kfm1_(trans, st, at):
        if store.current_active_animation != "ch10_518kfm1_":
            store.current_active_animation = "ch10_518kfm1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kfm1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kfm1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.6 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 36 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.02:
                    final_volume = max(0.005, 0.02 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.02 > 0.0125:
                    final_volume = max(0.005, 0.06 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
                if anim_speed <= 0.0125:
                    final_volume = max(0.1, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='soundfx')
                    renpy.sound.play(random_sound, channel='soundfx')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_518kfm5_(trans, st, at):
        if store.current_active_animation != "ch10_518kfm5_":
            store.current_active_animation = "ch10_518kfm5_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kfm5_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kfm5_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 3 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.6 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 13 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
screen ch10_518kfm1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch10_518kfm4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch10_518kfm3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch10_518kfm2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10_518kfm4_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_518kfm2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch10_518kfm4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch10_518kfm3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch10_518kfm1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10_518kfm4_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_518kfm3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch10_518kfm4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch10_518kfm2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch10_518kfm1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10_518kfm4_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_518kfm4_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch10_518kfm3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch10_518kfm2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch10_518kfm1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("afterch10_518kfm4_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_518kfm5_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed=0.015, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_518kfm5_beff"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
image ch10_518kfm1_:
    function ch10_518kfm1_
image ch10_518kfm2_:
    function ch10_518kfm2_
image ch10_518kfm3_:
    function ch10_518kfm3_
image ch10_518kfm4_:
    function ch10_518kfm4_
image ch10_518kfm5_:
    function ch10_518kfm5_
default ch10_518kfm = 0
label ch10_518kfm1_:
    $ ch10_518kfm = 1
    scene ch10_518kfm1_ with nothing
    call screen ch10_518kfm1_
label ch10_518kfm2_:
    $ ch10_518kfm = 2
    scene ch10_518kfm2_ with nothing
    call screen ch10_518kfm2_
label ch10_518kfm3_:
    $ ch10_518kfm = 3
    scene ch10_518kfm3_ with nothing
    call screen ch10_518kfm3_
label ch10_518kfm4_:
    $ ch10_518kfm = 4
    scene ch10_518kfm4_ with nothing
    call screen ch10_518kfm4_

init python:
    def ch10_518kf3_(trans, st, at):
        if store.current_active_animation != "ch10_518kf3_":
            store.current_active_animation = "ch10_518kf3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kf3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kf3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.021 :
                    final_volume = max(0.005, 0.01 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed > 0.018 <= 0.021 :
                    final_volume = max(0.005, 0.03 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed < 0.018:
                    final_volume = max(0.005, 0.06 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_518kf2_(trans, st, at):
        if store.current_active_animation != "ch10_518kf2_":
            store.current_active_animation = "ch10_518kf2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kf2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kf2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.021 :
                    final_volume = max(0.005, 0.01 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed > 0.018 <= 0.021 :
                    final_volume = max(0.005, 0.05 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed < 0.018:
                    final_volume = max(0.005, 0.1 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_518kf1_(trans, st, at):
        if store.current_active_animation != "ch10_518kf1_":
            store.current_active_animation = "ch10_518kf1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_518kf1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_518kf1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 16 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.021 :
                    final_volume = max(0.005, 0.01 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed > 0.018 <= 0.021 :
                    final_volume = max(0.005, 0.03 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
                elif anim_speed < 0.018:
                    final_volume = max(0.005, 0.06 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
image ch10_518kf3_:
    function ch10_518kf3_
image ch10_518kf2_:
    function ch10_518kf2_
image ch10_518kf1_:
    function ch10_518kf1_
default ch10_518kf3pos = 0
label ch10_518kf3_:
    $ ch10_518kf3pos = 3
    scene ch10_518kf3_ with Dissolve(0.2)
    call screen ch10_518kf3_
label ch10_518kf2_:
    $ ch10_518kf3pos = 2
    scene ch10_518kf2_ with Dissolve(0.2)
    call screen ch10_518kf2_
label ch10_518kf1_:
    $ ch10_518kf3pos = 1
    scene ch10_518kf1_ with Dissolve(0.2)
    call screen ch10_518kf1_
screen ch10_518kf1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Show("random_speed", max_speed= 0.028, min_speed= 0.031), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed= 0.018, min_speed= 0.021), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Show("random_speed", max_speed= 0.012, min_speed= 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed= 0.012, min_speed= 0.031), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_518kf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_518kf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_518kf1_asdww"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_518kf2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Show("random_speed", max_speed= 0.028, min_speed= 0.031), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed= 0.018, min_speed= 0.021), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Show("random_speed", max_speed= 0.012, min_speed= 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed= 0.012, min_speed= 0.031), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_518kf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_518kf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_518kf1_asdww"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_518kf3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Show("random_speed", max_speed= 0.028, min_speed= 0.031), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed= 0.018, min_speed= 0.021), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Show("random_speed", max_speed= 0.012, min_speed= 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed= 0.012, min_speed= 0.031), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_518kf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_518kf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_518kf1_asdww"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label afterch10_518kfm4_:
    pause 0.5
    if ch10_518kfm != 4:
        scene ch10_518kfm4_ with Dissolve(0.2)
    $ hide_anim_speed()
    $ anim_speed = 0.012
    k "{i}Ohh... aaah!"
    mia "What!?"
    mia "I can't hear you, I'm in the shower!"  
    pause
    $ anim_speed = 0.015
    play voicefx kmoanhard volume 0.5 loop
    scene ch10_518kfm5_ with hpunch
    k "Ahh! [mc]!"
    mc "*Hahh* You're squeezing me so tight..."
    k "[mc]... yes, yes!"
    mc "Damn... *mmh*.."
    mc "(Her pussy is gripping me so fucking good...)" with dissolve
    call screen ch10_518kfm5_ with dissolve
label ch10_518kfm5_beff:
    $ anim_speed = 0.013
    k "Haaah!{w=2.0}{nw}" with cumming
    stop voicefx fadeout 2.0
    scene ch10_518kfm5_10 with Dissolve(2.0)
    pause 0.5
    scene ch10_525
    mc "Wow..."
    k "*Phew, uh* {i}Uh..."
    play sound kissing volume 0.3 loop
    play voicefx2 kissing2 volume 0.3 loop
    scene ch10_519anim
    k "*Muah, smonch*"
    stop voicefx fadeout 0.1
    stop voicefx2 fadeout 0.1
    $ anim_speed = 0.02
    scene ch10_518kf3_
    play voicefx kmoansoft volume 0.25 loop
    pause
    k "*Hah* {i}That was... *huh*, amazing..."
    mc "You really liked it?"
    k "{i}Y-yeah, it was really good..."
    pause
    mc "{i}Do you like doing this with me?"
    k "{i}What, sex?"
    mc "{i}Yeah... I mean, do you enjoy it? Do you like me?"
    k "*Ah, ah* {i}You mean... if I like you?"
    mc "{i}I mean, I must be attractive, right? That’s why we keep doing this."
    k "*huh, ah* {i}I guess..."
    mc "{i}Good to know."
    k "*Ah, hah* {i}Yeah..."
    mc "*Ngh* {i}Hey, [k]..."
    k "*Ah, hah, ah* {i}What?"
    scene ch10_518kf2_ 
    mc "*Hah* {i}Never mind..."
    pause
    k "{i}Come on, don’t get all mysterious on me. *Hah, oh*"
    k "*Ah, ah* {i}Are you not going to tell me?"
    $ anim_speed = 0.02
    mc "*Ngh!* {i}It’s nothing. I just wanted to say you’re beautiful... And I love this."
    pause
    k "*Hah, ah, ah* {i}Idiot..."
    pause
    mc "{i}No matter what I say, you always call me that."
    k "*Ah, ah, uh* {i}It’s how I show affection."
    mc "*ngh!* {i}Well, you're very affectionate then..."
    pause
    k "*Ah, ah, ah* {i}It’s just... sometimes I don’t know how to answer the things you say..."
    pause
    k "*Uh, ah, ah* {i}I can feel you throbbing. Are you close?"
    mc "Not yet, but it’s starting to feel really good... *hmn*"
    scene ch10_518kf1_ 
    k "*Huh* {i}Let me know when you're close..."
    call screen ch10_518kf1_ with dissolve
label ch10_518kf1_asdww:
    if ch10_518kf3pos != 2:
        scene ch10_518kf2_
    k "*Ah, hah, uh* {i}Fuck... you're gonna make me cum again...{/i}"
    mc "*Heh...* {i}What is that now, your third time?{/i}"
    k "*Ah, hah, uh* {i}{size=-3}I’ve already lost count... maybe three times, yeah..."
    mc "*hngh* {i}Doesn't that mean you like me more than I like you?"
    k "{i}Keep dreaming...{/i} *Hah, uh, ah*"
    mc "{i}Feels like a dream, but no, you're actually fucking your hot [krelatmc], [mc]."
    k "*Ah, ah, ah* {i}You sound like a fucking narcissist."
    mc "{i}Just trying to spice things up."
    k "{i}Wanna turn up the heat?"
    mc "{i}I want *you* to get even hotter."
    $ hide_anim_speed()
    k "{i}Then keep fucking your personal bitch!"
    $ hide_anim_speed()
    $ anim_speed = 0.009
    play voicefx kmoanhard loop volume 0.5 fadein 0.1
    mc "Uh, fuck!"
    mc "*Ngh!*{i}Tell me you like it, say you love my cock."
    k "*Ah, aah* {i}I-love your cock... I love it when you fuck me with your huge cock."
    mc "{i}*G-gah!*, [k], ungh... *ngh!*"
    k "*ah, ah, dah!* {i}Yes, yes! Fuck your bitch!"
    mc "*Gah!* {i}Shit, I'm gonna have a fucking heart attack..."
    k "{i}Don't stop!, I don't give a fuck if you die, don't stop!"
    mc "*Argh!*{i} Take it, take it bitch!"
    k "*Aaah, hyaaa!*"
    stop music fadeout 0.1
    play soundfx "audio/wc.ogg" volume 0.5
    $ renpy.pause(1.0, hard=True)
    stop voicefx fadeout 0.1
    scene ch10_518kf2_1 with vpunch
    $ renpy.pause (4.0, hard=True)
    stop soundfx fadeout 1.0
    "..." 
    scene ch10_518_1
    pause
    s "I-I just got bored waiting in the bathroom -You two are taking forever..."
    scene ch10_518_2
    s "I'm going to lock the door..."
    pause
    scene ch10_518kf2_1
    pause 0.5
    play sound "audio/doorclosed.ogg" volume 0.5
    pause 4.0
    play music sexy2
    play voicefx kmoanhard volume 0.5 loop
    scene ch10_518kf2_ with nothing
    k "*Ah, aah, eaah!* {i}Give it to me, give it to me!" #they keep going as if nothing happened, despite [s] having just seen them, due to their great excitement.
    mc "*Argh!* {i}I'm going to cum inside."
    k "{i}It's not a safe day.{/i} *Haah, aah!*"
    mc "{i}I don't give a shit, I'll buy you the pill."
    $ anim_speed = 0.01
    mc "Aaah!, take it all bitch!"
    k "*Naah, aah!*"
    image ch10_529_anim:
        "ch10_529_1" with Dissolve(0.05)
        0.1
        "ch10_529_2" with Dissolve(0.05)
        1.0
        "ch10_529_3" with Dissolve(0.05)
        0.1
        "ch10_529_1" with Dissolve(0.05)
        0.1
        "ch10_529_2" with Dissolve(0.05)
        1.0
        "ch10_529_3" with Dissolve(0.05)
        0.1
        "ch10_529_1" with Dissolve(0.05)
        0.1
        "ch10_529_2" with Dissolve(0.05)
        0.1
        "ch10_529_3" with Dissolve(0.05)
        0.1
        "ch10_529_1" with Dissolve(0.05)
        0.1
        "ch10_529_2" with Dissolve(0.05)
        0.1
        "ch10_529_3" with Dissolve(0.05)
        0.1
        "ch10_529_1" with Dissolve(0.05)
        0.1
        "ch10_529_2" with Dissolve(0.05)
        1.0
        "ch10_529_3" with Dissolve(0.05)
        0.1
        repeat
    stop voicefx
    $ renpy.music.set_audio_filter("voicefx", af.Lowpass(440))
    play voicefx kmoansoft volume 0.5 loop
    scene ch10_529_anim with cumming
    mc "*Hngh, mnh!*"
    stop voicefx fadeout 5.0
    pause
    scene ch10_530-
    $ clear_audiofx()
    k "Uh..."
    k "Y-you came inside..." 
    k "Uh... I can feel it flowing inside me..." 
    mc "My balls feel totally dry..."
    pause
    k "D-don't pull out, leave it in there a little longer..."
    pause
    stop music fadeout 1.5
    scene blackscreen
    $ renpy.end_replay()
    pause
    play music scene2 fadein 1.0
    scene ch10_531
    mc "Let's stay here a little longer..."
    k "No way..."
    k "[mia] shouldn't be long. Quick, we gotta get dressed."
    scene ch10_532
    mc "You were amazing today, I gotta admit. That was the best sex I've ever had."
    k "Same here..."
    pause
    mc "What are we gonna tell [s]?"
    k "Nothing, what's there to tell?"
    k "She already promised she wouldn't say anything."
    mc "Still..."
    mc "I mean, she literally saw us in the act."
    k "You talk to her if you're so worried about it."
    mc "Yeah, I will."
    pause
    scene ch10_531
    k "Hurry up, we gotta get dressed."
    mc "If you give me five minutes, I think I can get hard again... *smch*"
    k "*Giggles* {i}Hmm, no..."
    scene blackscreen
    pause
    scene ch10_533 with fade
label ch10_518kf1_asdasd:
    mia "Hey, look who's here."
    mia "You guys can go for round two if you want, we'll wait."
    k "What? I don't know what you're talking about, l-let's just go."
    s "{size=-3}{i}I din't kniv whit yii'ri tilkink ibiit..."
    mc "(Shit, [s] doesn't look calm at all...)" with dissolve
    mia "What's with your hair? Were you guys fighting or something?"
    scene ch10_534
    k "Is my hair messy?"
    mc "Yeah, a little... quite a bit actually."
    pause
    scene ch10_535
    s "Let's go already, I'm really hungry and want to eat."
    mc "Y-yeah, me too."
    mia "I... was talking with [s]."
    mia "You won't say anything about what you saw, right?"
    s "Uhm... I don't know."
    mia "Huh? You told me you'd keep their secret."
    s "Yeah, yeah, I'll keep the secret, whatever. I just want to leave already."
    scene ch10_533
    mc "You told [mia]?"
    mia "No, that was [k] and her screaming."
    mia "Sorry girl, but you moan really loud."
    k "W-well, let's go already."
    scene ch10_535
    k "It's fine, she knows that if she says something [mc] will get kicked out of the house."
    mia "[s], you have to keep the secret, ok?"
    s "Yes, now let's go already."
    mia "I know she won't say anything."
    k "Let's get going, I'm starving too."
    stop music fadeout 1.5
    scene blackscreen 
    pause
    play music scene1 fadein 1.5
    scene ch10_536
    a "So many bags... Where did you get the money to buy all that?" 
    s "It was from the savings we had from the money [drelatks] has been giving us to make up for not spending time with us."
    s "[mc] bought us some things too."
    a "Oh."
    s "And there are more bags in the car."
    a "Will you show me what you got after we eat?"
    s "Yeah! I got some cute outfits."
    a "I can't wait to see them, sweetie."
    if stephloving == "True":
        scene ch10_537 with fade
        s "Put them on my bed."
        mc "Alright."
        scene ch10_538
        mc "Are there any more in the car?"
        s "Nope, that's all."
        mc "Wanna show me what you bought?"
        s "Yeah."
        scene ch10_539
        s "Look, I got this skirt I'm gonna wear today, and a top I really liked."
        s "Here it is..."
        scene ch10_540 with hpunch
        s "Wait, no!"
        s "I don't wanna talk to you!"
        pause
        mc "Why not?"
        mc "Are you mad at me?"
        s "Yeah."
        mc "Oh, well... I guess you don't wanna go to the fair with me then."
        scene ch10_541 with hpunch
        s "Yes I do!"
        mc "But you're super mad at me."
        s "Ugh, [mc], you're so dumb."
        scene ch10_543 with vpunch
        mc "You just want me to pamper you now, huh?"
        s "No, that's not true..."
        scene ch10_542
        mc "Oh really?"
        s "N-no, {w=0.5}*s-stop*, {i}don't tickle my ribs."
        mc "I promise we're gonna have so much fun today, we're getting on every ride."
        s "Every single one?"
        mc "Yep, and more than once. I'm buying a ton of tickets."
        mc "You're gonna be my princess today."
        s "O-okay..."
        mc "Aren’t you gonna show me what else you got?"
        scene ch10_543
        s "Uhm..."
        s "Alright, I’ll show you."
        scene ch10_544
        s "Look, I got a really cute bag."
        s "It’s a designer brand."
        scene ch10_545
        s "Ta-da!"
        mc "Oh, that’s a nice bag."
        s "It’s a Vuis Luiton, it’s a good brand."
        mc "Oh yeah, looks expensive."
        s "It is... well, not that much, it was on sale. But at regular price it’s pretty pricey."
        mc "Yeah, you can tell. It’s really pretty."
        scene ch10_546
        a "Are you hungry? [d] made burgers and they’re surprisingly not bad."
        mc "[drelat!cl] [d]?"
        a "He’s already serving the plates."
        mc "[drelat!cl] [d] actually cooking something decent? I gotta see that for myself."
    stop music fadeout 1.5
    scene blackscreen
    pause
    play music scene2 fadein 1.5
    scene ch10_548
    d "Look at that, not bad, huh?"
    mc "[drelat!cl] [d], that meat looks amazing."
    d "I've been watching some videos, the trick is the charcoal, you can't use too much."
    d "Go sit down, son. I'll make you the best burger you've ever had."
    scene ch10_549 with fade
    d "Look who's here."
    mia "Hi, Mr. [d]."
    k "Is it true that you cooked?"
    d "Yes, sit down, I'm going to make you the best burger of your lives."
    scene ch10_550:
        xalign 0.5 yalign 1.0
        ease 6 yalign 0.0
    mia "Hi, [mc]."
    mc "Hi, [mia]."
    mc "{i}(Wow, she looks gorgeous...)" with dissolve
    scene ch10_553
    a "Hey, [mia], you look beautiful!"
    mia "Thank you, Mrs. [a]! But not as beautiful as you."
    a "Oh, stop it, you're too sweet. So, who's the lucky guy?"
    mia "No one special. [k] and I are just heading out."
    a "Going dancing?"
    k "Yeah."
    d "I'll make you a burger too, honey. No saying no to that."
    scene ch10_559
    d "But first I need the judge's verdict."
    mc "First impression, it looks excellent."
    scene ch10_551
    mc "It looks really appetizing, let's see how it tastes."
    mia "[mc], baby..."
    mc "Uh?"
    scene ch10_552
    mia "Thanks for the gift, I loved it."
    mc "Oh, you mean the purse."
    mia "It goes well with my outift, don't you think?"
    mc "Yeah, it looks great on you."
    mia "You always know what I like, that's why I love you."
    mc "Eh..."
    scene ch10_554
    mc "Y-yeah."
    d "{i}{size=-3}Heh, that's my boy..."
    scene ch10_557
    mia "Mr. [d], are you gonna let [k] go out with me today?"
    d "You asked me this morning, I remember saying yes."
    d "But only until midnight, don't forget."
    mia "Yes, I remember. Can [mc] come with us too?"
    scene ch10_558
    d "Sorry, they can't go out together."
    mia "I'll take care of them, I'll make sure they won't have a drop of alcohol, if that's the problem."
    d "Uh… when those two get together, things usually don’t go well. Better not risk it."
    mia "Oh, okay."
    d "But another day, you can invite him out, just the two of you. I don’t have a problem with that."
    scene ch10_552
    mia "Alright, another day then."
    mc "Yeah, sorry."
    mia "It’s cool, we’ll catch up next weekend."
    mc "Sure."
    scene ch10_556
    d "Burger without mustard for you, dear?"
    a "Yes, no mustard, please."
    d "Alright, one burger without mustard coming up."
    scene ch10_560
    s "[mc]."
    mc "Yeah?"
    s "You haven’t showered yet..."
    mc "I’m eating."
    s "But it’s almost nighttime."
    mc "It’s barely seven. Go get ready, I only need fifteen minutes."
    scene ch10_561
    mia "[mc], can you come with us for a sec?"
    mc "Uh, yeah, just let me finish my burger."
    d "Girls, aren’t you going to eat?"
    k "We’ll be right back."
    scene ch10_564 with fade:
        zoom 0.75
    mia "I did good, huh?"
    mc "Yeah, I think [drelat] [d] has no doubt that you and I have something."
    mc "What's going on, why did you bring us here?"
    mia "Get in and close the door."
    scene ch10_565:
        zoom 0.75
    mia "[s], we need you to do us a favor."
    s "Me?"
    mia "Yeah, see..."
    mia "Your [drelatks] won’t let [mc] and [k] go out together, but if you come with us, maybe he'll give the okay."
    scene ch10_566:
        zoom 0.75
    mia "Isn’t that a good idea? If [s] comes with us, there won’t be any problem. He’ll definitely give permission."
    mia "Or did you think we were planning to leave you behind?"
    mc "I don't know, I..."
    image ch10_568anim:
        "ch10_567" with Dissolve(0.5)
        0.5
        "ch10_567-" with Dissolve(0.5)
        0.5
        repeat 2
    scene ch10_568anim:
        zoom 0.75
    $ renpy.pause(2.0, hard=True)
    scene ch10_568:
        zoom 0.75
    mia "Isn't it a good plan?"
    k "Y-yeah, I guess..."
    scene ch10_565:
        zoom 0.75
    mia "But we need you to come with us, it's the only way."
    scene ch10_569:
        zoom 0.75
    s "I don't want to."
    mia "Huh? Why not?"
    s "Well... because..."
    scene ch10_570:
        zoom 0.75
    s "I already have plans."
    mia "Plans?"
    s "I'm going on a date later tonight."
    scene ch10_571:
        zoom 0.75
    mia "A date?"
    k "Really? Like… you’re actually dating someone?"
    s "Yep."
    mia "Is he cute?"
    k "That's a lie. [drelatks!cl] would never give you permission."
    s "Well, ask him."
    k "Haha, I can't believe it."
    mia "He better be really cute."
    if stephloving == "True":
        scene ch10_572 with fade:
            zoom 0.75
        s "{i}You shower properly, and make sure you use lots of soap."
        mc "Uh... yeah, of course."
        s "{i}{size=-3}And don’t forget to wash your penis really well, too."
        mc "Shh! Yeah, yeah... {i}I’ll make sure to shower good."
        s "Now go, we’re running late."
        stop music fadeout 1.0
        scene blackscreen 
        pause
        play music scene2 fadein 1.0
        play background "audio/shower.ogg" volume 0.2 loop
        scene ch10_562
        pause
        mc "{i}([s] took it better than I expected.)" with dissolve
        mc "{i}(Guess she's gotten used to it.)" with dissolve
        pause
        mc "{i}(Actually... {w=1.0}I do want to spend time with her.)" with dissolve
        pause
        scene ch10_563
        mc "{i}(She told me to wash my dick well... what’s up with that?)" with dissolve
        mc "{i}(At least her intentions are pretty clear...)" with dissolve
        mc "{i}(When we get home, she’s definitely going to want us to do some ''sexy stuff''.)" with dissolve
        mc "{i}(I don’t know how to stop this anymore... {w=1.0}And honestly, I don’t have the willpower to try...)" with dissolve
        pause
        mc "{i}(I think I’m kinda excited to be honest...)" with dissolve
        scene ch10_562
    pause
    stop background fadeout 1.0
    stop music fadeout 1.0
    scene blackscreen
    pause
    play music scene1 fadein 1.5
    scene ch10_573
    s "N-no, you can't come in yet!"
    mc "Hurry up, [s]."
    mia "{i}{size=-3}Is he already there?!{/i}{/size}"
    mia "She's coming out now, I'm finishing her hair."
    scene ch10_574--:
        subpixel True
        xalign 0.5 yalign 1.0
        ease 6 yalign 0.0 zoom 0.5
    mia "Where, where is he?"
    k "Maybe he came in his car."
    if stephloving == "True":
        mc "{i}(Wow...)" with dissolve
        pause
    scene ch10_575 with vpunch
    s "Ow!"
    mia "Through the window!"
    k "What, did you see him?"
    scene ch10_576
    k "Where is he?"
    mia "I don't know, do you see anything?"
    mc "You’re wearing heels."
    s "Yeah."
    k "He must have parked outside."
    mia "I can see some lights over there."
    k "That's the neighbors."
    scene ch10_577
    mc "We're leaving now."
    a "Take care, don't come back too late."
    mc "Yeah."
    mia "Huh?"
    k "Liar!"
    stop music fadeout 1.0
    scene blackscreen
    if stephloving != "True":
        jump ch10_slfalse
    pause
    scene ch10_578
    play music scene2 fadein 1.5
    pause
    scene ch10_579
    mc "We're here. Ready to have some fun?" 
    s "Yeah... I guess."
    mc "Oh, you’re wearing makeup."
    mc "Did you do it yourself?"
    s "Uh-huh..."
    pause
    mc "You look really pretty."
    s "If you say so..."
    pause
    mc "Hm?"
    mc "Is my little princess still mad at me?"
    mc "My sugar cube?"
    mc "My kitty eyes?"
    scene ch10_580
    s "I don’t have..." 
    scene ch10_579
    s "{i}I don’t have kitty eyes."
    mc "Oh, I see... my pretty little puppy is still mad."
    scene ch10_580
    s "{i}I’m not a puppy either..."
    mc "Can I get a kiss?"
    scene ch10_579
    s "It’ll mess up my lipstick..."
    mc "Alright... Let me open the door for you."
    pause
    scene ch10_581
    mc "Hold my hand."
    s "{i}Thanks..."
    scene ch10_582
    mc "You're wearing high heels."
    s "..."
    pause
    mc "What's wrong, [s]?"
    mc "We're at the fair, remember?"
    mc "I want us to have a really great night together."
    pause
    scene ch10_583
    pause
    s "I do want a kiss..."
    scene ch10_584
    pause
    play sound "audio/mouth/kiss_01.ogg" volume 1.0
    pause 0.1
    scene ch10_583
    pause 0.75
    scene ch10_585
    mc "Oh, you did your nails too?"
    s "Yeah, I picked a pearly white 'cause it goes with my pearl necklace. \n{i}{size=-3}-They're not real pearls."
    mc "It looks really cute on you."
    s "Thanks."
    stop music fadeout 1.5
    scene blackscreen
    pause
    play background "audio/fairsfx.ogg" volume 0.18 loop fadein 1.5
    scene ch10_587 with Dissolve(2.0)
    s "Aren’t you scared of the rollercoaster?"
    mc "Scared? I’m pumped to ride it!"
    s "Me too!"
    s "There’s so many people today."
    mc "It’s the weekend."
    "Next in line, please."
    scene ch10_588
    mc "I'll pay by transfer."
    s "You wore your nice watch."
    mc "Of course, today’s a special day."
    s "Yeah, today’s gonna be really special."
    scene ch10_589
    mc "Ta-da!"
    s "That’s a ton of tickets!"
    mc "We're gonna have so much fun today."
    scene ch10_590
    s "Which one do we ride first?"
    s "Let’s go to those that spin and spin!"
    mc "Which ones?"
    s "Those! Hurry, they're about to start the ride."
    show ch10_591- with vpunch:
        xalign 0.5 yalign 1.0
        ease 5 yalign 0.0
    mc "Woah! How are you walking that fast in heels?"
    s "Come on, hurry up, [mc]!"
    pause
    scene ch10_592
    s "Haha, we almost didn’t make it."
    mc "Yeah, just barely."
    mc "I should’ve said this earlier, but this ride always makes me nauseous..."
    s "No, eww, don’t you dare throw up on me!"
    mc "I’ve got an idea, if I feel sick, you open your purse."
    scene ch10_593
    s "No! Eww! No, [mc]!"
    mc "It’s starting... better get that purse ready."
    s "N-no, [mc]! Don’t you dare!"
    mc "Haha, I’m kidding."
    scene ch10_594
    s "Waah!"
    mc "This is way faster than I remember."
    s "Hold me! I feel like I’m slipping!"
    scene ch10_595
    s "Hyaa!"
    pause
    show ch10_598 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    s "Hold me tight, [mc], I’m scared!"
    mc "Don’t worry, I got you."
    scene ch10_597- at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    pause
    scene ch10_597 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    pause
    scene ch10_599 with fade
    mc "Let’s go to that one next! That one!"
    mc "Come on!"
    scene ch10_600
    s "Waah! This one's super fast!"
    mc "Yeah, haha! I thought it was for little kids!"
    s "I told you!"
    scene ch10_601
    s "Hyaaa!"
    pause
    scene ch10_602 with hpunch
    s "Take that!"
    mc "You little rascal..."
    scene ch10_603 with vpunch
    mc "H-hey, time out! My car’s steering weird!"
    s "Not my problem!"
    mc "Hey!" with vpunch
    scene ch10_604 with fade
    s "Please, [mc]."
    mc "Okay, okay..."
    s "But ride with me!"
    mc "I can’t, [s]."
    s "Why not?"
    mc "I told you, I’m too big. The guy in charge will get mad."
    scene ch10_605
    s "Please...? I just want us to take a picture on the horsies, that’s all."
    mc "Alright, fine. But if I get scolded, it’s your fault."
    scene ch10_606
    s "Are these like... giant horses or what?"
    mc "You’re right, what’s up with these horsies?"
    scene ch10_607-
    mc "Let me give you a hand."
    s "Uhm, yeah, please..."
    scene ch10_607--
    mc "There you go."
    s "But get on with me too."
    mc "All the horses are already taken."
    s "Then ride with me here."
    scene ch10_608-
    mc "The things you make me do..."
    s "You said we were gonna ride everything tonight."
    mc "I know."
    scene ch10_609
    s "{i}That man’s watching us... *giggles*"
    s "See? He didn’t even say anything."
    scene ch10_608--:
        subpixel True
        zoom 1.01
        align (0.5, 0.5)
        around (0.502, 0.5)
        linear 3.0 counterclockwise circles 1
        around (0.498, 0.5)
        linear 3.0 clockwise circles 1
        repeat
    mc "{i}(God... my bulge feels so warm between those soft cheeks.)" with dissolve
    mc "{i}(Every time the horse goes up and down, my cock presses hard against her butt... it feels amazing.)" with dissolve
    s "[mc]."
    s "Look at the camera, [mc]."
    scene ch10_609- with cumming
    pause
    scene ch10_611
    mc "{i}We should probably get off now."
    s "You already paid for the ride!"
    s "Don’t get off yet!"
    mc "Ugh..."
    scene blackscreen 
    pause 1
    scene ch10_612
    s "Let’s go to that one now!"
    scene ch10_613
    mc "That one?"
    s "Yeah, it’s the rollercoaster!"
    mc "Uhm..."
    scene ch10_614
    mc "Didn’t look that crazy from the outside..."
    mc "But there’s a huge line... What if we try something else?"
    scene ch10_612
    s "Come on, let’s get in line."
    mc "Wait, this ride’s pretty intense, aren’t you scared?"
    s "When I’m with you, nothing scares me."
    mc "{i}(Damn it...)"
    mc "A-alright, fine... let’s get in line."
    scene blackscreen 
    pause 1.0
    scene ch10_615
    s "Hurry, [mc], they’re already getting on!"
    mc "Get the tickets out."
    s "Got them."
    scene ch10_616
    mc "Two, please."
    "Thank you, Next."
    scene ch10_617
    s "You’re scared?"
    mc "Me? Nah, this is nothing."
    s "You can hold onto me if you get scared."
    scene ch10_618
    "Excuse me one moment. This ride has a height requirement."
    "I need you to stand right here for a second."
    scene ch10_619-
    s "Huh? Height requirement?"
    "Yes, since this is an extreme ride, not everyone is allowed to board."
    scene ch10_620
    "I’ll be right back."
    s "Do I meet the height?"
    mc "Yeah, you’re totally fine."
    scene ch10_621
    "Excuse me again, this will just take a second."
    s "Huh?"
    scene ch10_622
    "Aha! knew it! -about three inches."
    scene ch10_623
    "Yep, three inches too short."
    mc "Are you sure? She looks tall enough to me."
    "Nope, see here? She falls just under the minimum height."
    scene ch10_624
    "I’ll refund your tickets."
    s "N-no, that won’t be necessary."
    "Why not?"
    scene ch10_625
    s "I’ve got it right here..."
    scene ch10_626
    s "See? Right here." #she shows her ID clearly showing she's over 21.
    "What’s this?"
    scene ch10_627
    "Uh, let’s see... over twenty-one, alright."
    s "It’s my ID."
    "Yes, I can see that..."
    scene ch10_628
    s "People always get confused because I’m short."
    "Yeah... this doesn’t really prove anything."
    s "What?"
    "You still have to meet the height requirement. It’s not up to me."
    scene ch10_630
    "What’s taking so long? People are getting restless."
    "Sorry, just handling a customer question."
    scene ch10_631
    "I’m really sorry, you can’t ride."
    s "B-but what about him? That guy’s shorter than me!"
    "I’m sorry, I can’t let you on. It’s the rules."
    s "But—!"
    "No buts. Rules are rules. My hands are tied."
    mc "It’s okay, [s], let’s go. We still have the Ferris wheel."
    s "But I really wanted to..."
    scene ch10_632 with fade
    s "That’s so unfair!"
    mc "It’s okay, next time we’ll bring you some tall boots."
    s "But I wanted to ride it today!"
    image ch10_633anim:
        "ch10_634" with Dissolve(0.7)
        1.0
        "ch10_635" with Dissolve(0.7)
        1.0
        repeat
    scene ch10_633anim
    s "That rotten onion head..." 
    s "He saw me standing in line and didn't say anything about the height requirement."
    s "And he did let other people shorter than me get on, that useless guy. Do only men have that privilege?"
    s "I hate him, I hate him, I hate him!"
    mc "Hey, calm down..."
    scene ch10_636 with hpunch
    s "I may be short but at least I have eyebrows!"
    mc "H-hey, calm down."
    s "I bet your mom doesn't have eyebrows either, you idiot!"
    scene ch10_638
    mc "[s], calm down, it's not that big a deal."
    s "Damn rotten onion head!"
    mc "Calm down."
    scene ch10_638 with hpunch
    s "N-no, I'm not going to calm down!"
    s "Break his face, [mc]!" with hpunch
    mc "You need to calm down, [s]."
    scene ch10_637 with hpunch
    s "Your mom probably draws her eyebrows with a Sharpie!"
    scene ch10_638
    mc "H-hey, he's going to hear you."
    s "Let him hear me! That's what I want!" with hpunch
    scene ch10_637 with hpunch
    s "Asshole!" with hpunch
    s "Damn bastard son of a...!{w=0.75}{nw}" with hpunch
    stop background fadeout 1.0
    scene ch10_639 with nothing
    play background "audio/fairsfx.ogg" volume 0.1 fadein 1.0
    s "Hmm!"
    mc "*Munch, munch* Is your hot dog good?"
    s "Uh-huh... *munch, munch*"
    scene ch10_640
    mc "Are you calm now?"
    s "{i}Hm? {/i}*munch*"
    mc "You always get irritable when you're hungry."
    mc "It's okay, we'll come back another day with triple insoles in your shoes."
    s "Yeah."
    scene ch10_641
    s "Look, [mc]..."
    mc "Hm?"
    s "I'm eating your sausage..."
    scene ch10_642
    mc "{i}S-stop, people are watching you"
    s "{i}*Giggle*{/i}{w=0.5}{nw}"
    mc "Are you having a good time?"
    s "A really good time."
label ch10s2:
    if _in_replay:
        scene ch10_642
        play background "audio/fairsfx.ogg" volume 0.1 fadein 1.0
    mc "Eat your ice cream or it's going to melt."
    s "Oops! You're right."
    scene ch10_643
    s "Is yours good?"
    mc "Yeah, it's tasty."
    s "You got the cookies and cream, right?"
    mc "Yeah, it's the best I've had. Want to try it?"
    s "Yeah."
    scene ch10_644
    s "Nyam..."
    scene ch10_645
    s "It tastes very different from the ice cream shop near home. It's good."
    mc "What flavor did you choose?"
    s "Strawberry yogurt."
    mc "Is it good?"
    s "Really good."
    scene ch10_646
    mc "Can I have some? Uh..."
    mc "You already finished it!"
    s "{i}Oopsh... I thought you weren't going to want any."
    mc "You ate it fast so you wouldn't have to share..."
    s "N-no, really I didn't!"
    mc "Wait, you have a little left there, can I try it?"
    s "Where? Inside the cone?"
    scene ch10_647
    s "Uhm..!"
    pause
    scene ch10_649
    mc "{i}There's still a little bit on your lips..."
    scene ch10_648
    s "Huh..."
    scene ch10_650
    s "{i}Hmm.."
    scene ch10_651
    s "Hmm..."
    scene ch10_652
    pause
    scene ch10_653
    play soundfx "audio/wavs/bj_42.ogg" volume 0.5
    mc "Hmm..."
    scene ch10_654
    s "Huh... {i}You put your tongue in."
    s "{i}Do you want to taste more?"
    image ch10_655anin:
        "ch10_655" with dissolve
        1.0
        "ch10_655-" with dissolve
        1.0
        repeat
    scene ch10_655anin
    pause 0.1
    play soundfx2 kissing loop volume 0.15
    play soundfx kissing2 loop volume 0.3
    s "*Smch, hmm...*"
    pause
    stop soundfx2 fadeout 0.3
    stop soundfx fadeout 0.3
    scene ch10_656
    s "{i}[persistent.name[0]]-[persistent.name]..."
    s "{i}People are going to think we're boyfriend and girlfriend..."
    mc "{i}So?"
    s "{i}Don't you care if people say you have a midget girlfriend?"
    mc "{i}Nobody would say that, [s]. You're a very pretty girl, I'd feel very lucky to have a girlfriend like you... {w=1.0}Uhm..."
    s "R-really?"
    mc "Uh... {w=1.0}of course."
    s "{i}[mc]... you're so romantic."
    mc "I meant..."
    mc "I'm sure whatever guy you choose in the future will feel very lucky to have you as his girlfriend."
    s "[mc]..."
    if _in_replay:
        scene blackscreen
        pause 0.5
    $ renpy.end_replay()
    pause
    scene ch10_656-:
        zoom 0.75
    s "[mc], I want to tell you something..."
    mc "Yeah?"
    s "I can't say it here."
    s "It's something I want to tell you in private..."
    s "C-come with me, [mc]..."
    pause
label ch10s3:
    stop music fadeout 1.5
    stop background fadeout 1.5
    scene blackscreen
    pause
    $ renpy.music.set_audio_filter("background", af.Lowpass(500))
    play background "audio/fairsfx.ogg" fadein 2.0 loop volume 0.2
    scene ch10_656_1
    s "Yeah... we’ll be alone here."
    mc "Let's go a little further."
    pause
    scene ch10_656_2
    s "No one's around anymore."
    mc "Let's go a little bit further, just in case..."
    scene ch10_656_3
    s "Where are you taking me, hm?"
    mc "Here, behind this."
    scene ch10_656_4
    pause
    mc "Well? Tell me."
    s "Uhm..."
    s "I love you, [mc]."
    mc "I love you too."
    s "Do you love me a lot?"
    scene ch10_656_6
    mc "So much."
    s "Me too. I love you a ton."
    scene ch10_656_7
    s "W-we both love each other, right?"
    mc "Yeah, of course."
    pause
    scene ch10_656_6
    pause
    mc "What you want to tell me?"
    scene ch10_656_7
    s "Uhm, I..."
    s "I want to say that..."
    s "I want you and me to..."
    pause
    mc "Tell me..."
    s "..."
    mc "You want us to...? {w=0.5}Kiss?"
    scene ch10_656_6
    s "Yes!"
    mc "Okay."
    scene ch10_656_7
    pause 1.0
    image ch10_656_8anim:
        "ch10_656_8" with dissolve
        1.5
        "ch10_656_9" with dissolve
        1.5
        repeat
    scene ch10_656_8anim
    play sound kissing volume 0.3 loop
    play soundfx kissing2 volume 0.3 loop
    pause
    stop sound
    stop soundfx
    image ch10_656_10anim:
        "ch10_656_10" with dissolve
        1.5
        "ch10_656_11" with dissolve
        1.5
        repeat
    play sound kissing volume 0.2 loop
    play soundfx kissing2 volume 0.2 loop
    scene ch10_656_10anim
    s "Mmm... *smch*"
    pause
    stop sound
    stop soundfx
    scene ch10_656_5
    s "W-wait, I actually wanted to tell you something."
    mc "Oh? Did you want to tell me something... or just kiss me?"
    s "I wanted to say something but then I suddenly felt like kissing you, hehe..."
    mc "Alright then, go ahead."
    s "Uhm... I-I just wanted to say today was amazing. Like, really special."
    mc "I'm really glad to hear that."
    mc "You make me so happy."
    scene ch10_656_7
    s "[mc]..."
    pause
    s "D-don’t you have something you want to tell me too?"
    mc "Something to tell you, huh...? Hmm..."
    s "Yeah... something you've been wanting to say right now..."
    pause
    mc "I love you."
    scene ch10_656_6
    pause
    s "{i}I-I love you too!"
    pause
    scene ch10_656_7
    s "Wanna kiss again?"
    mc "Of course I do."
    image ch10_656_13anim:
        "ch10_656_12" with dissolve
        1.5
        "ch10_656_13" with dissolve
        1.5
        repeat
    play sound kissing volume 0.1 loop
    play soundfx kissing2 volume 0.1 loop
    scene ch10_656_13anim
    s "*Smch, mch*..."
    pause
    scene ch10_656_17
    pause
    scene ch10_656_18
    s "Huh... *muah*"
    s "{i}Are we... really doing ''that'' here?"
    mc "{i}Just a little..."
    pause
    image ch10_656_19anim:
            "ch10_656_19" with dissolve
            1.5
            "ch10_656_20" with dissolve
            1.5
            repeat
    scene ch10_656_19anim
    s "*Smch, moch* {i}I like you, [mc]... Even though you're my [srelatmc] I like you..."
    mc "{i}I like you too."
    pause
    image ch10_656_24anim:
        "ch10_656_24" with dissolve
        1.5
        "ch10_656_23" with dissolve
        1.5
        repeat
    scene ch10_656_24anim
    mc "{i}I love this little butt..."
    s "{i}[mia] was right, she said this skirt would drive any guy crazy."
    mc "{i}Did [mia] help you get dressed?"
    s "{i}[mia] and [k]."
    mc "{i}I see..."
    pause
    scene ch10_656_25
    s "*Muah* {i}[mc], you're naughty..."
    mc "{i}Hmm, I want to touch your pretty breasts..."
    pause
    scene ch10_656_26
    mc "{i}Hmm..."
    s "*Smnch*"
    pause
    scene ch10_656_27
    s "*Hmm* {i}Uh..."
    mc "{i}Such nice little tits..."
    scene ch10_656_29
    mc "{i}(She's still not in the habit of wearing a bra...)"  with dissolve
    s "{i}You smell really good today."
    scene ch10_656_28
    mc "{i}Thanks, I put on some good cologne."
    mc "{i}You smell really good too..."
    pause
    scene ch10_656_31
    mc "{i}You smell like shampoo..."
    s "{i}It's the one [arelatks] uses."
    mc "{i}Ah... no wonder the scent seemed familiar."
    scene ch10_656_30
    mc "{i}Hmm..."
    image ch10_656_31anim:
        "ch10_656_31" with dissolve
        1.5
        "ch10_656_30" with dissolve
        1.5
        repeat
    scene ch10_656_31anim
    mc "{i}They're so soft..."
    s "{i}Uh..."
    pause
    scene ch10_656_23_1
    s "{i}[mc], w-what if someone comes?"
    mc "{i}Sorry, I got carried away..."
    s "{i}You got excited, didn't you?"
    s "{i}When you start touching me like this you get excited after a while."
    mc "{i}You're getting to know me..."
    s "{i}We do these things every day now, I'm learning."
    mc "{i}Oh, I see..."
    pause
    stop sound
    stop soundfx
    scene ch10_656_23_6
    mc "{i}Uh, how beautiful..."
    pause
    show ch10_656_23_1- with dissolve:
        subpixel True
        xalign 0.5 yalign 1.0
        ease 5 yalign 0.0
        ease 2.5 yalign 0.3
    pause
    s "{i}I like it when you hold me tight, it makes my legs tremble..."
    mc "{i}You're a very horny girl."
    s "*Giggle*{w=0.74}{nw}"
    show ch10_656_23_1-:
        ease 10 zoom 0.5
    mc "{i}Are you wet yet?"
    s "{i}I think so."
    mc "{i}Let's see..."
    pause
    scene ch10_656_23_1
    pause
    scene ch10_656_23_4
    s "{i}Uh..."
    pause
    scene ch10_656_23_7
    mc "{i}You're pretty wet already..."
    s "{i}I told you so..."

    image ch10_656_23animm:
        "ch10_656_23_4" with dissolve
        1.5
        "ch10_656_23_5" with dissolve
        1.5
        repeat
    scene ch10_656_23animm
    play voicefx smoansoft volume 0.5 loop
    s "{i}Uh... uhm..."
    mc "{i}I like it when you're this wet, it makes my fingers slide so nicely over your skin..."
    s "*huh* {i}Me too, it feels better..."
    pause
    scene ch10_656_23__:
        subpixel True
        zoom 1.01
        align (0.5, 0.5)
        around (0.502, 0.5)
        linear 3.0 counterclockwise circles 1
        around (0.498, 0.5)
        linear 3.0 clockwise circles 1
        repeat
    s "{i}[mc]..."
    mc "{i}Tell me."
    s "{i}You..."
    pause
    s "{i}Y-you've already made me fall in love with you."
    s "{i}So..."
    pause
    s "{i}Y-you have to ask me to be your girlfriend... {w=0.5}O-only if you want..."   
    scene ch10_656_23___:
        subpixel True
        zoom 1.01
        align (0.5, 0.5)
        around (0.502, 0.5)
        linear 2.0 counterclockwise circles 1
        around (0.498, 0.5)
        linear 2.0 clockwise circles 1
        repeat
    s "*Unh...*"
    s "*Uhh* {i}[mc], t-that feels good...."
    mc "{i}(I'm touching her in a place like this...)" with dissolve
    mc "{i}(I can't believe how excited that makes me...)" with dissolve
    pause
    scene ch10_656_32
    pause
    scene ch10_656_33
    pause
    image ch10_656_32anim:
        "ch10_656_32" with dissolve
        1.5
        "ch10_656_33" with dissolve
        1.5
        repeat
    scene ch10_656_32anim
    pause
    s "{i}*Uh, uh* [mc], I feel like I'm going to..."
    mc "{i}Go ahead, don't hold it in..."
    s "*Uh* {i}N-no, I'm going to wet my skirt..."
    s "W-wait, [mc], I really need to pee."
    stop voicefx fadeout 0.1
    play soundfx "audio/pee.mp3" volume 0.5
    show ch10_656_34 with dissolve:
        subpixel True
        xalign 0.5 yalign 1.0
        parallel:
            ease 5 yalign 0.0
        parallel:
            ease 10 zoom 0.75
    s "{i}Uhh... sorry, I couldn't hold it anymore. I drank way too much soda..."
    mc "{i}It's okay."
    s "{i}Uh... I feel better now."
    s "{i}Let me know if anyone comes."
    mc "{i}Don’t worry, I’ll keep watch."
    pause
    play soundfx2 "audio/bottledrop.mp3" volume 0.5
    pause 0.75
    mc "Huh?"
    scene ch10_656_23_10
    s "[mc], did you hear that too?"
    mc "Hey, who's there?"
    scene ch10_656_23_10-
    s "{i}I-it sounded like someone threw a plastic bottle."
    mc "Probably just some idiot trying to be funny."
    mc "Come out, you clown."
    s "{i}B-better let’s go."
    $ clear_audiofx()
    mc "{i}Yeah, better..."
    stop background fadeout 1.0
    scene blackscreen
    $ renpy.end_replay()
    pause
    $ clear_audiofx()
    play background "audio/fairsfx.ogg" volume 0.18 loop fadein 1.0
    scene ch10_657
    pause
    s "Let's go home now, [mc]..."
    scene ch10_658
    mc "You already wanna leave?"
    s "I wanna get back so we can... {w=0.5}{i}you know what."
    mc "We'll have the whole night for that."
    mc "Wanna go on the Ferris wheel and then head out?"
    s "Yeah!"
    scene ch10_659
    mc "Check that out."
    "{b}Step right up! Five tickets, five shots, win big prizes!"
    s "Look at the prize! Giant teddy bears!"
    mc "Wanna give it a shot?"
    s "Yes!"
    scene ch10_660
    "Five shots, five tickets! Pop five balloons, take home the grand prize!"
    mc "{i}(How hard can it be...)" with dissolve
    s "Come on, [mc], you got this!"
    pause
    scene ch10_661
    play sound "audio/balloonpop.ogg"
    s "Nice one, [mc]!"
    scene ch10_662
    play soundfx "audio/balloonpop.ogg"
    pause
    scene ch10_663
    mc "Ah, so close!"
    "Three balloons! You win this little plushie, buddy."
    mc "{i}(I want the big one... I’ve gotta win it for [s]...)" with dissolve
    scene ch10_664
    mc "Five more shots, please."
    "You got it. Five tickets."
    scene ch10_665
    play soundfx "audio/balloonpop.ogg"
    "Four balloons! Just one more and the big prize was yours!"
    mc "I know... Five more!"
    "Here you go, five more."
    scene ch10_666
    mc "Damn it... Gimme another round."
    "You got it!"
    scene ch10_666-
    play soundfx "audio/balloonpop.ogg"
    mc "Yes, one more! I just need one more good shot!"
    scene ch10_667
    mc "Damn..."
    "You were real close, buddy."
    mc "One more round, please."
    scene ch10_668
    s "[mc], my legs are tired. Can we just go now?"
    mc "Don’t you want the big teddy?"
    s "I do, but... [mc], your aim is terrible. We’ll be here all night."
    s "Let me try, okay?"
    mc "Sure, there’s no way you could do worse than me."
    s "Hold these bears for me."
    scene ch10_669
    "Change of plans! The little lady’s stepping up to throw!"
    "Looks like she ran out of patience and wants to win that prize herself!"
    mc "{i}(Her throwing stance isn’t bad...)" with dissolve
    pause
    scene ch10_670
    "She’s taking her time... lining up the shot..."
    pause
    scene ch10_671
    "And here it goes!{w=1.0}{nw}"
    "Aaaayyyaaahhh!" with hpunch
    scene ch10_672 with nothing
    s "S-sorry, sir!"
    "Oh god... *gulp* And I have a phobia of needles"
    s "I-it’s your fault for standing there!"
    mc "Are you okay?"
    scene ch10_673
    "Yeah, I think it didn’t pierce the fabric..."
    mc "{i}(Damn, I’m out of tickets.)" with dissolve
    pause
    scene ch10_674
    mc "[s], can you stay here and keep throwing while I go get more tickets? I used them all up and we still haven’t ridden the Ferris wheel."
    s "Yeah, I’ll wait here."
    mc "Alright, I'll be back in a sec, ok?"
    s "Okay."
    scene ch10_675 with fade
    "Sorry, transaction declined."
    mc "No way... This morning I had nearly eight hundred dollars."
    "Can you check on your phone?"
    scene ch10_676
    mc "What the hell?..."
    pause
    mc "Huh? Five bucks?"
    mc "This has to be a mistake."
    mc "{i}(What did I spend so much money on?)" with dissolve
    mc "{i}(There’s a charge for...)" with dissolve
    mc "{i}(Six hundred and ninety-nine...!)" with hpunch
    mc "{i}(This can’t be right, I need to call the bank, it might be fraud.)" with dissolve
    pause
    s "[mc]."
    scene ch10_678
    mc "Hey, where are the plushies?" #[mc] se gano unos peluches para [s] por tronar globos con dardos.
    s "The attendant’s holding onto them for me."
    mc "You already threw all five darts?"
    s "Yeah. What are you doing?"
    mc "Calling the bank..."
    mc "Wait... When we went to the clothing store you asked me for three hundred, right?"
    mc "I should still have at least two hundred left in my account."
    scene ch10_679
    s "Heh..."
    s "..."
    mc "You... know something about this?"
    scene ch10_680
    pause
    mc "Don’t tell me you..."
    pause
    scene ch10_681
    s "B-but look! It’s a name brand!"
    s "It’s a Vuis Luiton! These bags increase in value over time!"
    mc "[s]..."
    s "Uhm..."
    scene ch10_680
    s "W-well, that’s what the seller told me..."
    mc "[s], you spent my whole week’s salary on that purse..."
    pause
    scene ch10_682
    pause
    s "Sorry... I thought you wouldn’t mind."
    s "Are you mad at me?"
    mc "I’m gonna call [drelat] [d] and see if he can wire me some money."
    s "Don’t worry, I’ve got money. I can pay for everything, okay?"
    s "I’ll pay you back for the purse too!"
    pause
    scene blackscreen
    pause
    scene ch10_683-
    pause
    s "Are you mad?"
    mc "No, I'm fine."
    pause
    scene ch10_684
    s "[mc]..."
    s "You don't sound happy."
    pause
    s "[mc]!"
    scene ch10_685
    s "I'll pay you back, I just need a few days..."
    mc "It's okay. Money comes and goes. (Yeah...)" with dissolve
    pause
    mc "Hey, where are you planning to get all that money to pay me back anyway?"
    scene ch10_686
    s "[drelatks!cl] pays me to spy on you and [k]."
    mc "Wait, what?!" with hpunch
    scene ch10_687
    mc "[s]!"
    s "B-but I don't tell him anything!"
    mc "What do you mean you don't tell him anything? Then why does he pays you?"
    mc "You didn't tell him what you saw today, did you?"
    s "N-no, of course not! I swear!"
    scene ch10_686
    pause
    mc "So... he pays you for gossip?"
    s "[drelatks!cl] gives me money weekly for me to tell him stuff. And if nothing happens, he still gives me money anyway."
    s "I never tell him anything important."
    s "Sometimes I even lie to him so you don't get in trouble..."
    mc "Sometimes?"
    s "When you do things with [k], I tell him I didn't see anything."
    mc "[s]..."
    mc "How do I know I can trust you now?"
    s "Uhm..."
    s "I haven't told him what you and I do..."
    "..."
    mc "T-that's true, but still..."
    scene ch10_687
    s "I promise I won't say anything, really!"
    pause
    mc "{i}(If she had told him something, [drelat] [d] would have already kicked me out.)" with dissolve
    mc "{i}(They say there's no better partner in crime than an accomplice...)" with dissolve
    pause
    mc "O-okay..."
    s "But don't stay mad, when [drelatks] pays me I'll give you back every penny, I swear!"
    mc "I don't want you to pay me back anything, it's my gift to you."
    mc "{i}(I can't be picky right now...)" with dissolve
    scene ch10_686
    s "[mc], I don't know if you knew but the purse cost fifteen hundred."
    mc "F-fifteen hundred? So you put in the other thousand?"
    s "Yeah."
    mc "And where did you get that from?"
    s "From my job!"
    mc "You mean the spying thing?"
    s "He gives me fifty a week and fifteen dollars for each piece of gossip."
    mc "So you've told him, what, like a fifty gossips?"
    s "Uhm, maybe... Some gossips pays more."
    s "Like what I told him at the beach. I went to him with the info that you guys were drinking beer, heh..."
    mc "[s]..."
    scene ch10_687
    s "It's okay, I know what things to tell him. I only tell him stuff that I know won't get you in trouble."
    s "Next time you should tell me first what you're gonna tell him, okay?"
    s "Okay."
    scene ch10_688
    pause
    mc "A thousand dollars..."
    mc "I think you earn better than me..."
    s "It's because I already have years of experience."
    mc "That's true."
label ch10s4:
    if _in_replay:
        play background "audio/fairsfx.ogg" volume 0.18 loop fadein 1.0 
        scene ch10_688
        pause
    mc "Hey, is it just me, or is this skirt really short?"
    scene ch10_689
    s "Oh, {i}it got bunched up when I went to pee, I forgot to pull it down..."
    mc "It's still pretty short..."
    mc "People down there might be able to see your underwear..."
    scene ch10_690
    mc "That's better..."
    image ch10_691anim:
        "ch10_691" with dissolve
        2.0
        "ch10_692" with dissolve
        2.0
        repeat
    scene ch10_691anim
    s "Are you not upset anymore?"
    s "Hm?"
    mc "I was never upset, [s]."
    s "But you weren't happy either..."
    mc "Well, I have to admit I was a little sad."
    s "I'm sorry, [mc]..."
    image ch10_693_1anim:
        "ch10_693_1" with dissolve
        2.0
        "ch10_693_2" with dissolve
        2.0
        repeat
    scene ch10_693_1anim
    pause
    mc "What are you doing?"
    s "Making you happy."
    scene ch10_694
    mc "Uh?..."
    scene ch10_695
    s "{i}There's the bulge... and it's already very hard!"
    mc "{i}Hey..."
    image ch10_696anim:
        "ch10_696" with dissolve
        1.5
        "ch10_696-" with dissolve
        1.5
        repeat
    scene ch10_696anim
    s "{i}[mia] told me that guys really like short skirts."
    s "{i}That's why I wore a really short one for you today."
    mc "{i}What kind of advice you asking her for?..."
    s "{i}*Giggle*"
    pause
    image ch10_697anim:
        "ch10_697" with dissolve
        1.5
        "ch10_698" with dissolve
        1.5
        repeat
    scene ch10_697anim
    pause
    s "{i}I'm your bitch..."
    mc "{i}W-what?"
    mc "{i}Where did you hear that?"
    s "{i}That's what [k] was shouting at [mia]'s house."
    image ch10_699anim:
        "ch10_699_1" with dissolve
        1.5
        "ch10_699_2" with dissolve
        1.5
        repeat
    scene ch10_699anim
    s "*Giggle* {i}I'm your bitch too..."
    mc "*Gulp*"
    mc "{i}H-Hey, you can't just say stuff like that."
    s "Hmm... {i}Your thing is poking me through your pants."
    scene ch10_700
    mc "Uhm..."
    pause
    scene ch10_700_2
    s "{i}That's better..."
    image ch10_700anim:
        "ch10_700_1" with dissolve
        1.5
        "ch10_700_2" with dissolve
        1.5
        repeat
    scene ch10_700anim
    mc "{i}(My hips are already giving in to her teasing...)" with dissolve
    mc "{i}(My cock feels amazing between her warm little buttocks.)"
    s "{i}I'm getting excited again..."
    mc "{i}(Damn, what a girl...)" with dissolve
    pause
    scene ch10_700_3
    mc "{i}(She doesn't care about anything, just enjoying herself...)" with dissolve
    mc "{i}(I don't know if it's because of her innocence or her naughtiness.)" with dissolve
    scene ch10_700_4
    mc "{i}(God, this feels so good...)"
    s "{i}[mc], you're pushing me forward..."
    pause
    image ch10_700_4anim:
        "ch10_700_3" with Dissolve(0.5)
        3.0
        "ch10_700_4" with Dissolve(0.5)
        3.0
        repeat
    scene ch10_700_4anim with Dissolve(0.5)
    pause
    scene ch10_700_4
    mc "{i}(what a fluffy and delicious ass...)" with dissolve
    mc "{i}(It's so hot to see how my penis sinks into the middle of this round little butt...)" with dissolve
    pause
    scene ch10_701-
    s "{i}{size=-3}[mc], If you keep doing that, someone might see you."
    mc "{i}{size=-3}I'm being careful."
    "Hey! You're the girl from the pee-{w=0.5}\n S-sorry, I mean the roller coaster."
    scene ch10_702
    s "Huh? Are you talking to me?"
    "Uhm..."
    scene ch10_703
    "Uh..."
    s "Did you say something to me?"
    "Uhm, y-yeah, I..."
    scene ch10_704
    oliver "Hey, babe. I'm [oliver]."
    s "Hi...?"
    oliver "What's your name?"
    s "I'm [s]."
    oliver "Nice to meet you, [s]. That’s a really pretty name."
    s "Thank you."
    scene ch10_701
    s "{i}{size=-3}Put it here..."
    mc "{i}{size=-3}Where?"
    scene ch10_700_6
    s "{i}Inside my panties. No one will see it there..."
    mc "{i}Good idea..."
    scene ch10_700_7
    mc "{i}Hmm... (This is so fucking hot...)"
    mc "{i}Are you always this wet?"
    s "{i}Am I?"
    mc "{i}Yeah, I can feel it..."
    "Hey bro, what time is it?"
    scene ch10_700_5 with vpunch
    mc "Uh! It's!... uh..."
    mc "Ugh, my watch’s dead."
    oliver "Haha, he’s got a dead watch. What are you, broke?"
    oliver "It’s quarter past nine, bro."
    "Thanks."
    scene ch10_703
    oliver "Hey, girl... uh, [s]."
    s "Yeah?"
    scene ch10_704
    oliver "I've had some really pretty girlfriends before..."
    s "Ah..."
    oliver "Yeah..."
    s "Oh! I remember you now! You're the little guy they let on the roller coaster!"
    s "Is your friend the rotten onion head?"
    scene ch10_703
    oliver "Onion head?"
    scene ch10_704
    oliver "Ah, I know who you're talking about."
    oliver "Nah, I don’t even know that guy."
    jump afterch10_700sthj1_1
init python:
    def ch10_700sthj1_(trans, st, at):
        if store.current_active_animation != "ch10_700sthj1_":
            store.current_active_animation = "ch10_700sthj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_700sthj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_700sthj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 3 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 12 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.5 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_700sthj2_(trans, st, at):
        if store.current_active_animation != "ch10_700sthj2_":
            store.current_active_animation = "ch10_700sthj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_700sthj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_700sthj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 3 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 12 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.5 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_700sthj3_(trans, st, at):
        if store.current_active_animation != "ch10_700sthj3_":
            store.current_active_animation = "ch10_700sthj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_700sthj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_700sthj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 3 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 12 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.5 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed

init python:
    def ch10_700sthj4_(trans, st, at):
        if store.current_active_animation != "ch10_700sthj4_":
            store.current_active_animation = "ch10_700sthj4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 20 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_700sthj4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_700sthj4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 3 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 12 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.3:
                    final_volume = max(0.1, 0.5 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='sound')
                    renpy.sound.play(random_sound, channel='sound')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
screen ch10_700sthj1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.05), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.03), Show("random_speed", max_speed = 0.02, min_speed = 0.05), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        if current_pov == 4:
            textbutton "Pov 4" style "textbutton_choice"
        else:
            textbutton "Pov 4" action Jump("ch10_700sthj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice"
        else:
            textbutton "Pov 3" action Jump("ch10_700sthj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice"
        else:
            textbutton "Pov 2" action Jump("ch10_700sthj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice"
        else:
            textbutton "Pov 1" action Jump("ch10_700sthj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("aftersdch10_700sthj1_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label ch10_700sthj1_:
    $ current_pov = 1
    scene ch10_700sthj1_
    call screen ch10_700sthj1_  
label ch10_700sthj2_:
    $ current_pov = 2
    scene ch10_700sthj2_
    call screen ch10_700sthj1_  
label ch10_700sthj3_:
    $ current_pov = 3
    scene ch10_700sthj3_
    call screen ch10_700sthj1_  
label ch10_700sthj4_:
    $ current_pov = 4
    scene ch10_700sthj4_
    call screen ch10_700sthj1_  
image ch10_700sthj1_:
    function ch10_700sthj1_
image ch10_700sthj2_:
    function ch10_700sthj2_
image ch10_700sthj3_:
    function ch10_700sthj3_
image ch10_700sthj4_:
    function ch10_700sthj4_
label afterch10_700sthj1_1:
    $ hide_anim_speed()
    $ anim_speed = 0.03
    scene ch10_700sthj1_
    oliver "My dad's friends with the guy who owns this place. That’s why I get on all the rides for free."
    oliver "If you want, I can ask that guy to let you ride the roller coaster with me."
    s "*huh* {i}Thanks, but no, I can’t right now..."
    pause
    scene ch10_703:
        subpixel True
        zoom 1.01
        parallel:
            align (0.5, 0.5)
            around (0.502, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.498, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            repeat
    oliver "Is this guy with you your [srelatmc]?"
    s "*huh* Who...?"
    oliver "The guy who's hugging you."
    scene ch10_700sthj4_
    s "His name is [mc] and he's my... *huh*"
    mc "{i}{size=-3}Tell him I'm your boyfriend so he'll leave..."
    s "*Uh* H-he's my boyfriend."
    oliver "Your boyfriend?"
    oliver "Nah, he's too old for you."
    pause
    scene ch10_700sthj2_
    oliver "I-is he really your boyfriend?"
    oliver "No way, he's probably your brother or something."
    oliver "Why are you lying, huh?"
    pause
    scene ch10_700sthj3_
    oliver "Hey, I'm talking to you."
    oliver "Are you going to ride the ferris wheel?"
    oliver "If you come with me you won't have to wait in line, I have a fast pass."
    s "{i}*Huh, hmm*"
    oliver "Are you new here? I've never seen you before."
    s "*uh* {i}{size=-3}[mc], this guy won't leave..."
    mc "{i}{size=-3}Just let him talk, he'll leave when he gets bored."
    call screen ch10_700sthj1_ with dissolve
label aftersdch10_700sthj1_:
    oliver "Hey, w-why are you hugging her like that? What are you doing to her?"
    pause
    image ch10_710_1anim:
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.5

        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.5

        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.05
        "ch10_710_1"
        0.05
        "ch10_710_2"
        0.5

        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.5

        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.1
        "ch10_710_1"
        0.1
        "ch10_710_2"
        0.5
        repeat
    scene ch10_708:
        subpixel True
        zoom 1.01
        parallel:
            align (0.5, 0.5)
            around (0.502, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.498, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            repeat 
    s "{i}He's still there..."
    scene ch10_709:
        subpixel True
        zoom 1.01
        parallel:
            align (0.5, 0.5)
            around (0.502, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.498, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            ease 0.5 zoom 1.015
            ease 0.5 zoom 1.01
            repeat 
    s "{i}Maybe if you kiss me, he'd believe you're really my boyfriend and leave..."
    s "{i}U-unless you don't want to..."
    s "{i}J-just a little one, if you want..."
    play sound kissing volume 0.2 loop
    play soundfx kissing2 volume 0.2 loop
    image ch10_707_anim:
        "ch10_707_1" with dissolve
        1.5
        "ch10_707_2" with dissolve
        1.5
        "ch10_707_1" with dissolve
        1.5
        "ch10_707_2" with dissolve
        1.0
        "ch10_707_1" with dissolve
        1.0
        "ch10_707_2" with dissolve
        0.75
        "ch10_707_1" with dissolve
        0.75
        "ch10_707_2" with dissolve
        1.5
        repeat
    scene ch10_707_anim
    s "*Hm, smch* {i}hmm..."
    oliver "Hey, w-what are you doing?"
    pause
    image ch10_705anim:
        "ch10_705" with dissolve
        1.5
        "ch10_706" with dissolve
        1.5
        repeat
    scene ch10_705anim
    oliver "Uh..."
    oliver "T-that doesn't make you his girlfriend, anyone could give you a kiss, even me!..."
    pause
    oliver "Y-you're not that pretty anyway..."
    scene ch10_712
    pause
    scene ch10_713
    pause
    scene ch10_714
    oliver "Eh..."
    pause
    scene ch10_715 with Dissolve(0.25):
        zoom 1.05 xalign 0.5 yalign 0.5
        
        linear 0.2 zoom 1.1
        
        easeout 0.15 zoom 1.0
        
        easeout 0.1 zoom 1.075
        
        easeout 0.05 zoom 1.05
    pause
    oliver "It's that a...?"
    scene ch10_716 with nothing
    oliver "...You're a guy."
    $ renpy.pause(2.0, hard=True)
    scene ch10_716-
    pause
    scene ch10_710_1anim
    stop sound
    stop soundfx
    $ clear_audiofx()
    play voicefx smoansoft volume 0.5 loop
    s "*huh, uhmm*..."
    mc "{i}{size=-3}¿Are you cumming?..."
    s "*Uh, hmm*..."
    pause
    scene ch10_711
    stop voicefx fadeout 0.1
    s "{i}Unh..."
    s "{i}[mc], hmn..."
    mc "{i}(I can feel her fluids running down my cock.)" with dissolve
    pause
    scene ch10_708
    s "{i}I came."
    mc "{i}Yeah, I noticed..." 
    scene ch10_709
    s "{i}It's running down my legs..."
    s "{i}People are already getting off the ferris wheel."
    scene ch10_717
    s "Hurry up, let’s go."
    mc "W-wait..."
    stop background fadeout 1.5
    scene blackscreen
    $ renpy.end_replay()
    pause
label ch10s5:
    if _in_replay:
        scene blackscreen
        pause 0.5
    play background "audio/fairsfx.ogg" volume 0.1 loop fadein 1.0
    scene ch10_718 
    s "We're almost level with that building."
    mc "Yeah, we're pretty high up."
    pause
    scene ch10_719
    s "I like your cologne."
    s "Did you shower properly like I told you to?"
    mc "Yeah, I did..."
    scene ch10_732
    s "[mc]..."
    s "{i}Do you wanna kiss?"
    mc "Yeah."
    image ch10_729anim:
        "ch10_729" with dissolve
        1.5
        "ch10_730" with dissolve
        1.5
        repeat
    play soundfx kissing2 volume 0.35 loop
    play sound kissing volume 0.35 loop
    scene ch10_729anim
    s "*Hmm, smch*"
    mc "*Smch* {i}Wrap your tongue around mine..."
    s "*Muah, alh, mch*"
    pause
    stop sound fadeout 0.25
    stop soundfx fadeout 0.25
    scene ch10_732
    mc "Touch me here..."
    s "Your bulge is really showing."
    scene ch10_733
    mc "Squeeze it..."
    pause
    image ch10_734anim:
        "ch10_734" with dissolve
        1.5
        "ch10_735" with dissolve
        1.5
        repeat
    scene ch10_734anim
    s "It's pulsing..."
    pause
    image ch10_737anim:
        "ch10_736" with dissolve
        1.5
        "ch10_737" with dissolve
        1.5
        repeat
    scene ch10_737anim
    s "It's really hard."
    mc "Keep massaging it..."
    image ch10_738anim:
        "ch10_738" with dissolve
        1.0
        "ch10_739" with dissolve
        1.0
        repeat
    play soundfx kissing2 volume 0.15 loop
    play sound kissing volume 0.15 loop
    scene ch10_738anim
    s "*Muah, mlah*..."
    pause
    stop sound fadeout 0.5
    stop soundfx fadeout 0.5
    scene ch10_737anim
    s "What's wrong?"
    mc "Nothing, I'm just keeping an eye out."
    s "Why?"
    pause
    scene ch10_740
    mc "{i}For this..."
    s "{i}You took you dick out!"
    mc "{i}I'm so horny that it's uncomfortable to have it inside my pants."
    s "{i}That always happens to you."
    mc "{i}It needs some kisses..."
    scene ch10_741
    s "{i}Kisses or licks?"   
    mc "{i}Uhmm... {w=0.5}both."
    s "{i}And sucks! Do you want me to suck it here?"
    mc "{i}Yeah, just a little to calm it down."
    scene ch10_740
    s "Okay."
    scene ch10_742
    mc "Uh, yeah..."
    pause
    image ch10_734_anim:
        "ch10_743_1-" with Dissolve(0.5)
        0.75
        "ch10_743_2" with Dissolve(0.5)
        0.75
        "ch10_743_3" with Dissolve(0.5)
        0.75
        "ch10_743_2-" with Dissolve(0.5)
        0.75
        repeat
    scene ch10_734_anim
    play soundfx kissing2 volume 0.2 loop
    s "*Luah, lah*..."
    mc "That's it... get a little saliva on the tip."
    s "*Lah* {i}It's pulshing a lot."
    mc "{i}That's because you're licking it so well."
    pause
    image ch10_743_4anim:
        "ch10_743_4" with Dissolve(0.5)
        0.8
        "ch10_743_4-" with Dissolve(0.5)
        0.8
        "ch10_743_5" with Dissolve(0.5)
        0.8
        repeat
    image ch10_744_2anim:
        "ch10_744_3" with Dissolve(0.5)
        0.8
        "ch10_744_2" with Dissolve(0.5)
        0.8
        repeat
    scene ch10_743_4anim
    play soundfx kissing2 volume 0.35 loop
    mc "Uh... move your tongue around the head..."
    s "*Lah, lah* {i}Do you wan' me to shuck it now?"
    mc "Keep licking the tip a little longer..."
    pause
    mc "Or do you wanna suck it now?"
    scene ch10_744_2anim
    s "Yeah... I like sucking better."
    mc "Oh yeah?"
    s "*Lah-lah-lah* {i}Uh-hum..."
    scene ch10_743_4anim
    s "*Blah, lah* {i}It just feels more exciting to suck it."
    mc "I see..."
    mc "Alright then, suck it however you want..."
    stop soundfx fadeout 0.5
    scene ch10_743sbj1_
    mc "{i}Uh..."
    mc "{i}Oh yeah... I can tell you really like sucking it."
    s "*Chup, slurp* {i}{size=-3}Am I doing it right?"
    mc "{i}Yeah... you're doing great..."
    mc "{i}You're being really attentive with your tongue..."
    s "*Slurp, slsh* {i}{size=-3}I'm swirling it all around..."
    mc "{i}Y-yeah... *uh* That feels so good..."
    pause
    mc "{i}Hold on a sec, [s]."
    image ch10_744_5anim:
        "ch10_744_5" with Dissolve(0.5)
        0.8
        "ch10_744_4" with Dissolve(0.5)
        0.8
        repeat
    scene ch10_744_5anim
    s "{i}Why? {/i}-*Lah, lah, lah*"
    mc "W-wait, we're about to go under..."
    scene ch10_747
    mc "{i}Just act like nothing's happening."
    s "{i}Okay."
    mc "{i}You can only suck me when we're up high, okay?"
    mc "{i}Once we go back up, you can keep going..."
    s "{i}Okay."
    pause
    scene ch10_746:
        subpixel True
        zoom 1.005
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    s "We're going up again."
    mc "{i}Wait a little until we're higher..."
    pause
    s "Can I suck it now?"
    mc "Yeah... now you can."
    scene ch10_745:
        subpixel True
        zoom 1.005
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    s "*Chup* {i}It’sh really shlippery..."
    mc "{i}Slippery? *uh*"
    s "{i}Yeh... my tongue keeps sliding all over the tip of your penish..."
    mc "Y-yeah... *uh* I can feel it..."
    scene ch10_743sbj3_:
        subpixel True
        zoom 1.005
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    s "*Slurp, shup* {i}{size=-3}Hmm..."
    mc "{i}So innocent... and yet so horny..." with dissolve
    mc "{i}How does my duck taste, huh? Taste good?"
    s "*Chup, chup* {i}{size=-3}Hm-hmm..."
    pause
    mc "{i}Uh... your little lips feel so good..."
    mc "{i}I love how you wrap them around the tip of my dick, so gently..."
    pause
    mc "{i}Let's pause for a second, we're already going down."
    scene ch10_747
    s "{i}*Giggle*"
    mc "{i}What are you giggling at?"
    s "{i}People have no idea what we're doing..."
    mc "{i}You find that funny?"
    s "{i}Yeah, *giggle*."
    mc "{i}Me too."
    s "{i}*Chuckle*{w=1.0}{nw}"
    s "{i}We're going back up..."
    scene ch10_748
    pause
    mc "{i}Everything looks so small from here."
    mc "{i}People are starting to leave, it's late."
    scene ch10_743sbj2_
    s "*Slurp, suck* {i}{size=-3}Hmm..."
    mc "That's it, suck it good, keep using lots of saliva..."
    $ pov = 2
    call screen ch10_743sbj2_ with dissolve


screen ch10_743sbj1_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.026), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.026), Show("random_speed", max_speed = 0.015, min_speed = 0.04), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_743sbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_743sbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_ch10_743sbj1_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch10_743sbj2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.026), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.026), Show("random_speed", max_speed = 0.015, min_speed = 0.04), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch10_743sbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_743sbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_ch10_743sbj1_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch10_743sbj3_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.026), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.026), Show("random_speed", max_speed = 0.015, min_speed = 0.04), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch10_743sbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch10_743sbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Jump("ch10_ch10_743sbj1_"), Function(hide_anim_speed)] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1

    def ch10_743sbj3_(trans, st, at):
        if store.current_active_animation != "ch10_743sbj3_":
            store.current_active_animation = "ch10_743sbj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_743sbj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_743sbj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.2:
                    final_volume = max(0.1, 0.45 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='voicefx')
                    renpy.sound.play(random_sound, channel='voicefx')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.65 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_743sbj2_(trans, st, at):
        if store.current_active_animation != "ch10_743sbj2_":
            store.current_active_animation = "ch10_743sbj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_743sbj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_743sbj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.2:
                    final_volume = max(0.1, 0.3 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='voicefx')
                    renpy.sound.play(random_sound, channel='voicefx')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_743sbj1_(trans, st, at):
        if store.current_active_animation != "ch10_743sbj1_":
            store.current_active_animation = "ch10_743sbj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_743sbj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_743sbj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if random_chance < 0.2:
                    final_volume = max(0.1, 0.7 * fade_multiplier)
                    renpy.sound.set_volume(final_volume, channel='voicefx')
                    renpy.sound.play(random_sound, channel='voicefx')
                    store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_50.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg", "audio/wavs/bj_67.ogg", "audio/wavs/bj_22.ogg", "audio/wavs/bj_39.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def update_anim_speed(value):
        store.anim_speed = value
image ch10_743sbj3_:
    function ch10_743sbj3_
image ch10_743sbj2_:
    function ch10_743sbj2_
image ch10_743sbj1_:
    function ch10_743sbj1_

default pov = 0  
label ch10_743sbj1_:
    $ pov = 1
    scene ch10_743sbj1_ with Dissolve(0.2)
    call screen ch10_743sbj1_ 
label ch10_743sbj2_:
    $ pov = 2
    scene ch10_743sbj2_ with Dissolve(0.2)
    call screen ch10_743sbj2_ 
label ch10_743sbj3_:
    $ pov = 3
    scene ch10_743sbj3_ with Dissolve(0.2)
    call screen ch10_743sbj3_ 


label ch10_ch10_743sbj1_:
    if pov != 2:
        scene ch10_743sbj2_
    $ anim_speed = 0.015
    mc "*Oh*... *hmh*..."
    s "*Slurp, chup, slurp*"
    mc "W-wait, [s]..."
    "{w=1.0}{nw}" with vpunch
    pause
    scene ch10_732
    s "W-what happened?"
    mc "I think they're already letting people off."
    s "[mc], when we get home, can I sleep over in your room?"
    mc "Sure. Actually, I was goinna ask you that."
    s "Really?"
    mc "Yeah, I don't want to sleep tonight."
    s "Why? Do you have insomnia?"
    mc "Something like that."
    scene ch10_737
    pause
    mc "They're taking forever to let people off. We haven't moved."
    s "{i}Take your dick out, [mc]..."
    scene ch10_738anim
    mc "{i}Hey, save some kisses for me too."
    s "*Giggle* {i}Okay, okay. I'll give you kisses too. {/i}*Mahl, msch*"
    pause
    scene ch10_720
    pause
    mc "What's wrong?"
    s "My panties are soaked."
    s "I feel uncomfortable."
    scene ch10_721
    mc "Got any tissues in your bag?"
    s "Used them all already."
    mc "Spread your legs, let me see..."
    scene ch10_722
    mc "You're completely soaked."
    s "I told you..."
    mc "We have to take them off."
    scene ch10_723
    s "Am I going to have to walk around without panties?"
    mc "I don't think there's another choice."
    mc "You keep them in your bag."
    s "N-no! Not in my bag!"
    mc "Okay, I'll keep them for you."
    mc "How did you get so wet?"
    s "When we were lined up and you started sliding your penis between my legs, you made me come."
    scene ch10_731
    mc "{i}It was your idea to put it there."
    s "True..."
    s "I-I'm just a very horny girl, [mc]..."
    mc "Did you get very excited when I slid my penis between your legs?"
    s "Yeah, even with all those people around... {w=0.5}{i}Good thing no one saw us."
    mc "{i}I know. I got so turned on too, you were moving your ass so sexy..."
    s "{i}Do you really think I’m sexy?"
    mc "Of course I do."
    play soundfx kissing volume 0.3 loop
    scene ch10_729anim
    play sound kissing2 volume 0.3 loop
    s "*Hmch, smch*"
    pause
    image ch10_749anim:
        "ch10_749" with dissolve
        1.5
        "ch10_750" with dissolve
        1.5
        repeat
    image ch10_753anim:
        "ch10_752" with dissolve
        1.5
        "ch10_753" with dissolve
        1.5
        repeat
    scene ch10_749anim
    s "*Lah, muah* {i}Your fingers feel so good..."
    s "*Uh, smch* {i}[mc], if you keep massaging my pussy, I’m gonna pee again..."
    pause
    $ stop_sounds(0.5)
    scene ch10_753anim
    mc "A little pee doesn’t bother me at all."
    mc "[s], you’ve got to take these panties off."
    s "{i}Okay..."
    mc "{i}I want to lick you there..."
    scene ch10_751
    s "I don’t want to today, [mc]..."
    mc "Why? Don’t you feel like it?"
    s "N-no, it’s not that... it’s just that I want..."
    s "I want you and me to..."
    pause
    mc "Hm?"
    s "A-are you never gonna ask me to be your girlfriend?"
    mc "Eh, my girlfriend?"
    s "It’s just that..."
    s "[mia] said that [k] is your girlfriend..."
    mc "She said that?"
    s "A-are you never gonna ask me to be your girlfriend?"
    mc "[k] and I aren’t really boyfriend and girlfriend, [s]. Don’t listen to what [mia] says."
    mc "Besides, you’re already my favorite [srelat] who I love very much. That’s better than being my girlfriend."
    s "You don’t treat me the same as [k]..."
    s "And don’t say it’s not true because I already noticed."
    mc "Noticed what?"
    s "You hug and kiss [k] differently than you do me, like you’re in love..."
    s "And you have sex with her..."
    s "{i}Boyfriends and girlfriends do sex..."
    mc "We’re not really boyfriend and girlfriend, [s]."
    s "No?"
    mc "It’s... it’s just for fun, that’s all."
    mc "It’s fake."
    s "Fake?"
    s "Like with [mia]?"
    mc "Yeah."
    s "Then I wanna be your fake girlfriend too!" with hpunch
    s "{i}{size=-2}I-I want to make love with you..."
    pause
    scene ch10_754
    mc "Let’s take these off."
    s "[mc]..."
    mc "You’ve got to take them off."
    s "But you still haven’t answered me..."
    scene ch10_755
    mc "Hey, what are you doing?"
    s "Answer me..."
    scene ch10_756
    mc "Hey..."
    mc "[s], that’s dangerous..."
    s "Then hold me tight."
    scene ch10_758
    mc "[s], be careful."
    s "It’s okay, I’m just gonna sit on it for a little while..."
    scene ch10_760
    pause 0.5
    scene ch10_760-
    pause 0.5
    scene ch10_760--:
        subpixel True
        zoom 1.005
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    mc "Sit on it?"
    s "On your dick..."
    scene ch10_759
    s "I-I'm not going to put it in, I just want to feel it a little."
    s "I want to rub it against my pussy... Can I?"
    mc "Just rubs?"
    s "Yes."
    mc "{i}(I know where this is going, and I still accept it...)" with dissolve
    mc "{i}(I'm such a hypocrite...)" with dissolve
    pause
    $ anim_speed = 0.025
    play voicefx smoansoft volume 0.5 loop
    scene ch10_757grnd2_ with dissolve
    pause
    s "*Uh* {i}It slides really well, doesn't it?"
    s "{i}I put a lot of saliva on it."
    mc "B-be careful..."
    s "Careful?"
    mc "You know, it could... *gulp* {w=0.75}it could accidentally go in..."
    s "And... *huh* {i}If it accidentally goes in, would you be mad at me?"
    mc "Accidentally?"
    mc "W-well, if it accidentally goes in, it would be very bad... You understand that, right?"
    image ch10_761_1anim:
        "ch10_761_1" with Dissolve(0.2)
        0.35
        "ch10_761_2" with Dissolve(0.2)
        0.35
        "ch10_761_3" with Dissolve(0.2)
        0.35
        "ch10_761_4" with Dissolve(0.2)
        0.35
        repeat
    scene ch10_757grnd1_ 
    s "If it went in, would you like it?"
    mc "N-no... -I don't know..."
    s "Would you forgive me if that happens?"
    mc "Are you apologizing in advance? Don't even think of doing it..."
    s "*Giggle*{w=0.75}{nw}"
    s "I won't do it..."
    pause
    s "{i}It feels really good, doesn't it?"
    scene ch10_761_1anim
    mc "{i}Y-yeah..."
    s "{i}I don't know why I feel so eager to do these things..."
    s "{i}I think it's because I like getting excited. Do you like getting excited too?"
    mc "{i}Of course, everyone does..."
    scene ch10_757grnd2_
    s "{i}How does my vagina feel? Does it feel good?"
    mc "{i}Very good..."
    s "{i}Your dick feels very good too, I don't know why it makes me so horny..."
    pause
    s "{i}The good thing is that we're still not moving, so we have more time to do this."
    mc "{i}Yeah..."
    pause
    $ current_pov = 2
    call screen ch10_757grnd_
    




default current_pov = 0

screen ch10_757grnd_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed = 0.015, min_speed = 0.04), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_757grnd2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_757grnd1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("contch10_757grnd1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label ch10_757grnd1_:
    $ current_pov = 1
    scene ch10_757grnd1_ with Dissolve(0.2) 
    call screen ch10_757grnd_ 
label ch10_757grnd2_:
    $ current_pov = 2
    scene ch10_757grnd2_ with Dissolve(0.2) 
    call screen ch10_757grnd_ 
label contch10_757grnd1_:
    image ch10_762anim:
        "ch10_762" with dissolve
        1.5
        "ch10_762-" with dissolve
        1.5
        "ch10_762" with dissolve
        1.5
        "ch10_762-" with dissolve
        1.5
        "ch10_762" with dissolve
        1.5
        "ch10_763" with dissolve
        1.5
        "ch10_762" with dissolve
        1.5
        "ch10_762-" with dissolve
        1.5
        repeat
    scene ch10_762anim:
        subpixel True
        zoom 1.01 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.503, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.497, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 1.5 zoom 1.02
            ease 1.5 zoom 1.01
            ease 1.5 zoom 1.02
            ease 1.5 zoom 1.01
            repeat
    $ hide_anim_speed()
    s "*Huh* {i}It won't go in..."
    mc "Are you...?"
    mc "N-no, [s], don't even try."
    s "Why?"
    s "What does [k] have that I don't? Why do you love her and not me?"
    s "I'm pretty too, aren't I?"
    mc "Of course you are."
    s "But you still don’t love me..."
    mc "Don't say that. Of course I love you."
    mc "You're so sweet and beautiful, like an angel..."
    mc "And that’s exactly why we can’t... It wouldn’t be right."
    mc "You should be thinking about other things, not... {w=0.5}sex."
    mc "Do you understand?"
    s "Even if you say that..."
    s "I think about sex all the time, [mc]."
    s "Every night before I fall asleep, I picture you naked next to me, and I feel like touching myself..."
    s "And I do it until I pass out."
    s "And then in the morning, I think about you again, your hard dick in my mouth, and I feel like touching myself again."
    s "That’s why I’m always late for breakfast."
    mc "S-stop, [s]. This isn’t right."
    s "If it's not right... then why can’t I stop thinking about it?"
    mc "..."
    pause
    mc "{i}(There are a thousand ways I could answer that, and yet...)" with dissolve
    mc "{i}(I just can't bring myself to say any of them.)" with dissolve
    mc "{i}(Maybe deep down, I’m just waiting for a good enough excuse to give in.)" with dissolve
    mc "{i}(Because the truth is... it would be like a dream... a sweet, forbidden dream...)" with dissolve
    stop voicefx fadeout 0.1
    scene ch10_764
    pause
    scene ch10_765 
    s "We're moving now."
    image ch10_726anim:
        "ch10_726" with dissolve
        1.0
        "ch10_727" with dissolve
        1.0
        repeat
    image ch10_725-anim:
        "ch10_724" with dissolve
        1.0
        "ch10_724-" with dissolve
        1.0
        "ch10_725" with dissolve
        1.0
        "ch10_725-" with dissolve
        1.0
        "ch10_725" with dissolve
        1.0
        "ch10_725-" with dissolve
        1.0
        "ch10_725" with dissolve
        1.0
        "ch10_724-" with dissolve
        1.0
        "ch10_724" with dissolve
        1.0
        "ch10_725-" with dissolve
        1.0
        "ch10_725" with dissolve
        1.0
        "ch10_725-" with dissolve
        1.0
        "ch10_725" with dissolve
        1.0
        repeat
    scene ch10_726anim with hpunch
    play sound kissing volume 0.2 loop
    play soundfx kissing2 volume 0.3 loop
    s "Hmmm... *smch*"
    pause
    scene ch10_725-anim
    s "[mc]... *muah, smch*"
    pause 
    "Hey, time's up."
    stop sound 
    scene ch10_728
    stop soundfx
    s "[mc], he's talking to us..."
    "Come down now, please."
    scene ch10_766
    mc "Yeah, sorry."
    s "[mc], remember we have to go for my teddy bears."
    mc "Right, let’s go."
    scene blackscreen
    $ renpy.end_replay()
    pause
    scene ch10_766-
    s "Thank you."
    "Thanks for the tip."
    "Oh, wait a second."
    scene ch10_766--
    "You guys are the ones who did like ten rounds, right?"
    "Give me ten dollars and I'll give you the big bear you want, deal?"
    s "Really?"
    "Yeah, the fair's leaving anyway and these bears get lost or mistreated on the way."
    scene ch10_766---
    s "[mc], please."
    mc "Sorry, [s]. I don't have any cash left..."
    scene ch10_766----
    s "Right, I forgot..."
    s "Which one do you like best?"
    mc "Me?"
    s "Yes, I have money."
    mc "Choose the one you like best."
    s "I want the one you want..."
    mc "No, you choose."
    s "No, you."
    scene ch10_766-----
    "I'll give you this one, since you can't decide."
    "If he says no, I'm going to get pissed..."
    s "Thank you!"
    scene ch10_767 with fade
    mc "I had a lot of fun today."
    s "Me too."
    mc "It’s been a while since I laughed this much."
    s "Yeah... I didn’t want the day to end."
    mc "We should do stuff like this more often."
    s "But just the two of us!"
    mc "Yeah."
    scene ch10_768
    s "[mc], can I hold the teddy bear for a moment?"
    mc "Sure."
    pause
    scene ch10_769
    mc "It's heavy."
    s "D-do you want to be my boyfriend?"
    pause
    "..."
    scene ch10_772
    pause
    s "I-I mean, be my fake boyfriend..."
    s "Like you're pretending to be with [k]..."
    s "And just for tonight..."
    $ renpy.pause(0.5, hard=True)
    scene ch10_771
    $ renpy.pause(1.5, hard=True)
    scene ch10_772
    $ renpy.pause(1.0, hard=True)
    s "I-I thought about it, and I think it's a good idea."
    s "T-That way, if you see that I'm a bad girlfriend, it wouldn't matter because tomorrow I wouldn't be your girlfriend anymore...)"
    mc "{i}(It went in one ear and out the other...)" with dissolve
    scene ch10_771
    $ renpy.pause(1.5, hard=True)
    scene ch10_772
    $ renpy.pause(1.0, hard=True)
    s "I would be a good girlfriend..."
    mc "{i}(She didn't understand anything I explained to her.)" with dissolve
    s "I don't want to bother you with this anymore..."
    mc "{i}(She’s definitely going to ''bother'' me more about it.)" with dissolve
    scene ch10_771
    $ renpy.pause(1.5, hard=True)
    scene ch10_772
    $ renpy.pause(1.0, hard=True)
    s "A-aren't you going to answer me?"
    mc "{i}(In the end, she just likes me, that’s all that matters to her.)" with dissolve
    scene ch10_770
    s "[persistent.name[0]]-[persistent.name], I'm getting tired..."
    scene ch10_773
    s "Uh!"
    pause
    scene ch10_774
    pause 1.0
    scene ch10_775
    s "[mc]."
    mc "Okay."
    mc "Today I'll be your boyfriend... {w=0.75}{i}your real boyfriend."
    s "My real boyfriend?"
    s "[mc]..."
    s "So we're boyfriend and girlfriend now?"
    mc "For today, yes."
    s "{i}For today..."
    s "[mc], I'm so happy..."
    scene ch10_776
    mc "Let's go now."
    s "[mc], wait! [mc], I'm wearing heels!"
    mc "Do you want me to carry you?"
    $ renpy.start_predict("ch10_777blurred")
    s "If you want..."
    scene ch10_777-
    s "You're so strong..."
    mc "You have a very strong boyfriend."
    s "Yeah..."
    s "You're getting tired, don't lie."
    mc "But you're super light."
    s "Hmm... I bet you can’t carry both the teddy bear and me at the same time."
    mc "I can, no problem."
    s "You’re just saying that."
    image ch10_777blurred = im.Blur("images/scenes/ch10/ch10_777-------.webp", 10)
    scene ch10_777blurred:
        zoom 0.55
        xalign 0.5 yalign 0.5
    pause 0.5
    scene ch10_777-------:
        subpixel True       
        zoom 0.55 xalign 0.5 yalign 0.5
        ease 20 zoom 0.5
        ease 20 zoom 0.55
        repeat
    s "Aieee!"
    mc "{i}(She's pretty light, I just lift her in the air with just one hand...)" with dissolve
    scene ch10_777-- with cumming:
        subpixel True
        zoom 1.0 xalign 0.55 yalign 1.0
        ease 6 yalign 0.0
        ease 2 yalign 0.5 zoom 1.1
        pause 1.0
        ease 1 yalign 0.5 zoom 0.5
    $ renpy.pause(3.0, hard=True)
    pause
    scene ch10_777----:
        zoom 0.75 xalign 0.5 yalign 0.5
        linear 0.2 zoom 0.83
        easeout 0.15 zoom 0.75
        easeout 0.1 zoom 0.78
        easeout 0.05 zoom 0.75
    $ renpy.pause(1.0, hard=True)
    mc "{i}(Eh...)" with dissolve
    scene ch10_777----- with vpunch
    s "[mc], you dummy!"
    mc "{i}Sorry, I forgot you're wearing a skirt."
    mc "{i}Aren't you wearing any underwear?"
    scene ch10_777--------
    s "Silly, you took them off. You said you were going to keep them for me."
    mc "{i}Right!"
    mc "{i}Sorry, I'll buy you some new ones."
    s "Why? Did you leave them?"
    s "Do you know they cost me five hundred dollars?"
    scene ch10_777
    mc "R-really?"
    s "Nope."
    mc "You silly..."
    s "*Giggle* {w=1.0}{nw}"
    stop background fadeout 1.5
    scene blackscreen 
    pause
    play music scene1 fadein 1.5
    scene ch10_778:
        zoom 0.75
    a "Oh, you got so many teddy bears!"
    s "We won them at the fair."
    a "Did you have a lot of fun?"
    s "Yes, a lot!"
    a "Aww, you two look so cute."
    scene ch10_779:
        zoom 0.75
    a "Stay there, I'm going to take a picture of you."
    a "Aww..."
    a "Say cheese!"
    scene ch10_780:
            zoom 0.75
    s "W-well, I'm really sleepy now, and [mc] is too."
    a "Good night."
    a "I... will be upstairs."
    a "I'll sleep on the couch again in case you need anything, [mc]."
    s "-Yeah, thank you, good night!"
    stop music fadeout 1.5
    scene blackscreen
    pause
label ch10s6:
    play music sexy3 fadein 1.5
    scene ch10_781 with Dissolve(1.5)
    s "Quick, [mc]..."
    mc "I'm coming, don't be impatient. I'm locking the door now..."
    pause
    scene ch10_783
    mc "Ready?"
    s "{i}I was waiting for you."
    mc "{i}Sorry, [drelat] [d] asked me to put the car in the garage."
    mc "{i}Lift up your skirt, I want to see that cute little ass naked."
    scene ch10_784
    mc "That's it, very good..."
    s "{i}What are you going to do to me? *giggle*"
    mc "{i}I don't know yet. What do you feel like?"
    s "{i}Can the gluttonous shark come out?"
    mc "{i}Ah, you want the shark to eat you whole?"
    s "{i}Yes, I do."
    scene ch10_785_1
    play soundfx kissing2 volume 0.3 fadein 1.0 loop
    mc "*Hmm, muah*"
    scene ch10_785_2
    s "*Giggle*{w=0.65}{nw}"
    s "{i}Oh, the shark is eating me... {/i}*te-he*"
    image ch10_785anim:
        "ch10_785_1" with dissolve
        2.0
        "ch10_785_2" with dissolve
        2.0
        repeat
    scene ch10_785anim
    $ disable_even_frames()
    s "{i}You're covering my whole butt with your drool..."
    mc "*Hm, smch* {i}It's just that you're so tasty..."
    s "*Giggle*{w=1.0}{nw}"
    mc "*Hmmph* {i}So delicious..."
    jump ch10afetr12187

init python:
    def ch10_757grnd2_(trans, st, at):
        if store.current_active_animation != "ch10_757grnd2_":
            store.current_active_animation = "ch10_757grnd2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_757grnd2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_757grnd2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_757grnd1_(trans, st, at):
        if store.current_active_animation != "ch10_757grnd1_":
            store.current_active_animation = "ch10_757grnd1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_757grnd1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_757grnd1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            elif store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

image ch10_757grnd2_:
    function ch10_757grnd2_
image ch10_757grnd1_:
    function ch10_757grnd1_

init python:
    store.frame_num = 1
    store.anim_speed = 0.1
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    store.start_time = 0.0
    store.last_anim_speed = store.anim_speed
    store.current_active_animation = ""
    store.fade_in_counter = 0
    store.fade_in_active = True
    store.sound_played_this_cycle = False
    store.prev_frame_num = 1

    def ch10_788scl1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_788scl1_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_788scl2_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_788scl2_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_788scl3_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_788scl3_{}".format(store.frame_num))
        return store.anim_speed
screen ch10_788scl_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        # Pov 2 - se desactiva si current_pov es 2
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [SetVariable("current_pov", 3), Jump("ch10_788scl3_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        # Pov 2 - se desactiva si current_pov es 2
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_788scl2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        # Pov 1 - se desactiva si current_pov es 1
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_788scl1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("ch10_788scl1_cont")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    
image ch10_788scl1_:
    function ch10_788scl1_
image ch10_788scl2_:
    function ch10_788scl2_
image ch10_788scl3_:
    function ch10_788scl3_
label ch10afetr12187:
    stop soundfx
    scene ch10_787_1
    stop sound
    mc "{i}Uh, what a nice ass..."
    s "{i}Te-he, I'm getting excited, how about you?"
    mc "{i}I was already excited before."
    s "{i}[mc], I want the shark to eat my pussy now..."
    scene ch10_789
    s "{i}Aeeh! *giggles*..."
    $ audio_fade()
    mc "{i}Good, because I really want to eat this horny little pussy..."
    scene ch10_788scl1_
    pause 0.1
    play voicefx smoansoft volume 0.5 loop 
    play soundfx kissing2 volume 0.2 loop  
    mc "*Smch, suck* {i}Hmm..."
    s "*Uh* {i}[mc], you didn't even let me get comfortable..."
    pause
    mc "*Hmchp* {i}What we did on the Ferris wheel made me really horny."
    s "*Uhm* {i}Is the shark horny?"
    mc "{i}Yes... {/i}*smch* {i}Very horny..."
    s "*giggle*{w=0.7}{nw}"
    scene ch10_788scl3_ 
    pause 0.1
    mc "*Mah, lahl* {i}What a tasty pussy..."
    pause
    mc "{i}Do you like how I suck you here?"
    s "*Huh, hmm* {i}Y{w=0.5}-yes..."
    s "{i}You're moving your tongue all over my pussy... {/i}*huh*"
    s "{i}It feels so good, [mc]..."
    $ current_pov = 2
    scene ch10_788scl2_ 
    call screen ch10_788scl_
label ch10_788scl1_:
    $ current_pov = 1
    scene ch10_788scl1_ with Dissolve(0.2)
    call screen ch10_788scl_
label ch10_788scl2_:
    $ current_pov = 2
    scene ch10_788scl2_ with Dissolve(0.2) 
    call screen ch10_788scl_ 
label ch10_788scl3_:
    $ current_pov = 3
    scene ch10_788scl3_ with Dissolve(0.2) 
    call screen ch10_788scl_ 
label ch10_788scl1_cont:
    if current_pov != 2:
        scene ch10_788scl2_ with Dissolve(0.2) 
    $ anim_speed = 0.015
    image ch10_790anim:
        "ch10_790" with Dissolve(0.15)
        0.2
        "ch10_791" with Dissolve(0.15)
        0.2
        "ch10_792" with Dissolve(0.15)
        0.2
        "ch10_793" with Dissolve(0.15)
        0.2
        repeat
    scene ch10_790anim:
        subpixel True
        zoom 1.01 xalign 0.5 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.503, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.497, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    mc "*Chup, slurp, smonch!*"
    s "*Uh, uhmm...*"
    stop voicefx fadeout 0.5
    scene ch10_793-
    stop soundfx
    stop sound
    mc "*Hah* {i}How delicious..."
    pause
    scene ch10_794
    s "{i}[mc], I want you to lick me more...."
    mc "{i}I know, I just stopped to catch my breath."
    play voicefx smoansoft volume 0.5 loop
    play sound kissing2 loop volume 0.25
    camera:
        subpixel True
        zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    image ch10_799anim:
        "ch10_795" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_797" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_797" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        repeat
    image ch10_799-anim:
        "ch10_798" with dissolve
        0.75
        "ch10_799" with dissolve
        0.75
        repeat
    scene ch10_799anim
    mc "*lahm, lah* {i}"
    scene ch10_799-anim
    s "*Hah* {i}[mc], not there..."
    mc "*lahm* {i}Your little ass needs some love too..."
    s "*uh* {i}If you like it..."
    mc "{i}Doesn't it feel good?"
    s "{i}Uhm... y-yes, but that's dirty..."
    mc "*lah* {i}Don't worry, you're very clean..."
    mc "{i}It's just that you have such a pretty little ass that I can't resist."
    s "*Huh* {i}You're so naughty, [mc]..."
    image ch10_799anims:
        "ch10_795" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_797" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_797" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_795" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_797" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75
        "ch10_797" with dissolve
        0.75
        "ch10_796" with dissolve
        0.75

        "ch10_798" with dissolve
        0.75
        "ch10_799" with dissolve
        0.75
        "ch10_798" with dissolve
        0.75
        "ch10_799" with dissolve
        0.75
        "ch10_798" with dissolve
        0.75
        "ch10_799" with dissolve
        0.75
        "ch10_798" with dissolve
        0.75
        "ch10_799" with dissolve
        0.75
        repeat 
    scene ch10_799anims
    pause
    scene ch10_799-
    stop sound
    stop soundfx
    stop voicefx fadeout 1.0
    mc "{i}Take off your clothes."
    s "{i}Uh... huh..."
    s "{i}Uh... [mc], you licked me in a very pervy way..."
    mc "{i}Just the way you like it."
    s "{i}Y-yeah..."
    scene ch10_800
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    mc "Aren't you going to take your clothes off?"
    mc "{i}Don't tell me you're tired already..."
    s "{i}N-no, I just need a second *huh* to catch my breathe..."
    mc "{i}(I find it funny how her little legs are shaking, she can barely stand.)" with dissolve
    pause
    mc "{i}Ready to continue?"
    s "{i}Y-yes!..."
    scene ch10_801
    mc "Come here, I'll help you."
    mc "Raise your arms high."
    scene ch10_803
    s "{i}[mc], are we really boyfriend and girlfriend?"
    mc "{i}For today, yes."
    s "{i}You said real boyfriend and girlfriend."
    mc "{i}Yes, we're real boyfriend and girlfriend..."
    s "{i}You can see my tits..." 
    s "{i}W-well, I'll let you see them because you're my boyfriend."
    scene ch10_804 
    mc "{i}Are you still shy to show them to me?"
    s "{i}A little..."
    mc "{i}You don't have to be."
    scene ch10_802-
    s "{i}I-it's just that... I'm still not used to it."
    pause
    scene ch10_805
    mc "{i}Your tits are very pretty... I love those little pink nipples."
    s "Well, but don't stare at them so much..."
    mc "Aren't you supposed to be my girlfriend?"
    s "Yes, I am your girlfriend."
    play sound kissing2 volume 0.2 loop fadein 1.0
    scene ch10_806
    s "*Ayn*..."
    mc "*Hm* {i}You have nothing to be shy about."
    scene ch10_807
    mc "*chup* {i}Your small tits don't need to grow to be sexy."
    scene ch10_808
    mc "*Mahl*"
    scene ch10_809
    mc "*Mhl*"
    scene ch10_807
    mc "*Hmn*"
    image ch10_807anim:
        "ch10_806" with dissolve
        1.0
        "ch10_807" with dissolve
        1.0
        "ch10_808" with dissolve
        1.0
        "ch10_809" with dissolve
        1.0
        repeat
    scene ch10_807anim
    pause
    s "{i}[mc], I can't see anything..."
    s "{i}[mc]..."
    stop sound fadeout 0.5
    scene ch10_810
    mc "Your tits are like cute vanilla panna cottas..."
    pause
    s "[mc], I'm getting desperate."
    scene ch10_811
    s "{i}Silly! I didn’t say you could do that!"  
    mc "{i}Your face is all red."  
    s "{i}I told you to stop!"  
    s "{i}You’re not allowed to kiss my boobs anymore."  
    mc "{i}But we’re boyfriend and girlfriend."  
    s "{i}So what?"
    scene ch10_811-
    mc "{i}Okay, I'm sorry. Don't be mad at me."  
    s "{i}Yes, I’m mad..."  
    scene ch10_811--  
    mc "{i}Alright, alright... just kiss me..."  
    s "{i}N-no, I’m not gonna kiss you."  
    mc "{i}Kiss me..."  
    scene ch10_811---  
    s "*smonch* {i}No..."  
    pause  
    scene ch10_812 with hpunch  
    s "{i}No!"  
    s "{i}You have to ask for my permission!"  
    mc "{i}Now I have to ask for your permission for everything?"  
    s "{i}Yes!"  
    mc "{i}Even to give you a little kiss?"  
    s "{i}Yes, even for that."  
    mc "Oh, really?"  
    mc "{i}Did you ask for my permission that time you sucked my dick while I was sleeping?"  
    s "{i}Uhm..."  
    s "{i}N-no, that’s not the same!"
    $ store.animation_system_active = True
    $ hide_anim_speed()
    $ anim_speed = 0.02 
    scene ch10_814sthj1_ with vpunch
    s "{i}Eeek!... *giggle*"
    mc "{i}Come here..."
    play soundfx3 kissing volume 0.1 loop
    pause 0.01
    play soundfx2 kissing2 volume 0.1 loop
    pause 0.1
    scene ch10_814sthj3_
    play voicefx2 smoansoft volume 0.5 loop
    pause 0.5
    $ current_pov = 2
    call screen ch10_814sthj_ with dissolve

label ch10_814sthj3_:
    $ current_pov = 2
    scene ch10_814sthj3_ 
    pause 0.5
    call screen ch10_814sthj_ with dissolve
label ch10_814sthj1_:
    $ current_pov = 1
    scene ch10_814sthj1_ 
    pause 0.5
    call screen ch10_814sthj_ with dissolve
screen ch10_814sthj_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.01), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_814sthj3_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_814sthj1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_814sthj1_1")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
init python:
    def ch10_814sthj1_(trans, st, at):
        if not getattr(store, 'animation_system_active', True):
            return None
        if store.current_active_animation != "ch10_814sthj1_":
            store.current_active_animation = "ch10_814sthj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_814sthj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_814sthj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound3])
                store.last_played_sound3 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

    def ch10_814sthj3_(trans, st, at):
        if not getattr(store, 'animation_system_active', True):
            return None
        if store.current_active_animation != "ch10_814sthj3_":
            store.current_active_animation = "ch10_814sthj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_814sthj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_814sthj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound3])
                store.last_played_sound3 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
image ch10_814sthj1_:
    function ch10_814sthj1_
image ch10_814sthj3_:
    function ch10_814sthj3_












label afterch10_814sthj1_1:
    image ch10_815anis:
        "ch10_815" with dissolve
        1.0
        "ch10_815_1" with dissolve
        1.0
        "ch10_815_2" with dissolve
        1.0
        repeat
    $ store.animation_system_active = "False"
    $ stop_sounds()
    play sound kissing loop volume 0.3
    scene ch10_815anis
    play soundfx kissing2 loop volume 0.3
    pause
    image ch10_816anim:
        "ch10_816" with Dissolve(0.5)
        0.5
        "ch10_816-" with Dissolve(0.5)
        0.5
        repeat
    scene ch10_816anim
    #$ renpy.say(None, "current_active_animation: " + str(store.current_active_animation))
    pause
    s "*Lah-dah-lah* {i}Use more spit, [mc]..."
    mc "{i}(Fuck, these kisses with [s], so lewd and dirty...)" with dissolve
    pause
    stop sound
    stop sound_fx
    stop voicefx
    scene ch10_817
    $ stop_sounds()
    play sound kissing volume 0.1 loop
    s "*Mahl* {i}I'm going to lick you everywhere..."
    scene ch10_818
    mc "*Uh*..."
    s "*Hmch*"
    image ch10_819animm:
        "ch10_819" with Dissolve(0.5)
        0.5
        "ch10_819-" with Dissolve(0.5)
        0.5
        "ch10_819_" with Dissolve(0.5)
        0.5
        repeat
    scene ch10_819animm
    s "*Smch, muah, smoonch*"
    mc "{i}Uh, [s].... "
    pause
    scene ch10_818-
    s "{i}Do you like it when I suck your tits?" 
    mc "{i}It's nice, I guess."
    s "{i}I think they're bigger than mine."
    mc "{i}Of course not."
    scene ch10_818--
    s "{i}I like your abdomen... you're very strong, [mc]."
    s "{i}I want to give you lots of kisses all over..."
    play soundfx kissing2 volume 0.1 loop
    scene ch10_818---
    s "*Mmmh* "
    scene ch10_818----
    pause
    scene ch10_818-----
    pause
    scene ch10_818------
    pause
    scene ch10_818-------
    pause
    image ch10_818anim:
        "ch10_818---" with Dissolve(0.3)
        0.8
        "ch10_818----" with Dissolve(0.3)
        0.8
        "ch10_818---" with Dissolve(0.3)
        0.8
        "ch10_818-----" with Dissolve(0.3)
        0.8
        "ch10_818------" with Dissolve(0.3)
        0.8
        "ch10_818-------" with Dissolve(0.3)
        0.8
        "ch10_818-----" with Dissolve(0.3)
        0.8
        "ch10_818------" with Dissolve(0.3)
        0.8
        "ch10_818-------" with Dissolve(0.3)
        0.8
        repeat
    scene ch10_818anim
    mc "{i}Uh, yeah..."
    s "lah, bleh, mua"
    s "{i}Your dick's really warm... {/i}bleh {i}and super hard too..." 
    s "{i}When it gets hard and big, it looks so cute."
    pause
    scene ch10_818--------
    stop soundfx
    stop sound
    play sound "audio/mouth/saliva_01.ogg" volume 0.5
    s "*Pfft*" 
    scene ch10_818---------
    s "{i}I like it slippery."
    mc "{i}Yeah, I can tell..."
    s "{i}Now I’m gonna jerk you off, okay?"
    $ store.animation_system_active = True
    scene ch10_818shj1_
    pause 0.5
    s "{i}You like this?"
    mc "{i}Yeah..."
    mc "{i}(She’s squeezing it so nicely with her hands, all covered in spit...)" with dissolve
    mc "{i}(Still remembers how I taught her...)" with dissolve
    s "{i}Don’t cum yet, okay?"
    mc "{i}Alright, I’m still holding it..."
    mc "{i}Faster..."
    $ anim_speed = 0.015
    s "{i}Like this?"
    mc "{i}Yeah... uh..."
    mc "{i}(Her hands are so tiny... can't cover the whole size of my cock...)" with dissolve
    mc "{i}(But it feels really good...)" with dissolve
    mc "{i}(What turns me on the most is that sweet yet pervy look on her face...)" with dissolve
    mc "{i}(She definitely loves all this...)" with dissolve
    pause
    call screen ch10_818shj_ with dissolve


init python:
    def ch10_818shj1_(trans, st, at):
        if not getattr(store, 'animation_system_active', True):
            return None
        if store.current_active_animation != "ch10_818shj1_":
            store.current_active_animation = "ch10_818shj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_818shj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_818shj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound3])
                store.last_played_sound3 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

image ch10_818shj1_:
    function ch10_818shj1_

screen ch10_818shj_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.01), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_818shj_s")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label afterch10_818shj_s:
    mc "{i}Give it more spit..."  
    scene ch10_818--------
    play sound "audio/mouth/saliva_04.ogg" volume 0.5
    s "*Spit*"  
    scene ch10_818shj1_ with dissolve  
    mc "{i}Oh yeah..."  
    s "{i}Should I add more?"  
    mc "{i}A little more."  
    scene ch10_818--------
    play sound "audio/mouth/saliva_02.ogg" volume 0.5
    s "*Spit*"  
    scene ch10_818shj1_  
    s "{i}It's getting really slippery now. *giggle*"  
    s "{i}[mc], should I suck it now?"  
    mc "{i}You want to suck it, don't you?"  
    s "{i}Yes."  
    mc "{i}Allright, put it in your mouth..."  
    s "{i}I'll suck it like a perv... {/i}*giggle*"  
    $ anim_speed = 0.02 
    scene ch10_819sbj1_  
    pause  
    mc "{i}You're using so much spit... feels so good..."  
    mc "{i}Don't forget to use your tongue around the head too..."  
    s "*Slurp, suck* {i}*hmm-hmm..."  
    pause  
    scene ch10_819sbj2_ 
    mc "{i}That's it... *uh*, you know exactly how I like it..."  
    s "*Slurp, hmm* {i}*hmm..."  
    mc "{i}(I can feel how she pressing her tongue hard around my glans... It feels amazing.) *uh*" with dissolve  
    scene ch10_819sbj3_  
    $ current_pov = 3  
    mc "{i}(I can't believe I'm enjoying this so much...)" with dissolve  
    mc "{i}(I'm really lucky to have a [srelat] like [s].)" with dissolve
    call screen ch10_819sbj_ with dissolve  

image ch10_819sbj1_:
    function ch10_819sbj1_
image ch10_819sbj2_:
    function ch10_819sbj2_
image ch10_819sbj3_:
    function ch10_819sbj3_
init python:
    def ch10_819sbj1_(trans, st, at):
        if store.current_active_animation != "ch10_819sbj1_":
            store.current_active_animation = "ch10_819sbj1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_819sbj1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_819sbj1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_58.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.04, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.15:
                    if random_chance < 0.3: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='sound')
                        renpy.sound.play(random_sound, channel='sound')
                elif anim_speed < 0.151:
                    if random_chance < 0.5: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='sound')
                        renpy.sound.play(random_sound, channel='sound')
        return store.anim_speed

    def ch10_819sbj2_(trans, st, at):
        if store.current_active_animation != "ch10_819sbj2_":
            store.current_active_animation = "ch10_819sbj2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_819sbj2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_819sbj2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.3 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_58.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.04, 0.75 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.15:
                    if random_chance < 0.3: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='sound')
                        renpy.sound.play(random_sound, channel='sound')
                elif anim_speed < 0.151:
                    if random_chance < 0.5: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='sound')
                        renpy.sound.play(random_sound, channel='sound')
        return store.anim_speed

    def ch10_819sbj3_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_819sbj3_":
            store.current_active_animation = "ch10_819sbj3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_819sbj3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_819sbj3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_58.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.04, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.15:
                    if random_chance < 0.3: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.25 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='sound')
                        renpy.sound.play(random_sound, channel='sound')
                elif anim_speed < 0.151:
                    if random_chance < 0.5: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.25 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='sound')
                        renpy.sound.play(random_sound, channel='sound')

        return store.anim_speed
screen ch10_819sbj_:
    if ch10sdeep == True:
        $ ch10sdeep = True
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        xalign 0.99
        yalign 0.3
        if ch10sdeep == True:
            if current_pov == 1:
                textbutton "Deepthroat" action Jump("ch10_819sbj4_") style "textbutton_choice"
            elif current_pov == 2:
                textbutton "Deepthroat" action Jump("ch10_819sbj6_") style "textbutton_choice"
            elif current_pov == 3:
                textbutton "Deepthroat" action Jump("ch10_819sbj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [SetVariable("current_pov", 3), Jump("ch10_819sbj3_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_819sbj2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_819sbj1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        if ch10sdeep == True:
            textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10819sdeept")] style "textbutton_choice"   
        else:
            textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_819sbj1")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  




image ch10_819sbj2_:
    function ch10_819sbj2_
image ch10_819sbj3_:
    function ch10_819sbj3_

label ch10_819sbj1_:
    $ current_pov = 1
    $ ch10sdpos = 0
    scene ch10_819sbj1_ with nothing
    call screen ch10_819sbj_ 
label ch10_819sbj2_:
    $ current_pov = 2
    $ ch10sdpos = 0
    scene ch10_819sbj2_ with nothing
    call screen ch10_819sbj_
label ch10_819sbj3_:
    $ current_pov = 3
    $ ch10sdpos = 0
    scene ch10_819sbj3_ with nothing
    call screen ch10_819sbj_










init python:
    def ch10_819sbj4_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_819sbj4_":
            store.current_active_animation = "ch10_819sbj4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_819sbj4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_819sbj4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_58.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.04, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_7.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_15.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.02:
                    if random_chance < 0.75: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                elif anim_speed < 0.151:
                    if random_chance < 0.95: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
        return store.anim_speed

    def ch10_819sbj5_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_819sbj5_":
            store.current_active_animation = "ch10_819sbj5_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_819sbj5_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_819sbj5_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.3 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_58.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.04, 0.75 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_7.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_15.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.02:
                    if random_chance < 0.75: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                elif anim_speed < 0.02:
                    if random_chance < 0.95: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
        return store.anim_speed

    def ch10_819sbj6_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_819sbj6_":
            store.current_active_animation = "ch10_819sbj6_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
                renpy.sound.stop(channel='voicefx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_819sbj6_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_819sbj6_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_58.ogg", "audio/wavs/bj_48.ogg", "audio/wavs/bj_46.ogg", "audio/wavs/bj_44.ogg", "audio/wavs/bj_42.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                final_volume = max(0.04, 0.75 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/wavs/bj_7.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_15.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                if anim_speed > 0.02:
                    if random_chance < 0.75: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')
                elif anim_speed < 0.02:
                    if random_chance < 0.95: 
                        store.last_played_sound3 = random_sound
                        store.sound_played_this_cycle = True
                        final_volume = max(0.01, 0.5 * fade_multiplier)
                        renpy.sound.set_volume(final_volume, channel='voicefx')
                        renpy.sound.play(random_sound, channel='voicefx')

        return store.anim_speed
screen ch10_819sbj2_:
    if ch10sdeep == True:
        $ ch10sdeep = True
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        xalign 0.99
        yalign 0.3
        if ch10sdeep == True:
            if current_pov == 1:
                textbutton "Blowjob" action Jump("ch10_819sbj1_") style "textbutton_choice"
            elif current_pov == 2:
                textbutton "Blowjob" action Jump("ch10_819sbj2_") style "textbutton_choice"
            elif current_pov == 3:
                textbutton "Blowjob" action Jump("ch10_819sbj3_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [SetVariable("current_pov", 2), Jump("ch10_819sbj5_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_819sbj6_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_819sbj4_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        if ch10sdeep == True:
            textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10819sdeept")] style "textbutton_choice"   
        else:
            textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10819sdeept")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  



image ch10_819sbj4_:
    function ch10_819sbj4_
image ch10_819sbj5_:
    function ch10_819sbj5_
image ch10_819sbj6_:
    function ch10_819sbj6_


label afterch10_819sbj1:
    if current_pov != 1:
        scene ch10_819sbj1_ with nothing
    show screen random_anim_speed_fast with nothing
    $ anim_speed = 0.012
    mc "{i}Uh..."
    mc "{i}You're getting really good at this..."
    s "{i}*Slurp, slurp, slurph*"
    pause
    mc "{i}Can you go deeper?"
    s "*Slurp* {size=-3}{i}Mmh, deepah'?"
    mc "{i}Yeah, take it deeper into your mouth."
    scene ch10_818shj1_ with dissolve
    s "{i}But if I go too deep, it'll hit my throat... I don’t think I can handle all of it, [mc]." with nothing
    mc "{i}Do it as deep as you can..."
    s "{i}Do you want me to suck it like [k] does? She takes it all the way."
    s "{i}I saw you at [mia]'s house, she sucks your dick all the way down."
    s "{i}Hmm, maybe I can do it too."
    mc "{i}Wanna give it a try?"
    scene ch10_818----------
    s "{i}Yeah, I wanna try..."
    scene ch10_819sbj4_
    $ hide_anim_speed()
    $ anim_speed = 0.02
    s "*Guh, slurp* {i}I'll try to... {/i}*gugh, slorp* {i}-go as deep as she does...{/i}"
    mc "{i}That's it, uh... you're doing great. {/i}*hmm*"
    mc "{i}(She’s going deeper than most girls I’ve been with… and not even gagging.)"
    mc "{i}(Is this what they call natural talent?)" with dissolve
    s "*Slurp, gag, gag* {i}Hm-hmph...{/i}"
    scene ch10_819sbj1_
    play voicefx "sbjmoan_1.ogg" volume 1.0
    s "*Hah* {i}I can’t breathe if I go too deep...{/i}"
    mc "{i}That’s okay. You don’t have to force it."
    scene ch10_819sbj4_
    s "*Slurp, chup, slurg*"
    mc "{i}Oh, yeah..."
    pause
    scene ch10_819sbj5_
    s "*Gugh, slurp, slurp*"
    mc "{i}Uh... you're really getting good at this..."
    s "*Slurp, slurgh*"
    mc "{i}Uh..."
    scene ch10_819sbj6_
    mc "{i}You look so beautiful with my dick in your mouth..."
    $ ch10sdeep = True
    $ current_pov = 2
    call screen ch10_819sbj2_ with dissolve
define ch10sdpos = 0
label ch10_819sbj4_:
    $ current_pov = 1
    $ ch10sdpos = 1
    scene ch10_819sbj4_ with nothing
    call screen ch10_819sbj2_  
label ch10_819sbj5_:
    $ current_pov = 3
    $ ch10sdpos = 0
    scene ch10_819sbj5_ with nothing
    call screen ch10_819sbj2_  
label ch10_819sbj6_:
    $ current_pov = 2
    $ ch10sdpos = 0
    scene ch10_819sbj6_ with nothing
    call screen ch10_819sbj2_  

label afterch10819sdeept:
    $ anim_speed = 0.01
    if ch10sdpos != 1:
        scene ch10_819sbj4_
        s "*Slorp, slurp, gugsh*"
    scene ch10_819sbj1_
    s "*Hmph* {i}Hmm..."
    s "*Chup, slurp* {i}{size=-3}I can’t keep sucking this deep for long..." 
    mc "{i}It's okay, take it easy. You can do it however you prefer..."
    scene ch10_819sbj4_
    s "*Slurp, slorp, schlup*"
    mc "*Uh*"
    $ store.current_active_animation = "anim"
    scene ch10_820
    pause 0.2
    play sound "audio/mouth/swallow_06.ogg"
    pause 0.75
    scene ch10_820-
    play sound "audio/wavs/bj_65.ogg"
    mc "*Uh* {w=0.5}{nw}"
    scene ch10_821
    play sound "audio/wavs/bj_80.ogg.ogg"
    pause 0.5
    scene ch10_820
    play sound "audio/mouth/swallow_06.ogg"
    pause 0.3
    play soundfx "audio/wavs/bjgags10.ogg"
    pause 0.75
    scene ch10_820-
    play sound "audio/wavs/bj_67.ogg"
    mc "*Uh* {w=0.5}{nw}"
    scene ch10_821
    play sound "audio/mouth/saliva_01.ogg" volume 0.3
    pause 0.3
    play sound_fx "audio/wavs/s/sbjmoan_2.ogg"
    pause 0.5
    scene ch10_822
    play sound "audio/wavs/gag/bjgags1.ogg" volume 0.5
    s "*Burp, cough-cough-cough*"
    pause
    scene ch10_823
    mc "{i}Are you okay?"
    s "{i}Yeah... {/i}*sniff*{i} I couldn’t take it in that deep."
    mc "{i}It’s okay, it’s your first time trying this."
    scene ch10_822--
    s "*Cough-cough* {i}I wanted to do it like [k] does..."
    mc "{i}You don’t have to go that deep, okay? It already feels amazing just the way you do it."
    s "{i}Okay. {/i}*sniff*"
    scene ch10_822---
    mc "{i}What're you doing now, hm?"
    s "{i}Nothing..."
    mc "{i}[s]...?"
    image ch10_824anim:
        "ch10_824" with dissolve
        0.8
        "ch10_825" with dissolve
        0.8
        repeat
    scene ch10_824anim
    s "{i}Are we gonna make love today?"
    mc "{i}[s]..."
    s "{i}We're boyfriend and girlfriend now, [mc]..."
    mc "{i}[s], s-stop playing."
    s "{i}Isn't that what couples do?"
    mc "[s], we can't..."
    show screen random_anim_speed_normal with nothing
    $ anim_speed = 0.02
    scene ch10_822srj0_
    play voicefx smoansoft volume 0.2 loop fadein 1.0
    s "*Te-he*... {i}Look, we're gonna have sex..."
    mc "{i}[s], c-cut it out."
    s "{i}Why?"
    s "{i}Hmm, sex feels so good..."
    s "{i}Right? Doesn't it feel good?"
    mc "{i}Th-this isn't sex..."
    s "{i}I just need it to go in... {i}{w=0.5}and it's going in..."
    s "{i}My pussy's giving your tip a little kiss, can you feel it?"
    mc "{i}Uh, [s], s-stop..."
    mc "{i}(An inexperienced girl is messing with me...)" with dissolve
    mc "{i}*Uhh*... (My cock's gonna explode just from all this teasing...)" with dissolve
    call screen ch10_822srj_ with dissolve



label afterch10_822srjj:
    mc "{i}[s], w-wait..."
    s "{i}What? I'm not putting it in..."
    s "{i}It's going in on its own..."
    mc "*Hmgh*"
    s "{i}Are you getting turned on?"
    s "{i}You gonna shot it already?"
    s "{i}Do it in my pussy!"
    mc "{i}[s], stop... {/i}*hmgh*"
    pause
    scene ch10_822srj1_ with vpunch
    mc "*Hngh!*"
    s "{i}[mc], if you push me down, it's really going to go in..."
    s "{i}If it goes in, it's your fault, okay? {/i}*te-he*"
    mc "*Hah* (My hips won't stop moving, my body wants it...)" with dissolve
    s "''*Waah*'' {i}''I'm your bitch, [mc], this feels so good''..."
    s "{i}Why was [k] screaming like that? *giggles*"
    s "{i}Did you sticking your dick in her pussy drive her crazy?"
    mc "{i}-Shh, remember everyone's asleep... {/i}*hmgh*"
    s "{i}[k] isn't here, and [arelatks] and [drelatks] are sleeping upstairs. We can make a little noise."
    mc "{i}*Hah*."
    s "{i}''Tell me you're my bitch, argh!'', haha. Who am I, [mc]?"
    s "{i}[mc], you keep pushing..."
    s "{i}When you're turned on, you can't control yourself?, is that why you and [k] were so loud?"
    s "{i}But don't make too much noise now. Remember we need to be quiet!"
    mc "{i}Hah..."
    call screen ch10_822srj_ with dissolve
    
screen ch10_822srj_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed = 0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_822srjjj")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch10_822srj2_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.03), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.02), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.012), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_speed", max_speed = 0.012, min_speed=0.03), Function(disable_even_frames)] style "textbutton_choice" 
    vbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_822srj2_1")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
image ch10_822srj0_:
    function ch10_822srj0_
image ch10_822srj1_:
    function ch10_822srj1_ 
init python:
    def ch10_822srj0_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_822srj0_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_822srj1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_822srj1_{}".format(store.frame_num))
        return store.anim_speed
    def ch10_822srj1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_822srj1_{}".format(store.frame_num))
        return store.anim_speed

    def ch10_822srj1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        store.frame_num = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.frame_num > 40:
            store.frame_num = 1
        trans.set_child("ch10_822srj1_{}".format(store.frame_num))
        return store.anim_speed
label afterch10_822srjjj:
    $ anim_speed = 0.012
    s "{i}How does it feel? Is it like sex?"
    mc "{i}It feels good, but... {w=0.5}Well, if this is all we're doing, then it's okay..."
    s "{i}{size=-2}I want sex..."
    s "{i}{size=-2}Teach me how to have sex, [mc]..."
    scene ch10_822srj1_ with Dissolve(0.2)
    mc "{i}Hmnh..."
    mc "{i}(At first, I thought [s] was an angel, but she's actually a little devil...)"
    mc "{i}A sweet, cute little mischievous devil... *uh, hmngh*"
    s "{i}I'm not a little devil..."
    mc "{i}But you are mischievous..."
    s "*Te-he* {i}I'm super mischievous, yeah."
    s "{i}My pussy’s mischievous too... ’cause I’ve got a horny little pussy."
    s "{i}Haha..."
    mc "{i}S-stop teasing me, [s], or I don't know what I'll do..."
    s "{i}Why?"
    s "{i}What’ll happen if I keep teasing you?"
    s "{i}I'm getting so horny, [mc]..."
    mc "{i}[s]..."
    call screen ch10_822srj2_ with dissolve

    label afterch10_822srj2_1:
    s "{i}Put it in... you can put it in, I give you permission."
    mc "{i}[s], y-you don't know what you're saying, uh."
    s "{i}I do know."
    s "{i}[mc], I know you want it..."
    mc "{i}(I can't take it anymore...)" with dissolve
    pause
    scene ch10_826 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with Dissolve(0.2)
    mc "Gah!..."
    s "[mc], you’re squeezing me..."
    s "[mc]..."
    scene ch10_827 with vpunch
    mc "Argh!"
    s "Huh!"
    $ stop_sounds(0.5)
    scene ch10_828 with hpunch
    s "{i}{size=-2}Ow! {/size}*te-he*"
    mc "{i}(I almost did it...)" with dissolve
    $ store.animation_system_active = "anim"
    play soundfx kissing volume 0.25 loop
    play sound kissing2 volume 0.3 loop
    scene ch10_832
    play voicefx "audio/character/s/soft/s_moan_soft_12.ogg" volume 0.5
    s "*Hum, smch*..."
    scene ch10_831
    s "*Lah*"
    scene ch10_833
    s "*Hmmph*"
    scene ch10_834
    s "Hmch*"
    image ch10_834anim:
        "ch10_833" with Dissolve(0.5)
        1.0
        "ch10_834" with Dissolve(0.5)
        1.0
        "ch10_833" with Dissolve(0.5)
        1.0
        "ch10_834" with Dissolve(0.5)
        1.0
        "ch10_833" with Dissolve(0.5)
        1.0
        "ch10_834" with Dissolve(0.5)
        1.0

        "ch10_832" with Dissolve(0.5)
        1.0
        "ch10_831" with Dissolve(0.5)
        1.0
        "ch10_832" with Dissolve(0.5)
        1.0
        "ch10_831" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_834anim
    s "{i}Huh, [mc]... we were gonna do it.." 
    s "*Smnch* {i}Did you change your mind?" 
    "..."
    pause
    stop soundfx fadeout 0.1
    stop sound fadeout 0.1
    scene ch10_867
    mc "{i}(I almost did...)" with dissolve
    scene ch10_868
    mc "{i}(I almost took over this tiny, delicate body...)" with dissolve
    scene ch10_869
    mc "{i}(I can't do it, no...)" with dissolve
    scene ch10_870
    play sound kissing2 volume 0.2 loop
    s "{i}[mc], I'm talking to you."
    scene ch10_871
    s "{i}Uh, my boobs..."
    mc "{i}(I gotta settle for this...)" with dissolve
    s "{i}[mc], I wanna make love..."
    mc "{i}Drop it, [s]..."
    s "{i}But I want..."
    scene ch10_829_1
    s "{i}Uh, [mc], you're licking me all over..."
    mc "{i}(I gotta tough it out...)" with dissolve
    scene ch10_830
    pause
    scene ch10_830_____
    stop sound fadeout 0.1
    s "{i}Do you like licking my body?"
    s "{i}I love licking yours, it gets me all hot..."
    scene ch10_830_1
    mc "{i}Are these heels new?"
    scene ch10_830_2
    s "{i}Yep, I got 'em at the store."
    image ch10_830_2anim:
        "ch10_830_1" with dissolve
        1.1
        "ch10_830_2" with dissolve
        1.1
        repeat
    scene ch10_830_2anim
    mc "{i}They're really nice."
    s "{i}Hey, what are you doing? {i}*giggles*"
    mc "{i}I really like them..."
    image ch10_830_3anim:
        "ch10_830_3" with dissolve
        1.1
        "ch10_830_4" with dissolve
        1.1
        repeat
    scene ch10_830_3anim
    s "{i}That's weird..."
    s "{i}Do you like my new heels that much?"
    mc "{i}It's not just the heels..."
    s "{i}*giggles* I did my toenails too."
    mc "{i}Yeah, your feet are really pretty."

    menu:
        "[JGR]Lick her feet":
            $ ch10_830i_l_f_ = True
            "{nw}"
        "Go down on her now":
            jump ch10830idlf
    scene ch10_830_5
    mc "{i}Let's take 'em off..."
    s "{i}Why?"
    mc "{i}Don't you wanna be more comfortable?"
    s "{i}Fine, but just for a bit."
    scene ch10_830_6
    mc "{i}Hmm..."
    s "{i}[mc], you're tickling me. *giggles*"
    s "{i}Do they smell like cheese?"
    mc "{i}Not at all... hmm..."
    play soundfx kissing2 volume 0.2
    scene ch10_830_7
    pause
    scene ch10_830_9
    pause
    scene ch10_830_8
    pause
    scene ch10_830_10
    pause
    image ch10_830_10anim:
        "ch10_830_9" with dissolve
        1.0
        "ch10_830_8" with dissolve
        1.0
        "ch10_830_10" with dissolve
        1.0
        repeat
    scene ch10_830_10anim
    s "{i}[mc], that's... weird..."
    s "*Giggles* {i}It tickles..."
    s "Huh..."
    mc "{i}Hmm..."
    pause
    stop soundfx fadeout 0.1
    scene ch10_830_____
    s "{i}[mc], what you did was super pervy..."
    s "{i}I told you to put my heels back on."
    mc "{i}I'm doing that. Why don't you want to take them off?"
    s "{i}[mia] says they highlight my figure."
    scene ch10_830_1
    mc "{i}Ready."
    jump ch10830idlf
label ch10830idlf:
    stop soundfx fadeout 0.1
    scene ch10_830
    play soundfx kissing2 volume 0.2 loop
    mc "*hmm* {i}{size=-2}Have you been asking her for advice?"
    scene ch10_830-
    mc "*Muah, smch*"
    s "{i}Yeah, uh..."
    scene ch10_830---
    stop soundfx fadeout 0.1
    s "{i}[mc], lick my pussy now..."
    s "{i}Look how wet I am... {/i}*giggles*"
    mc "*Hah* (I'm panting, what the hell?)" with dissolve
    image ch10_830slp:
        "ch10_830----" with Dissolve(0.5)
        0.75
        "ch10_830-----" with Dissolve(0.5)
        0.75
        "ch10_830------" with Dissolve(0.5)
        0.75
        repeat
    play voicefx smoansoft volume 0.5 loop
    play sound kissing2 volume 0.3 loop
    scene ch10_830slp
    s "*Uhm.. uh..*"
    s "{i}You're being more pervy than usual..."
    s "{i}All of [mia]'s advice worked... *giggles*"
    s "{i}I like it more when you're pervy like this... *uh*"
    s "*hmm* {i}Because you do such dirty things..."
    s "*Huh, uhmm*...  {i}And I love stuff that gets me all hot like this..."
    mc "{i}(My mind, I can't think straight...)" with dissolve
    mc "{i}(The desire is too much, it hurts...)" with dissolve
    stop voicefx fadeout 0.5
    $ renpy.music.set_audio_filter("voicefx", af.Lowpass(440), replace=True)
    play voicefx smoansoft volume 0.5 loop
    play soundfx kissing volume 0.25 loop
    play sound kissing2 volume 0.3 loop
    scene ch10_834anim
    pause
    image ch10_835animm:
        "ch10_835" with dissolve
        1.0
        "ch10_835-" with dissolve
        1.0
        repeat
    scene ch10_835animm
    s "*Hmm, smch*... "
    mc "{i}(My hips are moving as I kiss her, I'm desperate...)" with dissolve
    mc "{i}(My heart... I can hear my heart pounding.)" with dissolve
    s "{i}I love you *smch*, I love you, [mc]..."
    $ stop_sounds()
    scene ch10_835------
    mc "*Hah* {i}W-what did you say?"
    s "{i}I love you."
    scene ch10_835animm with vpunch
    play voicefx smoansoft volume 0.5 loop
    play soundfx kissing volume 0.25 loop
    play sound kissing2 volume 0.3 loop
    mc "{i}I love you too!"
    s "*Muah, sch* {i}{size=-3}I really love you..."
    s "{i}{size=-1}I love you and I want...{/size} *smch*{w=0.5} {size=-3}I want us to have sex..."
    scene ch10_835------
    $ stop_sounds(0.5)
    mc "{i}[s]..."
    scene ch10_835--
    s "{i}I want us to have sex, [mc]."
    pause
    s "{i}N-no, I'm not gonna stop saying it until we do..."
    mc "{i}Why are you so obsessed, huh?"
    mc "{i}You don't even know if you will like it."
    scene ch10_835---
    s "{i}Neither do you..."
    pause
    s "{i}Besides, if I want to do these things, it's your fault..."
    s "{i}You do so many pervy things to me, I can't get it out of my head..."
    scene ch10_835----
    s "{i}You're the hottest guy ever."
    s "{i}Y-you drive me crazy..."
    s "{i}I want my first time to be with you, I've decided."
    s "{i}S-so... you have to accept it."
    pause
    mc "{i}[s], I'd like to, but we shouldn't..."
    scene ch10_835-----
    s "{i}No, no, [mc]!"
    mc "{i}[s], I've known you since you were a baby, I can't..."
    s "{i}I'm not a baby, and I'm not a little kid."
    s "{i}Stop treating me like one. I'm a woman, [mc]."
    mc "{i}You're not to me..."
    s "{i}You didn't think about that when you asked me to be your girlfriend..."
    mc "{i}You were the one who-{w=0.75}{nw}"
    s "{i}And what about when you kiss me?"
    scene ch10_835---
    s "{i}Or when you lick my boobs and give me those pervy tongue kisses?"
    s "{i}Or when you're, um... licking me down there..."
    s "{i}In all those moments, did I feel like a little girl to you?"
    mc "{i}T-that's not-{w=0.75}{nw}"
    s "{i}If it's not with you, it'll be with someone else eventually..."
    s "{i}So if you won't accept it, then... I'll find someone who will."
    mc "..."
    mc "{i}D-don't blackmail me like that..."
    mc "(My sweet [srelat] [s], with someone else...)" with dissolve
    mc "(I can't even imagine that...)" with dissolve
    pause
    mc "{i}Do you really want your first time to be with me?"
    scene ch10_835----- with hpunch
    s "{size=+3}Yes, you idiot!"
    scene ch10_835---
    mc "{i}{size=-3}H-hey."
    s "{i}{size=-1}How many times do I have to say it?"
    s "{i}I want my first time to be with the person I like the most in this world..."
    pause
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    mc "*Exhales* {i}O-okay."
    scene ch10_835------
    s "{i}Did you say okay?"
    s "{i}Really?"
    mc "{i}It's hard for me to accept that the little girl I've always cared for so much, could make me feel this way now..."
    mc "{i}But you're right."
    mc "{i}If you can have these kinds of feelings, then you're definitely a woman now."
    s "{i}I even wear heels now."
    mc "{i}Y-yeah..."
    s "{i}*Giggles*"
    s "{i}We are going to have sex..."
    s "{i}This is the happiest day of my life."
    s "{i}I've been dreaming about this for so long."
    s "{i}Almost a month now."
    mc "{i}(That's not long...)" with dissolve
    s "{i}Finally, you're gonna love me for real..."
    mc "{i}With or without sex, I'm gonna keep loving you the same, [s]. So much."
    s "{i}No, I want you to love me even more."
    mc "{i}That's impossible, I already love you as much as I can."
    s "{i}More than than that. I want all your love..."
    pause
    mc "{i}(She's so sweet...)" with dissolve
    mc "{i}B-but once we start, I might not be able to stop..."
    s "{i}Well, I won’t want you to stop, dummy."
    mc "{i}B-but..."
    mc "{i}I just... hope you never regret this."
    s "{i}I won’t."
    mc "{i}(I’ll make sure of it. Tonight has to be perfect.)" with dissolve
    mc "{i}Alright... you ready?"
    s "{i}Yes."
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_835animm
    scene ch10_836---:
        subpixel True
        xalign 0.5 yalign 0.0
        parallel:
            ease 10 zoom 0.5
        parallel:
            ease 5 yalign 1.0
    s "{i}O-okay, I'm ready now, [mc]. L-look... you can put it in now."
    mc "{i}([s] is the kind of girl who can take your breath away just by looking at her...)" with dissolve
    pause
    scene ch10_838
    mc "{i}This... is what’s about to go inside you."
    s "..."
    scene ch10_838-
    mc "{i}I’m pretty big, and you’re smaller than average, so it might hurt at first."
    s "{i}Uhm... D-does it have to go all the way in?"
    scene ch10_837
    mc "{i}I’ll be as gentle as I can."
    mc "{i}But once I start, I might not be able to stop myself."
    mc "{i}We can still back out."
    scene ch10_840
    mc "{i}So, you still think you’re ready?"
    mc "{i}We can forget about this and just go back to what we usually do."
    s "{i}No, I want to do it."
    s "{i}I’m ready, [mc]."
    mc "{i}(There’s no point in trying to change her mind now.)"
    mc "{i}A-alright... here we go..."
    scene ch10_839
    pause
    mc "{i}(I never thought this moment would actually come.)" with dissolve
    scene ch10_841
    mc "{i}If it hurts, tell me, okay?"
    s "{i}O-okay..."
    mc "{i}(I’m really going to take her virginity...)" with dissolve
    mc "{i}(Her first time will be with me...)" with dissolve

    $ audio_fade()
    pause 0.5
    mc "{size=-3}*Hah* {i}{/size}I love you. I love you so much."
    s "{i}I love you too, [mc]."
    scene ch10_844--
    mc "(Here we go...)" with dissolve
    scene ch10_844--- with dissolve
    $ audio_fade()
    $ clear_audiofx()
    pause 0.01
    play voicefx "audio/wavs/s/s_softmoan_1.ogg" volume 0.5
    pause
    scene ch10_841
    pause 0.5
    scene ch10_842 with dissolve
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    pause 0.01
    play voicefx "audio/character/s/mid/s_moan_mid_15.wav" volume 0.35
    mc "{i}D-does it hurt?"
    play voicefx smoansoft volume 0.3 fadein 3.0
    s "{i}N-no..."
    mc "{i}It’s supposed to feel good, not painful..."
    s "{i}I-it doesn’t hurt that much..."
    scene ch10_842
    s "*Unh*"
    scene ch10_844--
    pause
    scene ch10_844---
    pause
    mc "{i}(I’m barely in… just past the tip.)" with dissolve
    scene ch10_844--
    mc "{i}(Even with all the spit, I still can’t push in.)" with dissolve
    scene ch10_844---
    play voicefx "audio/character/s/soft/s_moan_soft_3.ogg" volume 0.35
    s "*Ahn*"
    image ch10_844---anim:
        "ch10_844--" with dissolve
        1.5
        "ch10_844---" with dissolve
        1.5
        repeat
    scene ch10_844---anim with dissolve
    play voicefx smoansoft volume 0.3 fadein 0.5
    pause
    mc "{i}(It's like her vaginal walls are pushing me out.)" with dissolve
    pause
    mc "{i}(I’ll have to push in a bit harder.)"
    scene ch10_844
    pause
    scene ch10_844-
    play voicefx "audio/character/s/soft/s_moan_soft_6.ogg" volume 0.7
    mc "{i}(I still can't get it in... she's so tight.)"
    pause
    scene ch10_842
    pause 0.75
    s "{i}Wait, [mc], wait..."
    scene ch10_841
    s "{i}Y-your dick is really big..."
    s "{i}I really want to do this, but..."
    s "{i}Since I'm so small, maybe your dick won’t fit..."
    mc "{i}It’s normal for it to hurt a little at first."
    s "{i}I'm scared, [mc]..."
    mc "{i}We can stop, it’s okay."
    s "{i}B-but I still want to..."
    mc "{i}Then maybe we should wait for another day."
    s "{i}N-no... you won’t want to another day."
    mc "{i}I promise we’ll try again, okay?"
    s "..."
    s "{i}I want it to be today..."
    mc "{i}(Girls tend to clench up more when they're nervous. I have to help her relax.)" with dissolve
    mc "{i}Alright, come here."
    scene ch10_835animm
    play voicefx smoansoft volume 0.5 loop fadein 0.5
    play soundfx kissing volume 0.25 loop fadein 0.5
    play sound kissing2 volume 0.3 loop fadein 0.5
    mc "*smnch* {i}If you're tense, it’s never gonna go in. You have to relax."
    s "{i}*muah* What if it just won’t fit?"
    s "{i}*hmch* {i}I hate being so tiny..."
    mc "{i}You’re just nervous."
    mc "{i}If you’re too nervous, your vagina won’t open."
    s "{i}I-I'm scared, {w=0.5}*muahl*{w=0.5} but at the same time, I want to do this."
    s "{i}Let’s keep trying, okay?"
    $ stop_sounds(0.5)
    scene ch10_841
    mc "{i}Just don’t push yourself too hard."
    mc "{i}Remember, sex has to feel good for both of us, otherwise it’s pointless."
    s "{i}Okay."
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_843
    mc "{i}Let's take it slow again."
    scene ch10_843-
    play voicefx smoansoft volume 0.45 loop
    s "*Huh*"
    mc "{i}Does it hurt like this?"
    image ch10_843animm:
        "ch10_843" with dissolve
        1.5
        "ch10_843-" with dissolve
        1.5
        repeat
    scene ch10_843animm
    s "{i}N-no, it feels good."
    s "{i}That actually feels nice..."
    mc "{i}Good, let’s keep going like this for a little while."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 1 zoom 1.01
            ease 1 zoom 1.005
            repeat
    scene ch10_835animm
    play voicefx smoansoft volume 0.5 loop fadein 1.0
    play soundfx kissing volume 0.25 loop fadein 0.5
    play sound kissing2 volume 0.3 loop fadein 0.5
    pause 
    mc "*Smch* {i}Just let go, forget about what we're doing."
    mc "*smch* {i}I want you to focus only on my kisses."
    s "*Muah, smch*"
    mc "*huh* {i}(I'm so turned on...)" with dissolve
    mc "{i}(My body’s reacting on its own again.)" with dissolve
    mc "{i}(I want to take her right now, hold her tight with all my strength...)" with dissolve
    mc "{i}(B-but I have to be gentle.)" with dissolve
    mc "{i}(I don’t want to hurt her.)" with dissolve
    camera:
        zoom 1.0 yalign 0.5 xalign 0.5
    scene ch10_843animm
    mc "{i}(Fuck...)" with dissolve
    s "*Huh*, *muah, smch*"
    mc "*hah* {i}(I’m getting more and more desperate...)" with dissolve
    mc "{i}(My wild impulses are taking control...)" with dissolve
    mc "*hah, muah* {i}(I can’t resist it, this thight little pussy... -I want to fuck her right now.)" with dissolve
    scene ch10_843--
    play voicefx "audio/character/s/soft/s_moan_soft_8.ogg" volume 0.5 
    s "*Uh*"
    s "{i}[mc]..."
    scene ch10_843animm
    play voicefx smoansoft volume 0.4 loop
    pause
    scene ch10_835animm
    pause 0.7
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 1 zoom 1.01
            ease 1 zoom 1.005
            repeat
    scene ch10_841 with dissolve
    $ stop_sounds(0.5)
    $ clear_audiofx()
    mc "*Hagh, gah*..."
    s "W-what’s wrong? Are you out of breath?"
    mc "{i}[s], I can’t take it anymore..."
    mc "-*Huh* {i}I’m going to do it."
    scene ch10_844
    pause
    scene ch10_844-
    play voicefx "audio/character/s/soft/s_moan_soft_7.ogg" volume 0.5 
    s "*Aah!*"
    mc "{i}Shh, r-remember everyone’s asleep..."
    s "{i}[mc], uh..."
    scene ch10_
    scene ch10_843
    pause
    scene ch10_843-
    pause
    scene ch10_843--
    play voicefx "audio/character/s/soft/s_moan_soft_1.ogg" volume 0.5 
    pause
    $ audio_fade()
    scene ch10_842
    s "{i}*Huh.. uh..*"
    scene ch10_842- with dissolve
    play voicefx "audio/character/s/mid/s_moan_mid_8.wav" volume 0.5
    s "*Aah!*"
    play voicefx smoansoft4 volume 0.3 loop fadein 2.0
    mc "{i}(Am I hurting her or is that a moan of pleasure?)" with dissolve
    mc "{i}(I don’t know, but I can’t stop now.)" with dissolve
    mc "{i}(I’m at my limit, there’s no turning back!)" with dissolve
    camera:
        zoom 1.0 yalign 0.5 xalign 0.5
    image ch10_843---anim:
        "ch10_843---" with Dissolve(0.5)
        0.5
        "ch10_834----" with Dissolve(0.5)
        0.5
        "ch10_843---" with Dissolve(0.5)
        0.5

        "ch10_843---" with Dissolve(0.25)
        0.25
        "ch10_834----" with Dissolve(0.25)
        0.25
        "ch10_843---" with Dissolve(0.25)
        0.25
        "ch10_843---" with Dissolve(0.25)
        0.25
        "ch10_834----" with Dissolve(0.25)
        0.25
        "ch10_843---" with Dissolve(0.25)
        0.25

        "ch10_843---" with Dissolve(0.5)
        0.5
        "ch10_834----" with Dissolve(0.5)
        0.5
        "ch10_843---" with Dissolve(0.5)
        0.5
        "ch10_843---" with Dissolve(0.5)
        0.5
        "ch10_834----" with Dissolve(0.5)
        0.5
        "ch10_843---" with Dissolve(0.5)
        0.5
        "ch10_834----" with Dissolve(0.5)
        0.25
        "ch10_843---" with Dissolve(0.5)
        0.25
        "ch10_834----" with Dissolve(0.5)
        0.25
        repeat
    scene ch10_843---anim
    mc "{i}I-it’s in, it went in already..."
    s "*A-aynh, uh*..."
    mc "{i}Your vagina needs to get used to me... *hah*... Let’s stay still like this for a while..."
    s "{i}Uh, unh..."
    pause
    mc "*Hah* {i}How does it feel?"
    s "*huh, uhm-hn* {i}I-I don’t know..."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_842
    mc "{i}Does it hurt?"
    s "{i}I-it doesn’t hurt... that much."
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        ease 1 xalign 0.5 
        ease 1 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    pause
    scene ch10_834anim
    play soundfx kissing volume 0.25 loop
    play sound kissing2 volume 0.3 loop
    s "*Muahl, smch, shlpk*"
    mc "{i}(Slowly, I have to push it in while she’s as turned on as possible...)" with dissolve
    scene ch10_834-
    pause
    $ stop_sounds(0.5)
    scene ch10_834--
    play voicefx "audio/character/s/soft/s_moan_soft_7.ogg" volume 0.5 
    s "*Aah, ayh..*"
    scene ch10_834---
    play voicefx "audio/character/s/mid/s_moan_mid_5.wav" volume 0.5 
    s "*Ah.. aeynh...*"
    scene ch10_834----
    play voicefx smoansoft4 volume 0.25 loop
    pause
    scene ch10_834-----
    play voicefx smoansoft4 volume 0.5 loop
    s "{i}*Aauh.. ah-aunh...*"
    mc "*uhh..* {i}(I'm all the way in...)"
    mc "{i}(I can feel the tip of my cock pressing against the back of her pussy... it feels amazing...)" with dissolve
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        ease 1 xalign 0.5 
        ease 1 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        #parallel:
        #    ease 1 zoom 1.01
        #    ease 1 zoom 1.005
        #    repeat
    scene ch10_842-
    mc "{i}I’m fully inside you now."
    s "{i}[mc]... *uh, hah...*"
    mc "{i}(Her vaginal walls are starting to tighten around my cock...)" with dissolve
    mc "{i}(Her insides are clenching and releasing convulsively... I wonder if it’s too much for her...)" with dissolve
    scene ch10_835animm
    play soundfx kissing volume 0.25 loop
    play sound kissing2 volume 0.3 loop
    s "*Huhm, shlkp, mualch* {i}Hah, uuh..."
    mc "{i}(My hips... they’re twitching involuntarily, I can barely keep them steady...)" with dissolve
    scene ch10_842
    stop soundfx fadeout 0.25
    stop sound fadeout 0.25
    stop music fadeout 5.0
    mc "*Hah, hah* {i}I-I’m gonna start moving now, okay?"
    s "{i}Uh-huh... Yeah."
    play music sexy4 fadein 1.5
    pause 1.5
    $ anim_speed = 0.0225
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_834sf3_
    play voicefx smoansoft3 volume 0.4 loop fadein 0.5
    s "*Huyn... a-auh... uhm...*"
    pause
    mc "*Hah* {i}(I'm actually doing it...)" with dissolve
    mc "{i}(I’m really fucking my sweet [srelat] [s]...)" with dissolve
    mc "{i}(My heart’s pounding... I can feel my pulse racing...)"
    mc "{i}(Fuck, she’s so tight...)" with dissolve
    mc "{i}(It’s like her pussy is sucking me in.)" with dissolve
    mc "*Hah* {i}(What a wonderful feeling...)" with dissolve
    s "{i}*Huh, huhyn...* S-slow down, [mc]."
    s "{i}-[mc]..."
    stop voicefx fadeout 0.1
    $ anim_speed = 0.045
    play voicefx smoansoft4 volume 0.5 loop
    mc "{i}S-sorry... uh..."
    mc "{i}This is better?"
    s "{i}Yeah.. This... is -better..."
    mc "{i}(I'm having sex with this beautiful angel... I must be dreaming...)" with dissolve
    pause
    mc "*Hmn* {i}D-does it still hurt?"
    s "{i}*Ahn, uhmm...* It hurts less... I-I think I’m getting used to it."
    mc "{i}(She says that with that expression on her face...)" with dissolve
    mc "{i}(She’s still very tense...)" with dissolve
    mc "{i}(That face and her tense body turn me on even more...)"
    pause
    mc "{i}Don’t try to be tough, remember it has to feel good."
    s "{i}Uh... *Ayhn*"
    s "{i}D-does it feel good for you?"
    mc "{i}Very good..."
    mc "{i}It feels unreal."
    mc "{i}(Even on her first time, she first cares about my pleasure...)" with dissolve
    mc "{i}(How could I not fall in love with a girl like this?)" with dissolve
    $ hide_anim_speed()
    stop voicefx fadeout 0.1
    $ anim_speed = 0.02
    pause 1.0
    play voicefx smoansoft3 volume 0.55 loop fadein 0.5
    s "*Ah* {i}[persistent.name[0]]-[persistent.name], are you going faster?..."
    s "*Ah, hah* [mc]..."
    mc "{i}(She looks so beautiful even with that tense look on her face...)" with dissolve
    s "*Uh, huh, ah* [mc], y-you’re going faster..."
    s "*Ah, ah* [mc]..."
    mc "{i}(Her insides feel unlike anything I’ve felt before, this tight, constant suction on my cock... it feels amazing.)" with dissolve
    mc "{i}(I’m trying to be careful, but I just can’t hold back...)" with dissolve
    mc "{i}(My cock is about to explode, it’s rock hard.)" with dissolve
    mc "*Hmgh* {i}(I feel this overwhelming urge to thrust into her with everything I’ve got.)" with dissolve
    pause
    $ anim_speed = 0.01
    mc "*Hmnh*"
    s "{i}*Aah, aaynh* [persistent.name[0]]-[persistent.name]..."
    s "{i}[mc], it hurts..."
    scene ch10_834sf2_
    mc "{i}I-I'm sorry, I can't go any slower now. *hngh*"
    s "*Ah, ah, ayn* {i}[mc], now it really hurts..."
    mc "{i}I-I can't stop, [s]."
    mc "*Hah* {i}Remember when I said I wouldn’t be able to control myself? You remember that, right?"
    mc "{i}H-hang in there... just a little longer, okay?"
    mc "*Mngh* {i}It’s gonna feel really good soon, I promise."
    s "{i}*Ahh, aynh, uh* [mc]..."
    mc "{i}Y-yeah?"
    s "*A-aynh* {i}I love you..."
    mc "*Hah* {i}I love you too, way more than you can imagine."
    mc "*Hngh*... {i}{w=0.5}My beautiful princess..."
    $ anim_speed = 0.009
    pause
    scene ch10_834sf1_
    s "*Aah, aah, ah*"
    pause
    mc "{i}Does it still hurt?"
    s "{i}Yes... I mean, no."
    s "*Hah, uh, uhm*"
    mc "{i}Can you hold on a little longer?"
    s "{i}*Hnn, uh, ayn* {i}Y-yes, I can."
    $ current_pov = 1
    call screen ch10_834sf_
init python:
    def ch10_834sf3_(trans, st, at):
        if not getattr(store, 'animation_system_active', True):
            return None
        if store.current_active_animation != "ch10_834sf3_":
            store.current_active_animation = "ch10_834sf3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_834sf3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sf3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 22 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_834sf2_(trans, st, at):
        if not getattr(store, 'animation_system_active', True):
            return None
        if store.current_active_animation != "ch10_834sf2_":
            store.current_active_animation = "ch10_834sf2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_834sf2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sf2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 22 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_834sf1_(trans, st, at):
        if not getattr(store, 'animation_system_active', True):
            return None
        if store.current_active_animation != "ch10_834sf1_":
            store.current_active_animation = "ch10_834sf1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_834sf1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sf1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 0.4 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 22 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
image ch10_834sf3_:
    function ch10_834sf3_
image ch10_834sf2_:
    function ch10_834sf2_
image ch10_834sf1_:
    function ch10_834sf1_
label ch10_834sf1_:
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    $ current_pov = 1
    scene ch10_834sf1_ 
    call screen ch10_834sf_
label ch10_834sf2_:
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    $ current_pov = 2
    scene ch10_834sf2_ 
    call screen ch10_834sf_
label ch10_834sf3_:
    camera:
        subpixel True
        ease 1.0 zoom 1.005 
        ease 1 xalign 0.5 
        ease 1 yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
        parallel:
            ease 1 zoom 1.01
            ease 1 zoom 1.005
            repeat
    $ current_pov = 3
    scene ch10_834sf3_ 
    call screen ch10_834sf_
screen ch10_834sf_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.01), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [SetVariable("current_pov", 2), Jump("ch10_834sf3_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_834sf2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_834sf1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_834sf1_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

label afterch10_834sf1_:
    $ store.animation_system_active = "anim"
    if current_pov != 2:
        scene ch10_834sf2_
    $ anim_speed = 0.009
    s "[mc], *uh, huh, auh!*, [mc]..."
    mc "*Hah, hmngh*"
    s "{i}I-It hurts, [mc]. *ah*, b-but *aah, auh, unh*"
    s "*Aah, auh, aynh* {i}[mc]!..."
    mc "{i}I’m sorry, [s], I can’t stop, m-my body’s moving on its own. *Hngh!*"
    $ anim_speed = 0.008
    s "{i}[mc]... *hmaah!*"
    image ch10_843---animcumms:
        "ch10_843---" with Dissolve(0.5)
        0.26
        "ch10_834----" with Dissolve(0.26)
        0.26
        "ch10_843---" with Dissolve(0.26)
        0.26

        "ch10_843---" with Dissolve(0.1)
        0.1
        "ch10_834----" with Dissolve(0.1)
        0.1
        "ch10_843---" with Dissolve(0.1)
        0.1
        "ch10_843---" with Dissolve(0.1)
        0.1
        "ch10_834----" with Dissolve(0.1)
        0.1
        "ch10_843---" with Dissolve(0.1)
        0.1

        "ch10_843---" with Dissolve(0.26)
        0.26
        "ch10_834----" with Dissolve(0.26)
        0.26
        "ch10_843---" with Dissolve(0.26)
        0.26
        "ch10_843---" with Dissolve(0.26)
        0.26
        "ch10_834----" with Dissolve(0.26)
        0.26
        "ch10_843---" with Dissolve(0.26)
        0.26
        "ch10_834----" with Dissolve(0.26)
        0.1
        "ch10_843---" with Dissolve(0.26)
        0.1
        "ch10_834----" with Dissolve(0.26)
        0.1
        repeat
    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
    scene ch10_843---animcumms with cumming
    s "*Aaah, aeyh!*"
    mc "{i}Shhh, shh..."
    s "*Huh, uhmm, hmmm*..."
    pause
    scene ch10_834---- with Dissolve(2.0)
    stop voicefx fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    s "{i}[mc]... th-that really hurt..."
    s "{i}Hah... ah..."
    scene ch10_846
    mc "{i}Come here..."
    s "{i}*Uuhn* [mc], it’s still inside me..."
    $ audio_fade()
    scene ch10_847
    play voicefx smoansoft volume 0.75 loop fadein 1.0
    mc "{i}Sorry, you’re so beautiful it’s hard to control myself."
    s "*Mch, smnch* {i}It’s okay..."
    scene ch10_847_1
    mc "*Hmmh*"
    play soundfx3 kissing volume 0.25 loop fadein 1.0
    play soundfx2 kissing2 volume 0.25 loop fadein 1.0
    scene ch10_847_3
    s "*Hm, monch*"
    scene ch10_847_4
    s "*Luah*"
    scene ch10_847_2
    s "*Mlah*"
    image ch10_847anim:
        "ch10_847_3" with Dissolve(0.5)
        1.0
        "ch10_847_4" with Dissolve(0.5)
        1.0
        "ch10_847_2" with Dissolve(0.5)
        1.0

        "ch10_847_3" with Dissolve(0.5)
        1.0
        "ch10_847_4" with Dissolve(0.5)
        1.0
        "ch10_847_2" with Dissolve(0.5)
        1.0
        "ch10_847_4" with Dissolve(0.5)
        1.0
        "ch10_847_2" with Dissolve(0.5)
        1.0
        repeat
    scene ch10_847anim
    pause
    scene ch10_848
    stop soundfx3 fadeout 0.5
    stop soundfx2 fadeout 0.5
    mc "{i}Sex shouldn’t hurt that much, it's my fault."
    s "{i}But I liked it..."
    s "{i}Y-you made me tremble. That felt good..."
    s "{i}And it didn’t hurt as much as at the beginning anymore."
    s "{i}I-if you want, we can keep going..."
    $ anim_speed = 0.045
    scene ch10_834sfm2_
    s "*Huh, uhm...* {i}Sex feels good even if it sometimes hurts..."
    s "{i}But when you were too rough, it did hurt a lot..."
    mc "{i}I'm sorry [s]. Does it not hurt like this?"
    s "{i}N-no... *uhm...*"
    mc "{i}Good, then let’s keep going like this..."
    pause
    image ch10_849anim:
        "ch10_849" with dissolve
        1.0
        "ch10_849-" with dissolve
        1.0
        repeat
    image ch10_848_1anim:
        "ch10_848_1" with Dissolve(0.5)
        0.3
        "ch10_848_2" with Dissolve(0.5)
        0.3
        "ch10_848_3" with Dissolve(0.5)
        0.3
        "ch10_848_4" with Dissolve(0.5)
        0.3
        repeat
    $ anim_speed = 0.02
    s "{i}*Huh, uhm*..."
    s "*Uhm, huh...*"
    scene ch10_848_1anim
    s "{i}*Huh, uh, uhm...*"
    mc "{i}(She’s the one moving now. Seems like she enjoys it more this way.)" with dissolve
    mc "{i}(I’m careful not to go all the way in, maybe that’s why.)" with dissolve
    mc "{i}What a sweet way to moan... Everything about you is so cute and sexy, I’m crazy about you." with dissolve
    s "*Huh, uhm, uhn* {i}[mc], I love you."
    s "*huh* {i}I-I want you to be my boyfriend forever."
    play sound kissing volume 0.2 loop
    play soundfx kissing2 loop volume 0.2
    scene ch10_849anim
    pause

    scene ch10_834sfm1_
    s "*smonch* {i}Your dick is throbbing inside me..."
    s "*Muahl* {i}I-I think I’m starting to like sex, [mc]."
    mc "{i}Really? *smch*"
    s "*smch* {i}Uh-hum..."
    $ current_pov = 1
    call screen ch10_834sfm_ with dissolve
    
    

screen ch10_834sfm_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.01), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_834sfm2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_834sfm1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_834sfm_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

label ch10_834sfm1_:
    $ current_pov = 1
    play sound kissing volume 0.2 loop fadein 1.0
    play soundfx kissing2 loop volume 0.2 fadein 1.0
    scene ch10_834sfm1_
    call screen ch10_834sfm_
label ch10_834sfm2_:
    $ stop_sounds(0.5)
    $ current_pov = 2
    scene ch10_834sfm2_
    call screen ch10_834sfm_

image ch10_834sfm1_:
    function ch10_834sfm1_
image ch10_834sfm2_:
    function ch10_834sfm2_
init python:
    def ch10_834sfm1_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_834sfm1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sfm1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 0.25 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound3])
                store.last_played_sound3 = sound
                final_volume = max(0.1, 0.25 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_834sfm2_(trans, st, at):
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if store.use_even_frames and new_frame % 2 != 0:
            new_frame = min(new_frame + 1, 40)
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_834sfm2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sfm2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 10 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound2])
                store.last_played_sound2 = sound
                final_volume = max(0.1, 0.25 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 26 <= store.frame_num and not store.sound_played_this_cycle:
                sound = renpy.random.choice([s for s in get_masturbating_sounds() if s != store.last_played_sound3])
                store.last_played_sound3 = sound
                final_volume = max(0.1, 0.25 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed

label afterch10_834sfm_:
    if current_pov != 1:
        scene ch10_834sfm1_
    scene ch10_847anim
    s "{i}Mahl, smch*"
    scene ch10_849anim
    pause 1.0
    image ch10_848_2anim:
        "ch10_848_1" with Dissolve(0.25)
        0.15
        "ch10_848_2" with Dissolve(0.25)
        0.15
        "ch10_848_3" with Dissolve(0.25)
        0.15
        "ch10_848_4" with Dissolve(0.25)
        0.15
        repeat
    $ stop_sounds(0.5)
    scene ch10_848_2anim
    play voicefx smoansoft volume 0.8 loop fadein 0.5
    s "{i}Uynh... uhnm..."
    s "*Ah-aynh* {i}N-not so fast, [mc]..."
    mc "{i}Wanna try a different position? One that doesn’t hurt so much?"
    s "*Huyn...* {i}Y-yeah, if you want..."
    scene ch10_849_1
    stop voicefx fadeout 1.0
    mc "{i}Let’s try doggy style now."
    s "{i}Doggy style?"
    mc "{i}Yeah, that’s what this one’s called."
    scene ch10_849_2
    mc "{i}Lift your hips higher. Just like that, perfect..."
    s "{i}You like doggy style?"
    mc "{i}I love it."
    scene ch10_850
    mc "{i}This way I get a better view of your waist and that cute heart-shaped butt of yours."
    s "{i}[mc], you really like my ass."
    scene ch10_851
    mc "{i}(Look at that... so round and well-shaped...)" with dissolve
    mc "{i}(This ass definitely comes from my [arelat] [a], it has the same perfect shape...)" with dissolve
    mc "{i}(Though, of course, adjusted for the size difference...)" with dissolve
    mc "{i}(But that doesn’t make it any less sexy...)" with dissolve
    scene ch10_850-
    mc "{i}Uh..."
    s "{i}S-so, this way won’t hurt?"
    mc "{i}I’ll be gentle."
    s "{i}Y-you already said that before..."
    scene ch10_850--
    mc "{i}I’ll be gentle this time, I promise."
    s "{i}Okay, if it feels really good... {/i}{w=0.5}*uhm* {i}t-then I’ll hold on..."
    $ anim_speed = 0.055
    show screen random_anim_speed_slow3 with nothing
    scene ch10_834sfd1_
    play voicefx smoansoft4 volume 0.5 loop
    s "{i}*Ayhnmm.. ouh-hm..."
    mc "{i}Uhh, yeah..."
    mc "{i}Does it hurt?"
    s "{i}*Ahn, uhmm.. uh...*"
    s "{i}N-not much... {/i}*uhhm.. anh...*"
    s "{i}It feels good, *huh, huh...*"
    mc "{i}Do you want me to keep going like this?"
    s "{i}Y-you can keep going like this... *Huh.. hunh...*"
    s "{i}*Uuhn, humn, uh*"
    mc "{i}You moan so cute, you make my heart race."
    s "*huh* {i}When you do ''argh,'' I like it too..."
    mc "{i}Oh, really?"
    s "{i}*Uhn.. ah, uhn* Yeah, it’s sexy..."
    mc "{i}Alright, I’ll try to do it more often then."
    scene ch10_834sfd2_
    pause
    s "{i}*Huh, huyn* -[mc]..."
    mc "{i}Yeah?"
    s "{i}D-don't call me cute anymore..."
    mc "{i}Why not?"
    s "*huh, uh...* {i}I'm not a little girl... Women aren't cute, they're sexy."
    mc "{i}Well, you're both cute and sexy at the same time."
    s "*Uhn, uyh.. uh...* {i}B-but I’m a woman now... who’s already has sex..."
    mc "{i}Even so."
    mc "{i}Besides, I like your cute side..."
    mc "{i}It's one of the things I like most about you."
    s "{i}Uhm... s-so that's okay. B-but I'm not a kid anymore..."
    stop voicefx fadeout 2.0
    pause 1.0
    $ hide_anim_speed()
    $ anim_speed = 0.025
    play voicefx smoansoft3 volume 0.5 loop fadein 2.0
    mc "*Uh* {i}Women can be cute too."
    mc "{i}You're my sweet and cute, *hmgn*{w=0.5}, but above all sexy girlfriend."
    mc "{i}Do you like that better?"
    s "*Hah, ah, uh* {i} Y-yeah..."
    s "I like that... {i}*Hah, ayh, auh...*"
    pause
    scene ch10_834sfd3_
    mc "Uh.. {i}You're taking my cock so well now..."
    mc "{i}How does it feel?"
    s "{i}Hard... and big... {/i}*huh, huym*"
    s "*Hah, ah* {i}[mc]... I-I feel like I'm..."
    mc "{i}Hm?"
    s "{i}*Ah, hah, uhmm...* {i}I want to moan, [mc]..."
    mc "*ngh* {i}You can moan all you want, just not too loud..."
    s "{i}*Aah, Aayhn...*"
    mc "*Mhmn*"
    mc "{i}[s]... *hah* D-do you think you can handle me being a little rougher?"
    s "{i}*Huh, hah, aunh...*"
    s "{i}I-I can take it, y-yes... {/i}*huh, uhmn...*"
    s "{i}Give me... {w=0.5}give me harder{/i}{w=0.5}, *Hun, uhhm*{w=0.5} {i}if you want..."
    $ anim_speed = 0.015
    s "{i}*Aah, hah, aah!*"
    mc "*Hmngh!* {i}[s]!..."
    s "{i}*humn!.. uuhmmnh!* {size=-3}[mc], n-no..."
    s "{i}[mc], i-if you want, you can go slow again... {/i}*hahu, huh, uhm*"
    mc "*Ngh!*{i} I can't, it feels too good... your pussy is sucking me like crazy..."
    s "*Hah, ah, aumh, uhm*"
    $ current_pov = 3
    call screen ch10_834sfd_ with dissolve

    






label ch10_834sfd1_:
    $ current_pov = 1
    scene ch10_834sfd1_ with nothing
    call screen ch10_834sfd_
label ch10_834sfd2_:
    $ current_pov = 2
    scene ch10_834sfd2_ with nothing
    call screen ch10_834sfd_
label ch10_834sfd3_:
    $ current_pov = 3
    scene ch10_834sfd3_ with nothing
    call screen ch10_834sfd_








screen ch10_834sfd_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.04), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.025), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.02), Show("random_anim_speed"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 3:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [SetVariable("current_pov", 2), Jump("ch10_834sfd3_")] style "textbutton_choice"
    
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 2:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [SetVariable("current_pov", 2), Jump("ch10_834sfd2_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        
        if current_pov == 1:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [SetVariable("current_pov", 1), Jump("ch10_834sfd1_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_834sfd3s_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
init python:
    def ch10_834sfd1_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_834sfd1_":
            store.current_active_animation = "ch10_834sfd1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 38 + 1  
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False  
        trans.set_child("ch10_834sfd1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sfd1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 7 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                              "audio/masturbating/cutmastrubating7.ogg",
                              "audio/masturbating/cutmastrubating8.ogg",
                              "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                              "audio/masturbating/cutmastrubating7.ogg",
                              "audio/masturbating/cutmastrubating8.ogg",
                              "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                store.last_played_sound3 = random_sound
                final_volume = max(0.05, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_834sfd2_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_834sfd2_":
            store.current_active_animation = "ch10_834sfd2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 38 + 1  
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False  
        trans.set_child("ch10_834sfd2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sfd2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 7 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                              "audio/masturbating/cutmastrubating7.ogg",
                              "audio/masturbating/cutmastrubating8.ogg",
                              "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                              "audio/masturbating/cutmastrubating7.ogg",
                              "audio/masturbating/cutmastrubating8.ogg",
                              "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                store.last_played_sound3 = random_sound
                final_volume = max(0.05, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_834sfd3_(trans, st, at):
        if store.current_active_animation == "anim":
            pass
        elif store.current_active_animation != "ch10_834sfd3_":
            store.current_active_animation = "ch10_834sfd3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 38 + 1  
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False  
        trans.set_child("ch10_834sfd3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_834sfd3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 7 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                              "audio/masturbating/cutmastrubating7.ogg",
                              "audio/masturbating/cutmastrubating8.ogg",
                              "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 24 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg",
                              "audio/masturbating/cutmastrubating7.ogg",
                              "audio/masturbating/cutmastrubating8.ogg",
                              "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                store.last_played_sound3 = random_sound
                final_volume = max(0.05, 1.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
        return store.anim_speed
image ch10_834sfd1_:
    function ch10_834sfd1_
image ch10_834sfd2_:
    function ch10_834sfd2_
image ch10_834sfd3_:
    function ch10_834sfd3_





init python:
    def ch10_835shf_(trans, st, at):
        if store.current_active_animation != "ch10_835shf_":
            store.current_active_animation = "ch10_835shf_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_835shf_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_835shf_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.3 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 38 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.011:
                    final_volume = max(0.04, 0.1 * fade_multiplier)
                else:
                    final_volume = max(0.04, 0.2 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 22 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_835shf1_(trans, st, at):
        if store.current_active_animation != "ch10_835shf1_":
            store.current_active_animation = "ch10_835shf1_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_835shf1_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_835shf1_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.3 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 38 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.011:
                    final_volume = max(0.04, 0.05 * fade_multiplier)
                else:
                    final_volume = max(0.04, 0.1 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 22 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_835shf3_(trans, st, at):
        if store.current_active_animation != "ch10_835shf3_":
            store.current_active_animation = "ch10_835shf3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_835shf3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_835shf3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 2 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 0.3 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 38 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/slaps/slap_1.ogg", "audio/slaps/slap_2.ogg", "audio/slaps/slap_3.ogg", "audio/slaps/slap_4.ogg", "audio/slaps/slap_5.ogg", "audio/slaps/slap_6.ogg", "audio/slaps/slap_7.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
                store.last_played_sound = random_sound
                if anim_speed > 0.011:
                    final_volume = max(0.04, 0.1 * fade_multiplier)
                else:
                    final_volume = max(0.04, 0.2 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='soundfx')
                renpy.sound.play(random_sound, channel='soundfx')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 22 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed




screen ch10_835shfsc_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.01), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.007), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.0125), Show("random_anim_speed2"), Function(disable_even_frames)] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 2:
            textbutton "Pov 3" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 3" action [Jump("ch10_835shf1_")] style "textbutton_choice"
    
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 1:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 2" action [Jump("ch10_835shf_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        
        if current_pov == 3:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        else:
            textbutton "Pov 1" action [Jump("ch10_835shf3_")] style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_835shfsc_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
image ch10_835shf_:
    function ch10_835shf_
image ch10_835shf1_:
    function ch10_835shf1_
image ch10_835shf3_:
    function ch10_835shf3_
label ch10_835shf_:
    if current_pov == 2:
        scene ch10_835shf_ with Dissolve(0.2)
    elif current_pov == 1:
        scene ch10_835shf_ with Dissolve(0.2)
    else:
        scene ch10_835shf_ with nothing
    $ current_pov = 1
    call screen ch10_835shfsc_ with nothing

label ch10_835shf1_:
    if current_pov == 1:
        scene ch10_835shf1_ with Dissolve(0.2)
    elif current_pov == 2:
        scene ch10_835shf1_ with Dissolve(0.2)
    else:
        scene ch10_835shf1_ with nothing
    $ current_pov = 2
    call screen ch10_835shfsc_ with nothing

label ch10_835shf3_:
    scene ch10_835shf3_ with nothing
    $ current_pov = 3
    call screen ch10_835shfsc_ with nothing

label afterch10_834sfd3s_:
    if current_pov != 2:
        scene ch10_834sfd2_
    $ hide_anim_speed()
    $ anim_speed = 0.0125
    s "{i}[mc], *hah, ah, ah*, [mc]..."
    s "{i}[mc], I-I feel like I'm going to..."
    s "{i}[persistent.name[0]]-[persistent.name]..."
    mc "{i}*Hah, mnh* J-just a little more *hngh!*..."
    s "{i}*Huh, umnh.. uh...*"
    scene ch10_834sfd3_
    mc "*Hah! Hmngh!* {i}C-can you hold on a little longer for me, [s]?"
    s "{i}*Hum... uhhnm*"
    mc "*Ngh!* {i}Th-that’s it, good girl..."
    mc "{i}You’re definitely a full woman now..."
    s "{i}*Hunh, hahum... uhnh...*"
    stop voicefx fadeout 0.5
    scene ch10_835shf_
    play voicefx smoanmid fadein 0.25 volume 0.5 loop
    $ anim_speed = 0.009
    mc "{i}Uh, [s]!... *hmngh!*"
    mc "{i}I-I love you, I love you so much..."
    s "*Hum, uhm, ah!* [mc], [mc]..."
    mc "{i}A-almost there..."
    $ anim_speed = 0.007
    mc "{i}*Gah!* I-I’m almost done, just a little more..."
    s "{i}*Humm, uh, hah, hah, ah!*"
    scene ch10_835shf1_ with Dissolve(0.2)
    s "{i}*A-aey, aumh, a-aynh!*"
    mc "{i}*Hagh!* D-does it hurt? Tell me, does it hurt?"
    s "{i}*uhm, uh-uhmm, a-hah* N-no, I..."
    mc "{i}*Hmngh!*"
    mc "{i}Lift that little ass for me..."
    scene ch10_835shf_ with Dissolve(0.2)
    mc "{i}That's it, just like I showed you. *hah*"
    s "{i}Huyn, uhmn, ahm, ah!*"
    mc "{i}*Hah* God, I love this little butt... and how you lift it so naturally. *hah*"
    scene ch10_835shf3_ with Dissolve(0.2)
    mc "{i}And the way you arch your back... really makes that sexy little ass pop..."
    s "*Hah, ayn, ha, aemh!*"
    mc "I love you, [s]! I love you, my beautiful, little princess!"
    call screen ch10_835shfsc_ with dissolve

label afterch10_835shfsc_:
    if current_pov != 1:
        scene ch10_835shf_
    $ anim_speed = 0.007
    s "*Ahn!... huhmn!* {i}[persistent.name[0]]-[persistent.name], uynh! *uymnh...*"
    mc "*hmng* (Calm down, [mc], you’re being too rough. Remember, it’s her first time!)" with dissolve
    scene ch10_835shf_1 with hpunch
    stop voicefx fadeout 1.0
    mc "*Hargh!* {w=0.7}{nw}"
    mc "*Huh* (Hold it in, hold it in!...)" with dissolve
    pause 0.75
    scene ch10_835shf_25
    play voicefx smoansoft4 volume 0.3 loop fadein 1.0
    pause 0.75
    mc "*Uhh...*"
    mc "{i}(I don't know how, but I managed to held it...)" with dissolve
    image ch10_852anims:
        "ch10_852" with Dissolve(0.1)
        0.15
        "ch10_852-" with Dissolve(0.1)
        0.15
        "ch10_852" with Dissolve(0.1)
        0.15
        "ch10_852-" with Dissolve(0.1)
        0.15
        "ch10_852" with Dissolve(0.1)
        1.0

        "ch10_852-" with Dissolve(0.1)
        0.15
        "ch10_852" with Dissolve(0.1)
        1.0
        "ch10_852-" with Dissolve(0.1)
        0.15

        "ch10_852" with Dissolve(0.1)
        0.15
        "ch10_852-" with Dissolve(0.1)
        0.15
        "ch10_852" with Dissolve(0.1)
        1.0
        repeat
    camera:
        subpixel True
        ease 0.5 zoom 1.005 
        xalign 0.5 
        yalign 0.5
        parallel:
            align (0.5, 0.5)
            around (0.501, 0.5)
            linear 3.0 counterclockwise circles 1
            around (0.499, 0.5)
            linear 3.0 clockwise circles 1
            repeat
    scene ch10_852anims with dissolve
    mc "{i}Uh?... {w=0.7}{nw}"
    s "*Huhm, uhn, uhmm...*"
    mc "{i}A-are you...?" with dissolve
    s "*Umh.. auhm.. uuh-uh...*"
    scene ch10_835shf_ with hpunch
    play voicefx smoanmid fadein 0.25 volume 0.5 loop
    mc "*Hagh!*"
    mc "{i}Even though it’s your first time, y-you’re enjoying it... and you even had an orgasm!"
    mc "{i}God, you’re so sexy! I can’t hold back!{/i}*Argh*"
    s "*Auh, uhhmm, uhn, ou!*"
    play voicefx smoansoft4 volume 0.5 loop
    scene ch10_835shf_25
    pause 0.5
    scene ch10_835shf_1 with hpunch
    pause 0.63
    scene ch10_835shf_25
    pause 0.75
    scene ch10_835shf_1 with hpunch
    pause 1.0
    scene ch10_835shf_25
    pause 1.0
    scene ch10_835shf_1 
    pause 1.0
    scene ch10_835shf3_
    play voicefx smoanmid fadein 0.25 volume 0.5 loop
    mc "*Hah, gah*"
    scene ch10_853 with vpunch
    stop voicefx fadeout 0.1
    mc "*Argh!*{w=1.0}{nw}"
    scene ch10_854
    pause 1.0
    play voicefx smoansoft fadein 0.25 volume 0.75 loop
    mc "A-ah..." with dissolve
    s "{i}{size=-3}*a-ah-ha.. uh...*"
    s "{i}You spilled it on my back... *huh*..."
    image ch10_854_anim:
        "ch10_854_1" with Dissolve(0.1)
        0.15
        "ch10_854_2" with Dissolve(0.1)
        0.15
        "ch10_854_1" with Dissolve(0.1)
        1.0

        "ch10_854_2" with Dissolve(0.1)
        0.15
        "ch10_854_1" with Dissolve(0.1)
        0.15
        "ch10_854_2" with Dissolve(0.1)
        0.15
        "ch10_854_1" with Dissolve(0.1)
        1.0

        "ch10_854_2" with Dissolve(0.1)
        0.15
        "ch10_854_1" with Dissolve(0.1)
        0.15
        "ch10_854_2" with Dissolve(0.1)
        0.15
        "ch10_854_1" with Dissolve(0.1)
        0.15
        "ch10_854_2" with Dissolve(0.1)
        0.15
        "ch10_854_1" with Dissolve(0.1)
        1.0
        repeat
    scene ch10_854_anim
    mc "{i}(She’s still having pleasure spasms...)" with dissolve
    mc "{i}(I think I came inside her a little too...)" with dissolve
    mc "{i}(I tried to pull out in time, but I couldn’t. I hardly ever miss...)" with dissolve
    mc "{i}(There’s nothing like a virgin pussy...)" 
    s "*Huh, uhm...*"
    mc "{i}My cock is still rock hard..."
    mc "{i}I want to keep going, I’m really enjoying this..."
    stop voicefx fadeout 1.5
    scene ch10_836___
    s "{i}[persistent.name[0]]-[persistent.name], but not too rough this time..."
    mc "{i}Does it hurt when I go too fast?"
    s "{i}Your dick is too large... it stings deep inside, th-that hurts, [mc]..."
    mc "{i}Lie on your side, we're gonna try something different."
    camera:
        ease 3.0 xalign 0.5 yalign 0.5 zoom 1.0
    scene ch10_836__
    s "{i}D-did you really enjoy it that much?"
    mc "{i}It was beautiful, like a dream come true."
    scene ch10_836_
    s "{i}[persistent.name[0]]-[persistent.name], remember, not too rough..."
    mc "{i}Thist way it won’t go all the way in. I’ll just put in the tip."
    mc "{i}Why didn’t you tell me it hurt, hmm?"
    s "{i}[k] never tells you to stop... and she screams a lot."
    mc "{i}E-everybody’s different, [s]. If it hurts you, you have to tell me."
    scene ch10_836sflay2_1
    s "*hah, uh...*"
    scene ch10_836sflay2_30
    s "*uh, uhm...*"
    $ hide_anim_speed()
    $ anim_speed = 0.05
    scene ch10_836sflay2_
    play voicefx smoansoft4 volume 0.5 loop fadein 1.0
    pause
    mc "{i}Does it hurt?"
    s "*huh, uh*..."
    pause
    mc "{i}Do you like it?"
    s "{i}Yes... *uhm*"
    pause
    mc "{i}Can I go a little faster?"
    s "{i}Y-yeah, *huh*..."
    $ anim_speed = 0.025
    play voicefx smoansoft3 loop volume 0.5 fadein 0.5
    pause
    scene ch10_836sflay3_
    pause
    mc "{i}Uh, you’re so tight..."
    mc "{i}I love you... Your tiny body drives me crazy..."
    mc "{i}Those beautiful legs... I can’t get enough of them, I want them to be mine forever."
    pause
    scene ch10_836sflay2_
    pause 
    scene ch10_836sflay4_
    $ anim_speed = 0.018
    mc "*Uh* {i}Uh, this feels so good..."
    mc "{i}Your pussy’s squeezing me so nicely..."
    s "*Hah, ah* {i}My pussy’s yours now, you can have sex with it whenever you want..."
    mc "{i}Uhngh! s-say it again..."
    s "*huh, aah* I’m yours... *huh* M-my pussy is yours, [mc]..."
    play voicefx smoanmid volume 0.4 loop fadein 0.5
    $ anim_speed = 0.01
    mc "*Hagh* {i}Uh..."
    mc "{i}And you can have my dick whenever you want, it’s yours too."
    pause
    scene ch10_836sflay5_
    call screen ch10_836sflay_ with dissolve

default ch10_836ol = False

screen ch10_836sflay_:
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 0.015), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.01), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.007), Function(hide_anim_speed), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.45
        textbutton "Auto" action [SetVariable("anim_speed", 0.0125), Show("random_anim_speed2"), Function(disable_even_frames)] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.3
        if current_pov == 1:
            textbutton "Pose 2" action [Jump("ch10_836sflay4_")] style "textbutton_choice"
        elif current_pov == 2:
            textbutton "Pose 2" action [Jump("ch10_836sflay5_")] style "textbutton_choice"
        elif current_pov == 3:
            textbutton "Pose 1" action [Jump("ch10_836sflay2_")] style "textbutton_choice"
        elif current_pov == 4:
            textbutton "Pose 1" action [Jump("ch10_836sflay3_")] style "textbutton_choice"
        
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 4 and ch10_836ol == True:
            textbutton "Pov 2"  style "textbutton_choice"
        elif current_pov != 4 and ch10_836ol == True:
            textbutton "Pov 2" action [Jump("ch10_836sflay5_")] style "textbutton_choice"
        else:
            text ""
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 3 and ch10_836ol == True:
            textbutton "Pov 1"  style "textbutton_choice"
        elif current_pov != 3 and ch10_836ol == True:
            textbutton "Pov 1" action [Jump("ch10_836sflay4_")] style "textbutton_choice"
        else:
            text ""
    
    hbox:
        yalign 0.05
        xalign 0.99
        
        if current_pov == 2 and ch10_836ol == False:
            textbutton "Pov 2" style "textbutton_choice" sensitive False
        elif current_pov != 2 and ch10_836ol == False:
            textbutton "Pov 2" action [Jump("ch10_836sflay3_")] style "textbutton_choice"
        else:
            text ""
    hbox:
        yalign 0.05
        xalign 0.89
        
        if current_pov == 1 and ch10_836ol == False:
            textbutton "Pov 1" style "textbutton_choice" sensitive False
        elif current_pov != 1 and ch10_836ol == False:
            textbutton "Pov 1" action [Jump("ch10_836sflay2_")] style "textbutton_choice"
        else:
            text ""
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Function(hide_anim_speed), Jump("afterch10_836sflay5_")] style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label ch10_836sflay2_:
    $ ch10_836ol = False
    $ current_pov=1
    scene ch10_836sflay2_
    call screen ch10_836sflay_
label ch10_836sflay3_:
    $ ch10_836ol = False
    $ current_pov=2
    scene ch10_836sflay3_
    call screen ch10_836sflay_
label ch10_836sflay4_:
    $ ch10_836ol = True
    $ current_pov=3
    scene ch10_836sflay4_
    call screen ch10_836sflay_
label ch10_836sflay5_:
    $ ch10_836ol = True
    $ current_pov=4
    scene ch10_836sflay5_
    call screen ch10_836sflay_
image ch10_836sflay2_:
    function ch10_836sflay2_
image ch10_836sflay3_:
    function ch10_836sflay3_
image ch10_836sflay4_:
    function ch10_836sflay4_
image ch10_836sflay5_:
    function ch10_836sflay5_
init python:
    def ch10_836sflay2_(trans, st, at):
        if store.current_active_animation != "ch10_836sflay2_":
            store.current_active_animation = "ch10_836sflay2_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_836sflay2_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_836sflay2_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_836sflay3_(trans, st, at):
        if store.current_active_animation != "ch10_836sflay3_":
            store.current_active_animation = "ch10_836sflay3_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_836sflay3_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_836sflay3_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed


init python:
    def ch10_836sflay4_(trans, st, at):
        if store.current_active_animation != "ch10_836sflay4_":
            store.current_active_animation = "ch10_836sflay4_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_836sflay4_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_836sflay4_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
init python:
    def ch10_836sflay5_(trans, st, at):
        if store.current_active_animation != "ch10_836sflay5_":
            store.current_active_animation = "ch10_836sflay5_"
            if not (store.current_active_animation and "anim" in store.current_active_animation):
                renpy.sound.stop(channel='sound')
                renpy.sound.stop(channel='soundfx')
            store.fade_in_counter = 0
            store.fade_in_active = True
        if store.last_anim_speed != store.anim_speed:
            current_progress = (st - store.start_time) / store.last_anim_speed
            store.start_time = st - (current_progress * store.anim_speed)
            store.last_anim_speed = store.anim_speed
        elapsed_time = st - store.start_time
        new_frame = int(elapsed_time / store.anim_speed) % 40 + 1
        if new_frame != store.frame_num:
            store.prev_frame_num = store.frame_num
            store.frame_num = new_frame
            store.sound_played_this_cycle = False
        trans.set_child("ch10_836sflay5_{}".format(store.frame_num))
        if store.current_active_animation == "ch10_836sflay5_":
            fade_multiplier = get_fade_volume_multiplier()
            if store.prev_frame_num < 6 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound
                final_volume = max(0.1, 4.0 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                store.sound_played_this_cycle = True
            if store.prev_frame_num < 15 <= store.frame_num and not store.sound_played_this_cycle:
                sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
                random_chance = renpy.random.random()
                final_volume = max(0.05, 0.5 * fade_multiplier)
                renpy.sound.set_volume(final_volume, channel='sound')
                renpy.sound.play(random_sound, channel='sound')
                if random_chance < 0.3: store.last_played_sound3 = random_sound
                store.sound_played_this_cycle = True
        return store.anim_speed
label afterch10_836sflay5_:
    $ anim_speed = 0.009
    if current_pov != 3:
        scene ch10_836sflay4_ with Dissolve(0.2) 
    mc "*Hngh!* [s]..."
    s "{i}*Huh, uh, ah!* [mc], [mc]..."
    stop voicefx fadeout 0.5
    image ch10_860_anim:
        "ch10_860" with Dissolve(0.2)
        0.5
        "ch10_861" with hpunch
        1.0
        repeat 3
    scene ch10_860_anim with Dissolve(0.2)
    play voicefx smoansoft3 volume 0.5 fadein 0.5 loop
    mc "*Aargh!*"
    pause
    play voicefx smoansoft volume 0.5 fadein 3.0 loop
    scene ch10_862
    mc "Uh... God..."
    s "*Hn, huh, uh...*"
    pause
    mc "{i}(I came pretty hard...)" with dissolve
    mc "{i}(But I still want more... I need more of this body.)" with dissolve
    s "*Huh... uh...*"
    s "*Huh*... [mc]..."
    stop voicefx fadeout 0.5
    scene ch10_844
    s "*Huh* {i}You've already spilled your semen on me twice..."
    mc "{i}Yeah..."
    scene ch10_844--
    pause
    scene ch10_844---
    play voicefx "audio/character/s/soft/s_moan_soft_1.ogg" volume 0.5
    s "Uh..."
    mc "{i}(My cock slides in a bit easier now.)"
    scene ch10_834sf3_
    play voicefx smoansoft4 volume 0.4 loop
    show screen random_speed(0.02, 0.03)
    s "*Ah, hah, unh*"
    mc "{i}(It feels way too good...)"
    mc "{i}(I can't stop fucking her even after two loads.)" with dissolve
    hide screen random_speed with nothing
    stop voicefx fadeout 0.1
    show screen random_speed(0.009, 0.01)
    play voicefx smoanmid volume 0.4 loop fadein 0.1
    mc "{i}(I still can’t get enough of this tight, delicious pussy!)" with dissolve
    mc "*Hah, hah*"
    s "*Huh, ah, ah* [persistent.name[0]]-[persistent.name]..."
    pause
    scene ch10_834sf1_
    s "*Huh, uh, uhn* {i}W-we've been having so much sex..."
    mc "*Hah* {i}Yeah... {w=0.5}*ngh*{w=0.5} It’s because I have such a beautiful girlfriend."
    s "*Huh, uh, ah-ayhn* [mc], I love you so much..."
    mc "*Hah* {i}I love you way more."
    scene ch10_834sf2_
    mc "*Hah* {i}Do you like having sex with me? Are you enjoying it?"
    s "*Uh, hun, ah* {i}Yes, I love having sex with you, [mc]..."
    s "*Ah, ah* {i}I really do..."
    mc "{i}*Nghah!* I’m about to come..."
    s "*Ah, uhsm* {i}Are you gonna cum inside me?"
    mc "{i}Huh?"
    s "*Ah, huh, uyhm* {i}You can cum inside my pussy, [mc]..."
    mc "*Hagh* {i}I-inside? You want me to cum inside?"
    s "*Huh, ah, ah*"
    scene ch10_834sf3_ at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with Dissolve(0.2)
    show screen random_speed(0.008, 0.01)
    mc "*Ngah!*"
    mc "(After two rounds... I’m about to cum again, and so fast...)" with dissolve
    mc "(I can’t do it inside again, it’s too risky...)" with dissolve
    mc "(But... {w=0.5}it would be amazing... {w=0.5}I shouldn’t but...)" with dissolve
    scene ch10_834-----
    pause 0.7
    scene ch10_834----
    pause 0.7
    scene ch10_855
    stop voicefx fadeout 0.5
    pause 0.7
    scene ch10_856
    play voicefx smoansoft4 volume 0.35 loop
    mc "Hah..."
    scene ch10_857
    pause 0.7
    scene ch10_857-
    mc "Uh...{w=0.7}{nw}"
    scene ch10_857--
    pause
    stop voicefx fadeout 0.1
    image ch10_863anim:
        "ch10_863---" with Dissolve(0.1)
        pause 1.0
        "ch10_863----" with Dissolve(0.1)
        pause 0.2
        "ch10_863---" with Dissolve(0.1)
        pause 0.2
        "ch10_863----" with Dissolve(0.1)
        pause 0.2
        "ch10_863---" with Dissolve(0.1)
        pause 3.0
        "ch10_863----" with Dissolve(0.1)
        pause 0.2
        repeat
    show ch10_863anim with dissolve:
        zoom 1.0 xalign 0.5 yalign 1.0
    mc "(I-I didn’t manage to pull out in time...)" with dissolve
    play voicefx smoansoft volume 0.25 loop
    show ch10_863anim:
        subpixel True
        ease 10 zoom 0.5 xalign 0.5 yalign 0.5
    s "*Huh... {w=0.5}hyn...*"
    $ renpy.pause(4.0, hard=True)
    s "{i}{w=0.5}Huh... uh... [mc]..."
    mc "Hah... uff..."
    pause
    mc "Are you okay?"
    mc "Was I too rough?"
    s "*Huh* Y-yeah, you were..."
    $ stop_sounds(1.0)
    scene ch10_864
    mc "It’s just... you’re so beautiful, I couldn’t control myself."
    s "{i}It’s okay... uh..."
    s "{i}I-I liked it... even if it hurt... I liked it..."
    pause
    scene ch10_864-
    mc "{i}My princess..."
    mc "{i}Sorry, beautiful..."
    s "{i}It’s okay, [mc]."
    scene ch10_865
    s "{i}I-I liked it... Even if sometimes you were rough, it felt good..."
    mc "{i}Next time I’ll be more careful."
    scene ch10_866
    s "{i}Next time?"
    s "{i}Does that mean we’re still going to be a couple?"
    mc "{i}A couple?"
    scene ch10_873
    s "{i}Yes."
    s "{i}Don't you remember?"
    mc "{i}Sorry, my mind went completely blank. I forgot I have a cute girlfriend now."
    s "{i}You dummy..."
    mc "{i}It’s pretty late already."
    s "{i}Yeah, I think I should go to my room."
    mc "{i}Don’t you want to stay and sleep with me tonight?"
    s "{i}Yes!"
    mc "{i}Alright then."
    scene ch10_872
    s "{i}Good night."
    mc "{i}Good night."
    $ renpy.end_replay()
    call screen chapter10end with Dissolve(5.0)

label ch10_slfalse:
    stop music fadeout 1.0
    scene blackscreen 
    pause
    scene ch10_587 with fade
    play background "audio/fairsfx.ogg" volume 0.18 loop fadein 1.0
    pause
    scene ch10_601 with fade
    pause
    scene ch10_600 with fade
    pause
    scene ch10_602 with fade
    pause
    scene ch10_645 with fade
    pause
    scene ch10_642 with fade
    pause
    scene ch10_660 with fade
    pause
    scene ch10_674
    mc "[s], will you stay here while I go get more tickets? I'm all out and we still haven't gotten on the Ferris wheel."
    s "Yeah, I'll wait here."
    mc "Alright, I'll be right back, okay?"
    scene ch10_675 with fade
    "Sorry, your card was declined."
    mc "No way... This morning I had nearly eight hundred dollars." 
    mc "(Oh come on... First Steam, now this? Do these payment companies run everything now?)"
    scene ch10_676
    mc "(Amazing... As if controlling online platforms wasn't enough, now they're gatekeeping my daily expenses too.)"
    mc "What the hell?..."
    pause
    mc "Huh? -Five dollars!?..."
    mc "This has gotta be a mistake."
    mc "{i}(Where did I spend so much money?)" with dissolve
    mc "{i}(There’s a payment for...)" with dissolve
    mc "{i}(Six hundred ninety-nine!...)" with hpunch
    mc "{i}(This can’t be, someone might've used my card)" with dissolve
    pause
    s "[mc]."
    scene ch10_678
    mc "You already threw all five darts?"
    s "Yeah. What are you doing?"
    mc "I’m calling the bank..."
    mc "Wait a sec... when we went shopping you asked me for three hundred, right?"
    mc "I should have at least two hundred dollars left in my account."
    scene ch10_679
    s "Heh..."
    s "..."
    mc "Do you know something about this...?"
    scene ch10_680
    pause
    mc "Don't tell me you..."
    pause
    scene ch10_681
    s "B-but look, it’s a good brand!"
    s "It’s a Vouis Luiton! These bags actually go up in value over time and get more expensive..."
    mc "[s]..."
    s "Uhm..."
    scene ch10_680
    s "W-well, that's what the guy at the store said..."
    mc "[s], you spent my entire week’s paycheck on that bag..."
    pause
    scene ch10_682
    pause
    s "Sorry, I thought you wouldn’t care."
    s "Are you mad?"
    mc "I'm gonna have to call [drelat] [d] to see if he can send me some cash." 
    s "Don’t worry, I have money. I can pay for everything, okay?"
    pause
    scene blackscreen
    pause
    scene ch10_683-
    pause
    s "Are you mad?"
    mc "No, I’m fine."
    pause
    scene ch10_684
    s "[mc]..."
    s "You don’t sound happy."
    pause
    s "[mc]!"
    scene ch10_685
    s "I will pay you back, I just need a few days..."
    mc "It's okay. Money comes and goes. (Yeah...)" with dissolve
    pause
    mc "Where are you gonna get all that money to pay me back by the way?"
    scene ch10_686
    s "[drelatks!cl] pays me to spy on you and [k]."
    mc "W-what!?" with hpunch
    scene ch10_687
    mc "[s]!"
    s "B-but I don’t tell him anything!"
    mc "What do you mean you don't tell him anything? Then why does he pay you?"
    mc "You didn't tell him what you saw today, right?"
    s "N-no, of course not! I swear!"
    mc "And how do I know you're telling the truth?"
    scene ch10_686
    s "Well..."
    pause
    mc "He pays you for gossip?"
    s "Not exactly for gossip. He gives me money every week to tell him stuff. And if nothing happens, he still gives me money."
    s "I never tell him anything important."
    s "Sometimes I even lie to keep you out of trouble..."
    mc "Sometimes?"
    s "When you do stuff with [k]... -I tell him I didn’t see anything."
    mc "[s]..."
    mc "How do I know I can trust you now?"
    s "I didn’t tell him anything about what happened today either."
    scene ch10_687
    s "I swear I won’t say anything, really!"
    pause
    mc "{i}(If she had told him anything, [drelat] [d] would've kicked me out already.)" with dissolve
    mc "{i}(They say there's no better partner in crime than an accomplice...)" with dissolve
    pause
    s "But don't stay mad, when [drelatks] pays me, I'll give you back every penny, seriously."
    mc "I don't want you to pay me back, it's my gift to you."
    mc "{i}(I can't afford to be picky right now...)" with dissolve
    scene ch10_686
    s "[mc], I don't know if you knew, but the bag cost fifteen hundred."
    mc "F-fifteen hundred? So you paid the other thousand?"
    s "Of course!"
    mc "And where'd you get that from?"
    s "From my job!"
    s "You mean spying on us?"
    s "Uh-huh. He gives me fifty a week, and fifteen bucks for each piece of gossip."
    s "Uh, maybe... Some gossips are worth more."
    s "Like the one I told him at the beach, about you guys drinking beer, heh..."
    mc "[s]..."
    scene ch10_687
    s "It’s okay, I know what to tell him. I only give him gossips I know won’t get you in trouble."
    mc "Next time, tell me first what you’re going to tell him, okay?"
    s "Okay."
    scene ch10_686
    pause
    mc "A thousand dollars..."
    mc "I think he pays you better than me..."
    s "Well, I’ve got a few years of experience."
    mc "That’s true."
    scene ch10_718 with fade
    pause
    scene ch10_766-
    "Hey, are you leaving?"
    s "Yeah."
    "Wait a second."
    scene ch10_766--
    "You guys did like ten tries, right?"
    "If you give me ten bucks, I'll let you pick any big teddy bear you want, how's that sound?"
    s "Really?"
    "Yeah, the fair's closing soon anyway, and those bears usually get lost or damaged on the way back."
    scene ch10_766---
    s "[mc], can I get one?"
    mc "Sorry, [s]. I’m out of money."
    scene ch10_766----
    s "Oh right, I forgot..."
    s "Which one do you like best?"
    mc "Me?"
    s "Yeah, I've got money."
    mc "Pick whichever one you like the most."
    s "I want whatever one you want..."
    mc "No, you pick."
    s "No, you."
    scene ch10_766-----
    "I'll give you this one, since you two can't make up your minds."
    s "Yeah, thanks."
    scene ch10_767 with fade
    pause
    stop background fadeout 1.5
    scene blackscreen with dissolve
    pause
    call screen chapter10end with Dissolve(5.0)








