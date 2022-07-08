label sayoriroute4:
    scene black
    with fade
    s "..."
    s "..."
    s "..."
    s "...{i}If happy little bluebirds fly{/i}..."
    call sayoriroute41
    jump sayoriroute5
return

label sayoriroute41:
    play music t12
    scene bg bedroom
    with fade
    "As my eyes slowly open, I stretch slightly and take a deep breath."
    "It takes a moment to realize that I'm lying in my bed."
    "More importantly, however, is the person lying next to me."
    "I look down to see Sayori resting her head on my chest, suddenly conscious of the soft breathing against it."
    "It's not the first time me and her have shared this bed, but it is the first time I took the time to really enjoy this feeling."
    "It's as if a strange sort of {i}fuzzy{/i} feeling is coming from where she's laying on me."
    "I really can't get enough of it." 
    "Originally, the plan was to wake her up, and get done with our morning activities, but maybe staying like this would be best after all."
    scene black
    with fade
    "I close my eyes and continue to enjoy the feeling."
    "Soon enough, I feel Sayori begin to stir against me."
    "She pokes my face a few times, probably to see if I'm awake or not."
    "I fake the idea that this action disturbed me from my slumber."
    stop music fadeout 1.5
    "After all, having Sayori realize that I watched her sleep... not the best idea."
    play music t2
    scene bg bedroom
    with fade
    show sayori undo at t11 zorder 2
    mc "Wh-what...?"
    "I say, trying my best to sound drowsy."
    s undr "Good morning, [player]!"
    show sayori undq at t11 zorder 2
    "Sayori sounds full of energy already."
    "I didn't take her for a morning person, she was almost always late for school..."
    "Although maybe that has something to do with how things are changing."
    mc "Good morning, Sayori."
    mc "Can I go back to sleep now?"
    s undx "Ehehe, that's funny, I was thinking sort of the same thing..."
    show sayori unda at t11 zorder 2
    "That's kind of shocking. Although, actually, no it isn't."
    s undc "I really don't want to get out of bed..."
    s "...so maybe we can just, you know, lay here together?"
    show sayori undd at t11 zorder 2
    mc "Is {i}cuddling{/i} the word you're looking for?"
    "I stop to think."
    menu:
        "Should we waste more time in bed together?"
        "Agree to it.":
            $SayoriVar += 1
            "Normally, I would despise saying that word."
            "But, strangely, offering to do it with Sayori doesn't at all phase me."
            "In contrast to how I would normally act, Sayori's ecstatic about the idea."
            show sayori undr at h11 zorder 2
            s "Yay! I'd love to!"
            show sayori at thide
            hide sayori
            "Not resisting, I turn to lay on my side, facing Sayori. I wrap my arms around her and she does the same to me, burying her face in my chest."
            "..."
            "{i}What normally happens after this?{/i}"
            "I'm reminded that my aversion to this type of thing in the media means that I have no idea what the hell I'm meant to do next."
            mc "Hey, Sayori?"
            s "Yeah?"
            "She turns her head up slightly to look at me."
            mc "What exactly are we supposed to do?"
            s "..."
            mc "I mean, you probably know more about this than I do, don't you? What normally comes next after this?"
            "Sayori seems to think about this question for a moment."
            s "Nothing, really."
            s "Maybe just some talking with each other? Not much else except enjoying the moment."
            "To say I'm not doing the latter would be a lie."
            "Sayori's hair, despite just waking up, looks as it always does."
            "Though that's probably because she doesn't fix her hair in the morning."
            "Not that I mind, though; there's something about this look that's really homely."
            "Having her bright blue eyes staring intently at me, too, is a great feeling."
            "If the eyes are the window to the soul, she's staring directly into mine, and it's enjoying the attention."
            "Plus, the hugging itself isn't bad, either."
            "And I totally got lucky, having a girlfriend that sleeps in underwear."
            "Erm..."
            "Anyway, the point is that \"enjoying the moment\" isn't all too difficult."
            "I only hope Sayori likes it as much as I do."
            stop music fadeout 1.5
            s "[player]?"
            mc "Yes, that's me."
            s "Is it weird to say I don't want this to end?"
            "Well, that answers that question."
            play music t9
            mc "No. Actually, I completely agree."
            "And I wasn't lying to her. Barring hunger and thirst, if staying like this was an option, I would take it."
            "Except it does get kind of boring. Maybe I could actually try talking with Sayori about things."
            mc "Hey, Sayori?"
            s "Yeah?"
            mc "What do you think the meaning of life is?"
            "Base level, but it at least gets a discussion going."
            s "Hmm."
            s "I think it's whatever makes you happy!"
            "..."
            "I really should have expected that."
            "Philosophical questions don't seem like Sayori's area of expertise."
            "Although in a cosmic sort of way, she might be right."
            mc "Okay, maybe philosophy isn't a good place to start..."
            mc "How about a more practical question?"
            mc "What should we do when, {i}or if{/i}, we actually get up?"
            s "Hmm..."
            "Sayori seems to be taking the effort to actually think this one out."
            s "Well, we should start out by having breakfast..."
            "...Never mind."
            s "After that... maybe play some more video games?"
            mc "You liked them that much?"
            s "Yeah, it's fun when I don't feel really stupid..."
            "I'll try to avoid the puzzle games, then."
            mc "I've got plenty of games that won't make you feel dumb."
            s "Yay!"
            mc "Hmm... what else? Just video games and food all day?"
            s "Maybe we can go see a movie when it gets late?"
            mc "Yeah..."
            "I don't have the heart to tell Sayori that I don't really feel like seeing a movie again so soon."
            "But I guess if it makes Sayori happy I don't have any reason to say no."
            s "And then, we can do the best part!"
            mc "And that is?"
            stop music fadeout 1.5
            s "Going back to bed, so we can cuddle like this again! I can't wait for that!"
            play music t2
        "Turn her down.":
            $SayoriVar -= 1
            mc "Sorry, Sayori, but we should probably get out of bed before we lose too much of our Sunday."
            show sayori undk at t11 zorder 2
            "She looks sad at first, so I decide to cheer her up with a quick cheek pinch."
            show sayori undd
            "That seemed to improve her mood a bit."

    scene black
    with fade
    
    
    "Upon Sayori and myself deciding to get out of bed, we go about our morning routine of brushing our teeth..."
    "(At the same time)"

    "Using the bathroom..."
    "(Obviously not at the same time)"

    "Taking quick showers..."
    "(Unfortunately not at the same time)"

    "Then going to the kitchen and making breakfast."

    scene bg kitchen
    with wipeleft_scene
    "After eating our breakfasts of scrambled eggs and toaster waffles, we get situated in the living room and play video games like she had asked."

    scene bg livingroom
    with wipeleft_scene
    "We have a lot of fun, before her short attention span kicks in and says..."
    show sayori pjc at t11 zorder 2
    s "I'm getting bored."
    show sayori pjb at t11 zorder 2
    mc "Well, that's a shame. It's almost as if I'd seen that coming."
    s pjj "What are you trying to say, meanie?"
    show sayori pji at t11 zorder 2
    mc "I just had a feeling you wouldn't wanna make this a full day thing."
    s pjj "Is that so wrong? Maybe I wanna explore other options!"
    show sayori pji at t11 zorder 2
    mc "I guess you're right, nothing wrong with that."
    show sayori pjq at t11 zorder 2
    "Sayori gives me a warm smile, and I smile back."
    mc "So, what do you wanna do for the rest of the day?"
    s pjr "Ooh, I know!"
    s "Let's watch that movie with the scarecrow in it!"
    mc "...Batman Begins?"
    s pjx "No, not Batman. The one with all the little singing dudes who were happy about the witch being dead!"
    s "And the girl with the ruby red shoes who makes friends with a robot!"
    show sayori pja at t11 zorder 2
    mc "Sayori..."
    mc "Are you talking about {i}The Wizard of Oz{/i}?"
    s pjx "Oh, yeah, that's it! Let's watch that, it's like my favorite movie!"
    show sayori pja at t11 zorder 2
    mc "First of all, Sayori, how can you call it your favorite movie if you don't even know the name?"
    mc "Better yet, how do you not know what it's called?"
    mc "Freaking everyone knows what the Wizard of Oz is."
    s pjn "Well, I dunno, I just remember loving it a lot. And that song the girl sang at the beginning."
    mc "Oh, yeah, I know what song you're talking about."
    mc "Because it's literally one of the most popular songs in any movie ever."
    s pjj "You don't have to be a meanie about it."
    show sayori pji at t11 zorder 2
    mc "Hahaha, sorry, Sayori."
    s pjc "It's okay. So can we watch it together?"
    show sayori pja at t11 zorder 2
    mc "I don't own it. And even if I did, I don't really like it that much, sorry."
    s pjj "Uuuu, you're no fun."
    s pjx "So, what do {i}you{/i} wanna do today?"
    show sayori pja at t11 zorder 2
    mc "Hmmm..."
    "That's actually a tough question."
    "You know...there's something that's come to mind, but I need a favor from someone first."
    mc "Give me a second, Sayori, I have to go call somebody."

    scene black
    with wipeleft_scene
    scene bg bedroom
    with wipeleft_scene

    "I need to make a phone call to somebody and get them to distract Sayori for a little while."
    stop music fadeout 1.5
    "Now...who to call..."

    menu:
        "Who do I call?"
        "Monika":
            play music t5
            "She seems like the most trustworthy of the bunch."
            "I give the club president a phone call and she picks up."
            m "Hello?"
            mc "H-hey, Monika, good afternoon. How do you do?"
            m "Ahaha~, why are you talking like that [player]?"
            mc "Uh-um, n-no reason."
            "Yeesh, I guess I'm still subconsciously nervous about talking to Monika."
            "After all, I don't think I've called her on her phone before. I hope I'm not intruding on anything."
            "She seems like she has a lot of important stuff going on."
            m "So, why'd you call?"
            mc "*Ahem* Well I kinda need your help with something at the moment. Are you busy?"
            mc "I-I mean I'd understand if you are, m-maybe I should ask someone else, s-sorry for bother--"
            m "Whoa, hey, [player], calm down! I don't have anything going on right now. So what can I help you with?"
            "Phew, that's a relief."
            mc "So, I want to surprise Sayori today by taking her to a picnic in the park, but I don't want her to see me preparing all the food."
            m "Hehe, now is that because you want it to be a surprise or because you don't want her to eat anything prematurely?"
            mc "It's Sayori and food. You do the math."
            mc "S-so, I just need you to go to her house, then call her acting like there's something important you need her help with."
            m "Then you want me to distract her for about an hour while you make all the picnic goodies, right?"
            mc "Yes, exactly!"
            mc "S-so, can you help?"
            m "Absolutely! I'm all for romantic gestures and surprises. Just let me know when you're ready."
            mc "Right now would be perfect. Just remember to call her as soon as you get to her house."
            m "You got it. Good luck~!"
            mc "Thank you so much, see ya!"
            "We end the call there."
            "This should be fun. Should only be about a five to ten minute walk for Monika to get to Sayori's place, so in that time I'm going to mentally plan all the foods I want to prepare for us."
            "Let's see, finger sandwiches, rice, fruit salad, and I think I have a little bit of sparkling apple cider tucked away somewhere in the kitchen."
            "{i}Non-alcoholic, of course."
            "Alright, this should work. Now I just gotta wait another four to eight minutes for Monika to reach Sayori's house and--"
            "Eh? My phone vibrated."
            m "{i}I'm at Sayori's place, I'm gonna call her now :)"
            "{i}Holy CRAP, that was fast!"
            scene bg livingroom
            with wipeleft_scene
            "I return to the living room to see Sayori, as expected, on the phone."
            s "Oh, you're at my house? Well gosh, that's sudden, sorry I'm not there!"
            s "Important literature club business?"
            s "Uh, sure, but how long do you think it'll take? [player] and I are trying to make plans."
            s "An hour, seriously? Um...well, if it's as important as you say then I guess I don't have much choice."
            s "Okay, I'll be right there. See you."
            show sayori pjb at t11 zorder 2
            "Sayori hangs up the phone and looks at me, having just emerged through the threeshold of the living room."
            s pjc "Hey, I'm really sorry but Monika needs me for something! I'll be gone for a little bit."
            s "But I promise we'll come up with something when I get back, alright?"
            show sayori pjb at t11 zorder 2
            mc "No problem, Sayori, do what you gotta do."
            mc "I'll just brainstorm while you're gone."
            show sayori pja at t11 zorder 2
            "Sayori agrees, then walks toward my front door."
            show sayori at thide
            hide sayori
            "I wonder what Monika has planned to keep Sayori distracted for a whole hour."
            "But she's just about the smartest person I know, I have no doubt she'll be good on her feet."
            #(they had lesbian sex) => unfortunatly, nope
            "Sayori waves goodbye to me, and the nanosecond I hear the door shut, I dash into the kitchen."
            $ distraction = "Monika"

        "Yuri":
            play music t6
            "Yuri seems like a romantic person, I'm sure she's willing to help."
            "Wait, am I mixing up romance with romanticism?"
            "Whatever, I'm sure Yuri will do fine anyway."
            "I give her a call, and wait about ten seconds before she picks up."
            y "H-hello?"
            mc "Hi, Yuri, how goes it?"
            y "Oh! Hi, [player]. I'm having a decent day, how about yourself?"
            mc "I'm good. I was actually hoping for a favor if you weren't busy."
            y "Hm, I had planned to start reading this new novel I'd bought recently but I suppose I can help you if you need me."
            "Hm, I kinda feel bad."
            "Yuri tends to not find much enjoyment out of much more than her reading, and if I ask her for a favor I'll be depriving her of that."
            mc "O-on second thought, maybe I should ask someone else for help."
            mc "See you, Yuri--"
            y "W-wait, hold on! I'm happy to help, don't feel like you're depriving me of anything."
            y "I assure you, I have quite a bit of time on my hands, I can delegate any time I want to read."
            mc "Well damn, it's like you read my mind."
            y "Huhuhu~, I can sense the way my friends feel."
            y "So, what is this favor of yours?"
            mc "Oh, right, that."
            mc "So, I want to surprise Sayori today by taking her to a picnic in the park, but I don't want her to see me preparing all the food."
            mc "And I was hoping that you could spend some time with her to distract her for a little while so she's not with me."
            y "..."
            y "Y-you want me to...distract Sayori?"
            y "Isn't that a bit...deceitful?"
            mc "I'd think it more along the lines of being a romantic gesture."
            y "If you say so..."
            y "Unfortunately, I'm not sure I'm the person for the job."
            y "I'm not exactly a very good liar."
            mc "You don't have to lie, necessarily! Just tell Sayori you'd like to see her at her house."
            mc "She's your friend, I can't imagine that's much of a lie."
            y "Hmm..."
            y "I suppose you're right."
            y "Okay, then, I'll lend you a hand."
            mc "Marvelous!"
            mc "Er, I mean..."
            mc "Cool!"
            y "Huhuhu~, so what would you like for me to do?"
            mc "Well, I'd like you to go to Sayori's house and then call her, telling her you'd like to see her."
            mc "Then she'll go see you, and you can just spend some time with her. Offer to make her tea or something."
            y "I understand. I'll leave my house whenever you need me to, just say the word."
            mc "Right now would be perfect, I'll probably need around an hour to make all our food."
            y "I'll leave now, then, and I'll call her once I reach her house."
            mc "Thank you, Yuri, you're the best!"
            y "Oh? I'd think Sayori would be the best considering all this trouble you're going through to surprise her."
            mc "Heheh, you got me there. Well, thank you again."
            y "You're welcome, [player]."
            "Awesome. So I just gotta wait maybe ten minutes for Yuri to get there, then I can get started."
            "In the meantime, I'll mentally plan all the foods I want to prepare for us."
            "Let's see, finger sandwiches, rice, fruit salad, and I think I have a little bit of sparkling apple cider tucked away somewhere in the kitchen."
            "{i}Non-alcoholic, of course."
            "Alright, perfect. Now I just need to wait about another nine minutes or so for Yuri to get into position."
            "..."
            "{i}I should phrase that better."
            "In any case, I return to the living room and spend the remaining time with Sayori."
            scene bg livingroom
            with wipeleft_scene
            show sayori pjx at t11 zorder 2
            s "There you are, where'd you go?"
            show sayori pja at t11 zorder 2
            mc "I was just taking care of something...with my dad."
            s pjc "Ohhh, okay. What did you talk about?"
            show sayori pja at t11 zorder 2
            mc "Uh..."
            "Crap."
            "{i}Lie, [player]! Lie like your life depends on it!"
            mc "Just boring stuff, like my funding while they're away."
            s pjc "Oh. That's no fun."
            "Success!"
            show sayori at thide
            hide sayori
            "Sayori and I snuggle together on the couch for a few minutes, minding our own businesses on our phones, and I realize that Yuri should be calling Sayori in a matter of moments."
            "Finally, the expected phone call arrives."
            s "Oh, Yuri's calling me."
            "Sayori answers."
            s "Hello?...Hi, Yuri! What's up?"
            s "O-oh, you're at my house? Um...sorry I'm not there right now, but I can come right over!"
            s "New tea? Sounds good! Can [player] come too?"
            mc "Uh..."
            s "Why not?...Ohhh, I get it."
            s "Hehe~, yeah he can be like that sometimes."
            "What in the..."
            "Hey! I can be like what?!"
            s "Well, I'll be right over there. See ya!"
            show sayori pjx at t11 zorder 2
            s "I'm sure you heard. I'll be at my house for a little while."
            s pjr "Sorry, Yuri says no guys allowed!"
            show sayori pjq at t11 zorder 2
            mc "I'm crushed..."
            "I'm being facetious, but admittedly I am wondering what she said about me...this wasn't part of the plan!"
            s pjx "Be back later! After that we can think of more stuff to do today!"
            mc "Sure thing. Have fun!"
            show sayori at thide
            hide sayori
            "Sayori walks out the door."
            stop music fadeout 1.5
            "Part of me wonders what Yuri has planned to keep her occupied for such a long time..."
            #{daydream sequence; maybe some kind of screen effect to emphasize}
            scene bg sayori_bedroom_daydream
            with fade
            show sayori 4bc at t21 zorder 2
            show yuri 1bc at t22 zorder 2 
            play music t5
            s "Say, Yuri, I'm feeling kind of weird."
            s "Is there something in this tea you gave me?"
            show sayori 4be at t21 zorder 2
            y 1bd "Oh no, of course not!"
            y "It's just the tea itself."
            stop music
            y 1bb "It's chamomile. You should be falling asleep in approximately eight seconds."
            "..."
            show sayori 4bp at s21 zorder 2
            "..."
            #show sayori at thide
            hide sayori
            play sound fall
            "..."
            #[Show sprite of Sayori falling with a thud sound effect]
            show yuri 3by1 at t22 zorder 2
            y "Hehehehe..."
            #(Then they have lesbian sex) => nice chipping
            #{end daydream}
            scene bg livingroom
            with fade
            "My mind goes to weird places sometimes..."
            "Oh well. To the kitchen!"
            play music t6
            $ distraction = "Yuri"



        "Natsuki":
            play music t6
            "She isn't exactly the most agreeable person but she is Sayori's best friend so she should be able to keep her occupied."
            "I call her up, and in a moment she answers."
            n "{i}[player]? What's going on?{/i}"
            mc "Why are you talking so quietly?"
            "Seriously, she sounds like a mouse."
            n "Uh, no reason."
            "She speaks up, finally."
            n "What's going on?"
            mc "So here's the deal, I wanted to surprise Sayori with a picnic but I need to make the food in private so she doesn't find out."
            mc "And that's where you come in. I need your help to distract her while I prepare all our food."
            n "Oh! That sounds cool!"
            n "Sure, I'll help you out. What do you need me to do?"
            mc "Great! I just need you to go to her house and tell her you wanna see her, then she'll go over there."
            n "Hm..."
            n "Hey, I'll do you one better."
            n "I'll ask her if she wants to bake something with me, then we can bake at her house and you can take some goodies with you on your picnic."
            mc "Natsuki, you're a genius!"
            n "I'm the best, don't you forget it."
            mc "Well actually Sayori's the best, it's why I'm doing all this for her."
            n "Grrr..."
            mc "I-I mean, you're both equally the best."
            n "That's more like it. Now, just give me a minute to gather my baking supplies and go over to Sayori's house."
            mc "Sure thing. Aaaaaand, {i}break!{/i}"
            n "Pffft, dork."
            "And with that she hangs up the phone."
            "{i}This should be awesome. And having some of Natsuki's cupcakes should make our picnic that much sweeter."
            "...piss off, cheesy inner monologue."
            "In any case, I return to the living room and spend the remaining time with Sayori."
            scene bg livingroom
            with wipeleft_scene
            show sayori pjx at t11 zorder 2
            s "There you are, where'd you go?"
            show sayori pja at t11 zorder 2
            mc "I was just taking care of something...with my dad."
            s pjc "Ohhh, okay. What did you talk about?"
            show sayori pja at t11 zorder 2
            mc "Uh..."
            "Crap."
            "{i}Lie, [player]! Lie like your life depends on it!"
            mc "Just boring stuff, like my funding while they're away."
            s pjc "Oh. That's no fun."
            "Success!"
            show sayori at thide
            hide sayori
            "Sayori and I snuggle together on the couch for a few minutes, minding our own businesses on our phones, and I realize that Natsuki should be calling Sayori in a matter of moments."
            s "Oh, Natsuki's calling...Hello?"
            s "Hey Natsuki!"
            s "D..."
            s "DID YOU SAY CUPCAKES?!"
            "My eyes go wide as Sayori nearly launches herself off the couch with the speed of a space shuttle."
            s "Oh, we have to bake them first?"
            s "Aw, dang it, I thought they'd be finished already."
            s "Oh well, baking with you sounds like tons of fun, I'd love to!"
            s "Sure, I'll head right over to my place."
            s "'Kay, see ya soon!"
            "She hangs up the call."
            show sayori pjr at h11 zorder 2
            s "I'm gonna go bake some cupcakes with Natsuki!"
            s "Hey, do you wanna come too?"
            show sayori pjq at t11 zorder 2
            mc "Oh, uh...n-no thanks, I don't think I'd enjoy that very much."
            s pjm "Whaaa?! What's not to enjoy about baking cupcakes?!"
            mc "Uh...I don't...like..."
            mc "...Natsuki."
            s pjn "Wait what? You don't like Natsuki? Since when?!"
            show sayori pjb at t11 zorder 2
            mc "Wait, no, that came out wrong. I do like her, I just don't know if she'd want me there if she only invited you."
            s pjh "Ehh?! But that's so different from what you said at firs--"
            mc "Hey, let's not talk about this. Just go have fun with Natsuki, and bring us back some cupcakes, okay?"
            show sayori pja at t11 zorder 2
            "Sayori lightens up and puts on a smile."
            s pjr "Yeah, okay."
            s "I'll see you soon then!"
            mc "See ya!"
            show sayori at thide
            hide sayori
            "Yeesh, that was a close call."
            "My BS'ing chops could use some refining."
            "With cupcakes in Sayori's near future she bolts out the front door back toward her place while she awaits Natsuki's arrival."
            "Once she's out of sight, I jump off the couch and dash to the kitchen."
            $ distraction = "Natsuki"

    scene bg kitchen
    with wipeleft_scene
    "I retrieve bread, rice, and veggies, then start to build our lunch."
    "Cutting all the square bread into little triangles proves to make applying the meat and veggies a little bit difficult."
    mc "Wait, what the hell am I doing?!"
    "I realize it's much easier to make the sandwiches on full square pieces of bread, and then cutting them into triangles."
    mc "Stupid idiot, party of one."
    "For some reason, self deprecation motivates me."
    "I finish the sandwiches in a flash after realizing the easier way to go about it, then I put a pot of water on the stove to make rice."
    "Once the water is boiling, I empty a bag of rice into it and continue to make rice like I've always done."
    "Finally, the fruit salad."
    "I pull apples, grapes, and oranges out of the refrigerator and start cutting, pulling, and peeling in order to create a presentable assortment."
    "I finish the fruit salad, then pull a can of whipped cream out of the fridge to complement it."
    mc "Sayori will like that the most, I think."
    "Everything is finished in about forty minutes."
    "Hm, maybe I could've taken my time just a little bit."
    "But I guess now I have time to look for..."
    mc "Oh, crap."
    mc "I don't think I own a picnic basket."
    mc "Stupid [player], stupid, stupid, stupid!"
    mc "*Sigh* It's fine. I have beach bags I can use."
    "I go to a closet in the hallway and grab a bag I can place all my food into."
    mc "Alright, I think that's good."

    if distraction == "Monika":
        $SayoriVar -= 1
        scene bg livingroom
        with wipeleft_scene
        "I sit in the living room catching my breath after that panic picnic preparation and wait for Sayori to come back."
        "As Monika promised, it took almost sixty minutes exactly for Sayori to walk back into my house."
        "If nothing else, you can call Monika trustworthy."
        show sayori 4bp at t11 zorder 2
        s "Ugh, that was so {i}boring{/i}!"
        s 4bh "I get that I'm vice president and everything but did she really need me for that?"
        show sayori 4bg at t11 zorder 2
        mc "W-what was it all about, anyway?"
        s 3bc "Stuff about advertising for the club and coming up with more activities for club meetings, regular stuff, but it made me wanna fall asleep."
        show sayori 3bb at t11 zorder 2
        mc "Yeesh, that's...unfortunate."
        "I pull out my phone, a little cheesed at Monika."
        "I send her a text."
        mc "{i}What the heck, Monika, I said to distract Sayori, not bore her to tears!"
        "A moment later she replies."
        m "{i}It was deliberate. Trust me, itll make your surprise that much better x3"
        "Hm, I wonder what she means."
        "Maybe Sayori being bored will get her more excited about this picnic?"
        "If that's the case then she did a good job."

    elif distraction == "Yuri":
        scene bg livingroom
        with wipeleft_scene
        "I sit in the living room catching my breath after that panic picnic preparation and wait for Sayori to come back."
        "The very moment my butt hits leather, Sayori walks in the front door, looking extra energetic."
        show sayori 1br at l11 zorder 2
        s "Yuri makes suuuch good tea! I feel on top of the world!"
        show sayori 1bq at h11 zorder 2
        pause(0.2)
        show sayori 1bq at h11 zorder 2
        "She stands in the center of the living room twirling like a ballerina."
        show sayori 1br at h11 zorder 2
        s 1br "I'm walking on sunshiiine, whooo-ooa!"
        show sayori 1bq at h11 zorder 2
        "...This isn't what I expected, but I can't say I'm not enjoying it."
        show sayori 1bq at h11 zorder 2
        mc "What was in that tea she gave you?"
        show sayori 1br at h11 zorder 2
        s "Caffeine, sugar, more caffeine, and {i}more sugar!{/i}"
        show sayori 1bq at h11 zorder 2
        "This is remarkably different from the daydream I had..."
        show sayori 1bq at h11 zorder 2

    elif distraction == "Natsuki":
        $SayoriVar += 1
        mc "I wonder how much longer they have on those cupcakes."
        scene bg livingroom
        with wipeleft_scene
        "I go to the living room and lie down, then close my eyes to rest."
        mc "I think this is going well. I just hope she comes back soon."
        stop music fadeout 1.5
        "..."
        "..."
        scene black
        with dissolve
        mc "URNGKH!"
        "I realize I was asleep, and I've now been awoken by...a cupcake?"
        "There's icing all over my face and a cupcake inside of my mouth."
        mc "Gahh..."
        mc "Sayori!"
        scene bg livingroom
        with fade
        show sayori 1br at t11 zorder 2
        play music t6
        s "Ahahahaha~!"
        s "You should've seen the look on your face!"
        s "Wait, I can show you!"
        show sayori 1bq at t11 zorder 2
        "She shows me her phone and a video of me, asleep, with her arm, cupcake in hand, approaching my open mouth, then stuffing it, icing first, inside of my mouth."
        "I want to be mad, but I have to admit she got me."
        "Plus the icing tasted good so who am I to complain."
        mc "You little prankster, come here!"
        show sayori 1br at h11 zorder 2
        pause(0.2)
        show sayori 1br at h11 zorder 2
        pause(0.2)
        show sayori 1br at h11 zorder 2
        s "Ahhhhhh! Ahahaha~!! Nooo~!"
        show sayori at thide
        hide sayori
        "I chase Sayori around the living room as a measure of revenge, then she stops."
        s "Wait!"
        scene bg kitchen
        with wipeleft_scene
        "Finally she walks to the kitchen counter, places the tray of fresh cupcakes on top of it, then continues running again."
        s "Catch me if you can, meanie~!"
        scene bg livingroom
        with wipeleft_scene
        "I oblige, then chase her around the living room some more, until I corner her, lift her over my shoulder like a fireman, then playfully drop her onto the couch."
        s "Hehehe...you got me~."
        "Quickly she lifts her head and gives me a peck on the cheek."
        mc "That was a nice reward."
        s "That wasn't the reward, that was for me."
        s "This is your reward."
        "Sayori pulls me on top of her and passionately starts to kiss me."
        "As tempting as it would be to take it a step further, I decide to end it there, then continue with our day like I'd planned."

    mc "Hey, Sayori, I have a good idea about what to do today."
    show sayori 1bx at t11 zorder 2
    s "Really? What is it?"
    show sayori 1ba at t11 zorder 2
    mc "Uh...one sec."
    scene bg bedroom
    with wipeleft_scene
    "I run to my bedroom and grab a sleeping mask I have lying around, then bring it back to Sayori."
    scene bg livingroom
    with wipeleft_scene
    show sayori 1bn at t11 zorder 2
    s "We're taking a nap?"
    mc "Ahaha, no silly. Here, put this on, and on top of that close your eyes so you won't be able to see."
    s 1bc "Are you sure about this?"
    show sayori 1bb at t11 zorder 2
    mc "Come on, don't you like surprises?"
    s 1bx "Uuu, yeah I guess I do. Okay, I'll play along, [player]."
    show sayori 1bq at t11 zorder 2
    "Sayori beams brightly at me, then with her smile still shining bright I put the sleeping mask over her eyes."
    show sayori at thide
    hide sayori
    s "Wow, it's pitch black!"
    show sayori blio at t11 zorder 2
    mc "Ahaha, perfect. Now, hold my hand, we're going outside."
    s blim "Wait, what?! Is that safe?"
    mc "Hey you said you'd play along!"
    mc "Besides, don't you trust me?"
    show sayori blig at t11 zorder 2
    "Sayori hesitates just a bit more this time around but she produces an answer."
    s blix "Alright, fine, I trust you."
    show sayori blia at t11 zorder 2
    mc "Perfect! Let's go!"
    "With Sayori's eyes covered, I grab her hand and lead her to the kitchen with the picnic bag, hoping not to shake it around too much so's to not give away the surprise."
    "Finally, we approach my front door then exit my house."
    scene bg residential_day
    with wipeleft_scene
    show sayori blio at t11 zorder 2
    "With Sayori's arm interlocked with mine we gingerly walk toward the park close to our neighborhood."
    "I haven't been there in a long time other than just passing through to get to the store or something, and I haven't been there with Sayori in an even longer time."
    "Sayori still seems nervous about walking outdoors with her eyes closed."
    "Honestly, now that we're actually doing it I can't really blame her, but I trust myself enough to not let her--"
    show sayori blip at s11 zorder 2
    s "WHOA!"
    mc "Oh gosh, Sayori!"
    "Sayori seems to have tripped over a crack in the cement but I was able to pull her back to her foot before she could faceplant."
    show sayori blih at h11 zorder 2
    s "[player], this is really difficult!"
    show sayori blig at t11 zorder 2
    mc "Hang tight, we're almost there."
    "We make a right turn and then walk another quarter of a mile before we arrive at the park."
    scene bg park
    with wipeleft_scene
    show sayori blio at t11 zorder 2
    "I lead us to a nice patch in the middle of the grass, and Sayori takes notice."
    s blic "Hey, are we on grass now?"
    mc "Uh-huh. Just stand right here, and don't take the mask off until I say so, okay?"
    s blig "*Sigh*"
    s blih "Okay..."

    show sayori blih at thide
    hide sayori

    "She seems to be losing some patience, but I think it'll be worth it."
    "I unpack the bag, pull out the blanket, spread across the ground, then individually place the sandwiches, the salad, the rice, and a non-alcoholic beverage around the fabric terrain."

    if distraction == 'Natsuki':
        "I also place the cupcakes front and center for Sayori to see."

    "Taking one final look at the presentation and making sure everything is in a good spot, I turn and look at Sayori."
    mc "Okay, you can take it off!"
    show sayori 4bn at t11 zorder 2
    "Rapidly, like she was trying to set a world record, Sayori rips the mask off and slings it away with no regard for the fact that it's mine."
    "I can ignore that for the adorable expression Sayori has on her face at this moment."
    s 4bc "[player]..."
    show sayori 4br at t11 zorder 2
    s "Ahhhh~! This is so awesome!"
    show sayori 4br at h11 zorder 2
    s "I love it I love it I love it!"
    s 2bc "But wait, when did you even have time to prepare all this?"
    show sayori 2ba at t11 zorder 2
    mc "Well, I had a little bit of help."

    if distraction == 'Monika':
        mc "That's why Monika dragged you away to take care of \"important club business\", because I asked her to help me distract you while I made all of this."

    elif distraction == 'Yuri':
        mc "That's why Yuri wanted to see you at your house. I asked her to help me distract you so you wouldn't suspect anything I was doing."

    elif distraction == 'Natsuki':
        mc "That's why Natsuki asked if you wanted to make cupcakes with her today, so that you'd be too preoccupied to know I was preparing all of this for us."

    s 4bh "[player]..."
    s 4bk "I...don't know what to say..."
    s 4bh "You did...all of this...for me?"
    s "A-and...[distraction] actually wanted to help?"
    s 4bk "I...I don't...I don't deserve all this..."
    show sayori 4bu at t11 zorder 2
    "Sayori starts to sob lightly."
    "I go over to her and wrap my arm around her shoulder."
    show sayori at thide
    hide sayori
    mc "Of course you do. And of course she wanted to help."
    mc "You spend so much of your energy trying to make us all happy as can be."
    mc "It's only natural we try to return the favor, right?"
    mc "Nobody deserves it more than you."
    mc "You're an angel and a blessing."
    mc "I love you so much, Sayori."
    s "*sniffle* I love you too, [player]."
    s "No number of \"thank you\"s could be enough to tell you how much this means to me."
    mc "Just one is enough, trust me."
    mc "Now, let's have lunch."
    mc "I worked really hard on this."
    show sayori 1bt at t11 zorder 2
    "Sayori and I sit down on the blanket and start to eat our lunches."
    show sayori 1br at t11 zorder 2
    "She's got nothing but good things to say about the food I made, which makes me happy."
    "Pretty soon after, Sayori speaks up with a mouthful of sandwich."
    s 1bo "Mmf, [player], 'ou 'anna 'lay a 'ame?"
    mc "Chew and swallow, Sayori, chew and swallow."
    show sayori 1br at t11 zorder 2
    "She does so, then giggles."
    s 1bx "Sorry! I was trying to say, do you wanna play a game?"
    show sayori 1ba at t11 zorder 2
    mc "Oh, sure! What'd you have in mind?"
    s 1bx "How 'booooout I Spy?"
    mc "That's a little childish, isn't it?"
    show sayori 1ba at t11 zorder 2
    s 1bc "Hey, I Spy is fun! You just have to get creative with it!"
    show sayori 1ba at t11 zorder 2
    mc "Hm, okay, why not."
    "Taking a look around the park, I can see that we're surrounded by a lot of stuff."
    "I have a feeling Sayori could get tricky with this."

    if battleship_played:
        s 3bx "Oh, and by the way..."
        s 3br "If you get an answer wrong, you have to take off some clothes."
        show sayori 3bq at t11 zorder 2
        mc "W-w-w-what?!"
        s 3br "Ahaha~! I'm joking, we're in public!"
        show sayori 1bq at t11 zorder 2
        mc "O-oh."

    s 1bx "Come on, let's play."
    stop music fadeout 1.5
    s 1br "Do your best!"
    "Let's go..."
    play music t4

    $point = 0

    show sayori 1bx at t11 zorder 2
    menu :
        s "Something red, mine got stuck in a tree once!"
        "A kite" :
            show sayori 1br at h11 zorder 2
            s "Congrats!"
            $point += 1
        "A cherry" :
            s 1bx "Nope!"
        "Your bow tie" :
            s 1bc "I'm not that tall!"
        "Some lipstick" :
            s 1bx "Nuh-uh!"

    show sayori 1bx at t11 zorder 2
    menu :
        s "A fruit that I'd be terrified of if I were a doctor!"
        "A banana" :
            s 1bx "Wrong!"
        "A cherry" :
            s 1bx "Still nope!"
        "An apple" :
            show sayori 1br at h11 zorder 2
            s "Yay!!"
            $point += 1
        "A pineapple" :
            s 1bn "Is that even a fruit?"

    show sayori 1bx at t11 zorder 2
    menu :
        s "Something heavy and good luck pushing that!"
        "Your butt" :
            s 1bj "You meanie!"
        "The Eiffel tower" :
            s 1bx "How I would love to see it! But {i}non!{/i} Ahaha!"
        "A big rock" :
            show sayori 1br at h11 zorder 2
            s "Got it!"
            $point += 1
        "A black hole" :
            s 1bc "Way too complicated!"

    show sayori 1bx at t11 zorder 2
    menu :
        s "Something big I'd like to climb!"
        "A tall tree" :
            show sayori 1br at h11 zorder 2
            s "We have a winner here!"
            $point += 1
        "The Eiffel tower?" :
            s 1bx "Still nope!"
        "A building" :
            s 1bx "Good guess but no!"
        "My d... *gulp*" :
            s 1bp "We're in public, [player]!"         

    show sayori 1bx at t11 zorder 2
    menu :
        s "Something round!"
        "The moon" :
            s 1bx "Very poetic, but nope!"
        "Your br...beautiful eyes?" :
            s 1bh "My...eyes? N...nope."
        "An American" :
            s 1bc "Whaaat? No!"
        "A soccer ball" :
            show sayori 1br at h11 zorder 2
            s "Yes! Makes me wanna play!"
            $point += 1

    show sayori 1bx at t11 zorder 2
    menu :
        s "Something really fast!"
        "A plane" :
            show sayori 1br at h11 zorder 2
            s "{i}Wooosh!{/i} Yes!"
            $point += 1
        "My heartbeat when I see you" :
            s 1bs "Aaawww. Unfortunately, nope!"
        "The light" :
            s 1bc "Is that that fast?"
        "My boredom in math" :
            s 1br "Haha it is really boring, yes! But no!"

    show sayori 1bx at t11 zorder 2
    menu :
        s "Something cute that is definitely not me! Ehehe~!"
        "Yuri" :
            s 1br "I'll tell her you said that! But nope!"
        "Can't think of anything else than you" :
            s 1bs "Aaw, you flirt. Doesn't count!"
        "A rabbit" :
            show sayori 1br at h11 zorder 2
            s "Those ears are melting my heart! Good answer!"
            $point += 1
        "Natsuki" :
            s 1br "Don't let her catching you say that! And wrong!"

    s 1bx "Last but not least..."

    menu :
        s "Something you love to play with! It's a living thing!"
        "Your boobs?" :
            s 1bp "THEY ARE NOT ALIVE!"
        "A...living...controller?" :
            s 1bm "Eww like in that movie? Gross! Nope!"
        "A cat" :
            s 1bx "I love cats too! But no!"
        "You" :
            s 1bs "...correct. Ehehe~!"
            $point += 1


    #{Commence mini-game from here}
    #{Preferably use Dreams of Love and Literature during it}

   # Sayori descriptions:

    # Strings are separated by commas. Read this as...
    #     The first string is the object you need to find, 
    #     Second string is what comes after "I spy ", 
    #     Third string is what comes after "A hint? Well... "
    #
    # The last two are dummy objects that you can click on, but don't actually have a prompt tied to them (and thus don't have hints either).

    # Format: object,prompt,hint

    #kite,something red,Mine got stuck in a tree!
    #apple,a fruit,I'd be terrified if I were a doctor!
    #big rock,something heavy,Good luck pushing that!
    #big tree,something tall,I want you to climb it later!
   # soccer ball,something round,I'm not sure what your {i}goal{/i} is asking for a hint on this one.
   # bird,something flying,I hope it doesn't poop on us!
   # balloon,something yellow,Don't let it pop!
   # banana,something bent,Don't slip on one!
   # fire hydrant,something important,I've dreamed of being a firefighter growing up!
    #sayori,what you loved to play with,{i}*giggles*{/i} It's a living thing!
    #plane,something fast,It's basically a magical bus!
    #rabbit,someone cute,It's definitely not me! {i}*giggles*{/i}
   # cherry,DUMMY_OBJECT,DUMMY_HINT
    #lamp post,DUMMY_OBJECT,DUMMY_HINT

    # { back to the script }

    show sayori 1bx at t11 zorder 2
    s "That was fun, wasn't it?"

    if point == 8 :
        $SayoriVar += 1
        s 1br "And you even got all the right answers!"
        show sayori 1bq at t11 zorder 2
        mc "Does that mean I got a nice reward?"
        s 1bs "Ehehe~! Maybe later..."
    elif point == 0 :
        s 1bn "Even if you didn't got a single good answer!"
        mc "I totally did that on purpose."
        s 1bx "Suuuuuuure !"
    elif point < 4 :
        s 1bc "You could have done way better though! More than half of your answers were wrong!"
        show sayori 1bb at t11 zorder 2
        mc "Having fun is the most important part!"
        s 1bx "Guess you're right!"
    else :
        $SayoriVar += 1
        s 1br "You even managed to get more than half of the good answers! Good job, [player]!"
        stop music fadeout 2.0
    show sayori 1ba at t11 zorder 2
    mc "I have to admit, it was a good time."
    mc "You always have good ideas, Sayori."
    s 1bb "Oh, stop. You're the one who planned this whole thing out."
    show sayori 1bb at t11 zorder 2
    mc "Hey I'm sure you'd do the same thing for me."
    s 1bf "..."
    mc "Sayori?"
    s 1bk "[player]..."
    play music t10
    s 1bh "Do you really think I'm thoughtful enough for that?"
    show sayori 1bf at t11 zorder 2
    mc "W-what are you talking about?"
    s 3bh "You planned out this amazing day for me without hesitating even a bit."
    s "You committed to taking me on a picnic as soon as the idea popped into your head."
    s "I just don't think I have the motivation you do."
    s 4bk "I don't think...I'm as good to you as you are to me."
    "..."
    mc "Sayori, you really don't have to think that way."
    mc "I did this because I love you and wanted to do something special for you."
    show sayori 4bf at t11 zorder 2
    mc "I-I-I wasn't trying to make you feel bad...I'm sorry if I did."
    "Is it possible that this picnic was too extravagant?"
    mc "But Sayori, you've already done plenty of amazing things for me! For instance, that poem you wrote about me for the Literature Club not too long ago!"
    s 4bh "That's different, [player], that was an assignment."
    show sayori 3bf at t11 zorder 2
    mc "Still, you didn't have to write about me, but you did anyway. I'm touched by that."
    s 3bh "Well to tell you the truth..."
    s "You're the only good thing about my life right now."
    s "Of course I'm gonna write about you."
    s 4bv "I have nothing else going for me at all..."
    show sayori 4bu at t11 zorder 2
    mc "Sayori, if that's how you feel, then I'm in the same boat."
    mc "If I wasn't with you then I have no idea where my life would be right now."
    s 4bv "I think you'd probably be dating someone else."
    show sayori 4bu at t11 zorder 2
    mc "Oh yeah? Like who?"
    s 2bv "Monika, probably."
    s "She's got so much going for her, and I'm sure that if you were dating her, she'd be thoughtful enough to make you a picnic like this..."
    s "Or throw you surprise birthday parties..."
    s 4bw "Or cook food for you without burning it!"
    s "[player], why do you even like me?!"
    if sayori_confronted == True:
        s "All I do is mess things up and make everyone mad like with Monika's jacket!"
        s "Or Natsuki and Yuri's argument about us in club!"
    else:
        s "All I do is mess things up and make everyone mad like when Natsuki and Yuri started arguing about us!"

    s "I'm a complete failure, you shouldn't want to be with me!"
    mc "Sayori!"
    mc "Please please please relax!"
    show sayori at thide
    hide sayori
    "I pull Sayori toward me and shush her as she sobs into my shoulder."
    s "You shouldn't want me, [player]."
    mc "Yes I should, and I do."
    mc "I've never once been upset with something you've done."
    mc "When you burned the eggs, I didn't care. I was happy you wanted to make me breakfast."
    if sayori_confronted == True:
       mc "When Monika got mad at you for the jacket, I defended you."

    mc "When Natsuki and Yuri got into that fight, it wasn't your fault whatsoever!"
    mc "Nothing that happens is as bad as you make it out in your head, Sayori, you don't need to feel so bad."
    s "I'm even bad at knowing when to feel bad..."
    s "I hate this endless cycle, [player]."
    s "I hate how my head works."
    s "I just want it to stop forever."
    mc "I'll help you, Sayori. There are steps we can take. Nothing is impossible."
    "Sayori stays silent, simply getting her breathing back to normal after a few minutes of crying."
    "I want her to relax, I really do."
    "I stroke her along the length of her back to calm her down, and I kiss her on the top of her head."
    "I whisper to her..."
    mc "{i}You can do this, Sayori. I believe in you.{/i}"
    "Sayori squeezes me tighter."
    "We lie there for what feels like hours, with nothing but the sound of animals and kids playing in the park."
    "As we do so, she speaks up for the first time in quite some time."
    s "I think I'm ready to finally go."
    #{It's assumed she means, "go home", but perhaps she means "go" in another way (Oof)}
    "Agreeing with her, I take her hand and help her up off the floor."
    "Together we clean and pack up our picnic, then head back to my house."
    
    stop music fadeout 1.5
return

   # {H-scene goes here}
    #{Set-up: arrive home from picnic, Sayori wants to repay MC and also satiate her needs, therefore, sex, naturally}
    # Unfortunatly...nope
   # {Will do this down the line somewhere}
