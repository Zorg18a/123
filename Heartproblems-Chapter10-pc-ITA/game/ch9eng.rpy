label ch9at:
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    scene ch9_2 with Dissolve(2.0)
    pause
    mc "..."
    scene ch8_1022- with flash
    mc "..."
    mc "(It really happened... I can still remember her lips caressing every part of my cock...)" with dissolve
    mc "(It was so damn hot.)" with dissolve
    mc "(I'm sure no one had ever touched or tasted her like I did.)" with dissolve
    scene ch9_2 with Dissolve(2.0)
    mc "Wow..."
    pause
    scene ch9_3 with dissolve
    mc "(It smells delicious, [a] must be making breakfast already.)" with dissolve
    mc "(I was hoping to wake her up myself, but she always gets up earlier.)" with dissolve
    mc "(Even these last few days when I've gone to work, she was already awake to make me breakfast.)" with dissolve
    mc "(I'm lucky to have [a], without her I know my life wouldn't be as good.)" with dissolve
    pause
    play music scene1 fadein 1.0
    scene ch9_4 with fade:
        zoom 0.75
    a "{i}{size=-2}I don't want to talk about it anymore, [d]."
    d "{i}{size=-2}Do you think that's the way to solve things?"
    pause
    scene ch9_5 with dissolve
    d "{i}{size=-2}So is this how it's going to be?"
    pause
    d "{i}{size=-2}And how long do you plan to ignore the issue?"
    d "{i}{size=-2}We need to fix this, the girls notice, you know?"
    pause
    d "{i}{size=-2}Don't stay silent, say something!"
    a "{i}{size=-2}I'm making breakfast, [d]."
    d "{i}{size=-2}And?"
    d "{i}{size=-2}Can't you talk while you cook?"
    scene ch9_6- with dissolve
    d "Answer me, [a]."
    d "{i}{size=-2}[a], you don't know the harm you're causing me by acting so cold..."
    d "{i}{size=-2}Y-you make me feel like garbage when all I want is to bring you happiness and support."
    d "{i}{size=-2}[a], I want to fix things, I truly do, but you have to meet me halfway."
    pause
    a "{i}{size=-2}So you admit it."
    d "{i}{size=-2}See? You're just looking for someone to blame, you don't want to fix anything. You want me to pay for something you're not even sure about."
    d "*Exhales* I love you, [a], I love you more than anything in this world."
    scene ch9_8-- with dissolve
    mc "Good morning."
    a "Good morning, sweetheart."
    d "Good morning, [mc]."
    scene ch9_9- with dissolve
    a "Go ahead and sit down at the table, honey, breakfast is almost ready."
    mc "Hmm, it smells delicious. What are we having for breakfast?"
    a "Eggs with bacon."
    d "Honey, we could use a bit of variety for breakfast sometimes, heheh."
    a "I woke up a little later today, so I didn't have time to make anything else."
    scene ch9_11- with dissolve
    a "I didn't know you were already tired of fried eggs."
    mc "Nah, we're not that picky in this house."
    d "Erm, yeah, exactly."
    d "As long as it fills us up, we're good, right, [mc]?"
    mc "Totally, as long as it fills my stomach, I'm happy."
    scene ch9_13- with dissolve
    mc "(That pair looks delicious, and I'm not talking about what's on the pan...)" with dissolve
    mc "Besides, if it's cooked by you, I could eat fried eggs all the time."
    d "Definitely, even if they're just simple eggs, your cooking makes them taste like caviar, heheh."
    a "I'm glad to hear that, heh..."
    scene ch9_10- with dissolve
    mc "So tell me, how did the most beautiful [arelat] in the world wake up?"
    a "Are you talking about me?"
    mc "Is there another [arelat] around here that fits those descriptions?"
    scene ch9_11- with dissolve
    d "I'm handsome, but I think he's referring to you, love, heh."
    a "Oh, haha..."
    scene ch9_14--- with dissolve
    a "Aww, you're sweet."
    a "I slept... {w=0.5} g-great!"
    a "Yeah, I slept really well."
    a "Uhm, how about you?"
    mc "I did too... Actually, even better than usual..."
    a "Oh, really...?"
    scene ch9_14---- with dissolve
    mc "Yes, don't you remember?"
    a "I-I don't know, I didn't see you sleeping, heh..."
    mc "Ah! Haha, good point. N-no {w=0.35}, it's just that... I had such a good time yesterday that I went straight to bed, I was exhausted."
    d "Yeah, I went straight to bed too."
    d "I'm glad you had fun; I knew you would like the place."
    scene ch9_14- with dissolve
    mc "We loved it, right?"
    a "Yeah, it was a lot of fun..."
    mc "*Sniff, sniff* Hm?"
    mc "[arelat!cl] [a], did you put on yesterday's perfume again?"
    a "N-no, {i}{size=-3}how embarrassing."
    a "I was so tired that I decided not to shower."
    d "We should go out together as a family more often; I had a fantastic time too."
    scene ch9_15- with dissolve
    d "I saw you drinking like a champ, [mc], you can really hold your liquor, huh?"
    mc "The one drinking like a champ was you, [drelat] [d]! Haha."
    d "But you too! Every time I looked over, you were pouring yourself another glass of wine."
    mc "They were yours! When one glass was empty, you asked me to fill the next one, haha."
    d "Oh, really?"
    mc "Yeah, I don't know how much you drank, but it was a lot— you even finished the bottle and asked for another."
    d "Did I really drink that much? Oh my God."
    d "But hey, I definitely saw [a] having a few glasses herself; she can't deny that."
    scene ch9_15--- with dissolve
    a "Um, yeah!"
    a "I did drink a little, heh..."
    a "I-I don't remember much from last night either."
    mc "Don't worry, I remember everything... I have a memory of every second from yesterday..."
    scene ch9_15---- with dissolve
    $ renpy.pause(0.5, hard=True)
    scene ch9_15--- with dissolve
    d "Wine can be sneaky, you don’t realize how drunk you are until you try to stand up and it hits you."
    k "Good morning."
    scene ch9_17- with dissolve
    a "Good morning, sweetheart."
    a "Do you know if [s] has woken up yet?"
    k "I don't know."
    a "Can you go wake her up so she can come for breakfast, please?"
    scene ch9_18- with dissolve
    mc "I'll go."
    a "Thank you, honey."
    stop music fadeout 1.0
    scene blackscreen with dissolve
    pause
label ch9s1:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
    play music scene2 fadein 1.0
    scene ch9_19 with dissolve
    pause
    mc "[s], wake up."
    mc "It's time for breakfast."
    pause
    scene ch9_20 with dissolve
    mc "Wake up, [s]."
    mc "(She's still very asleep...)" with dissolve
    pause
    scene ch9_21 with dissolve
    pause
    mc "[s], it's daytime, wake up."
    scene ch9_24 with dissolve
    s "Hngmm..."
    pause
    scene ch9_25 with dissolve
    s "{i}*Nom, nom*..."
    mc "[s]..."
    pause
    mc "(No response...)" with dissolve
    scene ch9_28-2 with dissolve
    mc "[s]."
    mc "(She really is a heavy sleeper...)" with dissolve
    mc "(What a cute little butt...)" with dissolve
    mc "..."
    if stephloving == "True":
        pause
        scene ch9_27 with dissolve
        mc "[s]."
        mc "[s]!" with hpunch
        pause
        scene ch9_29 with dissolve
        pause
        mc "..."
        scene ch9_30- with dissolve
        pause
        mc "([s] is developing very well...)" with dissolve
        pause
        show ch9_30-- with dissolve:
            subpixel True
            yalign 1.0
            xalign 0.5
            ease 10 zoom 0.5 yalign 0.0   
        $ renpy.pause(3.5, hard=True)  
        mc "(Genetics are a wonderful thing.)" with dissolve
        pause
        scene ch9_28-2 with dissolve
        mc "(What the hell am I doing?)" with dissolve
        mc "(Touching my little [srelat] while she's asleep, I should be ashamed...)" with dissolve
        menu:
            with dissolve
            "[JGR]Touch her":
                mc "(I should...)"
                pause
                mc "(I no longer have the mental strength to deny it...)" with dissolve
                mc "(She's a beautiful girl...)" with dissolve
                pause
                mc "(...){w=1.0} (Just a little.)" with dissolve
                scene ch9_28-3 with dissolve
                pause
                mc "(Oh...)" with dissolve
                mc "(So cute and round... I just want to devour it.)" with dissolve
                mc "..."
                pause
                mc "(She would like it, wouldn't she?)" with dissolve
                mc "(She's always teasing me to do naughty things to her, this wouldn't be any different... Right?)" with dissolve
                scene ch9_28-4 with dissolve
                pause
                mc "*Sniff* Hmm..."
                pause
                scene ch9_28-5 with dissolve
                mc "(It's so soft and smells so good...)" with dissolve
                pause
                scene ch9_28-6 with dissolve
                mc "(I think that's enough.)" with dissolve
                mc "(Though...{w=0.5} a little more wouldn’t hurt, right?)" with dissolve
                scene ch9_28-5 with dissolve
                mc "*Sniff* Hmmm, (It feels so good having these cheeks hugging my face...)" with dissolve
                pause
                scene ch9_28-4 with dissolve
                mc "(I could stay here for half an hour...)" with dissolve
                mc "(This is beautiful...)" with dissolve
                mc "(Yeah, I'm a degenerate, so what?)" with dissolve
                mc "*Hmmm* (I can't keep fighting my desires, I admit it, I like my sweet [srelat] [s].)" with dissolve
                mc "Damn..."
                pause
                scene ch9_28-3 with dissolve
                mc "(I need to see this cute little butt, and these panties are in the way...)" with dissolve
                mc "(But... what if she wakes up?)" with dissolve
                mc "(I know she wouldn't get mad but...{w=0.5} I don't know, it would be an awkward situation to explain.)" with dissolve
                pause
                mc "Fuck it."
                scene ch9_28-8 with dissolve
                pause
                mc "(Slowly...)" with dissolve
                pause
                scene ch9_28---1 with dissolve
                mc "(Beautiful.)" with dissolve
                mc "(I just want to squeeze it and kiss it...)" with dissolve
                pause
                mc "(A quick squeeze and that's it.)" with dissolve
                scene ch9_28------- with dissolve
                mc "Hmm..."
                pause
                scene ch9_28--------- with dissolve
                mc "(So sexy!...)" with dissolve
                pause
                scene ch9_29_ with dissolve
                mc "(I just have to do it; I can’t resist burying my face in those juicy cheeks.)" with dissolve
                pause
                play music sexy3 fadein 1.5
                scene ch9_29--- with dissolve
                mc "*Sniff, sniff* Hmm, hmm..."
                mc "(Oh my god, this is beyond exciting.)" with dissolve
                pause
                scene ch9_29__ with dissolve
                mc "*Hahh* (That was incredibly satisfying; I can hardly put it into words.)" with dissolve
                mc "(The fact that she’s asleep makes it even more thrilling...)" with dissolve
                pause
                scene ch9_29--- with dissolve
                mc "*Sniff* Hmph... hmm.."
                pause
                scene ch9_29-- with dissolve
                mc "*Hah!* (Damn, I can’t help but keep smelling her—it’s intoxicating.)" with dissolve
                mc "*Sniff* Hmph, hmmmph!"
                s "Hmn... huh..."
                pause
                mc "(Shit, she's waking up!)" with dissolve
                scene ch9_28- with vpunch
                pause
                scene ch9_25 with dissolve
                mc "[s], wake up, i-it's time for breakfast."
                s "Hmng... uhh..."
                $ renpy.end_replay()
                jump ch9_ssleepafer1

            "Wake her up":
                $ renpy.end_replay()
                jump ch9_ssleepafer1


    else:
        $ renpy.end_replay()
        jump ch9_ssleepafer

label ch9_ssleepafer:
    scene ch9_25 with hpunch
    mc "¡¡¡[s]!!!!"
    scene ch9_25- with dissolve
    s "Huh?"
    jump ch9_ssleepafer1
label ch9_ssleepafer1:
    scene ch9_25 with dissolve
    s "W-what's going on? Uhh..."
    mc "It's time for breakfast, wake up."
    if stephloving != "True":
        s "I'm coming..."
        mc "Hurry up, or it'll get cold."
        s "Yeah, I'll be right there."
        jump ch9_sktchn
    play music scene1 
    scene ch9_33 with hpunch
    s "Nooo! I overslept!"
    mc "What's wrong?"
    scene ch9_32 with dissolve
    s "I didn't wake up in time..."
    mc "For what?"
    s "You know, for the sexy things..."
    mc "Oh, that..."
    s "I don't want to wait until tomorrow, [mc]."
    mc "We'll find a moment for that later."
    scene ch9_34 with dissolve
    s "Really?"
    mc "(Damn, I said that impulsively, now she's going to be on about it all day...)" with dissolve
    mc "(Not that I mind too much...)" with dissolve
    mc "We did it the other day, don't you remember?"
    mc "Just make sure it's when no one suspects again."
    s "Yes!"
    mc "Alright, now hurry up and get dressed, it's breakfast time."
    scene ch9_35 with dissolve
    pause
    scene ch9_36 with dissolve
    s "I'll be there in a minute, wait for me in the kitchen, okay?"
    mc "Hurry up, your breakfast is going to get cold, okay?"
    s "Okay."
    scene ch9_37 with dissolve
    pause
    label ch9_sktchn:
    stop music fadeout 1.5
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 1.5
    scene ch9_38- with dissolve
    mc "Thanks."
    a "Did you wake up [s]?"
    show ch9_39- with dissolve:
        subpixel True
        xalign 0.5
        yalign 1.0
        zoom 0.5
        ease 5 zoom 0.85 yalign 0.2 xalign 0.3
    pause
    mc "Uh... yeah, she said she's coming, I think she's changing out of her pajamas."
    d "I think there's strawberry juice in the fridge, or am I wrong?"
    a "Yes, I'll get it now."
    a "Anything else?"
    mc "I'm good, thanks."
    d "Me too."
    d "I've missed this so much. There's nothing like having breakfast at home with the family."
    a "I’m skipping breakfast today."
    show ch9_40- with dissolve:
        xalign 0.5 yalign 0.0 zoom 0.8
    d "Honey..."
    show ch9_40-:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 0.8
        ease 5 yalign 0.8 
    a "It's part of the diet. Those love handles just won't budge, *chuckles*."
    d "I think your love handles are adorable."
    a "..."
    k "Umm, that’s not what you were supposed to respond..."
    d "What did I say wrong?"
    k "Never mind."
    scene ch9_40 with dissolve
    k "Thanks, [arelatks]."
    scene ch9_41 with dissolve
    d "Good morning, beautiful."
    scene ch9_42 with dissolve
    s "What's so good about it?"
    d "Hey, why the bad mood?"
    s "Because I didn’t wake up earlier."
    d "And how is that our fault?"
    s "..."
    scene ch9_43 with dissolve
    s "Hehe, you're such a drunk, [drelatks]."
    d "Huh?"
    s "I recorded you dancing when you were drunk, and then you fell, haha."
    a "I'll be in my room if you need anything. Enjoy your meal."
    d "Thanks, love."
    s "Wanna see [drelatks] fall?"
    k "Let's see it, hahaha."
    d "You're lying, I didn't even drink that much."
    k "[drelatks!cl], you were making toasts all the time."
    scene ch9_54- with flash
    d "I want to toast to [mc]'s first job, and how proud I am to have someone so hardworking in the family."
    k "And then you toasted to the family."
    scene ch9_54-- with flash
    d "Now, I want to toast to the family, for being here together in harmony and love..."
    scene ch9_54--- with flash
    k "And you kept drinking and toasting over and over."
    k "Toast after toast, hahaha."
    k "By the end, I had no idea what you were even saying, I just watched you tilt your glass to drink, hahaha."
    scene ch9_54---- with dissolve
    d "A toastsh for!... {w=0.5}uh...{w=0.5} cheersh!"
    scene ch9_44 with dissolve
    d "You better delete that right now, young lady."
    s "I'm gonna upload it to TokTik."
    d "Don't you dare!"
    scene ch9_45 with dissolve
    d "Don’t do it or I'll get really mad!"
    mc "([a] is still mad at [drelat] [d]...)"
    mc "(It’s been a few days and nothing has changed...)"
    d "Hmm, I wanted to take everyone to the beach today... Well, I’m afraid I'll be too angry for that."
    scene ch9_46 with dissolve
    s "Really!"
    d "If you delete the video."
    s "Okay, I'll delete it."
    d "Alright then, finish eating and we’ll go. I want to get there early to find parking."
    scene ch9_47 with dissolve
    k "I already made plans with [mia] today."
    d "No, [k]. You have to come, we’re all going."
    k "Yeah, but..."
    d "Tell your friend to come with us."
    scene ch9_48 with dissolve
    k "Uh, yeah. I guess I can do that."
    pause
    scene ch9_49 with dissolve
    d "[a] didn't give us any utensils."
    scene ch9_50 with dissolve
    d "[s]!"
    s "{i}Woat?"
    d "Please use utensils."
    s "{i}Dish way is fashter."
    scene ch9_51 with dissolve
    s "{i}I'm dhone."
    d "At least finish what’s in your mouth first."
    s "{i}Youh all hugy ugp."
    scene ch9_53 with dissolve
    d "The beach isn’t going anywhere, [s]."
    s "{i}Weren't you the one who wanted to go early?"
    pause
    scene ch9_55 with dissolve
    d "Good lord..."
    d "You're coming with us, right, [mc]?"
    mc "Erm..."
    d "Picture this: A beach umbrella, a couple of beers with your old man [drelat] [d]. Watching sexy girls in bikinis stroll by..."
    d "Doesn’t that sound nice?"
    d "How long has it been since we spent some quality time together?"
    mc "You don’t have to convince me, [drelat] [d], of course I’m going."
    d "That’s my boy, hehe."
    mc "You had me at the sexy girls in bikinis."
    d "Hahaha."
    stop music fadeout 1.5
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 1.5
    scene ch9_56 with dissolve
    pause
    mc "(Damn, [drelat] [d] made me agree to go to the beach when I really wanted to stay with [a].)" with dissolve
    mc "(With the house all to ourselves...)" with dissolve
    mc "(Damn it, why do I always have to play the good guy?)" with dissolve
    pause
    scene ch9_57 with dissolve
    mc "Need help?"
    a "Uhm, sure."
    scene ch9_58 with dissolve
    mc "Are you coming to the beach with us?"
    a "Are you going too?"
    mc "Yeah, are you?"
    a "Me?...{w=0.5} I don't know."
    a "I have a bit of a headache and... you know."
    mc "{i}{size=-3}Things still not going well with [drelat] [d]?"
    a "I'm afraid not."
    pause
    scene ch9_59 with dissolve
    mc "I saw you two arguing this morning. I was coming to the kitchen, so I couldn’t help but overhear."
    a "Yeah."
    pause
    mc "If you're staying, I could tell [drelat] [d] that I'm not going."
    mc "I could give him an excuse like I'm still sore from work or something."
    mc "That way I could keep you company, and you won’t be alone in the house..."
    a "..."
    pause
    scene ch9_58 with dissolve
    mc "Yesterday... I had a really good time."
    a "Y-yeah, me too..."

    pause
    mc "Really?"
    a "Uhm, yes..."
    pause
    a "We were dancing, drinking wine...{w=0.5} drinking a lot, actually *giggle*."
    a "It didn't seem like it, but I was pretty drunk, haha."
    mc "I drank quite a bit too, but I mixed mine with soda, hehe."
    a "Of course, I mixed mine too. Imagine if I hadn't, haha."
    a "Still, it was strong."
    mc "Yeah, it was that old wine [drelat] [d] bought. Normally, they don't have that much alcohol."
    a "Yeah."
    pause
    scene ch9_59 with dissolve
    a "When we got home, I felt like I was going to fall over."
    mc "When we got home, that was my favorite part."
    a "Oh, really?"
    mc "Yeah."
    pause
    mc "It was...{w=0.5} magical."
    pause
    a "Yeah..."
    pause
    scene ch9_62 with dissolve
    a "[mc], I know I said we wouldn’t talk about it..."
    a "But I need to clear my mind about something."
    mc "Hm?"
    a "Something from last night...{w=0.5} {i}{size=-5}when we were in my room."
    mc "Hmm, nope. I don’t remember."
    a "[mc], darling... you know exactly what I’m talking about."
    pause
    mc "Nope, I don't."
    scene ch9_61 with dissolve
    a "[mc], I know what we agreed on, I just want to talk about something specific."
    mc "We said nothing would change, we’ve talked about this a lot. I thought everything was fine."
    a "Yeah, I know, but no. This isn't about that. Just listen to me for a second."
    scene ch9_63 with dissolve
    mc "Not this again, please."
    mc "{i}What does it matter? No one will ever find out, we already talked about it, [a]."
    a "That's not what-..."
    pause
    scene ch9_66 with dissolve
    a "[mc], last night, you said something that left me... a bit unsettled."
    scene ch9_65 with dissolve
    a "It might be silly, but I just wanted to clear it up."
    mc "Tell me, [a]."
    pause
    a "Last night when we were in my room... {i}You said some things that made me think."
    scene ch9_66 with dissolve
    a "{i}You said something about love, or something like that."
    mc "Did I?"
    scene ch9_65 with dissolve
    a "Yeah, you said something along those lines."
    a "Or maybe I just misunderstood?"
    mc "Yeah, I love you, that's obvious, right?"
    a "Yeah, I guess it's obvious."
    a "But..."
    a "Well, maybe you don’t even remember."
    scene ch9_66 with dissolve
    a "It seemed like... you were talking about love in a different way."
    a "Maybe it's just me, but it felt like you were saying you were in love, in the 'romantic' sense of the word."
    mc "Oh, that... I honestly don’t remember."
    mc "Did that bother you?"
    scene ch9_65 with dissolve
    a "Hmm, I wouldn't say 'bothered', more like... it 'surprised' me a little."
    mc "Is that bad?"
    a "I can't say if it's bad or good. I just know it made me think about...{w=0.5} what you really want."
    pause
    mc "(What I really want?)" with dissolve
    pause
label ch9afterlose:
    scene ch9_66 with dissolve
    a "Forget it, it's kind of a weird question, I know."
    mc "No, no, I’m going to answer you."
    a "No, better not. It's silly."
    a "Actually, the idea of you... kind of scares me a little."
    scene ch9_65 with dissolve
    a "You... understand what I mean, right?"
    menu:
        with dissolve
        "[JGR]Confess your love to your [arelat]":
            stop music fadeout 1.5
            mc "The truth is, what I feel for you is much deeper than you think, [arelat] [a]."
            scene ch9_66 with dissolve
            a "What?"
            play music sexy2 fadein 1.5
            mc "I'm completely in love with you. Every day, I dream of starting a family with you."
            a "No, [mc]."
            mc "Please, let me finish."
            mc "My love for you is so strong that—"
            a "Stop, I don't want to hear any more..."
            a "Are you serious, [mc]?"
            mc "Absolutely."
            a "And you want to start a family with me? Are you talking about marriage?"
            a "Having children?"
            a "[mc], for god's sake, I'm twice your age, not to mention I'm your [arelat]!"
            mc "Children are optional..."
            a "[mc], I'm a married woman. How are you going to look your [drelat] in the eyes after what you just said?"
            mc "With the same eyes I see him with now."
            a "..."
            pause
            a "So, this was your goal all along?"
            a "To marry me, your [arelat]?"
            a "Are you sure of what you're saying, [mc]? Do you even hear yourself?"
            mc "I've never been more sure."
            a "[mc]! Don't joke like this."
            mc "It's not a joke."
            pause
            stop music fadeout 1.05
            a "I knew this was going to turn into a big problem."
            a "I'm sorry, but I can't return your feelings, obviously I can't."
            mc "Yeah, well... I know it can't happen, but..."
            mc "(Shit, I think I really screwed up this time...)" with dissolve
            mc "Can we just forget what I just said?"
            pause
            a "What were you thinking when you said that, [mc]?"
            a "It's best we stop this right now."
            mc "Stop?"
            a "For our own mental health, forget everything we've done, okay?"
            mc "But, [a]—"
            a "Let's pretend none of this ever happened, like we've been doing these past few days."
            mc "[a], no."
            a "It's for your own good, [mc]. I'm not someone you can fall in love with, I'm sorry."
            mc "But, everything we've done, was it all for nothing?"
            a "I think there was a misunderstanding on your part, I..."
            a "I wasn't trying to make you love me, and that was obvious!"
            a "I thought you understood that."
            a "If I let this continue, it'll only hurt you more. Find someone your age who can love you like I can't."
            mc "[arelat!cl] [a], no—"
            a "We agreed I'd always be your [arelat] no matter what, and that will never change."
            scene blackscreen
            centered "{size=+25}You ruined it."
            centered "{size=+25}Think more carefully before speaking next time."
            jump ch9afterlose
        "Avoid the conversation":
            mc "(Did I really say something like that last night?)"
            mc "(And what the hell do I say now?)"
            play music scene2 fadein 1.5
            jump ch9bforelose
label ch9bforelose:
    "..."
    pause
    scene ch9_67 with dissolve
    mc "{i}I want a kiss!"
    a "Huh?"
    mc "My good morning kiss. I demand my daily kiss."
    scene ch9_64 with dissolve
    a "Oh, ha-ha... Of course."
    a "A quick one."
    pause
    scene ch9_64- with dissolve
    a "*Hmmn*..."
    pause
    scene ch9_64 with dissolve
    a "*Smooch* There you go."
    pause
    scene ch9_67 with dissolve
    a "Now go get ready, you're going to the beach with the girls and [d], right?"
    mc "Are you going?"
    a "I don't think so."
    mc "If you don't go, neither will I."
    a "[mc], you know how things are with [d] and me."
    a "I’d rather avoid a fight for everyone’s sake."
    a "Remember what happened on the yacht?"
    a "I ruined everyone's afternoon."
    mc "{i}{size=-2}It was [drelat] [d] who ruined it by forcing you to dance with him."
    mc "Besides, we went out for dinner yesterday, and everything went fine, didn't it?"
    a "Yeah, but... you know, honey... things are still complicated."
    scene ch9_69 with dissolve
    mc "If you're not going, then I'll stay here with you."
    a "No, [mc], you're not skipping a day at the beach just to stay with me."
    mc "It's not like staying with you means being bored."
    scene ch9_68 with dissolve
    mc "I'm sure we'll have a good time alone at home."
    pause
    scene ch9_70 with dissolve
    mc "{i}{size=-5}I can't wait for everyone to leave..."
    a "Stop, honey..."
    scene ch9_71 with dissolve
    a "So that's your plan..."
    mc "Yes, it's my master plan."
    a "Well, if you stay, there'll be none of that."
    mc "None of what?"
    a "You know what."
    mc "Aww..."
    pause
    mc "I don't care."
    a "You're not getting your way, [mc]. I know what you're thinking."
    a "Go to the beach, sweetheart. I don't want you missing out because of me."
    mc "I don't want to leave you here alone."
    a "It doesn't matter, love. If you don’t go, I’ll feel like some kind of villain."
    a "I don't want [d] thinking I'm turning you all against him or something."
    mc "Then come with us."
    stop music fadeout 1.0
    scene ch9_72 with dissolve
    play music scene3 fadein 1.5
    "Let's see... there's nothing here!"
    s "[arelatks!cl], don't we have any ice cubes?"
    a "What do you need ice for?"
    s "For [drelatks]'s beers. He said we needed ice."
    s "Here they are, only five cubes left, but I guess that'll do."
    scene ch9_75 with dissolve
    s "And what are you two doing, just standing there watching?"
    s "Come on, get ready!"
    s "[mc], put on some shorts, and [arelatks], put on a swimsuit, because we're heading to the beach."
    a "Sweetheart, I think I have a bit of a headache and—"
    scene ch9_76 with dissolve
    s "Oh, [arelatks], don’t tell me you’re not coming with us again."
    s "Even [mc] is going."
    s "Whatever, we're leaving. Anyone who wants to come, get ready fast."
    scene ch9_73 with dissolve
    s "Where's the beer?"
    a "At the bottom."
    s "At the bottom where?"
    scene ch9_77 with dissolve
    s "I couldn’t find your beers, but I brought juice, [drelatks]!"
    d "They should be there!"
    s "Well, they're not!"
    stop music fadeout 0.5
    scene ch9_78 with dissolve
    play music scene1 fadein 1.5
    a "She looks so cute in her sun hat."
    mc "Yeah, haha."
    mc "Come on, [a], we’ll have a great time."
    pause
    scene ch9_79 with dissolve
    d "See, they were here! I told you, they were at the bottom of the fridge!"
    scene ch9_80 with dissolve
    d "And those beers and juices won't fit in that tiny cooler!"
    s "Where’s the big cooler?!"
    d "In the garage, I already told you!"
    s "The only one in the garage was this one!"
    scene ch9_81 with dissolve
    d "Sweetheart, didn’t the girls tell you we're going to the beach?"
    a "No, they told me, it’s just that I have a bit of a headache and don’t feel well in general."
    d "Love, we're all going. You're not staying home alone, are you?"
    scene ch9_82 with dissolve
    d "You have to come with us, [a]."
    d "What happened last time on the yacht... nothing like that will happen again."
    d "I'm committed to making sure everyone has a good time."
    a "[d], no. That’s not it."
    d "I'm serious, love. Plus, it would be good for the girls, and for [mc]."
    d "I want to give them a happy memory of all of us together."
    d "What do you say, love?"
    pause
    scene ch9_83 with dissolve
    mc "It's not the same without you, [arelat] [a]."
    d "Exactly."
    mc "Imagine this: a little umbrella, a couple of juices, and chatting about anything..."
    mc "Or sunbathing at the beach, with sunscreen! Let’s not forget the sunscreen, please, haha."
    mc "Doesn't that sound nice?"
    scene ch9_84 with dissolve
    a "Alright, you convinced me, *giggles*."
    a "I’ll take an ibuprofen and get ready."
    d "I’m so glad, dear. We’re going to have a great time, you’ll see."
    d "[mc], I’m going to need your help setting up the umbrella."
    mc "Of course."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    if stephloving == "True":
        jump ch9nxt
    else:
        jump ch9asgdf_
label ch9nxt:
    play music scene2 fadein 2.0
    scene ch9_85 with dissolve
    pause
label ch9s2:
    if _in_replay:
        scene ch9_85 with dissolve
        show screen Replayexit
        $ stephloving = "True"
        play music scene2 fadein 1.0
    s "*Ugh!*"
    mc "Need some help?"
    s "Yes, the door, [mc], it closed!"
    pause
    image ch9_86anim:
        "ch9_86" with dissolve
        1.0
        "ch9_87" with dissolve
        1.0
        repeat
    scene ch9_86anim with dissolve
    s "Thanks."
    if stephloving != "True":
        jump ch9asgdf_
    mc "Let me help you with the cooler."
    s "No, I can do it myself."
    pause
    mc "..."
    pause
    scene ch9_88 with dissolve
    s "..."
    pause
    s "*Hngh* Can you give me a push?"
    mc "Haha, sure."
    scene ch9_89 with dissolve
    s "Uh!"
    mc "There you go."
    pause
    scene ch9_90 with dissolve
    s "Thanks, [mc]."
    mc "One more push."
    pause
    scene ch9_91 with hpunch
    s "Hngh!"
    pause
    scene ch9_92 with dissolve
    s "Thanks, but I could do it myself."
    scene ch9_93 with dissolve
    s "Hey!"
    mc "Push!"
    pause
    scene ch9_94 with dissolve
    mc "That's it."
    s "I think I need another push..."
    mc "Another push?"
    s "Yes."
    stop music fadeout 2.0 
    s "You’re such a pervert, [mc]."
    mc "What?" 
    image ch9_95anim:
        "ch9_95" with dissolve
        1.0
        "ch9_96" with dissolve 
        1.0
        repeat
    play music sexy3 fadein 2.0
    show screen scrollable_animationch9_95anim with dissolve
default button_visiblech9_95 = True
screen scrollable_animationch9_95anim():
    default ypos = 0.0
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        add "ch9_95anim"
    hbox:
        xpos 20
        ypos 1000
        if button_visiblech9_95:  # Only show the button if button_visible is True
            textbutton "Hide" action [SetVariable("arrow_alpha", 0.0), SetVariable("button_visiblech9_95", False)] style "textbutton_choice"
    vbox:
        button:
            background None
            xpos 220
            ypos 0
            xsize 1700
            ysize 1080
            action Return()
            add "images/gamemenu/updownarrows.webp" xalign 0.75 yalign 0.5 alpha arrow_alpha
label after_animationch9_95anim:
    $ arrow_alpha = 0.8
    s "Give me another push, [mc], *tee-hee*."
    mc "Huh?"
    s "I need you to push me again with your thing, *tee-hee*."
    mc "W-with my what?"
    pause
    mc "(Honestly, I did it on purpose, but I didn't expect this, though I probably should have.)" with dissolve
    mc "(She’s such a naughty girl!)" with dissolve
    pause
    mc "(Look at that cute little butt moving...)" with dissolve
    scene ch9_97
    hide screen scrollable_animationch9_95anim with dissolve
    mc "(It was inevitable...)" with dissolve
    pause
    $ button_visiblech9450 = True
    jump animimagech9_99sap_
init python:
    def ch9_99sap_(trans, st, at):  
        trans.set_child("ch9_99sap_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

init python:
    def ch9_99sap2_(trans, st, at):  
        trans.set_child("ch9_99sap2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 31:
            store.frame_num = 2    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  

init python:
    def ch9_99sap3_(trans, st, at):  
        trans.set_child("ch9_99sap3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
screen scrollable_ch9_99sap_():
    default ypos = 0.0
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        add "ch9_99sap_"
    hbox:
        xpos 20
        ypos 1000
        if button_visiblech9450:  # Solo muestra el botón si button_visible es True
            textbutton "Hide" action [SetVariable("arrow_alpha", 0.0), SetVariable("button_visiblech9450", False)] style "textbutton_choice"
    vbox:
        button:
            background None
            xpos 220
            ypos 0
            xsize 1700
            ysize 1080
            action Return()
            add "images/gamemenu/updownarrows.webp" xalign 0.75 yalign 0.5 alpha arrow_alpha
label animimagech9_99sap_:
    image ch9_99sap_:
        function ch9_99sap_ 
    image ch9_99sap2_:
        function ch9_99sap2_ 
    image ch9_99sap3_:
        function ch9_99sap3_ 
    $ anim_speed = 0.05
    $ arrow_alpha = 0.8
    show screen scrollable_ch9_99sap_ with dissolve    
    s "*Hmm*... It feels so good."
    s "Push, [mc], *hmm*."
    pause
    s "It got hard, *tee-hee*."
    mc "(She's so cute and sexy at the same time...)" with dissolve
    hide screen scrollable_ch9_99sap_
    scene ch9_99sap2_
    s "Why aren’t you moving, huh, [mc]?"
    mc "(We've done these things several times, and she's starting to learn how to seduce me.)" with dissolve
    mc "(She loves teasing me.)" with dissolve
    s "And you're not talking either, hmmm, *humh*."
    pause
    scene ch9_99sap3_ with dissolve
    mc "And I am the pervert..."
    s "Yup, *tee-hee*."
    mc "And you're sooo naughty."
    s "And a pervert too, hehe, just like you."
    mc "Yeah, haha, like me{w=0.5}, but maybe a bit more you."
    s "Nooo, you're more!"
    pause
    mc "Alright, enough, we need to hurry up so we can leave."
    scene ch9_100 with dissolve
    s "[mc], I want to do sexy things now..."
    mc "Later, when we get back from the beach."
    s "But I want to now."
    scene ch9_101 with dissolve
    s "Just a little more."
    mc "No, [s]."
    mc "(She's such a horny girl...)" with dissolve
    scene ch9_100 with dissolve
    mc "We need to be careful, remember?"
    s "Yeah, I know..."
    pause
    scene ch9_102 with dissolve
    s "It's really hard, *tee-hee*, you can see it through your shorts."
    mc "Stop looking at it!"
    s "Humm..."
    scene ch9_103 with dissolve
    s "Yup, it's really hard too."
    mc "Move aside, [s], my arms are getting tired."
    s "Hmm... it's like it wants to pop out of your pants, *giggle*."
    pause
    s "Can I suck it?"
    mc "What?{w=0.5} N-no!"
    pause
    mc "{i}W-wait until later..."
    scene ch9_104 with hpunch
    s "Pull it out, I'll suck it really quick."
    mc "Hey, not here!"
    scene ch9_107 with vpunch
    s "Ah!"
    mc "*Ouch*."
    mc "I told you my arms were getting tired."
    s "Did you hurt yourself?"
    mc "No, I’m fine. Just move so I can close the door."
    scene ch9_106 with dissolve
    s "*Tee-hee*."
    mc "Hey, what's so funny?"
    s "N-{w=0.5}nothing, *tee-hee*."
    scene ch9_106- with dissolve
    mc "Eh."
    pause
    scene ch9_108 with dissolve
    pause
    s "*Hmm*..."
    scene ch9_108- with dissolve
    mc "Eh..."
init python:
    def ch9_99spg_(trans, st, at):  
        trans.set_child("ch9_99spg_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_99spg2_(trans, st, at):  
        trans.set_child("ch9_99spg2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   

label ch9_99spg_1:
    image ch9_99spg_:
        function ch9_99spg_
    image ch9_99spg2_:
        function ch9_99spg2_
    $ anim_speed = 0.03
    scene ch9_99spg_ with dissolve
    s "*Hmm, hmmg*."
    mc "[s]... *uhm*."
    s "It feels good, [mc]."
    s "Your penis feels nice when it touches me there."
    mc "Do you like it?"
    with hpunch
    mc "I-I mean, stop, [s]!"
    mc "(Someone might come.)" with dissolve
    mc "(But damn, this feels good.)" with dissolve
    pause
    scene ch9_99spg2_ with dissolve
    pause
    s "*Huhm, hmm*..."
    s "It tickles *hmmh*..."
    s "Don’t press so hard because it scratches."
    mc "Sorry."
    pause
screen animation_ch9_99spg_():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("afteranimation_ch9_99spg_") style "textbutton_choice"
        hbox:
            yalign 0.05
            xalign 0.99
            textbutton "Pov 2" action Jump("ch9_99spg_pov2") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen animation_ch9_99spg2_():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("afteranimation_ch9_99spg_") style "textbutton_choice"
        hbox:
            yalign 0.05
            xalign 0.99
            textbutton "Pov 1" action Jump("ch9_99spg_pov1") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"
    

    
label ch9_99spg_pov1:
    scene ch9_99spg_ with dissolve
    call screen animation_ch9_99spg_ with dissolve
label ch9_99spg_pov2:
    scene ch9_99spg2_ with dissolve
    call screen animation_ch9_99spg2_ with dissolve




label afteranimation_ch9_99spg_:
    scene ch9_112 with dissolve
    mc "We'd better stop now; someone might come."
    s "*Uhm!*... Oh no!"
    mc "What's wrong?"
    s "I'm getting wet."
    scene ch9_115 with dissolve
    mc "What's happening?"
    s "I was starting to get wet again."
    s "It's just that whenever we do sexy things, I end up soaking my panties..."
    pause
    scene ch9_114 with dissolve
    s "I don't want it to look like I peed in my swimsuit; that would be really embarrassing."
    mc "Ah- haha..."
    mc "Yeah, it's better if we stop or you'll end up soaked."
    pause
    scene ch9_113 with dissolve
    s "I'm going to the bathroom to clean up."
    s "So, we said this afternoon, right? No changing your mind."
    mc "This afternoon? Oh, right... the {i}{size=-5}sexy things."
    mc "I promised you, didn't I?"
    s "Yes."
    s "Well, I'll be quick."
    mc "Go on, go."
    $ renpy.end_replay()
    stop music fadeout 1.0
    pause
label ch9asgdf_:
    play music scene1 fadein 1.5
    scene ch9_117 with fade
    d "I can handle it, son, just open the trunk, please."
    mc "Sure."
    scene ch9_116 with dissolve
    d "Hold the door, I'm going for something else."
    pause
    scene ch9_118 with dissolve
    pause
    if stephloving == "True":
        show ch9_120- with dissolve:
            subpixel True
            xalign 0.5 yalign 1.0 zoom 1.0 
            ease 6 yalign 0.0
        pause 6
        show ch9_120-:
            subpixel True
            xalign 0.5 yalign 0.0 zoom 1.0 
            ease 3 yalign 1.0 xalign 1.0
        pause 3
        show ch9_120-:
            subpixel True
            xalign 1.0 yalign 1.0 zoom 1.0 
            ease 6 yalign 0.2
        pause 6
        show ch9_120-:
            subpixel True
            xalign 1.0 yalign 0.2 zoom 1.0 
            ease 3 xalign 0.0 yalign 1.0
        pause 3
        show ch9_120-:
            subpixel True
            xalign 0.0 yalign 1.0 zoom 1.0 
            ease 6 yalign 0.0 xalign 0.0
        pause 6
        show ch9_120-:
            subpixel True
            xalign 0.0 yalign 0.0 zoom 1.0 
            ease 1.5 yalign 0.0 xalign 0.5 zoom 0.45
        pause 1.5
    else:
        show ch9_120- with dissolve:
            subpixel True
            xalign 0.5 yalign 1.0 zoom 1.0 
            ease 6 yalign 0.0
        pause 6
        show ch9_120-:
            subpixel True
            xalign 0.5 yalign 0.0 zoom 1.0 
            ease 3 yalign 1.0 xalign 0.0
        pause 3
        show ch9_120-:
            subpixel True
            xalign 0.0 yalign 1.0 zoom 1.0 
            ease 6 yalign 0.0 xalign 0.0
        pause 6
        show ch9_120-:
            subpixel True
            xalign 0.0 yalign 0.0 zoom 1.0 
            ease 1.5 yalign 0.0 xalign 0.5 zoom 0.45
        pause 1.5

    mc "(Beautiful...)" with dissolve
    k "I’m telling you that you look nice. I don’t know why you’re getting upset."
    s "And why are you laughing?"
    k "I’m not laughing."
    s "I heard you talking with [arelatks]. You said I have a big butt."
    k "For your information, that was a compliment."
    a "You look very pretty, [s], stop fighting."
    pause
    scene ch9_122 with dissolve
    d "[k], what did your friend say? Do we need to go get her?"
    k "No, she’s on her way. She said her boyfriend will bring her."
    d "To here? Tell her we can go pick her up, it’s no problem."
    show ch9_123 with dissolve:
        subpixel True
        xalign 0.5 yalign 1.0
        ease 2 yalign 0.3
    mc "(Those shorts really show off her nice butt.)"
    pause
    k "She said she was on her way."
    d "Alright. Do you have everything? Sunscreen, towels?"
    k "I’ve got everything."
    scene ch9_124 with dissolve
    d "I think your friend is coming. What was her name again?"
    k "It’s [mia]."
    mia "I hope I didn’t make you wait too long!"
    scene ch9_125 with dissolve
    "Kyaaa!" with hpunch
    mia "It feels like we haven’t seen each other in weeks, haha."
    k "Yeah, haha. Wow, nice bikini! Looking so sexy as always."
    mia "Of course! You never know when the next opportunity will strike."
    k "Haha, oh babe! I thought your boyfriend had finally tamed you."
    mia "That will never happen."
    k "Haha."
    scene ch9_126 with dissolve
    d "Hey, it’s been a while since I saw you. How’s your mother?"
    mia "Hello Mr. [d]! My mom is fine; she went back to Puerto Rico for a little issue but she’ll be back soon."
    d "I see."
    mia "And what’s the miracle of finding you at home?"
    d "I was on a business trip; my company has been keeping me busy, haha."
    mia "That’s good, right? It means things are going well."
    d "If you see it that way, yes, it’s a good thing. But I was really looking forward to coming back home to my kids."
    d "Are we ready?"
    s "Yes!"
    d "Well, everyone on board, haha."
    s "Wait, I forgot my towel!"
    d "Hurry up, dear!"
    scene ch9_127 with hpunch
    k "Ow! Sorry."
    scene ch9_129 with dissolve
    pause
    scene ch9_128 with dissolve
    mc "{i}{size=-5}Nice tits, I mean, bikini."
    k "*Giggles* Move, I need to open the door."
    scene ch9_130 with fade
    a "Hi, [mia], how are you?"
    mia "Mrs. [a], I’m fine. And you?"
    a "I’m good, thank God."
    a "Your mom told me you were about to come back."
    mia "I think she’s finishing up some divorce paperwork and also dealing with some inheritance from her grandfather, or something like that."
    a "And are you living alone now or is someone with you?"
    mia "My boyfriend is at home almost all the time, so I don’t feel alone."
    a "I see, it’s good that you have someone to keep you company."
    scene ch9_130- with dissolve
    d "Don’t tell me your parents are divorced."
    mia "Yes, it’s been a long time since my parents were together."
    d "I’m really sorry."
    mia "Why?"
    d "Uh... never mind."
    mia "Honestly, I think we’re better this way. He on his side and us on ours."
    d "Y-yeah..."
    scene ch9_131 with dissolve
    d "Hurry up, dear, we want to leave."
    s "I’m coming."
    scene ch9_132 with vpunch
    mc "*Ooof*"
    s "Ready, let’s go."
    d "You can’t go there, dear, the police will stop us."
    d "[k], make some space for [s]."
    k "Barely enough room for [mia] and me."
    scene ch9_133 with dissolve
    k "You’re stepping on me!"
    s "I don’t fit!"
    mia "Ouch!"
    s "Sorry!"
    stop music fadeout 3.0
    scene blackscreen with Dissolve(2.0)
    pause
label ch9gttb:
    play music scene2 fadein 2.0
    scene ch9_133- with Dissolve(2.0)
    pause
    d "The good thing is we’re going on a Friday morning, so there won’t be much people."
label ch9s3:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene2 fadein 1.0
    scene ch9_134 with dissolve
    s "Are we almost there?"
    k "[s], it’s the place we went to the other day, where you cried because you wanted to go swimming."
    s "Oh."
    pause
    scene ch9_135 with dissolve
    s "I didn’t cry, silly!"
    k "You did cry."
    mia "Aw, poor thing."
    s "I didn’t cry! Don’t believe this ugly witch."
    mia "Haha."
    k "If I’m a witch, then what are you?"
    s "A pretty princess."
    k "Who’s still turned into a frog."
    mia "Haha."
    s "You stop laughing!"
    mia "I’m laughing at something else. By the way, it was the prince who was turned into a frog."
    s "Ha-ha, you’re so dumb, [k]."
    mc "(God, my head hurts and the girls won’t stop screaming.)" with dissolve
    mc "(And when they’re not arguing, [s] won’t stop talking and talking...)" with dissolve
    mc "(Long trips put me in such a bad mood, I feel like jumping out the window from anxiety.)" with dissolve
    pause
    if stephloving != "True":
        jump ch9bfcgd
    mc "(This would be hell if it weren’t for...) " with dissolve
    image ch9_138anim:
        "ch9_137" with Dissolve(0.5)
        2.5
        "ch9_138" with Dissolve(0.5)
        0.2
        "ch9_137" with Dissolve(0.5)
        1.0
        "ch9_138" with Dissolve(0.5)
        0.2
        "ch9_137" with Dissolve(0.5)
        3.0
        "ch9_138" with Dissolve(0.5)
        0.2
        "ch9_137" with Dissolve(0.5)
        1.0
        "ch9_138" with Dissolve(0.5)
        0.2
        "ch9_137" with Dissolve(0.5)
        0.5
        "ch9_138" with Dissolve(0.5)
        0.2
        "ch9_137" with Dissolve(0.5)
        0.5
        "ch9_138" with Dissolve(0.5)
        0.2
        repeat
    image ch9_140anim:
        "ch9_140" with Dissolve(0.5)
        2.5
        "ch9_139" with Dissolve(0.5)
        0.2
        "ch9_140" with Dissolve(0.5)
        1.0
        "ch9_139" with Dissolve(0.5)
        0.2
        "ch9_140" with Dissolve(0.5)
        3.0
        "ch9_139" with Dissolve(0.5)
        0.2
        "ch9_140" with Dissolve(0.5)
        1.0
        "ch9_139" with Dissolve(0.5)
        0.2
        "ch9_140" with Dissolve(0.5)
        0.5
        "ch9_139" with Dissolve(0.5)
        0.2
        "ch9_140" with Dissolve(0.5)
        0.5
        "ch9_139" with Dissolve(0.5)
        0.2
        repeat
    image ch9_141anim:
        "ch9_141" with Dissolve(0.5)
        2.5
        "ch9_142" with Dissolve(0.5)
        0.2
        "ch9_141" with Dissolve(0.5)
        1.0
        "ch9_142" with Dissolve(0.5)
        0.2
        "ch9_141" with Dissolve(0.5)
        3.0
        "ch9_142" with Dissolve(0.5)
        0.2
        "ch9_141" with Dissolve(0.5)
        1.0
        "ch9_142" with Dissolve(0.5)
        0.2
        "ch9_141" with Dissolve(0.5)
        0.5
        "ch9_142" with Dissolve(0.5)
        0.2
        "ch9_141" with Dissolve(0.5)
        0.5
        "ch9_142" with Dissolve(0.5)
        0.2
        repeat
    scene ch9_138anim with dissolve
    mc "(These delicious little buns...)" with dissolve
    pause
    scene ch9_151 with dissolve
    s "Hey, [mia], do you know how to swim?"
    mia "Yes, do you?"
    s "Nope, can you teach me when we get to the beach?"
    mia "Sure, but it's dangerous to swim at the beach."
    s "Really?"
    mia "Yes, you can get swept away by a wave and pulled out to sea if you try to swim too deep."
    scene ch9_140anim with dissolve
    s "And a shark could eat you."
    mia "Yes, that could happen too, *laughs*."
    mia "Though I don’t think there are sharks in these waters."
    mc "(God... her butt feels so good.)" with dissolve
    s "Do you know how to surf?"
    mia "Yes."
    scene ch9_141anim with dissolve
    s "Really?"
    mia "Yes, do you want me to teach you?"
    s "Yesss!"
    mc "(If all my trips were with a cute little butt bouncing on my cock, I’d travel every day.)" with dissolve
    pause
    s "Did you know I know how to roller skate?"
    mia "Wow, on skates or a skateboard?"
    s "On skates."
    k "Liar."
    s "I do, silly! I was practicing in the yard the other day."
    d "Enough arguing, girls, my head is starting to hurt from all the shouting."
    k "It’s just that [s] can’t talk without shouting."
    s "{size=+5}I’m not!{/size}{w=0.5}{size=-5} shouting..."
    image ch9_143anim:
        "ch9_143" with Dissolve(0.5)
        2.5
        "ch9_144" with Dissolve(0.5)
        0.2
        "ch9_143" with Dissolve(0.5)
        1.0
        "ch9_144" with Dissolve(0.5)
        0.2
        "ch9_143" with Dissolve(0.5)
        3.0
        "ch9_144" with Dissolve(0.5)
        0.2
        "ch9_143" with Dissolve(0.5)
        1.0
        "ch9_144" with Dissolve(0.5)
        0.2
        "ch9_143" with Dissolve(0.5)
        0.5
        "ch9_144" with Dissolve(0.5)
        0.2
        "ch9_143" with Dissolve(0.5)
        0.5
        "ch9_144" with Dissolve(0.5)
        0.2
        repeat
    scene ch9_143anim with dissolve
    s "[k] just makes me angry..."
    a "Behave, girls, you’re not kids anymore."
    pause
    s "So you do know how to surf?"
    mia "Yes, I used to surf when I lived in Puerto Rico."
    s "Do they have beaches like this in Puerto Rico?"
    mia "Of course, and they’re very beautiful."
    s "And were there sharks?"
    scene ch9_152 with dissolve
    mia "Not that I remember, I never saw one."
    k "I didn’t know you surfed."
    mia "I haven’t done it in about five years, but I think I still remember how."
    k "You’ve always been the type who likes skating and breaking your bones."
    s "[mc], what are you...?"
    pause
    scene ch9_153 with dissolve
    s "{i}{size=-5}[mc], I know what you’re doing, *heh*."
    mc "{i}{size=-5}Shh..."
    s "{i}{size=-5}Naughty."
    scene ch9_143 with dissolve
    pause
    scene ch9_145 with dissolve
    mc "{i}{size=-5}H-hey!"
    image ch9_146anim:
        "ch9_146" with Dissolve(0.5)
        2.5
        "ch9_147" with Dissolve(0.5)
        0.2
        "ch9_146" with Dissolve(0.5)
        1.0
        "ch9_147" with Dissolve(0.5)
        0.2
        "ch9_146" with Dissolve(0.5)
        3.0
        "ch9_147" with Dissolve(0.5)
        0.2
        "ch9_146" with Dissolve(0.5)
        1.0
        "ch9_147" with Dissolve(0.5)
        0.2
        "ch9_146" with Dissolve(0.5)
        0.5
        "ch9_147" with Dissolve(0.5)
        0.2
        "ch9_146" with Dissolve(0.5)
        0.5
        "ch9_147" with Dissolve(0.5)
        0.2
        repeat
    scene ch9_146anim with dissolve
    pause
    mc "{i}{size=-5}What are you doing?"
    s "*Shh*."
    mia "I also skate."
    s "Really?"
    mia "But on a skateboard, I’m not so good with roller skates."
    s "I can teach you to skate on roller skates, and you can teach me to skateboard."
    mia "Sounds like a great idea."
    image ch9_148anim:
        "ch9_148" with Dissolve(0.5)
        2.5
        "ch9_149" with Dissolve(0.5)
        0.2
        "ch9_148" with Dissolve(0.5)
        1.0
        "ch9_149" with Dissolve(0.5)
        0.2
        "ch9_148" with Dissolve(0.5)
        3.0
        "ch9_149" with Dissolve(0.5)
        0.2
        "ch9_148" with Dissolve(0.5)
        1.0
        "ch9_149" with Dissolve(0.5)
        0.2
        "ch9_148" with Dissolve(0.5)
        0.5
        "ch9_149" with Dissolve(0.5)
        0.2
        "ch9_148" with Dissolve(0.5)
        0.5
        "ch9_149" with Dissolve(0.5)
        0.2
        repeat
    scene ch9_148anim with dissolve
    s "I’ll teach you when we get home."
    mia "Alright."
    s "And do you like to dance?"
    mia "Hmm, yes, I do. Do you know how to dance?"
    s "Me?"
    mia "Yes, *laughs*."
    s "I’m the best dancer I know."
    mc "(Damn, this feels so good.)" with dissolve
    mc "(The fact that everyone is inches away and we’re doing this in secret makes it so much hotter.)" with dissolve
    mc "([s] is right, I am a naughty pervert after all.)" with dissolve
    mc "*Hmm* (I need to calm down or I’m going to burst.)" with dissolve
    s "Hey, but how are we going to surf without a surfboard?!"
    mia "Oops, that’s right."
    mia "I think there’s a surf shop near the beach."
    mia "Mr. [d], we’re going to the beach near the pedestrian bridge, right?"
    d "Yeah, why do you ask?"
    mia "There’s a surf shop nearby where they sell surfboards."
    scene ch9_155 with dissolve
    s "Yes!"
    s "[drelatks!cl], can you buy me one, please?"
    d "Do you want a surfboard?"
    s "Yes, please, please with chocolate sprinkles!"
    d "Sure, I’ll buy you one."
    k "I want one too."
    scene ch9_157 with dissolve
    d "I’ll buy you one."
    pause
    scene ch9_158 with dissolve
    mc "(It’s so warm...)" with dissolve
    mc "(She must be getting pretty wet down there.)" with dissolve
    pause
    scene ch9_159 with dissolve
    pause
    d "And how much does a surfboard cost, [mia]?"
    mia "It depends on the quality. Mine was fairly good, and I sold it for three thousand dollars, but it was used."
    d "What?!" with hpunch
    scene ch9_160 with vpunch
    mc "A-ah!"
    scene ch9_161 with dissolve
    pause
    scene ch9_162 with vpunch
    mc "*Gulp* (I could swear I heard my dick snap.)" with dissolve
    pause
    a "Careful, [d]!"
    d "Sorry, I choked on my saliva."
    s "I want mine in pink."
    d "Honey, three thousand dollars for a piece of wood..."
    mia "Sorry, I said three thousand, I meant three hundred."
    d "That sounds more reasonable..."
    scene ch9_163 with dissolve
    mia "Although it might be a better idea to get a boogie board."
    s "What’s that?"
    mia "It’s like a surfboard but smaller. It’s also easier to use, and in calm beaches like this one, you have a lot of fun."
    mc "{i}{size=-5}[s]..."
    scene ch9_164 with dissolve
    s "Hmm?"
    s "So naughty..."
    mia "Did you say something?"
    s "N-no."
    pause
    scene ch9_166 with dissolve
    s "{i}{size=-5}Naughty."
    s "{i}{size=-5}You can't wait to get home either, can you?"
    mc "{i}{size=-5}Erm.. lift up a bit so I can slip it into my pants."
    pause
    image ch9_168-anim:
        "ch9_168" with dissolve
        1.0
        "ch9_168-" with dissolve
        1.0
        repeat
    scene ch9_168-anim with dissolve
    s "{i}{size=-5}It’s so hard..."
    mc "{i}{size=-5}[s], wait..."
    s "{i}{size=-5}I’m just rubbing it."
    mc "{i}{size=-5}Yes, but... *hmm*... (It feels so good...)" with dissolve
    pause
    scene ch9_168-- with dissolve
    s "{i}{size=-5}You’re starting to leak semen."
    mc "{i}{size=-5}It’s not semen."
    s "{i}{size=-5}It’s coming and coming..."
    s "{i}{size=-5}I thought men didn’t get wet."
    mc "(If this doesn’t stop, I’m going to explode.)" with dissolve
    pause
    scene ch9_167 with dissolve
    pause
    scene ch9_168 with dissolve
    pause
    scene ch9_168- with dissolve
    pause
    scene ch9_168-- with dissolve
    s "{i}{size=-5}Keep it coming, [mc]!"
    pause
    scene ch9_168--- with dissolve
    pause
    scene ch9_168---- with dissolve
    pause
    s "{size=-5}{i}[mc]..."
    scene ch9_166 with dissolve
    s "{i}{size=-5}Do you want to see something really lewd?"
    mc "{i}{size=-5}What?"
    mc "{i}{size=-5}M-maybe not..."
    pause
    scene ch9_169- with dissolve
    s "{i}{size=-5}*Yum*..."
    mc "Uh..."
    pause
    scene ch9_166- with dissolve
    s "{i}{size=-5}*Mahl*..."
    pause
    scene ch9_166-- with dissolve
    s "{i}{size=-5}Hmmm, tasty."
    mc "[s]..."
    pause
    scene ch9_166 with dissolve
    s "{i}{size=-5}Hehe, you turned all red."
    mc "(What a pervert girl!)" with dissolve
    d "[s]."
    scene ch9_165 with hpunch
    s "Y-yes?"
    d "Choose, boogie board or surfboard. I can't buy both."
    s "Umm... boogie board!"
    d "You have until we get there to decide, but only one thing. I can’t buy both, got it?"
    s "Got it!"
    d "Okay."
    scene ch9_166 with dissolve
    s "{i}{size=-5}That was close, hehe..."
    pause
    scene ch9_168---- with dissolve
    pause
    scene ch9_168----- with dissolve
    mc "{i}{size=-5}[s]..."
    pause
    scene ch9_168------ with dissolve
    pause
    image ch9_168---anim:
        "ch9_168-----" with dissolve
        1.2
        "ch9_168------" with dissolve
        1.2
        "ch9_168-" with dissolve
        1.2
        "ch9_168" with dissolve
        1.2
        "ch9_168-" with dissolve
        1.2
        "ch9_168" with dissolve
        1.2
        "ch9_168-" with dissolve
        1.2
        "ch9_168--" with dissolve
        1.2
        "ch9_168------" with dissolve
        1.2
        "ch9_168-----" with dissolve
        1.2
        "ch9_168------" with dissolve
        1.2
        "ch9_168-----" with dissolve
        1.2
        "ch9_168" with dissolve
        1.2
        "ch9_168-" with dissolve
        1.2
        "ch9_168--" with dissolve
        1.2
        "ch9_168------" with dissolve
        1.2
        "ch9_168-----" with dissolve
        1.2
        "ch9_168------" with dissolve
        1.2
        repeat
    scene ch9_168---anim with dissolve
    s "{i}{size=-5}I want to see your cum, [mc]."
    mc "{i}{size=-5}No, stop, [s]!"
    s "{i}{size=-5}''Stop, [s]''."
    s "{i}{size=-5}*Hehe* you say that, but when I touch you, you move your hips like you enjoy it."
    pause
    mc "*Hmm* (I have it so upright that it even hurts a little.)" with dissolve
    pause
    mia "Are you okay, [s]?"
    scene ch9_170 with hpunch
    s "What? Why do you ask? Did you see something?"
    s "I-I'm fine. What about you?"
    k "She’s been quiet for five minutes; there’s definitely something wrong or she’s plotting something."
    s "There’s nothing wrong. Why would I be hiding something?"
    k "Hmm... You’re all red. Do you have a headache?"
    mia "I get headaches when I travel by car."
    s "Oh, yeah, I have a really bad headache."
    $ renpy.end_replay()
    scene ch9_133- with dissolve
    d "We’re almost there."
label ch9bfcgd:
    stop music fadeout 2.0
    scene blackscreen with Dissolve(1.5)
    pause
    play background "audio/beachsfx.ogg" loop fadein 2.0
    scene ch9_171- with dissolve
    d "Look at that! The beach is almost empty."
    k "That’s what you get living in a town abandoned by God."
    d "If you lived in the city, you’d want to come back here on the third day."
    mia "It’s great here! Everything you need is so close, malls, school and all that stuff."
    s "{i}{size=-5}[mc]."
    play music scene1 fadein 3
    if stephloving != "True":
        jump ch9170sskip
    scene ch9_171---_ with dissolve
    s "{i}{size=-5}[mc], I don't know if you’ve noticed, but you have a big bugle in your pants."
    scene ch9_172 with hpunch
    mc "(Shit!)"
    pause
    scene ch9_172- with dissolve
    s "{i}{size=-5}Why does nobody else have it showing in their pants like you, [mc]?"
    mc "{i}{size=-5}I-I don’t know. Let’s let them get a bit ahead..."
    pause
    scene ch9_171---_ with dissolve
    s "{i}{size=-5}Why are you covering it if everyone has already seen it?"
    mc "{i}{size=-5}What?!"
    s "{i}{size=-5}It’s been like that since we got out of the car, the whole way here."
    s "{i}{size=-5}A lady was staring at you and laughed."
    mc "{i}{size=-5}Why didn’t you tell me earlier?!"
    s "{i}{size=-5}Uhm... I don’t know."
    s "{i}{size=-5}Just kidding, hehe."
    s "{i}{size=-5}But don’t worry, I have a solution."
    scene ch9_172-- with dissolve
    s "Ta-dah!"
    mc "{i}{size=-5}Oh, clever."
    s "{i}{size=-5}Hehe."
    mc "{i}{size=-5}Thanks, [s]."
    jump ch9170sskip
label ch9170sskip:
    scene ch9_173 with dissolve
    d "What’s up, son, do you need help?"
    mc "No, and you?"
    d "Nah. This old dog still has the energy of a pup, hehe."
    pause
    scene ch9_174 with fade
    mc "Is this okay or do you want me to tilt it a bit more?"
    a "It’s perfect as it is, thank you, dear."
    if stephloving != "True":
        jump ch9174sskip
    scene ch9_175- with dissolve
    a "[s], didn’t you really want to come to the beach?"
    s "Yeah."
    a "And what are you waiting for, beautiful? We’re here, go get in the water!"
    scene ch9_178 with dissolve
    s "I’m waiting for [mc] so we can go together."
    a "Then help him, don’t just stand there hugging him."
    scene ch9_176 with dissolve
    mc "[s] is helping me with something, right?"
    s "Yep."
    a "Aww, you look so cute."
    mc "{i}{size=-5}You can take off the hat now."
    scene ch9_177 with dissolve
    a "Don’t forget the sunscreen, okay? I don’t want to see you like [mc] the other day."
    s "Yes, [arelatks]."
    jump ch9174sskip
label ch9174sskip:
    scene ch9_179 with dissolve
    d "Didn’t we forget something in the car?"
    mc "I’ve already taken everything of mine out, not sure about the others."
    s "Me too."
    k "No, [drelatks]."
    scene ch9_180 with dissolve
    d "I’ll be right back."
    mc "Where are you going?"
    d "We forgot to buy ice. I’ll go to the nearby supermarket."
    mc "Do you want me to come with you?"
    d "No, I’ll be quick."
    scene ch9_181 with dissolve
    s "Can you help me put on sunscreen?"
    mc "Of course."
    mc "Do you have the sunscreen?"
    s "Nope."
    a "I have it."
    scene ch9_182 with dissolve
    mc "Thanks."
    mc "Nice glasses."
    a "Do they look good on me?"
    mc "They look great, [arelat] [a]."
    a "I bought them at the supermarket for half price the other day, *giggles*"
    scene ch9_183 with dissolve
    a "They say UV light damages your eyes, so that’s why I bought them."
    mc "I hadn’t seen you wear them before."
    a "I didn’t have a good excuse to wear them."
label ch9s4:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene1 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_184 with dissolve
    s "Can you put sunscreen on my back?"
    mc "Sure."
    pause
    scene ch9_185 with dissolve
    a "What a beautiful day."
    mc "See? And you didn’t want to come..."
    a "I had a bit of a headache from drinking so much last night."
    pause
    image ch9_186anim:
        "ch9_186" with dissolve
        2.0
        "ch9_187" with dissolve
        2.0
        repeat
    scene ch9_186anim with dissolve
    mc "I also woke up with a bit of a headache, but it went away with breakfast."
    a "I didn’t have breakfast."
    mc "There’s the problem."
    pause
    s "Can you also put it on my legs, please?"
    scene ch9_188 with dissolve
    pause
    scene ch9_190 with dissolve
    mc "Aren’t you hungry?"
    mc "I can order something to eat here on the beach."
    a "No need, dear, you know I’m on a diet."
    mc "It’s not good to skip meals too often."
    image ch9_191anim:
        "ch9_191" with dissolve
        2.0
        "ch9_192" with dissolve
        2.0
        repeat
    scene ch9_191anim with dissolve
    a "I’m trying something called intermittent fasting, had you heard of it before?"
    mc "yeah, I think I’ve heard of that."
    mc "I don’t think you should aim to lose more weight, you look spectacular just the way you are."
    pause
    scene ch9_193 with dissolve
    a "Or I could follow your diet."
    mc "Well, maybe following my diet isn’t the best idea either, haha."
    mc "Unless you want to end up like a blowfish."
    scene ch9_194 with dissolve
    a "Haha, but I already am."
    mc "[arelat!cl] [a], your body dysmorphia is starting to worry me."
    a "My what?"
    image ch9_195anim:
        "ch9_195" with dissolve
        2.0
        "ch9_195-" with dissolve
        2.0
        repeat
    scene ch9_195anim with dissolve
    mc "Body dysmorphia, it’s when you mentally feel either too fat or too thin... or something like that."
    a "I think it refers to focusing too much on your flaws."
    mc "Yeah, I think that’s a better definition."
    a "It’s just that I want to get back to those times when I was more agile. Now I can’t even run twenty meters without getting tired."
    mc "Well, you can fix that with cardiovascular exercise, the diet will just weaken you more."
    a "Do you think so?"
    mc "Yes."
    s "I’m very agile."
    a "I know, honey."
    a "I envy you young people, so young and full of energy."
    a "And here I am, old and worn out..."
    s "{size=-5}{i}*Uhmm*..."
    mc "You're exaggerating. You don't even look old."
    image ch9_202anim:
        "ch9_202" with dissolve
        1.0
        "ch9_203" with dissolve
        1.0
        "ch9_204" with dissolve
        1.0
        repeat
    scene ch9_202anim with dissolve
    a "I’m just joking, haha."
    s "{size=-5}{i}*Hmp*... *Uh*.."
    pause
    mc "What are you reading?"
    a "It’s a novel I bought the day we went to the supermarket."
    mc "Is it good?"
    a "It’s fantastic, I just started reading it and I’m hooked. I’ll lend it to you later."
    s "{size=-5}{i}*Huh*..."
    pause
    image ch9_208-anim:
        "ch9_208-" with dissolve
        1.0
        "ch9_208--" with dissolve
        1.0
        "ch9_208---" with dissolve
        1.0
        repeat
    scene ch9_208-anim with dissolve
    a "Speaking of novels, I remember when you were a kid, you said you wanted to be a writer."
    mc "Really?"
    a "Yeah, you were about twelve."
    mc "Yeah, well."
    mc "As a kid, I wanted to be a writer-firefighter-police officer-military, all at the same time, haha."
    a "Haha, you had a lot of goals."
    s "{size=-5}{i}*Huh* [mc]."
    image ch9_209anim:
        "ch9_209" with dissolve
        1.0
        "ch9_210" with dissolve
        1.0
        "ch9_211" with dissolve
        1.0
        repeat
    scene ch9_209anim with dissolve
    mc "I still want to."
    mc "And you, what did you want to be when you were a child?"
    a "Me? Hmm..."
    pause
    a "Honestly, a housewife, haha."
    a "I never had many expectations."
    mc "No, that’s a good goal."
    mc "Although more than a goal, it’s more like a lifestyle, right?"
    s "{size=-5}{i}[mc]{w=0.5}, *hmm*."
    a "Well, you see, as a child I really liked modeling and those things."
    a "I suppose I would have liked to be a model or a fashion designer."
    scene ch9_196 with dissolve
    mc "Those things can still be achieved."
    a "Yeah, I think so."
    a "Maybe with a lot of luck."
    k "[mc]..."
    scene ch9_212 with dissolve
    k "Could you bring me the sunscreen?"
    mc "Wait, let me finish with [s]."
    scene ch9_197 with dissolve
    pause
    scene ch9_198 with dissolve
    pause
    scene ch9_197 with dissolve
    mc "All done."
    scene ch9_212 with dissolve
    k "Bring it to me..."
    mc "Lift your butt and come get it."
    k "Aww..."
    scene ch9_213 with dissolve
    mc "All done, beautiful."
    s "[mc]..."
    $ renpy.end_replay()
label ch9k1:
    scene ch9_214 with dissolve
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene2 fadein 1.0
        play background beachsfx fadein 1.0
    mc "Here you go."
    k "Put it on my back."
    mc "Here, put it on yourself."
    k "Put it on me, baby."
    scene ch9_220- with dissolve
    mc "([drelat!cl] [d] isn’t here...)" with dissolve
    pause
    scene ch9_215 with dissolve
    mc "Alright..."
    mc "And don’t call me baby, it’s weird..."
    k "I told you, he does whatever I tell him."
    mia "Yeah, I see."
    k "It’s like having a slave but more obedient."
    mc "Yeah, [k], we heard you, you’re very funny..."
    image ch9_218anim:
        "ch9_218" with dissolve
        2.0
        "ch9_219" with dissolve
        2.0
        repeat
    scene ch9_218anim with dissolve
    k "Does your boyfriend also do whatever you ask?"
    mc "(Your boyfriend? What the hell is she trying to say?)" with dissolve
    mia "I’ve got him totally whipped."
    "*Laughter*"
    show ch9_217 with dissolve:
        xalign 0.0 yalign 0.0 zoom 1.0
    k "I thought you were going to bring your boyfriend."
    mia "So he can get annoyed after ten minutes saying he wants to leave? Nah."
    mia "Today I want to spend the day with my friend."
    k "Aww, I love you too."
    show ch9_217:
        subpixel True
        xalign 0.0 yalign 0.0 zoom 1.0
        ease 3 xalign 1.0 yalign 1.0 zoom 1.0
    pause 3
    show ch9_217:
        subpixel True
        xalign 1.0 yalign 1.0 zoom 1.0
        ease 6 xalign 0.1 yalign 0.5 zoom 0.9
    pause 6
    mc "([dereck], you lucky bastard...)" with dissolve
    if miatell > 2:
        mc "(Though, I hooked up with her the other day so... maybe not that lucky.)" with dissolve
    pause
    scene ch9_218anim with dissolve
    k "Put some on my legs too, please."
    mc "{size=-5}{i}It’s already a lot that I’m putting sunscreen on you, don’t you remember our current situation with [drelat] [d]?"
    k "{size=-5}{i}He went to buy ice at the supermarket, he’ll be a while."
    mia "Hey, rude, I also want to be part of the conversation."
    k "He’s scared that my [drelatks] will see him putting sunscreen on me."
    mia "Isn’t that what a boyfriend does? Apply sunscreen, worry about his girl."
    mc "(What the hell are they talking about?)" with dissolve
    mc "(Oh, I remember now!)" with dissolve
    mc "(But if [mia] already knows about us, I don’t know why we have to keep pretending.)" with dissolve
    mc "(Alright, I guess I can play along.)" with dissolve
    image ch9_221anim:
        "ch9_221" with dissolve
        2.0
        "ch9_222" with dissolve
        2.0
        "ch9_223" with dissolve
        2.0
        repeat
    scene ch9_221anim with dissolve
    mia "Aww, [mc] is so sweet with you."
    k "He’s a sweetheart, always looking for ways to please me."
    k "I’m his first love, right, darling?"
    mc "..."
    mia "Aww, he’s blushing."
    mia "My boyfriend isn’t like that at all."
    mc "Maybe you’re not treating your boyfriend the way [k] treats me."
    mia "And what does [k] do that makes you treat her so well?"
    mc "Well, she washes my clothes, greets me after work with a kiss and dinner ready."
    mia "Really? *Giggles*."
    mc "Yeah, and I haven’t even mentioned her cooking. It’s out of this world."
    mia "I see. I’ll try to put that into practice."
    k "What can I say, I'm a dream of a girlfriend"
    scene ch9_222- with dissolve
    pause 0.5
    scene ch9_223- with dissolve
    mc "Nah, the truth is I’m nice to her because she gives me her ass."
    k "What?!" with hpunch
    mia "*Giggles* Now I get it."
    k "That’s a lie! I’m totally a virgin there, and I’ll stay that way."
    show ch9_217 with dissolve:
        xalign 0.1 yalign 0.5 zoom 0.9
    mc "She’s embarrassed to admit it."
    mia "Yeah, you can tell."
    k "[mia], that’s obviously not true."
    mia "Okay."
    k "I’m serious."
    mia "I believe you."
    k "Really."
    mia "A-ha."
    scene ch9_220-- with dissolve
    s "What are you guys doing?"
    mia "Your swimsuit looks so cute."
    s "Thanks, your bikini is cute too."
    scene ch9_224 with dissolve
    mia "Aren’t you going to get in the water?"
    s "I’m waiting for [mc]."
    mia "Aww, how sweet."
    mia "Hurry up, [mc], someone's waiting for you here."
    k "Wait, you haven't finished."
    image ch9_225anim:
        "ch9_225" with dissolve
        2.0
        "ch9_226" with dissolve
        2.0
        "ch9_227" with dissolve
        2.0 
        repeat
    scene ch9_225anim with dissolve
    k "What [mc] said isn’t true, by the way."
    mia "Yeah, [k], we believe you."
    s "What isn’t true?"
    k "That [mc] is a woman."
    s "Haha."
    k "Of course it’s not true because he’s half-man."
    if stephloving == "True":
        s "Haha, women don’t have huge dicks."
        mia "Huh?"
        "..."
        pause
        s "Don’t blame me, that’s just how men are."
        "Haha."
        mc "(I had a mini heart attack.)" with dissolve
        mia "Haha, you’re very witty."
        mia "I like you, [s]."
        k "Wait until you get to know her better."
    image ch9_228anim:
        "ch9_228" with dissolve
        2.0
        "ch9_229" with dissolve
        2.0
        "ch9_230" with dissolve
        2.0
        repeat
    scene ch9_228anim with dissolve
    s "Don’t believe the ugly witch."
    mia "Haha."
    mc "I think you’re ready now."
    k "Don’t stop applying it."
    mc "[k], there are no more parts left where I haven’t put sunscreen."
    k "I like the massage."
    mc "Alright."
    mc "But you’ll have to give it to me when we get home."
    k "Give you what?"
    scene ch9_232 with dissolve
    pause
    scene ch9_231 with dissolve
    mc "You know what I mean."
    mc "(Oh, look at that... her ass looks so fucking good in the sunlight.)" with dissolve
    pause
    scene ch9_233 with hpunch
    k "![mc]!"
    pause
    scene ch9_234 with dissolve
    k "{i}{size=-5}Stop doing that."
    mia "Looks like you’re going to have a tough night, [k]."
    scene ch9_220 with dissolve
    k "No one is putting anything in my ass today or ever."
    mc "Alright, you’re all set."
    scene ch9_235- with hpunch
    pause 0.2
    scene ch9_235 with dissolve
    k "Hey!"
    pause
    scene ch9_236 with dissolve
    k "Where do you think you’re going? You need to put sunscreen on my friend now."
    k "Do you want [mc] to put sunscreen on you too?"
    mia "So you can go crazy like last time?"
    scene ch9_237 with dissolve
    mia "I’ll pass."
    k "Hey, what do you mean?"
    mia "You know."
    k "I didn’t go crazy, it was all a misunderstanding."
    mia "You didn’t talk to me for an entire day."
    scene ch9_238 with dissolve
    mc "Yeah, I’ll pass too. You’re too toxic and jealous, [k]."
    k "Stop talking crap, I’m not jealous and I didn’t go crazy."
    scene ch9_237 with dissolve
    k "And I did talk to you at night, I sent you a message, don’t lie."
    mia "Yeah... I prefer to avoid problems."
    k "What problems?!"
    $ renpy.end_replay()
    scene ch9_239 with dissolve
    s "Let’s get in the water already, okay?"
    scene ch9_240 with dissolve
    mc "Yeah, let’s go."
    k "It wasn’t jealousy, stop saying that!"
    stop music fadeout 1.5
    stop background fadeout 2.0
label ch9s5:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
    scene ch9_240__1 with fade
    play music scene2 fadein 1.5
    play background "audio/beachsfx.ogg" fadein 1.5 loop 
    s "It’s cold!"
    mc "Come on, run!"
    scene ch9_240_1 with dissolve
    s "It’s really cold!"
    mc "It’s not."
    s "Wait, [mc], yes it is cold!"
    mc "No, come on."
    play sound "audio/splashw.mp3" volume 0.3
    scene ch9_240_2 with hpunch
    s "Oh, really?"
    mc "Ah!"
    s "Wasn’t it supposed to not be cold?"
    mc "Stop, [s]!"
    scene ch9_240_3 with dissolve
    mc "This is war!"
    s "No, haha! Don’t splash me!"
    jump ch9bfr240
init python:
    def ch9_240shj1_(trans, st, at):  
        trans.set_child("ch9_240shj1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_240sgd2_(trans, st, at):  
        trans.set_child("ch9_240sgd2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 39:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_240sgd3_(trans, st, at):  
        trans.set_child("ch9_240sgd3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 39:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

screen ch9_240shj1_():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.005) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("contch9_240shj1_") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_240sgd2_():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.045) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("afterch9_240sgd2_") style "textbutton_choice"
        hbox:
            yalign 0.05
            xalign 0.99
            textbutton "Pov 2" action Jump("ch9_240sgd3_") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_240sgd3_():
        vbox:
            xalign 0.99
            yalign 0.8
            textbutton "Slow" action SetVariable("anim_speed", 0.045) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.7
            textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
        vbox:
            xalign 0.99
            yalign 0.6
            textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"        
        hbox:
            yalign 0.95
            xalign 0.99
            textbutton "Continue" action Jump("afterch9_240sgd2_") style "textbutton_choice"
        hbox:
            yalign 0.05
            xalign 0.99
            textbutton "Pov 1" action Jump("ch9_240sgd2_") style "textbutton_choice"
        hbox:
            yalign 0.95
            xalign 0.05
            textbutton _("Hide") action HideInterface() style "textbutton_choice"

label ch9bfr240:
    image ch9_240sgd2_:
        function ch9_240sgd2_
    image ch9_240sgd3_:
        function ch9_240sgd3_
    image ch9_240shj1_:
        function ch9_240shj1_
    if stephloving == "True":
        scene ch9_240_4
        mc "I’m a shark, *rwar*!"
        s "Noo, a shark that roars like a lion is going to eat me!"
        scene ch9_240_5 with dissolve
        s "*Kyaa!*."
        mc "Hahaha."
        scene ch9_240_6 with dissolve
        mc "I’m going to eat you!"
        s "Noo, help!"
        scene ch9_240_8 with dissolve
        mc "Nom..."
        s "The shark bit me! Kyaa! Hahaha."
        mc "*Sniff* Ahh..."
        s "No, don’t bite me!"
        scene ch9_240_9 with dissolve
        mc "I’m going to eat you all up."
        scene ch9_240_8 with dissolve
        mc "*Rwaar*"
        s "Noo!"
        mc "*Sniff*, hmm..."
        scene ch9_240_18 with dissolve
        mc "Hmm, salty."
        s "Stop, [mc], you’re tickling me, *tee-hee*."
        pause
        scene ch9_240_11 with dissolve
        s "You’re the pervy shark, hehe."
        mc "The what shark? Don’t call me that, [s]..."
        s "Why? You are one."
        mc "I don’t like it when you call me that."
        scene ch9_240_10 with dissolve
        s "The horny shark!"
        mc "Not that either!" with hpunch
        mc "Better not give me names, haha."
        scene ch9_240_12 with dissolve
        s "The gluttonous shark!"
        mc "That name fits me well."
        mc "The gluttonous shark wants to keep eating!" with vpunch
        s "*Kyaa* haha."
        mc "I’ve eaten your legs already, hmm, what else can I eat?"
        stop music fadeout 1.5
        scene ch9_240_13 with dissolve
        play music sexy3 fadein 1.5
        s "*Tee-hee* Here’s something for the gluttonous shark to eat."
        mc "Uh..."
        pause
        scene ch9_240_14 with dissolve
        pause
        scene ch9_240_15 with dissolve
        mc "*Hmmp*."
        s "Why isn’t the shark eating now? Eat, little glutton..."
        scene ch9_240_16 with dissolve
        s "*Uhm* That’s it, keep eating."
        s "*Hmm* I think the shark lost its teeth, it’s not biting like before, hehe."
        mc "I’m going to bite you for real!"
        s "No, don’t bite me!"
        scene ch9_240_17 with dissolve
        mc "*Nom, nom, nom*."
        s "It feels good to be eaten by the shark."
        pause
        scene ch9_240_19 with dissolve
        s "I got really wet, but since we’re in the water, it doesn’t show, hehe."
        mc "I-I’m glad, ha-ha..."
        pause
        scene ch9_240_20 with hpunch
        s "Now I’m the pervy shark!"
        s "I’m going to eat you, [mc]!"
        mc "Waa, nooo! Haha."
        mc "Ouch! Wait, haha." with vpunch
        pause
        scene ch9_240_21 with dissolve
        s "O-oh, it’s up again."
        mc "Seems like it, ha-ha..."
        pause
        scene ch9_240_22 with dissolve
        s "Hmm..."
        mc "[s], people are watching us."
        scene ch9_240_23 with dissolve
        s "They’re not looking over here."
        s "Besides, they’re so far away I can’t even make out their faces."
        mc "Yeah, but... It’s one thing to do pervy stuff at home, but doing it here where everyone can see us..."
        s "[drelatks!cl] hasn’t even come back from buying the ice yet."
        scene ch9_240_22 with dissolve
        pause
        scene ch9_240_24 with hpunch
        s "Off with your pants!"
        mc "Hey!"
        $ anim_speed = 0.035
        scene ch9_240shj1_ with dissolve
        mc "Stop, [s]."
        s "You say, 'Stop, [s],' but you never do anything to make me stop, haha."
        s "And I know why."
        mc "Why?"
        s "Because you like it!"
        mc "*Hmm*... (I’d love to say otherwise, but the truth is I love it.)" with dissolve
        mc "Aren’t you afraid someone will see you doing that?"
        s "As long as it’s not [drelatks], nah."
        mc "We could still get into trouble, the beach isn’t for doing these things."
        s "No one’s watching."
        pause
        call screen ch9_240shj1_ with dissolve
    else:
        jump ch9stnws
label contch9_240shj1_:
        scene ch9_240_27 with dissolve
        s "I’m really turned on, [mc]."
        mc "W-what?"
        pause
        $ anim_speed = 0.035
        scene ch9_240sgd3_ with dissolve
        mc "Hey..."
        s "*Huh*... This feels good."
        s "It’ll only be a little while, okay?"
        mc "People will see us, [s]!"
        s "*Uh*{w=0.5}No, I’ll keep watch."
        mc "(I knew going along with her sexual whims was a bad idea.)"
        mc "(But I’m having such a good time...)"
        pause
        scene ch9_240sgd2_ with dissolve
        s "No one’s watching us, okay?"
        s "I just want to rub it a little more to feel... *huh* pleasure..."
        mc "Yeah, I know what you're thinking but..."
        s "Almost there... *uhmm*."
        mc "Y-you can’t do this whenever you feel like it."
        s "It's just... when you get hard, I start imagining things and then I get wet."
        mc "Ah, w-well..."
        pause
        call screen ch9_240sgd2_ with dissolve

label ch9_240sgd2_:
    scene ch9_240sgd2_ with dissolve
    call screen ch9_240sgd2_ with dissolve
label ch9_240sgd3_:
    scene ch9_240sgd3_ with dissolve
    call screen ch9_240sgd3_ with dissolve

label afterch9_240sgd2_:
    play music scene2 fadein 1.0
    scene ch9_241 with dissolve
    mia "Hey, guys, what are you doing? Can we join?"
    play sound "audio/splashw.mp3"
    scene ch9_242 with hpunch
    s "Kyaa!"
    $ renpy.end_replay()
    pause
    scene ch9_243 with dissolve
    s "*Cough, cough* Why did you do that? You’re mean."
    mc "Sorry!"
    k "[mc], do you want to swim with us?"
    scene ch9_244 with vpunch
    s "No, I’m using him."
    k "What do you mean you're using him? He's a living person, he decides who to be with."
    s "He wants to be with me, I asked him to come to the water first!"
    mia "You were right, haha."
label ch9km1:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene1 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_245 with dissolve
    s "Right about what?"
    mia "Lend him to us for a bit."
    k "At least let him decide."
    s "He wants to stay with me, go away."
    k "What do you say, [mc]?"
    mc "Erm-"
    s "He doesn’t want to go with you, stop pestering."
    k "But he hasn’t said anything yet."
    s "I told him to come to the water first, so I’m in charge."
    s "And if I say he stays with me, he stays!"
    jump labelafterch9_kmdnc_1
label ch9stnws:
    play music scene2 fadein 1.0
    scene ch9_241 with fade
    mia "Hey, guys, what are you doing? Can we join?"
    scene ch9_245 with vpunch
    s "No, I’m using him."
    k "What do you mean you're using him? He's a living person, he decides who to be with."
    s "He wants to be with me, I asked him to come to the water first!"
    mia "You were right, haha."
    scene ch9_244 with dissolve
    s "Right about what?"
    mia "Lend him to us for a bit."
    jump ch9km1
    k "At least let him decide."
    s "He wants to stay with me, go away."
    k "What do you say, [mc]?"
    mc "Erm-"
    s "He doesn’t want to go with you, stop pestering!" with hpunch
    k "But he hasn’t said anything yet."
    s "I told him to come to the water first, so I’m in charge."
    s "And if I say he stays with me, he stays!"
    jump labelafterch9_kmdnc_1
init python:
    def ch9_kmdnc_(trans, st, at):  
        trans.set_child("ch9_kmdnc1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 2    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_kmdnc2_(trans, st, at):  
        trans.set_child("ch9_kmdnc2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 2    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
label labelafterch9_kmdnc_1:
    image ch9_kmdnc_1:
        function ch9_kmdnc_
    image ch9_kmdnc_2:
        function ch9_kmdnc2_
    $ anim_speed = 0.025
    scene ch9_kmdnc_1 with dissolve
    k "Come on, [mc], dance with us."
    s "Haha, you're dancing without music."
    pause
    s "..."
    s "S-stop dancing already!" with hpunch
    k "What, now we can't even dance?"
    s "Let's go, [mc]."
    mc "..."
    pause
    s "[mc]!" with hpunch
    mc "What?"
    s "Ush! They're doing it on purpose to make them bounce!"
    k "Hahaha, What things are bouncing?"
    $ anim_speed = 0.015
    scene ch9_kmdnc_2 with dissolve
    s "You're dancing to make your boobs bounce like balls because you know [mc]..."
    s "..."
    pause
    scene ch9_247 with dissolve
    s "..."
    mia "That's it, [k], move those hips."
    k "Lalala, nanana~"   
    show ch9_248 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2) with dissolve
    k "Woohoo, [mc]..."
    k "Look, [mc], look over here."
    pause
    play music scene1 fadein 0.5
    scene ch9_249 with hpunch
    k "Watch out! Hahaha." 
    mia "Wait, [s]!"
    s "Come here, you pair of ugly witches, horrid... uh, furries!"
    mia "It was just a joke between friends!"
    k "Furries?!"
    $ renpy.end_replay()
    scene blackscreen with dissolve
    pause
    scene ch9_250-- with fade
    s "*Glug, glug*."
    mc "Hey, that's the last one, don't drink it all yourself."
    d "This is the life, right guys?"
    s "Yes!"
    k "Yeah, but it would be even better with some cute guys around."
    scene ch9_250 with dissolve
    k "Just kidding."
    d "You better be..."
    k "[s], how can you eat so much and not gain weight?"
    s "I don't know."
    mc "Hey, give me that, you're going to finish it all yourself."
    scene ch9_251- with dissolve
    s "Ugh! I can't reach the chips."
    k "Seriously, all that fat will make you sick."
    s "Shut up, I don't gain weight like you."
    k "Your butt does."
    s "That's not true."
    scene ch9_252 with dissolve
    k "It's in your genes, I suffer from it too."
    s "[arelatks!cl], tell her to shut up."
    a "Your butt is fine, [s]."
    mia "There's nothing wrong with having a big butt."
    scene ch9_254 with dissolve
    k "[mc], send us the photos."
    mc "I sent them to you a while ago."
    k "Right, here they are."
    mia "These are bad photos..."
    k "[mc], you took very few."
    mc "I did my best, girls."
    mia "He took them horizontally..."
    s "[mc], open your mouth."
label ch9s6:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene2 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_255 with dissolve
    s "Here comes the airplane."
    scene ch9_256 with dissolve
    mc "Yum."
    s "Hehe."
    if stephloving != "True":
        jump ch9256sskip
    scene ch9_257 with dissolve
    s "{i}{size=-5}[mc], come closer."
    scene ch9_258 with dissolve
    s "{i}{size=-5}I thought of an idea to do sexy things at the beach."
    scene ch9_259 with dissolve
    mc "Oh, really?"
    mc "Wait, no!" with hpunch
    scene ch9_260 with dissolve
    s "{i}{size=-5}I found a secret spot where there's no one around!"
    s "{i}{size=-5}We can go hide there, no one will see us!"
    scene ch9_259 with dissolve
    mc "{i}{size=-5}[s], just wait until we get home, it's only a few hours."
    mc "{i}{size=-5}Besides, we already did some sexy things in the car and earlier in the ocean, aren’t you tired?"
    scene ch9_261 with dissolve
    s "{i}{size=-5}I do get tired but..."
    s "{i}{size=-5}But I'm already in the mood again."
    image ch9_262anim:
        "ch9_262" with dissolve
        1.25
        "ch9_263" with dissolve
        1.25
        repeat
    scene ch9_262anim with dissolve
    mc "Uh..."
    pause
    scene ch9_261 with dissolve
    mc "[s], they're going to see you!"
    jump ch9256sskip
label ch9256sskip:
    scene ch9_264 with dissolve
    k "Aren't you coming to the water with us, [arelatks]?"
    a "No, honey, maybe later. You girls have fun."
    show ch9_266 with dissolve:
        zoom 0.5
    s "[mia], you said you'd teach me to surf! Remember?"
    $ renpy.end_replay()
    mia "Yeah, do you want to go buy your board?"
    s "Yeah."
    mia "You'll need to ask your [drelatks] for money to get it."
    scene ch9_267 with dissolve
    s "[drelatks!cl], the money, quick!"
    d "How far is this surf shop you're talking about?"
    mia "I think it's about a ten-minute walk."
    d "I'll take you."
    s "Hurry up!"
    d "At least let me digest my food first."
    s "But we want to go now."
    d "Alright, help me get up."
    scene ch9_268 with dissolve
    s "*Ugh! Get up, chubby."
    mc "How's your book going, [arelat] [a]?"
    a "I'm only halfway through, but it's getting really good."
    scene ch9_269 with dissolve
    d "We'll be back soon, love."
    a "Yeah."
    pause
    scene ch9_270 with dissolve
    mc "The water is freezing."
    a "With this heat, I wouldn't mind an ice bath."
    mc "Let's go, then."
    a "I don't have a swimsuit, honey."
    mc "You can borrow mine."
    a "Did you bring extra shorts for me?"
    mc "No, I'll lend you the ones I'm wearing."
    a "And you'll just walk around naked, or what?"
    mc "Yeah, what's wrong with that?"
    mc "I'll go au naturel, as nature intended."
    a "What are you, an exhibitionist?"
    mc "Maybe a little, yeah."
    a "[mc]!"
    mc "I'm kidding, haha."
    a "Hey, I saw you with [k]'s friend, trying to be funny..."
    mc "Who, me?"
    a "Yeah, what do you think, that I don't notice?"
    a "She's trying to steal you away from me."
    mc "No way."
    a "You don't like her? She's cute."
    mc "Hmm, nah... she's cute, but I'll pass."
    a "Her mom is [lauren]."
    mc "I remember, but nah..."
    mc "Plus, she has a boyfriend, and we know each other."
    a "..."
    pause
    mc "What? Why are you looking at me like that? Haha."
    a "I don't know..."
    a "I hear her laughing at your jokes a lot..."
    mc "Well, I'm pretty charming."
    a "And handsome, in shape..."
    mc "Haha, you see that because you love me a lot."
    mc "Girls in general don't really notice me."
    a "Now you're going to play modest?"
    mc "Haha, alright, alright. But you can relax, no one’s going to take me away from my [arelat], not ever."
    a "I'm just teasing, honey, you're right. Getting into trouble just for a fling is never a good idea."
    mc "I agree."
    "..."
    pause
    mc "Shall we go in the water?"
    a "[mc], I already told you I’m not wearing a swimsuit."
    mc "Then what’s that I see under your shirt?"
    a "T-this?"
    pause
label ch9a1:
    if _in_replay:
        scene ch9_270 with dissolve
        show screen Replayexit
        play music scene1 fadein 1.0
        play background beachsfx fadein 1.0
    a "Allright, I'll tell you a secret."
    a "Yeah, I’m wearing something, but I really don’t like how it looks on me."
    mc "A bikini?"
    a "Yeah, well, it looks more like lingerie."
    mc "Can I see?"
    a "No, it looks too vulgar."
    mc "What, is it too tight or...?"
    a "Exactly, it's way too tight."
    a "I would’ve worn something else, but [s] was rushing me, and I couldn’t find anything else."
    mc "At least come get your feet wet."
    a "Okay, let’s go."
    mc "Uh, my back itches, and I can’t reach."
    a "Do you want me to scratch it?"
    mc "Yes, please."
    scene ch9_273 with dissolve
    a "[mc], are you sure you put on sunscreen?"
    mc "Yeah, why? Am I sunburned?"
    a "Your back is a little red. Turn around, I’ll put some sunscreen on you."
    scene ch9_272 with dissolve
    mc "I was so busy putting sunscreen on everyone else that I forgot to put it on myself."
    a "It’s pretty red..."
    a "When we get back, remind me to put some ointment on you."
    mc "It’s not that bad, is it?"
    a "I don’t know, it’s just red, but your skin might peel later."
    mc "Damn, last time I couldn’t even sleep because it was so uncomfortable."
    scene ch9_274 with dissolve
    a "You know how sensitive your skin is to the sun, how could you forget sunscreen?"
    mc "I did put it on, I just forgot my back."
    a "Are you sure you put it on?"
    a "Here, let me put some on your front."
    image ch9_276anim:
        "ch9_276" with dissolve
        1.5
        "ch9_275" with dissolve
        1.5
        repeat
    scene ch9_276anim with dissolve
    pause
    a "You didn't put sunscreen on your chest, [mc]. Look how dry it is."
    a "And then I have to put lotion on you because the kid's whole body is burning."
    mc "Sorry, [arelat] [a]."
    a "Haha, I'm just kidding, honey. I don't mind taking care of my [arelatmc]."
    stop music fadeout 4.0
    pause
    play music sexy3 fadein 2.0
    scene ch9_277 with dissolve
    a "Oh..."
    mc "Uh..."
    pause
    scene ch9_278 with dissolve
    pause
    mc "Oops."
    scene ch9_279 with dissolve
    mc "I was just imagining the bikini, haha..."
    a "[mc], what am I going to do with you? *Giggle*."
    a "Don’t worry, I know these things are totally Involuntary."
    mc "After it happening so many times, you’re not even surprised anymore."
    scene ch9_280 with dissolve
    a "No, it still surprises me...{w=0.5} erm..."
    pause
    scene ch9_281 with dissolve
    pause
    a "Honey, you’re going to scare someone if you walk around like that."
    scene ch9_282 with dissolve
    a "You better stay here with me until it calms down."
    mc "Yeah, I should probably do that."
    mc "It doesn’t really stand out that much, does it?"
    scene ch9_284 with dissolve
    pause
    scene ch9_283 with dissolve
    pause
    a "I’m afraid it’s pretty noticeable, and not just a little..."
    scene ch9_282 with dissolve
    a "Did you wear underwear?"
    mc "Uh... actually, I didn’t."
    a "What, [mc]! Why not?"
    mc "I didn’t think I’d need them."
    mc "I’m planning to get in the water anyway, I didn’t want to get them dirty."
    mc "Now that I have a job, I don’t feel like washing clothes that often."
    scene ch9_285 with dissolve
    a "[mc], you have to wear underwear all the time, especially with... that big."
    a "Even with the shorts, the outline is still noticeable."
    mc "Don’t tell me it was obvious I wasn’t wearing underwear before."
    a "Well, if you don’t pay much attention, it’s not that noticeable but..."
    "..."
    scene ch9_281 with dissolve
    a "Erm..."
    pause
    scene ch9_283 with dissolve
    a "The thing is... yes, you need to take care of that."
    pause
    scene ch9_291 with dissolve
    a "Try..."
    pause
    scene ch9_286 with dissolve
    a "{i}Try to hide it a bit, honey."
    mc "{i}I can’t, [arelat] [a]."
    pause
    scene ch9_286- with dissolve
    a "I didn’t know it was so problematic to have one of these..."
    mc "Yeah..."
    pause
    scene ch9_291 with dissolve
    a "..."
    pause
    scene ch9_284 with dissolve
    mc "Aren’t you going to show me the bikini?"
    scene ch9_285 with dissolve
    a "Oh no, [mc]."
    mc "{i}Come on, just a little peek now that no one’s around."
    a "Do you seriously want to see it that badly?"
    mc "You have no idea."
    a "*Giggle* Well..."
    pause
    a "I can show you the top part, but it’ll be quick."
    mc "Guess I’ll have to make do with that."
    scene ch9_292 with dissolve
    a "I’m just going to show you, then I’ll put my shirt back on."
    mc "Sure."
    pause
    scene ch9_294 with dissolve
    a "Here it is."
    a "A bit tight, hehe."
    show ch9_295 with dissolve:
        subpixel True
        yalign 0.5 xalign 0.5 zoom 0.5
        ease 6 xalign 0.5 yalign 0.7 zoom 1.0
    mc "Wow, that’s... tight."
    mc "(Look at those exquisite tits, wow!...)" with dissolve
    mc "(It looks like they’re going to burst out of the bra!)" with dissolve
    pause
    show ch9_295:
        subpixel True
        xalign 0.5 yalign 0.7 zoom 1.0
        ease 3 xalign 0.5 yalign 0.5 zoom 0.5
    a "See?"
    mc "Well, it is a bit tight, but I don’t know."
    mc "I don’t think it looks bad or anything like you said."
    a "You think so?"
    mc "If you ask the girls, I’m sure they’d think the same as me."
    mc "Besides, you’ve got to spice things up in life sometimes and try new styles."
    a "I don’t know... I don’t feel very comfortable."
    pause
    a "But, maybe you’re right."
    mc "Of course I am!"
    show ch9_295:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 3 xalign 0.5 yalign 0.7 zoom 1.0
    mc "Wow, I can’t wait to get home..."
    a "Home? For what?"
    show ch9_295:
        subpixel True
        xalign 0.5 yalign 0.7 zoom 1.0
        ease 1.0 zoom 0.5
    mc "You know..."
    a "No, I don’t know..."
    mc "Yeah, we can't remember..."
    pause
    mc "I just thought that maybe in the privacy of your room, you’d feel less shy showing me the full bikini..."
    a "Yeah, maybe, heh..."
    show ch9_295:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 3 xalign 0.5 yalign 0.7 zoom 1.0
    pause
label afterch9296:
    play music scene1 fadein 0.5
    show ch9_296 with hpunch:
        subpixel True
        xalign 0.7 yalign 0.5 zoom 1.0
        ease 0.05 zoom 0.5
    a "Ah!"
    s "Quick, [mia]! let’s go to the water!"
    scene ch9_297 with vpunch:
        subpixel True
        xalign 0.5 zoom 0.5
    pause
    $ renpy.end_replay()
    scene ch9_298 with dissolve:
        subpixel True
        zoom 0.5
    k "[arelatks!cl], wow!"
    mia "You look stunning, Mrs. [a]."
    a "Th-thank you, girls, you caught me off guard, hehe..."
    k "And you said my bikini was too provocative."
    a "Uh, haha... no, I..."
    a "I just wanted a bit of sun, I’m going to put my shirt back on."
    k "Yeah, you’d better do that, [arelatks], or you’ll drive the guys crazy."
    mia "Leave some for us, haha."
    a "Which guys? Haha."
    k "But seriously, don’t cover up! We’re at the beach."
    mia "No way you’re hiding that cute yellow bikini under all those clothes, Mrs. [a]."
    mc "She thinks she looks vulgar."
    a "I just don’t like how it fits me."
    k "[arelatks!cl], it looks really good on you."
    a "But look how tight it is, what will people think of me?"
    mia "Mrs. [a], what century do you think we’re in?"
    k "Yeah, [arelatks], nobody cares about that."
    mia "Look around, we’re all wearing pretty tight bikinis and no one’s making a fuss, it’s normal."
    a "But your bikinis fit you perfectly."
    a "Look at me, I look like braided meat!"
    k "Are you serious? You look great, [arelatks]."
    scene ch9_299 with dissolve:
        zoom 0.5
    mia "We’re not going to let you put your shirt back on."
    k "Shirts are banned on this beach."
    a "Okay, fine, haha."
    scene ch9_301 with dissolve
    k "That’s the spirit, [arelatks]! Haha."
    mia "We need to show off our bodies while we can; you never know when our beauty will fade."
    a "Well said, [mia]."
    mc "(Uff... such beauties.)" with dissolve
    mc "(I would have loved to stay home with [arelat] [a], but having these beauties around in those sexy bikinis isn’t so bad either.)" with dissolve
    scene ch9_302 with dissolve
    k "[mia], film us, let’s do a runway."
    mia "Yeah, let’s get your [arelatks] to loosen up."
    mia "Hey, but I want to join in too."
    k "[mc], be useful and film us."
label ch9akm1:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene1 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_302- with dissolve
    mia "Can you film us?"
    mc "Sure."
    mia "My phone’s camera isn’t that great, can you use yours instead?"
    mc "Of course, whatever you want."
    scene ch9_302--- with dissolve
    a "Are we going to model for the camera?"
    k "Yes."
    a "Girls, I don’t know how to model."
    k "Just go with it, [arelatks], it’s all in good fun."
    mia "We’re missing the music."
    k "We’ll add the music to the video later."
    k "When I give the signal, you start recording, [mc]."
    mc "Got it."
    scene blackscreen with dissolve
    pause 0.5
    show screen noclick
    image ch9_mdl = Movie(size=(1920, 1080), play="images/scenes/ch9/anim/a_ks/ch9_mdl.mp4", loop=False)
    show ch9_mdl with dissolve
    $ renpy.pause(5.0, hard=True)
    mia "Oh, so much glamour!{w=2}{nw}"
    $ renpy.pause(1.0, hard=True)
    mc "(What a great ass!){w=2}{nw}" with dissolve
    $ renpy.pause(2.0, hard=True)
    k "Just look at that Latina beauty!{w=2}{nw}"
    $ renpy.pause(1.0, hard=True)
    k "Does [dereck] eat all of that?{w=1}{nw}"
    $ renpy.pause(0.5, hard=True)
    mia "Haha{w=0.5}{nw}"
    mc "(She’s not far behind either, slim but with a sexy figure...){w=2}{nw}" with dissolve
    $ renpy.pause(1.0, hard=True)
    mc "Oh, wow!{w=1}{nw}" with dissolve
    $ renpy.pause(0.5, hard=True)
    k "Wow, [arelatks]!{w=1}{nw}"
    mia "Mrs. [a]!{w=2}{nw}"
    $ renpy.pause(3.0, hard=True)
    mc "(Look at that ass!){w=2}{nw}"
    $ renpy.pause(1.5, hard=True)
    hide screen noclick
    scene ch9_302-- with dissolve
    a "Oh my God, how embarrassing!"
    k "[arelatks!cl]!"
    mia "And she was pretending to be shy, haha."
    scene ch9_303 with dissolve
    mia "I knew you had a great body, but wow, mrs. [a], you're gorgeous! haha."
    a "Hahaha, look what you made me do!"
    $ renpy.end_replay()
    k "No, [arelatks], don’t act shy now, you just modeled like you were in Paris."
    mia "What a lucky man Mister [d] is!"
    scene ch9_304 with dissolve
    pause
    scene ch9_305 with dissolve
    mc "What’s wrong? Don’t you want to model too?"
    s "Uh... no, I... I’m not in the mood."
    scene ch9_307 with dissolve
    a "Come on, don’t be shy! It’ll be fun!"
    mia "Even your [arelatks] did it."
    k "We’ve all done it, you’re the only one left."
    s "Hmm..."
    show ch9_310 with Dissolve(0.2):
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 0.25 zoom 0.6
        ease 0.2 zoom 0.5
        ease 0.15 zoom 0.55
    pause
    show ch9_308 with Dissolve(0.2):
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 0.25 zoom 0.8
        ease 0.2 zoom 0.5
        ease 0.15 zoom 0.55
    pause
    show ch9_309 with Dissolve(0.2):
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 0.25 zoom 1.0
        ease 0.2 zoom 0.5
        ease 0.15 zoom 0.7
        ease 0.15 zoom 0.5
        ease 0.15 zoom 0.55
    pause
    scene ch9_311 with dissolve:
        zoom 0.5
    pause
    scene ch9_312 with dissolve:
        zoom 0.5
    s "I don’t feel like it..."
    s "I’m waiting to go surfing with [mia]."
    scene ch9_313- with dissolve
    a "If you don’t want to, that’s okay, sweetie."
    mia "Do you want me to teach you how to surf?"
    s "Yes!"
    k "[arelatks!cl], what are you doing? Don’t put your clothes back on."
    scene ch9_314 with dissolve
    a "No, no, It was just for the video, [k]."
    k "You really exasperate me sometimes, [arelatks]..."
    scene ch9_316 with dissolve
    mc "[k] is right, [arelat] [a]."
    mc "You even modeled the bikini, so why not stay like this for a while?"
    mc "At least to sunbathe."
    a "Alright, alright!"
    a "I’ll do it just because you’re almost forcing me to."
    scene ch9_314 with hpunch
    k "No, I want you to do it because you want to!"
    a "But-{w=0.5}{nw}"
    k "But nothing!"
    k "I know you want to."
    k "Put that embarrassment aside!"
    k "..."
    k "Sorry for shouting..."
    scene ch9_316 with dissolve
    a "Okay, okay, everyone calm down."
    a "I’m going to do it because I want to, happy?"
    mc "Very happy."
    a "But only to sunbathe, nothing more."
    k "*Exhales*."
    scene ch9_318 with dissolve
    d "What are you all doing?"
    k "We were talking about how great the bikini looks on your beautiful wife."
label ch9a2:
    if _in_replay:
        show screen Replayexit
        play music scene1 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_319 with dissolve
    d "Oh, wow..."
    d "Um..."
    d "Honey, that bikini looks very tight on you, could it be?"
    k "It looks good, [drelatks]."
    a "You bought it for me, don’t you remember?"
    d "Really?"
    d "It must have been several years ago."
    k "[drelatks!cl]!" with hpunch
    k "Man you had to be... Come with me to the water."
    d "What’s wrong?"
    k "Quickly!" with hpunch
    scene ch9_322 with dissolve
    d "{size=-5}So, am I wrong for not wanting others to see my wife like this?"
    k "{size=-5}[drelatks!cl]!"
    pause
    mc "I don’t think..."
    mc "What’s so funny, [arelat] [a]?"
    a "Oh, nothing special."
    a "I just found it funny how he acted, as if he cared."
    a "It’s amusing how hypocritical he is."
    mc "I hope it didn’t make you change your mind."
    a "Not at all, on the contrary, now more than ever I want to wear this bikini."
    pause
    mc "(Now I get it, she wore it to make [drelat] [d] angry.)" with dissolve
    mc "([arelat!cl] [a] isn’t the type of woman who likes to show off her body.)" with dissolve
    pause
    scene ch9_323 with dissolve
    mc "I do like how it looks on you, [arelat] [a]."
    a "Yeah, I know you like it, honey..."
    pause
    mc "So... are you going to sunbathe?"
    a "I suppose so."
    scene ch9_324 with vpunch
    mc "Should I put sunscreen on you?"
    a "Uh...."
    a "Yes, please. *giggles*"
    pause
    scene ch9_324- with dissolve
    pause
    scene ch9_325 with dissolve
    pause
    mc "Erm... it seems like it hasn’t gone down yet."
    a "Yeah, I can see that..."
    pause
    scene ch9_326- with dissolve
    a "[mc], don’t just stand there!"
    mc "Oops!"
    scene ch9_327 with dissolve
    a "Don’t just stand there with that bulge!"
    mc "I didn’t realize."
    a "How could you not notice such a volume coming out of your shorts? *giggle*"
    mc "I’m sorry."
    mc "Anyway, they wouldn’t notice even if they looked this way, we’re far away."
    a "I wouldn’t be so sure."
    pause
    scene ch9_327- with dissolve
    pause
    scene ch9_327-- with dissolve
    pause
    image ch9_327anim:
        "ch9_327-" with dissolve
        2.0
        "ch9_327--" with dissolve
        2.0
        repeat
    scene ch9_327anim with dissolve
    mc "You have very soft skin."
    a "And you, rough hands. *giggles*"
    mc "It’s the calluses from work, am I hurting you?"
    a "No, I’m just playing around."
    pause
    a "This is how a man's hands should be. That's what my aunt used to say."
    pause
    scene ch9_327--- with dissolve
    mc "(Damn, it’s starting to hurt...)"
    mc "(I just want to get home and have my [arelat] [a] all to myself until I can’t take it anymore!...)"
    pause
    a "Are you done yet?"
    mc "N-no..."
    scene ch9_327---- with dissolve
    pause
    mc "(That fat and delicious ass, God...)" with dissolve
    scene ch9_327----- with dissolve
    a "[mc]."
    scene ch9_327_ with dissolve
    mc "I’m applying sunscreen on you."
    a "Yes, but..."
    mc "Remember that the sun doesn’t discriminate, it burns everywhere on your body."
    scene ch9_327_- with dissolve
    a "W-well..."
    a "Just don’t draw too much attention."
    mc "Sure."
    scene ch9_327_-- with dissolve
    pause
    scene ch9_327_--- with dissolve
    pause
    image ch9_327_--anim:
        "ch9_327_--" with dissolve
        2.0
        "ch9_327_---" with dissolve
        2.0
        repeat
    scene ch9_327_--anim with dissolve
    a "Don’t think I don’t know what you’re doing, young man..."
    mc "I’m applying sunscreen on you."
    a "A-ha..."
    pause
    mc "What else am I doing?"
    a "You know very well, don’t pretend otherwise."
    mc "I’m just being considerate with my beautiful [arelat]."
    a "Yes, sure..."
    pause
    mc "(Damn, this is so hot...)" with dissolve
    mc "(The good thing is that we’re far from people and no one can see us.)" with dissolve
    mc "(I can take my time to savor the moment.)" with dissolve
    pause
    scene ch9_336 with dissolve
    a "Okay, honey, that’s enough."
    mc "What’s wrong?"
    a "You know very well what’s wrong."
    a "Someone might see us and take things out of context."
    scene ch9_328 with dissolve
    mc "I think the context is pretty clear."
    scene ch9_329 with dissolve
    a "No, no... I think you’re mistaken."
    a "Whatever you have in mind, better forget it."
    pause
    scene ch9_330 with dissolve
    mc "Maybe you could change your mind later?"
    a "Hm?"
    image ch9_328anim:
        "ch9_328" with dissolve
        1.75
        "ch9_329" with dissolve
        1.75
        "ch9_330" with dissolve
        1.75
        repeat
    scene ch9_328anim with dissolve
    mc "You know, when we get home this afternoon, just you and me in your room again..."
    mc "Not applying sunscreen, but a massage."
    mc "And... maybe repeat what we did yesterday?"
    a "We said we wouldn’t talk about that."
    mc "Yes, I know."
    pause
    a "Besides, we don’t even know if my room will be available."
    mc "Is that a yes?"
    a "T-that’s not what I said!"
    pause
    scene ch9_331 with dissolve
    mc "Should I put some on your legs too?"
    a "Please."
    scene ch9_332 with dissolve
    pause
    scene ch9_333 with dissolve
    a "On the legs."
    mc "That’s what I’m doing."
    pause
    image ch9_331anim:
        "ch9_331" with dissolve
        1.75
        "ch9_332" with dissolve
        1.75
        "ch9_333" with dissolve
        1.75
        repeat
    scene ch9_331anim with dissolve
    pause
    a "Are you having fun?"
    mc "Yes, very much."
    a "I meant if you’re having fun at the beach."
    mc "I was referring to that too."
    mc "[arelat!cl] [a], you sure have a mind on you."
    a "Stop it! Haha."
    a "You’re an expert at making me say things I don’t want to."
    mc "What? I’m just answering your questions."
    a "Yeah, yeah, sure..."
    pause
    mc "(I’m way too horny...)" with dissolve
    pause
    a "It feels good."
    a "You have good hands for giving massages."
    mc "I know, it’s one of my talents. But this isn’t really a massage."
    a "Well, it feels like one."
    pause
    mc "([a] knows what she’s doing letting me touch her body...) " with dissolve
    mc "(She lets me put sunscreen on her knowing my intentions.) " with dissolve
    mc "(Isn’t that a way to provoke me?) " with dissolve
    mc "(It definitely is, then... even if she says no, she’s probably expecting a reaction from me.) " with dissolve
    pause
    scene ch9_334 with dissolve
    pause
    scene ch9_335 with dissolve
    a "Hey..."
    pause
    scene ch9_336 with dissolve
    a "No, [mc]."
    pause
    scene ch9_328anim with dissolve
    mc "I'm really turned on, [arelat] [a]..."
    mc "The bikini and applying sunscreen are starting to drive me crazy."
    a "Oh..."
    pause
    scene ch9_336- with dissolve
    mc "Yeah..."
    pause
    scene ch9_337 with dissolve
    pause
    scene ch9_339 with dissolve
    a "..."
    pause
    scene ch9_340 with dissolve
    a "H-honey..."
    pause
    scene ch9_341 with dissolve
    mc "You know I can't resist my urges when I'm alone with you..."
    a "We're not alone, [mc]..."
    mc "No one can see us."
    a "Sure, until someone does."
    pause
    scene ch9_342 with dissolve
    a "No, [mc], I’m not going to kiss you with [d] and the girls just a few meters away."
    pause
    scene ch9_344- with dissolve
    a "Okay, that's enough, [mc]."
    mc "Just a little more."
    pause
    scene ch9_345 with dissolve
    mc "Oh, god... you have an amazing breasts, [arelat] [a]."
    mc "Definitely the best on the beach."
    a "God, [mc]..."
    pause
    a "A-are you telling me that with all these sexy girls around, your thirty-something [arelat]'s breasts are the best?"
    a "Well, thirty-something heading toward forty-something, *giggle*."
    mc "Clearly, yes, you have the best body and the best tits."
    a "Oh, God..."
    pause
    scene ch9_346 with hpunch
    a "Alright, I think we’re done here, heh..."
    mc "Huh? B-but..."
    pause
    scene ch9_347 with dissolve
    mc "(She can't be serious.)" with dissolve
    a "Can you help me move the umbrella? It’s blocking the sun."
    mc "[arelat!cl] [a]-{w=1.0}{nw}"
    a "Please, [mc]."
    mc "Sure..."
    scene ch9_348 with dissolve
    pause
    a "Thanks, honey."
    scene ch9_349 with dissolve
    mc "(I feel cheated.)" with dissolve
    mc "(But of course, it's not like I could screw her on the beach...)" with dissolve
    pause
    scene ch9_350 with dissolve
    mc "(But damn it... why does she let me grope her if she’s not going to... I don’t know, at least let me touch her tits a bit more?)" with dissolve
    mc "(I need to release, or my balls are going to explode.)" with dissolve
    pause
    mc "(Maybe I can sneak away for a moment with [k]...)" with dissolve
    mc "(But I don't think we can, [drelat] [d] has been watching us the whole time.)" with dissolve
    mc "(Maybe I could find a moment when he’s distracted or something...)" with dissolve
    scene ch9_352 with dissolve
    mia "Why aren’t you with us on the beach?"
    mc "I forgot to put on sunscreen and was starting to get sunburned on my back."
    mc "(Shit, she’s going to see me with this huge erection while I’m here like a pervert staring at my [arelat] [a].)" with dissolve
    mc "(I’d better stay behind this chair until she leaves.)" with dissolve
    pause
    scene ch9_353 with dissolve
    mia "Enjoying the sun?"
    a "Yeah, haha. I’m making the most of it now that there aren’t many people around."
    mia "Don’t be embarrassed, life is meant to be enjoyed."
    pause
    scene ch9_354 with dissolve
    mia "I’m teaching the girls how to surf, you should come, it's super funny."
    mc "Really?"
    scene ch9_355 with dissolve
    mia "Yeah."
    a "Don’t go too deep into the sea."
    scene ch9_356 with dissolve
    mia "Yeah, don’t worry. Mr. [d] and I are watching them."
    mia "They’re not very good yet, but they’re trying."
    mia "Oh, there’s beer. It must be Mr. [d]’s. Do you think he’ll be mad if I steal one?"
    mc "I don’t think so."
    show ch9_358 with dissolve:
        zoom 0.5 xalign 0.5 yalign 0.5
    mia "Nah, just kidding."
    mia "Aren’t you coming? [k] told me to call you."
    mc "It’s just... I got sunburned on my back and..."
    show ch9_358:
        subpixel True
        zoom 0.5 xalign 0.5 yalign 0.5
        ease 3 yalign 0.7 zoom 1.0
    pause
    mc "(Nice ass...)" with dissolve
    pause
    mia "Hey, [mc]?"
    show ch9_358 with hpunch:
        subpixel True
        yalign 0.7 zoom 1.0 xalign 0.5
        ease 0.5 yalign 0.1 zoom 0.5
    mc "I-I was just saying I’ll come in a bit."
    mia "[k] told me to drag you along if necessary."
    mc "Oh, really? Well, tell her that-{w=0.7}{nw}"
    scene ch9_359 with vpunch
    mc "Hey, wait!"
    mia "Come on, it’s not as fun if it’s just her and me."
    mc "But I..."
    mia "No buts, you’re coming with me."
    mc "(Shit, she’s going to see it!)" with dissolve
    a "Honey, can you put sunscreen on me, please?"
    scene ch9_361 with dissolve
    pause
    mc "Huh?"
    mia "Your [arelat] [a] is talking to you."
    a "I said if you could do me a favor and put sunscreen on my back."
    show ch9_360 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 50 zoom 0.8
    mc "Again?{w=0.5}, I mean! Of course."
    mc "(Thanks, [arelat] [a]!)" with dissolve
    mc "(Of course I’m staying to put sunscreen on her, wouldn’t miss it...)" with dissolve
    pause
    a "I’ll send him to you guys when he's done."
    mia "Alright."
    scene ch9_362- with dissolve
    mia "I want you in the water later."
    mc "Yeah, sure."
    pause
    scene ch9_362 with fade
    mc "[arelat!cl] [a], you don’t know what you just saved me from."
    mc "I would have had to walk around the beach with this thing in my pants."
    a "Oh! Haha."
    image ch9_363anim:
        "ch9_363" with dissolve
        1.75
        "ch9_364" with dissolve
        1.75
        repeat
    scene ch9_363anim with dissolve
    a "I saw that [mia] was trying to drag you a bit forcibly."
    mc "I would have died of embarrassment if she had seen me with this all hard."
    a "I can imagine, *giggle*."
    pause
    scene ch9_365 with dissolve
    a "Besides, I couldn’t let you go yet, you haven’t finished putting sunscreen on me. There are still a few places you missed."
    scene ch9_366 with dissolve
    mc "True, I didn’t cover your back completely."
    scene ch9_367 with dissolve
    mc "And I missed applying it behind your legs as well."
    scene ch9_367- with dissolve
    mc "Hmm..."
    scene ch9_370 with dissolve
    pause
    scene ch9_370- with dissolve
    pause
    image ch9_370anim:
        "ch9_370" with dissolve
        1.75
        "ch9_370-" with dissolve
        1.75
        repeat
    scene ch9_370anim with dissolve
    a "..."
    mc "(It’s great that she lets me do these things now.)"
    a "Honey, I think you covered that spot well with sunscreen before."
    mc "Oh, really? I don’t remember."
    mc "I’ll put more on just to be sure."
    a "Okay... *giggle*."
    pause
    scene ch9_371-- with dissolve
    a "[mc]..."
    scene ch9_371- with dissolve
    pause
    a "..."
    pause
    scene ch9_371-- with dissolve
    a "The girls are having fun."
    mc "(I thought she was going to tell me to stop...)" with dissolve
    mc "[mia] is teaching them how to surf."
    pause
    scene ch9_366- with dissolve
    pause
    scene ch9_367-- with dissolve
    pause
    scene ch9_367---- with dissolve
    mc "Hmm..."
    mc "[arelat!cl] [a]."
    a "Yes?"
    mc "You might also win the best ass on the beach award."
    a "What do you mean 'also'?"
    mc "You know, because you already have the award for the best breasts."
    a "[mc], what’s with you? *Giggle*."
    image ch9_365anim:
        "ch9_365" with dissolve
        1.75
        "ch9_366" with dissolve
        1.75
        "ch9_367" with dissolve
        1.75
        "ch9_367-" with dissolve
        1.75
        "ch9_366-" with dissolve
        1.75
        "ch9_367----" with dissolve
        1.75
        "ch9_367--" with dissolve
        1.75
        repeat
    scene ch9_365anim with dissolve
    mc "What? I really think so."
    a "It’s not that, I’m not used to you talking to me like that."
    a "Remember, I’m your [arelat]."
    mc "My very sensual and sexy [arelat]."
    a "[mc]..."
    pause
    scene ch9_370_ with dissolve
    pause
    scene ch9_369- with dissolve
    pause
    scene ch9_369 with dissolve
    pause
    scene ch9_369------ with dissolve
    pause
    scene ch9_369---- with dissolve
    pause
    scene ch9_369-- with dissolve
    pause
    image ch9_369-anim:
        "ch9_370_" with dissolve
        1.75
        "ch9_369-" with dissolve
        1.75
        "ch9_369" with dissolve
        1.75
        "ch9_369------" with dissolve
        1.75
        "ch9_369----" with dissolve
        1.75
        "ch9_369--" with dissolve
        1.75
        repeat
    scene ch9_369-anim with dissolve
    a "Aren’t you done there yet?"
    mc "I still have a few spots left."
    a "[mc], I know my ass is big, but not big enough for you to use up the whole bottle of sunscreen on it, *giggle*."
    mc "Wasn’t it a massage you wanted?"
    a "Hmm..."
    a "Yes, *giggle*."
    pause
    scene ch9_371 with dissolve
    a "I’m starting to get embarrassed, I want to cover up now."
    mc "Already giving up?"
    mc "You’re going to upset [k]."
    a "You’re not going to spill the beans, are you?"
    mc "I guess I am."
    a "You’re so nosy..."
    mc "You have to keep your promise, [arelat] [a]."
    a "Yes, I know."
    pause
    scene ch9_371- with dissolve
    pause
    a "I don’t understand [k]’s obsession with making me do these things."
    a "I’m talking about the bikini and all that."
    scene ch9_372 with dissolve
    pause
    scene ch9_372- with dissolve
    pause
    scene ch9_372-- with dissolve
    pause
    mc "(She’s become so permissive...)" with dissolve
    mc "(She’s letting me touch her in a public place.)" with dissolve
    mc "(Sure, no one can see us from here, but a few days ago I would have hesitated to even suggest it.)" with dissolve
    scene ch9_372--- with dissolve
    pause
    scene ch9_372---- with dissolve
    pause
    scene ch9_372----- with dissolve
    pause
    scene ch9_371- with dissolve
    a "Haha, look at [k], she just fell off the board."
    a "Now [s] is going to give it a try."
    mc "(I bet she’s paying close attention in case someone looks over here.)" with dissolve
    mc "(She doesn’t want anyone to see how her [arelatmc] is applying sunscreen all over her delicious ass.)"
    pause
    image ch9_372anim:
        "ch9_372" with dissolve
        1.75
        "ch9_372-" with dissolve
        1.75
        "ch9_372--" with dissolve
        1.75
        "ch9_372---" with dissolve
        1.75
        "ch9_372----" with dissolve
        1.75
        "ch9_372-----" with dissolve
        1.75
        repeat
    scene ch9_372anim with dissolve
    mc "(Ugh... I’ve had a hard-on for I don’t know how long...)" with dissolve
    mc "(The amount of pre-cum I must have in my shorts has to be impressive.)" with dissolve
    pause
    a "Yesterday [k] wanted me to go to dinner in a mini skirt, and now she want me to wear this bikini."
    pause
    mc "I think she wants to help you in her own way."
    mc "It seems like she’s giving you a self-esteem exercise."
    pause
    #
    scene ch9_368----- with dissolve
    a "I have self-esteem."
    scene ch9_368- with dissolve
    a "Another thing is that I’m a bit shy, but that’s part of my personality."
    scene ch9_368 with dissolve
    a "Although... well, it’s true that sometimes I wish I weren’t so much."  
    scene ch9_368--- with dissolve
    pause
    scene ch9_368---- with dissolve
    pause
    #
    image ch9_368anim:
        "ch9_368-----" with dissolve
        1.75
        "ch9_368-" with dissolve
        1.75
        "ch9_368" with dissolve
        1.75
        "ch9_368---" with dissolve
        1.75
        "ch9_368----" with dissolve
        1.75
        repeat
    scene ch9_368anim with dissolve
    pause
    mc "Maybe [k] has noticed it."
    mc "Sometimes we need someone to give us a push to dare to do things."
    mc "Those kinds of things that you’ve always wanted to do but are unsure about."
    pause
    a "Yeah... You’re right about that."
    pause
    scene ch9_371 with dissolve
    pause
    scene ch9_371- with dissolve
    pause
    scene ch9_371-- with dissolve
    pause
    a "I think you’re applying too much sunscreen, honey."
    a "Can you put on my legs too?"
    mc "It’ll be a pleasure."
    pause
    scene ch9_373 with dissolve
    a "From the calves."
    mc "Sure."
    pause
    scene ch9_374 with dissolve
    pause
    scene ch9_375 with dissolve
    pause
    scene ch9_376 with dissolve
    pause
    scene ch9_377 with dissolve
    mc "(My mouth is watering...)" with dissolve
    pause
    scene ch9_378 with dissolve
    pause
    mc "(I want to squeeze it with all my strength...)" with dissolve
    pause
    mc "(After letting me touch her all over, she won’t get mad about this... I hope.)" with dissolve
    scene ch9_379 with dissolve
    pause
    mc "(God...{w=0.5} The best part is that there’s no reaction, I’m sure she’s enjoying it as much as I am.)"
    pause
    scene ch9_379_ with dissolve
    pause
    scene ch9_379- with dissolve
    mc "(Little by little I’m getting to know her, not [a] in her [arelat] role, but the woman, the real [a].)" with dissolve
    pause
    scene ch9_380 with dissolve
    pause
    image ch9_379anim:
        "ch9_377" with dissolve
        1.0
        "ch9_378" with dissolve
        1.0
        "ch9_379" with dissolve
        1.75
        "ch9_379_" with dissolve
        1.0
        "ch9_379-" with dissolve
        1.0
        "ch9_380" with dissolve
        1.0
        repeat
    scene ch9_379anim with dissolve
    mc "(She likes to give me subtle signals to act accordingly...)" with dissolve
    mc "(She loves that I touch her 'without permission'.)" with dissolve
    mc "([a] seduces me in a way that no one ever has before, little by little...)" with dissolve
    mc "(Acting like she doesn’t want it, but making it clear that she does.)" with dissolve
    pause
    scene ch9_382- with dissolve
    pause
    scene ch9_382-- with dissolve
    a "Don’t squeeze too hard or you’ll burst them, honey, *giggle*."
    pause
    mc "(It's like pinching paradise...) " with dissolve
    pause
    mc "(I need to do it, I have to bury my face there...)" with dissolve
    mc "(I could really do it, no one is looking over here right now...)" with dissolve
    pause
    scene ch9_383 with dissolve
    a "[mc], what are you...?"
    mc "Hmm..."
    pause
    scene ch9_384 with dissolve
    a "[mc], what are you doing?"
    pause
    scene ch9_385 with dissolve
    a "[mc]?..."
    pause
    mc "Hmph..."
    scene ch9_386 with dissolve
    mc "(She’s been turning me on all this time, I just can’t help it.)" with dissolve
    mc "(I’d love to fast forward to being at home already.)" with dissolve
    mc "(In my room, hers, the living room, the patio, or anywhere, but I want to savor her whole body now.)" with dissolve
    pause
    a "O-okay, [mc], let’s stop for a moment."
    scene ch9_387 with dissolve
    mc "Sorry, I-I let my impulses get the better of me, hehe..."
    a "[mc], it’s not funny..."
    pause
    scene ch9_388- with dissolve
    a "Honey, have you gone crazy?"
    mc "Sorry, I..."
    a "We’re still at the beach [mc]."
    scene ch9_390 with dissolve
    mc "Yeah, I don’t know what I was thinking doing that."
    mc "Did it bother you?"
    a "It’s not about that, [mc]..."
    scene ch9_394 with dissolve
    a "..."
    pause
    scene ch9_390 with dissolve
    a "At least no one saw you, it would have been hard to explain."
    mc "Nah, it would be easy to explain."
    scene ch9_389 with dissolve
    a "And what would your explanation be?"
    mc "That I’m with my girlfriend."
    scene ch9_390 with dissolve
    a "Haha, [mc], what nonsense you’re talking about..."
    mc "There’s no reason not to believe me."
    a "But I look much older than you."
    mc "You don’t look much older than me, don’t exaggerate."
    scene ch9_389 with dissolve
    a "Would you say it wouldn’t look strange for a woman my age to date a guy like you?"
    mc "I couldn’t care less what others think."
    a "Yeah, I know you don’t care but..."
    mc "You care way too much about what people think of you, [arelat] [a]."
    scene ch9_390 with dissolve
    a "I guess so."
    a "I try to change that, but it’s difficult."
    pause
    mc "If you come into the water with me in a bikini, I’ll do the dishes for a week."
    scene ch9_389 with dissolve
    a "Enough with the challenges, please."
    mc "A month?"
    a "No, stop it already!"
    mc "Okay, okay..."
    scene ch9_390 with dissolve
    a "It’s already a lot that I agreed to be like this."
    mc "When someone fears success, there’s not much more to do..."
    a "I’m going to buy a decent swimsuit and you’ll see."
    mc "That wouldn’t be as fun."
    a "You can never keep people happy."
    pause
    scene ch9_393 with dissolve
    pause
    scene ch9_394 with dissolve
    pause
    scene ch9_391 with dissolve
    pause
    scene ch9_392 with dissolve
    pause
    a "And, um..."
    pause
    scene ch9_396 with dissolve
    a "Oh, honey..."
    a "It hasn’t gone down this whole time."
    mc "Hm?"
    pause
    scene ch9_397 with dissolve
    a "Your...{w=0.5} erection."
    mc "Ah, yes..."
    mc "I’ve been like this for a while, and it just won’t go away."
    pause
    scene ch9_392 with dissolve
    a "Sorry, honey, I-I didn’t notice."
    mc "Don’t worry, but why are you apologizing?"
    a "I don’t know, maybe..."
    pause
    scene ch9_398 with dissolve
    a "Maybe it’s because of me, could it be?"
    mc "You know it is."
    mc "Is it wrong?"
    a "Uhmm... uh, *giggle*."
    a "But well, it can't be helped, right?"
    mc "I’m afraid not, haha."
    pause
    scene ch9_399 with dissolve
    a "..."
    pause
    scene ch9_402 with dissolve
    a "Oh, [mc]... Look how hard you are..."
    a "It must be uncomfortable to have it like that for so long."
    pause
    scene ch9_400 with dissolve
    pause
    scene ch9_401 with dissolve
    a "It always gets so hard and big..."
    pause
    scene ch9_401- with dissolve
    pause
    scene ch9_403 with dissolve
    mc "{i}{size=-3}[arelat] [a], I really want to get home..."
    a "{i}{size=-3}I know, honey..."
    a "{i}{size=-3}But we’re going to have to wait a while for that."
    mc "{i}{size=-3}But I need it so badly..."
    scene ch9_402 with dissolve
    a "{i}{size=-3}I-I know, but I can’t help you to...{w=0.5} ''relieve'' this here."
    pause
    mc "{i}{size=-3}Maybe if you touch it a little..."
    a "{i}{size=-3}You want me to touch it?"
    mc "{i}{size=-3}Yes..."
    scene ch9_402 with dissolve
    pause
    a "{i}{size=-3}O-okay..."
    scene ch9_400 with dissolve
    pause
    scene ch9_401 with dissolve
    pause
    scene ch9_401- with dissolve
    pause
    image ch9_400anim:
        "ch9_400" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_400" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_400" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_400" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_400" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        "ch9_401-" with dissolve
        1.5
        "ch9_401" with dissolve
        1.5
        repeat
    scene ch9_400anim with dissolve
    a "{i}{size=-3}Does it feel good?"
    mc "Yes..."
    pause
    scene ch9_402 with dissolve
    a "{i}{size=-3}So hard and big..." with dissolve
    a "{i}{size=-3}How can you stay like this for so long?" with dissolve
    mc "{i}{size=-3}I don't know, I guess that's just how I am..." with dissolve
    a "{i}{size=-3}It was a rhetorical question, heh..." with dissolve
    pause
    scene ch9_400anim with dissolve
    a "{i}{size=-3}Does it still hurt?"
    mc "{i}{size=-3}A little, but it’s not too bad."
    mc "{i}{size=-3}Did I say it hurt?"
    a "{i}{size=-3}Eh, no..."
    pause
    scene ch9_401-- with dissolve
    pause
    scene ch9_401--- with dissolve
    pause
    image ch9_401--anim:
        "ch9_401--" with dissolve
        1.5
        "ch9_401---" with dissolve
        1.5
        repeat
    scene ch9_401--anim with dissolve
    a "{i}{size=-3}I figured that... since it's so, ''erect'', it would hurt."
    mc "{i}{size=-3}Well, yes, it does hurt a bit..."
    a "{i}{size=-3}..."
    pause
    a "{i}{size=-3}Still so rigid..."
    pause
    scene ch9_402 with dissolve
    pause
    mc "{i}{size=-3}[arelat!cl] [a]..."
    scene ch9_403 with dissolve
    a "{i}{size=-3}Tell me, honey."
    mc "{i}{size=-3}I’m dying to get home and kiss you..."
    a "{i}{size=-3}[mc]... Y-you really like my kisses don't you?"
    mc "{i}{size=-3}Yeah... Can I give you a kiss?"
    a "{i}{size=-3}Mmm..."
    pause
    a "{i}{size=-3}A quick kiss."
    scene ch9_404 with dissolve
    mc "{i}{size=-3}Let me take off your glasses..."
    scene ch9_405 with dissolve
    a "{i}{size=-3}On the cheek."
    mc "{i}{size=-3}No, on the lips."
    mc "{i}{size=-3}I love my beautiful [arelat] [a]'s lips..."
    scene ch9_406 with dissolve
    pause
    scene ch9_407 with dissolve
    play sound "audio/mouth/french_kiss_07.ogg"
    a "*Hmnch*..."
    pause
    scene ch9_408 with dissolve
    pause
    play sound "audio/mouth/french_kiss_06.ogg"
    scene ch9_409 with dissolve
    pause
    scene ch9_410 with dissolve
    a "[mc]!"
    mc "{i}{size=-3}Relax, we’re so far away that we’re barely visible from where the girls are."
    a "{i}{size=-3}Yes, but what about the people who are closer?"
    mc "{i}{size=-3}They don’t know us, and they’re not paying attention."
    mc "{i}{size=-3}[arelat!cl] [a], the world doesn’t revolve around us."
    scene ch9_411 with dissolve
    a "{i}{size=-3}Honey, can you and [k] stop giving me these weird tests of security and self-esteem for a minute, please?"
    mc "Haha, {i}{size=-3}But this isn’t a test."
    a "{i}{size=-3}Then what is it?"
    mc "{i}{size=-3}I just want to steal a few kisses from you."
    a "{i}{size=-3}Do you like the risk, huh?"
    mc "{i}{size=-3}I love it, and you?"
    a "{i}{size=-3}No, I don’t like risk at all."
    scene ch9_410 with dissolve
    pause
    scene ch9_409 with dissolve
    play sound "audio/mouth/french_kiss_05.ogg"
    pause
    scene ch9_407 with dissolve
    pause
    scene ch9_406 with dissolve
    pause
    scene ch9_411 with dissolve
    mc "{i}{size=-3}Oh... Why was that?"
    a "{i}{size=-3}Sometimes you need to add a little spice to life, right?"
    mc "Absolutely."
    pause
    scene ch9_406 with dissolve
    pause
    play music something fadein 0.5
    scene ch9_412 with dissolve
    a "Uh!"
    scene ch9_413 with vpunch
    d "Hahh! Nothing like a cold beer after swimming."
    a "{i}{size=-5}Get up, quickly!"
    scene ch9_415 with dissolve
    d "Come have a beer with your [drelat], son."
    mc "Uh..."
    a "We were just about to go into the water, dear."
    scene ch9_415- with dissolve
    d "Wait a second."
    a "Y-yes?"
    pause
    scene ch9_415--- with dissolve
    a "Eh?"
    d "The girls asked me to bring them the ball."
    pause
    scene ch9_415----
    a "A-ah! y-yes, of course."
    d "Thanks, love."
    $ renpy.end_replay()
    pause
    stop music fadeout 2.0
    stop background fadeout 2.0
    scene blackscreen with dissolve
    pause
    play background "audio/beachsfx.ogg" fadein 1.5 loop
    play music scene1 fadein 1.5
    jump ch9_415beach

label ch9_415beach:
    scene ch9_415-1 with dissolve
    a "There it goes!"
    k "Thanks, [arelatks]."
    scene ch9_415-2 with dissolve
    k "In the end, you dared to go into the sea, congratulations, [arelatks]!"
    a "Eh?"
    a "Oh, yes, I couldn’t resist, hehe."
    pause
    scene ch9_415-3 with dissolve
    mc "Hey, is it true you were embarrassed?"
    a "Embarrassed about what?"
    scene ch9_415-4 with dissolve
    mc "About being seen in this bikini, since it’s a bit tight and all that."
    a "Ah, haha."
    scene ch9_415-3 with dissolve
    mc "What made you change your mind so quickly?"
    a "Well, I realized that the only person who really cares about how I look in this bikini is me."
    a "So I decided to stop worrying and just enjoy the day."
    scene ch9_415-5 with dissolve
    a "Because a beautiful woman like me shouldn’t be embarrassed to show off her body."
    mc "A-ha..."
    mc "I’m sure it has nothing to do with how nervous you got when [drelat] [d] appeared behind you..."
    scene ch9_415-6
    a "Haha, you should be happy that I made progress."
    mc "Nah, it wasn’t by choice."
    a "You just want to avoid the month of washing dishes you promised."
    mc "You know you cheated, right?"
    a "I don’t remember us setting any conditions."
    a "Look, just because I’m nice, I’ll reduce it to one week."
    mc "Yay..."
    mc "Hey, but you didn’t even agree to the deal!"
    a "I did!"
    mc "Yeah, sure... Anyway, I’ll do it."
    a "Aww, that’s why I love you so much."
    mc "I know."
    "Haha!"
label ch9a3:
    if _in_replay:
        show screen Replayexit
        play music scene2 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_415-8 with dissolve
    pause
    mc "{i}{size=-3}When [drelat] [d] arrived, you got up so quickly and looked super nervous."
    a "{i}{size=-3}I got scared, I didn’t expect him to arrive so suddenly."
    mc "{i}{size=-3}If we had come to the water earlier, this wouldn’t have happened."
    scene ch9_415-7 with dissolve
    a "{i}{size=-3}Yeah, yeah, it would have been much better if they had seen you walking with that thing you have there..."
    a "{i}{size=-3}We were lucky that no one saw you coming here."
    mc "{i}{size=-3}Well, you’re right about that."
    a "{i}{size=-3}And... did the cold water help calm that down?"
    scene ch9_415-8 with dissolve
    mc "{i}{size=-3}No, not at all."
    scene ch9_415-9 with dissolve
    mc "{i}{size=-3}Still hard and big..."
    a "{i}{size=-3}Oh, dear... {w=0.5}We should get that checked, it’s not normal for you to get like that so easily..."
    pause
    scene ch9_415-10 with dissolve
    a "{i}{size=-3}[mc]..."
    pause
    scene ch9_415-7 with dissolve
    pause
    scene ch9_415-7- with dissolve
    pause
    scene ch9_415-7-- with dissolve
    pause
    scene ch9_415-7--- with dissolve
    a "..."
    pause
    scene ch9_415-7-- with dissolve
    pause
    scene ch9_415-11 with dissolve
    a "{i}{size=-3}The girls are just centimeters away from us!"
    pause
    scene ch9_415-9 with dissolve
    a "{i}{size=-3}Honey, you’re hopeless..."
    scene ch9_415-8 with dissolve
    mc "{i}{size=-3}Remember about spicing up life."
    a "{i}{size=-3}I think we’re going overboard with the spice."
    k "[mc], [arelatks], do you want to play a volleyball match or are you scared?"
    scene ch9_415-12 with dissolve
    k "You two against us."
    a "Y-yes, sure."
    k "The winner gets [arelatks]’s bikini!"
    mia "I want it! Haha."
    scene blackscreen with dissolve
    pause
    show ch9_415-15 with dissolve:
        subpixel True
        xalign 0.5 yalign 1.0 zoom 0.5
        ease 3 yalign 0.0
    $ renpy.pause(2.65, hard=True)
    show ch9_415-15:
        subpixel True
        xalign 0.5 zoom 0.5 yalign 0.0
        ease 3 zoom 1.5 yalign 0.425
    $ renpy.pause(2.65, hard=True)
    mc "(Look at how those big boobs bounce...)" with dissolve
    pause
    show ch9_415-15:
        subpixel True
        xalign 0.5 zoom 1.5 yalign 0.425
        ease 3 zoom 0.5 yalign 0.25
    $ renpy.pause(2.65, hard=True)
    s "Here, I want to play too!"
    pause
    show ch9_415-16 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 0.5
        ease 3 yalign 0.0
    $ renpy.pause(2.65, hard=True)
    show ch9_415-16:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 0.5
        ease 3 yalign 0.4 zoom 1.5
    $ renpy.pause(2.65, hard=True)
    mc "([k] also has some exquisite big tits...)" with dissolve
    pause
    show ch9_415-16:
        subpixel True
        xalign 0.5 yalign 0.4 zoom 1.5
        ease 3 yalign 0.2 zoom 0.5
    pause
    show ch9_415-14 with dissolve:
        subpixel True
        xalign 0.5 zoom 1.0 yalign 1.0
        ease 3 zoom 1.0 yalign 0.0
    $ renpy.pause(2.65, hard=True)
    show ch9_415-14:
        subpixel True
        xalign 0.5 zoom 1.0 yalign 0.0
        ease 3 zoom 1.5 yalign 0.45
    $ renpy.pause(2.65, hard=True)
    mc "([mia] isn't bad either, she has small but playful tits...)" with dissolve
    mia "Here you go, [s]!"
    scene ch9_415-13 with dissolve
    a "That's it, that's how you do it!"
    mc "(I still have this enormous erection that won't go away...)" with dissolve
    pause
    scene ch9_415-17 with dissolve
    mc "(Damn... I even feel like going off to hide by myself so I can jerk off...)"
    mc "(I'm still very aroused, I need to do something...)"
    pause
    scene ch9_415-18 with dissolve
    d "Are the teams ready? Who of you needs a volleyball expert?"
    k "Hey, [drelatks] is here, we can play three against three."
    d "[a], [mc], and I against you three."
    k "Hmm, it feels a bit unfair if the two worst players are on [arelatks]'s team."
    scene ch9_415-19 with dissolve
    d "What are you saying? I'm great and I'm sure [mc] is too."
    k "The first team to reach 10 points wins!"
    pause
    scene ch9_415-20 with fade
    mc "![drelat!cl] [d]!" 
    scene ch9_415-21 with hpunch
    d "It's yours, [a]!"
    scene ch9_415-22 with dissolve
    a "Watch out!"
    play sound "audio/splashw.mp3" volume 0.3
    scene ch9_415-23 with vpunch
    mc "Oof!"
    scene ch9_415-25 with vpunch
    mia "Damn!"
    d "Point for us, hahaha!"
    scene ch9_415-24 with dissolve
    mc "That's it, [arelat] [a]!"
    a "Ah! Haha."
    scene ch9_415-26 with dissolve
    mc "Well done, [arelat] [a], you're the best!"
    a "Aww, haha!"
    a "It's the first ball I've touched, haha."
    mc "And it's the first point we've scored too, haha!"
    scene ch9_415-27 with dissolve
    mc "That makes you the best on our team."
    d "Well done, love!"
    a "If you say so... haha."
    scene ch9_415-28 with dissolve
    d "High five, my love!"
    d "We definitely have the best player on our team, hehe."
    scene ch9_415-29 with dissolve
    d "Hehehe, come here, love!"
    scene ch9_415-30 with dissolve
    a "I'm not even that good, don't exaggerate, hah..."
    d "Eh..."
    scene ch9_415-31 with dissolve
    d "Uh..."
    pause
    k "I don't know why you're celebrating if the score is nine to one in our favor."
    scene ch9_415-32 with dissolve
    s "Yes, and it's just the first point."
    mia "Nice shot, Mrs. [a]."
    k "Yeah, good save."
    a "Thanks, girls."
    d "Alright, I'll play seriously if that's what you want."
    k "Are you going to say you were holding back?"
    d "We'll serve now, and you'll see what a real game is like, young lady."
    k "You know what? Let's restart the game, we'll see what the score is when you play ''seriously''."
    scene ch9_415-33 with dissolve
    d "Now I'll be in the front, you two stay behind me."
    k "We'll serve."
    scene ch9_415-34 with dissolve
    pause
    mc "(Damn, it's like her juicy ass is staring back at me...)" with dissolve
    mc "..."
    pause
    scene ch9_415-35 with dissolve
    pause
    d "Haha, point!"
    scene ch9_415-34-- with dissolve
    k "You can't spike!"
    s "Yeah, [drelatks] is cheating!"
    scene ch9_415-34--- with dissolve
    a "{i}{size=-3}Uh?"
    d "That was legal."
    k "Then this is legal too!"
    scene ch9_415-34--- with dissolve
    pause
    scene ch9_415-34---- with dissolve
    a "{i}{size=-3}[mc], what are you...?" 
    pause
    scene ch9_415-34-1 with dissolve
    a "{i}{size=-3}No, [mc]..." 
    scene ch9_415-34-2 with dissolve
    a "{i}{size=-3}[mc], they’re going to see you." 
    mc "{i}{size=-3}They’re focused on the game." 
    scene ch9_415-36 with dissolve
    a "{i}{size=-3}Yes but...." 
    pause
    scene ch9_415-37 with dissolve
    pause
    scene ch9_415-38 with dissolve
    pause
    scene ch9_415-39 with dissolve
    pause
    scene ch9_415-40 with dissolve
    pause
    scene ch9_415-41 with dissolve
    pause
    scene ch9_415-42 with dissolve
    a "{i}{size=-3}No, honey, stop."
    pause
    scene ch9_415-35 with dissolve
    pause
    mc "(Damn, I can't resist...)" with dissolve
    image ch9_415-36anim:
        "ch9_415-38" with dissolve
        1.5
        "ch9_415-37" with dissolve
        1.5
        "ch9_415-38" with dissolve
        1.5
        "ch9_415-39" with dissolve
        1.5
        "ch9_415-40" with dissolve
        1.5
        "ch9_415-39" with dissolve
        1.5
        "ch9_415-41" with dissolve
        1.5
        repeat
    scene ch9_415-36anim with dissolve
    pause
    a "{i}{size=-3}[mc]..."
    pause    
    scene ch9_415-34-2 with dissolve
    a "{i}{size=-3}[mc], listen to me-"
    mc "{i}{size=-3}No one is watching us."
    pause
    scene ch9_415-44 with dissolve
    pause
    scene ch9_415-43 with dissolve
    mc "(Her ass feels amazing on my hand...)"
    pause
    scene ch9_415-44 with dissolve
    pause
    scene ch9_415-45 with dissolve
    pause
    scene ch9_415-46 with dissolve

    pause
    scene ch9_415-45 with dissolve
    pause
    scene ch9_415-47 with dissolve
    pause
    image ch9_415-44anim:
        "ch9_415-44" with dissolve
        1.5
        "ch9_415-43" with dissolve
        1.5
        "ch9_415-44" with dissolve
        1.5
        "ch9_415-45" with dissolve
        1.5
        "ch9_415-46" with dissolve
        1.5
        "ch9_415-45" with dissolve
        1.5
        "ch9_415-47" with dissolve
        1.5
        repeat
    scene ch9_415-44anim with dissolve
    pause
    mc "([drelat!cl] [d] is right in front of us, and I'm squeezing and massaging his wife's ass...)"
    d "Ha ha! I told you, when I get serious, things change."
    k "Pure luck."
    s "Hey, are just the two of you going to play or what?"
    d "Did this get personal, huh?"
    k "Stop talking and serve."
    pause
    scene ch9_415-50 with dissolve
    pause
    scene ch9_415-49 with dissolve
    pause
    scene ch9_415-50 with dissolve
    pause
    scene ch9_415-51 with dissolve
    pause
    scene ch9_415-52 with dissolve
    pause
    scene ch9_415-51 with dissolve
    pause
    scene ch9_415-53 with dissolve
    pause
    image ch9_415-50anim:
        "ch9_415-50" with dissolve
        1.5
        "ch9_415-49" with dissolve
        1.5
        "ch9_415-50" with dissolve
        1.5
        "ch9_415-51" with dissolve
        1.5
        "ch9_415-52" with dissolve
        1.5
        "ch9_415-51" with dissolve
        1.5
        "ch9_415-53" with dissolve
        1.5
        repeat
    scene ch9_415-50anim with dissolve
    mc "(My cock is throbbing like crazy...)"
    mc "(I want to jerk off so bad, but I'm afraid someone will see me.)"
    mc "(Damit!)"
    pause
    k "A-ha!"
    d "It went out of bounds."
    k "What are you talking about? It was a point!"
    d "Let's ask [a]."
    k "[arelatks!cl]?"
    a "Huh? N-no, I don't know."
    k "It was a point!"
    d "Alright, alright, five to five."
    k "Cheater."
    d "Yeah, yeah, just serve already."
    pause
    scene ch9_415-42 with dissolve
    a "{i}{size=-3}Enough, [mc]."
    pause
    scene ch9_415-35 with dissolve 
    pause
    scene ch9_415-54 with dissolve
    pause
    scene ch9_415-55 with dissolve
    a "{i}{size=-3}[mc], what are you doing? Stop it!"
    mc "{i}{size=-3}Just a little more..."
    pause
    scene ch9_415-56 with dissolve
    pause
    mc "(Uuh... this feels good.)" with dissolve
    a "{i}{size=-3}[mc]!"
    scene ch9_415-58 with dissolve
    a "{i}{size=-3}Are you out of your mind?" 
    image ch9_415-59anim:
        "ch9_415-59" with dissolve
        1.5
        "ch9_415-58" with dissolve
        1.5
        repeat
    scene ch9_415-59anim with dissolve
    a "{i}{size=-3}[mc]..."
    stop music fadeout 1.5
    pause
init python:
    def ch9_415agb_(trans, st, at):  
        trans.set_child("ch9_415agb_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agb1_(trans, st, at):  
        trans.set_child("ch9_415agb1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    def ch9_415agb2_(trans, st, at):  
        trans.set_child("ch9_415agb2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  
init python:
    def ch9_415agb3_(trans, st, at):  
        trans.set_child("ch9_415agb3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agb4_(trans, st, at):  
        trans.set_child("ch9_415agb4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agb5_(trans, st, at):  
        trans.set_child("ch9_415agb5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agb6_(trans, st, at):  
        trans.set_child("ch9_415agb6_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agb7_(trans, st, at):  
        trans.set_child("ch9_415agb7_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_415agb_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_415agb1") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_415agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9contagb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_415agb1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch9_415agb") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_415agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9contagb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_415agb2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch9_415agb") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch9_415agb1") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9contagb") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

####################
####################

screen ch9_415agb3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0085) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_415agb4") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_415agb5") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_415agb6") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agb7") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_415agb4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0085) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agb3") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_415agb5") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_415agb6") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agb7") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_415agb5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0085) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agb3") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_415agb4") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_415agb6") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agb7") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_415agb6_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0085) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agb3") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_415agb4") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_415agb5") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agb7") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch9_415agb7_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0085) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agb3") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_415agb4") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_415agb5") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch9_415agb6") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9agb2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
label afteranimch9_415agb:
    image ch9_415agb:
        function ch9_415agb_
    image ch9_415agb1:
        function ch9_415agb1_
    image ch9_415agb2:
        function ch9_415agb2_
    image ch9_415agb3:
        function ch9_415agb3_
    image ch9_415agb4:
        function ch9_415agb4_
    image ch9_415agb5:
        function ch9_415agb5_
    image ch9_415agb6:
        function ch9_415agb6_
    image ch9_415agb7:
        function ch9_415agb7_
    $ anim_speed = 0.05
    play music sexy2 fadein 1.5
    scene ch9_415agb with dissolve
    pause
    a "..."
    pause
    a "{i}{size=-3}No, [mc]..."
    mc "{i}{size=-3}They're so focused on the game that they don't even pass us the ball anymore."
    pause
    $ anim_speed = 0.03
    scene ch9_415agb1 with dissolve
    pause
    a "{i}{size=-3}T-this is too much..."
    scene ch9_415agb2 with dissolve
    pause
    a "{i}{size=-3}Try not to be too obvious..."
    mc "{i}{size=-3}Don't worry, I'm keeping an eye out in case they look over."
    call screen ch9_415agb2_ with dissolve
label ch9_415agb:
    scene ch9_415agb with dissolve
    call screen ch9_415agb_ with dissolve
label ch9_415agb1:
    scene ch9_415agb1 with dissolve
    call screen ch9_415agb1_ with dissolve
label ch9_415agb2:
    scene ch9_415agb2 with dissolve
    call screen ch9_415agb2_ with dissolve   
    
label ch9contagb:
    $ anim_speed = 0.025
    scene ch9_415-59anim with dissolve
    a "{i}{size=-3}Honey, we need to stop now."
    mc "{i}{size=-3}Just a little bit more."
    a "{i}{size=-3}God, [mc]..."
    pause
    scene ch9_415-56 with dissolve
    pause
    scene ch9_415-55 with dissolve
    pause
    scene ch9_415-59- with dissolve
    a "{i}{size=-3}A-are you satisfied now?"
    pause
    scene ch9_415-59anim with dissolve
    a "{i}{size=-3}D-did you take it out of your...?"
    mc "{i}{size=-3}Yeah, it just... feels much better this way."
    a "..."
    pause
    scene ch9_415agb3 with dissolve
    pause
    a "{i}{size=-3}Hurry up, honey."
    mc "{i}{size=-3}J-just a little more..."
    a "{i}{size=-3}..."
    scene ch9_415agb4 with dissolve 
    pause
    a "{i}{size=-3}Don't move so fast, you'll draw attention..."
    mc "{i}{size=-3}They don't even notice us."
    scene ch9_415agb5 with dissolve
    a "{i}{size=-3}You are moving fast, [mc]."
    mc "{i}{size=-3}Hmmm, I can't help it..."
    mc "{i}{size=-3}M-my body just moves on its own..."
    pause
    a "{i}{size=-3}H-hurry up, honey, please."
    mc "{i}{size=-3}I’m{w=0.5}, mngh, I’m almost..."
    pause
    scene ch9_415agb6 with dissolve
    pause
    mc "{i}{size=-3}You can move your hips a little..."
    a "{i}{size=-3}M-my hips?"
    mc "{i}{size=-3}It would help me finish faster."
    a "{i}{size=-3}[mc], you said you were almost done..."
    pause
    a "{i}{size=-3}L-like this?"
    mc "{i}{size=-3}Hmm... yes."


    a "{i}{size=-3}[mc], we have to do it here and now?"
    call screen ch9_415agb6_ with dissolve

label ch9_415agb3:
    $ update_scene_name("ch9_415agb3")
    scene ch9_415agb3 with dissolve
    call screen ch9_415agb3_ with dissolve
label ch9_415agb4:
    $ update_scene_name("ch9_415agb4")
    scene ch9_415agb4 with dissolve
    call screen ch9_415agb4_ with dissolve
label ch9_415agb5:
    $ update_scene_name("ch9_415agb5")
    scene ch9_415agb5 with dissolve
    call screen ch9_415agb5_ with dissolve 
label ch9_415agb6:
    $ update_scene_name("ch9_415agb6")
    scene ch9_415agb6 with dissolve
    call screen ch9_415agb6_ with dissolve 
label ch9_415agb7:
    $ update_scene_name("ch9_415agb7")
    scene ch9_415agb7 with dissolve
    call screen ch9_415agb7_ with dissolve 
label afterch9agb2:
    $ anim_speed = 0.005
    a "{i}{size=-3}Don't do it so fast or they'll notice, [mc]."
    pause
    jump ch9qbls
default current_scene = ""

init python:
    def update_scene_name(scene_name):
        global current_scene
        current_scene = scene_name

label ch9qbls:
    if current_scene != "ch9_415agb3":
        scene ch9_415agb3 with dissolve
    a "{i}{size=-3}[mc], slow down!"
    mc "{i}{size=-3}Hmm, ngh!"
    mc "(I can't stop, my hips are moving on their own.)" with dissolve
    a "{i}{size=-3}H-honey..."
    pause
    scene ch9_415-60 with hpunch
    a "{i}![mc]!"
    d "There it goes!"
    scene ch9_415-61 with dissolve
    d "Haha, point!"
    s "It's so boring that only [drelatks] and [k] are playing."
    pause
    scene ch9_415-62 with dissolve
    pause
    mc "{i}{size=-3}[arelat!cl] [a], I'm too aroused..."
    a "{i}{size=-3}Yes..."
    a "{i}{size=-3}I-I can tell..."
    pause
    scene ch9_415-62-1 with dissolve
    mc "{i}{size=-3}What beauties..."
    pause
    scene ch9_415-65 with dissolve
    mc "{i}{size=-3}Can I touch your breasts?"
    a "{i}{size=-3}[mc], for god's sake..."
    mc "{i}{size=-3}Just a little. If they didn't notice what happened before, they definitely won't notice this."
    a "{i}{size=-3}... {w=0.5}Be discreet..."
    scene ch9_415-62-1 with dissolve
    pause
    scene ch9_415-62-2 with dissolve
    mc "Hmm..."
    pause
    scene ch9_415-62-1 with dissolve
    pause
    scene ch9_415-62-2 with dissolve
    d "I won, hahaha! I mean, we won!"
    scene ch9_415-63 with vpunch
    pause 0.5
    scene ch9_415-64 with dissolve
    a "G-good job, dear!"
    d "Haha, you did great too."
    mc "W-we were just watching, hehe..."
    k "Rematch!"
    scene ch9_415-65- with dissolve
    d "Do you want to lose again? Are you sure?"
    k "We were nine to ten, don't act like it was easy."
    d "Alright, alright, one more."
    s "So boring..."
    mia "Do you want to go play with the boogie?"
    s "Yes, let's go!"
    scene ch9_415-65 with dissolve
    a "{i}{size=-3}Oh my god, [mc]..."
    mc "{i}{size=-3}That was close."
    a "{i}{size=-3}I told you."
    scene ch9_415-63- with dissolve
    pause
    scene ch9_415-65- with dissolve
    a "{i}{size=-3}[mc]..."
    mc "{i}{size=-3}They've started playing again."
    scene ch9_415-63- with dissolve
    pause
    scene ch9_415-63-- with dissolve
    mc "{i}{size=-3}What a treat..."
    pause
    scene ch9_415-63---- with dissolve
    pause
    image ch9_415-63anim:
        "ch9_415-63--" with dissolve
        1.75
        "ch9_415-63----" with dissolve
        1.75
        repeat
    scene ch9_415-63anim with dissolve
    pause
    scene ch9_415-63----- with dissolve
    pause
    a "{i}{size=-3}S-stop it, [mc]..."
    mc "{i}{size=-3}Let's move away a bit."
    scene ch9_415-66 with dissolve
    a "{i}{size=-3}[mc]!"
    pause
    scene ch9_415-73 with dissolve
    a "{i}{size=-3}[mc], I'm not liking this anymore."
    a "{i}{size=-3}Y-you're losing control."
    scene ch9_415-71 with dissolve
    a "{i}{size=-3}H-honey, I know how aroused you are but..."
    pause
    scene ch9_415-67 with dissolve
    pause
    scene ch9_415-68 with dissolve
    pause
    scene ch9_415-68- with dissolve
    a "{i}{size=-3}Oh..."
    mc "{i}{size=-3}I'll just rub like before."
    scene ch9_415agf3_1 with dissolve
    a "{i}{size=-3}Honey..."
    pause
    a "{i}{size=-3}R-remember to be discreet, okay?"
    jump afterch9_415agf_
init python:
    def ch9_415agf_(trans, st, at):  
        trans.set_child("ch9_415agf_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agf2_(trans, st, at):  
        trans.set_child("ch9_415agf2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agf3_(trans, st, at):  
        trans.set_child("ch9_415agf3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agf4_(trans, st, at):  
        trans.set_child("ch9_415agf4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_415agf5_(trans, st, at):  
        trans.set_child("ch9_415agf5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

screen ch9_415agf_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_415agf2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_415agf3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_415agf4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_415agfscreen") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch9_415agf2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agf_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_415agf3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_415agf4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_415agfscreen") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch9_415agf3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agf_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_415agf2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_415agf4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_415agfscreen") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch9_415agf4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agf_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_415agf2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_415agf3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_415agf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_415agfscreen") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_415agf5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.035) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_415agf_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_415agf2_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_415agf3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch9_415agf4_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_415agfscreen") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
label afterch9_415agf_:
    image ch9_415agf_:
        function ch9_415agf_
    image ch9_415agf2_:
        function ch9_415agf2_
    image ch9_415agf3_:
        function ch9_415agf3_
    image ch9_415agf4_:
        function ch9_415agf4_
    image ch9_415agf5_:
        function ch9_415agf5_
    $ anim_speed = 0.02
    scene ch9_415agf3_ with dissolve
    pause
    a "{i}{size=-3}I can't help but think about what would happen if they saw us..."
    mc "{i}{size=-3}I'm just giving my [arelat] a hug."
    a "{i}{size=-3}No [arelatmc] hugs their [arelat] like this."
    scene ch9_415agf2_ with dissolve
    mc "{i}{size=-3}Well, I do."
    mc "{i}{size=-3}Hmm, hmng. And I love it."
    a "{i}{size=-5}Uhm, hmm..."
    pause
    image ch9_415-73anim:
        "ch9_415-73" with dissolve
        1
        "ch9_415-74" with dissolve
        1
        repeat
    image ch9_415-71anim:
        "ch9_415-71" with dissolve
        1
        "ch9_415-72" with dissolve
        1
        repeat
    scene ch9_415-73anim with dissolve
    mc "{i}{size=-3}Are you enjoying it too?"
    a "{i}{size=-3}What a question, [mc]..."
    pause
    mc "{i}{size=-3}I feel like I'm forcing you to do this, and I don't like it."
    scene ch9_415-71anim with dissolve
    a "{i}{size=-3}No... no, this..."
    pause
    a "{i}{size=-3}I know you've had that erection for a long time, and it's my fault."
    a "{i}{size=-3}I want to make you feel good."
    pause
    mc "{i}{size=-3}No."
    a "{i}{size=-3}No?"
    mc "{i}{size=-3}I want you to enjoy it too."
    a "..."
    pause
    scene ch9_415agf4_ with dissolve
    mc "{i}{size=-3} Hmm, hmm..."
    pause
    mc "{i}{size=-3}I don't like that you feel like you have to do these things for me."
    a "{i}{size=-3}N-no, it's not like that, [mc]."
    pause
    scene ch9_415agf5_ with dissolve
    mc "{i}{size=-3}Then?"
    pause
    a "{i}{size=-3}Yes, I-I do like it..."
    mc "{i}{size=-3}Really?"
    a "{i}{size=-3}I-I like that you find me so attractive."
    pause
    scene ch9_415agf_ with dissolve
    a "{i}{size=-3}Uhm, hmm. It's just that..."
    a "{i}{size=-3}This situation makes me uncomfortable, the girls and [d] are just right there."
    pause
    a "{i}{size=-3}Are you close?"
    mc "{i}{size=-3}Yes{w=0.5}, *hmm*{w=0.5}, I can feel it."
    a "{i}{size=-3}N-now that we're a bit further away...{w=0.5} you can go a little faster if you want."
    mc "{i}{size=-3}Really?"
    a "{i}{size=-3}Yes, but you know, be discreet."
    $ anim_speed = 0.008
    $ renpy.pause(1.0, hard=True)
    a "Uhmm..."
    a "{i}{size=-3}Hmm... hmm..."
    pause
    mc "{i}{size=-3}*Hmm* Do you want me to go slower?"
    a "{i}{size=-3}*Hmm, hmm...*"
    a "{i}{size=-3}*Uhm.. uh...* N-no, they're still playing, they're not watching us."
    call screen ch9_415agf_ with dissolve
    pause
label ch9_415agf_:
    scene ch9_415agf_ with dissolve
    call screen ch9_415agf_ with dissolve
label ch9_415agf2_:
    scene ch9_415agf2_ with dissolve
    call screen ch9_415agf2_ with dissolve
label ch9_415agf3_:
    scene ch9_415agf3_ with dissolve
    call screen ch9_415agf3_ with dissolve
label ch9_415agf4_:
    scene ch9_415agf4_ with dissolve
    call screen ch9_415agf4_ with dissolve
label ch9_415agf5_:
    scene ch9_415agf5_ with dissolve
    call screen ch9_415agf5_ with dissolve

label afterch9_415agfscreen:
    image ch9_415-71animfast:
        "ch9_415-71" with Dissolve(0.2)
        0.5
        "ch9_415-72" with Dissolve(0.2)
        0.5
        repeat
    image ch9_415-73animfast:
        "ch9_415-73" with Dissolve(0.5)
        0.5
        "ch9_415-74" with Dissolve(0.5)
        0.5
        repeat
    mc "*A-ah, hmmngh*."
    a "{i}{size=-3}That's it, let it out, honey."
    mc "¡Hmmngh!"
    pause
    scene ch9_415agf_ with dissolve
    pause 1
    $ anim_speed = 0.006
    mc "¡Hmnghhh!"
    pause
    k "¡No!"
    d "¡Hahaha, nine to nine!"
    scene ch9_415-71animfast with dissolve
    a "{i}{size=-3}[mc], hurry up."
    mc "{i}{size=-3}*¡Hmngh!*..."
    k "Hey, that went too far, it doesn't count."
    d "If you touch it before it goes out the limits, of course it counts."
    k "You're such a cheater, [drelatks]."
    d "Last point, and it's my serve, hahaha!"
    k "[arelatks!cl]!"
    scene ch9_415-73animfast with dissolve
    a "Yes?"
    a "{i}{size=-3}Let me go, [mc]!"
    a "Yes, honey?"
    k "Can you do-...?"
    k "What are you guys doing?"
    scene ch9_415-77 with vpunch
    a "Erm... w-we're swimming."
    scene ch9_415-80 with dissolve
    pause
    scene ch9_415-78 with dissolve
    a "{i}{size=-3}H-hide it well."
    mc "{i}{size=-3}Yes."
    scene ch9_415-79 with dissolve
    k "Can you be the referee for a bit?"
    scene ch9_415-77 with dissolve
    a "R-referee?"
    k "Yeah, to make sure everything's legal, you know how [drelatks] is."
    d "All the points I scored were legal, stop making excuses."
    scene ch9_415-81 with dissolve
    a "N-no, uh..."
    a "I have to go to the car for something."
    k "[mc], you be the referee."
    scene ch9_415-82 with dissolve
    a "He...{w=0.5} he can't either, I need his help."
    d "Do you need more help? I can go too, love."
    a "No! {w=0.5}No need, dear."
    a "Let's go, [mc]."
    $ renpy.end_replay()
    stop music fadeout 1.5
    stop background fadeout 3.0
    scene blackscreen with dissolve
    pause
label ch9a4:
    if _in_replay:
        show screen Replayexit
    play music scene2 fadein 3.0
    play background "audio/beachsfx.ogg" fadein 2.0 loop volume 0.5
    scene ch9_416 with Dissolve(2.0)
    mc "It’s not that noticeable, is it?"
    a "Don’t worry, no one here can see you anymore."
    scene ch9_417 with dissolve
    pause
    mc "So, why are we here?"
    a "For underwear."
    a "[d] asked me to pack him an extra pair of boxers, they should fit you."
    scene ch9_419 with dissolve
    mc "Why do you want me to wear [drelat] [d]’s boxers?"
    a "So they can hide or at least tone down your little 'problem,' *giggles*."
    mc "Ah, I get it now."
    mc "But I don’t mind being seen, though."
    a "Don’t tell me you’re one of those weird pervs."
    scene ch9_417 with dissolve
    mc "I’m just proud of my body, that’s all."
    a "Next thing I know, I’ll see you on the twelve o'clock news: 'Perv terrorizes beachgoers.'"
    mc "'Alongside a woman with voluptuous hips in a wickedly tight bikini.'"
    a "Shh, stop it! *giggles*"
    mc "You know I’m joking, you look good."
    a "Well, let's see if we can find them."
    scene ch9_418--- with dissolve
    mc "[arelat!cl] [a], I was thinking..."
    pause
    scene ch9_419 with dissolve
    a "Yes?"
    mc "Earlier, when we were in the water, I couldn’t kiss you because [drelat] [d] and [k] were there."
    mc "And since we’re alone now..."
    pause
    stop music fadeout 3.0
    scene ch9_419- with dissolve
    pause
    scene ch9_419-- with dissolve
    pause
    scene ch9_419--- with dissolve
    a "Okay."
    play music sexy2 fadein 1.5
    play sound kissing loop volume 0.2
    scene ch9_420 with dissolve
    pause
    scene ch9_420- with dissolve
    a "Hmm, hmnch"
    image ch9_419anim:
        "ch9_420" with dissolve
        1.5
        "ch9_420-" with dissolve
        1.5
        repeat
    scene ch9_419anim with dissolve
    mc "(I know we've been kissing and touching for days now, but it still feels so surreal...)" with dissolve
    pause
    scene ch9_418--- with dissolve
    pause
    scene ch9_418 with dissolve
    pause
    image ch9_418---anim:
        "ch9_418---" with dissolve
        1.5
        "ch9_418" with dissolve
        1.5
        repeat
    scene ch9_418---anim with dissolve
    pause
    scene ch9_421 with dissolve
    a "*Hmmnch, smnch*"
    pause
    scene ch9_419anim with dissolve
    pause
    scene ch9_423 with dissolve
    mc "(We’re kissing... [arelat!cl] and [arelatmc], shamelessly, under the sun...)" with dissolve
    pause
    scene ch9_422 with dissolve
    mc "(It’s like the world stopped just for us.)" with dissolve
    pause
    scene ch9_424--- with dissolve
    a "*Hmnch, hmm*"
    pause
    scene ch9_424-- with dissolve
    pause
    scene ch9_424 with dissolve
    a "*Smnch, hmmnch*"
    pause
    scene ch9_425 with dissolve
    a "*Ahlm, mnch*"
    pause
    scene ch9_426 with dissolve
    a "*Lhmnch, lmhmm*"
    pause
    image ch9_424anim:
        "ch9_424---" with dissolve
        1.25
        "ch9_424--" with dissolve
        1.25
        "ch9_424" with dissolve
        1.25
        "ch9_425" with dissolve
        1.25
        "ch9_426" with dissolve
        1.25
        #
        "ch9_424---" with dissolve
        1.25
        "ch9_425" with dissolve
        1.25
        "ch9_424" with dissolve
        1.25
        "ch9_426" with dissolve
        1.25
        "ch9_424---" with dissolve
        1.25
        #
        "ch9_425" with dissolve
        1.25
        "ch9_426" with dissolve
        1.25
        "ch9_424" with dissolve
        1.25
        repeat
    scene ch9_424anim with dissolve
    mc "*Hmnch* {i}I wish we didn’t have to hide..."
    a "*Uhmnsh* {i}Yes..."
    mc "{i}[arelat!cl] [a], you’re so beautiful... I love kissing you more than you could ever know..."
    a "*Hmm, hmnch* {i}Oh, sweetheart..."
    pause
    scene ch9_420- with dissolve
    $ renpy.pause(0.25, hard=True)
    scene ch9_420 with dissolve
    $ renpy.pause(0.025, hard=True)
    stop sound fadeout 0.5
    scene ch9_419--- with dissolve
    a "Wait, remember we’re at the beach."
    scene ch9_419- with dissolve
    mc "There’s no one here, [a]."
    scene ch9_419-- with dissolve
    a "Still, we need to be careful."
    a "Imagine if one of the girls suddenly showed up, or worse..."
    mc "I don’t think anyone’s coming, we’re far away. If they wanted to come, it’d take a while to get here."
    scene ch9_419--- with dissolve
    mc "Let’s keep kissing."
    scene ch9_419---- with dissolve
    a "Sweetheart, we can’t keep taking risks, can’t you wait until we get home?"
    mc "No, I can’t, [a]. Every second of waiting would be torture."
    mc "I just want to keep kissing you."
    a "[mc]..."
    scene ch9_419--- with dissolve
    a "T-that was really sweet."
    pause
    scene ch9_419---- with dissolve
    a "Alright, just a little more."
    play voicefx kissing loop volume 0.2
    scene ch9_419anim with dissolve
    pause
    scene ch9_424anim with dissolve
    pause
    mc "([a] is such a clean and reserved woman... but when our lips meet, all that shyness fades away.)" with dissolve
    mc "(God, I can perfectly feel the texture and warmth of her lips, of her tongue...)" with dissolve
    pause
    scene ch9_419anim with dissolve
    mc "(I bet she, just like me, was longing for this moment.)" with dissolve
    mc "(The way her tongue and breath move sensually inside my mouth confirms it.)" with dissolve
    pause
    mc "(God, I’m starting to lose it.)" with dissolve
    mc "(No, I already have. I’m completely desperate!)" with dissolve
    scene ch9_427 with vpunch
    a "Hmmh!"
    stop voicefx fadeout 0.5
    scene ch9_435 with dissolve
    mc "Sorry, I got carried away."
    a "Oh, God. T-that was intense..."
    scene ch9_436 with dissolve
    a "What are you doing, [mc]?"
    mc "Uhh, my shorts are really tight."
    a "P-people walk through here."
    scene ch9_434 with dissolve
    mc "I haven’t seen a single person walk by."
    scene ch9_437 with dissolve
    pause
    scene ch9_438 with dissolve
    a "N-neither have I, but!..."
    pause
    scene ch9_435 with dissolve
    a "Put it between my legs like before."
    a "That way, if someone walks by, at least they won’t see you with it out."
    mc "Good idea..."
    scene ch9_438 with dissolve
    pause
    scene ch9_439 with dissolve
    pause
    scene ch9_441 with dissolve
    a "Tuck it in well so it doesn’t show."
    mc "Yeah."
    pause
    scene ch9_442 with dissolve
    a "G-good, just like that..."
    pause
    scene ch9_434 with dissolve
    pause
    play voicefx kissing loop volume 0.2
    scene ch9_427 with dissolve
    a "*Hmnsh, hmnch*"
    pause
    jump afterch9_440

init python:
    import random
    store.frame_num = 1  
    store.current_seriesch9_428athjBF_ = random.choice(["ch9_428athjfb_", "ch9_428athjbf_", "ch9_428athjst_"])
    store.previous_seriesch9_428athjBF_ = None
    def ch9_428athjBF_(trans, st, at):  
        animation_series = ["ch9_428athjfb_", "ch9_428athjbf_", "ch9_428athjst_"]
        trans.set_child("{}{}".format(store.current_seriesch9_428athjBF_, store.frame_num))        
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1
            store.previous_seriesch9_428athjBF_ = store.current_seriesch9_428athjBF_
            if random.random() < 0.6:
                store.current_seriesch9_428athjBF_ = "ch9_428athjst_"
            else:
                if store.previous_seriesch9_428athjBF_ in ["ch9_428athjfb_", "ch9_428athjbf_"]:
                    if random.random() < 0.9:
                        store.current_seriesch9_428athjBF_ = "ch9_428athjfb_" if store.previous_seriesch9_428athjBF_ == "ch9_428athjbf_" else "ch9_428athjbf_"
                    else:
                        store.current_seriesch9_428athjBF_ = "ch9_428athjst_"
                else:
                    store.current_seriesch9_428athjBF_ = random.choice(["ch9_428athjfb_", "ch9_428athjbf_"])
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
#
init python:
    def ch9_428athj1_(trans, st, at):  
        trans.set_child("ch9_428athj1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
#
init python:
    def ch9_428athj2_(trans, st, at):  
        trans.set_child("ch9_428athj2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
#
init python:
    def ch9_428athj3_(trans, st, at):  
        trans.set_child("ch9_428athj3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
#
init python:
    def ch9_428athj4_(trans, st, at):  
        trans.set_child("ch9_428athj4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 30:
            store.frame_num = 1    
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_428athj1_():
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
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_428athj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_428athj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_428athj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_428athjBF_") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9428anim") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
#############
screen ch9_428athj2_():
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
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_428athj1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_428athj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_428athj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_428athjBF_") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9428anim") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
###########
screen ch9_428athj3_():
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
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_428athj1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_428athj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_428athj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_428athjBF_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9428anim") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
################
screen ch9_428athj4_():
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
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_428athj1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_428athj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_428athj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_428athjBF_") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9428anim") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
################
screen ch9_428athjBF_():
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
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_428athj1_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_428athj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_428athj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_428athj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" style "textbutton_choice"    
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9428anim") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

label afterch9_440:
    image ch9_428athjBF_:
        function ch9_428athjBF_
    image ch9_428athj1_:
        function ch9_428athj1_
    image ch9_428athj2_:
        function ch9_428athj2_
    image ch9_428athj3_:
        function ch9_428athj3_
    image ch9_428athj4_:
        function ch9_428athj4_
    $ anim_speed = 0.025
    scene ch9_428athj1_ with dissolve
    a "*Hmph, hmm, hmnch* {i}Oh, sweetheart..."
    mc "(This time, she’s the one who jumped on me...)" with dissolve
    a "*Hmnch, hmmn, mmh*"
    pause
    scene ch9_428athj3_ with dissolve
    mc "(The contrast between the usual [a] and the one right now is unbelievable...)" with dissolve
    pause    
    scene ch9_428athjBF_ with dissolve
    a "*Hmph, smnchm hmm*" 
    mc "(I love how her tongue circles around mine...)" with dissolve
    mc "(This must be the most obscene kiss I’ve ever had, and not just because of the kiss itself...)" with dissolve
    mc "(I don’t even know if the drool running down my mouth is mine or hers...)" with dissolve
    pause
    scene ch9_428athj4_ with dissolve
    a "*Smnch, smonch, hmmhs*"
    a "*Uhmm* [mc]..."
    pause
    jump ch9_428athj3_
default current_scene_ch9428 = ""
init python:
    def set_current_scene_ch9428(scene_name_ch9428):
        global current_scene_ch9428
        current_scene_ch9428 = scene_name_ch9428

label ch9_428athj1_:
    $ set_current_scene_ch9428 = "ch9_428athj1_"
    scene ch9_428athj1_ with dissolve
    call screen ch9_428athj1_ with dissolve
label ch9_428athj2_:
    $ set_current_scene_ch9428 = "ch9_428athj2_"
    scene ch9_428athj2_ with dissolve
    call screen ch9_428athj2_ with dissolve
label ch9_428athj4_:
    $ set_current_scene_ch9428 = "ch9_428athj4_"
    scene ch9_428athj4_ with dissolve
    call screen ch9_428athj4_ with dissolve
label ch9_428athj3_:
    $ set_current_scene_ch9428 = "ch9_428athj3_"
    scene ch9_428athj3_ with dissolve
    call screen ch9_428athj3_ with dissolve
label ch9_428athjBF_:
    $ set_current_scene_ch9428 = "ch9_428athjBF_"
    scene ch9_428athjBF_ with dissolve
    call screen ch9_428athjBF_ with dissolve

label continuech9428anim:
    if set_current_scene_ch9428 != "ch9_428athjBF_":
        scene ch9_428athjBF_ with dissolve
    pause
    scene ch9_429 with dissolve
    pause 0.25
    scene ch9_430 with dissolve
    pause 0.25
    scene ch9_431 with dissolve
    pause 0.25
    stop voicefx fadeout 0.5
    scene ch9_431- with dissolve
    pause
    scene ch9_443 with dissolve
    a "Wait, [mc], l-let's not get too carried away."
    a "We came here for something else."
    mc "Again with that?"
    a "I know you don’t care if people see us, but I do."
    scene ch9_419-- with dissolve
    a "Look, t-there are people walking by."
    mc "[a], I don’t see anyone..."
    image ch9_418-----aniom:
        "ch9_419---" with dissolve
        1.0
        "ch9_419----" with dissolve
    scene ch9_418-----aniom with dissolve
    a "Let’s save it for when we get home, okay?"
    mc "I was so close..."
    scene ch9_418 with dissolve
    a "At home, we can fully take care of that."
    pause
    mc "Alright..."
    scene ch9_418- with dissolve
    a "Let’s see if those underwear are around here, heh..."
    pause
    scene ch9_444 with dissolve
    a "I thought I put them in this bag, hmm..."
    a "I put them next to the sunscreen, how are they not here?"
    pause
    scene ch9_445 with dissolve
    a "Let’s check this other bag..."
    a "Or did I put them in my purse?"
    mc "(She can’t be doing this to me...)" with dissolve
    a "I don’t think so, I would’ve remembered. Where did I put them?"
    pause
    scene ch9_446 with dissolve
    pause
    mc "(That bikini is really tight on her, I can’t believe we convinced her to wear it.)" with dissolve
    mc "(Her bottoms look like a thong with how tight they are...)" with dissolve
    mc "(Ugh... Having an erection this long can’t be good for my health.)" with dissolve
    mc "(I’ll go sit in the car and jerk off, or my dick’s going to rot off.)"
    a "Ah, here!{w=0.5} No, it’s just a shirt. Where did I put them?"
    pause
    scene ch9_447 with dissolve
    pause
    a "[mc]..."
    mc "Do you want me to help you look?"
    a "N-no, if they’re not in this bag, they’re probably at the beach in my purse."
    mc "(Do those underwear even exist?)" with dissolve
    pause
    scene ch9_450 with dissolve
    mc "(I don’t know if that’s the case, but I can’t take this any longer...)" with dissolve
    scene ch9_452 with dissolve
    mc "(I’m gonna fuck these asscheeks!)" with dissolve
    a "Huh?"
init python:
    def ch9_450aaj1_(trans, st, at):  
        trans.set_child("ch9_450aaj6_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(1.0, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    def ch9_450aaj2_(trans, st, at):  
        trans.set_child("ch9_450aaj2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.4, channel='sound')  
            renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_450aaj3_(trans, st, at):  
        trans.set_child("ch9_450aaj3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_450aaj4_(trans, st, at):  
        trans.set_child("ch9_450aaj4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.75, channel='sound')  
            renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_450aaj5_(trans, st, at):  
        trans.set_child("ch9_450aaj5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_450aaj6_(trans, st, at):  
        trans.set_child("ch9_450aaj7_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)  
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value


init python:
    def ch9_450aaj7_(trans, st, at):  
        trans.set_child("ch9_450aaj8_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_450aaj8_(trans, st, at):  
        trans.set_child("ch9_450aaj9_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
$ arrow_alpha = 0.8 
default button_visiblech9450 = True
$ button_visiblech9450 = True
screen scrollable_ch9_450aaj1_():
    default ypos = 0.0
    
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        add "ch9_450aaj1_"
    hbox:
        xpos 20
        ypos 1000
        if button_visiblech9450:  
            textbutton "Hide" action [SetVariable("arrow_alpha", 0.0), SetVariable("button_visiblech9450", False)] style "textbutton_choice"
    vbox:
        button:
            background None
            xpos 220
            ypos 0
            xsize 1700
            ysize 1080
            action Return()
            add "images/gamemenu/updownarrows.webp" xalign 0.75 yalign 0.5 alpha arrow_alpha
transform rotate_text:
    rotate -90
screen scrollable_ch9_450aaj1_2():
    default ypos = 0.0
    
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        add "ch9_450aaj1_"
    hbox:
        xpos 20
        ypos 1000
        if button_visiblech9450: 
            textbutton "Hide" action [SetVariable("arrow_alpha", 0.0), SetVariable("button_visiblech9450", False)] style "textbutton_choice"
    vbox:
        button:
            background None
            xpos 220
            ypos 0
            xsize 1700
            ysize 1080
            action Show("ch9_450aaj1_") style "textbutton_choice"
            add "images/gamemenu/updownarrows.webp" xalign 0.75 yalign 0.5 alpha arrow_alpha

screen ch9_450aaj1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj2_") ] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj3_")] style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj4_")] style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj5_")] style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj6_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj7_")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action [Hide("scrollable_ch9_450aaj1_2"), Jump("ch9_450aaj8_")] style "textbutton_choice"

    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action [Hide("scrollable_ch9_450aaj1_2"), Jump("continuech9_450a")] style "textbutton_choice"   
    hbox:
        yalign 0.99
        xalign 0.2
        textbutton _("Hide") action Hide("ch9_450aaj1_") style "textbutton_choice"  
    #
screen ch9_450aaj2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action Jump("ch9_450aaj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action Jump("ch9_450aaj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action Jump("ch9_450aaj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action Jump("ch9_450aaj6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action Jump("ch9_450aaj7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action Jump("ch9_450aaj8_") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
    #
screen ch9_450aaj3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action Jump("ch9_450aaj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action Jump("ch9_450aaj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action Jump("ch9_450aaj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action Jump("ch9_450aaj6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action Jump("ch9_450aaj7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action Jump("ch9_450aaj8_") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
 #
screen ch9_450aaj4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action Jump("ch9_450aaj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action Jump("ch9_450aaj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action Jump("ch9_450aaj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action Jump("ch9_450aaj6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action Jump("ch9_450aaj7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action Jump("ch9_450aaj8_") style "textbutton_choice" 
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
    #
screen ch9_450aaj5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")]style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action Jump("ch9_450aaj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action Jump("ch9_450aaj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action Jump("ch9_450aaj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action Jump("ch9_450aaj6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action Jump("ch9_450aaj7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action Jump("ch9_450aaj8_") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
        #
screen ch9_450aaj6_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action Jump("ch9_450aaj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action Jump("ch9_450aaj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action Jump("ch9_450aaj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action Jump("ch9_450aaj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action Jump("ch9_450aaj7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action Jump("ch9_450aaj8_") style "textbutton_choice"  
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
        #
screen ch9_450aaj7_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action Jump("ch9_450aaj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action Jump("ch9_450aaj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action Jump("ch9_450aaj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action Jump("ch9_450aaj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action Jump("ch9_450aaj6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" action Jump("ch9_450aaj8_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      
screen ch9_450aaj8_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 1" action [SetVariable("button_visiblech9450", True), Jump("ch9_450aaj1_")] style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 2" action Jump("ch9_450aaj2_") style "textbutton_choice" 
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 3" action Jump("ch9_450aaj3_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 4" action Jump("ch9_450aaj4_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 5" action Jump("ch9_450aaj5_") style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 6" action Jump("ch9_450aaj6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 7" action Jump("ch9_450aaj7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 8" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("continuech9_450a") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"      
  
            
label afterch9452:
    image ch9_450aaj1_:
        function ch9_450aaj1_
    image ch9_450aaj2_:
        function ch9_450aaj2_
    image ch9_450aaj3_:
        function ch9_450aaj3_
    image ch9_450aaj4_:
        function ch9_450aaj4_
    image ch9_450aaj5_:
        function ch9_450aaj5_
    image ch9_450aaj6_:
        function ch9_450aaj6_
    image ch9_450aaj7_:
        function ch9_450aaj7_
    image ch9_450aaj8_:
        function ch9_450aaj8_
    $ anim_speed = 0.0085
    show screen scrollable_ch9_450aaj1_ with dissolve
    a "[mc]!"
    mc "*Uh* Sorry, [arelat] [a], but I had to do it."
    a "Honey, I told you we’d take care of this when we got home..."
    mc "*Hngh* I couldn’t resist, you look too sexy in this bikini, and when you bent over, I just..."
    mc "*Hmngh*"
    a "Honey..."
    a "*Uh* D-don’t thrust so hard."
    mc "*Hngh* (I couldn’t go slower even if I wanted to, this feels too good.)"
    a "Honey, y-you need to learn to control yourself..."
    mc "I’m sorry, it’s just with this bikini and these hips... *hmnh*{w=0.5} it’s hard to hold back."
    a "[mc]..."
    mc "(Acting like she doesn’t want it again...)" with dissolve
    mc "(I could be wrong, but isn’t it a little obvious that the underwear was just an excuse to get me alone here with her?)" with dissolve
    mc "(It might not be the case, but if it wasn't, she wouldn’t be standing still while I’m doing this...)" with dissolve
    pause
    mc "(Though I also don’t want her to think I’m taking advantage of her...)" with dissolve
    mc "If it bothers you, I can stop..."
    a "..."
    pause
    scene blackscreen with dissolve
    hide screen scrollable_ch9_450aaj1_
    scene ch9_450aaj5_ with dissolve
    a "N-no... I-I..."
    pause
    a "E-earlier, we were at the beach sunbathing and then in the water."
    a "Then, {w=0.5}*uh, uh*{w=0.5} I brought you here and we kissed..."
    a "I’ve been teasing you the whole time..."
    scene ch9_450aaj3_ with dissolve
    a "N-not teasing you intentionally, I..."
    a "You know, I’m {w=0.5}*uh, uh*{w=0.5} a very attractive woman and..."
    a "{w=0.5}*Uh, uh*{w=0.5} Maybe not that attractive, but definitely appealing to you, or well, that’s what you always tell me and... I mean..."
    pause
    a "W-what I’m trying to say is I understand your frustration, I’m not insensitive."
    a "Uhm..."
    pause
    scene ch9_450aaj2_ with dissolve
    mc "I get what you’re trying to say, [arelat] [a], you don’t need to explain it to me."
    a "Yeah, in short, that’s it."
    pause
    mc "(She’s acting really strange, must be the fear of someone seeing us.)" with dissolve
    pause
    scene ch9_450aaj4_ with dissolve
    a "So... it’s okay."
    mc "*Hngh* Oh, yes..."
    pause
    a "Does it feel good?"
    mc "Yes, it feels really good... *hmmh*"
    pause
    mc "You have such a beautiful ass, [arelat] [a]..."
    scene ch9_450aaj7_ with dissolve
    a "T-thanks, honey..."
    pause
    a "And... how long have you had that erection now?"
    mc "I don’t know, an hour or two?"
    a "Oh my God..."
    a "T-then hurry up, honey. Having an erection for so long cannot be good for your health."
    $ anim_speed = 0.0075
    mc "Yeah, {w=0.5}*uhmh*{w=0.25} I’m trying."
    scene ch9_450aaj8_ with dissolve
    a "*Uh, uh, uh* [mc]..."
    a "Honey, there’s a car coming."
    mc "It’s... {w=0.25}*Hmgh*{w=0.25} far away."
    a "{i}But it’s getting closer!"
    mc "*Hngh* They’re parking."
    a "Yes, but..."
    mc "*Hmgh* Almost there..."
    pause
    call screen ch9_450aaj8_ with dissolve
default current_scenech9aaj1_ = ""
init python:
    def current_scenech9428(scene_namech9428):
        global current_scenech9428
        current_scenech9428 = scene_namech9428
label ch9_450aaj1_:
    $ arrow_alpha = 0.25  
    $ current_scenech9aaj1_ = False
    scene blackscreen with dissolve
    show screen scrollable_ch9_450aaj1_2 with dissolve
    call screen ch9_450aaj1_ with dissolve  
label ch9_450aaj2_:
    $ current_scenech9aaj1_ = "False"
    scene ch9_450aaj2_ with dissolve
    call screen ch9_450aaj2_ with dissolve
label ch9_450aaj3_:
    $ current_scenech9aaj1_ = "False"
    scene ch9_450aaj3_ with dissolve
    call screen ch9_450aaj3_ with dissolve
label ch9_450aaj4_:
    $ current_scenech9aaj1_ = "False"
    scene ch9_450aaj4_ with dissolve
    call screen ch9_450aaj4_ with dissolve
label ch9_450aaj5_:
    $ current_scenech9aaj1_ = "False"
    scene ch9_450aaj5_ with dissolve
    call screen ch9_450aaj5_ with dissolve
label ch9_450aaj6_:
    $ current_scenech9aaj1_ = "True"
    scene ch9_450aaj6_ with dissolve
    call screen ch9_450aaj6_ with dissolve
label ch9_450aaj7_:
    $ current_scenech9aaj1_ = "False"
    scene ch9_450aaj7_ with dissolve
    call screen ch9_450aaj7_ with dissolve
label ch9_450aaj8_:
    $ current_scenech9aaj1_ = "False"
    scene ch9_450aaj8_ with dissolve
    call screen ch9_450aaj8_ with dissolve

label continuech9_450a:
    if current_scenech9aaj1_ != "True":
        scene ch9_450aaj6_ with dissolve
    $ anim_speed = 0.0060
    mc "*Hmngh*..."
    a "I’ve already seen that same car pass three times."
    mc "*Hmhgh, Hngh!*"
    a "I-it’s coming back again..."
    mc "*Hmngh* Uhh..."
    a "*Uh* {i}S-stop, [mc]."
    a "{i}Oh my God, they’re going to see us!"
    mc "*NHGH!*"
    pause
    scene ch9_454 with hpunch
    a "{i}[mc]!"
    a "Don’t you hear me telling you to stop?"
    mc "But no one was coming."
    a "But what if someone did?"
    mc "But that didn’t happen."
    pause
    scene ch9_455 with dissolve
    a "Well, but..."
    a "M-more people are arriving."
    mc "[arelat!cl] [a], I don’t see anyone..."
    scene ch9_456 with dissolve
    a "..."
    pause
    image ch9_456anim:
        "ch9_457" with dissolve
        0.5
        "ch9_458" with dissolve
        0.5
        "ch9_459" with dissolve

    scene ch9_456anim with dissolve
    pause
    a "Uhm..."
    a "Erm, so..."
    scene ch9_461 with dissolve
    a "What do you propose we do, hmm, [mc]?"
    mc "Uh?"
    scene ch9_460 with dissolve
    a "Eh... t-to finish with this situation."
    mc "I’m confused, didn’t you want us to stop?"
    scene ch9_461 with dissolve
    a "Eh, no..."
    a "I mean, yes."
    a "But not leaving you like this..."
    a "What I said was that we should be more discreet."
    pause
    scene ch9_462 with dissolve
    a "{i}Pull up your pants, a car is coming!"
    scene ch9_462- with vpunch
    pause
    scene ch9_463- with dissolve
    mc "It’s turning around, it wasn’t coming here."
    mc "No one will come here. Relax."
    a "We don’t know that, [mc]."
    pause
    scene ch9_463-- with dissolve
    a "God, this is making me so nervous..."
    a "If someone passes by and sees us... Oh God, I don’t even want to imagine it..."
    a "A-allright..."
    pause
    a "So..."
    mc "[a], yesterday..."
    mc "Yesterday felt so good when you did it with your mouth..."
    a "W-with my mouth?"
    a "Eh... I was a bit drunk yesterday, hehe... Erm..."
    a "I-I don’t really remember..."
    scene ch9_463--- with hpunch
    mc "*Ngh* [arelat!cl] [a], I can’t take it anymore..."
    a "O-okay, just..."
    scene ch9_463---- with dissolve
    a "We’ll take care of it, but..."
    a "God, [mc], this is so risky..."
    a "And then there’s that car that keeps driving around."
    pause
    scene ch9_464 with dissolve
    a "{i}{size=-3}Oh my God..."
    a "No one’s coming, right?"
    scene ch9_465 with dissolve
    mc "We’re still as alone as when we arrived."
    a "It’s just hearing a car or something and I get nervous."
    a "..."
    pause
    scene ch9_466 with dissolve
    a "I’m going to... jerk you off. That will help, right?"
    mc "Yes..."
    scene ch9_467 with dissolve
    mc "Thanks, [a], you’re the best."
    a "Y-you’re welcome, honey."
    mc "(I won’t finish just with her hand but I’m not going to reject it either...)"
    a "..."
    pause
    scene ch9_468ahj1_1 with dissolve
    a "I’m scared of the idea of someone discovering us but I can’t let you go like this."
    a "Don’t think I’ll do this every time you want."
    mc "Of course not."
    a "I-I mean..."
    jump aftercch9_468ahj1_animations
init python:
    store.last_played_sound2 = None
    store.current_seriesch9_468ahj1_ = None
    store.frame_num = 1
    store.series_playedch9_468ahj1_ = False
    def ch9_468ahj1_(trans, st, at):
        if not store.series_playedch9_468ahj1_:
            if store.current_seriesch9_468ahj1_ is None:
                store.current_seriesch9_468ahj1_ = renpy.random.choice(["ch9_468ahj1_", "ch9_468ahj1fx_"])
                store.frame_num = 1
            trans.set_child("{}{}".format(store.current_seriesch9_468ahj1_, store.frame_num))
            store.frame_num += 1
            if store.frame_num > 14:
                store.series_playedch9_468ahj1_ = True
                store.frame_num = 15
                store.current_seriesch9_468ahj1_ = "ch9_468ahj1_"
        else:
            trans.set_child("ch9_468ahj1_{}".format(store.frame_num))
            store.frame_num += 1
            if store.frame_num > 40:
                store.series_playedch9_468ahj1_ = False
                store.current_seriesch9_468ahj1_ = None
                store.frame_num = 1
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value





init python:
    store.last_played_sound2 = None
    store.current_series2 = None
    store.frame_num = 1
    store.series_played2 = False
    def ch9_468ahj2_(trans, st, at):
        if not store.series_played2:
            if store.current_series2 is None:
                store.current_series2 = renpy.random.choice(["ch9_468ahj2_", "ch9_468ahj2fx_"])
                store.frame_num = 1
            trans.set_child("{}{}".format(store.current_series2, store.frame_num))
            store.frame_num += 1
            if store.frame_num > 14:
                store.series_played2 = True
                store.frame_num = 15
                store.current_series2 = "ch9_468ahj2_"
        else:
            trans.set_child("ch9_468ahj2_{}".format(store.frame_num))
            store.frame_num += 1
            if store.frame_num > 40:
                store.series_played2 = False
                store.current_series2 = None
                store.frame_num = 1
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value




init python:
    store.last_played_sound2 = None
    store.current_seriesch9_468ahj3_ = None
    store.frame_num = 1
    store.series_playedch9_468ahj3_ = False
    def ch9_468ahj3_(trans, st, at):
        if not store.series_playedch9_468ahj3_:
            if store.current_seriesch9_468ahj3_ is None:
                store.current_seriesch9_468ahj3_ = renpy.random.choice(["ch9_468ahj3_", "ch9_468ahj3fx_"])
                store.frame_num = 1
            trans.set_child("{}{}".format(store.current_seriesch9_468ahj3_, store.frame_num))
            store.frame_num += 1
            if store.frame_num > 14:
                store.series_playedch9_468ahj3_ = True
                store.frame_num = 15
                store.current_seriesch9_468ahj3_ = "ch9_468ahj3_"
        else:
            trans.set_child("ch9_468ahj3_{}".format(store.frame_num))
            store.frame_num += 1
            if store.frame_num > 40:
                store.series_playedch9_468ahj3_ = False
                store.current_seriesch9_468ahj3_ = None
                store.frame_num = 1
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

screen ch9_468ahj1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_468ahj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_468ahj3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_468ahj2_anims") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

screen ch9_468ahj2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch9_468ahj1_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_468ahj3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_468ahj2_anims") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

screen ch9_468ahj3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch9_468ahj1_") style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_468ahj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_468ahj2_anims") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   

label aftercch9_468ahj1_animations:
    image ch9_468ahj1_:
        function ch9_468ahj1_
    image ch9_468ahj2_:
        function ch9_468ahj2_
    image ch9_468ahj3_:
        function ch9_468ahj3_
    $ anim_speed = 0.03
    scene ch9_468ahj1_ with dissolve
    mc "*Hmm*... feels so good..."
    pause
    mc "Faster..."
    $ anim_speed = 0.015
    mc "Just like that, oh..."
    mc "Your hands feel so good, they’re warm and nice..."
    pause
    mc "Can you grip it a little tighter?"
    a "Like this?"
    mc "*Hmm* Yes... ohh..."
    pause
    a "This is the last time I do this for you... {w=0.5}Uhm...{w=0.5} outdoors."
    a "Today is an exception because of the bikini and all that..."
    mc "But at home, right?"
    a "Shhh..."
    pause
    scene ch9_468ahj2_ with dissolve
    a "I’m not happy with you, young man."
    mc "Did I do something wrong?"
    a "The way you grabbed me from behind... {i}You seemed like a wild man!"
    mc "Oh, that..."
    mc "I got desperate, I didn’t even know what I was doing."
    a "Those aren’t excuses, apologize, young man."
    mc "Sorry, [arelat] [a]."
    a "*Giggles*"
    pause
    mc "And what’s the proper way?"
    a "Hm?"
    scene ch9_468ahj3_ with dissolve
    mc "You said you didn’t like how I took you from behind that way."
    mc "What’s the correct way?"
    pause
    a "Well, asking for permission, for example."
    mc "Got it..."
    pause
    mc "Can I touch one of your breasts?"
    a "*Giggles* Permission is asked before you do it, you know?"
    mc "Oops."
    a "You little rascal..."
    pause
    call screen ch9_468ahj3_ with dissolve
    pause


label ch9_468ahj1_:
    scene ch9_468ahj1_ with dissolve
    call screen ch9_468ahj1_ with dissolve
label ch9_468ahj2_:
    scene ch9_468ahj2_ with dissolve
    call screen ch9_468ahj2_ with dissolve
label ch9_468ahj3_:
    scene ch9_468ahj3_ with dissolve
    call screen ch9_468ahj3_ with dissolve


init python:
    store.last_played_soundch9_468atj1 = None
    store.current_seriesch9_468atj1 = None
    store.frame_num = 1
    store.series_playedch9_468atj1 = False
    def ch9_468atj1_(trans, st, at):
        if not store.series_playedch9_468atj1:
            if store.current_seriesch9_468atj1 is None:
                store.current_seriesch9_468atj1 = renpy.random.choice(["ch9_468atj1_", "ch9_468atj1fx_"])
                store.frame_num = 1
            trans.set_child("{}{}".format(store.current_seriesch9_468atj1, store.frame_num))
            store.frame_num += 1
            if store.frame_num > 14:
                store.series_playedch9_468atj1 = True
                store.frame_num = 15
                store.current_seriesch9_468atj1 = "ch9_468atj1_"
        else:
            trans.set_child("ch9_468atj1_{}".format(store.frame_num))
            store.frame_num += 1
            if store.frame_num > 40:
                store.series_playedch9_468atj1 = False
                store.current_seriesch9_468atj1 = None
                store.frame_num = 1
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

init python:
    store.last_played_soundch9_468atj2 = None
    store.current_seriesch9_468atj2 = None
    store.frame_num = 1
    store.series_playedch9_468atj2 = False
    def ch9_468atj2_(trans, st, at):
        if not store.series_playedch9_468atj2:
            if store.current_seriesch9_468atj2 is None:
                store.current_seriesch9_468atj2 = renpy.random.choice(["ch9_468atj2_", "ch9_468atj2fx_"])
                store.frame_num = 1
            trans.set_child("{}{}".format(store.current_seriesch9_468atj2, store.frame_num))
            store.frame_num += 1
            if store.frame_num > 14:
                store.series_playedch9_468atj2 = True
                store.frame_num = 15
                store.current_seriesch9_468atj2 = "ch9_468atj2_"
        else:
            trans.set_child("ch9_468atj2_{}".format(store.frame_num))
            store.frame_num += 1
            if store.frame_num > 40:
                store.series_playedch9_468atj2 = False
                store.current_seriesch9_468atj2 = None
                store.frame_num = 1
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

init python:
    store.last_played_soundch9_468atj3_ = None
    store.current_seriesch9_468atj3 = None
    store.frame_num = 1
    store.series_playedch9_468atj3 = False
    def ch9_468atj3_(trans, st, at):
        if not store.series_playedch9_468atj3:
            if store.current_seriesch9_468atj3 is None:
                store.current_seriesch9_468atj3 = renpy.random.choice(["ch9_468atj3_", "ch9_468atj3fx_"])
                store.frame_num = 1
            trans.set_child("{}{}".format(store.current_seriesch9_468atj3, store.frame_num))
            store.frame_num += 1
            if store.frame_num > 14:
                store.series_playedch9_468atj3 = True
                store.frame_num = 15
                store.current_seriesch9_468atj3 = "ch9_468atj3_"
        else:
            trans.set_child("ch9_468atj3_{}".format(store.frame_num))
            store.frame_num += 1
            if store.frame_num > 40:
                store.series_playedch9_468atj3 = False
                store.current_seriesch9_468atj3 = None
                store.frame_num = 1
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value

init python:
    def ch9_468atj4_(trans, st, at):  
        trans.set_child("ch9_468atj4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    def ch9_468atj5_(trans, st, at):  
        trans.set_child("ch9_468atj5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

screen ch9_468atj1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_468atj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_468atj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_468atj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_468atj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9468atjdwy") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

screen ch9_468atj2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_468atj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_468atj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch9_468atj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9468atjdwy") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

screen ch9_468atj3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_468atj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_468atj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch9_468atj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9468atjdwy") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

screen ch9_468atj4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_468atj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_468atj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" action Jump("ch9_468atj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9468atjdwy") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  

screen ch9_468atj5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 1" action Jump("ch9_468atj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 2" action Jump("ch9_468atj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 3" action Jump("ch9_468atj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9468atjdwy") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
label afterch9_468ahj2_anims:
    image ch9_468atj1_:
        function ch9_468atj1_
    image ch9_468atj2_:
        function ch9_468atj2_
    image ch9_468atj3_:
        function ch9_468atj3_
    image ch9_468atj4_:
        function ch9_468atj4_
    image ch9_468atj5_:
        function ch9_468atj5_
    scene ch9_468ahj1_ with dissolve
    mc "(This is so good... And those tits are fucking delicious.)"
    mc "(If I ask her to take off her bra, she'll probably say no but man I'd love to see those huge tits while she jerks me off.)"
    pause
    a "You haven’t stopped looking at them..."
    mc "Sorry?"
    a "I mean, you can’t stop looking at my breasts."
    mc "Ah, yes... Your tits are gorgeous."
    a "Do you want me to do it with them?"
    a "You know, I could just... place it between my breasts to make this quicker."
    mc "You read my mind, [arelat] [a]..."
    a "*Giglge*... I know how much you like them..."
    a "Well, come a little closer, sweetheart."
    scene ch9_469 with dissolve
    a "Does it feel good like this?"
    mc "Yes..."
    $ anim_speed = 0.03
    scene ch9_468atj1_ with dissolve
    mc "*Hmmh* Feels so good..."
    mc "Oh, they’re so soft..."
    a "You’re so hot..."
    mc "Do you really think so?"
    a "I mean, your... dick, it feels hot between my breasts."
    mc "Oh..."
    mc "I’m just so horny."
    mc "And now that I’m between those beauties, even more."
    a "{i}You need to finish now, sweetheart..."
    a "We need to go back to the beach, [d] must be wondering where we are."
    pause
    call screen ch9_468atj_1bfr with dissolve
screen ch9_468atj_1bfr():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.04) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_468atj_1bfr") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
label ch9_468atj_1bfr:
    mc "Can we do it without the bra?"
    a "Yes... but hurry up, honey."
    scene ch9_468atj2_ with dissolve
    a "Watch out for anyone coming."
    mc "Yeah, don’t worry... *hmm*"
    pause
    scene ch9_468atj3_ with dissolve
    $ anim_speed = 0.021
    a "Almost done, honey?"
    mc "Not yet, but it feels so good."
    a "Hurry up, [mc], we don’t have all day."
    a "Want me to do it faster?"
    $ anim_speed = 0.011
    a "How about this, does it feel better?"
    mc "Yes, *hmm* so good..."
    pause
    scene ch9_468atj4_ with dissolve
    mc "I still can’t believe [drelat] [d] has been neglecting you like this..."
    a "What do you mean?"
    mc "I would spend at least two hours a day with you..."
    pause
    mc "You’re too much woman for him."
    scene ch9_468atj5_ with dissolve
    a "Shh... let’s not talk about that."
    a "Focus on what’s important... I need you to finish soon."
    a "That's it, honey, finish for me..."
    mc "*Hmgh, hmgh*"
    pause
    jump ch9_468atj2_
label ch9_468atj1_:
    scene ch9_468atj1_ with dissolve
    call screen ch9_468atj1_ with dissolve
define current_scenech9_468atj2_ = "False"    
label ch9_468atj2_:
    $ current_scenech9_468atj2_ = "True"
    scene ch9_468atj2_ with dissolve
    call screen ch9_468atj2_ with dissolve
label ch9_468atj3_:
    $ current_scenech9_468atj2_ = "False"
    scene ch9_468atj3_ with dissolve
    call screen ch9_468atj3_ with dissolve
label ch9_468atj4_:
    $ current_scenech9_468atj2_ = "False"
    scene ch9_468atj4_ with dissolve
    call screen ch9_468atj4_ with dissolve
label ch9_468atj5_:
    $ current_scenech9_468atj2_ = "False"
    scene ch9_468atj5_ with dissolve
    call screen ch9_468atj5_ with dissolve

label afterch9468atjdwy:
    $ anim_speed = 0.01
    if current_scenech9_468atj2_ == "False":
        scene ch9_468atj2_ with dissolve
    mc "What about you, [arelat] [a]?"
    a "What do you mean?"
    mc "*Hmn* I also want to please you..."
    pause
    mc "I don’t like it when only one side enjoys."
    mc "I want to taste you, [arelat] [a]."
    a "Taste me?"
    mc "Yes... savor you."
    a "..."
    play voicefx kissing loop volume 0.25
    scene ch9_470 with dissolve
    pause
    stop voicefx fadeout 0.5
    scene ch9_471 with dissolve
    mc "I'll be quick."
    a "[mc]..."
    pause
    play voicefx kissing loop volume 0.25
    scene ch9_472 with dissolve
    a "*Smnch, mnch*"
    pause
    scene ch9_473 with dissolve
    a "*Hmh* If someone comes, we won't be able to see them."
    a "*Hmn, smnch*"
    pause
    scene ch9_474 with dissolve
    pause
    scene ch9_475 with dissolve
    pause
    image ch9_474anim:
        "ch9_474" with dissolve
        1.5
        "ch9_475" with dissolve
        1.5
        repeat
    scene ch9_474anim with dissolve
    pause
    stop voicefx fadeout 0.5
    scene ch9_476 with dissolve
    a "Oh, honey..."
    mc "You look beautiful, [arelat] [a]..."
    scene ch9_477 with dissolve
    mc "Hmm... your breasts fascinate me."
    a "*Hmm* Oh..."
    scene ch9_477- with dissolve
    mc "*Hmpsh, hmmph, hmpsh*"
    a "Don't suck so hard, [mc]. *hmh*"
    scene ch9_478 with dissolve
    pause
    a "*Uhmm* Baby, it hurts a little, be gentler."
    scene ch9_479 with dissolve
    mc "What a delight..."
    a "Huh..."
    pause
    scene ch9_480 with dissolve
    a "W-what are you doing, honey?"
    mc "I want to savor you, [a]..."
    a "Oh, god..."
    scene ch9_481 with dissolve
    mc "(Oh, look how wet she is...)" with dissolve
    a "[mc], we have to go back..."
    scene ch9_480 with dissolve
    mc "You're quite wet, [arelat] [a]..."
    mc "I'm not going to let you go like this."
    scene ch9_481 with dissolve
    a "Honey..."
    pause
    a "Okay, l-let's hurry then..."
    scene ch9_482 with dissolve
    mc "Oh, wow..."
    mc "(I love that she moved her panties aside for me...)" with dissolve
    mc "(I'm not speaking figuratively when I say she looks delicious, I'm literally drooling.)" with dissolve
    image ch9_482anim:
        "ch9_482-" with Dissolve(0.5)
        0.5
        "ch9_482" with Dissolve(0.5)
        4.0
        "ch9_482-" with Dissolve(0.5)
        0.5
        "ch9_482" with Dissolve(0.5)
        1.0
        "ch9_482-" with Dissolve(0.5)
        0.5
        "ch9_482" with Dissolve(0.5)
        4.0
        repeat
    scene ch9_482anim with dissolve
    pause
    mc "(Look at how she's moving, and I haven't even touched her yet...)"
    a "Honey..."
    mc "What a beauty..."
    scene ch9_484- with dissolve
    mc "(And what a scent...)"
    pause
    scene ch9_484 with dissolve
    a "*Hmm* Uh..."
    pause
    scene ch9_485 with dissolve
    pause
    scene ch9_487 with dissolve
    pause
    scene ch9_486 with dissolve
    pause
    image ch9_483anim:
        "ch9_483" 
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.0
        ease 2.0 zoom 1.025
        ease 2.0 zoom 1.0
        repeat
    scene ch9_483anim with dissolve
    play sound kissing2 fadein 0.5 loop volume 0.15
    play voicefx "/audio/wavs/a/amoansoft.ogg" fadein 2.0 loop volume 0.3
    a "*Uhh, uhm*"
    pause
    jump bfch9_480acl1_ 
init python:
    def ch9_480acl1_(trans, st, at):  
        trans.set_child("ch9_480acl1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_480acl2_(trans, st, at):  
        trans.set_child("ch9_480acl2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
init python:
    def ch9_480acl3_(trans, st, at):  
        trans.set_child("ch9_480acl3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value  


screen ch9_480acl1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.045) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_480acl2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_480acl3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_480acl1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_480acl2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.045) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch9_480acl1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_480acl3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_480acl1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_480acl3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.045) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.015) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch9_480acl1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_480acl2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_480acl1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
label bfch9_480acl1_:
    image ch9_480acl1_:
        function ch9_480acl1_
    image ch9_480acl2_:
        function ch9_480acl2_
    image ch9_480acl3_:
        function ch9_480acl3_
    $ anim_speed = 0.03
    scene ch9_480acl1_ with dissolve
    a "*Mha.. hmm...*"
    pause
    mc "*Smnch, hmph* Are you comfortable like this?"
    a "*Hmm* Y-yes, hmm..."
    mc "*Smch, slrp, lmmph*"
    a "Oh, [mc]... *Hmh*..."
    pause
    a "Do you really enjoy doing this to me?"
    mc "Of course. *shlup*"
    mc "Why the question?"
    a "No, just wondering..."
    mc "*Hmnch* I love your pussy... So delicious..."
    pause
    a "*Hmm, uhmh* This is crazy..."
    a "*Uh, hmm* We should have stayed home like you said. *Uhh*"
    mc "*Mnch* And miss out on this lovely family beach day?"
    a "*Hmh* D-don't joke, [mc]."
    pause
    a "While everyone is playing and having fun at the beach, we {w=0.25}*Hmm*{w=0.25} are here, doing this..."
    a "We're {w=0.25}*uhm*{w=0.25} horrible..."
    pause
    scene ch9_480acl2_ with dissolve
    a "*Uuh, hmm* This has completely gotten out of hand."
    mc "*Hmch* That's why you brought me here, right?"
    mc "To enjoy ourselves alone without worrying."
    a "..."
    mc "*Mhlm, smnch*"
    pause
    a "Oh... *hmh* Oh, honey... that feelt really good."
    mc "*Lah, lmhm* Like this?"
    scene ch9_480acl3_ with dissolve
    a "*Hmh, ah* Y-yes, ahm..."
    mc "That's it... it's just you and me, don't think about anything else but your own pleasure."
    a "*Hmm, mhm, ah*..."
    pause
    define ch9_480acl1_pov = "False"
    call screen ch9_480acl3_ with dissolve
label ch9_480acl1_:
    $ ch9_480acl1_pov = "False"
    scene ch9_480acl1_ with dissolve
    call screen ch9_480acl1_ with dissolve

label ch9_480acl2_:
    $ ch9_480acl1_pov = "True"
    scene ch9_480acl2_ with dissolve
    call screen ch9_480acl2_ with dissolve
    
label ch9_480acl3_:
    $ ch9_480acl1_pov = "False"
    scene ch9_480acl3_ with dissolve
    call screen ch9_480acl3_ with dissolve


label afterch9_480acl1_:
    if ch9_480acl1_pov == "False":
        $ anim_speed = 0.015
        scene ch9_480acl2_ with dissolve  
    a "Ah... *hmgh* [mc]..."
    a "I-I’m close, baby... *Huhm, hmmngh*"
    $ anim_speed = 0.0075
    a "*Ah, uhhmm!* [mc]! *Hmmgh, mauhh!*"
    pause
    image ch9_484anim:
        "ch9_484-" with dissolve
        0.5
        "ch9_484" with dissolve
        0.5
        "ch9_485" with dissolve
        0.5
        "ch9_487" with dissolve
        0.5
        "ch9_486" with dissolve
        0.5
        "ch9_485" with dissolve
        0.5
        "ch9_487" with dissolve
        0.5
        "ch9_486" with dissolve
        0.5
        "ch9_485" with dissolve
        0.5
        "ch9_487" with dissolve
        0.5
        "ch9_486" with dissolve
        0.5
        "ch9_485" with dissolve
        0.5
        "ch9_486" with dissolve
        0.5
        "ch9_485" with dissolve
        0.5
        "ch9_486" with dissolve
        0.5
        "ch9_485" with dissolve
        0.5
        "ch9_484-" with dissolve
        0.5
        "ch9_484" with dissolve
        0.5
        repeat
    scene ch9_484anim with dissolve
    mc "*Hmhch, slch, smnch*"
    a "*Hah!* Baby... *Huh, uhm, ahh!*"
    pause
    stop sound fadeout 0.5
    stop voicefx fadeout 0.5
    play voicefx "/audio/wavs/a/amoanhard_2.ogg" fadein 0.1 volume 0.5
    scene ch9_488 with cumming
    a "*Hmhm, Aaah!*" with flash
    mc "Oh!"
    pause
    scene ch9_490 with dissolve
    pause
    scene ch9_491 with dissolve
    pause
    image ch9_490anim:
        "ch9_490" with dissolve
        3.0
        "ch9_491" with dissolve
        0.5
        "ch9_490" with dissolve
        3.0
        "ch9_491" with dissolve
        0.5
        "ch9_490" with dissolve
        3.0
        "ch9_491" with dissolve
        0.5
        "ch9_490" with dissolve
        3.0
        "ch9_491" with dissolve
        0.5
        repeat
    scene ch9_490anim with dissolve
    a "Uff, huf... {i}Oh, God..."
    mc "(That was intense.)" with dissolve
    pause
    mc "(Wow... she's still having aftershocks of pleasure...) " with dissolve
    mc "(She really likes oral sex...) " with dissolve
    pause
    mc "(What a pose... legs spread, like inviting me to take her...) " with dissolve
    mc "(My mind is full of these intrusive thoughts of just jumping on her and making her mine...) " with dissolve
    mc "(I’m so turned on I don’t even know how I’ll act next.)" with dissolve
    mc "(But I must control myself, I would never forgive myself if she hated me for doing something stupid.)" with dissolve
    pause
    mc "(Still...)" with dissolve
    scene ch9_492 with dissolve
    mc "(Maybe if I try, if I get closer and look into her eyes...)"
    mc "(-Maybe she'll let me do it...)" with dissolve
    pause
    a "{i}[mc], what are you doing?"
    a "[mc]."
    mc "(Even just once, I would settle for a single occasion...)" with dissolve
    mc "(I want to fuck her, having sex with my [arelat] is what I desire most...)" with dissolve
    scene ch9_496 with vpunch
    a "Wait, [mc], w-we can't."
    mc "I'm going to explode, [a]..."
    a "Yes, I know, baby, but..."
    a "How about we do that again?"
    mc "What do you mean, [arelat] [a]?"
    a "..."
    pause
    scene ch9_494 with dissolve
    a "Look at how you are..."
    pause
    a "You haven’t stopped being hard for a single second..."
    a "And it’s all because of this bikini. I didn’t realize it would cause us so many problems..."
    mc "Problems?"
    scene ch9_493 with dissolve
    a "Yes, big and hard problems..."
    mc "If these are problems, I hope life keeps treating me this badly..."
    a "..."
    pause
    a "I can use my mouth again... Would you like that?"
    mc "I would love that..."
    a "Alright..."
    pause
    scene ch9_490abj2_1 with dissolve
    pause
    mc "Oh, yeah..."
    jump beforech9_490abj2_

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_490abj2_(trans, st, at):  
        trans.set_child("ch9_490abj2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_490abj1_(trans, st, at):  
        trans.set_child("ch9_490abj1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.05:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_490abj3_(trans, st, at):  
        trans.set_child("ch9_490abj3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.05:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_490abj4_(trans, st, at):  
        trans.set_child("ch9_490abj4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.05:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_490abj5_(trans, st, at):  
        trans.set_child("ch9_490abj5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.05:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_490abj1_():
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
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_490abj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_490abj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_490abj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_490abj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_490abj2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"  
screen ch9_490abj2_():
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
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_490abj1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_490abj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_490abj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_490abj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_490abj2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_490abj3_():
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
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_490abj1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_490abj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_490abj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_490abj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_490abj2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_490abj4_():
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
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_490abj1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_490abj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_490abj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" action Jump("ch9_490abj5_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_490abj2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_490abj5_():
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
        textbutton "Fast" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 1" action Jump("ch9_490abj1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 2" action Jump("ch9_490abj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_490abj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 4" action Jump("ch9_490abj4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 5" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_490abj2_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label beforech9_490abj2_:
    image ch9_490abj1_:
        function ch9_490abj1_
    image ch9_490abj2_:
        function ch9_490abj2_
    image ch9_490abj3_:
        function ch9_490abj3_
    image ch9_490abj4_:
        function ch9_490abj4_
    image ch9_490abj5_:
        function ch9_490abj5_
    $ anim_speed = 0.03
    scene ch9_490abj2_ with dissolve
    mc "Oh, [arelat] [a]... *mmhm*"
    pause
    scene ch9_490abj1_ with dissolve
    a "*Hmm, slurp*"
    mc "So good, uh... *hmm*"
    pause
    scene ch9_468ahj1_ with dissolve
    $ anim_speed = 0.01
    a "I’m not very experienced..."
    a "Am I doing it right?"
    mc "Yes, it feels really good, [a]."
    a "Please, keep an eye out for anyone coming, [mc]."
    a "We’ve been here for a while and the girls must be wondering where we are."
    scene ch9_490abj1_ with dissolve
    $ anim_speed = 0.02
    mc "Yes, *uh* I'm...{w=0.5} watching."
    pause
    mc "(Oh man, she’s sucking it so good...)"
    mc "(And she doesn’t make any faces or signs of disgust, she really likes it.)"
    scene ch9_490abj3_ with dissolve
    mc "(Her tongue is gently moving around my glans...)"
    a "*Hmm, smnch, suck*"
    mc "(She’s such a classy woman that even when she’s giving head, she does it with grace...)"
    mc "(But every woman, no matter how refined, likes to feel desired, to be pleased...)"
    mc "(And that's why I'm here, I’ll make sure she feels desired every day.)"
    pause
    scene ch9_490abj4_ with dissolve
    mc "(I see a car approaching in the distance...)"
    mc "(I’d better not let [a] see it, or she’ll stop giving me head.)"
    mc "(They parked far away, so it doesn’t matter if I don’t tell her.)"
    pause
    jump ch9_490abj5_



label ch9_490abj1_:
    scene ch9_490abj1_ with dissolve
    call screen ch9_490abj1_ with dissolve
label ch9_490abj2_:
    scene ch9_490abj2_ with dissolve
    call screen ch9_490abj2_ with dissolve
label ch9_490abj3_:
    scene ch9_490abj3_ with dissolve
    call screen ch9_490abj3_ with dissolve
label ch9_490abj4_:
    scene ch9_490abj4_ with dissolve
    call screen ch9_490abj4_ with dissolve
label ch9_490abj5_:
    scene ch9_490abj5_ with dissolve
    call screen ch9_490abj5_ with dissolve


label afterch9_490abj2_:
    scene ch9_498 with dissolve
    pause 0.5
    scene ch9_497 with dissolve
    a "{i} A car, a car is approaching!"
    $ renpy.end_replay()
    stop music fadeout 0.5
    play music doing fadein 0.5
    play sound "audio/carengine.mp3" fadein 0.5 volume 0.5
    scene ch9_499 with dissolve
    pause
    scene ch9_500 with dissolve
    a "{i} It's stopped, [mc]! It's stopped!"
    a "It's backing up, they saw us!"
    scene ch9_501 with hpunch
    a "{i} Oh God! What do we do, what do we do?!"
    "Hey!"
    stop sound fadeout 1.5
    scene ch9_502 with dissolve
    mc "Y-yes, how can I help you?"
    mc "(Shit, now we’re in trouble!)" with dissolve
    "You do know THAT is not allowed here, right?"
    mc "Excuse me?"
    mc "(She saw us! We need to get out of here!)" with dissolve
    "The police are on their way, if I were you, I’d leave right now."
    mc "(Shit!)" with hpunch
    mc "We’re leaving, s-sorry, we didn’t mean to be seen, really."
    "Well, you were seen. I’m tired of everyone doing whatever they want."
    "Everyone comes to this town thinking they can do whatever they please, but there are rules here just like in the city."
    mc "We’re really sorry, we’re leaving, we truly didn’t mean to bother anyone."
    a "{i}{size=-3}Oh God, let’s go now, [mc]."
    "Is the car in front with you?"
    mc "The red car?"
    mc "N-no, we don’t know them."
    "I’ve told those in the red car several times that parking on the beach is not allowed and they don’t listen, I thought you were with them."
    "This area is part of the beach, you can’t drive cars here."
    "Move your car, there’s a parking lot a few streets away."
    mc "Ooh! (So that’s all it is, thank goodness!)"
    mc "W-we understand, we’re leaving!"
    "Sorry for using such a threatening tone, I asked those in the red car politely to leave and they started insulting me."
    mc "It's okay, thanks for letting us know!"
    "No problem, but move your car now, the police are on their way."
    scene ch9_503 with dissolve
    mc "That was close..."
    pause
    a "Did she leave?"
    mc "Yes."
    mc "I thought she had caught us."
    a "{i} My heart almost exploded, how embarrassing!"
    mc "She didn’t see us, she just came to let us know can't park here."
    pause
    mc "What nerve does she have to tell us to move when she also drove her car here?"
    a "She seemed to suspect something, I noticed her tone."
    mc "Really?"
    stop music fadeout 0.5
    play music scene1 fadein 0.5
    scene ch9_504 with dissolve
    mc "I didn’t notice... uh..."
    a "What’s wrong? Is something happening?"
    mc "Pfff!"
    mc "No wonder she suspected something, haha."
    a "Let’s go, [mc]!"
    scene ch9_505 with dissolve
    mc "She’s gone, you can take off the bag."
    a "No, I’m keeping it on until we’re far away."
    mc "Haha."
    scene ch9_506 with dissolve
    a "Start the car, [mc]!"
    mc "Let’s go back and thank her for warning us."
    a "No, let’s just leave!"
    mc "Haha."
    stop music fadeout 2.0
    stop background fadeout 3.0
    scene blackscreen with Dissolve(2.0)
    pause
    play background "audio/beachsfx.ogg" fadein 1.0 volume 0.35
    play music scene2 fadein 2.0
    scene ch9_505- with dissolve
    pause
    a "There’s no one here, right?"
    mc "No, [arelat] [a], we’re in a secluded place just like you said."
    scene ch9_505-- with dissolve
    mc "You can take off the bag now, haha."
    a "Are you sure? Take a look, maybe she followed us."
    mc "We’re completely alone here."
    scene ch9_505--- with dissolve
    a "That was really stupid, [mc]. What on earth were we thinking?"
    mc "Yeah, I know..."
    mc "But it was fun."
    a "It wasn’t fun at all, [mc]."
    a "In the end, we would have ended up on TV as perverts like we said earlier."
    mc "Haha, that would have been incredible."
    mc "Fortunately, it turned out to be just a funny story."
    a "Funny story?"
    a "What are you going to say? That you almost got caught with your [arelat] on the beach?"
    mc "Well..."
    scene ch9_505---- with dissolve
    a "..."
    pause
    mc "Come on, it wasn’t that bad."
    a "How can you say it wasn’t that bad? We could have ended up in jail."
    a "..."
    scene ch9_505----- with dissolve
    pause
    a "Now that I remember, there are some underwear in the trunk."
    mc "Yeah, speaking of that..."
    scene ch9_505---- with dissolve
    mc "I still have this erection and it felt really good when-"
    scene ch9_505--- with hpunch
    a "No, [mc], what’s wrong with you?"
    a "We almost went to jail for that and you want to keep going?"
    mc "Jail? Don’t you think you’re exaggerating a little?"
    a "I said no and that’s final!" with hpunch
    mc "Alright, alright, fine. I’ll get the underwear..."
    mc "(Wow, it’s been a while since I’ve seen [a] so angry.)" with dissolve
    a "No, I’ll go. We don’t want anyone to see you with that bulge."
    scene ch9_505------ with fade
    mc "And that towel?"
    a "To cover myself."
    a "I don't want to walk down the street in this small bikini."
    mc "I can get you a bigger bag if you want."
    mc "You know, like the one you had on your head earlier."
    a "*Giggle* Very funny..."
    a "Good luck finding one big enough for my butt."
    "*Laughter*"
    stop music fadeout 1.0
    stop background fadeout 3.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 3.0
    play background "audio/beachsfx.ogg" fadein 1.0 volume 0.75
    scene ch9_507 with dissolve
    mc "Back to the book."
    a "Yes."
    scene ch9_507- with dissolve
    a "We can’t be together, [mc], Someone might recognize us."
    mc "I’m sure no one saw us, [arelat] [a]."
    mc "You’re overreacting."
    scene ch9_508 with dissolve
    a "Just in case."
    a "Go with the girls, [mc]. For now, we can’t be together."
    mc "Okay..."
    scene ch9_509 with dissolve
    mc "[drelat!cl] [d] fell asleep."
    a "{i}{size=-2}Yes, let him rest for a while, so I can read my book in peace."
    scene ch9_511 with dissolve
    mc "Well, I’m going with the girls. I’ll leave you with the sleeping beauty."
    scene ch9_510 with dissolve
    mc "I love you."
    scene ch9_511 with dissolve
    a "I love you too."
    mc "I’ll see you in a while."
    scene blackscreen with dissolve
    pause
    scene ch9_514 with dissolve
    mc "(They’re taking photos again...)"
    pause
    scene ch9_515 with dissolve
    mia "Oh, I like this one!"
    k "Oh, look at this one."
    mia "Oh, wow!"
    mia "You really know how to take photos."
    k "Of course."
    mc "What’s up? What are you doing?"
    scene ch9_516 with dissolve
    k "Where were you?"
    mia "We were looking for you. Well, [k] was looking for you."
    k "Yeah, you disappeared."
    mc "I went with my [arelat] [a] to get some things from the car."
    scene ch9_517 with dissolve
    k "Take one like this for me."
    mia "Turn towards me."
    k "Move aside, [mc]."
    mc "Yes, sorry."
    scene ch9_518 with dissolve
    mia "Lift your chin more."
    k "Like this?"
    mia "Less... a little more. Stop, like that, like that!"
    pause
    k "Hurry up, my neck is getting tired."
    mia "I’m taking several."
    jump screollable_ch9_518
screen scrollable_ch9_519():
    default ypos = 0.0
    viewport id "vp":
        xpos 0
        ypos ypos
        draggable True
        add "ch9_519"
    vbox:
        align (0.95, 0.9)
        spacing 10
        textbutton "{size=+5}Continue" action Return() style "textbutton_choice"
label screollable_ch9_518:
    show screen scrollable_ch9_519 with dissolve
    while arrow_alpha < 1.0:
        $ arrow_alpha += 0.05 
        $ renpy.pause (0.005)  
    $ renpy.pause(0.0005)
    while arrow_alpha > 0.2:
        $ arrow_alpha -= 0.05
        $ renpy.pause(0.005) 
    mc "([k] looks really sexy...)"
    pause
    mc "(God... I want to fuck her so bad.)" with dissolve
    hide screen scrollable_ch9_519 with dissolve
    mia "Let’s see from this angle..."
    k "Already? I’m getting tired..."
    mia "Hold on!"
    pause
    scene ch9_520 with dissolve
    mc "Can I be in the photo?"
    k "No, move aside."
    mc "What? Can’t the boyfriend be in a photo with his girl?"
    scene ch9_521 with dissolve
    k "No, step aside, will you?"
    mc "Hey, why don’t we go somewhere together now that we can?"
    k "What the hell is wrong with you?"
    mc "{i}{size=-3}C'mon, [k], [drelat] [d] is naping."
    scene ch9_522 with dissolve
    k "Are you crazy? Stop bothering me."
    mia "What’s going on?"
    k "Stop it, [mc]. What's wrong with you?"
    scene ch9_522- with dissolve
    k "What the hell are you doing?"
    mc "[drelat!cl] [d] is asleep, we have at least an hour free from him."
    k "So?"
    mc "I was thinking we could make the most of the time alone, just you and me..."
    scene ch9_523 with dissolve
    k "Hey!"
    scene ch9_524 with dissolve
    mc "{i}Come on, [k], I’m so hot, come with me."
    k "N-no, [mc], don’t be stupid."
    mc "{i}{size=-2}I promise you'll love it."
    k "Are you on drugs or something?"
    mc "I’m high on love."
    k "Let go of me, idiot."
    scene ch9_525 with dissolve
    mia "Aww, poor thing."
    mia "He just wants to spend time with his girl."
    scene ch9_526 with dissolve
    k "Control your damn hormones or whatever is happening to you."
    mia "I wish [dereck] would look for me as desperately as [mc] is looking for you."
    mia "Love is such a beautiful thing..."
    scene ch9_527 with dissolve
    k "Stop encouraging him!"
    mia "He’s just so cute, haha."
    k "He’s not, he’s just being annoying."
    scene ch9_528 with dissolve
    mc "Jokes aside, should we do something?"
    



    k "Actually, [mia] and I were heading to the store to grab some beers."
    mc "Sounds good! I'll cover it."
    mc "Wait, [drelat] [d] is going to flip if he sees you drinking"
    k "Are you going to gossip to him?"
    mc "Of course not."
    k "So what’s the problem?"
    mc "I guess there isn't one."
    scene ch9_529 with dissolve
    mia "He looks for you, buys you things... [k], treat him well or he’s going to leave"
    k "Let him leave if he wants."
    mia "You’re bad, girl *giggles*."
    scene ch9_530 with dissolve
    k "Where are you going?"
    mc "Can’t I come with you?"
    k "No."
    k "You know why."
    k "But you can give me the money."
    mc "Hey, now I’m really feeling bad..."
    k "Oh, shut up! We’ll bring the stuff back here when we return."
    mc "Okay..."
    scene ch9_531 with dissolve
    pause
    mc "(Damn [k]...)"
    mc "(She’s showing off just because her friend is here.)" with dissolve
    pause
    image ch9_532zoom:
        "ch9_532" with dissolve
        subpixel True
        yalign 0.5 xalign 0.5 zoom 1.0
        ease 10 zoom 1.3
        ease 10 zoom 1.0
        repeat
    scene ch9_532zoom with dissolve
    pause
    mc "(If it weren’t for those tits and that ass, I’d tell her to screw off.)" with dissolve
    stop music fadeout 1.5
    stop background fadeout 3.0
    scene blackscreen with dissolve
    pause
    play background "audio/beachsfx.ogg" fadein 1.5 loop volume 1.0 
    play music scene2 fadein 3.0
    scene ch9_512 with dissolve
    s "[mc]!"
    mc "Hey, you know how to surf."
    s "Yes!"
    s "Well, yes and no."
    s "I can surf, but only on my belly."
    mc "On your belly?"
    s "Yes, I lie on the board and can surf."
    mc "Oh, I want to see that."
    scene ch9_513 with dissolve
    s "Do you want me to teach you?"
    s "But it's a bit difficult, it might not work out on the first try."
    mc "No problem, can I try too?"
    s "Yes, but don’t be sad if it doesn’t work out on the first try, okay?"
    if stephloving == "True":
        scene ch9_517- with dissolve
        mc "Sure."
        scene ch9_517- with dissolve:
            subpixel True
            xalign 0.5 yalign 0.5 
            ease 3 yalign 0.8 zoom 1.1
        mc "(What a cute little butt...)" with dissolve
        pause
    scene ch9_519- with fade
    s "You have to wait for a wave to come, and then just hold on to the boogie board."
    mc "Got it."
    s "And you need balance so you don’t fall sideways, but it’s easy."
    s "Even you can surf like this, it’s not that hard."
    mc "(what do you mean even me?)" with dissolve
    s "Watch how I do it."
    image ch9_519anim:
        "ch9_519--" with dissolve
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.0
        ease 20 zoom 1.3
        ease 20 zoom 1.0
        repeat
    if stephloving == "True":
        scene ch9_519anim with dissolve
        pause
        mc "(Such cute butt cheeks...)" with dissolve
        mc "(Maybe I could...)" with dissolve
        mc "(No, forget about that [mc]. You’re so hot that you’re starting to think crazy things...)" with dissolve
    scene ch9_519--- with dissolve
    s "Yay! Look, [mc]!"
    mc "I’m watching you, haha."
    stop music fadeout 1.5
    stop background fadeout 3.0
    scene blackscreen with dissolve
    centered "{size=+5}You play around with [s] in the water for a while..."
    play background "audio/beachsfx.ogg" fadein 1.0
    play music scene2 fadein 2.0
    scene ch9_516- with dissolve
    s "Now let’s go deeper, okay?"
    mc "I’m tired, [s]..."
    mc "How about we go for a walk instead?"
    s "Yes, let’s explore the beach!"
    mc "Let’s go."
    scene ch9_519---- with dissolve
    s "I’ll take you to a secret place I found!"
    s "It’s a very secret place, and there are lots of crabs."
    mc "Oh, really?"
    s "Yes, but they don’t do anything, they’re harmless."
    scene ch9_533 with dissolve
    s "There are also seagulls, and they fight with the crabs."
    mc "That’s wild."
    mc "And why do they fight?"
    s "I don’t know, I didn’t ask them."
    s "Do you also talk to animals?"
    mc "Uh... yes, sometimes. Do you too?"
    s "Yep{w=0.25}, but they don’t understand me."
    mc "Haha."
    s "Well, I don’t understand them either, but I still talk to them sometimes, haha."
    mc "I talk too, not just to animals, but to anything."
    mc "Sometimes I just want someone to listen."
    scene ch9_534 with dissolve
    s "You can talk to me whenever you want, [mc]."
    mc "Thanks, [s]. I know."
    s "Did you know that [arelatks] talks to the pigeons?"
    mc "Really?"
    s "Yes, I saw her talking to one the other day."
    mc "And what was she saying?"
    s "I don’t remember."
    s "We’re almost there."
    scene ch9_535 with dissolve
    s "Look, it’s over there, behind those big rocks!"
    s "But be careful with the crabs because if you step on them, they can bite you with their pincers."
    mc "Yes, I’ll be careful."
    scene ch9_536 with dissolve
    s "We need to jump over these rocks, but if you can’t, I’ll help you, don’t worry."
    mc "I can, I’m a big guy too."
    s "You’re big but a bit silly."
    mc "Haha."
    pause
    mc "You’re not serious about that, are you?"
    if stephloving == "True":
        scene ch9_538 with dissolve
        s "Hmmm, no..."
        mc "(I can’t stop looking at this little butt...)" with dissolve
        pause
        scene ch9_539 with dissolve
        mc "(Not even these boxers can completely hide the erection I have.)" with dissolve
        pause
    s "Look, [mc], there are many seagulls."
    scene ch9_536 with dissolve
    mc "Let me see."
    s "They’re over there, fighting with the crabs like I told you."
    s "Poor things, I’m going to defend them."
    mc "Wow, there are so many..."
    s "Let’s scare them away."
    scene ch9_537 with dissolve
    s "!Hey! Hey...!"
    stop music fadeout 0.25
    play music something fadein 0.25
    play sound "audio/seagulls.ogg" fadein 1.0 volume 0.5 loop 
    scene ch9_540 with vpunch
    s "KYAAA! The seagulls are attacking us!"
    mc "WAAAAH!"
    scene ch9_541 with dissolve
    s "Come back, you cowards! Don’t run away!"
    "You’re just a bunch of featherbrains!"
    pause
    stop sound fadeout 10.0
    scene ch9_542 with dissolve
    s "Stupid seagulls...."
    s "They think they’re better than pigeons, but they’re the ugliest birds."
    s "I’ve never liked those ugly, thieving birds."
    stop music fadeout 1.5
    scene blackscreen with dissolve
    s "[mc], why are you curled up like that?"
    mc "Are they gone?"
    play music scene3 fadein 1.0
    scene ch9_543 with flash
    s "They’re gone, don’t worry. I scared them all away."
    mc "Uh... T-thanks."
    mc "(She’s like an angel...)" with dissolve
    pause
    scene ch9_544 with dissolve
    s "Are you okay? Did they peck you?"
    mc "I’m fine."
    s "Are you sure? I can ask [drelatks] to take you to the doctor."
    scene ch9_545 with dissolve
    mc "No, haha, I’m fine, really."
    s "Poor thing, they made you scream like a little girl."
    mc "I hope no one heard me..."
    if stephloving == "True":
        scene ch9_546 with dissolve
    mc "I was supposed to be the one protecting you, haha."
    s "Wait, what’s that on your back?"
    mc "Where?"
    s "On your back."
    scene ch9_547 with dissolve
    mc "Huh?"
    s "Eeeww, it’s poop."
    mc "Really?"
    s "Yeah, the seagulls pooped on your back."
    scene ch9_548 with dissolve
    mc "Ugh! Gross!"
    pause
    stop music fadeout 1.0
    scene ch9_549 with fade
    play music scene2 fadein 1.5
    s "Look, [mc], there are so many crabs."
    s "There weren’t this many earlier."
    mc "Be careful, they pinch hard with their claws."
    s "Yeah, I know."
    scene ch9_551 with dissolve
    mc "This place is nice."
    s "Isn’t it?"
    s "The best part is that it’s a place only we know about."
    mc "That’s great."
    if stephloving != "True":
        jump ch9_621sskip
label ch9s7:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
        play music scene3 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_552 with dissolve
    s "N-no one ever comes here..."
    s "Uhmm..."
    pause
    scene ch9_553 with dissolve
    mc "Hmm?"
    s "I wanted to ask you something, but..."
    s "But I know you’re going to say no..."
    mc "What is it?"
    s "Uhm..."
    scene ch9_552 with dissolve
    s "First say yes, and then I’ll tell you."
    mc "How can I say yes if you won’t tell me what it is?"
    scene ch9_553 with dissolve
    s "It’s just that I wanted you and me to..."
    pause
    scene ch9_554 with dissolve
    s "Forget it."
    mc "No, tell me."
    scene ch9_555 with dissolve
    s "You won’t want to..."
    mc "You won’t know unless you ask me."
    s "..."
    pause
    play music scene3 fadein 1.5
    scene ch9_557 with dissolve
    mc "Tell me! Nom, nom."
    s "I don’t want to. *te-he*"
    scene ch9_556 with dissolve
    mc "Nom, nom, I’ll eat you if you don’t tell me."
    s "No, haha."
    mc "(She’s so cute, I just want to squish her like a plush toy...)" with dissolve
    scene ch9_564 with dissolve
    s "Te-he, that tickles, [mc]."
    pause
    scene ch9_565 with dissolve
    s "Ah, te-he."
    s "Stop! Te-he-he."
    scene ch9_558 with dissolve
    mc "Aren’t you going to tell me?"
    s "Hmm, nope!"
    scene ch9_556 with vpunch
    s "Kyaa!"
    mc "Nom, nom, nom."
    scene ch9_560 with dissolve
    mc "Then I’m going to eat your cheeks."
    s "Kyaa! Don’t bite my cheeks, it tickles, haha."
    pause
    scene ch9_561 with dissolve
    mc "(Her skin is so soft...)" with dissolve
    pause
    scene ch9_562 with dissolve
    pause
    scene ch9_563-- with dissolve
    pause
    scene ch9_563- with dissolve
    pause
    image ch9_563anim:
        "ch9_562" with dissolve
        1.5
        "ch9_563--" with dissolve
        1.5
        "ch9_563-" with dissolve
        1.5
        repeat
    scene ch9_563anim with dissolve
    mc "(She knows exactly what's happening here, she acts innocent, but she’s a total pervert.)" with dissolve
    mc "(And that makes her even sexier...)" with dissolve
    mc "(She loves it when I touch her all over...)" with dissolve
    mc "(She’s always liked being pampered all the time...)" with dissolve
    s "{i}Has the pervy shark returned?"
    mc "Yes, nom nom!"
    s "{i}{size=-1}Nooo, te-he."
    pause
    scene ch9_563---- with dissolve
    s "Uh... hm..."
    scene ch9_563--- with dissolve
    s "N-no, don’t eat me... *Uhm*"
    image ch9_563anim2:
        "ch9_563----" with dissolve
        1.5
        "ch9_563---" with dissolve
        1.5
        repeat
    scene ch9_563anim2 with dissolve
    s "*Uh, hmm*"
    mc "(I can feel how wet she’s getting, she definitely loves it when I touch her...)" with dissolve
    pause
    s "*Hmm, uhmm, hm* Don’t stop touching me there..."
    mc "Do you like it?"
    s "Yes... *uh, hmm* I love it when the shark runs its fin over me."
    scene ch9_563----- with dissolve
    mc "Does my fin feel good?"
    scene ch9_563------ with dissolve
    s "Y-yes... *hmm, hm*"
    image ch9_563panim:
        "ch9_563-----" with dissolve
        1.5
        "ch9_563------" with dissolve
        1.5
        repeat
    scene ch9_563panim with dissolve
    s "*Uh, hmm, uhm*"
    pause
    s "Kiss me, [mc]..."
    scene ch9_571 with dissolve
    mc "W-wait, let’s make sure no one’s coming."
    s "No one’s coming, [mc]."
    scene ch9_564 with dissolve
    s "Te-he, hehehe."
    scene ch9_565 with dissolve
    s "W-wait, [mc], hehehe, that tickles a lot."
    mc "I’m going to eat you all up."
    image ch9_565animds:
        "ch9_564" with dissolve
        1.75
        "ch9_565" with dissolve
        1.75
        repeat
    scene ch9_565animds with dissolve
    pause
    scene ch9_566 with dissolve
    s "Stop, wait, [mc]. Or else, I’m going to eat you."
    mc "Oh, really?"
    scene ch9_567 with dissolve
    mc "{i}No one beats the gluttonous shark!"
    s "{i}Kyaaah! Hehehe."
    scene ch9_568 with dissolve
    s "Nom, nom!"
    mc "Haha. (She’s so cute...)"
    pause
    scene ch9_569 with dissolve
    s "Kiss me, [mc]..."
    scene ch9_570 with dissolve
    s "*Mummh*"
    scene ch9_572 with dissolve
    mc "(We’re alone, so it’s fine if we kiss for a bit...)" with dissolve
    pause
    play sound kissing fadein 0.5 volume 0.5 loop
    scene ch9_573 with dissolve
    s "*Hmh, smnch, muhl*"
    mc "(She always kisses me with tongue...)" with dissolve
    pause
    stop sound fadeout 0.5
    scene ch9_574 with dissolve
    s "*Mwah* Your kisses feel so good, [mc]."
    s "Do mine feel good too?"
    mc "Yeah, your lips are really delicious."
    play sound kissing fadein 0.5 volume 0.5 loop
    scene ch9_573 with dissolve
    s "*Smnch, mlah, lhmh*"
    stop sound fadeout 0.5
    scene ch9_574 with dissolve
    s "*Mwah*"
    s "Did you know that we're already doing what I was going to tell you before?"
    mc "Ahh... So you wanted kisses."
    s "Yup, and we're already doing it, hehe."
    mc "What if I told you I already knew?"
    s "Really?"
    s "You're just as perverted as I am, hehehe."
    stop music fadeout 2.0
    play sound kissing fadein 0.5 volume 0.5 loop
    scene ch9_573 with dissolve
    play music sexy3 fadein 1.5
    pause
    scene ch9_575 with dissolve
    s "*Hmsh, schlk, smnch*"
    pause
    scene ch9_576 with dissolve
    s "*Lhm, hmm, smnch*"
    pause
    image ch9_576anim:
        "ch9_575" with dissolve
        1.2
        "ch9_576" with dissolve
        1.2
        repeat
    scene ch9_576anim with dissolve
    s "*Hmph, shmnch*"
    mc "*Hmh* (She’s so intense when kissing, her tongue explores my mouth very aggressively.)" with dissolve
    pause
    scene ch9_576- with dissolve
    pause
    scene ch9_576-- with dissolve
    pause
    image ch9_576anim2:
        "ch9_576-" with dissolve
        1.2
        "ch9_576--" with dissolve
        1.2
        repeat
    scene ch9_576anim2 with dissolve
    s "*Hmhp, shmh, smonch*"
    pause
    image ch9_575animated:
        "ch9_575" with dissolve
        1.2
        "ch9_576" with dissolve
        1.2
        "ch9_577" with dissolve
    scene ch9_575animated with dissolve
    $ renpy.pause(2.4, hard=True)
    mc "*Hmhm*"
    pause
    stop sound fadeout 0.5
    scene ch9_579 with dissolve
    mc "(We better move behind the rock, just in case someone sees us from afar.)"
    pause
    s "What are you looking at?"
    scene ch9_578 with dissolve
    mc "Nothing, I was just making sure no one’s coming."
    s "Let’s keep kissing, okay?"
    play sound kissing fadein 0.5 volume 0.5 loop
    scene ch9_578- with dissolve
    pause
    scene ch9_578-- with dissolve
    s "*Lalh, lhmh, lhm*"
    pause
    stop sound fadeout 0.5
    scene ch9_580 with dissolve
    play sound kissing2 fadein 0.5 volume 0.25 loop
    pause
    stop sound fadeout 0.5
    scene ch9_581 with dissolve
    play sound kissing2 fadein 0.5 volume 0.5 loop
    pause
    scene ch9_582 with dissolve
    pause
    scene ch9_583 with dissolve
    pause
    scene ch9_584 with dissolve
    pause
    scene ch9_584- with dissolve
    pause
    scene ch9_584-- with dissolve
    pause
    scene ch9_584--- with dissolve
    pause
    scene ch9_584---- with dissolve
    pause
    #
    scene ch9_585 with dissolve
    pause
    scene ch9_586 with dissolve
    pause
    scene ch9_587 with dissolve
    pause
    scene ch9_588 with dissolve
    pause
    scene ch9_589 with dissolve
    pause
    scene ch9_590 with dissolve
    pause
    scene ch9_591 with dissolve
    pause
    scene ch9_592 with dissolve
    pause
    $ anim_speed = 0.9
    image ch9_584anim1:
        "ch9_581" with Dissolve(0.4)
        anim_speed-(anim_speed/6)
        "ch9_582" with Dissolve(0.3)
        anim_speed-(anim_speed/5)
        "ch9_583" with Dissolve(0.4)
        anim_speed
        "ch9_584" with Dissolve(0.4)
        anim_speed
        "ch9_582" with Dissolve(0.4)
        anim_speed
        "ch9_583" with Dissolve(0.4)
        anim_speed
        "ch9_584" with Dissolve(0.4)
        anim_speed
        "ch9_584-" with Dissolve(0.4)
        anim_speed-(anim_speed/6)
        "ch9_584--" with Dissolve(0.3)
        anim_speed-(anim_speed/5)
        "ch9_584---" with Dissolve(0.4)
        anim_speed
        "ch9_584----" with Dissolve(0.4)
        anim_speed
        "ch9_584---" with Dissolve(0.4)
        anim_speed
        "ch9_584----" with Dissolve(0.4)
        anim_speed
        repeat
    image ch9_584anim2:
        "ch9_585" with Dissolve(0.4)
        anim_speed-(anim_speed/6)
        "ch9_586" with Dissolve(0.3)
        anim_speed-(anim_speed/5)
        "ch9_587" with Dissolve(0.4)
        anim_speed
        "ch9_588" with Dissolve(0.4)
        anim_speed
        "ch9_586" with Dissolve(0.4)
        anim_speed
        "ch9_587" with Dissolve(0.4)
        anim_speed
        "ch9_588" with Dissolve(0.4)
        anim_speed
        "ch9_589" with Dissolve(0.4)
        anim_speed-(anim_speed/6)
        "ch9_590" with Dissolve(0.3)
        anim_speed-(anim_speed/6)
        "ch9_591" with Dissolve(0.4)
        anim_speed-(anim_speed/6)
        "ch9_592" with Dissolve(0.4)
        anim_speed
        "ch9_591" with Dissolve(0.4)
        anim_speed
        "ch9_592" with Dissolve(0.4)
        anim_speed
        repeat
    scene ch9_584anim1 with dissolve
    call screen ch9_584anim1 with dissolve
screen ch9_584anim1():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 1.3), Jump("ch9_584anim1")] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.8), Jump("ch9_584anim1")] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.5), Jump("ch9_584anim1")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" action Jump("ch9_584anim2") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_584anim2continue") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_584anim2():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action [SetVariable("anim_speed", 1.3), Jump("ch9_584anim2")] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action [SetVariable("anim_speed", 0.8), Jump("ch9_584anim2")] style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action [SetVariable("anim_speed", 0.5), Jump("ch9_584anim2")] style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 1" action Jump("ch9_584anim1") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_584anim2continue") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label ch9_584anim1:
    scene ch9_584anim1 with dissolve
    call screen ch9_584anim1 with dissolve
label ch9_584anim2:
    scene ch9_584anim2 with dissolve
    call screen ch9_584anim2 with dissolve

label ch9_584anim2continue:
    $ anim_speed = 0.5
    image ch9_584anim3:
        "ch9_585" with Dissolve(0.3)
        anim_speed-(anim_speed/4)
        "ch9_586" with Dissolve(0.2)
        anim_speed-(anim_speed/3)
        "ch9_587" with Dissolve(0.3)
        anim_speed
        "ch9_588" with Dissolve(0.3)
        anim_speed
        "ch9_586" with Dissolve(0.3)
        anim_speed
        "ch9_587" with Dissolve(0.3)
        anim_speed
        "ch9_588" with Dissolve(0.3)
        anim_speed
        "ch9_589" with Dissolve(0.3)
        anim_speed-(anim_speed/4)
        "ch9_590" with Dissolve(0.2)
        anim_speed-(anim_speed/4)
        "ch9_591" with Dissolve(0.3)
        anim_speed-(anim_speed/4)
        "ch9_592" with Dissolve(0.3)
        anim_speed
        "ch9_593" with dissolve
    scene ch9_584anim3 with dissolve
    $ renpy.pause(4.5, hard=True)
    stop sound fadeout 0.5
    play voicefx "audio/character/s/soft/s_moan_soft_1.ogg" fadein 0.1
    s "Blahh..."
    pause
    play sound kissing2 fadein 0.5 loop volume 0.5
    scene ch9_597 with dissolve
    s "*Hahl*"
    scene ch9_598 with dissolve
    s "*Lhalh*"
    image ch9_597anim:
        "ch9_597" with dissolve
        1.5
        "ch9_598" with dissolve
        1.5
        repeat
    scene ch9_597anim with dissolve
    s "*Mahl, lahm, halh*"
    mc "(Damn, her taste is so intoxicating...)"
    mc "(The amount of saliva in my mouth is totally obscene.)"
    pause
    scene ch9_596 with dissolve
    s "*Hhml* Hmm.. [mc]..."
    mc "(This is way too lewd...)"
    pause
    stop sound fadeout 0.5
    scene ch9_579 with dissolve
    pause
    scene ch9_594 with dissolve
    pause
    stop sound fadeout 0.5
    scene ch9_594- with dissolve
    pause
    s "{size=-3}{i}Awww..."
    mc "{size=-3}{i}Let me rest my arms for a second."
    s "{size=-3}{i}Did my spit gross you out?"
    scene ch9_599 with dissolve
    mc "Of course not."
    mc "It's just that my arms are tired."
    s "I’m getting heavier. [k] says my butt got bigger, hehe."
    mc "Your butt is fine, don’t listen to her."
    mc "(What a naughty look on her face... and those big eyes that keep staring at me...)" with dissolve
    mc "(She's so beautiful...)" with dissolve
    mc "(I knew what was happening, bringing me here alone, then the kisses... This was her plan.)" with dissolve
    s "[mc]?"
    mc "Sorry, I got lost in my thoughts."
    s "What were you thinking about?"
    mc "Nothing, I just felt something get hard in my pants..."
    s "You're talking about your dick, right?"
    mc "Yeah, I think so."
    scene ch9_602 with dissolve
    mc "It got really hard and it hurts..."
    s "Hmm..."
    s "Does it hurt a lot?"
    scene ch9_600 with dissolve
    mc "Yeah... Your kisses really turned me on."
    s "Hmm, and I don’t have my hat with me to cover it when we leave."
    mc "Really? Hmm, that's bad..."
    pause
    scene ch9_603 with dissolve
    s "Hmm..."
    pause
    mc "I-I was thinking maybe you could, do that again..."
    scene ch9_604 with dissolve
    mc "Will you suck it for me?"
    s "With my mouth?"
    s "Uhm, yeah..."
    s "But we're at the beach."
    mc "Eh, yeah, heh..."
    mc "(You know you've really lost it when the voice of reason comes from [s].)" with dissolve
    scene ch9_603 with dissolve
    pause
    scene ch9_604 with dissolve
    s "You really want me to suck it, don’t you?"
    scene ch9_605 with dissolve
    s "{i}We can do it in secret!"
    mc "{i}Good idea!"
    s "No one comes here anyway."
    s "Alright, I’ll suck it for you."    
    scene ch9_606 with dissolve
    s "But on one condition..."
    s "You have to suck my pussy too."
    mc "Of course, I love doing it."
    scene ch9_605 with dissolve
    s "Deal, hehe."
    scene ch9_607 with dissolve
    s "Alright, pull down your shorts."
    mc "Wait, let me check to make sure no one's coming."
    pause
    scene ch9_608 with dissolve
    s "Oh! It bounced on my face, hehe."
    mc "H-hey..."
    s "No one's coming, remember this is a secret spot."
    mc "You're such an impatient girl."
    pause
    scene ch9_610_-- with dissolve
    s "Ooh, it's really swollen today."
    s "The bigger it gets, the harder it gets too, right?"
    mc "Yeah."
    mc "When it gets really big and hard, it means I like that person a lot."
    scene ch9_610_- with dissolve
    s "*Hmch*, ¿really?"
    mc "Yeah, my dick gets really hard when I'm with you."
    s "*Smnch, smhm, smnch* I'm going to cover it with kisses first."
    mc "Yeah... *hmh*"
    mc "*Hmmh* I love kisses..."
    s "It's throbbing a lot. *Hmch, smnch, mhwa*"
    scene ch9_610_ with dissolve
    mc "Put it in your mouth..."
    s "*Lhl, lhm*"
    pause
    scene ch9_612- with dissolve
    s "*Hmmph*"
    pause
    jump beforech9_612sbja_

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_612sbja_(trans, st, at):  
        trans.set_child("ch9_612sbja_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_612sbj00_(trans, st, at):  
        trans.set_child("ch9_612sbj00_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_612sbj01_(trans, st, at):  
        trans.set_child("ch9_612sbj01_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_612sbj02_(trans, st, at):  
        trans.set_child("ch9_612sbj02_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_612sbj03_(trans, st, at):  
        trans.set_child("ch9_612sbj03_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_612sbj05_(trans, st, at):  
        trans.set_child("ch9_612sbj05_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_612sbj04_(trans, st, at):  
        trans.set_child("ch9_612sbj04_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_612sbj00_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch9_612sbja_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch9_612sbj01_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch9_612sbj02_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch9_612sbj03_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch9_612sbj05_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch9_612sbj04_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_612sbja_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" action Jump("ch9_612sbj00_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch9_612sbj01_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch9_612sbj02_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch9_612sbj03_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch9_612sbj05_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch9_612sbj04_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_612sbj01_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" action Jump("ch9_612sbj00_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch9_612sbja_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch9_612sbj02_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch9_612sbj03_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch9_612sbj05_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch9_612sbj04_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_612sbj02_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" action Jump("ch9_612sbj00_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch9_612sbja_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch9_612sbj01_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3"  style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch9_612sbj03_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch9_612sbj05_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch9_612sbj04_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_612sbj03_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" action Jump("ch9_612sbj00_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch9_612sbja_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch9_612sbj01_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch9_612sbj02_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch9_612sbj05_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch9_612sbj04_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_612sbj04_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" action Jump("ch9_612sbj00_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch9_612sbja_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch9_612sbj01_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch9_612sbj02_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch9_612sbj03_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" action Jump("ch9_612sbj05_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_612sbj05_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 0" action Jump("ch9_612sbj00_") style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 1" action Jump("ch9_612sbja_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 2" action Jump("ch9_612sbj01_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 3" action Jump("ch9_612sbj02_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 4" action Jump("ch9_612sbj03_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 5" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 6" action Jump("ch9_612sbj04_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_612sbj00_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label beforech9_612sbja_:
    image ch9_612sbja_:
        function ch9_612sbja_
    image ch9_612sbj00_:
        function ch9_612sbj00_
    image ch9_612sbj01_:
        function ch9_612sbj01_
    image ch9_612sbj02_:
        function ch9_612sbj02_
    image ch9_612sbj03_:
        function ch9_612sbj03_
    image ch9_612sbj04_:
        function ch9_612sbj04_
    image ch9_612sbj05_:
        function ch9_612sbj05_
    $ anim_speed = 0.03
    scene ch9_612sbja_ with dissolve
    mc "Oh... that's it, lick the tip really well..."
    s "*Hmph, slrp, suck*"
    pause
    mc "(I can't believe I'm doing this...)" with dissolve
    mc "(Letting my little [srelat] suck my dick in a public place... Today I’ve definitely fallen one step lower...)" with dissolve
    mc "(But damn, this feels incredibly good.)" with dissolve
    mc "(I love the feeling of her little lips around my head, and her tongue fluttering around my cock.)" with dissolve
    pause
    scene ch9_612sbj01_ with dissolve
    mc "Are you touching yourself?"
    s "*Hmch, shlp* U-hum..."
    mc "(That's the only reason I agree to these things, because she really enjoys doing it...)" with dissolve
    mc "(That makes it less inappropriate, right?…)" with dissolve
    pause
    mc "(Anyway, it’s ridiculous to keep having these dilemmas. I've given in so many times that I can't keep being a hypocrite with myself.)" with dissolve
    mc "Oh, just like that, uh..." with dissolve
    pause
    scene ch9_612sbj02_ with dissolve
    mc "(This feels so good, but I need to make sure no one comes...)" with dissolve
    mc "(I can’t let my guard down, we’re still in a public place, so I need to stay alert.)" with dissolve
    s "*Hmch, schlp, schlp*"
    mc "(But it’s hard when I’m feeling so much pleasure...)" with dissolve
    pause
    mc "Uh... [s], you've gotten really good at this."
    s "*Shlrp, schlp* Hhm, hmm..."
    pause
    scene ch9_612sbj03_ with dissolve
    mc "Keep using your tongue."
    s "*Shlrp, shlp, schkl*"
    mc "Just like that, oh... *hmhh*"
    pause
    scene ch9_612sbj05_ with dissolve
    mc "*Hmgh* Uh, [s], if you suck it that hard I'll..."
    mc "*Hmhh*"
    mc "Uh, suck it harder..."
    s "*Slrp, schlrp, shlrp*"
    mc "Oh, *hmmh* good girl..."
    pause
    scene ch9_612sbj04_ with dissolve
    call screen ch9_612sbj04_ with dissolve
define ch9_612at = "False"
label ch9_612sbj00_:
    $ ch9_612at = "False"
    scene ch9_612sbj00_ with dissolve
    call screen ch9_612sbj00_ with dissolve
label ch9_612sbja_:
    $ ch9_612at = "True"
    scene ch9_612sbja_ with dissolve
    call screen ch9_612sbja_ with dissolve
label ch9_612sbj01_:
    $ ch9_612at = "False"
    scene ch9_612sbj01_ with dissolve
    call screen ch9_612sbj01_ with dissolve
label ch9_612sbj02_:
    $ ch9_612at = "False"
    scene ch9_612sbj02_ with dissolve
    call screen ch9_612sbj02_ with dissolve
label ch9_612sbj03_:
    $ ch9_612at = "False"
    scene ch9_612sbj03_ with dissolve
    call screen ch9_612sbj03_ with dissolve
label ch9_612sbj04_:
    $ ch9_612at = "False"
    scene ch9_612sbj04_ with dissolve
    call screen ch9_612sbj04_ with dissolve
label ch9_612sbj05_:
    $ ch9_612at = "False"
    scene ch9_612sbj05_ with dissolve
    call screen ch9_612sbj05_ with dissolve


    
label afterch9_612sbj00_:
    if ch9_612at == "False":
        scene ch9_612sbja_ with dissolve
    mc "*Mngh* Go a little faster."
    $ anim_speed = 0.0084
    s "*Slrp, shlk, hmslp*"
    mc "Oh... this feels so good."
    mc "A-almost there... *hmngh* [s], the cum is about to come out..."
    mc "(Other girls back away immediately when they hear 'cum' during a blowjob, but not her.)" with dissolve
    mc "(It almost seems like her intention is to make me finish in her mouth...)" with dissolve
    pause
    k "[mc]!"
    scene ch9_613 with hpunch
    s "*Gasp* Hmh."
    mc "(That was [k]! They're looking for me.)" with dissolve
    mc "{i}Shh..."
    mc "(Damn, I completely forgot! I was supposed to wait for them where we were.)" with dissolve
    mc "(Right, behind the rock at my back is where they were taking pictures earlier.)" with dissolve
    pause
    scene ch9_614 with dissolve
    pause
    play voicefx "audio/wavs/bjgags3.ogg" volume 0.5 
    scene ch9_615 with dissolve
    mc "*Hmhm* {i}Uh..."
    mc "(Damn, she hasn't taken my dick out of her mouth this whole time...)" with dissolve
    pause
    scene ch9_616 with dissolve
    s "*Guh*"
    pause
    play voicefx "audio/wavs/bjgags8.ogg" volume 0.5
    scene ch9_617 with dissolve
    s "*Gugh, hmmph*"
    image ch9_617anim:
        "ch9_616" with dissolve
        2
        "ch9_617" with dissolve
        2
        repeat
    scene ch9_617anim with dissolve
    s "*Hmph, guhg, buhg*"
    mc "{i}Hmmh... (Even at a time like this, she keeps sucking and trying to go deeper...)" with dissolve
    k "{i}{size=-2}Where could he be?"
    mia "{i}{size=-2}Didn't he say he'd wait for us here?"
    mc "(They're getting closer.)"
    pause
    scene ch9_618 with dissolve
    s "Hmwah... {i}{size=-2}I can't go that deep."
    mc "{i}{size=-2}Shhh, keep sucking..."
    scene ch9_612sbj04_ with dissolve
    k "[mc]!"
    mia "{i}{size=-2}Maybe he went to get something."
    k "{i}{size=-2}They're going to get cold if he doesn't hurry."
    scene ch9_612sbj00_ with dissolve
    mc "{i}Uh... A-almost there.. {/i}*¡nhgh!*"
    pause
    mia "{i}{size=-2}Why don't we wait for him here?"
    k "{i}{size=-2}Yeah, he'll be here soon."
    mia "{i}{size=-2}What if he got mad because we left him alone?"
    k "{i}{size=-2}Nah, he never gets mad. I'm going to be mad at him now when he comes, for not staying where we told him to."
    mia "{i}{size=-2}Haha, it’s so funny when you two fight."
    mc "(It's coming, I can feel it)... *¡hmgh!*"
    pause
    jump ch9_621noskip
label ch9_621sskip:
    $ renpy.end_replay()
    scene ch9_622 with dissolve
    k "Hey, what are you doing here?"
    s "[mc]'s not here!"
    k "What are you talking about? I can see him."
    s "This is a private spot!"
    k "The beach is for everyone, what are you hiding?"
    jump ch9_621cont

label ch9_621noskip:
    stop music fadeout 0.5
    play music doing fadein 0.2
    scene ch9_620 with hpunch
    mc "Waaaaah!!!"
    s "Kyaaaa!"
    $ renpy.end_replay()
    mia "{size=-2}{i}Was that [mc] and [s]?"
    k "{i}[mc]?"
    stop music fadeout 0.5
    scene ch9_621- with dissolve
    play music scene2 fadein 0.5
    k "Hey, what are you doing here?"
    s "[mc]'s not here!"
    k "What are you talking about? I can see him."
    s "This is a private spot!"
    k "The beach is for everyone, what are you hiding?"
    mc "Ouch, damn... These little bastards sure pinch hard."
    stop music fadeout 1.0
    scene ch9_622 with dissolve
    play music scene1 fadein 1.0
    k "Didn't you hear us calling for you?"
    mc "No, ouch, I was playing with [s]."
    k "And why were you screaming?"
    s "[mc] got bitten by a crab."
    k "How are you going to scream like that over a stupid crab?"
    s "{i}'How ire yii giing ti scriim liki thit ivir a stipid crib?'{/i}"
    s "For your information, crabs have a lot of strength in their claws."
    jump ch9_621cont
label ch9_621cont:
    mia "Woah, look how many crabs there are! And they're big."
    mia "This place is nice, huh."
    k "Yeah, I like it too."
    scene ch9_623 with dissolve
    k "Hand me the towel."
    mia "Here you go."
    k "Lift your ass, [mc], I’m not sitting on the sand."
    scene ch9_624 with dissolve
    pause
    mia "One for Prince Charming."
    scene ch9_625 with dissolve
    mia "And one for Snow White."
    k "And you, which of the seven dwarfs are you?"
    mia "I’m the mirror giving advice to the old witch."
    k "Ha-ha..."
    k "Do you have something to open it?"
    mia "Of course."
    scene ch9_626 with dissolve
    k "Hey..."
    pause
    scene ch9_627 with dissolve
    mia "Here you go."
    mc "Cool."
    k "You're going to break your teeth..."
    scene ch9_628 with dissolve
    mc "Hey, [mia], can you open mine?"
    mia "Sure."
    scene ch9_629 with dissolve
    k "Wait!"
    mia "What?"
    scene ch9_630 with dissolve
    k "Give me that."
    mia "Yeah, wouldn't want to give him an indirect kiss..."
    k "A what kiss?"
    scene ch9_631 with dissolve
    pause
    k "It's a twist-off cap."
    scene ch9_632 with dissolve
    k "Here."
    mc "Uh..."
    mc "Thanks."
    scene ch9_633 with dissolve
    pause
    mia "..."
    k "What?"
    mia "I didn’t say anything..."
    k "Don't start with that."
    scene ch9_634 with dissolve
    s "Hey, who invited you two anyway?"
    k "Oh, by the way."
    k "[drelatks!cl]’s looking for you. He wants to know where you left the boogieboard."
    scene ch9_635 with dissolve
    k "You haven’t lost it already, have you?"
    s "Uhm..."
    scene ch9_636 with dissolve
    s "..."
    pause
    k "What are you waiting for?"
    scene ch9_637 with dissolve
    s "Don’t let them do anything that [krelat]s shouldn’t do while I’m gone!"
    mia "Huh?"
    scene ch9_638 with dissolve
    k "Hey!"
    pause
    scene ch9_639 with dissolve
    k "Uh..."
    pause
    scene ch9_640 with dissolve
    mia "*Pfff...*"
    pause
    scene ch9_641 with dissolve
    mia "What did she mean by that?"
    k "..."
    pause
    scene ch9_642 with dissolve
    pause
    k "Hm?"
    scene ch9_643 with dissolve
    mc "For being [krelat]s."
    k "What?"
    pause
    scene ch9_644 with dissolve
    k "{i}{size=-2}[mc], are you sure you want her to know?"
    mc "Come on, [k], the three of us know."
    mc "Don’t tell me you're the only one who didn't know that I know that [mia] knows what you and I know."
    k "What?"
    mc "[mia] told me a few days ago that you told her."
    k "Huh?"
    scene ch9_645 with dissolve
    mia "Woah, look at the sky, the sunset is so beautiful!"
    k "[mia], is that true?"
    mia "What? I wasn’t listening."
    k "Are you serious?"
    scene ch9_646 with dissolve
    pause
    scene ch9_647 with dissolve
    mia "For being [krelat]s..."
    k "..."
    pause
    scene ch9_649 with dissolve
    k "Bitch!"
    k "And here I am acting like... I hate you!"
    mia "Forgive me, I didn’t mean it!"
    mc "Hahaha."
    scene ch9_650 with dissolve
    k "Oh my god, now you're going to be unbearable!"
    mia "Long live the [krelat]s! Hahaha."
    pause
    stop music fadeout 2.0
    stop background fadeout 3.0
    scene blackscreen with Dissolve(2.0)
    pause
    play background "audio/beachsfx.ogg" loop volume 0.7 fadein 1.0
    scene ch9_651 with dissolve
    play music scene1 fadein 2.0
    mia "So, which university do you plan to attend?"
    k "I don't know..."
    k "Whichever one accepts me, I guess."
    k "And you? You said you’re going back to Puerto Rico to study, if I remember correctly."
    mia "Yeah, I plan to leave in a few months to do university there."
    k "But you're coming back, right?"
    mia "Yeah."
    mia "Are you going to miss me?"
    k "I’m going to cry when you leave."
    mia "Aww, really?"
    k "Of course, dummy, I’m going to miss you."
    mia "I don’t want to leave either, but university is way too expensive here."
    pause
    k "[mc], pay for [mia]'s university."
    mc "With my salary, I couldn’t even pay for her Zumba classes."
    pause
    mia "Come with me."
    k "To Puerto Rico?"
    mia "Yeah, we could live together. Dad has an apartment there, or well... depending on how things go, it’ll be Mom’s, haha."
    mia "It’ll be great."
    k "I don’t know..."
    k "I’m not even sure what I should study."
    k "Actually, I’m not even sure if I want to study."
    $ imageh = 1680
    $ imagew = 1920
    show  ch9_659 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.0
        ease 3 yalign 1.0 zoom 1.2
    mc "(I feel like I’ve been lifting weights with my dick...)" with dissolve
    mc "(At least I’ve calmed down a bit, and the bulge isn’t that noticeable anymore. The underwear’s helping too, but damn, I really want to fuck already.)" with dissolve
    pause
    mia "Why the sad face?"
    show ch9_653 with dissolve
    mia "Relax, [k]'s going to stay with you, I know her."
    mc "Uh... Haha, right."
    scene ch9_653- with dissolve
    k "What do you mean by 'you know me,' you nosy bitch?"
    mia "I’m just saying what I think!"
    pause
    scene ch9_651 with dissolve
    mia "Hey, when you guys, you know... How does it work?"
    k "How does what work?"
    mia "Fucking."
    k "[mia]..."
    mia "Do you do it in your room or [mc]’s?"
    mia "You know, because of your dad."
    k "[mia], please!" with hpunch
    mc "You told her about that too?!"
    mia "Come on! Tell me, I’m really curious."
    scene ch9_652 with dissolve
    k "You just had to open your big mouth..."
    mc "Me? You’re the one who told her."
    mc "Besides, I felt ridiculous pretending like a fool when all three of us already know the truth."
    k "At least she wasn’t going to keep bringing it up."
    mc "Shut up, I bet you told her more stuff."
    k "I didn’t tell her anything."
    scene ch9_654 with dissolve
    mia "Oh... So there is more."
    k "No, there isn’t."
    mia "I bet you do it every day."
    k "No."
    mc "No way..."
    mia "Liars!"
    pause
    mia "Come oooon! Tell me!"
    mia "At least tell me what it’s like?"
    mia "Or should I start talking?"
    scene ch9_653- with hpunch
    k "No, shut uuuuup!"
    mia "Fine, fine!"
    scene ch9_654 with dissolve
    mia "Just tell me, what’s it like to have someone so 'close' as a lover?"
    k "We’re not lovers..."
    mia "Whatever."
    k "..."
    pause
    k "Well... it’s the same..."
    k "Ugh, I don’t know! Ask [mc]."
    mc "Why me?"
    mc "Well, it’s..."
    mc "It’s... How do I explain it?..."
    mia "Like friends with benefits?"
    mc "Uhm..."
    mia "Friends with perks?"
    mia "Or better yet, '[krelat]s' with benefits?"
    mc "Uh... yeah, sort of..."
    scene ch9_655 with dissolve
    mc "Yeah, it’s pretty much the same but with some 'extra benefits.'"
    k "Hey..."
    scene ch9_656 with dissolve
    mia "So... does that mean your relationship is purely physical?"
    k "Relationship is a strong word."
    image ch9_656anim:
        "ch9_657" with dissolve
        1.7
        "ch9_656" with dissolve
        1.7
        repeat
    scene ch9_656anim with dissolve
    mc "Yeah, it’s like..."
    mc "It’s like having an inflatable doll, but cheaper."
    k "Idiot..."
    mia "Got it."
    mia "So you guys just do sexual favors, nothing else."
    mc "Yeah, you could say I’m doing her a favor."
    k "Of course..."
    k "You’re the one who pounced on me that time, in case you forgot."
    scene ch9_663 with dissolve
    mc "If I remember right, when we went to [mia]'s place, you’re the one who climbed on top of me."
    k "And when we came back and snuck in through my window? Did you forget about that?"
    mia "I don’t know about you guys, but all this smells like romance to me."
    k "Shut up, [mia]..."
    mia "I wish I had a cousin like [mc], I’m so jealous, seriously."
    pause
    k "Jealous of what?"
    mia "Huh?"
    scene ch9_664 with dissolve
    mia "I said like [mc]! Ugh, there you go with your jealousy!"
    k "What the hell are you talking about? You can fuck him if you want."
    scene ch9_663 with dissolve
    mia "Haha, relax, geez!"
    mia "You look so comfortable leaning on [mc]'s legs."
    mia "I should’ve brought [dereck], so I don’t feel like a third wheel."
    scene ch9_665 with dissolve
    k "Go ahead, I’ll lend him to you for a bit."
    mia "Hmm... I just want to lie down like you."
label ch9m1:
    if _in_replay:
        show screen Replayexit
        play music scene1 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_663 with dissolve
    k "Do whatever you want with him, I don’t care."
    mia "..."
    k "Seriously."
    mia "Well..."
    mia "I just want to lie down."
    scene ch9_666 with dissolve
    mia "I hope you don’t mind, [mc]."
    mc "It’s fine."
    scene ch9_667 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.0
        ease 20 yalign 1.0 
        ease 20 yalign 0.0
    mc "(Damn, I’ve got two beauties leaning on my leg.)" with dissolve
    mc "(It’s literally torturous...)" with dissolve
    mc "(Now’s the time I should bring out my silver tongue and seduce them with my words.)" with dissolve
    pause
    mc "(Yeah, right...)" with dissolve
    pause
    mc "(The alcohol is starting to kick in.)" with dissolve
    mc "(Let’s hope it’ll at least get rid of this damn erection once and for all.)" with dissolve
    scene ch9_668 with dissolve
    mia "..."
    pause
    k "What?"
    mia "I didn’t say anything..."
    k "If you keep bothering with that, I’ll leave."
    scene ch9_670 with hpunch
    k "And you, stop touching me!"
    mia "Okay, okay, relax!"
    scene ch9_671-- with dissolve
    k "Is the beer all gone?"
    mia "I think so."
    mc "Yeah, I have the last one. Do you want it?"
    k "No, thanks."
    mia "Aww, how sweet."
    k "Seriously? Are you going to be like this all day?"
    mia "Okay, sorry."
    scene ch9_671- with dissolve
    mia "Uh..."
    pause
    scene ch9_671--- with dissolve
    mc "Oh..."
    mc "(No wonder I felt less pressure in my groin...)" with dissolve
    mia "Are you still grounded?"
    k "N-no..."
    mia "Want to go to the mall tomorrow? I want to buy a bag."
    mc "(God, it’s throbbing...)" with dissolve
    mia "I bought a beautiful wine-colored outfit, and I want a bag to match it."
    k "The one in the photos you sent me?"
    scene ch9_671---- with dissolve
    mc "(What the hell?)" with dissolve
    image ch9_671anim:
        "ch9_671-----" with dissolve
        1.75
        "ch9_671----" with dissolve
        1.75
        repeat
    scene ch9_671anim with dissolve
    mc "Uhm..."
    mia "Yes."
    mc "(She’s rubbing my dick...)" with dissolve
    mc "(Having a boyfriend and doing this... I must seem super attractive to her.)" with dissolve
    mc "(Or maybe she’s just a bitch.)" with dissolve
    pause
    k "Ah! I also bought a bunch of clothes the other day, now that I remember."
    scene ch9_671------ with dissolve
    mia "Really?"
    scene ch9_671------- with dissolve
    mc "(This girl...)" with dissolve
    image ch9_671anim2:
        "ch9_671------" with dissolve
        1.75
        "ch9_671-------" with dissolve
        1.75
        repeat
    scene ch9_671anim2 with dissolve
    k "[drelatks!cl] took [s] and me shopping to make up for his days away from home."
    mia "Hmm, not a bad way to say sorry."
    k "Yeah, he’s been feeling really guilty lately for not being with us."
    k "That and something else I’ll tell you about later."
    mia "At least he cares, mine hates me."
    mc "(This girl seriously doesn’t give a damn about anything.)" with dissolve
    k "Don’t you talk to your dad?"
    mia "..."
    k "[mia]?"
    mia "What?"
    k "I’m asking if you talk to your dad."
    mia "No, he left our lives a while ago..."
    scene ch9_671anim with dissolve
    mia "Do you think if I ask your dad for some beers, he’ll get mad?"
    k "He won’t let me drink."
    mia "Yeah..."
    k "Do you want to go buy more?"
    scene ch9_672 with dissolve
    mia "Uhm..."
    scene ch9_673 with dissolve
    mia "No, wait, I brought something!"
    $ renpy.end_replay()
    k "What thing?"
    mia "I have it in my backpack."
    scene ch9_674 with dissolve
    mia "Ta-da!"
    k "What’s that?"
    mia "It’s a whiskey or something, my boyfriend and I bought it, but he didn’t like it."
    scene ch9_675 with dissolve
    k "It smells sweet."
    mia "Doesn’t it?"
    mc "Let me see."
    scene ch9_676 with dissolve
    mc "It smells sweet, that’s true."
    mc "(The smell seems familiar.)" with dissolve
label ch9k2:
    if _in_replay:
        show screen Replayexit
        play music scene2 fadein 1.0
        play background beachsfx fadein 1.0
    scene ch9_683 with dissolve
    mc "Shall we try it?"
    k "I’m a bit drunk from the beers already."
    scene ch9_677 with dissolve
    mc "Let me have a sip..."
    scene ch9_683 with dissolve
    k "Is it good?"
    mc "It’s a bit strong."
    pause
    mc "(She always has that sexy look...)" with dissolve
    pause
    scene ch9_693 with dissolve
    k "Hmh.."
    pause
    scene ch9_683 with dissolve
    k "Hey... D-don’t kiss me."
    mc "You should try it too."
    scene ch9_678 with dissolve
    k "Just a little..."
    scene ch9_679 with dissolve
    pause
    scene ch9_680 with dissolve
    pause
    scene ch9_681 with dissolve
    pause
    scene ch9_682 with dissolve
    pause
    image ch9_682anim:
        "ch9_681" with dissolve
        1.75
        "ch9_682" with dissolve
        1.75
        repeat
    scene ch9_682anim with dissolve
    k "*Hmh...*"
    mc "Do you like it?"
    k "Yes..."
    k "But I don’t want to get drunk."
    k "In fact, you shouldn’t drink either. *Hmhm* I-if [drelatks] sees you drunk, he’ll get mad."
    mc "You’re right..."
    pause
    scene ch9_684 with dissolve
    k "{i}{size=-3}[mc]..."
    mia "So, did you like it?"
    scene ch9_685 with hpunch
    k "Ahem! We can’t drink this, it has too much alcohol."
    k "B-but it’s good!"
    mia "If you want, I can leave."
    k "Eh... N-no, hehe..."
    k "We weren’t..."
    scene ch9_689 with dissolve
    k "Alright, [mc]."
    mia "It’s okay, I don’t mind."
    k "Shut up. We weren’t doing anything."
    scene ch9_690 with dissolve
    mia "Are you sure?"
    mia "Because I don’t think that’s anyhing."
    scene ch9_691 with dissolve
    pause
    scene ch9_692 with dissolve
    k "T-that’s not... I didn’t know..."
    mia "[k], please."
    scene ch9_686 with dissolve
    mia "Stop acting like I don’t know that you two are fucking like rabbits all day in your room."
    mia "Kiss, live the damn life, don’t let embarrassment limit you."
    scene ch9_698 with dissolve
    pause
    scene ch9_697- with dissolve
    k "{i}{size=-2}What the hell is wrong with you?"
    mc "{i}{size=-2}You look so fucking sexy in that bikini."
    scene ch9_697 with dissolve
    k "{i}{size=-2}Thanks."
    k "{i}{size=-2}You also look good without a shirt..."
    scene ch9_696 with dissolve
    pause
    scene ch9_698 with dissolve
    pause
    scene ch9_699 with dissolve
    pause
    scene ch9_700 with dissolve
    pause
    scene ch9_701 with dissolve
    pause
    image ch9_696anim:
        "ch9_698" with dissolve
        1.5
        "ch9_699" with dissolve
        1.5
        "ch9_700" with dissolve
        1.5
        "ch9_701" with dissolve
        1.5
        repeat
    scene ch9_696anim with dissolve
    mc "*Hmm...*"
    k "{i}{size=-2}Showing off your huge dick like that... Aren’t you embarrassed?"
    mc "{i}{size=-2}*Hmh* It just popped out, it has a mind of its own."
    pause
    scene ch9_695- with dissolve
    pause
    scene ch9_695-- with dissolve
    pause
    scene ch9_695 with dissolve
    pause
    scene ch9_694 with dissolve
    pause
    image ch9_695anim2:
        "ch9_695-" with dissolve
        1.5
        "ch9_695--" with dissolve
        1.5
        "ch9_695" with dissolve
        1.5
        "ch9_694" with dissolve
        1.5
        repeat
    scene ch9_695anim2 with dissolve
    mc "Hmm..."
    k "{i}{size=-2}Wow, it’s already throbbing..."
    k "{i}{size=-2}Aren’t you cumming already, don't you?"
    scene ch9_696 with dissolve
    k "{i}{size=-2}Have you been hard for a long time?"
    mc "{i}{size=-2}Longer than you can imagine."
    k "{i}{size=-2}Hahaha, poor thing."
    mc "{i}{size=-2}Why the laughter?"
    scene ch9_697 with dissolve
    k "{i}{size=-2}I don’t know."
    pause
    scene ch9_697- with dissolve
    k "{i}{size=-2}I think the beers are starting to kick in..."
    mc "{i}{size=-2}Me too..."
    pause
    scene ch9_693 with vpunch
    play sound kissing fadein 0.5 loop volume 0.5
    k "Hmch!"
    pause
    stop sound fadeout 0.5
    scene ch9_686 with dissolve
    mia "Guys, where did you leave the lid for this thing?"
    mia "Forget it. Here it is."
    scene ch9_686- with dissolve
    mia "Hey, how about we get some sodas? Maybe it’ll taste better diluted."
    mia "Hm? What do you say, guys?"
    scene ch9_686----- with dissolve
    mia "No! I just came up with a good idea for a game!"
    mia "How about we play a game of challenges and whoever doesn’t complete theirs takes a shot of this stuff?"
    mia "Yes, I know you don’t want to get drunk, but that’s the fun of the game."
    scene ch9_688 with dissolve
    mia "Guys?..."
    stop music fadeout 1.5
    mia "Eeeh?"
    play music sexy1 fadein 1.5
    scene ch9_702 with dissolve
    mc "{i}{size=-2}Wow, what a face... and you said you didn’t like giving head."
    mc "{i}{size=-2}Is this what you want?"
    k "..."
    mc "{i}{size=-2}Don’t just stand there staring."
    play sound "audio/wavs/bj_9.ogg" 
    scene ch9_703 with dissolve
    k "Buhm!"
    mc "{i}{size=-2}Go ahead, start sucking the cock you love."
    scene ch9_704 with hpunch
    k "Hmm!"
    pause
    jump bfrch9_705kbj1_1

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_705kbj1_(trans, st, at):  
        trans.set_child("ch9_705kbj1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 1:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 35:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_705kbj2_(trans, st, at):  
        trans.set_child("ch9_705kbj2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 1:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 35:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_705kbj3_(trans, st, at):  
        trans.set_child("ch9_705kbj3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 1:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 35:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_705kbj1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_705kbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_705kbj3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("aftersch9_705kbj3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_705kbj2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch9_705kbj1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" action Jump("ch9_705kbj3_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("aftersch9_705kbj3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_705kbj3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 1" action Jump("ch9_705kbj1_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_705kbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("aftersch9_705kbj3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label bfrch9_705kbj1_1:
    image ch9_705kbj1_:
        function ch9_705kbj1_
    image ch9_705kbj2_:
        function ch9_705kbj2_
    image ch9_705kbj3_:
        function ch9_705kbj3_
    $ anim_speed = 0.03
    scene ch9_705kbj1_ with dissolve
    mc "Oh..."
    mc "{i}{size=-2}You like giving head on your own, huh?"
    k "*Slrp, schuck, shlp*"
    pause
    mc "(In the end, we didn’t care that [mia] was watching us.)" with dissolve
    mc "(I trust that [mia] won’t tell anyone.)" with dissolve
    pause
    mc "{i}{size=-2}Oh... *hmh*..."
    k "*shlp, chup, shlup*"
    mc "(God, this is such a good blowjob; Deep, good suction, and a lewd tongue movement...)" with dissolve
    pause
    scene ch9_705kbj2_ with dissolve
    mc "{i}{size=-2}Uh... Jesus..."
    $ anim_speed = 0.01
    k "Chup, shlp, shuck*"
    mc "{i}{size=-2}You're so good, [k]... oh..."
    pause
    mc "(Mia is looking over here...)" with dissolve
    pause
    show ch9_706 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.55 zoom 1.05
        ease 0.5 yalign 0.45
        ease 0.5 yalign 0.55
        repeat
    mc "(I don’t know why, but having her watch makes it much hotter.)" with dissolve
    mc "(I guess I am a bit of an exhibitionist after all.)" with dissolve
    pause
    hide ch9_706 with dissolve
    scene ch9_705kbj3_ with dissolve
    mc "{i}{size=-2}Uhh, suck it really well and make sure to get it nice and wet because I’m going to fuck that tight little pussy hard..." with dissolve
    k "*Slurp, suck, slrp* Uhm."
    mia "{i}{size=-3}God... *giggle*"
    call screen ch9_705kbj3_ with dissolve

label ch9_705kbj1_:
    scene ch9_705kbj1_ with dissolve
    call screen ch9_705kbj1_ with dissolve

label ch9_705kbj2_:
    scene ch9_705kbj2_ with dissolve
    call screen ch9_705kbj2_ with dissolve

label ch9_705kbj3_:
    scene ch9_705kbj3_ with dissolve
    call screen ch9_705kbj3_ with dissolve

label aftersch9_705kbj3_:
    scene ch9_707 with dissolve
    play sound "audio/wavs/bj_9.ogg"
    pause
    mc "You can go deeper than that..."
    scene ch9_708 with hpunch
    play sound "audio/wavs/bjgags10.ogg" volume 0.65
    pause
    scene ch9_709 with dissolve
    play sound "audio/moan/breathpitch8.wav"
    k "*Ugh!* {i}Idiot, cough, cough..."
    pause
    scene ch9_711 with dissolve
    play sound kissing loop volume 0.25 fadein 0.5
    pause
label afterch9_710ksf1_:
    jump ch9_711pan_050



label ch9_711pan_044:
    scene ch9_711pan_044 with Dissolve(0.1) 
    call screen arrow_buttons44  

label ch9_711pan_045:
    scene ch9_711pan_045 with Dissolve(0.1)  
    call screen arrow_buttons45     

label ch9_711pan_046:
    scene ch9_711pan_046 with Dissolve(0.1)  
    call screen arrow_buttons46     

label ch9_711pan_047:
    scene ch9_711pan_047 with Dissolve(0.1)  
    call screen arrow_buttons47     

label ch9_711pan_048:
    scene ch9_711pan_048 with Dissolve(0.1)  
    call screen arrow_buttons48     

label ch9_711pan_049:
    scene ch9_711pan_049 with Dissolve(0.1)  
    call screen arrow_buttons49     

label ch9_711pan_050:
    scene ch9_711pan_050 with Dissolve(0.1)  
    call screen arrow_buttons50     

label ch9_711pan_051:
    scene ch9_711pan_051 with Dissolve(0.1)  
    call screen arrow_buttons51     

label ch9_711pan_052:
    scene ch9_711pan_052 with Dissolve(0.1)  
    call screen arrow_buttons52     

label ch9_711pan_053:
    scene ch9_711pan_053 with Dissolve(0.1)  
    call screen arrow_buttons53     

label ch9_711pan_054:
    scene ch9_711pan_054 with Dissolve(0.1)  
    call screen arrow_buttons54     

label ch9_711pan_055:
    scene ch9_711pan_055 with Dissolve(0.1)  
    call screen arrow_buttons55     

label ch9_711pan_056:
    scene ch9_711pan_056 with Dissolve(0.1)  
    call screen arrow_buttons56     

screen arrow_buttons44:
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_045") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice" 

screen arrow_buttons45:       
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_044") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_046") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons46:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_045") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_047") xalign 1.0 yalign 1.0
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice" 

screen arrow_buttons47:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_046") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_048") xalign 1.0 yalign 1.0
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice" 

screen arrow_buttons48:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_047") xalign 0.0 yalign 1.0 
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_049") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons49:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_048") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_050") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons50:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_049") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_051") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons51:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_050") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_052") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons52:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_051") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_053") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons53:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_052") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_054") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons54:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_053") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_055") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons55:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_054") xalign 0.0 yalign 1.0
    textbutton "{image=right_arrow}" action Jump("ch9_711pan_056") xalign 1.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"

screen arrow_buttons56:
    textbutton "{image=left_arrow}" action Jump("ch9_711pan_055") xalign 0.0 yalign 1.0 
    textbutton "Continue" action Jump("ch9_arrowbuttons711") xalign 0.99 yalign 0.05 style "textbutton_choice"
label ch9_arrowbuttons711:
    image ch9_711mckk:
        "ch9_711----" with dissolve
        1.75
        "ch9_711-----" with dissolve
        1.75
        repeat
    scene ch9_711mckk with dissolve
    k "*Mmh, smnch, mnch*"
    pause
    scene ch9_711--- with dissolve
    mia "I knew this was going to happen, haha."
    mia "Well... So, should we play truth or dare?"
    mia "Guys?"
    pause
    image ch9_711mckk2:
        "ch9_711------" with dissolve
        1.75
        "ch9_711-------" with dissolve
        1.75
        repeat
    scene ch9_711mckk2 with dissolve
    play sound kissing fadein 0.5 loop volume 0.5
    k "*Llmch, hmmh, smnch*"
    pause
    stop sound fadeout 0.5
    scene ch9_711-------- with dissolve
    mc "Shall we go for it?"
    k "[mia] is watching."
    mc "She's already unbearable anyway."
    mc "Let's give her a reason to be."
    k "You're crazy."
    mc "No, I'm drunk and horny."
    k "Me too."
    scene ch9_711mckk2 with dissolve
    play sound kissing fadein 0.5 loop volume 0.5
    k "*Llmch, hmmh, smnch*"
    stop sound fadeout 0.5
    scene ch9_711---------- with dissolve
    mia "{i}{size=-2}Wow..."
    pause
    mia "Are you seriously going to...?"
    mia "You can ignore me, I won't..."
    mia "I won't tell anyone, hehe..."
    scene ch9_711- with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.0
        ease 5 yalign 1.0
    mia "{i}{size=-3}You guys aren’t even listening to me, haha."
    mc "{i}Uff, you're super wet..."
    k "{i}Just put it in..."
    pause
    scene ch9_711------------- with dissolve
    k "*Uhm...*"
    mc "Ohh, finally, a nice tight pussy..."
    scene ch9_711------------ with dissolve
    play sound "audio/character/k/soft/k_moan_soft_23.ogg" fadein 0.1 volume 0.3
    k "*Ah... hmm...*"
    jump beforech9_710ksf1_x






init python:
    def ch9_710ksf1_(trans, st, at):  
        trans.set_child("ch9_710ksf1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(1.0, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf2_(trans, st, at):  
        trans.set_child("ch9_710ksf2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.9, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf3_(trans, st, at):  
        trans.set_child("ch9_710ksf3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.85, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf4_(trans, st, at):  
        trans.set_child("ch9_710ksf4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1  
        if store.frame_num in [13, 33]:
            sound_files = ["audio/masturbating/cutmastrubating6.ogg", "audio/masturbating/cutmastrubating7.ogg", "audio/masturbating/cutmastrubating8.ogg", "audio/masturbating/cutmastrubating9.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)() 
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(1.0, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf5_(trans, st, at):  
        trans.set_child("ch9_710ksf5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf6_(trans, st, at):  
        trans.set_child("ch9_710ksf6_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.85, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf8_(trans, st, at):  
        trans.set_child("ch9_710ksf8_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.4, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf9_(trans, st, at):  
        trans.set_child("ch9_710ksf9_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.6, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_710ksf10_(trans, st, at):  
        trans.set_child("ch9_710ksf10_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 37:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(1.0, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_710ksf1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf6_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf8_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf9_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" action Jump("ch9_710ksf10_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710ksf10_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0075) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.19
        textbutton "Pov 9" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.29
        textbutton "Pov 8" action Jump("ch9_710ksf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.39
        textbutton "Pov 7" action Jump("ch9_710ksf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.49
        textbutton "Pov 6" action Jump("ch9_710ksf6_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710ksf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710ksf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710ksf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710ksf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710ksf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710ksf8_2") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label beforech9_710ksf1_x:
    image ch9_710ksf1_:
        function ch9_710ksf1_
    image ch9_710ksf2_:
        function ch9_710ksf2_
    image ch9_710ksf3_:
        function ch9_710ksf3_
    image ch9_710ksf4_:
        function ch9_710ksf4_
    image ch9_710ksf5_:
        function ch9_710ksf5_
    image ch9_710ksf6_:
        function ch9_710ksf6_
    image ch9_710ksf8_:
        function ch9_710ksf8_
    image ch9_710ksf9_:
        function ch9_710ksf9_    
    image ch9_710ksf10_:
        function ch9_710ksf10_
    $ anim_speed = 0.021
    play voicefx "audio/wavs/k/kmoansoft.ogg" fadein 0.5 loop volume 0.3
    scene ch9_710ksf4_ with dissolve
    k "*Ah... uhm...* God, take it slow at first..."
    mc "I am going slowly, hmmh, ohh..."
    mc "(God, I don’t know if it’s because I needed it, but her pussy feels especially good today.)" with dissolve
    mc "(It’s like she’s sucking me, it’s super tight.)" with dissolve
    pause
    mc "Were you looking forward to this, huh?"
    k "*Ah, hmm, hmm* W-Wait?"
    mc "Yes, you’re squeezing me like never before... oh..."
    k "I’m not squeezing{w=0.5}, *uh, uhm*{w=0.5}, I think you’re bigger than usual."
    pause
    $ anim_speed = 0.01
    scene ch9_710ksf1_ with dissolve
    k "*Ah, ah, ah*"
    mc "(Her ass always looks delicious, but especially when she bends over, it looks even better.)" with dissolve
    k "*Ah, oh, ohm, ah*"
    pause
    k "And no, I wasn’t looking forward to anything..."
    k "You were the one who, {w=0.5}*hah, uhm*{w=0.5}, was acting like a pervert."
    mc "I won’t deny that..."
    mc "*Hm...* But you too, don't act like you don't love my cock trusting inside your pussy."
    pause
    scene ch9_710ksf2_ with dissolve
    k "N...{w=1.0} I don’t know. *uh, uh, uh*"
    mc "Don’t know? {i}{size=-4} Are you shy because [mia] is watching?"
    k "*Ah, hmmm* Shut up!"
    mc "Shh... don’t raise your voice so much."
    k "Then stop saying stupid things."
    $ anim_speed = 0.0079
    k "*Ah, mah, oh, auh* {i}{size=-3} Not so hard!"
    mc "*Hmmh* Shhh... {i}{size=-5} Yes... oh..."
    k "*Hmnh, mah, ah, ahm*"
    pause
    show ch9_712- with dissolve:
        subpixel True
        xalign 0.49 yalign 0.5 zoom 1.0015
        ease 0.2 xalign 0.51 zoom 1.0
        ease 0.2 xalign 0.49 zoom 1.0015
        repeat
    k "*Ahh, ah, ah!*"
    mia "..."
    pause
    mc "(She’s paying close attention...)" with dissolve
    mc "(She hasn’t taken her eyes off us, she looks like a puppy in a butcher shop.)" with dissolve
    mc "(Of course, she came home early today, so she didn’t get any dick.)" with dissolve
    pause
    scene ch9_710ksf5_ with dissolve
    hide ch9_712- with dissolve
    k "*Ahh, uh, uh*"
    mia "Gez... {i}{size=-3}You’re fucking like porn stars, haha."
    pause
    scene ch9_710ksf3_ with dissolve
    mc "{size=-3}{i}Look, your friend can’t stop watching us."
    k "*Hah, hah, uh*"
    k "*Uh, ah* {size=-3}{i}Just ignore her."
    mc "{size=-3}{i}Are you sure? Maybe she wants to join..."
    k "*Hah, huh, uh*{size=-4}{i}Are you stupid?"
    mc "{size=-4}{i}Look at her..."
    mc "{size=-4}{i}Don’t you like sharing?"
    k "{size=-4}{i}And you?"
    pause
    mc "{size=-4}{i}Uhm..."
    pause
    scene ch9_710ksf9_ with dissolve
    mc "*Hmhm* {size=-4}{i}Oh, god, yes..."
    mc "{size=-2}{i}I’m going to cum soon..."
    k "*Huh, uh, hmhm* {size=-2}{i}So soon?"
    k "{size=-2}{i}H-Hold on a little longer. *uh, uh, ouh*"
    pause
    scene ch9_710ksf10_ with dissolve
    mc "Mhhg!"
    k "*Hah, hah, oh* Oh god, hmhm!"
    mc "(I love how her ass bounces and how her whole body trembles with each thrust.)" with dissolve
    mc "(God, I love her whole body...)" with dissolve
    mc "(I’m lucky to have such a sexy [krelat]!)" with dissolve
    pause
    scene ch9_710ksf6_ with dissolve
    k "Uh, uuhh, uhm!"
    mc "*Hngh!*"
    mia "Damn..."
    mc "(I’m so fucking close!)" with dissolve
    pause
    scene ch9_710ksf8_ with dissolve
    call screen ch9_710ksf8_ with dissolve
define ch9710ksf1_pov = "False"
label ch9_710ksf1_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf1_ with dissolve
    call screen ch9_710ksf1_ with dissolve
label ch9_710ksf2_:
    $ ch9710ksf1_pov = "True"
    scene ch9_710ksf2_ with dissolve
    call screen ch9_710ksf2_ with dissolve
label ch9_710ksf3_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf3_ with dissolve
    call screen ch9_710ksf3_ with dissolve
label ch9_710ksf4_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf4_ with dissolve
    call screen ch9_710ksf4_ with dissolve
label ch9_710ksf5_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf5_ with dissolve
    call screen ch9_710ksf5_ with dissolve
label ch9_710ksf6_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf6_ with dissolve
    call screen ch9_710ksf6_ with dissolve
label ch9_710ksf8_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf8_ with dissolve
    call screen ch9_710ksf8_ with dissolve
label ch9_710ksf9_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf9_ with dissolve
    call screen ch9_710ksf9_ with dissolve
label ch9_710ksf10_:
    $ ch9710ksf1_pov = "False"
    scene ch9_710ksf10_ with dissolve
    call screen ch9_710ksf10_ with dissolve


label beforech9_710ksf8_2:
    $ anim_speed = 0.0079
    if ch9710ksf1_pov == "False":
        scene ch9_710ksf2_ with dissolve 
    "Are we going to those rocks over there?"
    "You didn’t eat your sandwich, don’t think I didn’t notice."
    mia "{i}{size=-2}There are people on the other side of the rock."
    pause
    mia "{i}{size=-2}Hey, guys!" with dissolve
    pause
    stop voicefx fadeout 0.5
    scene ch9_712-1 with dissolve
    mia "Hey, hi there, little one."
    "I came to see the crabs."
    scene ch9_712-2 with hpunch
    k "{i}{size=-4}Duck down!"
    scene ch9_712-3 with dissolve
    mia "T-there are no crabs here."
    "Hmm... I came earlier and there were some."
    mia "N-no, they already left!"
    "Hmm..."
    "Are you a brunette?"
    mia "Uh... yeah.."
    "Ah..."
    "Where are you from?"
    mia "I’m from Puerto Rico."
    "Ah..."
    "Is this how girls in Puerto Rico wear their hair?"
    mia "Uh... no... I don’t know."
    mia "And your mom?"
    "My mom is with dad, over there."
    mia "Well, go with them—"
    "You’re pretty even with your hair like that."
    mia "Uh... heh, thanks..."
    scene ch9_712-4 with dissolve
    k "{i}{size=-3}Is she a child?"
    mc "{i}{size=-3}Sounds like one."
    k "{i}{size=-3}What the hell is a kid doing here?"
    mc "{i}{size=-3}How the hell should I know?"
    scene ch9_712-3 with dissolve
    mc "{i}{size=-3}What are you doing?"
    k "{i}{size=-3}I want to get my panties."
    mc "{i}{size=-3}No, you’ll be seen! Wait until she leaves."
    "I don’t like short hair because I look like a boy."
    mia "I see, go with your parents, okay?"
    "Are you gay?"
    mia "Uh... hah..."
    mia "I think your mom is calling you, go to her, kids can’t be here."
    "Why not?"
    mia "It’s forbidden."
    "Hmm... Alright."
    scene ch9_712-9 with dissolve
    mia "Yes, go with your mom instead."
    "Who bought you your bikini?"
    scene ch9_712-5 with dissolve
    mia "I bought it myself, but—"
    "My mom bought me mine."
    scene ch9_712-6 with dissolve
    mia "How nice, heh..."
    image ch9_712animk:
        "ch9_712-7" with dissolve
        1.75
        "ch9_712-7-" with dissolve
        1.75
        repeat
    scene ch9_712animk with dissolve
    play sound kissing fadein 0.5 volume 0.35 loop
    k "{i}{size=-3}*Hmnch, smch, slch*"
    "Do you want to play?"
    "{i}Honey, come eat your sandwich!"
    "I have to go!"
    mia "Bye!"
    stop sound fadeout 0.5
    scene ch9_712-10 with dissolve
    pause
    scene ch9_712-10--- with dissolve
    pause
    scene ch9_712-10 with dissolve
    pause 0.5
    scene ch9_712-10- with dissolve
    k "*Uhm...*"
    pause
    jump afterch9_710kcf9_
init python:
    def ch9_710kcf2_(trans, st, at):  
        trans.set_child("ch9_710kcf2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1  
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf3_(trans, st, at):  
        trans.set_child("ch9_710kcf3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf4_(trans, st, at):  
        trans.set_child("ch9_710kcf4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf5_(trans, st, at):  
        trans.set_child("ch9_710kcf5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf6_(trans, st, at):  
        trans.set_child("ch9_710kcf6_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)      
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf7_(trans, st, at):  
        trans.set_child("ch9_710kcf7_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.35, channel='sound')  
                renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf8_(trans, st, at):  
        trans.set_child("ch9_710kcf8_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
init python:
    def ch9_710kcf9_(trans, st, at):  
        trans.set_child("ch9_710kcf9_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if anim_speed > 0.015:
            if store.frame_num == 4:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)     
        if anim_speed < 0.015:
            if store.frame_num == 3:
                sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
                random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
                store.last_played_sound2 = random_sound  
                renpy.sound.set_volume(0.5, channel='sound')  
                renpy.sound.play(random_sound)         
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value   
screen ch9_710kcf2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710kcf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710kcf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710kcf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710kcf7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_710kcf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710kcf7_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710kcf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710kcf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710kcf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710kcf2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_710kcf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710kcf3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710kcf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710kcf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710kcf7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710kcf2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_710kcf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710kcf4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_710kcf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710kcf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710kcf7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710kcf2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_710kcf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710kcf5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_710kcf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710kcf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710kcf7_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710kcf2_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_710kcf5_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label afterch9_710kcf9_:
    image ch9_710kcf2_:
        function ch9_710kcf2_
    image ch9_710kcf3_:
        function ch9_710kcf3_
    image ch9_710kcf4_:
        function ch9_710kcf4_
    image ch9_710kcf5_:
        function ch9_710kcf5_
    image ch9_710kcf6_:
        function ch9_710kcf6_
    image ch9_710kcf7_:
        function ch9_710kcf7_
    image ch9_710kcf8_:
        function ch9_710kcf8_
    image ch9_710kcf9_:
        function ch9_710kcf9_
    $ anim_speed = 0.01
    play voicefx "audio/wavs/k/kmoansoft.ogg" fadein 0.5 loop volume 0.3
    scene ch9_710kcf2_ with dissolve
    mia "She’s already g-... gone..."
    k "*Hah, hah, huh*"
    pause
    scene ch9_710kcf7_ with dissolve
    mia "You couldn’t wait even a second longer, haha."
    mia "God, a bit of alcohol makes you go crazy..."
    k "*Hah, huh, huh*"
    pause
    scene ch9_710kcf3_ with dissolve
    mia "I can imagine everything those bedroom walls have seen, haha..."
    k "*Huh, huh, auh*"
    mia "..."
    pause
    scene ch9_710kcf4_ with dissolve
    k "*Ouh, uhm, huh*"
    pause
    scene ch9_710kcf5_ with dissolve
    mia "I love your [krelat] relationship."
    mia "You look so cute fucking like rabbits..."
    k "*Ouh, huh, ah, ah*"
    call screen ch9_710kcf5_ with dissolve



label ch9_710kcf2_:
    scene ch9_710kcf2_ with dissolve
    call screen ch9_710kcf2_ with dissolve
label ch9_710kcf7_:
    scene ch9_710kcf7_ with dissolve
    call screen ch9_710kcf7_ with dissolve
label ch9_710kcf3_:
    scene ch9_710kcf3_ with dissolve
    call screen ch9_710kcf3_ with dissolve
label ch9_710kcf4_:
    scene ch9_710kcf4_ with dissolve
    call screen ch9_710kcf4_ with dissolve
label ch9_710kcf5_:
    scene ch9_710kcf5_ with dissolve
    call screen ch9_710kcf5_ with dissolve



label afterch9_710kcf5_:
    image ch9_722animf:
        "ch9_722" with Dissolve(0.25)
        0.4
        "ch9_723" with Dissolve(0.25)
        0.4
        "ch9_724" with Dissolve(0.25)
        0.4
        "ch9_725" with Dissolve(0.25)
        0.4
        repeat
    show ch9_722animf with dissolve
    k "*Ah, uh, huh*"
    mc "*Hmmngh!* (Damn, I'm close.)" with dissolve
    pause
    mc "(We need to do this again someday.)" with dissolve
    mc "(Doing it secretly and in a public place is really exciting!)" with dissolve
    mc "(I'm sure it's exciting for her too. Just look at her face, she’s enjoying it as much as I am.)" with dissolve
    mc "*Hmnh* (I'm about to come...)" with dissolve
    mc "(She wouldn’t get mad if I finish inside by 'accident,' right?)" with dissolve
    $ anim_speed = 0.0075
    scene ch9_710kcf4_ with dissolve
    mc "*Hmmngh!*"
    k "*Hauh, huh, oh!*"
    pause
    scene ch9_714 with hpunch
    stop voicefx fadeout 1.0
    k "*Uh..* It came out... Put it back in."
    $ renpy.end_replay()
label ch9km2:
    if _in_replay:
        show screen Replayexit
        scene ch9_714 with hpunch
        play background beachsfx fadein 1.0
        play music sexy1 fadein 1.0
        k "*Uh..* It came out... Put it back in."
    scene ch9_715 with dissolve
    pause
    scene ch9_714 with dissolve
    k "Put it in, what are you waiting for?"
    scene ch9_715- with dissolve
    mc "I can’t put it in, lift your ass a bit more."
    k "Sorry, my legs are shaking."
    mia "I-I’ll help..."
    scene ch9_715-- with dissolve
    mc "(What...)" with dissolve
    mc "(Is she touching herself?)" with dissolve
    scene ch9_715--- with dissolve
    mc "(I was so focused I didn’t realize she was right there.)" with dissolve
    mc "(Look at that slutty face...)" with dissolve
    mc "(She wants some too, it’s obvious in her eyes...)" with dissolve
    scene ch9_716 with dissolve
    mia "Lift your ass a bit more, [k]."
    k "*Uff, uh* What...?"
    scene ch9_717 with dissolve
    mia "Lift your butt a bit, I’ll help put it in."
    k "Seriously?..."
    mia "O-of course."
    scene ch9_718 with dissolve
    mia "..."
    mia "That’s what friends are for, right?"
    k "But..."
    scene ch9_719 with dissolve
    mia "*Lah, lhm*"
    mc "Huh?"
    jump bfrch9_718msd1_1


init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_718msd1_(trans, st, at):  
        trans.set_child("ch9_718msd1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_718msd2_(trans, st, at):  
        trans.set_child("ch9_718msd2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_718msd3_(trans, st, at):  
        trans.set_child("ch9_718msd3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 39:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/bj_1.ogg", "audio/wavs/bj_3.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.2:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value
screen ch9_718msd1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"    
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_718msd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_718msd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_718msd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_718msd3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_718msd2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_718msd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_718msd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_718msd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_718msd3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_718msd3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_718msd3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_718msd2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_718msd1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_718msd3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label bfrch9_718msd1_1:
    $ anim_speed = 0.03
    image ch9_718msd1_:
        function ch9_718msd1_
    image ch9_718msd2_:
        function ch9_718msd2_
    image ch9_718msd3_:
        function ch9_718msd3_
    scene ch9_718msd1_ with dissolve
    mia "*slurp, slsh, schup*"
    mc "Oh... *Hmh*"
    k "What's wrong with you?"
    mc "N-nothing, I was startled by her hand..."
    pause 
    scene ch9_718msd3_ with dissolve
    mia "*Slrp, smch, suck*"
    mc "(It feels like... Is she really giving me a blowjob?)" with dissolve
    pause
    scene ch9_718msd2_ with dissolve
    mia "*Slurp, slrp, slsh*"
    mc "(She is... This girl is totally crazy...)" with dissolve
    mc "*Uh...*"
    call screen ch9_718msd3_ with dissolve
define ch9718at = "False"
label ch9_718msd1_:
    $ ch9718at = "True"
    scene ch9_718msd1_ with dissolve
    call screen ch9_718msd1_ with dissolve
label ch9_718msd2_:
    $ ch9718at = "False"
    scene ch9_718msd2_ with dissolve
    call screen ch9_718msd2_ with dissolve
label ch9_718msd3_:
    $ ch9718at = "False"
    scene ch9_718msd3_ with dissolve
    call screen ch9_718msd3_ with dissolve  

label afterch9_718msd3_:
    if ch9718at == "False":
        scene ch9_718msd1_ with dissolve
    pause
    scene ch9_719 with dissolve
    mia "*Lah...*"
    play sound "audio/mouth/saliva_04.ogg" fadein 0.1 volume 0.5 
    scene ch9_720 with dissolve
    mia "*Spurt*"
    k "What are you doing?"
    scene ch9_721 with dissolve
    mia "Uhm, no, nothing..." 
    k "Did you spit?"
    mia "I-I just added a bit of saliva..."
    pause
    $ anim_speed = 0.00795
    play voicefx "audio/wavs/k/kmoansoft.ogg" volume 0.5 loop fadein 0.3
    scene ch9_710kcf8_ with dissolve
    k "*Uh, uhm, uh*"
    mia "{i}{size=-3}Haha, they don't waste a second..."
    pause
    scene ch9_710kcf6_ with dissolve
    mc "*Uhmng*"
    mc "(She left me well-lubricated, now it slides much better.)" with dissolve
    k "*Ah, hmm, uh*"
    pause
    image ch9_713-anim:
        "ch9_713-" with Dissolve(0.5)
        0.7
        "ch9_713--" with Dissolve(0.5)
        0.7
        repeat
    show ch9_722animf with dissolve
    mc "*Uhmmgh* I-I’m almost there."
    k "*Ah, ah* No, wait a little longer."
    mc "I don’t know how much longer I can hold it."
    k "Squeeze your balls or whatever you need to squeeze, but don’t come yet."
    mc "*¡Hmngh!* -Damn..."
    pause
    show ch9_713-anim with dissolve:
        xalign 0.5 yalign 0.4 zoom 1.001
        ease 0.5 yalign 0.3 
        ease 0.5 yalign 0.4
        repeat
    hide ch9_722animf with dissolve
    mc "(And what the hell is she doing?)" with dissolve
    mc "(I guess she likes to watch...)" with dissolve
    mc "(Damn, look at that expression...)" with dissolve
    mc "(She’s dying to ride a cock too...)" with dissolve
    pause
    scene ch9_710kcf9_ with dissolve
    call screen ch9_710kcf9_ with dissolve

screen ch9_710kcf6_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710kcf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710kcf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710kcf8_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710kcf8_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_710kcf9_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710kcf6_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710kcf8_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_710kcf9_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.021) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_710kcf8_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_710kcf6_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_710kcf8_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"

label ch9_710kcf6_:
    scene ch9_710kcf6_ with dissolve
    call screen ch9_710kcf6_ with dissolve
label ch9_710kcf8_:
    scene ch9_710kcf8_ with dissolve
    call screen ch9_710kcf8_ with dissolve
label ch9_710kcf9_:
    scene ch9_710kcf9_ with dissolve
    call screen ch9_710kcf9_ with dissolve
    
label beforech9_710kcf8_:
    show ch9_722animf with dissolve
    k "*Ah, ah, ah!*"
    mc "*Nghh!*" with dissolve
    pause
    "Hey..."
    show ch9_726 with dissolve:
        xalign 0.4 yalign 0.5 zoom 1.001
        ease 0.5 yalign 0.6
        ease 0.5 yalign 0.4 
        repeat
    stop music fadeout 5.0
    mc "What?"
    mc "(I thought I heard her say something)" with dissolve
    s "Guys, [drelatks] is coming!"
    stop voicefx fadeout 0.5
    scene ch9_727 with dissolve
    k "What?"
    s "He’s coming!"
    mia "Your [drelatks]!"
    k "My [drelatks]?!" with hpunch
    mia "Yes, hide!"
    play music doing fadein 0.5
    scene ch9_728 with vpunch
    k "{i}{size=-3}Shit!"
    mc "Hell no!" with dissolve
    scene ch9_729 with vpunch
    mc "*Huh!*"
    pause
    $ renpy.end_replay()
    scene ch9_730 with dissolve
    d "Guys, is [k] around here?"
    d "Uh, what are you...?"
    pause
    scene ch9_731 with dissolve
    d "Oh, s-sorry..."
    d "Let’s go, [s]."
    s "I told you she wasn't here."
    d "Yes, yes, no I get what you were trying to tell me... L-let’s go..."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene2 fadein 1.5
    scene ch9_732 with dissolve
    mia "Has you [drelat] left?"
    mc "Y-yes, he’s gone..."
    mia "That was close, haha."
    mc "(My heart nearly exploded...)" with dissolve
    mia "You’re pale, *giggle*."
    mia "Don’t worry, it’s over now, haha."
    mc "I thought he was going to discover us, I saw my life flash before my eyes."
    mia "Haha, you guys are something else."
    mc "Hey, why did you jump on me?"
    scene ch9_733 with dissolve
    mia "Your girlfriend forgot this here."
    mc "God, I’m glad you noticed."
    mc "It would have been hard to explain why her panties were lying around."
    mia "Let’s take them to her, she ran off naked."
    mc "Yeah, haha... just give me a second..."
    mia "C'mon, don’t be so dramatic, haha."
    scene ch9_734 with fade
    k "Has [drelatks] left?"
    mia "Yes."
    k "Are those my panties?"
    k "Can you throw them to me, please?"
    mc "Haha, don’t give them to her, let her come for them."
    k "I’m going to hate you forever if you don’t give them to me right now, [mia]."
    mia "Haha, here you go."
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 1.5
    scene ch9_735 with fade
    mia "Where are you going?"
    k "[drelatks!cl] is looking for me, didn’t you hear?"
    mia "Aren’t you going to help us clean up?"
    mc "Hey, she's right, help us pick up the bottles at least."
    k "I have to leave, what part don’t you understand that [drelatks] is looking for me?"
    k "Bye."
    scene ch9_736 with dissolve
    mia "Can you believe it?"
    mc "I’m afraid so..."
    mia "Not even helping me get your cock into her vagina, she’s considerate."
    mc "Haha."
    mia "Haha."
    pause
    mia "Well, let’s clean up."
    mc "Yes."
    scene ch9_737- with dissolve
    mia "I can’t believe this happened, haha."
    mc "Neither can I, it was crazy."
    pause
    mc "(At least the scare made my erection go down...)" with dissolve
    if miatell < 2:
        jump ch9_737mskip
    mia "In the end, we didn’t drink any of the bottle I brought."
    mia "I was thinking of giving it to your [drelat], do you know if he likes to drink?"
    scene ch9_738 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.0
        ease 20 zoom 1.01 xalign 0.5 yalign 0.5
        ease 20 xalign 0.5 yalign 0.5 zoom 1.0
        repeat
    mc "Yes, I’ve seen him drink whisky a few times..."
    mc "..."
    pause
    mia "What did you say?"
    mc "That I’ve seen him drink whisky a few times, maybe he likes it."
    mia "I’ll give it to him, neither my boyfriend nor I will drink it anyway."
    mc "Yeah..."
    pause
label ch9m2:
    if _in_replay:
        play background beachsfx
        play music scene2 fadein 1.0
        scene ch9_738 with dissolve:
            subpixel True
            xalign 0.5 yalign 0.5 zoom 1.0
            ease 20 zoom 1.01 xalign 0.5 yalign 0.5
            ease 20 xalign 0.5 yalign 0.5 zoom 1.0
            repeat
        show screen Replayexit
        $ miatell = 5
    mc "([mia] has a nice ass too...)" with dissolve
    pause
    scene ch9_739 with dissolve
    mc "(Damn, it had gone down...)" with dissolve
    if miatell > 2:
        mc "(I’ve had her once, she’s super slutty. I’m sure if I ask her to fuck, she’ll agree.)" with dissolve
        mc "(But it’s a bit weird after having fucked [k], asking her to fuck.)" with dissolve
        mc "(Besides, I haven’t spoken to her since then.)" with dissolve
        mc "(To hell with it, what’s the worst that can happen? She’ll just say no.)" with dissolve
        pause
        jump ch9miatell739
    jump ch9_contsph


label ch9miatell739:
    scene ch9_740 with dissolve
    mc "Should we put the bottles in your backpack?"
    mia "Huh?"
    mc "*Gulp* I said if we should put the bottles in your backpack, so we don’t have to carry them by hand."
    pause
    scene ch9_741 with dissolve
    mia "Yes, sure..."
    pause
    mia "Is that all you want to put in there?"
    mc "In your backpack?"
    mia "Yes, in my backpack..."
    stop music fadeout 2.0
    pause
    play music sexy2 fadein 2.0
    scene ch9_742 with dissolve
    mia "Or it could be somewhere else..."
    mc "Oh..."
    mc "What do you have in mind?"
    mia "I don’t know... use your imagination..."
    mia "I’m not talking about bottles, by the way..."
    scene ch9_740 with dissolve
    pause
    scene ch9_743 with dissolve
    mc "Uh..."
    mc "(This girl is really slutty, and I love it...)" with dissolve
    mia "So?..."
    scene ch9_743- with dissolve
    mc "First, we need to take off our clothes."
    mia "Alright... *giggle*."
    pause
    scene ch9_744 with dissolve
    mc "I’m just worried about one thing..."
    mia "What thing?"
    mc "That you might not be able to handle it."
    mia "I can handle whatever you give me...{w=0.5} inside, *giggle*."
    mc "But, will you be able to fit it all?"
    mia "I’m sure I can, *giggle*."
    mc "Haha, well..."
    scene ch9_745 with dissolve
    mia "Uh... it’s still wet..."
    mc "Does it bother you?"
    mia "On the contrary..."
    play voicefx "audio/character/m/mid/s_moan_mid_1.ogg" fadein 0.5 volume 0.2
    pause 0.2
    scene ch9_746 with dissolve
    mia "*Ah!... uhh...*"
    mia "Uhhh... uh.."
    mia "W-wait.. let me get used to it first..."
    pause
    scene ch9_747 with dissolve
    mia "God... wait, don’t move..."
    mc "You’re already so wet."
    mia "Yes, but you’re big... uh.."
    mc "The last time we fucked, it didn’t seem to hurt you that much."
    mia "Y-yeah, that was pretty wild..."
    play voicefx "audio/character/m/mid/s_moan_mid_2.ogg" fadein 0.5 volume 0.2 
    scene ch9_748 with dissolve
    mia "*Ouh, uhh...*"
    pause
    jump ch9_748befor
init python:
    def ch9_748mf1_(trans, st, at):  
        trans.set_child("ch9_748mf1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 36:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_748mf2_(trans, st, at):  
        trans.set_child("ch9_748mf2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 36:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_748mf3_(trans, st, at):  
        trans.set_child("ch9_748mf3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 36:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_748mf4_(trans, st, at):  
        trans.set_child("ch9_748mf4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 36:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_748mf5_(trans, st, at):  
        trans.set_child("ch9_748mf5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num == 36:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.5, channel='sound')  
            renpy.sound.play(random_sound)       
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_748mf1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.02) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_748mf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_748mf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_748mf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_748mf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_contsph") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_748mf2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_748mf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_748mf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_748mf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_748mf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_contsph") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_748mf3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_748mf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_748mf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_748mf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_748mf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_contsph") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_748mf4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_748mf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_748mf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_748mf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_748mf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_contsph") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
screen ch9_748mf5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.00795) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_748mf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_748mf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_748mf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_748mf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_contsph") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"
label ch9_748befor:
    image ch9_748mf1_:
        function ch9_748mf1_
    image ch9_748mf2_:
        function ch9_748mf2_
    image ch9_748mf3_:
        function ch9_748mf3_
    image ch9_748mf4_:
        function ch9_748mf4_
    image ch9_748mf5_:
        function ch9_748mf5_
    $ anim_speed = 0.01
    play voicefx "audio/wavs/m/mmoanmid.ogg" fadein 0.5 volume 0.3 loop
    scene ch9_748mf1_ with dissolve
    mia "*Aah, oh, auh*"
    mia "Like that, just like that... *uh, uh, oh*"
    pause
    mc "Did you say you were feeling down the last time we did this?"
    mia "*Uh, uuh, uh* You’re one of those who talks while doing it, huh?"
    mc "I can stop if it bothers you."
    mia "No, *Ouh, uh*, I’m the same way."
    pause
    mia "Yes, I was feeling down..."
    pause
    mc "Problems with your boyfriend?"
    mia "Uhmm... something like that. *Uhm, ah, ah*."
    pause
    mc "I know your boyfriend, he was with me in high school."
    mia "Yes, I know."
    scene ch9_748mf3_ with dissolve
    mc "(Sorry [dereck], I don’t know what you did but this is karma.)" with dissolve
    mia "*Ah, ah, ah*"
    mc "Do you like it like this?"
    mia "Yes, *Uh, ah, ah*."
    pause
    mia "*Uh, uh* It was so hot seeing you two fuck..."
    mc "Me and [k]?"
    mia "Yes, it was quite a show, haha... *Uh*"
    mia "I was dripping down there just from watching you."
    mc "You could have joined us."
    mia "I know! *Ah, ah*"
    mia "But then that girl arrived and your [drelat] ended the party..."
    pause
    mia "I need to hang out with you guys more, *Ah, ah, ah*."
    pause
    mia "Do you think [k] would have accepted a threesome?"
    mc "Yeah, right? You’re her friend."
    mia "I don’t know..."
    mia "She’s very possessive, I don’t think she would have wanted to share you."
    mc "Nah, you should have told us."
    pause
    scene ch9_748mf2_ with dissolve
    mia "I don’t know, you saw how she reacted the day I cut your hair."
    mc "Yes..."
    pause
    mia "I have to say, you fuck really well, haha."
    mc "Seriously? Do you think I’m good at it?"
    mia "Like a porn star, both of you."
    mc "Haha..."
    mc "Doesn’t your boyfriend fuck you like this?"
    pause
    mia "No, he... he’s not that imaginative."
    mc "Imaginative?"
    mia "Yes, he..."
    mia "Every time we do it, it has to be at his house or mine, nothing else."
    mia "He can’t get it up if we don’t do it on a bed."
    mc "I see..."
    pause
    scene ch9_748mf4_ with dissolve
    pause
    $ anim_speed = 0.007949
    mc "*Hmngh!*"
    mia "Aah! *Uh, uh, uh, uh*"
    mc "*Argh!* You’re so good..."
    mc "You have an amazing ass being so slim..."
    mia "*Ah, ah, ah*"
    mc "*Urghm* When you feel like it, call me and we’ll arrange the threesome."
    mc "*Uhh*, I’ll convince [k]."
    mia "*Uh, uh, uh* Forget it, you’ll ruin it."
    mc "Why do you say that?"
    mia "*Uh, uh, uh* She’ll get mad at you."
    mc "She’ll be fine."
    scene ch9_748mf5_ with dissolve
    pause
    mia "For her, what you two have is like a relationship."
    mia "*Ah, ah, ah* I don’t want to make her feel bad because of us."
    mc "We made it clear from the start, no feelings."
    mia "That’s what she tells you, but it’s not like that."
    mia "I, *Ah, ah*, know her."
    mia "She, *ah, ah*, really cares about you."
    mc "..."
    pause
    call screen ch9_748mf1_ with dissolve

define ch9_748mfat = "False"
label ch9_748mf1_:
    $ ch9_748mfat = "True"
    scene ch9_748mf1_ with dissolve
    call screen ch9_748mf1_ with dissolve 
label ch9_748mf2_:
    $ ch9_748mfat = "False"
    scene ch9_748mf2_ with dissolve
    call screen ch9_748mf2_ with dissolve 
label ch9_748mf3_:
    $ ch9_748mfat = "False"
    scene ch9_748mf3_ with dissolve
    call screen ch9_748mf3_ with dissolve 
label ch9_748mf4_:
    $ ch9_748mfat = "False"
    scene ch9_748mf4_ with dissolve
    call screen ch9_748mf4_ with dissolve 
label ch9_748mf5_:
    $ ch9_748mfat = "False"
    scene ch9_748mf5_ with dissolve
    call screen ch9_748mf5_ with dissolve    


label ch9_contsph:
    $ anim_speed = 0.00795
    if ch9_748mfat == "False":
        scene ch9_748mf1_ with dissolve
    mia "¡Ah, ah!"
    stop voicefx fadeout 0.5
    image ch9_749anim:
        "ch9_749"
        0.05
        "ch9_750"
        0.051
        "ch9_749"
        0.0595
        "ch9_750"
        0.05
        "ch9_749"
        0.059
        "ch9_750"
        0.05
        repeat
    scene ch9_754anim with dissolve
    play voicefx "audio/wavs/m/mmoancum1.ogg" volume 0.4 
    mia "*¡Hmnah, Uuhmh!{w=1.5}{nw}"
    scene ch9_754 with Dissolve(1.5)
    mia "Oh, my God! uff, uh..."
    image ch9_754anim:
        "ch9_754"
        0.05
        "ch9_755"
        0.05
        repeat
    scene ch9_749anim with dissolve
    play voicefx "audio/wavs/m/mmoancum2.ogg" volume 0.4 
    mc "*Hmm*, that’s...{w=1.5}{nw}"
    scene ch9_749 with Dissolve(1.5)
    mia "Uff, uhh..."
    mia "Oh my god, that was good..."
    pause
    scene ch9_757 with dissolve
    pause
    scene ch9_758 with dissolve
    mia "Put it in my ass."
    mc "I-in your ass?"
    scene ch9_759 with dissolve
    mia "Haven’t you ever done it from behind?"
    mc "Uhm..."
    mc "Y-yeah... Yeah, of course."
    pause
    scene ch9_760 with dissolve
    mc "(This day just keeps getting better and better!)" with dissolve
    mc "(The truth is I’ve never done anal before...)" with dissolve
    mc "(It’s just about inserting it, right?)" with dissolve
    scene ch9_761 with dissolve
    mc "(Let’s see...)" with dissolve
    pause
    mc "(Damn, I’m nervous.)" with dissolve
    mc "(It’s like losing my virginity again.)" with dissolve
    scene ch9_762 with dissolve
    pause
    scene ch9_763 with dissolve
    pause
    scene ch9_762 with dissolve
    mc "Uhm..."
    image ch9_762anim:
        "ch9_762" with dissolve
        1.5
        "ch9_763" with dissolve
        1.5
        repeat
    scene ch9_762anim with dissolve
    pause
    mc "(It’s not going in...)" with dissolve
    pause
    mc "(I can’t get it in, but if I push harder I feel like I’m going to hurt myself.)" with dissolve
    pause
    mc "Does it hurt?"
    mia "Relax, just keep going in slowly."
    scene ch9_764 with dissolve
    pause
    scene ch9_765 with dissolve
    pause
    scene ch9_766 with dissolve
    pause
    scene ch9_764 with dissolve
    mc "(It’s still not going in.)" with dissolve
    mc "Maybe it needs more lubrication."
    mia "That’s fine, just insert it safely, but slowly."
    mc "O-ok..."
    image ch9_764anim:
        "ch9_764" with dissolve
        1.5
        "ch9_765" with dissolve
        1.5
        "ch9_766" with dissolve
        1.5
        "ch9_765" with dissolve
        1.5
        repeat
    scene ch9_764anim with dissolve
    pause
    mc "(There’s no way it’s going in without lubrication.)" with dissolve
    mc "(Or maybe it’s my technique?)" with dissolve
    mc "(Damn, it won’t go in even a centimeter. When I push, it just sinks but doesn’t penetrate.)" with dissolve
    pause
    mc "(Maybe if I spit on it well it’ll be easier...) " with dissolve
    pause
    stop music fadeout 2.0
    "Yes! I told you children aren’t allowed."
    play music doing fadein 0.5
    scene ch9_767 with hpunch
    mc "What?!" 
    "W-what...!{w=0.7}{nw}"
    "Sick, degenerates!"
    scene ch9_768 with vpunch
    mc "(Damnit!!)" with dissolve
    $ renpy.end_replay()
    "So that’s why!"
    "What’s going on, mommy?"
    "Vulgar! Aren’t you ashamed, girl?"
    mia "Don’t be so dramatic, ma’am..."
    "Dramatic? My daughter could have seen you!"
    mia "And why should I care about your stupid daughter?"
    scene ch9_768-1 with hpunch
    mc "Mia!"
    "Oh, yeah?"
    "Go call daddy, honey, hurry."
    scene ch9_768-2 with dissolve
    "We’ll see if you still don't care after this."
    mc "(Oh, no...)" with dissolve
    scene ch9_768-3 with dissolve
    pause
    "..."
    mia "What?"
    "Say that again!"
    mia "..."
    pause
    "Hm? Not saying anything now?"
    "Where is the rude girl now?"
    mia "..."
    "I would be embarrassed to have such a promiscuous daughter."
    "Your mother must be very proud of you..."
    mia "..."
    scene ch9_768-4 with dissolve
    pause
    mc "Hey, let’s calm down, okay?"
    scene ch9_768-5 with hpunch
    mc "Ma’am, we’re really sorry, we thought no one would come here."
    mc "Could you forgive us?"
    "..."
    pause
    scene ch9_768-6 with dissolve
    "You only come here to commit crimes..."
    mia "Excuse me?"
    "Yes, yours. You only come here to dirty this beautiful country."
    scene ch9_768-5 with hpunch
    mc "Ma’am!"
    mc "We don’t want any trouble."
    mc "Y-you see..."
    mc "She’s my... girlfriend."
    mc "And her flight leaves this afternoon. I won’t see her for several months and didn’t want to waste the time."
    "There are motels."
    mia "You must know them very well."
    scene ch9_768-6
    "..."
    scene ch9_768-7 with hpunch
    mc "Forgive her, she’s very temperamental!"
    mc "Look... my salary doesn’t cover a motel... And..."
    pause
    mc "Uhm..."
    mc "She’s pregnant and... uhm, we’re going through a lot..."
    scene ch9_768-8 with dissolve
    mc "So, *sniff*, I’m asking from the heart that you don’t call the police."
    mc "I don’t know if I can pay the fine with everything about the pregnance and stuff, *sniff*..."
    mc "She would never do this, you know, the mood swings and everything that come with pregnancy... uhm..."
    scene ch9_768-9 with dissolve
    mc "P-please forgive us. {i}{size=-3}Forgive her..."
    pause
    "Are you sure the child is yours?"
    mc "Ma’am..."
    scene ch9_768-10 with dissolve
    "Sorry, sorry... It’s just that when it comes to my children I can’t control myself either."
    "It’s fine, I won’t call the police."
    "But you have to leave here, and you need to leave it clean, as it was before you arrived."
    scene ch9_768-9 with hpunch
    mc "Yes, thank you very much, ma’am! God bless you!"
    "I hope everything goes well and you have a beautiful and healthy baby."
    play music something
    scene ch9_768-11- at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=4)
    mc "Mia!"
    pause
    scene ch9_768-13 with hpunch
    mc "Sorry!"
    "You’re lucky you’re pregnant, or else..."
    pause
    scene ch9_768-12 with dissolve
    mia "Let me go, [mc]! Let me gooo!"
    pause
    "*Gulp*"
    jump ch9_737mskip
label ch9_737mskip:
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 1.5 
    scene ch9_769 with dissolve
    d "Hey, finally you show up, hehe."
    d "What were you up to?"
    scene ch9_770 with dissolve
    mc "Erm, nothing, we were just exploring the place and..."
    if miatell < 2:
        jump ch9770mskip
    mia "{i}{size=-3}That fucking old hag is still staring over here.{/size}{/i}"
    mc "{i}{size=-3}Stop looking at her, you’re going to get us in trouble!{/size}{/i}"
    mia "{i}{size=-3}No fucking old hag is going to intimidate me.{/size}{/i}"
    mia "{i}{size=-3}If she wants trouble, bring it on, I love trouble.{/size}{/i}"
    mc "(This girl...)" with dissolve
    jump ch9770mskip
label ch9770mskip:
    k "Your card didn't work."
    scene ch9_771 with dissolve
    d "What?"
    k "It’s blocked or something."
    d "That doesn't have any sense."
    d "How dumb of me, I brought the old card."
    scene ch9_772 with dissolve
    d "Hey, [mc], I forgot my card at home. Do you happen to have some cash?"
    mc "Sure, how much do you need?"
    d "About 150 dollars."
    mc "Sure."
    d "Another thing, you can go pay it? My back hurts..."
    mc "Of course."
    mc "Pay what?"
    d "The board for [s]."
    scene ch9_773 with dissolve
    s "See? For renting things..."
    d "[s], better not say anything, you were the one who lost it."
    s "..."
    d "Go with [mc]."
    s "I don’t want to..."
    scene ch9_774 with dissolve
    d "Or maybe you want [mia] to go with you..."
    scene ch9_775 with dissolve
    s "O-okay, I’ll go with you."
    d "What happened? I thought you didn’t want to."
    s "Uhm, now I do..."
    scene ch9_776 with dissolve
    d "Haha."
    s "What?"
    d "Nothing, honey, hehe."
    stop music fadeout 3.0
    stop background fadeout 5.0
    scene blackscreen with dissolve
    pause
    if stephloving != "True":
        jump ch9_900sskip
    play background "/audio/beachsfx.ogg" fadein 1.0
    scene ch9_777 with dissolve
    play music scene2 fadein 2.0
    mc "What happened to the boogie?"
    s "I don’t know..."
    mc "Hmm..."
    pause
    scene ch9_778 with dissolve
    s "..."
    mc "You’re quiet... Did something happen?"
    s "No."
    pause
    scene ch9_780 with dissolve
    mc "Did [drelat] [d] scold you a lot?"
    s "..."
    pause
    mc "Hm?"
    s "It was a secret place..."
    mc "What thing?"
    s "..."
    pause
    scene ch9_778 with dissolve
    mc "I don’t understand what you’re trying to say, [s]."
    s "Hushh! You’re so dumb..."
    mc "What?"
    scene ch9_779 with dissolve
    s "I found the secret place and you let the girls take it over..."
    scene ch9_778 with dissolve
    pause
    mc "Oh... Sorry about that."
    pause
    mc "I couldn’t chase them away, it would have been rude."
    scene ch9_780 with dissolve
    mc "Do you want to go find another secret place when we get back?"
    s "There are no more secret places..."
    mc "We won’t know until we look for them."
    s "I already did, there aren’t any."
    mc "Uh..."
    pause
    mc "I’m sure we’ll find one, we just need to search more."
    pause
    scene ch9_781 with dissolve
    s "[k] thinks I went to tell [drelatks] that you were drinking."
    mc "Don’t pay attention to her. I know it wasn’t you."
    s "..."
    pause
    scene ch9_779 with dissolve
    s "Y-yes, it was me..."
    mc "Why did you do that?"
    s "It’s just..."
    scene ch9_778 with dissolve
    pause
    s "B-but I didn’t know you were doing that..."
    mc "What do you mean? What did you see us doing?"
    s "I saw you having sex with [k], but [drelatks] was already coming."
    s "I wanted to stop him but he knows when I’m lying."
    mc "It’s okay, it’s no big deal."
    pause
    mc "T-tomorrow I’ll take you to the fair, remember?"
    s "Yes..."
    pause
    mc "(I guess I can’t be mad at her this time.)" with dissolve
    mc "(It was supposed to be our secret place for doing 'sexy things,' as she calls it.)" with dissolve
    mc "(But in the end, I ended up having sex with [k] there, and the worst part is that she saw us.)" with dissolve
    mc "(She must feel betrayed. I really feel bad for her.) " with dissolve
    scene ch9_779 with dissolve
    s "You like big breasts, don’t you?"
    mc "What?"
    s "Do you like big boobs more?"
    mc "Why do you ask that?"
    scene ch9_778 with dissolve
    s "No, just wondering..."
    pause
    scene ch9_779 with dissolve
    s "I don’t have big boobs, heh..."
    mc "Your boobs are perfect, [s]."
    scene ch9_778 with dissolve
    pause
    scene ch9_781 with dissolve
    s "You’re a liar and unfaithful like [drelatks]."
    mc "Huh?"
    s "I don’t have boobs..."
    scene ch9_784 with dissolve
    mc "You do."
    mc "I-I like your boobs the way they are."
    s "Stop lying, everything you say is a lie..."
    mc "Uh..."
    mc "Let’s hurry, okay?"
    stop music fadeout 1.5
    stop background fadeout 3.0
    scene blackscreen with dissolve
    pause
    play music scene1 fadein 1.5
    jump ch9_900sskip
label ch9_900sskip:
    scene ch9_785 with dissolve
    mc "Are you sure it’s here?"
    s "Yes, I don’t lie like others..."
    mc "Uh..."
    scene ch9_786 with dissolve
    "How can I help you?"
    mc "I came to pay for a rented board."
    scene ch9_786- with dissolve
    "*Cough, cough, cough*"
    mc "Do you rent boards here, right?"
    scene ch9_786-- with dissolve
    mc "It was pink, a boogie board."
    "..."
    pause
    mc "We lost it on the beach."
    scene ch9_786--- with dissolve
    pause
    "..."
    mc "Are you okay?"
    scene ch9_786 with dissolve
    "What?"
    mc "I want to pay for a rented board..."
    scene ch9_787 with dissolve
    "Ah, yes, we rent surfboards here."
    mc "Yes... I came to pay for a lost board."
    "Ah! Yes, a girl came earlier to pay but the card didn’t go through."
    mc "Yes, I’m here instead of her, I brought cash."
    scene ch9_788 with dissolve
    "All our boards have a smart tag and-"
    mc "Really? Can you track it?"
    "Yes."
    mc "And can’t you recover it?"
    "No, bro. It’s currently moving, looks like someone took it."
    mc "I’ll pay for it, no problem."
    "It’s 150 plus the tag, so 200 dollars."
    scene ch9_789 with dissolve
    mc "Yes, of course..."
    mc "Here you go."
    "Thank you for your purchase."
    if stephloving != "True":
        jump ch9_1000sskip
    scene ch9_790 with dissolve
    mc "You’re welcome."
    mc "(And [s]?)" with dissolve
    pause
    scene ch9_791 with dissolve
    mc "[s]?"
    "I think I saw her go into the fitting room."
    scene ch9_792 with dissolve
    mc "[s], are you in there?"
    s "Yes."
    mc "I’ve paid, let’s go."
    s "I’m trying on clothes."
    mc "(Yeah, I think I can buy her something, I owe her after what happened.)" with dissolve
    mc "(I hope this gift helps make up for it a bit.)" with dissolve
    mc "(What I did was horrible...)" with dissolve
    mc "Okay, I’ll be waiting here."
    pause
    "..."
    pause
    mc "Just hurry up, there’s no place to sit here and my legs are a bit tired."
    pause
    s "Y-you can come in, there’s a bench for you to sit on."
label ch9s8:
    if _in_replay:
        show screen Replayexit
        $ stephloving = "True"
    stop music fadeout 1.5
    scene blackscreen with dissolve
    scene ch9_793 with Dissolve(4.0)
    play music sexy3 fadein 1.5
    mc "Oh..."
    mc "(Is that a bikini?)" with dissolve
    pause
    s "Close the door!" with hpunch
    mc "Oh, sorry!"
    scene ch9_795 with dissolve
    mc "Is that what you want me to buy you?"
    s "I’m not sure yet."
    scene ch9_797 with dissolve
    s "Uhm... Does it look nice?"
    mc "(That ass...)" with dissolve
    mc "Yeah, you look very pretty."
    scene ch9_796 with dissolve
    s "It’s the only bikini in my size they had."
    mc "Do you like it?"
    s "I do like it, but..."
    scene ch9_798 with dissolve
    mc "Do you want to take it?"
    s "I’m still not sure."
    mc "What’s the matter?"
    scene ch9_800 with dissolve
    s "It’s that I do like it..."
    s "What I don’t like is how it looks on me."
    mc "Why? I think it looks very nice."
    s "No, it doesn’t look good on me..."
    mc "Let me see."
    s "Uhmm, better not."
    mc "I bet it looks adorable on you."
    s "It’s not like that, it looks bad."
    scene ch9_801 with hpunch
    mc "Show me! {i}Or do you want me to turn into the perv-...{w=0.5} glutton shark..."
    s "Oh no! te-he."
    s "No, [mc], it’s just that it looks weird on me..."
    mc "Weird how?"
    scene ch9_802- with dissolve
    mc "Look how cute the bottom part looks."
    s "Do you like it?"
    mc "I love it."
    scene ch9_802-- with dissolve
    mc "Those oranges look tempting!"
    s "Oh, hehe. Don’t squeeze!"
    scene ch9_805 with dissolve
    mc "Then show me the top part."
    image ch9_805anim:
        "ch9_803" with dissolve
        1.75
        "ch9_805" with dissolve
        1.75
        repeat
    scene ch9_805anim with dissolve
    s "I’m embarrassed..."
    mc "Why?"
    mc "If it doesn’t fit, we’ll look for another one."
    s "There aren’t any more in my size, [mc]."
    pause
    scene ch9_806- with dissolve
    s "Te-he, don’t tickle me."
    scene ch9_807 with dissolve
    mc "Does this tickle you?"
    s "Not your hand, your mouth, te-hehe."
    image ch9_806anim:
        "ch9_806-" with dissolve
        1.75
        "ch9_807" with dissolve
        1.75
        repeat
    scene ch9_806anim with dissolve
    s "You’re giving me kisses and it tickles."
    mc "Then I’ll give you more kisses."
    s "Noo, hehehe."
    mc "(What a scent...)" with dissolve
    s "Stop, [mc], te-he."
    s "It’s not just tickling! hehehe."
    mc "Oh, really? And what else do you feel?"
    pause
    image ch9_808anim:
        "ch9_808" with dissolve
        1.75 
        "ch9_809" with dissolve
        1.75 
        repeat
    scene ch9_808anim with dissolve
    s "{i}{size=-3}Your kisses are making me start to feel sexy!{/size}{/i}"
    s "{i}{size=-3}I’m feeling aroused, {/size}{/i}hehehe."
    mc "(I couldn’t stand seeing her so sad, it broke my heart to think that, in a way, I had betrayed her.)" with dissolve
    mc "(I’m so glad she’s happy now.)" with dissolve
    pause
    scene ch9_810 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.48 zoom 1.002
        ease 1 yalign 0.52 zoom 1.0
        ease 1 yalign 0.48 zoom 1.002
        repeat
    mc "{i}Show me!"
    s "Nope."
    mc "*Rwawr* Show meee!" with hpunch
    s "Alright, hehe, fine! But stop already, hehehe!"
    scene ch9_811 with dissolve
    s "Look..."
    pause
    scene ch9_812 with dissolve
    mc "Oh..."
    pause
    mc "It’s a bit loose on you."
    scene ch9_813 with dissolve
    s "I-I told you..."
    mc "No, no..."
    s "I don’t like it, I don’t want it anymore."
    mc "(So that’s it...)" with dissolve
    mc "(She has a lot of complexes about the size of her breasts.)" with dissolve
    mc "(She lives with two women who have breasts bigger than their heads, anyone would feel insecure like that.)" with dissolve
    pause
    scene ch9_815 with dissolve
    mc "It can be adjusted."
    s "I don’t think it can be adjusted much more."
    mc "Yes, it can."
    s "E-even if you adjust it, it won’t look good..."
    scene ch9_816 with dissolve
    s "No, [mc]..."
    mc "Trust me."
    s "That’s not true."
    mc "Let me do what I have in mind and then, if you don’t like it, we’ll leave it and I’ll buy you something else, okay?"
    s "..."
    scene ch9_817 with dissolve
    s "O-okay, but it won’t look good no matter what you do."
    mc "We’ll see."
    pause
    scene ch9_818 with dissolve
    pause
    mc "How about now?"
    pause
    scene ch9_819 with dissolve
    mc "Look how cute you look!"
    s "..."
    pause
    scene ch9_820 with dissolve
    s "*Sniff*"
    mc "Do you like it?"
    s "They still look small..."    
    scene ch9_821 with dissolve
    mc "No, no... You look very cute, really!"
    s "I don’t want to look cute, I want to be sexy like [mia] and [k]..."
    mc "But..."
    mc "(I had forgotten she saw me with both of them...)" with dissolve
    mc "(Now she also thinks [mia] is more attractive to me...)" with dissolve
    pause
    scene ch9_822 with dissolve
    s "I want to have big boobs to please you..."
    mc "[s]..."
    mc "I like you the way you are, you don’t need to have bigger boobs."
    s "And why do you always do sexy stuff with [k] and only sometimes with me?"
    mc "What? That’s not..."
    pause
    mc "Allright, let’s talk about that."
    scene ch9_824 with dissolve
    pause
    mc "I like you a lot too, [s]."
    mc "Really."
    s "Yeah, I know..."
    scene ch9_825 with dissolve
    s "But not as much as you like [k]."
    s "And I know why..."
    s "It's because I don't have boobs."
    scene ch9_824 with dissolve
    mc "Where are you getting this from?"
    s "From today, at the beach..."
    s "You chose to stay with [k] and her friend instead of coming with me to get the surfboard."
    pause
    mc "I-I thought you were coming back..."
    s "I did come back but..."
    s "..."
    pause
    mc "(I feel bad...) " with dissolve
    pause
    scene ch9_826 with dissolve
    mc "I do like your boobs."
    pause
    scene ch9_828 with dissolve
    mc "It's just that since you never let me see them..."
    pause
    scene ch9_829 with dissolve
    s "And why do you want to see them? They're small..."
    mc "That doesn't matter."
    mc "Big, small, medium... they're all beautiful."
    scene ch9_825 with dissolve
    s "That's not true, everyone says that having big boobs is the best."
    mc "And who says that?"
    scene ch9_829 with dissolve
    s "Well... on the internet and stuff..."
    mc "Not everything on the internet is true."
    mc "Some of us like small breasts too. Sometimes more than big ones..."
    s "Hmm..."
    scene ch9_825 with dissolve
    s "Really?"
    mc "Yes."
    s "Swear it..."
    mc "I swear, I like small breasts just as much as big ones."
    scene ch9_825- with dissolve
    s "*You said more!*"
    mc "I said sometimes... I like them both equally!"
    mc "..."
    scene ch9_825--
    s "*Hmmh!*"
    scene ch9_825--- with dissolve
    play sound kissing fadein 0.5 volume 0.35 loop
    s "*Smnch*"
    pause
    stop sound fadeout 1.5
    scene ch9_825_1 with dissolve
    play sound kissing2 fadein 1.0 volume 0.35 loop
    mc "*Hsmch* {i}Your boobs are just as sexy as [k]'s. Just because they're small doesn’t make them any less beautiful."
    scene ch9_825_2 with dissolve
    s "*Lahl, lsch* {i}R-really?"
    scene ch9_825_3 with dissolve
    mc "*Smnch, hlsh* {i}Of course, I love them!"
    scene ch9_825_4 with dissolve
    mc "{i}Show them to me, I want to suck on them."
    scene ch9_825_5 with dissolve
    s "*Hmnch, lhahl, lsch* {i}I'm embarrassed..."
    scene ch9_825_6 with dissolve
    pause
    image ch9_825anim:
        "ch9_825_7" with Dissolve(0.5)
        0.65
        "ch9_825_6" with Dissolve(0.5)
        0.65
        "ch9_825_5" with Dissolve(0.5)
        0.65
        "ch9_825_6" with Dissolve(0.5)
        0.65
        "ch9_825_5" with Dissolve(0.5)
        0.65
        "ch9_825_4" with Dissolve(0.5)
        0.65
        "ch9_825_3" with Dissolve(0.5)
        0.65
        "ch9_825_2" with Dissolve(0.5)
        0.65
        "ch9_825_1" with Dissolve(0.5)
        0.65
        "ch9_825_2" with Dissolve(0.5)
        0.65
        "ch9_825_3" with Dissolve(0.5)
        0.65
        "ch9_825_4" with Dissolve(0.5)
        0.65
        "ch9_825_5" with Dissolve(0.5)
        0.65
        "ch9_825_6" with Dissolve(0.5)
        0.65
        "ch9_825_5" with Dissolve(0.5)
        0.65
        repeat
    image ch9_825anim2:
        "ch9_825_14" with Dissolve(0.5)
        0.65
        "ch9_825_13" with Dissolve(0.5)
        0.65
        "ch9_825_12" with Dissolve(0.5)
        0.65
        "ch9_825_13" with Dissolve(0.5)
        0.65
        "ch9_825_12" with Dissolve(0.5)
        0.65
        "ch9_825_11" with Dissolve(0.5)
        0.65
        "ch9_825_10" with Dissolve(0.5)
        0.65
        "ch9_825_9" with Dissolve(0.5)
        0.65
        "ch9_825_8" with Dissolve(0.5)
        0.65
        "ch9_825_9" with Dissolve(0.5)
        0.65
        "ch9_825_10" with Dissolve(0.5)
        0.65
        "ch9_825_11" with Dissolve(0.5)
        0.65
        "ch9_825_12" with Dissolve(0.5)
        0.65
        "ch9_825_13" with Dissolve(0.5)
        0.65
        "ch9_825_12" with Dissolve(0.5)
        0.65
        repeat
    scene ch9_825anim with dissolve
    s "*Lalh, lmnch, lshm*"
    s "{i}If I show them to you, will you get an erection?"
    mc "{i}Probably."
    pause
    s "*Smnch, lahl, lmnmh*"
    mc "(I love kissing her...) " with dissolve
    scene ch9_825anim2 with dissolve
    mc "(Her mouth is so soft I want to devour it...)" with dissolve
    s "*Smnch, slrch, lhlch*" with dissolve
    mc "(I'm literally drinking her saliva, it's so much that it's spilling over our lips...)" with dissolve
    stop sound fadeout 0.5
    scene ch9_825_15 with dissolve
    play sound "audio/character/s/soft/s_moan_soft_1.ogg" fadein 0.5 volume 0.5
    s "*Blah...* Alright, I'll show you my boobs."
    scene ch9_830 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0
        ease 5 yalign 1.0
        ease 3 yalign 0.45
    pause
    s "I-I told you they're not big..."
    mc "They’re very cute... {w=1.0} And sexy too."
    scene ch9_836 with dissolve
    mc "Come a bit closer, I want to see them up close..."
    s "Uhm..."
    mc "What’s wrong?"
    s "I’m a little embarrassed, [mc]..."
    mc "You don’t have to be embarrassed, [s]..."
    scene ch9_831 with dissolve
    s "*Uhmh*"
    mc "They look tempting..."
    scene ch9_832 with dissolve
    s "Uh..."
    scene ch9_833 with dissolve
    mc "Hmmh, delicious... *hmmh*."
    scene ch9_834 with dissolve
    pause
    scene ch9_835 with dissolve
    pause
    image ch9_831animn:
        "ch9_831" with dissolve
        1
        "ch9_832" with dissolve
        1
        "ch9_831" with dissolve
        1
        "ch9_832" with dissolve
        1
        "ch9_835" with dissolve
        1
        "ch9_833" with dissolve
        1
        "ch9_834" with dissolve
        1
        "ch9_833" with dissolve
        1
        "ch9_834" with dissolve
        1
        repeat
    scene ch9_831animn with dissolve
    s "*Uh, hmmh*"
    s "It feels weird. *uhmm*"
    mc "Don't you like me sucking on them?"
    s "I do like it!"
    pause
    mc "Hmm, I love your small breasts, they're delicious."
    s "*Uhmh* You’re just saying that to make me feel better."
    scene ch9_838 with dissolve:
        subpixel True
        xalign 0.45 yalign 0.5 zoom 1.015
        ease 0.65 xalign 0.55 yalign 0.5 zoom 1.015
        ease 0.65 xalign 0.45 yalign 0.5 zoom 1.015
        repeat
    mc "Stop saying that, [s]..."
    mc "If you keep saying that, I’ll stop sucking on them."
    s "O-okay, I won’t say it anymore."
    mc "Good girl."
    scene ch9_839 with dissolve
    mc "If I say I like them, you should believe me."
    scene ch9_840 with dissolve
    s "*Hmm* Okay..."
    image ch9_839anin:
        "ch9_839" with dissolve
        1.5
        "ch9_840" with dissolve
        1.5
        repeat
    scene ch9_839anin with dissolve
    s "You’ll have to buy me the bikini."
    mc "It looks beautiful on you, I knew you’d like it."
    s "N-no, *hmmh*, it’s just that I already soaked the panties."
    mc "Oh, then yes, we’ll have to take it, hehe..."
    s "*Uh, hmm, hm*"
    pause
    scene ch9_841 with dissolve
    pause
    scene ch9_842 with dissolve
    pause
    image ch9_842anim:
        "ch9_841" with dissolve
        1.5
        "ch9_842" with dissolve
        1.5
        repeat
    scene ch9_842anim with dissolve
    s "It feels good when you suck on my breasts and touch my vagina..."
    s "*Hmh* It's sexier..."
    pause
    scene ch9_843 with dissolve
    pause
    scene ch9_844 with dissolve
    pause
    image ch9_844anim:
        "ch9_843" with dissolve
        1.5
        "ch9_844" with dissolve
        1.5
        repeat
    scene ch9_844anim with dissolve
    mc "These tasty little tits, *yum*."
    s "*Hmh* Hehe, the perverted shark is back."
    mc "-Glutton."
    s "Ah, yes, glutton, hehe."
    pause
    scene ch9_838 with dissolve
    mc "I’ve had enough of boobs, I want to eat other parts too."
    s "And what does the shark want to eat now?"
    mc "I want your little butt..."
    s "Hehe, you’re a glutton and a pervert, Mr. Shark."
    mc "Yes, hehe... Now turn around."
    scene ch9_845 with dissolve
    s "Like this?"
    mc "Bend over a little."
    pause
    scene ch9_846 with dissolve
    s "Like this?"
    scene ch9_847 with dissolve
    mc "Not so much..."
    mc "Uhm...{w=1.0} I mean, just like that!"
    s "Okay."
    mc "(Wow, look at this ass...)" with dissolve
    s "And what should I do now?"
    scene ch9_846 with dissolve
    mc "N-nothing, just stay like that for a while."
    s "Alright."
    scene ch9_848 with dissolve
    mc "Hmmh, what a nice little butt."
    s "Uh..."
    scene ch9_849 with dissolve
    s "Don’t put your mouth there, hehe, it tickles."
    image ch9_848anim:
        "ch9_848" with dissolve
        1.5
        "ch9_849" with dissolve
        1.5
        repeat
    scene ch9_848anim with dissolve
    s "Hehe, *hmmh*"
    mc "Hmh, hmmmh."
    pause
    scene ch9_850 with dissolve
    pause
    scene ch9_851 with dissolve
    pause
    image ch9_851anim:
        "ch9_850" with dissolve
        1.5
        "ch9_851" with dissolve
        1.5
        repeat
    scene ch9_851anim with dissolve
    s "What are you doing, [mc]?"
    mc "I really like your little butt."
    s "My butt?"
    mc "Yeah, I love it."
    s "You’re so weird, hehe."
    pause
    scene ch9_847 with dissolve
    mc "*Hmmh* what a nice little butt you have, [s], I can’t get tired of saying it."
    s "Hmm..."
    scene ch9_846 with dissolve
    s "You said you liked my boobs more."
    mc "No, I like your boobs a lot, but I love your bootie too."
    mc "Can I take off your panties?"
    s "Hmm, okay... but you’ll see my butt like this."
    scene ch9_847- with dissolve
    pause
    mc "Oh..."
    s "I’m embarrassed, [mc]..."
    mc "(Look at that butt... So delicious!)" with dissolve
    s "Don’t look at it too much, I’m embarrassed..."
    scene ch9_852 with dissolve
    s "Uhmh... N-no..."
    scene ch9_853 with dissolve
    s "[mc]..."
    image ch9_853anim:
        "ch9_852" with dissolve
        1.5
        "ch9_853" with dissolve
        1.5
        repeat
    scene ch9_853anim with dissolve
    play sound kissing2 volume 0.2 loop
    play voicefx "audio/wavs/s/smoansoft.ogg" fadein 1.0 volume 0.7 loop
    mc "Hmmh..."
    s "*Uhm* [mc], d-don’t do that..."
    s "*Uhm, hmmh*"
    pause
    scene ch9_855 with dissolve
    s "*Uh, hmh*"
    scene ch9_856 with dissolve
    mc "*Smnch*"
    image ch9_855anim:
        "ch9_855" with dissolve
        1.5
        "ch9_856" with dissolve
        1.5
        repeat
    scene ch9_855anim with dissolve
    s "Don’t kiss me there, [mc]..."
    mc "Doesn’t it feel good?"
    s "Uhm... It does feel good but..."
    pause
    scene ch9_860 with dissolve
    s "Ah... N-no, [mc]..."
    scene ch9_861 with dissolve
    mc "*Lahl* Don’t you like it?"
    s "It’s not that... *hmmh*, it’s just not there..."
    image ch9_861anim:
        "ch9_860" with dissolve
        1.5
        "ch9_861" with dissolve
        1.5
        repeat
    scene ch9_861anim with dissolve
    s "*Uhmm, uh* Not there, [mc]."
    mc "Do you want me to stop? *lahl, lhml*"
    s "U-um... But I think you’re at the wrong spot."
    mc "*Lhal, lhmm* But do you like it?"
    s "*Uhm, hmh* Yes..."
    s "Is it dirty?"
    mc "*Lhm, lhhl* Not at all."
    pause
    play sound kissing2 volume 0.5 loop
    scene ch9_857 with dissolve
    mc "*Lhal, lhmm*"
    scene ch9_858 with dissolve
    s "*Uh, hmmh*"
    scene ch9_859 with dissolve
    s "*Ah, uhm* D-don’t put your tongue in..."
    image ch9_858anim:
        "ch9_857" with dissolve
        1.5
        "ch9_858" with dissolve
        1.5
        "ch9_859" with dissolve
        1.5
        repeat
    scene ch9_858anim with dissolve
    mc "*Lhl, lhm* Just a little..."
    s "*Hmh* A little..."
    mc "(I can barely get the tip of my tongue in, it’s so tight...)" with dissolve
    s "That... {w=0.5}*Uh*{w=0.5}, it’s very lewd, [mc]..."
    mc "You like lewd things, don’t you?"
    s "*Uh, hmuh* Y-yes, I do..."
    s "And you?"
    mc "*Lhah* I love them."
    pause
    stop voicefx fadeout 1.0
    stop sound fadeout 0.5
    scene ch9_862 with dissolve
    mc "Hah... (That was... wow.)"
    pause
    s "My legs are starting to get tired..."
    mc "Just wait a little longer."
    s "Okay."
    jump beforech9_863stf1_

init python:
    def ch9_863stf1_(trans, st, at):  
        trans.set_child("ch9_863stf1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 37:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.8, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_863stf2_(trans, st, at):  
        trans.set_child("ch9_863stf2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 37:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.9, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_863stf3_(trans, st, at):  
        trans.set_child("ch9_863stf3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 37:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.55, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_863stf4_(trans, st, at):  
        trans.set_child("ch9_863stf4_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 37:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.73, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_863stf5_(trans, st, at):  
        trans.set_child("ch9_863stf5_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 37:
            store.frame_num = 1   
        if store.frame_num == 10:
            sound_files = ["audio/sex/fuck_naked5.ogg", "audio/sex/fuck_naked11.ogg", "audio/sex/fuck_naked10.ogg", "audio/sex/fuck_naked8.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            renpy.sound.set_volume(0.73, channel='sound')  
            renpy.sound.play(random_sound)     
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

screen ch9_863stf1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.007945) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_863stf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_863stf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_863stf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_863stf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_863stf5_cont") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"    
screen ch9_863stf2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.007945) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_863stf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_863stf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_863stf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_863stf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_863stf5_cont") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_863stf3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.007945) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_863stf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_863stf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_863stf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_863stf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_863stf5_cont") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
screen ch9_863stf4_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.007945) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" action Jump("ch9_863stf5_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_863stf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_863stf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_863stf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_863stf5_cont") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_863stf5_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.007945) style "textbutton_choice"   
    hbox:
        yalign 0.05
        xalign 0.59
        textbutton "Pov 5" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.69
        textbutton "Pov 4" action Jump("ch9_863stf4_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_863stf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_863stf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_863stf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("ch9_863stf5_cont") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice"   
label beforech9_863stf1_:
    $ anim_speed = 0.011
    image ch9_863stf1_:
        function ch9_863stf1_
    image ch9_863stf2_:
        function ch9_863stf2_
    image ch9_863stf3_:
        function ch9_863stf3_
    image ch9_863stf4_:
        function ch9_863stf4_
    image ch9_863stf5_:
        function ch9_863stf5_
    scene ch9_863- with dissolve
    mc "(I want to fuck her thights so bad.)" with dissolve
    mc "Spread your legs a little."
    s "Are you going to put your penis between them?"
    mc "Yeah."
    scene ch9_863stf2_ with dissolve
    play voicefx "audio/wavs/s/smoansoft.ogg" fadein 1.0 volume 0.7 loop
    s "*Huh, uh* You really like rubbing your penis between my legs."
    mc "*hmm* I love it."
    s "Hehe..."
    s "And also on my butt."
    mc "That’s right..."
    s "*Uh, uh, uh* So does that mean you also love my legs?"
    mc "Correct{w=0.5}, *hmh*{w=0.5}, I love the cute and sexy legs of my little [srelat] [s]."
    s "*Giggle*"
    s "And my ass."
    mc "Haha, yes, I also love your cute ass."
    mc "(We’re making quite a bit of noise...)" with dissolve
    mc "(These juicy cheeks really clap loudly.)" with dissolve
    pause
    s "*Uhm, uh* It’s very slippery..."
    mc "What’s very slippery?"
    s "Your... dick, hehe."
    s "Do you know why? *Giggle*"
    s "{i}Because I’m very wet..."
    s "{i}You have my stuff all over your dick,{/i} hehe.."
    mc "Your fluids?"
    s "Yep, hehe."
    mc "*Uh* That’s very lewd."
    s "Yes, hehe..."
    pause
    scene ch9_863stf1_ with dissolve
    mc "So good..."
    s "*Uh, uh* I also feel good..."
    s "Perverted things feel really good..."
    mc "(I’m in a store’s dressing room doing sexual things with my little [srelat].)" with dissolve
    mc "([s] is right, the most pervy things are the best...)" with dissolve
    mc "(I need to cum, if I don’t release now I’ll have to jerk off.)" with dissolve
    scene ch9_863stf3_ with dissolve
    pause
    s "*Uh, uh* [mc]."
    mc "Yes?"
    s "We’ve been in here for a while,{w=0.5} *huh, uh*{w=0.5}, [drelatks] is going to get mad if we don’t get out soon."
    mc "(Shit, that’s right! Also, we can’t take too long or the store clerk might get suspicious.)" with dissolve
    mc "(But I don’t care, I’m not leaving until I cum.)" with dissolve
    pause
    s "I thought of something to tell [drelatks] as an excuse."
    mc "Oh, really?"
    s "Yes, we’ll say that{w=0.5}, *uh, huh*{w=0.5}, I was trying on a lot of clothes."
    s "*Huh* I always do that anyway."
    scene ch9_863stf4_ with dissolve
    mc "Oh... how clever. (It’s actually a good idea.)"
    s "*Hmh* I have perverted intelligence, hehe."
    mc "Haha, *Hmh*."
    pause
    s "*Uh, uh* My legs are shaking."
    mc "Do you want to rest?"
    s "*Uhm, Uh, huh* I do want to rest but... it feels good."
    scene ch9_863stf5_ with dissolve
    mc "*Uh..* Me too, do you want me to go faster?"
    s "Yes, rub faster, [mc]."
    mc "Alright..."
    $ anim_speed = 0.0079925
    s "*Huh...*{w=0.5} *Uh, hmmh, huh*"
    mc "*Hmh, hmgh* Does it feel good?"
    s "*Uhh* Yes... *Huh, huh*"
    call screen ch9_863stf5_ with dissolve

    
label ch9_863stf1_:
    scene ch9_863stf1_ with dissolve
    call screen ch9_863stf1_ with dissolve
label ch9_863stf2_:
    scene ch9_863stf2_ with dissolve
    call screen ch9_863stf2_ with dissolve
label ch9_863stf3_:
    scene ch9_863stf3_ with dissolve
    call screen ch9_863stf3_ with dissolve
label ch9_863stf4_:
    scene ch9_863stf4_ with dissolve
    call screen ch9_863stf4_ with dissolve
label ch9_863stf5_:
    scene ch9_863stf5_ with dissolve
    call screen ch9_863stf5_ with dissolve   
    
label ch9_863stf5_cont:
    s "I can’t hold my legs anymore, [mc]..."
    s "Can we take a break for a moment, please?" 
    stop voicefx fadeout 1.5
    $ anim_speed += 0.005
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.005
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed += 0.01
    pause 0.005 
    $ anim_speed = 999999999999
    pause
    scene ch9_863 with dissolve
    s "I'm so tired."
    mc "Let's rest a bit."
    s "Uhmm... [mc]..."
    mc "Yes?"
    s "When we were at the beach, I sucked your dick but you didn’t lick my pussy..."
    mc "(Right, [k] and her friend showed up and interrupted us... Damn, that was close.)" with dissolve
    mc "Do you want me to do it now?"
    s "{i}{size=-1}Yes!"
    scene ch9_864 with dissolve:
        subpixel True
        zoom 1.0 yalign 0.5 xalign 0.5
        ease 0.5 zoom 1.015 xalign 0.5 yalign 1.0
        ease 0.5 zoom 1.0 xalign 0.5 yalign 0.5
    mc "*Hmph* Let's lay you down here so those pretty legs can rest."
    s "Te-hehe..."
    s "I wish you were my boyfriend."
    mc "Would you like to have a boyfriend like me?"
    s "Yes."
    s "But just like you."
    s "Named [mc] and handsome and strong just like you."
    mc "Aww, that's very sweet."
    play sound kissing fadein 0.5 volume 0.5 loop
    scene ch9_865 with dissolve
    s "*Hmm, smnch*"
    pause
    stop sound fadeout 0.5
    scene ch9_867 with dissolve
    mc "Spread those legs wide..."
    mc "(Wow, she's quite wet...)" with dissolve
    pause
    scene ch9_868 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.015
        ease 1 yalign 0.5 zoom 1.00
        ease 1 yalign 0.0 zoom 1.015
        repeat
    play voicefx "audio/wavs/s/smoansoft.ogg" fadein 1.0 volume 0.85 loop
    play sound kissing2 loop volume 0.5 fadein 0.5
    mc "*Hmsh, lmsh* (I'm soaking my whole mouth with her fluids...)" with dissolve
    s "{i}*Huh, hmmh* {i}{size=-2}So good..."
    pause
    mc "(The person in charge must be wondering why we're taking so long...)" with dissolve
    s "{i}{size=-2}*Hmah, hah, hmmh*"
    s "*Hmh, uh* Use your tongue higher up, [mc]..."
    play sound kissing2 loop volume 0.25 fadein 0.5
    scene ch9_869 with dissolve
    mc "Here?"
    scene ch9_870 with dissolve
    s "On my clit."
    mc "(She's talking about her clitoris...)" with dissolve
    image ch9_869anim:
        "ch9_869" with dissolve
        1.75
        "ch9_870" with dissolve
        1.75
        repeat
    image ch9_871anim:
        "ch9_871" with dissolve
        1.75
        "ch9_872" with dissolve
        1.75
        repeat
    scene ch9_869anim with dissolve:
        subpixel True
        xalign 0.4 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.6 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.4 yalign 0.5 zoom 1.005
        repeat
    s "*Uhmm, hmmh* Y-yes, there... *uh, hmh*"
    mc "(She loves it when I lick her little clitoris in circles...)" with dissolve
    pause
    scene ch9_871anim with dissolve:
        subpixel True
        xalign 0.4 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.6 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.4 yalign 0.5 zoom 1.005
        repeat
    mc "*Umch, shlp*"
    s "*Huh* I-it feels so good, [mc]."
    s "*Uhh, hmmh* When you suck hard, it feels good too..."
    pause
    scene ch9_874 with dissolve
    mc "I can’t forget these nice little tits..." with dissolve
    scene ch9_873 with dissolve
    s "*Huh, hmh*..."
    image ch9_874anim:
        "ch9_874" with dissolve
        1.75
        "ch9_873" with dissolve
        1.75
        repeat
    scene ch9_874anim with dissolve:
        subpixel True
        xalign 0.4 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.6 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.4 yalign 0.5 zoom 1.005
        repeat
    mc "Do you like it when I play with your tits?"
    s "Yes...{w=0.5} *huh*{w=0.5}, I like it..."
    s "I-I, *huh*, like it a lot..."
    s "*Huh, uhh*"
    pause
    image ch9_876anim:
        "ch9_876" with dissolve
        1.75
        "ch9_875" with dissolve
        1.75
        repeat
    scene ch9_876anim with dissolve:
        subpixel True
        yalign 0.4 xalign 0.5 zoom 1.005
        ease 1.75 yalign 0.6 xalign 0.5 zoom 1.005
        ease 1.75 yalign 0.4 xalign 0.5 zoom 1.005
        repeat
    mc "*Hmsh, hmshl, lhm*"
    s "*Uuh, uhmh*..."
    mc "Almost done?"
    s "Uhm, no.. I mean, yes...*huh*"
    mc "*Slrp, lhmm*"
    s "*Huh* Keep licking..."
    s "A-and I'll suck your dick later, okay?"
    mc "Okay. (She's so cute...)"
    pause
    image ch9_878anim:
        "ch9_878" with Dissolve(0.7)
        1.2
        "ch9_877" with Dissolve(0.7)
        1.2
        repeat
    image ch9_878anim2:
        "ch9_878" with Dissolve(0.7)
        1.2
        "ch9_877" with Dissolve(0.7)
        0.7
        "ch9_878" with Dissolve(0.7)
        0.7
        "ch9_877" with Dissolve(0.7)
        0.7
        "ch9_878" with Dissolve(0.7)
        0.7
        "ch9_877" with Dissolve(0.7)
        0.7
        repeat
    scene ch9_878anim with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.015
        ease 0.75 yalign 0.5 zoom 1.00
        ease 0.75 yalign 0.0 zoom 1.015
        repeat
    s "*Hmh, huh, hmhm*"
    mc "(I think she's close...)"
    pause
    image ch9_878anim2mv:
        "ch9_878anim2"
        xalign 0.4 yalign 0.5 zoom 1.015
        ease 0.3 xalign 0.6
        ease 0.3 xalign 0.4
        repeat 2

    scene ch9_878anim2mv with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0 zoom 1.015
        ease 0.75 yalign 0.5 zoom 1.00
        ease 0.75 yalign 0.0 zoom 1.015
        repeat
    play voicefx smoancum volume 1.5 fadein 0.5
    s "*Uhmm, hmh, hmgh!*"
    mc "*lmh, lmh, lmh*"
    pause
    stop sound fadeout 0.7
    scene ch9_877 with dissolve
    s "*Huh...*"
    s "That felt really good, [mc]..."
    pause
    scene ch9_879 with dissolve
    mc "You came?"
    s "Huh?"
    mc "Did it feel good?"
    s "Ah... yes, I came..."
    pause
    play sound kissing2 fadein 1.0 volume 0.5 loop
    scene ch9_880 with dissolve
    mc "*Lhm* Are you going to suck my dick now?"
    scene ch9_881 with dissolve
    mc "*Lah*"
    s "Y-yeah..."
    scene ch9_882 with dissolve
    mc "*Lhmm*"
    scene ch9_883 with dissolve
    mc "*Hmm*"
    scene ch9_884 with dissolve
    mc "*Hmch*"
    s "*Huh...*"
    image ch9_880anim:
        "ch9_881" with dissolve
        1.7
        "ch9_882" with dissolve
        1.7
        "ch9_883" with dissolve
        1.7
        "ch9_881" with dissolve
        1.7
        "ch9_882" with dissolve
        1.7
        "ch9_883" with dissolve
        1.7
        "ch9_884" with dissolve
        1.75
        repeat
    scene ch9_880anim with dissolve:
        subpixel True
        xalign 0.4 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.6 yalign 0.5 zoom 1.005
        ease 1.75 xalign 0.4 yalign 0.5 zoom 1.005
        repeat
    s "I thought you were lying, but you really do like my tits, hehe."
    mc "Your little tits are the best, I love them."
    s "Yeah, hehe, I can see that now."
    pause
    s "*Huh* When you suck them, I start to feel sexy again..."
    mc "Then I'll keep sucking them a little longer."
    mc "(My balls are burning...)" with dissolve
    mc "(I want to cum already, I'll tell her to suck me off so I can release and we can leave.)" with dissolve
    s "Kiss me, [mc]..."
    mc "You really like kisses, huh?"
    s "Yes."
    scene ch9_885 with dissolve
    s "*Hmch*"
    pause
    scene ch9_886 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.45 zoom 1.01
        ease 0.75 yalign 0.6 xalign 0.5 
        ease 0.75 yalign 0.4 xalign 0.5 
        repeat
    mc "(I'm so, so aroused...)" with dissolve
    pause
    stop sound fadeout 0.5 
    stop voicefx fadeout 0.5
    scene ch9_887 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.45 zoom 1.01
        ease 0.75 yalign 0.6 xalign 0.5 
        ease 0.75 yalign 0.4 xalign 0.5 
        repeat
    mc "Hah... What delicious kisses..."
    s "Hehe..."
    mc "(I'm shaking, I feel like my cock is going to fly off like a rocket.)" with dissolve
    mc "(God, her lips are so pretty...)" with dissolve
    mc "(Soon they’ll be wrapped around the tip of my dick.)" with dissolve
    s "[mc], your cock feels so hot..."
    mc "My cock?"
    s "Yes..."
    scene ch9_888 with dissolve
    pause
    scene ch9_889 with dissolve
    pause
    scene ch9_888 with dissolve
    pause
    scene ch9_889 with dissolve
    pause
    image ch9_888anim:
        "ch9_888" with dissolve
        1.5
        "ch9_889" with dissolve
        1.5
        repeat
    image ch9_888anim2:
        "ch9_888" with dissolve
        0.7
        "ch9_889" with dissolve
        0.7
        repeat
    scene ch9_888anim with dissolve
    mc "(My hips are moving on their own, I feel like an idiot...)" with dissolve
    mc "(A girl with much less experience is making me act like this.)" with dissolve
    pause
    mc "(But it’s normal, considering how beautiful she is, it would be strange not to feel anything.)" with dissolve
    pause
    scene ch9_888anim2 with dissolve
    mc "*Hmgh... hmngh..*" with dissolve
    s "*Huh, hmh*"
    pause
    jump beforech9_888anim

init python:
    def ch9_866ssf1_(trans, st, at):  
        trans.set_child("ch9_866ssf1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [11, 31]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    def ch9_866ssf2_(trans, st, at):  
        trans.set_child("ch9_866ssf2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [11, 31]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 

init python:
    def ch9_866ssf3_(trans, st, at):  
        trans.set_child("ch9_866ssf3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [11, 31]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_866ssf1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0079925) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_866ssf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_866ssf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_866ssf1") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_866ssf2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0079925) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_866ssf3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_866ssf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_866ssf1") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_866ssf3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0079925) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_866ssf2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_866ssf1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_866ssf1") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label beforech9_888anim:
    image ch9_866ssf1_:
        function ch9_866ssf1_
    image ch9_866ssf2_:
        function ch9_866ssf2_
    image ch9_866ssf3_:
        function ch9_866ssf3_
    $ anim_speed = 0.02
    play voicefx smoansoft loop fadein 1.0 volume 0.7
    play sound kissing loop fadein 0.5 volume 0.3
    scene ch9_866ssf3_ with hpunch
    mc "*Hmnh!*"
    s "*Hmnch, slmh*"
    mc "(She's hugging me tightly...)" with dissolve
    mc "(She must love the feeling of my dick rubbing against her little pussy...)" with dissolve 
    pause
    scene ch9_866ssf2_ with dissolve
    s "*Hmnchm, lhmsh* Uh, [mc], this feels really good."
    mc "*Hmmh* Yes..."
    mc "(It feels like we're really fucking...)" with dissolve 
    mc "(Damn, this is too much... I'm so close to doing it...)" with dissolve
    mc "(How would it feel to fuck this little pussy?)" with dissolve
    mc "(No! Stop thinking about that...)" with dissolve
    mc "(That's a line I can't cross...)" with dissolve
    pause
    scene ch9_866ssf1_ with dissolve
    call screen ch9_866ssf1_ with dissolve
define currentch9866pos = "False"
label ch9_866ssf1_:
    $ currentch9866pos = "True"
    scene ch9_866ssf1_ with dissolve
    call screen ch9_866ssf1_ with dissolve
label ch9_866ssf2_:
    $ currentch9866pos = "False"
    scene ch9_866ssf2_ with dissolve
    call screen ch9_866ssf2_ with dissolve
label ch9_866ssf3_:
    $ currentch9866pos = "False"
    scene ch9_866ssf3_ with dissolve
    call screen ch9_866ssf3_ with dissolve

label beforech9_866ssf1:
    $ anim_speed = 0.0075
    mc "*Hnngh*"
    if currentch9866pos == "False":
        scene ch9_866ssf3_ with dissolve
    mc "(I shouldn't do this...)" with dissolve
    mc "(Although, this is already wrong anyway, right?...)" with dissolve
    mc "(Whether I do it or not, the sin is already committed, right?...)" with dissolve
    pause
    stop sound fadeout 0.5
    scene ch9_893 with hpunch
    mc "*¡Hngh!* (No, no... I'm not going to do it, I'm just going to...)" with dissolve
    s "*Uhmm*"
    scene ch9_895 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.0015
        ease 0.5 xalign 0.5 yalign 0.5 zoom 1.0
        ease 0.5 xalign 0.5 yalign 0.5 zoom 1.0015
        repeat
    mc "*Hah.. hah..* (I can hear my own heart beating.)"
    s "Huh.. uhm..."
    pause
    scene ch9_892 with dissolve
    mc "(Damn!...)" with dissolve
    pause
    jump afterch9_896
init python:
    def ch9_896sgp1_(trans, st, at):  
        trans.set_child("ch9_896sgp1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [11, 31]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_896sgp2_(trans, st, at):  
        trans.set_child("ch9_896sgp2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [11, 31]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
init python:
    def ch9_896sgp3_(trans, st, at):  
        trans.set_child("ch9_896sgp3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1   
        if store.frame_num in [11, 31]:
            sound_files = ["audio/masturbating/cutmastrubating5.ogg", "audio/masturbating/cutmastrubating2.ogg", "audio/masturbating/cutmastrubating3.ogg", "audio/masturbating/cutmastrubating4.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound
            atl_play_sound(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_896sgp1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0079925) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_896sgp3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_896sgp2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_896sgp3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_896sgp2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0079925) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_896sgp3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_896sgp1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_896sgp3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_896sgp3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.025) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.011) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.0079925) style "textbutton_choice"  
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_896sgp2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_896sgp1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("beforech9_896sgp3_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label afterch9_896:
    $ anim_speed = 0.015
    image ch9_896sgp1_:
        function ch9_896sgp1_
    image ch9_896sgp2_:
        function ch9_896sgp2_
    image ch9_896sgp3_:
        function ch9_896sgp3_
    scene ch9_896sgp1_ with dissolve
    mc "(She started masturbating.)" with dissolve
    mc "(How sexy she looks!...)" with dissolve
    pause
    mc "(I'm just rubing it, that's all.)" with dissolve
    s "*Huh, hmmmh* Don't push so hard, [mc]..." with dissolve
    pause
    scene ch9_896sgp2_ with dissolve
    mc "*Hmgh* (My hips keep moving on their own again...)" with dissolve
    mc "(I want to fuck her so bad...)" with dissolve
    s "*Huh, huh, hmmh* D-don't stop rubbing me..." with dissolve
    mc "(It looks like she's going to cum again...)" with dissolve
    pause
    scene ch9_896sgp3_ with dissolve
    s "*Huh, hmmmh, hmm*"
    mc "(I'm so close to doing it... I'm going to lose control...)" with dissolve
    mc "(I need to calm down... Calm down, calm down...)" with dissolve
    call screen ch9_896sgp3_ with dissolve

label ch9_896sgp1_:
    scene ch9_896sgp1_ with dissolve
    call screen ch9_896sgp1_ with dissolve
label ch9_896sgp2_:
    scene ch9_896sgp2_ with dissolve
    call screen ch9_896sgp2_ with dissolve
label ch9_896sgp3_:
    scene ch9_896sgp3_ with dissolve
    call screen ch9_896sgp3_ with dissolve

label beforech9_896sgp3_:
    image ch9_893anim:
        "ch9_893" with Dissolve(0.7)
        1.0
        "ch9_894" with Dissolve(0.7)
        1.0
        repeat
    scene ch9_893anim with vpunch:
        subpixel True
        xalign 0.5 yalign 0.5 zoom 1.005
        ease 1.0 xalign 0.5 yalign 0.5 zoom 1.0
        ease 1.0 xalign 0.5 yalign 0.5 zoom 1.005
        repeat
    s "*Ouh...*"
    mc "(I can't stand it anymore...)" with dissolve
    s "N-no, [mc], it hurts like that."
    pause
    scene ch9_897 with dissolve
    s "*Hnmh, ah*"
    mc "(My pulse is racing.)" with dissolve
    pause
    stop voicefx fadeout 0.5
    scene ch9_898 with dissolve
    s "N-no, [mc], it hurts."
    mc "(All I can think about is fucking, screwing, fornicating, coupling!)" with dissolve
    scene ch9_900 with dissolve
    s "*Hmnnh*"
    s "Y-you're acting strange, [mc]."
    s "D-don't push so hard, it hurts."
    pause
    scene ch9_901- with vpunch:
        xalign 0.5 yalign 0.5 zoom 1.0
        ease 0.5 zoom 1.05 xalign 0.5 yalign 0.5
        ease 0.5 zoom 1.025 xalign 0.5 yalign 0.5
    s "*Uhmm!*"
    s "[mc], a-are you going to put it in?"
    mc "*Hnghh*"
    s "Are we going to have sex?"
    mc "Eh... s-sex?"
    mc "(God, I lost control for a second.)"
    pause
    play voicefx smoancum fadein 0.1 volume 0.85
    scene ch9_902 with hpunch
    s "*Ahmmh!*"
    pause
    scene ch9_901 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.5
        ease 2 zoom 1.0 xalign 0.5 yalign 0.5
    pause 1.5
    s "It felt really good, hehe..."
    mc "S-sorry..."
    pause
    scene ch9_903 with dissolve
    mc "(I... was going to do it...)" with dissolve
    s "Uhh..."
    pause
    show ch9_904 with dissolve
    mc "(I'm shaking.)" with dissolve
    mc "(I really was going to do it...)" with dissolve
    pause
    scene ch9_905 with dissolve
    mc "{i}{size=-3}I want to cut off my dick..."
    s "[mc], why am I wet?"
    s "You didn't piss on me, did you?"
    s "Hm?"
    s "Did something get in your eye?"
    pause
    scene ch9_906 with dissolve
    s "[mc], are you okay?"
    mc "Yeah, yeah, I'm just rubbing my eyes."
    mc "Put your clothes on, we need to go."
    s "But..."
    scene ch9_907 with dissolve
    mc "Uh..."
    s "Now I'm going to suck your dick."
    mc "We need to leave, [s]."
    s "I'll be quick."
    scene ch9_908 with dissolve
    s "I've already felt good twice, and you haven't felt good even once, that's not fair."
    mc "But..."
    play sound kissing2 fadein 0.5 loop volume 0.5
    scene ch9_908- with dissolve
    s "*Lhal*"
    scene ch9_908-- with dissolve
    s "*Lah*"
    scene ch9_908--- with dissolve
    s "*Lahb*"
    scene ch9_908---- with dissolve
    s "*Smch*"
    image ch9_908anim:
        "ch9_908-" with Dissolve(0.5)
        1.2
        "ch9_908--" with Dissolve(0.5)
        1.2
        "ch9_908---" with Dissolve(0.5)
        1.2
        "ch9_908----" with Dissolve(0.5)########
        1.2
        "ch9_908-" with Dissolve(0.5)
        1.2
        "ch9_908--" with Dissolve(0.5)
        1.2
        "ch9_908---" with Dissolve(0.5)
        1.2
        "ch9_908----" with Dissolve(0.5)#######
        1.2
        "ch9_908---" with Dissolve(0.5)
        1.2
        "ch9_908--" with Dissolve(0.5)
        1.2
        "ch9_908-" with Dissolve(0.5)
        1.2
        "ch9_908----" with Dissolve(0.5)#######
        1.2
        "ch9_908---" with Dissolve(0.5)
        1.2
        "ch9_908--" with Dissolve(0.5)
        1.2
        repeat
    play sound kissing2 fadein 0.5 loop volume 0.5
    scene ch9_908anim with dissolve
    mc "*Uh...*"
    mc "{i}W-we need to leave..."
    s "*Lhm, blah, lmah, smnch*"
    mc "{i}Ah..."
    pause
    stop sound fadeout 0.5
    jump beforech9_900sbj

init python:
    store.last_played_sound = None
    store.last_played_sound2 = None
    store.last_played_sound3 = None
    def ch9_900sbj1_(trans, st, at):  
        trans.set_child("ch9_900sbj1_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_900sbj2_(trans, st, at):  
        trans.set_child("ch9_900sbj2_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
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
    def ch9_900sbj3_(trans, st, at):  
        trans.set_child("ch9_900sbj3_{}".format(store.frame_num))
        store.frame_num += 1
        if store.frame_num > 40:
            store.frame_num = 1
        if store.frame_num == 6:
            sound_files = ["audio/wavs/bj_62.ogg", "audio/wavs/bj_64.ogg", "audio/wavs/bj_66.ogg", "audio/wavs/bj_68.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound2])
            store.last_played_sound2 = random_sound  
            atl_play_sound(random_sound)()        
        if store.frame_num == 26:
            sound_files = ["audio/wavs/bj_52.ogg", "audio/wavs/bj_80.ogg", "audio/wavs/bj_60.ogg", "audio/wavs/bj_69.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound])
            store.last_played_sound = random_sound  
            atl_play_sound(random_sound)()
        if store.frame_num == 15:
            sound_files = ["audio/wavs/s/sbjmoan_1.ogg", "audio/wavs/bj_5.ogg", "audio/wavs/s/sbjmoan_4.ogg", "audio/wavs/bj_7.ogg"]
            random_sound = renpy.random.choice([sound for sound in sound_files if sound != store.last_played_sound3])
            random_chance = renpy.random.random()
            if random_chance < 0.1:
                store.last_played_sound3 = random_sound
                atl_play_voicefx(random_sound)()
        return store.anim_speed
    def update_anim_speed(value):
        store.anim_speed = value 
screen ch9_900sbj1_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_900sbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_900sbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_900sbj1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_900sbj2_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" action Jump("ch9_900sbj2_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_900sbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_900sbj1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
screen ch9_900sbj3_():
    vbox:
        xalign 0.99
        yalign 0.8
        textbutton "Slow" action SetVariable("anim_speed", 0.05) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.7
        textbutton "Normal" action SetVariable("anim_speed", 0.03) style "textbutton_choice"
    vbox:
        xalign 0.99
        yalign 0.6
        textbutton "Fast" action SetVariable("anim_speed", 0.01) style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.79
        textbutton "Pov 3" action Jump("ch9_900sbj3_") style "textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.89
        textbutton "Pov 2" style"textbutton_choice"
    hbox:
        yalign 0.05
        xalign 0.99
        textbutton "Pov 1" action Jump("ch9_900sbj1_") style "textbutton_choice"
    hbox:
        yalign 0.95
        xalign 0.99
        textbutton "Continue" action Jump("afterch9_900sbj1_") style "textbutton_choice"   
    hbox:
        yalign 0.95
        xalign 0.05
        textbutton _("Hide") action HideInterface() style "textbutton_choice" 
label beforech9_900sbj:
    image ch9_900sbj1_:
        function ch9_900sbj1_
    image ch9_900sbj2_:
        function ch9_900sbj2_
    image ch9_900sbj3_:
        function ch9_900sbj3_
    $ anim_speed = 0.05
    scene ch9_908---- with dissolve
    pause
    scene ch9_900sbj1_ with dissolve
    mc "Oh... *hmmh*"
    s "*Slup, chup, hmpsh*"
    pause
    mc "(She's wrapping it with her tongue, it feels so good...)" with dissolve
    mc "(Focusing the blowjob just on the tip feels really nice too...)" with dissolve
    pause
    mc "(My cock is sore from being erect for so long, and this feels like a healing massage...)"
    pause
    scene ch9_900sbj3_ with dissolve
    s "*Chup, chlp, slsh*"
    mc "Use your tongue underneath the tip..."
    s "Hubm, hub... *chup, slchp*"
    mc "J-just like that, hmm..."
    pause
    mc "You're such a good girl..."
    s "Hmm, hm... *Schup, chulp*"
    pause
    scene ch9_900sbj2_ with dissolve
    mc "*Uhmgh* So good..."
    pause
    mc "Can you go a little faster?"
    s "Um-hum."
    $ anim_speed = 0.013
    mc "Good girl, uhmm..."
    call screen ch9_900sbj1_ with dissolve

label ch9_900sbj1_:
    scene ch9_900sbj1_ with dissolve
    call screen ch9_900sbj1_ with dissolve
label ch9_900sbj3_:
    scene ch9_900sbj2_ with dissolve
    call screen ch9_900sbj2_ with dissolve
label ch9_900sbj2_:
    scene ch9_900sbj3_ with dissolve
    call screen ch9_900sbj3_ with dissolve

label afterch9_900sbj1_:
    mc "*Uhmgh!* That's... almost there..."
    $ anim_speed = 0.009
    s "*Chup, shlup, chulp*"
    mc "*Angh!* {i}{size=-2}It's about to come, [s]!"
    s "*Shlp, chup, shup*"
    pause
    mc "*Arghmm!* W-wait, [s]..."
    scene ch9_909 with hpunch
    show ch9_909 at Shake((0.5, 1.0, 0.5, 1.0), 999.0, dist=2.5)
    mc "*Arghmmhm!*"
    scene ch9_910- with cumming
    mc "*Arghhh...!*" with flash
    pause
    scene ch9_911 with dissolve
    mc "{i}{size=-2}Uff... uhh... huhh..."
    mc "Oh god..."
    mc "That was so good..."
    pause
    scene ch9_910-_ with dissolve
    s "Uhm..."
    mc "L-let me clean you up."
    pause
    scene ch9_910-- with dissolve
    mc "I told you to stop, but you kept going."
    mc "Now let's change quickly and leave, okay?"
    pause
    scene ch9_914 with dissolve
    mc "We need to hurry, they must be worried about us."
    pause
    scene ch9_912 with dissolve:
        subpixel True
        yalign 1.0 xalign 0.5 zoom 1.0
        ease 5 yalign 0.0 xalign 0.5 zoom 1.0
    mc "I hope you're satisfied now."
    pause
    mc "{i}{size=-3}Hurry, we need to go!"
    mc "(What's wrong with her?)" with dissolve
    mc "Do you need your clothes?"
    scene ch9_915 with dissolve
    mc "Here."
    pause
    s "..."
    scene ch9_916-- with dissolve
    s "*Buaah...*"
    mc "Oh..."
    pause
    s "*Guh, guh*"
    mc "(She's trying to talk with all that in her mouth...)" with dissolve
    mc "(It looks like she's gargling with my cum...)"
    pause
    scene ch9_917 with dissolve
    play sound "audio/mouth/swallow_05.ogg" fadein 0.2 volume 1.0
    s "*Gulp*"
    pause
    scene ch9_918 with dissolve
    s "Aaah..."
    mc "D-did you drink it?..."
    s "Uh-huh."
    pause
    scene ch9_919 with dissolve
    s "I drank it all, hehe..."
    mc "..."
    pause
    mc "(That was...{w=0.5} way too sexy!)" with dissolve
    scene ch9_910-- with dissolve
    mc "I-I didn't tell you to drink it, why did you do that?"
    s "Uhm...{w=0.5} I don't know."
    s "Your dick is moving again!"
    mc "{i}{size=-2}Shh, don't say it so loudly!"
    s "{i}{size=-2}Sorry..."
    mc "{i}{size=-2}You're such a perverted girl."
    s "Te-hehe."
    mc "Put on your clothes so we can leave."
    s "Yes."
    $ renpy.end_replay()
    pause
    stop music fadeout 3.0
    scene blackscreen with Dissolve(2.0)
    pause
    play music scene2 fadein 2.0
    scene ch9_920 with dissolve
    s "I was a bit hungry, but not anymore, hehe."
    s "Your cum-{w=0.5}{nw}"
    mc "Shh!..." with hpunch
    pause
    scene ch9_921 with dissolve
    mc "Hey, dude, we'll take this bikini."
    pause
    scene ch9_922 with dissolve
    "Hsh..."
    pause
    mc "Bro?"
    s "Hey!"
    scene ch9_923 with vpunch
    "Hmmphhh!"
    play sound coughing volume 0.2 loop
    scene ch9_924 with hpunch
    "Cof, cof, cof, cof!"
    "Bro, I almost had a heart attack. *Cof, cof, cof*"
    "What can I {w=0.5}, *Cof, cof, cof!* offer?"
    "Cof, cof, cof, cof*"
    mc "Erm... we..."
    s "It smells weird..."
    "*Cof, cof, cof* Five dollars, it's on sale, *cof*, but it's free for you. *cof*"
    mc "Really?"
    "Yes."
    stop sound fadeout 0.5
    scene ch9_925 with fade
    s "Thanks!"
    "Remember, you didn’t see anything, okay?"
    s "Yes."
    s "Say thank you too, [mc]."
    mc "Thanks..."
    pause
    jump ch9_1000sskip
label ch9_1000sskip:
    stop background fadeout 2.0
    stop music fadeout 2.0
    scene blackscreen with dissolve
    pause
    scene ch9_927 with dissolve
    play background beachsfx fadein 1.0 volume 0.8
    play music scene1 fadein 3.0
    play sound bonfire fadein 0.3 volume 0.1 loop
    mc "[s] was taking a long time."
    d "Trying on clothes?"
    mc "Yeah."
    d "I figured, haha."
    s "And then he started coughing and a weird-smelling puff of smoke came out of his mouth."
    s "And he said he'd gift it to me if I kept it a secret."
    a "Oh, really?..."
    s "Yep, and I agreed."
    pause
    scene ch9_931 with dissolve
    a "Why did it take so long? We were worried."
    d "[s] was trying on clothes, dear."
    mc "Yeah, she didn’t know what to wear."
    s "None of them looked good to me..."
    s "Hehehe..."
    mc "..."
    play sound bonfire volume 0.35 loop
    scene ch9_928 with dissolve
    d "Hey, Mia, don’t your parents get mad at you for being out so late?"
    d "I can tell [mc] to take you home if you want."
    mia "No, it’s okay. For now, I’m home alone. No rules, hehe."
    d "Oh, yeahm I just forgot. Your mom is out of the conuntry."
    mia "Yeah."
    d "Aren’t you scared of being home alone?"
    mia "Scared of being alone?"
    mia "Sometimes, yeah, haha."
    d "I can have [mc] to keep you company for a few days, if you want."
    mia "Haha, my boyfriend keeps me company enough, but thanks."
    scene ch9_929 with Dissolve(0.3)
    d "Eh..."
    d "I thought..."
    scene ch9_930 with dissolve
    d "Oh, right... I forgot you have a boyfriend, hehe. My apologies."
    mia "Don’t worry about it, haha."
    scene ch9_933 with dissolve
    mia "No need to apologize."
    mc "..."
    pause
    scene ch9_932 with dissolve
    a "So, Mia, how’s the divorce going?"
    mia "Well, it’s almost finalized; they’re just discussing the assets and stuff."
    mia "Mom is fighting over an apartment they bought together, or so she says, let’s see what happens." 
    a "I see. I hope it works out."
    mia "Yeah, I hope so."
    mc "The runway video has like ten thousand views now."
    mc "Everyone’s saying the mom is the prettiest."
    k "Really? Did you upload it?"
    scene ch9_934 with dissolve
    a "[mc], stop joking!"
    mc "What?"
    a "I told you to cut out the part where I appear!"
    mc "Oh, sorry."
    a "Delete it!"
    mc "Just kidding, haha."
    "Hahaha."
    stop background fadeout 2.0
    stop sound fadeout 2.0
    stop music fadeout 3.0
    scene blackscreen with dissolve
    pause
    play sound bonfire fadein 1.0 volume 0.4 loop
    play background beachsfx fadein 1.0
    scene ch9_935 with Dissolve(2.0)
    mc "So then the quality inspector showed up, but since he had nothing to do, they asked him to help the welders."
    mc "He agreed, and they had him catching sparks from the grinder with a plastic container until he collected a pound of that, and the poor guy was there for an hour, haha."
    k "And so what?"
    mc "Those sparks are less than half the size of a grain of sand, so he barely captured anything and spent an hour catching sparks."
    a "That’s awful, haha. You can’t trust them, [mc]."
    k "Seems like a good work environment."
    mc "It would be great if the work wasn’t so heavy..."
    scene ch9_936 with dissolve
    mia "Jobs where the coworkers are so fun are the best."
    k "Have you had a job?"
    mia "Of course, I worked at a pizzeria, don’t you remember?"
    k "Right, you worked at BigCesar’s, didn’t you?"
    mc "([drelat!cl] [d] has been silent this whole time...)" with dissolve
    mc "(And no one’s talking to him...)" with dissolve
    mc "(I feel a bit bad for him...)" with dissolve
    mc "(Whether he’s an unfaithful man or not, he’s never treated me badly.)" with dissolve
    d "..."
    mia "I’ve had several jobs, not just that one."
    k "Really?"
    mia "Haven’t you ever had a job?"
    k "No."
    mc "[drelat!cl] [d]."
    scene ch9_937 with dissolve
    d "Yes, son?"
    mc "I’m going to get a beer, do you want one?"
    d "Sure, but I think they’re all gone."
    mc "I’ll check."
    scene blackscreen with dissolve
    play sound bonfire volume 0.1 loop
    scene ch9_938 with fade
    d "None left, right?"
    mc "No, just some water at the bottom."
    scene ch9_939 with dissolve
    d "Yeah, I finished them all."
    mc "Oh well."
    d "{i}{size=-3}Don’t think I didn’t see you.{/i}"
    mc "What are you talking about?"
    d "{i}{size=-3}That puertorican girl is pretty, huh?{/i}"
    mc "{i}{size=-3}Oh, that... haha...{/i}"
    scene ch9_940- with dissolve
    d "{i}{size=-3}She said she has a boyfriend.{/i}"
    mc "{i}{size=-3}Uh, yeah...{/i}"
    scene ch9_941 with dissolve
    d "{i}{size=-3}I’m not judging you, she’s quite attractive.{/i}"
    d "{i}{size=-3}When I was your age, that was never an obstacle for me either, haha.{/i}"
    mc "{i}{size=-3}Haha...{/i}" with dissolve
    d "{i}{size=-3}I’m glad that...{/i}"
    d "{i}{size=-3}Never mind, forget it.{/i}"
    pause
    mc "{i}{size=-3}How’s it going with [arelat] [a]?{/i}"
    scene ch9_942 with dissolve
    d "B-better, little by little, yes..."
    d "At least she’s talking to me a bit now. Everything will get better, don’t worry."
    mia "Excuse me, Mr. [d]."
    scene ch9_943- with dissolve
    d "Yeah?"
    mia "Look in my backpack, I have a gift for you."
    d "Oh, really?"
    mia "Yes, [mc] knows what it is."
    scene ch9_939 with dissolve
    d "{i}{size=-3}I think she wants to earn points, haha. You’ve got her crazy.{/i}"
    mc "Haha, I guess so."
    d "Ha-ha-ha."
    scene blackscreen with dissolve
    pause 0.1
    play sound bonfire volume 0.4 loop
    scene ch9_944 with fade
    d "Ohh... this is..."
    mia "Is it good? I don’t know much about wines and that stuff."
    d "Of course... it’s very good."
    pause
    scene ch9_945 with dissolve
    d "I haven’t seen one of these bottles in a long time."
    pause
    d "Your father loved this."
    mc "My father drank?"
    d "Yeah, this was his favorite rum."
    scene ch9_946 with Dissolve(2.0)
    pause 1.0
    scene ch9_945 with Dissolve(2.0)
    pause
    mc "Yeah, I think I remember..."
    d "Sometimes I’d join him for a drink, and he’d pull one of these from the pantry..."
    d "He’d light a cigar or a cigarette and drink it straight from the bottle."
    d "He always had one around, even in his office. He loved it..."
    pause
    d "Want to try it?"
    mc "Sure, if you don’t mind."
    d "Get us a cup."
    scene blackscreen with dissolve
    pause
    play sound bonfire volume 0.3 loop
    scene ch9_947 with dissolve
    "{i}''In the quiet of the night, I sit alooone,''"
    "{i}''Thinking 'bout the love we built, the seeds we've sooown.''"
    k "[arelatks!cl], let’s go home now, this is embarrassing."
    a "Let them have some fun for a while."
    "{i}''But I let temptation lead me down a darker rooooad,''"
    "{i}''Now I'm standing here, carrying this heavy loaaaaad.''"
    a "Hide the bottle without them seeing..."
    play sound bonfire volume 0.4 loop
    scene ch9_949 with dissolve
    d "To us, and to the lovely family we are."
    d "And to my nephew, the only thing I have left of my dear brother."
    mc "Cheers, [drelat] [d]."
    scene ch9_949 with dissolve
    d "And I also want to say that I’ve forgotten what you did, [mc], [k]..."
    d "Neither of you is grounded anymore."
    k "R-really?"
    d "Yes, I don’t want you to see me like the bad person."
    k "The bottle’s here if you want to keep drinking."
    a "[k]!"
    d "Really, I’m not a bad father, seriously!"
    d "It’s just that, I’m weak... very weak."
    scene ch9_949 with dissolve
    d "[mc], now I know what it feels like to be alone..."
    d "Forgive me for sending you to that apartment. *Sniff, sniff*"
    mc "*Sniff* Don’t worry, [drelat] [d]... I would have done the same."
    d "Thank you, son. Thank you for understanding... And sorry for... everything."
    play sound bonfire volume 0.3 loop
    scene ch9_947 with dissolve
    "{i}''In the quiet of the night, I sit alooone!''"
    k "[arelatks!cl]!"
    a "Yeah..."
    a "Take them to the car while I clean this up, please, and come back to help me."
    k "Sure."
    play sound bonfire volume 0.1 loop
    scene ch9_948 with dissolve
    d "{i}''Thinking 'bout the love we built, the seeds we've sooown.''"
    k "Stop singing, [drelatks]!"
    d "I love you, daughter, forgive me."
    d "Forgive me, everyone..."
    k "Yes, yes, I forgive you, just stop talking."
    mia "Walk straight, [mc]."
    mc "Yes..."
    a "Honey, wake up, it’s time to go."
    scene chapterend with Dissolve(3.0)
    call screen chapter9end with Dissolve(2.0)




            











    
















































