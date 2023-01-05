label Monika3:
    #C1 - Jan 16th - Pep Talk
    stop music fadeout 2.0
    #---TESTING, DELETE BEFORE RELEASE---
    menu
        "SayoriVar setting"
        "=3":
            $ SayoriVar = 3
        "=2":
            $ SayoriVar = 2
        "=1":
            $ SayoriVar = 1
        "=0":
            $ SayoriVar = 0
    #------------------------------------
    scene bg class_day 
    with dissolve_scene_full
    play music t3
    "With the holidays over and long behind us, school has turned into a long and boring drag."
    "The next big break is still far away and it seems like the teachers want to cram as much school work on us as they can before we get there."
    "The students, however, seem to be more fixated on the big holiday for February."
    "I've never really paid attention to Valentine's Day in the past, it was always a holiday for the young couples of our school to over exaggerate."
    "For the rest of us it was a day for joking about being single, with varying levels of self-deprecation."
    "Well, I guess I've gone from the latter category to the former. Monika has been going non-stop about what we could do for a date since the month started."
    "She really wants it to be something we can remember, and if I'm being honest with myself I'm on the same mindset."
    "I wouldn't want my first real Valentine's Day to be a wreck."
    "As the bell rings for the last time today, a silent cheer rings through the room as we pack our things and start to make our way out of the room."
    scene bg h_corridor 
    with wipeleft_scene
    "I sling my bag over my shoulder and start to make my way to the club room for the day."
    "My mind wanders to the poems I had been working on yesterday, trying to think of ways to make it better."
    "Moving to publishing these in the school paper has really raised the bar on how good they need to be."
    "I miss the days where all they had to do was impress Monika, now they have to impress enough people to sell copies."
    "As I'm walking, I notice a few students congregating near a pair of benches."
    "My curiosity gets the better of me and as I close the distance I notice one of the small newspaper dispensers at the center of the group."
    "One of the students slots a coin into the machine and a fresh copy of the latest edition drops into the open slot."
    "A smile creeps across my face as I pass them, at least one of my poems went into the paper this week."
    "Maybe those poems were good enough after all."
    scene bg corridor 
    with wipeleft_scene
    "As I neared the clubroom the students started to thin out in the hallways until I was walking alone."
    "The silence was nice for writing, but I always wished Monika would have picked a room a little closer to the rest of the clubs."
    "I sighed to myself as I took the doorknob in my hand and opened the door."
    scene bg club_day 
    with wipeleft_scene
    mc "Hey everyone, I'm here."
    show monika 2b at l11 zorder 1
    m "[player], finally!"
    m 4l "I was waiting for you to get here before starting today."
    show monika 2a
    mc "Sorry, I guess I got caught in the traffic rush today."
    m 2n "It's alright, I know those hallways are tough to navigate when everyone is walking through them."
    m 3b "But anyway, now that you're here I can finally start the club for today."
    show monika 1c at t22
    show natsuki 2k at l21
    show natsuki at f21
    n "But Monika, we already know what we're working on today."
    n 2t "I mean, did we really need to wait for [player] to get started?"
    show monika 2e at t33 zorder 4
    show natsuki 1c at t32 zorder 3
    show sayori 3n at l31 zorder 2
    show sayori at f31
    s "Ooo, are we going to do something special today that Monika was waiting to reveal?"
    s 4p "Tell us Monika, tell us!"
    show monika 2m at t44
    show natsuki 1k at t43
    show sayori 2m at t42
    show yuri 2h at l41 zorder 4
    show yuri at f41
    y "Well if Monika wanted all of us here it must be important."
    y 1f "Please, do tell us what you have in mind."
    show yuri 1g at t41 zorder 1
    show sayori 1o
    show natsuki 2m
    show monika 4n at f44
    m "Oh, well I didn't have anything {i}that{/i} special planned guys."
    show sayori 1b
    show natsuki 3k
    show yuri 1e
    m 3b "I just wanted to give a little praise to everyone for how much love and effort you guys are putting into this."
    show sayori 1a
    show natsuki 1j
    show yuri 2i
    m 2e1 "It means a lot to me that you all want to put your best work into the school paper."
    m 4n "I know I kinda dumped this all on you without any real warning, but I'm so glad you all decided you wanted to work on this."
    m 2k "Now instead of just us five, everyone in the school has a chance to enjoy your writing and I think that's really amazing!"
    m 3b "And as long as we keep writing, our skills can only get better."
    m 1l "Alright, I think that's all I had planned to say."
    m 4k "Okay everyone, let's take a break today! You're free to do whatever you like!"
    show monika 2a at t44
    show sayori 4r at f42 zorder 4
    s "Yay! Nap time! Ehehe~!"
    show sayori at t42 zorder 3
    show natsuki 4l at f43 zorder 4
    show monika zorder 3
    n "Sweet, I can catch up on my newest volume of Parfait Girls!"
    show monika zorder 4
    show natsuki zorder 3
    show yuri 3q at f41 zorder 4
    y "Oh, I guess I can finally start that new novel as well."
    show yuri 2i at lhide zorder 1
    hide yuri
    show sayori at lhide zorder 1
    hide sayori
    show natsuki at lhide zorder 1
    hide natsuki
    show monika at t11 zorder 4
    "The girls walked back to their usual chairs, a new found energy radiating between all of them."
    "I turn to Monika, seeing a warm smile radiate from her face as she looks over the club."
    show monika 2c
    mc "It seems like your speech did wonders, everyone looks ecstatic now."
    m 2b "Yup, just the energy we like to see in this club."
    m 2e1 "I also should be thanking you personally, [player]."
    show monika 2e
    mc "Me? I've just been doing my part like everyone else though."
    m 4e1 "It's not just about writing for the club, I want to thank you for everything so far."
    m 1n "You've really helped me keep my spirits up, even just by being by my side."
    show monika 1e
    mc "Aww jeez, it's nothing Monika."
    show monika 1j at face 
    with dissolve
    "I reach out my arms and Monika gladly plants herself against my chest, wrapping her own arms around my torso."
    show monika 3n at t11
    m "So um, while you're still happy with me..."
    show monika 2m
    mc "Monika, where are you going with this?"
    m 4n "Well.. I kinda need to grab some supplies for the clubroom from the supply room down the hall."
    m 5a1 "I was wondering if my big strong boyfriend could help me grab a couple boxes of paper while I grabbed some other stationery supplies."
    show monika 5a
    "As much as I would like to, how could I resist Monika with a smile like that."
    show monika 1j
    mc "Ugh, you know just where to hit me. Alright, let's get this over with."
    m 1k "Thank you [player], ahaha~"
    m 2b "Hey everyone, I'm going to grab some supplies with [player]. Sayori, you're in charge till we get back."
    show monika 2c
    s "Okay! I'll make sure nothing is broken before then!"
    show monika 2e
    n "Sayori, we should be worrying about {i}you{/i} breaking stuff."
    y "Girls, please!"
    show monika 1j at lhide zorder 1
    hide monika
    "Monika made her way out of the clubroom, waving me along."
    "I took one last look at the others before making my way out of the room as well."
    stop music fadeout 1.5

#C2
    scene bg corridor 
    with wipeleft_scene
    play music tmonika
    show monika 1j at t11 zorder 4
    "Monika immediately took my hand as we started down the hallway, a wide smile across her face."
    m 1k "I love this time of year, all the happiness flowing through the halls. Can't you feel it in the air, [player]?"
    show monika 1a
    mc "Hmm? What do you mean?"
    m 1b "Valentine's day is almost here silly!"
    m 3k "It's actually one of my favorite holidays believe it or not."
    m 2b "A day dedicated to love and the people who mean the most to you, it's such a heartwarming atmosphere."
    show monika 2c
    mc "Yeah, I guess so..."
    m 1g "Is something the matter [player]?"
    show monika 1c
    mc "No nothing is wrong, it's just... weird..."
    show monika 1f
    mc "I've always seen this time of year as a sort of drain, seeing others enjoy themselves while I mostly spent it by myself."
    m 3e1 "But now it's different, right?"
    m 5a1 "You have someone to look forward to spending Valentine's day with now~"
    show monika 1j
    mc "You're right, it's all just so new to me I suppose."
    m 3e1 "It's new to me too [player], but we'll learn together!"
    m 2k "Cause that's what couples do! Ahaha~"
    show monika 1j
    "Monika giggles as she clutches my arm and I can't help but smile along with her."
    scene bg h_corridor 
    with wipeleft_scene
    show monika 1a at t11
    "We make the long hike across the school and make our way to one of the large supply closets."
    show monika 2a
    "As we near the door Monika reaches into her blazer pocket and extracts a small key."
    show monika 1c
    mc "Wait you need a key for this closet? How did you get one?"
    m 3b "Well I'm a club president after all!"
    m 2b "The school gives one to each club so they can grab stuff when they need to. Of course we need to sign out what we take so they can keep track of things."
    m 2r "Though it took forever for the student council to actually get me my copy of the key."
    m 4i "I had all the papers submitted the day you officially joined the club and they waited till {i}just before{/i} the festival to get around to giving it to me."
    show monika 2c
    mc "So how did you get club supplies before? Sayori goes through pencils like candy and Natsuki burns out erasers re-writing things a dozen times."
    m 3n "Well... that may reflect poorly on me as a club president..."
    show monika 1m
    mc "What, did you steal them or something?"
    m 2l "Gosh no, I'm not that bad [player]!"
    m 2e1 "Some of the writing teachers that helped me create the club told me I could use some of their supplies if I ever needed to."
    m 2n "Of course, I didn't want to depend on their supplies for that long..."
    m 4k "And since we're an official club now I don't have to keep bothering them anymore!"
    m 1b "But enough about that, let's grab the stuff we need and get back to the girls."
    show monika 1a
    mc "Alright, I can already feel that something is either broken or amiss while we're here."
    m 3l "You feel it too? I thought I was the only one, ahaha~"
    show monika 1a
    "Monika slots the key into the keyhole and turns it to unlock the door."
    show monika 1d at t43
    stop music fadeout 2.0
    "As soon as she reached for the handle however, it turned on its own and the door swung open."
    "Standing in the doorway were two girls of our grade, both of them holding a few small notebooks."
    $ y_name = "Girl 1" #<-- Name changes just an FYI
    $ n_name = "Girl 2"
    play music t7
    y "Oh. My. God. Is that {i}Monika?!{/i}"
    n "Where have you been girl? We've missed you!"
    show monika 1n at t11
    m "Veronica, Rachel, it has been a while hasn't it?"
    show monika 1m
    "I'm completely speechless at the current string of events."
    "Were these some of Monika's friends? Should I know these girls already?"
    m 3n "[player], this is Veronica and Rachel from the debate club."
    m "Veronica and Rachel this is [player], my-{nw}"
    $ y_name = "Veronica"
    $ n_name = "Rachel"
    show monika 1m
    y "Noooo, {i}the{/i} [player]?"
    n "O.M.G, I've heard, like, sooo much about your new {i}boyfriend{/i} Monika!"
    show monika 1d at t44
    m "Hey!"
    "The girls close in on me, cutting Monika off and cornering me."
    show monika 1c
    y "So you're the one that our Monika is {i}dating{/i} now?"
    n "He doesn't even look that cute though... like, his face is so weird."
    show monika 1h
    y "And his arms look so scrawny too, I bet even I could beat him up."
    n "What does Monika even see in you anyway? Is she pity-dating you? I feel {i}soooo{/i} bad."
    n "I bet she wishes she could take someone like our boyfriends out in public."
    y "I bet she's talking to a few guys already and we don't even know!"
    n "Aww and poor little [player] here is none the wiser, huh?"
    y "I bet she doesn't even want to have-{nw}"
    m 1i "{b}ENOUGH.{/b}"
    show monika 1i at t43
    m "You are {b}NOT{/b} going to talk down my boyfriend in front of {b}ME{/b}."
    show monika at t11
    m 3r "I will {i}personally{/i} make sure you two regret it if I have to."
    show monika 1h
    y "Oooo, you're getting {i}feisty~{/i}"
    n "Cat fight, cat fight!"
    m 1i "Just go back to your club so I can get my stuff and go back to mine."
    show monika 1h
    y "Oh right, your little \"literature club\" or whatever it was called."
    n "More like \"drama club\" if you ask me."
    m 1r "Give it a break already."
    m 1i "Don't you have anything better to be doing?"
    show monika 1h
    n "Why, when seeing you like this is {i}exciting.{/i}"
    y "Come on Rachel, lets leave poor Monika and her poor cuck to themselves while we go see our wonderful boys."
    "The two walk off with their noses pointed up at us, snickering to themselves as they walk down the hallway."
    stop music fadeout 6.0
    show monika 1q
    "I was completely speechless, the unforeseen bombardment that came from the both of them left me completely empty."
    "Is that what girls see in me? Is that why I was alone for so long..."
    m 2r "[player], please don't take a single word those... {i}bitches{/i} said seriously okay?"
    play music t9
    show monika 2q
    mc "M-Monika..."
    m 2r "I don't know why I ever associated myself with those two anyway, nothing but bricks in those heads of theirs."
    m 1i "Saying stuff like that to you, what right do they think they have?"
    m 1r "It makes me so upset I could... gahh!"
    show monika 1f
    mc "Hey, hey, don't worry about it. I'm not hurt by it anyway."
    m 1g "But they said so many mean things!"
    m 1p "I would never do something like talk to other people behind your back..."
    show monika 1o
    mc "And I know that, they're just some mean words with no truth."
    mc "They're just jealous of what we have, that's all."
    m 2n "Yeah, they're just jealous of what we have."
    m 1e1 "They're just jealous they don't have someone like you."
    show monika 1j at face 
    with dissolve 
    "Monika reaches out and wraps her arms around my waist, pulling herself tightly against my chest."
    "I could feel her rapid heartbeat through my jacket and shirt, she must have been really fired up at them."
    "I run my hand through her hair and gently caress her back with my other hand as I return her hug."
    mc "Let's grab the stuff we need and get back to the club Monika, then we can really relax."
    m 1e1 "Can we stay like this just a bit longer, please?"
    show monika 1e
    mc "Alright, just a little more."
    show monika 1j
    "Monika buries herself ever deeper into my chest, and I couldn't have complained even if I wanted to."
    stop music fadeout 2.0
    show monika at thide
    hide monika

#C3
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    scene bg corridor 
    with wipeleft_scene
    play music t3
    "As we made our way back to the club room, my arms begged me for mercy."
    "Monika had decided we needed three whole boxes of paper for the club instead of the original two."
    show monika 1o at l11 zorder 4
    "Monika had been quiet for most of the way back, with a slight frown seemingly stuck on her lips."
    show monika 1c
    mc "Monika?"
    m 1d "Yeah?"
    show monika 1c
    mc "You doing okay?"
    m 1n "Yeah, I'm fine."
    m 1e1 "How are you doing [player]?"
    show monika 1e
    mc "I'm doing the best I can, but I don't know if I'm going to make it though."
    m 1l "I'm sorry, I shouldn't have signed out three boxes. I just wanted to make sure we had plenty of paper for everyone."
    show monika 1e
    mc "I just hope this much will last a while so we don't have to do another supply run soon."
    m 1n "What, do you not like spending time with me?"
    show monika 1e
    mc "Come on, that's not true and you know it."
    show monika 1m
    mc "I just don't want to throw my back out carrying boxes across the school."
    m 3l "I could have taken one, you know."
    show monika 1c
    mc "I'm supposed to be the big strong boyfriend though, remember?"
    m 1e1 "[player], you're plenty strong for me. You don't have to push yourself to impress me or anything."
    m 1g "I would feel bad if you got yourself hurt doing something like that for me."
    show monika 1e
    mc "I wouldn't get myself hurt, trust me."
    m 1e1 "I'll take your word for it."
    m 1b "Hey, we're almost to the club!"
    show monika 1a
    "We rounded the last corner and the familiar room number came within sight."
    "Monika walked ahead of me and rapped her foot against the door."
    m 1b "Hey guys, can you come open the door for us? Our hands are full!"
    show monika 1a
    s "They're back, they're back! I'll get it!"
    show monika 1d
    play sound "sfx/fall2.ogg"
    "A loud thud comes from the other side of the door."
    n "Jeez Sayori, careful!"
    show monika 1e
    s "I'm okay!"
    play sound closet_open
    "The door swings open and we step inside."
    show monika at lhide zorder 1
    scene bg club_day 
    with wipeleft_scene
    show monika 1a at l21 zorder 3
    show sayori 4x at t22 zorder 3
    show sayori at f22
    s "What did you guys get!"
    s 2m "Wow [player], those boxes look really heavy!"
    s 2n "You must be really strong if you brought all those here!"
    s 1s "But I already knew you were, ehehe~"
    show sayori 1a at t22
    show monika 3b at f21
    m "Yup, that's why I brought him along."
    m 2b "Now we should have enough paper and writing utensils to get us through a few more weeks of writing."
    show monika 2c at t21
    show sayori 1m at f22
    s "We're going to need all of this! We're going to be writing forever!"
    show sayori 1n at t22
    show monika 4l at f21
    m "No no, we're not necessarily going to use {i}all{/i} of this right away."
    m 4e1 "We grabbed enough so we wouldn't need to go back for a while."
    show monika 2e at t21
    show sayori 3l at f22
    s "Oh, {i}pheew{/i}, I thought we were going to write so much our hands would fall off."
    show monika 2c
    s 3c "So what took you guys so long? We thought you two had left the school."
    show sayori 1b at t22
    show monika 1p at f21
    m "Oh we..{w=.75} had a conversation with some people along the way."
    show monika 1m at t21
    mc "Yeah, I guess it just took longer than we realized..."
    show monika 1f at t21
    show sayori 2e at f22
    s "Monika, [player], what happened?"
    show monika 1o
    s 1h "You both look really upset, did they say something mean to you?"
    show sayori 1g at t22
    show monika 1q
    mc "Well..."
    show monika 2r at f21
    m "They just... said some insensitive things about us and to [player]."
    m "Stuff about us... being together."
    m 2p "I didn't think anyone would just openly say that to someone but I suppose I was mistaken."
    m 2e1 "But it was just some harsh words with no meaning behind them, it's behind us now."
    show monika 1o at t21
    show sayori 1j at f22
    s "What a bunch of meanies!"
    show monika 1e
    s 2j "They don't know anything about you two, and how happy you two are!"
    s 4h "How could anyone say stuff like that about you, about [player]?!"
    show monika 2c at t31
    show sayori 1b at t32
    show natsuki 5q at t33
    show natsuki at f33
    n "I would have just socked them right then and there."
    n 5w "What right do they have that they can just go and say stuff like that?"
    n 5r "No one should talk to my friends like that, no one."
    show natsuki 5s at t33
    show sayori 2a
    show monika 2e
    mc "Thanks Natsuki, I'm glad I could count on you to have my back."
    show natsuki 1t at f33
    show monika 2m
    show sayori 1d
    n "I didn't mean just you, I mean.. I would do the same thing for all my friends."
    show monika 2c at t41 zorder 4
    show sayori at t42 zorder 2
    show natsuki 3k at t43 zorder 3
    show yuri 1h at t44 zorder 4
    show yuri at f44
    y "Someone like that is just easier to avoid than confront."
    y 2l "They can spread all the lies and gossip they want but it's all just empty words."
    y 1j "The only truth they hold is the discontent everyone has in themselves and project on someone else."
    y 3p "W-wait did I ramble again? I'm so sorry!"
    y 3o "I got so caught up in my thoughts and I opened my mouth and..."
    show yuri 3n at t44
    show natsuki 3j
    show monika 4e1 at f41
    m "Yuri, you're absolutely right though. They're only projecting onto us."
    m 2e1 "Thank you, all of you, it really means a lot."
    show monika 2e at t41
    show yuri 3q at f44
    y "Um, yes, you're welcome..."
    show yuri 3u at t44 zorder 3
    show natsuki 4d at f43 zorder 4
    n "Any time! We don't let bullies get our friends down!"
    show natsuki 4a at t43 zorder 3
    show monika at t41 zorder 3
    show sayori 4r at f42 zorder 4
    s "Yeah! We make sure everyone is happy!"
    show natsuki at t43 zorder 2
    show sayori 1a at t42 zorder 3
    show monika 2e at t41 zorder 4
    mc "Thanks everyone, you guys are the best."
    show monika 4b at f41
    m "Okay everyone! Let's get back to enjoying club today."
    show monika 2c at t41 zorder 3
    show sayori 2c at f42 zorder 4
    s "But Monika, it's almost time to head home."
    show sayori 1b at t42 zorder 3
    show monika 2d at f41 zorder 4
    m "It is?"
    m 2n "Oh gosh, I didn't think we took {i}that{/i} long to grab those supplies."
    m 4l "Well I guess we can just pack up a bit early today."
    m 2b "Just remember that when we return back from the weekend we'll jump right back into writing."
    show yuri at lhide zorder 1
    hide yuri
    show natsuki at lhide zorder 1
    hide natsuki
    show sayori at lhide zorder 1
    hide sayori
    show monika 2j at t11
    "Everyone moved to pack up their belongings and made their way to the door."
    "I took my time fixing my bag as Monika walked around the room for the last time this week, making sure we didn't leave any mess."
    show monika 2a
    mc "Everything all set?"
    m 5a1 "Getting impatient to walk with me [player]? Ahaha~"
    m 2k "We're all set, let's get going then."
    show monika 1j at face with dissolve
    pause .5
    show monika 1a at t11
    "Monika wraps her arms around me in a quick hug before taking my hand and pulling me out the door."
    stop music fadeout 2.0
    show monika at thide
    hide monika
    scene black with 
    dissolve_scene_full

#C4
    scene bg bedroom with open_eyes
    play music t8
    "Lazily opening my eyes I roll over in my bed, reaching out for my phone."
    "After a bit of flailing I finally get a grip on it and bring it over to my face."
    "The time on the overly bright screen reads \"11:56\", and I quickly turn the screen off and let the phone fall to my side."
    "Ahh the weekend, sleep till whenever you want with nothing pressing to do till Monday."
    "I try to roll onto my side and fall back asleep for a bit more to no avail, I was fully awake now whether I wanted to be or not."
    "Sitting up with a huff I grab my phone again, this time taking care to lower the brightness a bit."
    "The notification bar is noticeably lacking a new text message icon and I frown."
    "Why hasn't she... Ohhh right, yeah I forgot she said something about today."
    "I shake my head as I stand up, stretching my arms. Monika had told me on the way home yesterday how she had to go with her mother to some gathering with her mother's co-workers."
    "Monika had sounded less than thrilled, complaining that her mother took her on these trips from time to time and she expected Monika to be engaged with the women there."
    "This usually meant her phone stayed buried within her purse for a good amount of the day, and by the sound of it her sanity too."
    "I cleared out my mobile game notifications one by one, with the last one being a calendar notification of all things."
    "Tapping on it out of curiosity only brought me to an ad about heart shaped sticker packs for the app."
    "I cleared the ad and looked at the calendar behind it, with today's date being shaded in and a red shading covering the 14th only a row away."
    "Oh God, Valentine's day is only a week away and I don't even have a clue of what to do."
    scene bg kitchen 
    with wipeleft_scene
    "I groan into the emptiness of my kitchen at my newfound dilemma."
    "It's like Christmas all over again, scrambling to figure out what I should do."
    "I grab a box of cereal and pour myself a bowl, hoping the food would provide me some energy to work out an answer."
    scene bg livingroom 
    with wipeleft_scene
    "After breakfast I ended up pacing back in fourth in the living room for a while."
    "I had a vague idea of what we should do, maybe a classy dinner in the city, but nothing I could call a plan."
    "What to do, what to do... I can't ask the others for help again, I need to figure this out myself."
    "As the seconds drag by, I could feel the warmth of the sunlight coming in through my windows."
    "The forecast for today was exceptionally well, I probably didn't even need a heavy coat outside today."
    "Hmm, maybe I should enjoy the sunlight a little bit today. If Monika was here she would definitely find a way to drag me outside anyway."
    "I make my way back upstairs to put on something more than lounging pants."
    scene bg residential_day 
    with wipeleft_scene
    "As I stepped outside the cool but comfortable air wrapped around my body as I looked up and down the street."
    "Maybe I should take a walk or something, stretch my legs and think a little as I go."
    "I lock the door behind me and make my way down to the sidewalk."
    "By instinct I find myself starting to walk towards school, my brain reasoning if I'm outside it must be for school."
    "As I walk my eyes look over to Sayori's place and I pause for a moment."
    "Maybe Sayori could help me figure something out..."
    #--TESTING, DELETE THIS BEFORE THE RELEASE----------
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause(.25)
    hide screen tear
    show noise zorder 4:
        alpha (1.0)
    menu:
        "shoppingval=1":
            $ shoppingval = 1
        "shoppingval=0":
            $ shoppingval = 0
    hide noise
    scene bg residential_day
    #----------------------------------------------------
    if shoppingval == 1:
        "No, she already helped me pick Monika's gift for Christmas. I shouldn't need to bother her again."
        "I need to figure this out myself and make it me and Monika's day, not someone's else's day."
    else:
        "Though, she didn't seem to want to help me last time..."
        "Maybe she wants to stay out of stuff like that?"
        "I'd rather not try and force her if she doesn't want to be involved."
    "I continue past Sayori's place and down the road some more."
    scene bg h_residential 
    with wipeleft_scene
    "As I continued on my walk, an idea started to form in my head."
    "Maybe while I'm out here I can check out some restaurants and other places to take Monika."
    "It was the perfect opportunity, with her away and occupied I could get some ideas without her snooping in."
    "Yeah, this is perfect! I can do this!"
    "I check my phone and see the time reads \"12:47\", still plenty of time in the day."
    "My new priority was trying to find a bus stop I could use to hitch a ride into the city center."
    "I know there was at least one on the way to school, where was it..."
    "Ah, there it is, and there's a bus just pulling up!"
    "I quickly dash over and hop onto the bus destined for downtown, ready to start my real mission for today."
    scene bg downtown_1 with 
    dissolve_scene_full
    "I finally stepped off the bus at the downtown terminal and found myself in awe looking around."
    "It seemed the whole city was alive, with people bustling on the sidewalks and cars packed on the roads."
    "All it takes is a warm day to get people outside after being cooped up all winter, and I guess I'm guilty of it too."
    "I start to make my way into the crowd and towards the downtown shopping and dining district."
    "If I was going to find a perfect place for Valentine's day, it was going to be there."
    "As I walked however, the thought of going a little off course popped into my mind."
    "Maybe straight into the center of downtown first wasn't the only option, maybe I could snoop around the outskirts before going into the super busy center."
    "I still had a whole day to look around, but I have to start somewhere."
    menu:
        "Just where to go first?"
        "Stay the course to downtown":
            "Nah, I'll check the main dining district first. The places there must be some of the best if they're still standing downtown."
            "I stick with the crowd moving towards the towering skyline of the city."
            $ e2c4 = 1
            jump downtown
        "Deviate towards the outskirts":
            "Yeah, maybe I'll find a small gem of a venue just out of the prying eye of everyone else."
            "I make my way out of the crowd and start walking toward the edge of downtown."
            $ e2c4 = 1
            jump outskirts
    label downtown:
        scene bg downtown_2 
        with wipeleft_scene
        "The crowds seemed to get even worse as I got closer to downtown, with people walking almost shoulder to shoulder."
        "I try and keep my head above the crowd, looking for any restaurant that catches my eye."
        "Most of the store fronts along the walk were covered in hearts and advertisements for candies and flowers."
        "I make a mental note that I will actually need to pick some of those up for Monika between now and next week."
        "With more walking around downtown I spot a rather large building front draped in pink and red tinsel that draws my eyes."
        "As I move closer to the building the sign finally comes in sight, {i}The Sapphire Star.{/i}"
        "It was quite the restaurant, a dining area surrounded by large aquariums with a local menu everyone praised."
        "I remember going once with my parents for a special occasion and being completely in awe."
        "As I stepped closer to the front door I spotted a notice board standing in the sidewalk with a few pink and red balloons tied to it."
        "On the little board it read: {i}\"Young Couples Welcome! Special Student Discounts for Reservations on Valentine's Day!\"{/i}"
        "That's right! All the kids back at school talk about this place around this time of year!"
        "It was always the go to place to bring your girlfriend here for a date, and they had this special event for every Valentine's day as far as I could remember people talking about."
        "If it was going to be any place downtown, it had to be here."
        "I pull out my phone and write down the store's reservation phone number for later."
        if e2c4 == 1:
            "Still, I haven't looked around the whole area. Maybe I can find something out on the edge of downtown."
            "I take a turn at the next crosswalk and start to make my way towards the edge of downtown."
            $ e2c4 += 1
            jump outskirts
        elif e2c4 == 2:
            "I think I've got two solid contenders here, I'll just have to pick between them."
            "Checking the time again reads \"16:47\", time really does fly when you're having fun."
            "I should probably head back home, I am starving."
            jump e2c4join

    label outskirts:
        scene bg downtown_3 
        with wipeleft_scene
        "The crowds seemed to thin out the farther I went from the city center thankfully, but less and less stores seemed to pop up as I walked along."
        "Maybe coming out here wasn't such a good idea anyway, it's all just offices here..."
        "Eventually however, one smaller building caught my eye as I walked."
        "It sat just at the corner of an intersection, standing out against the array of office buildings around it."
        "It was a short and small building compared to it's towering neighbors, and was currently billowing out smoke from a small chimney."
        "I walked toward the door and a sign hung above it read: {i}\"The Lucchini's Family Restaurant est. 1956\"{/i}"
        "The name sounded foriegn to me, though I couldn't place where from."
        "I took a peak through the window and found most of the tables full, with waitresses running back and forth carrying fresh food to the tables."
        "It seemed like a nice place, and a full restaurant means the food there must be good."
        "I spot a telephone number on the door labeled for reservations and write it down in my phone."
        "Satisfied, I step back onto the sidewalk."
        if e2c4 == 1:
            "Even with this place being a good contender, I should check downtown to see all the big fancy restaurants."
            "Looking to the high rises, I make my way downtown."
            $ e2c4 += 1
            jump downtown
        elif e2c4 == 2:
            "These two seemed like the best options for next week, so I think I'll call this a mission success."
            "Checking the time again reads \"13:47\", time really does fly when you're having fun."
            "I should probably head back home, my stomach is already growling for something to eat."
            jump e2c4join

    label e2c4join:
        scene bg downtown_1 
        with wipeleft_scene
        "On the way back to the bus terminal, I took a swig from a soda I grabbed out of a vending machine."
        "I'd say today was pretty successful, I found two really promising places to take Monika next week without any help!"
        "I knew you could do it, me. This drink is well deserved."
        "But the real question is which one do I take her to?"
        "They both seemed like great venues, but I can only take her to one."
        "I stare into the sidewalk as I make my way back and think long and hard."
        menu:
            "Where am I going to take her for Valentine's Day?!"
            "The Sapphire Star":
                $ c4_1 = 1
                $ c4_2 = 0
                "Of course, everyone brings their date to the Sapphire Star for Valentine's Day."
                "If the word on the street is anything to go by, its a surefire way to impress your partner."
                "And boy would I look like a bad partner if I didn't impress Monika on our first Valentine's day."
            "Lucchini's Family Restaurant":
                $ c4_2 = 1
                $ c4_1 = 0
                "Even though it's not a big place, that restaurant did seem like a good place to eat."
                "It also won't be packed with kids like the Sapphire Star would be."
                "I'm sure Monika would love it there, I just know it."
        "Satisfied with my choice, I smile to myself and walk with a bit more energy."
        "My pocket vibrates a bit as I reach the terminal and I reach inside it."
        "One new message sat across my lock screen;"
        m "{i}Hi [player]! Sorry I couldnt talk to u all day, I was sooo bored -_-{/i}"
        "I chuckled to myself as I read her message and type my response."
        mc "{i}I cant imagine lol, are u home now?{/i}"
        m "{i}Yup! But its kinda boring here too{/i}"
        mc "{i}Aww, well maybe when I get home we can video call?{/i}"
        m "{i}Ur not home [player]? Thats a new one lol!{/i}"
        mc "{i}Very funny, I go outside 2 u know{/i}"
        m "{i}So why wont you when I ask huh?!?{/i}"
        "I groan internally as I board a bus on my route home."
        mc "{i}Because u make me run around and stuff, I just went on a long walk downtown{/i}"
        m "{i}Wow, that is a long walk! Why downtown though?{/i}"
        mc "{i}Idk, felt like it ig{/i}"
        "I'd rather not say I was looking for a place for us to go on the big day, it would completely ruin the surprise."
        m "{i}Mhmmm, did u get me a gift?!{/i}"
        mc "{i}Nooope{/i}"
        m "{i}Awww ur so mean!!{/i}"
        m "{i}Im gonna find out y u were over there today, mark my words!{/i}"
        mc "{i}I already told u, I went for a walk!{/i}"
        "I sink into my seat as sigh, she's onto me again for sure."
        scene bg h_residential_sunset 
        with dissolve_scene_full
        "The long bus ride finally ended and I started to make my way back toward my house."
        "Monika's texts had stopped coming in by the last leg of the bus ride, leaving me confused."
        "I mean her phone may have died on her, but she would have said something about it right?"
        "It isn't like her to just randomly stop texting me out of the blue..."
        "I shake my head and start walking with a bit more speed, I'll just call her when I get home."
    
    #C5
        scene bg residential_sunset 
        with wipeleft_scene
        "One last turn down and the familiar view of my street came into sight."
        "Just a bit more and I can finally sit down and rest my legs for good and have some dinner."
        "What to make though... maybe just some instant ramen, I'm too tired for anything else."
        "As I walk up to the door I imagine the taste of noodles on my tongue as I reach out for the door."
        "Ah wait, I need my ke-{w=1.5}{nw}"
        "I stop and notice the door is slightly ajar."
        stop music fadeout 10.0
        "{i}That's impossible, I'm positive I locked the door when I left earlier!{/i}"
        "Did I just not close the door all the way when I left? Did someone break in while I was gone?!"
        "The ideas raced through my mind as I slowly edged the door open and looked into the house."
        "Nothing seemed out of place from here except maybe the shoes near the door being a bit messed up."
        "Someone was definitely here, I could feel it."
        play music hb
        "I slowly made my way into the doorway, listening to anything that may be a person."
        "My heart felt like it was beating out of my chest, each beat being harder than the last."
        "A noise from the living room made me almost jump, like someone had turned on the television."
        "I looked around and found my wiffle ball bat propped up near the door."
        "I took it in my hand and said a long prayer to whatever deity wanted to listen before I lunged into the living room."
        stop music
        scene bg livingroom_sunset 
        with wipeleft_scene
        mc "YOU PICKED THE WRONG HOUSE FOOL!"
        show monika 1bd at t11#PLACEHOLDER FOR SPOOKED MONIKA SPRITE!!
        m "[player]! I-It's me, Monika!! Relax!!"
        show monika 1bc at s11 #PLACEHOLDER
        mc "M-Monika?"
        "I stood in awe holding my bat up ready to strike."
        "Monika had managed to jump behind the couch looking just as terrified as I had felt seeing the door opened."
        mc "B-but, how did you get here? How'd you even get inside?!"
        m 3bn "You told me about your extra key remember?! Inside the flap of the door mat!"
        show monika 1be at t11
        stop music fadeout 2.0
        mc "I did?"
        "My memory starts to form itself together and I recall telling Monika off hand about the emergency key my family had just in case we locked ourselves out of the house."
        mc "I... guess I did huh..."
        play music t6
        "I start to chuckle to myself. Between the last 30 seconds of stress and realization my mind had seemed to just stop."
        show monika 1bl at face 
        with dissolve
        "Monika steps over to me joining in my fit of laughter and wraps me in a big hug."
        m 1bn "I probably shouldn't have just barged in without telling you, I'm really sorry for scaring you like that."
        show monika 1be
        mc "It's.. okay I guess, at least it's you and not some burglar."
        show monika 1bl
        "I drop the plastic bat and wrap my arms around Monika, the both of us breaking into a fit of relieving laughter."
        show monika 1bm at t11
        mc "So why {i}did{/i} you come here after all?"
        show monika at s11
        "I motioned Monika over to the couch and we both took a seat across from one another."
        m 3bn "Well I just..."
        m 1bl "I don't know, I was just so bored of today I wanted to get out of the house."
        m 1bn "The first thing I thought of to do was see you [player], and I figured I would just meet you here as a surprise."
        m 2bl "I didn't expect to beat you here though, or scare you like that!"
        m 1be1 "I'm sorry I just let myself in, I should have asked you beforehand."
        show monika 1be
        mc "It's fine, really, but yeah a little heads up would have been nice."
        "I lay down into the couch with a sigh of relief, finally a moment to relax."
        show monika 1bc
        mc "So how was your day with your mom?"
        m 2br "Oh my gosh it was so boring, you don't even know."
        m 1bn "How can a bunch of middle aged women just go on and on about their office job? I seriously don't get it!"
        m 4bi "And of course Mom is all \"Monika, get off your phone and join the conversation.\", like, what am I going to add to your gossip?"
        m 2br "I just don't get why she insists on me going to her stupid work lunchings."
        show monika 2bq
        mc "Maybe it's so you can network or whatever they call it in school. Get to know people in the workforce you can call on for help later."
        m 1bn "I guess, but what networking could I do with a bunch of secretaries that all work in the same department of the same company."
        m 1bp "I'll probably just end up working in the same place they are anyway, so why go through all this trouble."
        show monika 1bm
        mc "Not if you don't want to, you could basically do anything you want with your grades."
        m 2bl "I guess you're right, ahaha~"
        m 2bn "I think my parents just see me following their footsteps and doing the same stuff they do."
        show monika 1be
        mc "But they shouldn't make that choice for you, it should be you who decides what you do for a living."
        m 2be1 "I know that, I just have to find something I want to do with myself I suppose."
        m 4bl "But enough about me, what did {i}you{/i} do today, [player]?"
        show monika 2ba
        mc "I told you, I went for a long walk through downtown today."
        m 2bb "I just can't believe you went all by yourself!"
        m 2bl "I didn't even have to drag you out! Ahaha~"
        show monika 2bj
        mc "Well I had my reasons, and I'd say it was a good day."
        m 1bb "Oh? Was it for me by any chance?"
        show monika 1ba
        mc "It might have been, maybe it was just for me, who knows..."
        m 2br "Oh really?"
        m 1bh2 "Well, I bet I could get you to tell me!"#CUSTOM H WITH B MOUTH HERE
        show monika 1bh1 #CUSTOM WITH SMILE
        mc "And how will yo-{w=1.0}{nw}"
        play sound fall
        show monika 1bj at face 
        with dissolve
        "All the wind was almost knocked out of me as Monika jumped from her seat and onto my chest, wrapping her arms around me and locking me down."
        m 1bk "You better tell me right now or else I'm not letting go!"
        show monika 1bj
        mc "I can't say, it's a secret!"
        show monika 1bk
        "I tried to move Monika off of me but it was no use."
        "The long walk had drained me of all my energy and I was running on empty."
        "Monika also seemed to double down on her grip, giggling as she locking her arms behind my back so I couldn't move them."
        show monika 1bj
        mc "Monika, please!"
        m 1bk "I don't hear you telling me what you did~!"
        show monika 1bj
        "Against my better judgement I struggled against her once again to no avail."
        "This time however Monika brought her hips up and sat right on top of mine, using her legs to lock her in place."
        show monika 1be
        "As I felt her rubbing against me I stopped resisting and looked up at her."
        mc "M-Monika.."
        show monika 1bj
        scene black 
        with close_eyes
        "Monika closes the gap with me and plants her lips on mine."
        "I slowly eased into the kiss and wrapped my arms around Monika, engulfing myself in her warmth."
        "Everything seemed to fade away in that instance, all that remained was this kiss with Monika."
        "It was just what I needed after a long day."
        "My trance was broken however when I felt Monika start to pull away from me."
        scene bg livingroom_sunset 
        with open_eyes
        show monika 1be1 at face 
        with dissolve
        m "You know, it's not nice to poke down there.."
        show monika 1be
        "Monika moves one of her hands from behind my back and rests it just above my waist."
        mc "O-oh, uh..."
        m 1bl "Don't be so ashamed of it, ahaha~"
        m 1be1 "Just relax..."
        show monika 1be
        "Monika starts to shift herself lower, rubbing against my legs and waist."
        "I really can't do something like this right now, my body was aching and my eyelids felt like lead weights."
        show monika 1bc
        mc "W-Wait Monika..."
        m 1bd "Hmm, what is it [player]?"
        show monika 1bc
        mc "Can we just..."
        show monika 1bd
        "I sigh and pull Monika in tight against me as best I can."
        mc "Can we just stay like this and maybe take a nap?"
        show monika 1be
        mc "I'm just... super sleepy right now..."
        m 1bl "I've almost never heard of someone saying no to something like this [player], ahaha~"
        m 1be1 "But of course we can, if that's what you really want."
        show monika 1bj
        "Monika snuggles up against me once again, wrapping her arms around me."
        "It wasn't long before the warmth of her against me started to seep in again and my body began to relax."
        scene black 
        with close_eyes
        "I felt bad cutting Monika off like that, but I just didn't have the strength in me to do something like that right now."
        "My legs were aching and my eyes wouldn't open anymore."
        "I'm glad she didn't take it personally, I don't think I would have been able to forgive myself."
        "She's just too perfect sometimes..."
        "A smile creeped over my face as I started to drift into unconsciousness."
        "So..perfect..."
        stop music fadeout 2.0
        scene black 
        with dissolve_scene_full
        scene bg livingroom_night 
        with open_eyes
        "After what seemed like only a moment I lazily opened my eyes."
        "Why was I in the living room..."
        "Oh right, nap..."
        "But why is it so dark, and where's Monika?"
        "She wasn't still on top of me, and she wasn't anywhere around the living room."
        mc "Monika?"
        "As I sat up and rubbed my eyes, a piece of paper on the coffee table caught my attention."
        call showpoem (poem_m6, revert_music=True, where=truecenter)
        stop music fadeout 30.0
        play music t5
        "Damn, I'm surprised I didn't hear or even feel her getting up and leaving."
        "I check the time on my phone and see its well into the night, which means she's probably asleep by now for tomorrow."
        "My stomach growls at me and I feel a wave of hunger wash over me."
        "Sleeping on an empty stomach isn't comfortable, duely noted."
        "I fire up the television and my console down here and make my way over to the kitchen for something quick to eat."
        "I guess I can play something and hope I fall back asleep soon."
        "As I take a seat back on the couch I find myself taking Monika's note into my hand again."
        "It's just a simple note, a small message on a scrap piece of paper but I feel oddly drawn to it."
        "Maybe it's because she wrote it that I want to save it, is that a weird thing to do though?"
        "I read it once again and decide to pocket the note, unable to part with it."

#C6
        stop music fadeout 2.0
        scene bg bedroom 
        with dissolve_scene_full
        play music t2
        "By some miracle I managed to get some more sleep in before morning came, recovering most of my energy from yesterday."
        "I stretched my arms and legs as I got dressed for the day, noting the slight ache in my legs."
        "If that walk is still messing with me, I must be really out of shape..."
        "I shrug to myself and head downstairs for something to eat."
        scene bg kitchen 
        with wipeleft_scene
        "I took the easy route for breakfast and threw some eggs in boiling water and toast in the toaster."
        "Knowing Monika, she's probably already on her way over."
        "With some butter spread on the toast, I gingerly take the hot eggs out of the water."
        "I bring my small meal over to the table and take a seat, my joints rejoicing at the small break."
        "I quickly down the toast and get the shells off of the eggs before I hear a knock at the door."
        "Damn she's quick, I'm not even done eating yet."
        "Taking one egg in my hand, I move over to the door."
        scene bg livingroom w
        ith wipeleft_scene
        mc "I'm coming, hold on!"
        "I plop the egg in my mouth and unlock the door, opening it wide open."
        show monika 2bk at l11 zorder 3
        m "Hi [player]! How are you feeling?"
        show monika 1bd
        mc "Jubs breab!"
        "I swallow the egg in my throat and wipe my mouth off."
        show monika 2be
        mc "That nap really helped me recharge from yesterday."
        m 4bn "I'm glad to hear that, but swallow your food next time!"
        m 2bl "I can wait while you finish what's in your mouth, ahaha!"
        show monika 2be
        mc "Sorry, you caught me in the middle of breakfast."
        m 3bl "But [player], its almost noon."
        show monika 1be
        mc "And it's the weekend! It's how you enjoy the end of the week."
        m 2be1 "What am I ever going to do with you [player]?"
        show monika 2be
        mc "That is completely up to you, Monika."
        show monika 1ba at s11
        "I motion Monika over to the couch and she makes her way over and sits down."
        m 3bb "So what's the plan for today, [player]?"
        show monika 1ba
        mc "Well I uh..."
        show monika 1bc
        mc "I didn't really come up with anything to do today, I was still getting myself together when you knocked on the door."
        m 2bl "Oh dear, I'm sorry [player]. I didn't mean to mess up your routine this bad."
        show monika 1be
        mc "It's fine, really, I didn't mean to sleep this far into a Sunday anyway."
        show monika 1bc
        mc "But since I don't have a plan, maybe you can have the choice for today."
        m 1bd "Are you sure, I picked last week so it's only fair that you pick today."
        show monika 1bc
        mc "I'm sure, I didn't have any good ideas anyway."
        "I was just gonna suggest staying home and watching some anime or playing games but I know Monika would have most likely pushed for something else anyway."
        "Might as well give her the choice and save myself the trouble."
        m 3bn "Well in that case..."
        m 3be1 "Maybe we could go into downtown and do a little shopping?"
        m 2bb "I heard there's a couple big places doing some really great deals on new outfits for the summer!"
        show monika 1ba
        mc "Well..."
        "I could feel my legs screaming at me, \"No God please don't make us do that again!\", but the way Monika beamed up at me made me realize I couldn't refuse her request."
        mc "..Sure, why not. Could always use more fresh air."
        m 1bk "You mean it, yay!"
        show monika 2bb at t11
        m "Let's go right now, before all the good stuff is gone!"
        show monika 2ba
        "Monika jumped right to her feet and started to get herself ready to leave."
        mc "Alright, let me just grab the last of my breakfast."
        "My limbs groaned in retaliation but I forced them along with me to the kitchen."
        scene bg residential_day 
        with wipeleft_scene
        "I stepped out of the door into the cool midday air with the last egg in my mouth."
        show monika 1bj at l11
        play sound closet_close
        "Monika stepped out from behind me and I closed the door behind her, being sure to lock it again."
        m 4bb "So what do you think I should get? Maybe some new skirts or maybe a flashy new bow in a spring color?"
        m 1bk "Come on, we gotta get there now!"
        show monika 1bj
        mc "Monika, wait a little!"
        show monika at lhide zorder 1
        hide monika
        "My cry fell on deaf ears however, as Monika took my hand and started making her way to the bus stop."
        "I tried to keep pace with her as she seemingly ran along the sidewalk as best I could."
        "My legs wanted to fall off but I grimmised through the slight agony."
        scene bg h_residential 
        with wipeleft_scene
        show monika 1bj at l11
        "After what seemed like forever we finally made it to the bus stop."
        "I took this moment to rest and plopped down onto the closest bench."
        m 2bd "[player], are you tired all ready?"
        show monika 2bc
        mc "No no, just fine, just.. resting my legs for the city."
        m 2be1 "Okay, but don't hesitate to tell me if you need a break along the way."
        m 4be1 "Promise?"
        show monika 2be
        mc "I promise I'll tell you."
        show monika 1bj at s11
        "Monika sits down next to me while we wait for the next bus."
        "Even if she would want me to say I needed to rest, I don't want to look that pathetic to her."
        "It's just a simple walk, I shouldn't be an old man about it."
        "Soon enough a bus came around the corner and rolled up to our stop, opening its doors for us."
        show monika 1bb at t11
        m "Come on [player], let's get going!"
        scene bg downtown_1 
        with wipeleft_scene
        "The bus ride downtown was a lot more enjoyable than the one from yesterday."
        "Mostly because I had Monika sitting next to me through the whole trip, but also it wasn't as cramped as yesterday."
        show monika 2bb at l11 zorder 1
        m "Come on [player], the shop is this way!"
        show monika 1bj
        "Monika immediately grabbed my hand and started making her way into the downtown area, dragging me along with her."
        "The crowds today were also less cramped on the sidewalk, allowing Monika to slip through them with me in tow."
        m 1bk "Isn't it so nice out today, [player]! Sun shining, the streets full of people."
        show monika 1ba
        mc "Yeah, nice change of pace from the snow and cold."
        m 3bb "Absolutely, and soon I can finally start to use my summer fashion!"
        m 1bl "It's been too long since I could wear any of it."
        m 1bk "And this new stuff will make my selection even better! Ahaha~"
        m 3bb "This way, we'll reach the place faster if we turn over here."
        scene bg downtown_2 
        with wipeleft_scene
        show monika 1ba at l11
        "Monika guided me through the city streets and we reached the center of downtown for my second time this weekend."
        "Compared to yesterday there was far fewer people than before, making navigation the strip a breeze."
        m 3bb "Ah, we're here!"
        show monika 2ba
        "Monika stopped us in front of a large outlet store, signs all along the storefront boasting of the great deals behind the door."
        m 1bk "Come on, let's see what they got!"
        scene bg clothingstore 
        with wipeleft_scene
        show monika 1bd at l11
        "We stepped into the store and Monika stopped and gazed around the sales floor, her mouth wide open."
        show monika 1bc at h11
        mc "Overwhelmed a bit?"
        m 2bn "No no, just thinking of what to look at first..."
        m 2be1 "There's just so much I could get here."
        show monika 2bc
        mc "Well how about we check out the summer stuff like you wanted to, then we can go from there?"
        m 4bb "Alright, we'll do that!"
        m 1bk "It's this way, come on!"
        show monika 1bj
        "Monika took my arm and started toward the section under a large sign saying:\"Women's Summer Wardrobe\"."
        "I tried to keep a smile on my face as we walked, but I had a bad feeling about this."
        scene bg clothingstore 
        with wipeleft_scene
        "After what felt like an eternity Monika had worked her way through most of the clothing she picked out and took them over to the fitting booths."
        "She sat me just outside of it while she tried each outfit, claiming I wasn't getting any free shows."
        "\"Well, at least today~\" she said before she jumped into the booth giggling."
        "As much as I jokingly protested with her, my legs rejoiced at a chance to sit down."
        "I almost decided to rest my eyes as well before Monika piped up from the other side of the door."
        m "Okay [player], I think this is the last one!"
        m "Are you ready?"
        mc "Ready as I'll ever be."
        show monika 2ce at l11
        "Monika stepped out of the booth and my eyes widened in amazement."
        show monika 2cm
        "The tank top and jean shorts she picked out looked even better than I had expected them to."
        "It was all so mesmerizing."
        m 2cn "[player], it's not nice to stare you know."
        show monika 2cm
        mc "O-Oh, I'm sorry! I just..."
        show monika 2ce
        mc "I really like the outfit."
        m 2ck "I'm really glad, I was hoping you would like this one in particular."
        m 5cb "I picked it just for you, ahaha~"
        show monika 1cj
        mc "I'd say you hit the nail right on the head."
        "I give her a wide smile and become painfully aware that I'm blushing a beet red."
        m 2cb "Well, I'll change back into my clothes and we'll pay for this."
        m 4ck "Give me one second!"
        show monika 1cj at lhide zorder 1
        hide monika
        "Monika jumped back into the booth and I leaned back into the bench and smiled."
        "Who would've thought I'd ever be sitting in a fitting room, waiting for a girl like Monika."
        "I try to shake my blush and grin off before Monika finishes changing."
        show monika 2bk at l11
        m "Okay, I'm ready [player]!"
        m 3be1 "Are you sure you don't want to shop for yourself before we go?"
        m 4bb "I'm sure we could find something really cute for you!"
        show monika 2bm
        mc "I'm sure, we've been here for so long now!"
        m 2bl "Alright, alright, I get it."
        m 2bn "We should probably get out of here before I find something else I want anyway."
        scene bg downtown_2 
        with wipeleft_scene
        show monika 1ba at t11
        "We checked out Monika's things and we stepped back onto the sidewalk."
        m 1bb "So where to now, [player]?"
        show monika 1ba
        mc "Hmm? What do mean, I though you were picking today."
        m 1bk "But we did what I wanted to do today, now it's your turn to pick!"
        show monika 1bj
        mc "Well..."
        "I quickly went through my memory of the area from yesterday to think of something to do."
        "Soon enough a lightbulb went off."
        show monika 1ba
        mc "I know of a park that's kinda close by, we could go there for a bit."
        m 3bb "That sounds great, let's head there now!"
        show monika 1ba
        mc "Perfect, it's this way if I remember.."
        show monika 1bj at t11
        "I started to make my way towards the path I took yesterday to regain my bearings."
        "Monika wrapped her arm around mine as she held onto her bags of goodies and walked beside me."
        "The crisp winter air filled our lungs as we made our way through downtown, the noise of a busy city ringing all around."
        m 3bd "Hey, [player] look!"
        show monika 3bc
        mc "Hmm?"
        show monika 3ba
        "Monika pointed across the street and I turned to look at what it was."
        "As I turned I gasped to see the front of a very familiar place for the second time this weekend."
        m 1bb "That's The Sapphire Star!"
        m 1bk "Almost {i}everyone{/i} at school takes their partner to for Valentine's Day!"
        m "I've heard so many stories from my friends about it that I've always wanted to go."
        show monika 1bj
        mc "Ah, yeah.. I've heard a lot about it too I guess..."
        if c4_1 == 1:
            "Yes! I knew I chose the right place!"
        else:
            "Crap! I knew this place was a better choice than that stupid little restraunt!"
        m 1bn "But you know, while I say all that..."
        m 1bp "I don't really know who we'd run into if we went..."
        show monika 1bo
        mc "What do you mean?"
        m 1bg "Well, remember what Veronica and Rachel said to us when we saw them?"
        show monika 1bf
        mc "Veronica and Rachel...Oh right, them..."
        m 1bg "What if there's other students there and they say stuff like that to us?"
        m 1br "It would just ruin the whole night..."
        show monika 1bq
        "We keep walking for a distance in silence, Monika with closed eyes and a scowl across her face."
        if c4_1 == 1:
            "Welp, maybe The Sapphire Star isn't the best place to take her then..."
        else:
            "With that risk, maybe Lucchini's isn't such a bad pick after all..."
        m 1bn "Let's not think about the bad what-if's though, let's just enjoy each other today, ahaha~"
        show monika 1be
        mc "Right, we shouldn't spoil the day like that."
        show monika 1bj
        "With that I lead Monika onward toward the park."
        scene bg downtown_3 
        with wipeleft_scene
        show monika 1bj at t11
        "Following my footsteps from the restaurant made the trip a whole lot easier."
        m 1bd "You sure seem to know this area well [player]."
        show monika 1be
        mc "Oh yeah, well I.. just remember it from a while back is all."
        m 3bl "A while back huh? Are you sure it wasn't a more recent memory?"
        show monika 1bj
        mc "W-well I didn't go down here yesterday per say. I went another direction."
        "Monika just giggles as I fumble through an excuse and we reach a familiar crossroads."
        m 3bb "[player], look!"
        show monika 3ba
        "Monika points toward a small brick building that immediately sparks my memory."
        m 1bk "That is such a cute little restaurant oh my gosh!"
        m 1bb "Can we go take a quick look at it [player], please?"
        show monika 1ba
        mc "Of course, I don't see why not."
        if c4_2 == 1:
            "Though it is ruining a bit of the surprise..."
        else:
            "It's not the Sapphire though, so I doubt it'll be that impressive to her."
        "We crossed the road over to the small building and Monika was completely enamored with the exterior of the building."
        m 1bd "It's so different than any place I've ever been to."
        m 3bb "Can we go inside [player]? I mean, it is kinda getting near dinner time and all so maybe-"
        show monika 1bc
        mc "Well maybe some other time, we should get to the park before you have to go home and we miss out on a great day!"
        m 1bn "Okay okay, we should get going then."
        show monika 1be
        "I take Monika's arm and guide her to the sidewalk once again."
        if c4_2 == 1:
            "I internally sigh in relief, I didn't want to ruin the allure of the place early by accident."
        else:
            "Even if I wasn't originally planning to take her there for the big day, it's a nice backup for a dinner date another day."
        "I make a turn away from the restaurant and down the street."
        "As we walked I started to think about everything Monika said."
        "She thought both of the places were nice, but that doesn't help me at all!"
        "But I need to make a desision on this, I can't wait on it forever..."
        menu:
            "Ahh, what to do..."
            "The Sapphire Star":
                "Of course, she really wanted to go there."
                "It would make the night an unforgettable memory for both of us."
                "I can figure out the people thing there, I'm sure it wouldn't be that bad anyway."
                $ dinnervar = 1
            "Lucchini's Family Restraunt":
                "She really did seem to like the place, so maybe it isn't such a bad idea."
                "Someplace peaceful and away from all the other students that could ruin the night."
                "Yeah, that sounds like a wonderful night."
                $ dinnervar = 0
        "With my desision made, I could walk with a bit more confidence."

#C7
        scene bg park 
        with wipeleft_scene
        show monika 1ba at l11
        "Soon enough we finally reached the city park and I looked up and sighed."
        mc "We made it, finally."
        m 3bn "Finally tired [player]? I'm actually quite impressed you made it this far!"
        show monika 1bm
        mc "Hey, what's that supposed to mean!"
        m 2bl "Nothing, nothing!"
        m 2be1 "I'm just glad to see you out and about instead of cooped up in your house all day."
        show monika 2be
        "As much as I would've liked to stay home at this point, making her happy was worth the bit of suffering."
        show monika 1bd
        "I looked over to see Monika staring off into the distance with a look of surprise."
        mc "Monika? What are you-"
        m 3bb "[player] look over there!"
        m 3bk "It's a lemonade stand!"
        show monika 3bj
        "Sure enough, following Monika's finger my eyes landed on a small table in the middle of the park surrounded by a group of adults and small children."
        "Lemonade? In the middle of winter?"
        m 1bb "Come on, let's get some!"
        show monika 1ba
        "Monika quickly grabs my hand and starts to make her way over."
        #show monika at lhide zorder 1
        #hide monika
        #mc "Monika wait!"
        #scene bg park with wipeleft_scene
        #show monika 1ba at l11
        "As we approached the table the scene started to come into better focus."
        "Signs stood all around and were emblazoned with one of the city's youth scout group's emblem and motto"
        "It seems they were using the profits from the stand to help fund summer plans the group had."
        "Talk about fundraising early, I would have never guessed they'd take this aproach."
        "Looking toward the table I could see a group of children no older than ten dressed up in their scouting uniforms working the table and drinks while a few adults supervised and helped where they could."
        m 2be1 "Oh my gosh, this is so adorable, my heart can't take it [player]."
        m 2bb "Let's get in line to buy some!"
        show monika 1ba
        "We took our place in line and looked to the large menu sign they had for drinks."
        m 1bd "Wow, they sure do have a pretty decent selection for a lemonade stand."
        show monika 1bc
        mc "Guess that shows how much planning went into this."
        m 2bn "Yeah, they do like to make you plan in youth scouts."
        m 2bb "Have I ever told you about when I was a Daisy Scout [player]?"
        show monika 2ba
        mc "Actually no, I don't think you have."
        m 2bk "Oh it was so much fun! I remember all the fun trips we'd take out of the city."
        m 1bb "Hiking and camping with your friends, learning about the outdoors..."
        m 2br "But school started to get in the way so I had to drop it before I could become a Rose Scout."
        m 2bn "I wish I could go back in time a bit, it was so much easier back then."
        show monika 1be
        mc "Well, if you went back in time you wouldn't have me with you though."
        m 4be1 "Your right, I'd probably be lost without you."
        show monika 2bc
        mc "Though, I bet you looked super adorable in a Daisy Scout uniform."
        m 2bl "No, I looked super goofy back then! I can't stand looking at old pictures of me."
        show monika 2bm
        mc "Come on, I doubt it was {i}that{/i} bad!"
        m 2bn "Maybe I'll show them to you one day, but only if you promise not to laugh at them."
        show monika 2be
        mc "I promise, swear it."
        show monika 1bc
        mc "Did you decide on a drink? We're almost up."
        m 2bl "Oh right, yeah I decided!"
        show monika 1ba
        "As the people ahead of us finished we stepped up to the table."
        $ y_name = "Boy Scout"
        $ n_name = "Girl Scout"
        y "Hello! What can I get for you today?"
        mc "Hey bud, can I have an original lemonade for myself and.."
        m 2bb "I'd like to try one of the strawberry lemonades please."
        show monika 2be
        y "Okay! One original and one strawberry please!"
        n "Got it!"
        "One of the girls grabbed two cups and made her way to the rest of the troupe in the back."
        "We could see both kids and adults working hard to squeeze lemons and mix the juices with sugar and water."
        show monika 1ba
        "Soon enough the girl returned over with two full cups with straws."
        n "Here you go! Thank you and enjoy!"
        m 1bk "Thank you!"
        show monika 1bj
        "We took our drinks and started toward some of the benches close by."
        m 3bk "Wow, this stuff is really good!"
        m 1bb "How is yours [player]?"
        show monika 1ba
        mc "Pretty good actually, I'm impressed."
        m 4be1 "Hey, you didn't doubt the scouts did you?"
        m 2bk "I knew they'd make something excellent!"
        show monika 2bj
        mc "I didn't doubt them, I can be suprised can't I?"
        m 2bl "Fine, I guess you could be a little bit surprised."
        m 2bn "They're just so cute, aren't they [player]?"
        show monika 2bm
        mc "Is what so cute, the drinks?"
        m 2bl "No silly, ahaha~"
        m 4be1 "The kids. They all seem so cheerful and happy."
        show monika 2be
        mc "Oh, well uh.. yeah I guess they are kinda cute."
        m 1bn "You know, I'd be lying if I said the thought of kids hasn't crossed my mind a few times."
        show monika 1bm
        mc "O-Oh, well, I mean if we stay together I mean-"
        m 1bi "What do you mean {i}if{/i} we stay together?"
        show monika 1bh
        mc "Huh?"
        "I looked over to Monika and she was staring me down with a deep scowl."
        m 1br "You aren't thinking of leaving me, are you?"
        show monika 1bq
        "What has gotten into her?!"
        mc "No, no I didn't say that at all, I was just..."
        m 4bk "I'm joking [player], relax! Ahaha~"
        m 2bl "Your reaction was just perfect, I couldn't go on with my act."
        m 1bn "Sorry, I couldn't help myself. "
        show monika 2bm
        "She thought it would be funny to just pull that?"
        "Gosh, what did I do to deserve this?"
        mc "Oh, well just don't do that again so suddenly!"
        show monika 1bc
        mc "Wait, is that..."
        show monika 1bd at t21
        show sayori 4bm at t22
        show sayori at h22
        mc "Sayori?!"
        show monika 1bc
        show sayori 1bo at f22
        s "M-Monika? [player]?"
        s 2bl "W-What are you guys doing here?"
        show sayori 2bb at t22
        show monika 1bm
        mc "Well we were just out on the town and we decided to come here and... now we're here."
        show sayori 3bl at f22
        s "Oh, that's... great..."
        show sayori 1bn at t22
        mc "But why are you here Sayori?"
        show sayori 2bl at f22
        s "Well I was just... bored today and I..."
        s 4br "...guess I decided to come out here today! Ehehe~"
        show sayori 2bq at t22
        show monika 3bl at f21
        m "Well that's good of you to come out and enjoy the sunshine."
        show monika 2be at t21
        mc "Yeah, I barely ever see you out and about like this."
        show sayori 3br at f22
        s "Yup, decided to do something different today!"
        s 1bx "So I just walked out the door and jumped on the first bus that came."
        s 2bl "But um, now that I'm here I... don't know what to do."
        show sayori 1by at t22
        "Sayori clutches a cup similar to ours in her hands and looks down into the concrete."
        show monika 4bn at f21
        m "Well we should probably get going anyway, we wouldn't want to be late on the way back."
        m 2bk "Come on [player], let's head back to the bus and-"
        show monika 2bc at t21
        mc "Wait, Monika."
        "Maybe we would be a tad bit late but..."
        menu:
            "Should we really just leave Sayori here?"
            "Yes":
                mc "Uh, yeah, maybe we should head back. It is getting kinda late for you."
                mc "We can catch up at school though Sayori, right?"
                show sayori 3bl at f22
                s "Oh um.. yeah, I'll see you guys back at the club!"
                s 2bs "Have fun!"
                show sayori 1bq at t22
                show monika 1bb at f21
                m "Of course Sayori, we'll see you then!"
                show sayori at thide zorder 1
                hide sayori
                show monika 1bj at t11
                "We turn back towards the closest bus stop and start to make our way over to it."
                mc "Monika?"
                m 1bc "Hmm?"
                mc "You know we could have made it back in time even if we sat with Sayori for a little bit."
                m 3bn "Well maybe, but I didn't want to risk it you know?"
                show monika 1bm
                mc "But we were going to sit in the park anyway weren't we?"
                m 2bl "Maybe, I guess time just flies by when your having fun, ahaha~"
                m 2bk "But I wouldn't have wanted to spend it with anyone other than you [player]!"
                show monika 1bj
                mc "Monika..."
                "What's gotten into her, first the outburst and now ditching Sayori?"
                show monika 2bc
                mc "Next time we're going to be nice to her."
                m 1bp "Okay, okay, I know."
                mc "You say that now..."
                "Monika grips my arm again as we walk but I felt a small pit in my stomach grow ever so slightly."
                "Sorry Sayori, next time I promise."
            "No":
                show sayori 2bn
                show monika 2bd
                mc "Why don't we sit a while, I mean we were going to anyway."
                show sayori 3bl at f22
                show monika 2bq
                s "Oh, I don't want to make you late for anything though!"
                show sayori 3bd at t22
                show monika 1bh
                mc "We'll be fine, trust me."
                show monika 2bm
                show sayori 1bq
                "I look over to Monika with a quick scowl and we all sit down together."
                show sayori 1bb
                mc "You know, you could have just texted me and asked what we were up to. I'm sure we would have found something to do."
                show sayori 2bl at f22
                show monika 1bq
                s "But [player], Sunday is when you and Monika go out together, I wouldn't want to ruin that."
                show sayori 1bg at t22
                show monika 3br at f21
                m "Yes, it is our day and we were doing something-"
                show monika 1bo at t21
                show sayori 1bd
                mc "BUT we could have at least done something small, maybe."
                mc "What about Yuri or Natsuki? What were they up to today?"
                show sayori 2bc at f22
                s "I'm not sure, I didn't even think to ask them..."
                show sayori 1bb at t22
                show monika 1bq
                mc "Well, next time you want to do something let us know! We're all friends here right?"
                show sayori 2bl at f22
                s "Yeah, okay I'll keep that in mind for next time."
                s 2bx "Thank you, [player]."
                show sayori 1by at t22
                mc "Anytime, Sayori."
                show monika 1br at f21
                show sayori 2bn
                m "[player] we need to go, my mom keeps texting me asking where I am."
                "Monika seemed to jump out of her seat and start walking towards the bus stop before turning and looking at me."
                m 1bi "Are you coming or not?"
                show monika 1bh at thide zorder 1
                hide monika
                show sayori 1bb at t11
                "Monika keeps walking just out of earshot and I turn to Sayori."
                s 2bd1 "Go [player], I'll be fine here." #<-- Open Mouth Sayori D expression
                show sayori 1bd
                mc "But-"
                s 4br "No buts, go with her!"
                show sayori 2bq
                "Sayori pushes me towards Monika and giggles."
                mc "Alright, we'll see you tomorrow Sayori!"
                s 2br "Bye!"
                show sayori at thide
                hide sayori
                show monika 1bq at t11
                "I wave to Sayori and rejoin Monika's side. I can't help but notice the huff in her breath."
                mc "Monika..."
                m 1br "What?"
                show monika 1bq
                mc "Your doing it again."
                m 2bi "Doing what again?"
                show monika 2bo
                mc "Glowing green, with envy. She's our friend Monika."
                m 2bp "I know that, I just..."
                m 1bg "I'm sorry. I just wanted to sit in the park alone with you, and got a little upset that it was ruined."
                show monika 1be
                mc "We'll have plenty of time to sit together at the park this spring and summer, don't worry."
                m 2bp "I guess, but I'm just annoyed I have to wait now."
                show monika 1bf
                mc "Come here."
                show monika 1bm at face 
                with dissolve
                "I wrap my arm around Monika and she rests her head against my shoulder while we make our way to the buses back home."
                $ SayoriVar += 1

#C8
        stop music fadeout 2.0
        scene bg class_day 
        with dissolve_scene_full
        play music t3
        "The next day while I sat in homeroom, I got a text from Monika."
        m "{i}I cant make it in today, my neck is killing meee{/i}"
        mc "{i}Oh no, did something happen?!{/i}"
        m "{i}No, I just slept wrong and now its sore -_-{/i}"
        m "{i}I told Sayori to watch the club today, so there's no excuse to skip!!{/i}"
        mc "{i}I wont I wont, I promise{/i}"
        mc "{i}Don't have too much fun today, luv u{/i}"
        m "{i}Yeah yeah, love u too [player]~<3{/i}"
        "I couldn't help but smile as I read her text and slipped my phone into my pocket as the teacher stepped up to the front of the classroom."
        "Guess today will be a bit of a dull day without seeing Monika to look forward to."
        scene bg corridor 
        with wipeleft_scene
        "Class after class went by but I couldn't be bothered to pay attention to any of them."
        "Without Monika to keep me in check, my mind could only focus on the prospect of the lunch sitting in my bag."
        "Soon enough though my prayers were answered and chow time was upon us."
        "As I hastily made my way toward the cafeteria, a realization came to mind."
        "Without Monika here today, who am I gonna sit with today?"
        "I slowed down as I pondered the situation, I could do what I normally did before I started dating Monika and eat in the classroom..."
        "Or maybe I could go up to the roof!"
        "...but that might be crowded today since it is so nice out, ugh."
        "What to do, what to do..."
        show sayori 1q at t11
        "Oh, its Sayori!"
        "We haven't had lunch together in a while, maybe..."
        mc "Hey! Sayori!"
        show sayori 1o at h11
        "I waved my hand in the air through the crowd in an attempt to get her attention."
        "Sayori seemed confused and was frantically looking around her to find out who called her name."
        show sayori 1n
        "After a moment Sayori finally spotted me in the crowd."
        s 2o "[player]?"
        if SayoriVar > 1:
            $ c8s = 1
            show sayori 1q
            "Sayori made her way over to me with a large smile on her face."
            mc "Yup, that's my name don't wear it out."
            s 2c "What are you doing here? I thought you'd be down at the cafeteria by now."
            show sayori 2b
            mc "Well, I probably would have been but I uh... ran into a bit of a problem."
            s 4h "[player], what's wrong! Did something happen?!"
            show sayori 4f
            mc "No no, nothing happened! I just..."
            show sayori 1e
            mc "Well I guess I'm just so used to sitting with Monika for lunch that I uh..."
            s 2l "Oh [player], I get it."
            s 1x "I'd love to sit with you!"
            show sayori 1a
            mc "Thanks a bunch, I don't know what I would have done without you."
            s 5b "Anything.. for you [player]."
            s 2s "Ehehe~"
            s 4x "Come on, this way!"
            scene bg h_class with wipeleft_scene
            show sayori 1q at l11
            "Sayori cheerfully made her way through the school with me in tow until we reached an empty classroom."
            s 3r "Here we are!"
            show sayori 1b
            mc "Well, I guess I ended up eating in a classroom anyway."
            s 4p "Huh? I'm sorry [player]!"
            s 1l "I just..."
            s 5a "I usually eat up here anyway, kinda just went with my usual I guess, ehehe~"
            show sayori 5b
            mc "I-it's fine, really, but.. why not sit with Natsuki or Yuri? You could have even sat with us if you wanted."
            s 2m "No, I couldn't sit with you guys. I don't want to ruin anything special like that..."
            s 2c "And the other's kinda just..."
            extend 2l"sit by themselves anyway."
            s 4r "So I found a nice quiet spot up here and enjoy myself."
            show sayori 1q
            "Sayori beamed as she took out her lunch but her response left me slightly off."
            mc "Really Sayori, if you ever want to sit with us you can. You won't ruin anything, it's just lunch."
            s 1l "Well..."
            s 2e "...I'll think about it, okay?"
            show sayori 1y
            mc "I can live with that answer."
            "We both started to dig into our food, the sweet tastes finally being realized from all those hours of waiting."
            show sayori 1b
            mc "Oh man I needed this soooo bad today."
            s 3c "Me too! Class was just sooo boring, I could barely stay awake."
            show sayori 1g
            mc "That might just be you not getting enough sleep."
            s 2h "I do!"
            s 2l "But who could say no to some extra sleep here and there.."
            show sayori 1d
            mc "What am I gonna do with you Sayori."
            "I chuckle and keep working through my lunch."
            show sayori 1y
            "Sayori kept a smile on her face and tried to start little conversations here and there but I felt like she kept giving me a strange look from time to time."
            "I just brushed it off and finished up the rest of my food."
            show sayori 1b
            mc "Welp, I think I'm gonna take a walk before the next class."
            s 1e "O-oh, okay [player]."
            s 3s "Well, I'll see you later at club!"
            show sayori 1q
            mc "See you there Sayori!"
            scene bg h_corridor 
            with wipeleft_scene
            "I waved back to Sayori and closed the door behind me."
            "As I started off down the hallway I took my phone from my pocket and clicked it on."
            "Immediately a new notification flashed up on the screen."
            m "{i}[player]!{/i}"
            "Confused, I opened up the messenger app and found a few other texts from Monika."
            mc "{i}Srry, was eating lunch w/ Sayori and didn't notice the texts{/i}"
            m "{i}With Sayori?{/i}"
            "Monika's response was faster than I expected."
            mc "{i}Yeah, had noone else to sit with{/i}"
            "I could see Monika immediately open the message but she didn't immediately start typing."
            "Seconds seemed to drag as I waited for her bubble to pop up saying she was typing, but after a minute or so I gave up looking."
            "Maybe she was just busy? Her mom did like to randomly drag her into things sometimes..."
            "Still... something tells me it's about what I said. Was she mad at me for sitting with Sayori?"
            "I thought we had this conversation though... ugh."
            "I try and shake the feeling by starting my walk to nowhere in particular."
            "Not too far though I get another text."
            m "{i}Well did you at least enjoy yourself?{/i}"
            mc "{i}I guess, it was just lunch{/i}"
            mc "{i}Was diffrent without you though{/i}"
            m "{i}Aw stop, I promise I'll make it up to you tomorrow <3{/i}"
            mc "{i}Alright, Ill hold you to it then <3{/i}"
            "I smile and sigh as I slip my phone back into my pocket."
            "Even something as simple as lunch can be a hassle sometimes, give me a break."
        else:
            $ c8s = 0
            "Sayori seemed to fumble around once she spotted me, like an animal trapped in a cage."
            mc "Hey Sayori! What's up?"
            s "Oh um... nothing really."
            mc "Well that's good, cause I wanted to ask you something."
            mc "I was wondering if maybe-"
            s "W-well I um.. need to go see someone before the period ends so..."
            s "I-I gotta go! I-I'll see you at club!"
            "Sayori races away into the crowd before I could react, vanishing from sight."
            mc "Sayori!"
            "My cry never reached her though, she was gone before I knew it."
            "Damn it Sayori, what's with her?"
            "Guess I'll be finding a classroom then..."
            scene bg class_day 
            with wipeleft_scene
            "After a bit of searching I found my old hiding spot."
            "I plopped down at the table in the back and took out my lunch."
            "The bento I had prepared just screamed my name as I took off the lid and the aroma hit me."
            "I took a bite of rice and fished my phone out of my pocket, placing it on the table."
            "As soon as I got it out a notification buzzed itself onto the screen."
            m "{i}How's school been so far? Have I missed anything?{/i}"
            "She doesn't miss a beat does she?"
            "I take another bite and tack out a response."
            mc "{i}No, nothin 2 serious. Were u waiting for lunchtime to text me?{/i}"
            m "{i}Well yeah! I didnt want u to miss anything!{/i}"
            m "{i}I'm not gonna be more of a bad influence on u than u already are for yourself{/i}"
            mc "{i}Hey! I can pay attention if I want to!{/i}"
            m "{i}Suuuure [player] <3{/i}"
            "I shake my head as I lean back into my chair and let out a sigh."
            mc "{i}You know, it's kinda dull round here without you{/i}"
            m "{i}Aww I miss you too [player]{/i}"
            m "{i}I'm feeling a lot better now that I've stretched and rested it, I'll definitely be back tomorrow!{/i}"
            mc "{i}That's great, Im glad it was nothing serious{/i}"
            "I felt a smile creep across my face."
            "The last bite of lunch finally came and tasted just as good as the first."
            "I wiped my face and threw the box and utensils back into my bag, making my way back out into the hallways."
            scene bg corridor 
            with wipeleft_scene
            "I step out into the hallway and take a peek at my phone again."
            m "{i}No, just a silly mistake that's gonna cost me -_-{/i}"
            mc "{i}Dont be 2 hard on yourself, u didnt miss much I swear{/i}"
            m "{i}I hope so, I can always just copy the notes from you, right [player]?{/i}"
            mc "{i}Yeah, of course!{/i}"
            m "{i}Thanks, your the best boyfriend ever [player]~<3{/i}"
            "I shudder at the thought of Monika seeing my half-assed notes and what terrible verbal lashing I'd get."
            "{i}You need to pay attention! How are you gonna pass the test!{/i}"
            "Don't worry Monika, I always figure it out in the end."
            "I rest my bag on my shoulder and start walking through the halls."
#C9
        scene bg cafeteria 
        with wipeleft_scene
        "I ended up making my way into the cafeteria."
        "Students bustled around every table and the buzz of conversation kept the room alive."
        "Compared to eating in a classroom, the difference was night and day almost."
        "Though the livelihood around here is probably why Monika likes eating here so much when we share a meal."
        "I started to make my way through the cafeteria to make my lap of the school when a small group of tables caught my eye."
        "They were all covered in pink, and a big sign stood next to it with a big red heart surrounded by a dozen other colorful hearts."
        "As I closed the distance I could make out the letters written in the big heart."
        "{i}Student Council's Annual Candy Gram Drive!{/i}"
        "{i}Send someone a sweet treat and help your school!{/i}"
        "Yup, another fundraiser for some event or another."
        "I always used to scoff at the silly things they'd come up with around this time of year but now..."
        "..I should probably get one for Monika, as cheesy as it is she would be upset if I didn't."
        "I wonder, do I even have any cash..."
        "Aha, I do! A couple crumpled bills in my wallet should do the trick if that sign is correct."
        "I make my way over to the table and get in line."
        "It's not too long, but I feel people step in line behind me almost immediately."
        "Guess it was a good thing I hopped in line when I did."
        "The person in front of me finally finishes paying the girl behind the counter and I step up to the table."
        $ s_name = "Student Council Member 1"
        s "Hello, how are you today?"
        mc "I'm fine, yourself?"
        s "Bored if I'm being honest, haha!"
        s "So how many candy grams will you be sending?"
        mc "Oh, just one please."
        s "Alright, that'll be just five bucks please."
        "I flattened out my bills and hand them over to the girl."
        s "Thaaank you! What color heart would you like?"
        mc "Oh um.. a green one, please."
        s "Coming right up!"
        "The girl ducked under the table and procured a box of heart candies and a green heart cut out of construction paper."
        s "Just head on over to the table to your left and write out your message to your sweetheart of choice! Then head over to my other associate to get it stamped for delivery."
        mc "Thanks!"
        "I take my things over to another table covered in an array of markers, sticker sheets and glitter glue."
        "Well, might as well go all out. Wouldn't want to disappoint."
        "I take my time lining the edge of the heart with a string of green glitter, taking care not to put too much."
        "As I let that dry, I pondered on what to actually write down on the heart."
        "Nothing too cheesy, but not terrible either."
        "I settled on: \"For the sweetest girl I'll ever know, Happy Valentine's Day! Love, [player]\"."
        "Still kinda cheesy but the whole idea of a candy gram is anyway."
        "Once that was done, I snagged a green stick-on gem to put at the end of my message."
        "I admired my work for a moment and quietly chuckled to myself."
        "Who would've thought I'd be writing out a candy gram for a girl, that girl being Monika no less."
        "With a smirk on my lips I got up and made my way over to the boy standing near a few boxes."
        $ s_name = "Student Council Member 2"
        s "Ah you're done, great. Now, who will we be sending this to on the big day?"
        mc "Well it's going to..."
        mc "..to Monika, Monika-{w= .5}{nw}"
        $ n_name = "???"
        stop music fadeout 1.5
        n "You?! Sending a gram to her?!"
        "I quickly turned around and found myself looking at a nerve wracking sight."
        play music t7
        "A group of your average run-of-the-mill jocks stood across from me all looking square at me."
        "The one in the middle steps a bit closer to me, his eyes burning into my own."
        $ n_name = "Jock 1"
        n "Who the hell do you think you are kid?"
        mc "Me? I'm-"
        n "{i}You{/i} are a scrawny little shit."
        n "Do you really think {i}she{/i} would want to get a gram from you?"
        mc "Yeah, I think she would enjoy one from me."
        "I widen my stance a little bit and puff up my chest."
        "Who the hell are these kids and what do they want?"
        $ y_name = "Jock 2"
        y "Heh, maybe I should send one to her. I bet she'd {i}love{/i} to see my name on a gram to her."
        n "I bet she'd like to see all our names, maybe she could even show us her appreciation some.. {i}other way.{/i}"
        "The whole group laughed at the leader's joke, but I could feel my blood burning."
        mc "Like hell she would, now get the hell outta my sight."
        n "Or what, pipsqueak?"
        "The kid started to slowly close the distance between us, his goons slowly forming a semi circle around me."
        n "Maybe we should just beat the sense into you, huh?"
        "{i}Crap, this isn't good. I'm outnumbered and outgunned here.{/i}"
        "{i}What am I gonna do...{/i}"
        $ m_name = "Boy"
        m "HEY! LEAVE THE KID ALONE!"
        "A student stepped in front of me, his arms stretched out wide."
        m "YOUR INJUSTICE WILL NOT GO UNNOTICED SCOUNDRELS!"
        m "GO BACK FROM WHERE YOU CAME AND NO ONE HAS TO GET HURT!"
        n "What the hell is your problem? You want a beating too?"
        "The boy stood his ground firm, I could even spot a smirk across his face."
        m "If a fight is what you want..."
        m "I WILL DELIVER JUSTICE SWIFTLY AND DECISIVELY TO YOU SCOUNDRELS!"
        "At this point the entire cafeteria had stopped to stare at the events unfolding in front of me."
        "Even a bit of a crowd had gathered around us, watching on from a safe distance."
        "The jocks noticed the shifting atmosphere and started to squirm."
        n "Fine, have it your way you pipsqueak fucks."
        stop music fadeout 1.0
        "The group scattered into the crowd just as one of the teachers made it through to us."
        play music t8
        $ s_name = "Teacher"
        s "Tom, what is going on here?"
        "The boy turned to the teacher with his hands at his hips and a wide smile on his face."
        $ m_name = "Tom"
        m "An altercation has been avoided and justice has been upheld, sir."
        m "All in a day's work."
        $ n_name = "???"
        n "Jeez Tom, enough with the justice act already."
        "Another student stepped up to Tom's side and shook his head."
        s "Well Jerry, it seems Tom's little act helped out once again."
        $ n_name = "Jerry"
        n "I can tell..."
        s "And you young man, are you okay?"
        "The teacher turned to me and asked in a sincere tone."
        mc "Yeah.. yeah I'm alright."
        s "What happened? I couldn't see through the crowd of students too well myself so I'm not sure what the commotion was about."
        mc "It was..."
        m "Jake and his posey of boneheads tried to intimidate this fine gentleman over something before I stepped in."
        n "And nearly get yourself beaten up in the process Tom!"
        m "If that is the price for upholding justice, then it is a price I'm always willing to pay!"
        s "Never a dull moment with you Mr. Tom, now is it?"
        "The teacher turned to me and smiled."
        s "If you are alright, I'll leave you in Mr. Tom's care for the rest of the period. I'll speak with security and we'll sort this out."
        mc "Thank you, sir."
        "The teacher nodded and strolled off away from us, and I turned to the two boys in front of me."
        mc "Thanks, I don't know what would have happened if you hadn't stepped in."
        m "No worries, I wouldn't let scum like him harm a soul in the presence of justice."
        n "You seriously need to give that game a break Tom, that Ausburne girl is really getting to you."
        m "W-well she's right! We must uphold justice whenever we can, no matter the circumstances."
        "Jerry sighed and shook his head at Tom before turning to me."
        n "You get used to him after a while, or at least that's what I tell myself."
        m "Hey! Don't ask me to help you out with your little predicament then if I'm {i}tough to work with{/i}."
        n "I didn't say that!"
        "Jerry seemed to back down after Tom's comment, looking away from us and holding his tongue but still keeping a sly grin."
        m "Anyway, it's been fun my friend but we should get these grams stamped for the mail department over here."
        m "Wouldn't want to fuck it up after all this and poor Monika doesn't get her message from her sweetheart now."
        "Tom slapped me on the back with a laugh and took me up to the student council member that was sitting there still in shock."
        "We got them stamped and put away correctly, with Tom asking the student council member something in a whisper that I couldn't catch."
        "He rejoined me and Jerry shortly afterward."
        m "Alright, it's all set Jerry."
        n "Thanks Tom.. I guess I owe you one again."
        m "No need, you know how I roll."
        m "Just want everyone's Valentine's Day to go the best it can, including yours my friend."
        "Tom extends a hand to me and I gladly shake it."
        m "Just try and avoid any more confrontations with anyone over your Monika and you'll have a smashing night, I can already tell."
        mc "You think so? I just don't understand why..."
        m "Why would people do something like this? Cause jealousy and hatred run deep in people, I've seen it first hand."
        m "But the light of justice will always ring out true, that I can assure you."
        n "We gotta get going or we're gonna be late for class, nice meeting you..uh.."
        mc "[player], it's been nice meeting you Jerry, and Tom."
        m "Eh, sounds better the other way around."
        n "Oh would you shut up!"
        "The two boys wave me off and start off towards the school hallways."
        "What a pair of kids if I've ever seen some."
        $ m_name = "Monika"
        $ s_name = "Sayori"
        $ n_name = "Natsuki"
        $ y_name = "Yuri"
        n "[player]!"
        "And now another pair has taken their place."
        show natsuki 4g at t21
        show yuri 3n at t22
        "Natsuki and Yuri came running up to me, both panting and looking at me with worry."
        show yuri 2p at f22
        y "[player] what happened! We couldn't get a good look from across the cafeteria but we heard that you were involved and..."
        show yuri 3o at t22
        show natsuki 3r at f21
        n "I was ready to knock someone's lights out! I just couldn't make my way to you fast enough.."
        show yuri 3q
        show natsuki 3s at t21
        mc "It's okay guys, I'm fine. Just some pushovers were all."
        show yuri 3u
        show natsuki 1p at f21
        n "What did they look like, what did they want! I'll freaking beat their faces in!"
        show natsuki 2u at t21
        mc "Natsuki, it's over now. Just some guys trying to talk trash about me and..."
        show yuri 2w at f22
        y "Monika, I'm presuming..."
        extend 2t "I'm sorry [player], that must have been awful."
        show yuri 1s at t22
        mc "A little, but they're gone now. Nothing to worry about for the time being."
        show natsuki 4w at f21
        n "What is it with people! First the girls at the supply closet, now this."
        n 3x "Why do people want to talk about my friends like this! It makes me so... GAHH!"
        show natsuki 2r at t21
        show yuri 2t at f22
        y "I understand your frustrations Natsuki, I feel the same, but acting rashly will only make the circumstances worse."
        y 1l "We'll let the school punish those boys and [player] here will be fine."
        show yuri 1i at t22
        show natsuki 3s
        mc "Yeah, thanks Yuri, and thank you for wanting to put up a fight for me Natsuki."
        show natsuki 1c
        mc "You probably could've been a big help to Tom."
        show natsuki 1k at f21
        n "Who's Tom?"
        show natsuki 1c at t21
        mc "Oh, just a friend. Saved my hide from those guys even, was willing to fight with me."
        show yuri 1j at f22
        show natsuki 2j
        y "Sounds like a great friend to have."
        show yuri 2a at t22
        mc "Yeah, nice kid that one."
        show yuri 2f at h22
        show natsuki 1k at h21
        "Just as I could catch my breath the bell went off for the end of lunch."
        show natsuki at f21
        show yuri 2o
        n "Oh no, we gotta go Yuri!"
        n 1m "I don't wanna be late again!"
        n 2t "Bye [player], see you at club later!"
        show natsuki at lhide zorder 1
        hide natsuki
        show yuri 1q at lhide zorder 1
        hide yuri
        "Natsuki takes Yuri by the arm and starts racing towards the hallways of the school."
        "I take her lead and make my own way to the next class of the day."

#C10
        stop music fadeout 2.0
        scene bg club_day 
        with dissolve_scene_full
        play music t3
        "The day dragged on for a few hours more before club time rolled around."
        "I took my time making it over to the club room, stretching a bit before stepping in."
        mc "Hey guys, I'm here."
        show natsuki 2b at l11
        n "There you are [player]! You know, just because Monika isn't here today doesn't mean you can just show up whenever!"
        show natsuki 2s
        mc "I'm not even that late though!"
        show natsuki 1e
        n "Late is late, doesn't matter how bad it is the fact still stands."
        show natsuki 1s at lhide zorder 1
        hide natsuki
        "I sigh and look around the room."
        "Yuri gives me a wave and a smile that just screams \"Sorry, you know how she is!\"."
        "I wave back and look over to the head of the room."
        show sayori 1y at t11
        "Sayori is knee deep in a daydream and clearly not paying attention to anything around her."
        "I step over to her and make an effort to make my approach as obvious as possible."
        mc "So, Vice President Sayori, what's on the agenda for today?"
        show sayori 4p at h11
        s "Uwwah! [player]!"
        s 5b "Sorry! I was just..."
        extend 5a "ehehe~"
        show sayori 1d
        mc "I know, so what's the plan for today?"
        s 2c "Well, Monika left me with a couple things she wanted done today."
        s 2l "We're mostly just wrapping up the Valentine's Day stuff for the papers, your poem and Yuri's short story."
        s 3r "Me and Natsuki are going to do some peer review on our stuff so it's extra cutesy!"
        show sayori 1q
        n "Hey! It's not going to be cutesy!"
        "We both laugh a bit before I regain my composure."
        show sayori 1a
        mc "Seems you got your hands full today."
        s 1x "No, it'll be super fun!"
        s 2l "But you do have {i}your{/i} hands full [player]! You wouldn't want to miss the deadline!"
        show sayori 1d
        mc "I know I know, I'll get on it."
        show sayori 4q at lhide zorder 1
        hide sayori
        "I sit down at a desk and pull out my work for the day. A few drafts of the big poem Monika wanted me to try for the paper."
        "We ended up agreeing on a sonnet styled poem to go with the big playwright curriculum we were doing in writing class."
        "As nice as it sounded on paper, actually writing the thing in the right format following all the rules was a pain in the neck."
        "I tried to widdle my way out of it, but Monika insisted that I give it my best shot."
        "Looking through the many drafts I had though, it was slowly coming together."
        "As much as I tried not to make it mirror Monika and I, the words just poured out onto the paper and connected in just the right ways to make a poem."
        "The best inspiration for a love poem just happened to be what had been right in front of me at the time."
        "After a bit of fumbling with the poem I decided to take a small break and stretch my arms."
        show sayori 1k at t11
        "As I looked up I noticed Sayori sitting back at the head desk, staring off into the distance again."
        "This time though she looked troubled by something, but I couldn't imagine what."
        "Sayori was the most cheerful girl I knew, it would take a lot to sour her mood."
        "I got up from my chair and made my way over to her, kneeling down and lowering my tone to a whisper."
        mc "Hey, Sayori..."
        show sayori 4p at h11
        s "Uwwah! [player], not again!"
        show sayori 3n
        mc "Shh sorry, sorry! Didn't mean to spook you."
        s 1l "It's okay, I guess I was in my own little world for a little bit."
        show sayori 1l
        mc "I could tell, even from across the room."
        show sayori 1d
        mc "Is something wrong Sayori?"
        s 2e "Huh? W-what do you mean [player]?"
        show sayori 1g
        mc "I mean is something bothering you? You just had a look that made me wonder I guess..."
        s 2l "No, no, nothing is wrong, see!"
        show sayori 4q
        "Sayori beams a smile at me bright with what would seem like joy under any other circumstance."
        show sayori 2e
        mc "Sayori please, you can tell me if something is wrong. I'm your friend, right?"
        s 1h "Well...yeah I know that..."
        s 2l "But nothing is wrong [player], I promise."
        show sayori 1d
        mc "Alright, but don't hesitate to tell me if something is bothering you remember."
        s 3c "If anything I should be asking you if your okay, I kinda heard about what happened from some classmates."
        s 1g "What happened?"
        show sayori 1f
        mc "Nothing serious, just some guys tryna act tough. I'm fine."
        s 2h "Are you sure [player]?"
        show sayori 1d
        mc "Yeah, just peachy."
        s 1d1 "Alright, if you say so. You know I'll always listen though."
        s 4r "Now get back to work [player]! Ehehe~"
        show sayori 3q
        mc "Yeees ma'am."
        scene bg club_day 
        with wipeleft_scene
        "With a bit more work done the poem was coming along nicely."
        "Maybe I'd even have it done by tomorrow's meeting, that would be nice."
        "I take a look at my phone for the time and see it's almost time to pack up and leave."
        "I also notice a new message sitting on my lock screen from Monika."
        m "{i}Meet me by the bus stop after school. I need to see you.{/i}"
        "Didn't leave much room to argue, but that's Monika for you."
        s "Everyone!"
        "Sayori's voice breaks my train of thought and I look up."
        show sayori 3x at t32
        show natsuki 3a at t31
        show yuri 1a at t33
        show sayori at f32
        s "It's time to pack up for today! Good job on the progress today everyone!"
        show sayori 1a at t32
        show yuri 2b at t33
        y "Thank you Sayori, with another day or so this should be all set for the paper."
        show yuri 1i at t33
        show natsuki 1l at f31
        show sayori 2x
        n "Yeah, my poem is just about done too! This edition of the paper is gonna be great!"
        show natsuki 1j at t31
        show yuri 1a
        show sayori 1a
        mc "Maybe even our best yet."
        show natsuki 3t at f31
        n "Yeah, but I know we can do even better."
        n 4y "Knock the ratings right outta the park!"
        show natsuki 4a at t31
        show sayori 4r at f32
        show yuri 1m
        s "Yeah! Go team!"
        show sayori 1q at lhide
        hide sayori
        show natsuki 2a at lhide
        hide natsuki
        show yuri 1a at lhide
        hide yuri
        "With that we all laughed and started to grab our things and clean up the room for the day."
        "As I tuck my folder into my bag I notice Sayori shuffle her way over to me."
        show sayori 2l at l11
        s "Hey... [player]..."
        show sayori 1e
        mc "Oh hey, what's up Sayori?"
        s 5b "Um.. well I was wondering if..."
        s 5a "Maybe since Monika isn't here today we could.. you know.. walk home together again?"
        show sayori 3y
        mc "Oh, well uh.."
        "Sayori's asking me to walk home with her again while Monika's not here."
        "I thought I said she could come with us on a walk home, but why insist on asking while she's not around?"
        "And I still have to see Monika on the way home too, so it's not like we'd be alone on the walk anyway."
        menu:
            "What do I tell her?"
            "Sure":
                show sayori 1n
                mc "Sure, if you wanna tag along you can."
                s 4r "Okay! Thanks [player]!"
                show sayori 1q
                mc "It's nothing, really."
                show sayori at t41
                mc "But Sayori..."
                show sayori 2q at t44
                "Sayori was darting around the clubroom putting things away and lining up the desks for tomorrow's class."
                show sayori at t42
                mc "Sayori."
                show sayori 3n at t11
                s "Hmm? What is it?"
                show sayori 3e
                mc "Well, Monika wanted to see me after school today. She said she'd be waiting by the bus station on the way back."
                s 1h "Oh..."
                if SayoriVar >= 1:
                    $ SayoriVar += 1
                    s 2l "Well that's okay, right? You said it yourself..."
                    show sayori 1d
                    mc "Yeah of course, I just didn't want it to be a surprise."
                    s 2d1 "Well let's get going then, wouldn't want Monika to worry would we?"
                    show sayori 2q at lhide
                    hide sayori
                    "Sayori happily skips out of the clubroom and motions me along."
                    scene bg schoolgate 
                    with wipeleft_scene
                    "I step outside into the evening sunlight and take a long breath."
                    show sayori 1a at l11
                    "Sayori pops up beside me and also takes in a deep breath."
                    show sayori 2x at h11
                    s "Okay! Let's go find Monika!"
                    show sayori 1a
                    mc "Couldn't have said it better myself, this way."
                    scene bg h_residential 
                    with wipeleft_scene
                    "I take the usual route I walk with Monika toward her bus stop she takes home."
                    "It's a nice part of town no doubt, and the walk is filled with enough sites to keep myself entertained."
                    show sayori 1y at l11
                    "Sayori seemed to enjoy the walk, but I could tell something was eating at her."
                    "I tried to ask her about it but she just said it was nothing."
                    "After enough walking I spot the small stop and spot a familiar looking girl sitting alone at it's bench."
                    show sayori 1e
                    mc "Sayori, stay here for a second alright?"
                    s 2l "Oh okay. What are you gonna do?"
                    show sayori 1b
                    mc "Watch."
                    show sayori at thide
                    hide sayori
                    "I lay my bag beside Sayori and give the bus stop a wide berth so I can get out of Monika's line of sight."
                    "I slowly approach Monika until I was right next to her, and I slip myself onto the bench seat next to her."
                    mc "Excuse me, is this seat taken beautiful?"
                    show monika 1bb at t11
                    show monika at h11
                    m "[player]!"
                    show monika 1bj at face 
                    with dissolve
                    "Monika immediately jumps up from the bench and wraps her arms around me."
                    m 1bg "[player], I was so worried..."
                    show monika 1bf
                    mc "Worried about what, I didn't take that long did I?"
                    m 1bn "No silly, not that."
                    m 1bg "I heard.. I heard about the fight that almost happened today."
                    show monika 1bf
                    mc "Oh, that.. well nothing happened and I'm fine, see."
                    show monika 1be at t11 
                    with dissolve
                    "I do a small self inspection with my hands and Monika giggles a bit."
                    m 4be1 "I'm glad, but a girl can still worry about her boyfriend."
                    m 2bg "What happened? All anyone told me was that a bunch of kids almost beat you up!"
                    s "Yeah, what {i}did{/i} happen [player]?"
                    show monika 1bd at t21
                    show sayori 1b at t22
                    "Sayori finally walked over and looked at both of us."
                    show monika 2bd at f21
                    m "Sayori? What are you doing here?"
                    show monika 1bc at t21
                    show sayori 3l at f22
                    s "Well, I kinda... asked [player] if he wanted to walk together and he said yeah."
                    s 1d1 "But I knew he needed to see you too so I'll just be going then."
                    show sayori 1y at t22
                    mc "Sayori, you don't-"
                    show sayori 2x at f22
                    s "I'll see you guys tomorrow okay? Bye!"
                    show sayori 1q at lhide
                    hide sayori
                    show monika 2bm at t11
                    "Sayori skipped away before I could even retaliate, humming a tune to herself as she went."
                    show monika 2bc
                    mc "God damn it Sayori..."
                    m 1bg "What's wrong?"
                    show monika 1bf
                    mc "I don't know, something is off with her today."
                    m 2bn "I'm sure it's nothing [player], just your imagination."
                    show monika 2be
                    mc "I hope so, but I don't know..."
                    m 4be1 "I'm sure of it, let's not worry about her, okay?"
                else:
                    $ SayoriVar += 1
                    "Sayori seemed to burn out of her enthusiasm in an instant when I mentioned Monika."
                    s "O-oh..."
                    s "Well you should probably see her then instead, I wouldn't want to get in the way of things."
                    mc "No, Sayori, you wouldn't get in the way of anything."
                    s "[player], don't worry about it."
                    s "Go see Monika, I'll finish up here alright?"
                    s "Thank you for at least offering though!"
                    "Sayori turns to the room once again and starts cleaning up a small mess on the floor."
                    mc "Okay, see you tomorrow Sayori."
                    s "See ya [player]!"
                    "I sling my bag onto my back and head for the door."
                    scene bg schoolgate 
                    with wipeleft_scene
                    "I step outside into the evening sunlight and take a long breath."
                    "Alright, off to find Monika."
                    "I take the usual route I walk with Monika toward her bus stop she takes home."
                    "It's a nice part of town no doubt, and the walk is filled with enough sites to keep myself entertained."
                    "After enough walking I spot the small stop and spot a familiar looking girl sitting alone at it's bench."
                    mc "Is this seat taken?"
                    m "[player]!"
                    "Monika immediately jumps up from the bench and wraps her arms around me."
                    m "[player], I was so worried..."
                    mc "Worried about what, I didn't take that long did I?"
                    m "No silly, not that."
                    m "I heard.. I heard about the fight that almost happened today."
                    mc "Oh, that.. well nothing happened and I'm fine, see."
                    "I do a small self inspection with my hands and Monika giggles a bit."
                    m "I'm glad, but a girl can still worry about her boyfriend."
                    m "What happened? All anyone told me was that a bunch of kids almost beat you up!"
                    mc "Well I was just... doing something and then these kids started talking bad about us, about you."
                    m "What were you doing that could make them say that?"
                    mc "I was..."
                    "Can't say candy grams cause that'll ruin the surprise."
                    mc "..just talking with a friend and you came up in the conversation."
                    mc "They must have been listening in or something."
                    if c8s == 1:
                        m "Was it Sayori?"
                        mc "Huh? No she was somewhere else when it all happened."
                        m "Funny, I thought you ate lunch with her today?"
                        mc "I did, but she stayed in the classroom while I took a walk."
                        m "You two ate alone?"
                        "Monika's tone seemed to sour almost immediately."
                        mc "Well yeah, but we just chatted for a bit and ate. Nothing bad."
                        m "Okay, if you say so."
                        mc "Monika, I just sat with Sayori as a friend. That's it."
                        mc "I thought we went over this."
                        m "Yeah, I know. I just..."
                        "I pull Monika into a hug and lower my head into her shoulder."
                        mc "I love you Monika, and only you."
                        mc "Remember?"
                        m "Yeah, I remember."
                        "Monika eventually pulls away and looks back at me."
                    else:
                        m "Oh, who were you with?"
                        mc "Just an.. old friend of mine. We happened to catch up in the cafeteria."
                        m "Mhmm, sounds like a bad excuse [player].."
                        mc "No really, I just-"
                        m "I'm kidding! Come on, I'm not that mean, ahaha~"
            "Actually...":
                mc "Actually Sayori, I need to see Monika after school today."
                mc "She texted me not too long ago asking to meet her."
                s "Oh... okay then."
                s "Well I wouldn't want to get in the way of that so I understand!"
                s "Maybe... some other time then."
                mc "Yeah definitely, and you don't have to wait for Monika to be absent either."
                mc "You can always-"
                s "I know, but..."
                s "Anyway, I'll see you tomorrow [player]! I can finish up here today."
                s "Wouldn't want to keep Monika waiting, ehehe~!"
                "Sayori then basically pushed me out of the clubroom against my protests."
                scene bg corridor 
                with wipeleft_scene
                mc "Sayori!"
                "The door closed behind me with a thud, and wouldn't budge when I tried the handle."
                "Damn it Sayori!"
                "I tried the door again before giving up the struggle against her."
                "I didn't mean for it to come off mean anything, I just..."
                "With a sigh I adjust my backpack and start for the door."
                scene bg schoolgate 
                with wipeleft_scene
                "I step outside into the evening sunlight and take a long breath."
                "Alright, off to find Monika."
                "I take the usual route I walk with Monika toward her bus stop she takes home."
                "It's a nice part of town no doubt, and the walk is filled with enough sites to keep myself entertained."
                "After enough walking I spot the small stop and spot a familiar looking girl sitting alone at it's bench."
                mc "Is this seat taken?"
                m "[player]!"
                "Monika immediately jumps up from the bench and wraps her arms around me."
                m "[player], I was so worried..."
                mc "Worried about what, I didn't take that long did I?"
                m "No silly, not that."
                m "I heard.. I heard about the fight that almost happened today."
                mc "Oh, that.. well nothing happened and I'm fine, see."
                "I do a small self inspection with my hands and Monika giggles a bit."
                m "I'm glad, but a girl can still worry about her boyfriend."
                m "What happened? All anyone told me was that a bunch of kids almost beat you up!"
                mc "Well I was just... doing something and then these kids started talking bad about us, about you."
                m "What were you doing that could make them say that?"
                mc "I was..."
                "Can't say candy grams cause that'll ruin the surprise."
                mc "..just talking with a friend and you came up in the conversation."
                mc "They must have been listening in or something."
                if c8s == 1:
                    m "Was it Sayori?"
                    mc "Huh? No she was somewhere else when it all happened."
                    m "Funny, I thought you ate lunch with her today?"
                    mc "I did, but she stayed in the classroom while I took a walk."
                    m "You two ate alone?"
                    "Monika's tone seemed to sour almost immediately."
                    mc "Well yeah, but we just chatted for a bit and ate. Nothing bad."
                    m "Okay, if you say so."
                    mc "Monika, I just sat with Sayori as a friend. That's it."
                    mc "I thought we went over this."
                    m "Yeah, I know. I just..."
                    "I pull Monika into a hug and lower my head into her shoulder."
                    mc "I love you Monika, and only you."
                    mc "Remember?"
                    m "Yeah, I remember."
                    "Monika eventually pulls away and looks back at me."
                else:
                    m "Oh, who were you with?"
                    mc "Just an.. old friend of mine. We happened to catch up in the cafeteria."
                    m "Mhmm, sounds like a bad excuse [player].."
                    mc "No really, I just-"
                    m "I'm kidding! Come on, I'm not that mean, ahaha~"
        m 2bk "Anyway, I'm just glad to see your okay."
        show monika 1ba
        mc "Thanks, and how's your neck doing by the way?"
        m 2bn "Oh it's fine now, guess I'll never sleep like that again, ahaha~"
        m 2be1 "Did club go smoothly without me?"
        show monika 2be
        mc "Yeah, things are almost done for the big day."
        m 2bl "I'm glad, I was worried we'd never finish in time."
        m 4bk "And you could say more than just writing is coming together for the big day as well."
        show monika 1bj at face 
        with dissolve
        "Monika gives me a huge smirk and clings onto me once again."
        "Whatever she's planning, it must be good."
        show monika 2bn at t11 
        with dissolve
        m "Well I better get going before Mom gets antsy about where I am."
        m 3bl "She might think I'm hiding away with you or something, ahaha~"
        show monika 2be
        mc "Wouldn't want her to think that, I'll see you tomorrow okay?"
        m 2bb "Yup, see you then!"
        m 4bn "And send me the homework you got so I can get a start on it please!"
        show monika 1be
        mc "Mhmm, I will. Love you Monika."
        m 1bb "Love you too [player]!"
        show monika 1bj at lhide
        hide monika
        "She blows me a kiss before hoping on a bus that just pulled up."
        "I wave back as it rolls off down the road and sigh."
        "I hope I don't screw up my end of the day."
#C11
    stop music fadeout 2.0
    scene bg class_day 
    with dissolve_scene_full
    play music t2
    "Finally, the day was here."
    "As I sat in homeroom, I was surprised to feel relatively calm."
    "Even though I had spent the last week or so trying to make everything right for today, sitting here felt like any other day."
    "Just another day at school with boring classes until we get out for the day."
    "That is, until a girl not in this class came in with a cart full of small boxes."
    $ s_name = "Student Council Member"
    s "Good morning everyone, before classes start for the day we wanted to deliver your candy grams to you all."
    s "Please raise your hand if I call your name and I'll bring them over to you."
    "She then began to list off a couple names from a clipboard she had."
    "It was mostly girls who received them from our class, probably from boyfriends or secret admirers."
    "I just hope Monika smiles as much as these girls do when she gets mine."
    s "Do we have a [player] in class today?"
    mc "Oh, here!"
    "I shot my hand up out of muscle memory to hearing my name in the morning."
    s "Perfect, here you are."
    "The girl plucks a box from her cart and places it on my desk."
    s "That seems to be the last of them from this class, enjoy your day everyone!"
    "As she took her leave from the class, the room burst into chatter as students gathered around the ones who got candy grams."
    "Luckily for me nobody came over to me immediately so I could look at mine in piece."
    "A very neatly decorated red heart adorned my box of sweets, with red glitter and a red ruby sticker in the center."
    "I flipped the heart over and took a look at the inscription on the back"
    call showpoem (poem_m7, revert_music=True, where=truecenter)
    stop music
    play music t2
    "I couldn't help but smile as I set the heart down."
    "She really was something else, that I couldn't deny."
    "I packed the candy away in my bag for later and took great care to pack the note safely in one of my folders to bring home."
    $ s_name = "Female Student"
    s "So, who got you a gram this year [player]?"
    "Some of the girls had broken away from talking and turned to me."
    mc "Well, my girlfriend did."
    s "And who would that be?"
    "The way she sneered that sentence gave me enough to know where this was going."
    mc "I have a feeling you already know the answer to that question."
    s "Aww, did she really get you one? Or did you buy yourself one to feel better?"
    "All I could manage to muster was a scowl as the girls laughed amongst themselves."
    "Thankfully the teacher walked into class just as they started to laugh so I wouldn't have to deal with them."
    "Never thought I'd be grateful for class to start in my life."
    $ s_name = "Sayori"
    scene bg h_corridor 
    with wipeleft_scene
    "The day went on as normally as it usually does, class being boring and me not paying attention too well."
    "Though instead of the usual doodling I found myself rereading Monika's little poem over and over again."
    "It seemed to make me smile every time I looked at it."
    "But nothing made me smile more than the thought of going to computer science class today."
    "I felt my heartbeat start to quicken as I got closer and closer to the room."
    "I'm finally going to see Monika today, it's nothing new but today made it seem so special."
    "Nervous for nothing, but I still couldn't get the edge off as I walked."
    m "[player]!"
    "That all to familiar voice rang out from behind me and I immediately spun around."
    show monika 1a at t11
    "There she was, walking toward me with her arms wide open."
    mc "Monika!"
    show monika 1j at face with dissolve
    "I couldn't stop myself. I almost ran right to her and wrapped my arms around her waist, nearly lifting her up in excitement."
    m 1l "Gosh, I've never seen you like this [player], ahaha~"
    show monika 1e
    mc "Sorry, I just... really wanted to see you."
    show monika 1e at t11 with dissolve
    "I put her back down and felt myself blush a bit from embarrassment."
    m 2e1 "Hey don't be sorry, I wanted to see you too."
    m 1n "And I wanted to thank you for the gift this morning."
    m 3e1 "It really made my morning that much more special."
    show monika 1e
    mc "It was the least I could do for you, and I should thank you for your gift this morning too."
    mc "It made my morning too."
    m 1k "I'm glad!"
    m 2l "Now come on, we're going to be late for class if we stay out here for much longer."
    m 5a1 "Unless your trying to get me to skip class with you, maybe even..."
    show monika 1k at face 
    with dissolve
    m "Hide in a closet somewhere?~"
    show monika 5a at t11 
    with dissolve
    mc "H-hey, Monika!"
    show monika 1j at lhide
    hide monika
    "Monika just laughed as she made her way into class in front of me, covering her now flush face from everyone but me."
    "I just shook my head and sighed to myself as I followed her in."
    scene bg class_day 
    with wipeleft_scene
    "I took my seat next to Monika and did my usual routine of logging into the computer."
    "As I leaned back and watch the loading wheel spin, I felt something touch my neck."
    show monika 1j at face 
    with dissolve
    "I turned to find Monika nearly in my face, a huge grin on her's."
    "I couldn't help but laugh at the sight of it."
    mc "Monika, what do you think your doing?"
    m 1k "Well, just enjoying your company, [player]~"
    show monika 1j
    mc "That close?"
    show monika 2n at t11 
    with dissolve
    m "Well you were {i}supposed{/i} to turn so our lips matched up but {i}that{/i} didn't happen, ahaha~"
    show monika 2m
    mc "Jeez, what's with all the cheesy lovey-dovey stuff today?"
    m 2k "It's Valentine's Day silly! That's what today is about!"
    show monika 1a
    "Monika scoot's her chair closer to me, her legs coming to rub up against mine."
    m 3b "It's about expressing and celebrating the love we share together."
    m 1n "I just wish we weren't stuck at school for most of the day."
    show monika 1c
    mc "I'd suggest taking it up with the student council, I bet you could sway them to make Valentine's day a half day next year."
    m 1l "I would try if this wasn't our last year here silly."
    show monika 1e
    mc "I know, but we still can celebrate as best as we can this year."
    mc "Even if it's spent in this prison for half of it."
    m 3l "Well would prison let you play games freely in computer science class?"
    show monika 1e
    mc "No, but I'd still try to anyway."
    m 2n "I know you would [player], ahaha~"
    m 1b "Hey, how about you boot up one of them for us? Something two player?"
    show monika 1c
    mc "Do my ears deceive me? The star student Monika asking to play computer games in class?"
    m 1n "Yeah yeah, you heard me right."
    m 1e1 "I just wanna spend as much time with you as I can today, [player]."
    m 3k "Besides, I'm ahead with the curriculum anyway. I technically have nothing to do today."
    m 3l "And I bet you were planning to play games anyway, right?"
    show monika 1e
    "Crap, she knows me too well."
    mc "Fiiine, I'll check and see what I got."
    show monika 1a
    "I scroll through my \"schoolwork\" folder and look at all the subfolders."
    "I finally get to \"NewReligion\" folder and I open it up."
    show monika 1c
    "Running the executable pops up the old reliable Damned."
    m 1d "Wait, don't you have this at home? Why does it look so different?"
    show monika 1c
    mc "This is the original version of it, the one I have at home is a newer version."
    mc "The granddaddy of all the shooters to date right here."
    m 3n "That's cool and all [player], but isn't it super gory and all?"
    show monika 1m
    mc "Well I mean I guess, but it's all pixilated and stuff."
    show monika 1c
    mc "But we're not gonna be fighting demons, unless you wanna of course."
    "I move the cursor over to the \"Multiplayer\" tab and hit enter."
    mc "We can battle each other, just like on Rumble back home."
    mc "This is where that kinda game originated from."
    m 2b "Alright, I'll take you up on your offer."
    m 3n "As long as it doesn't turn into anymore of a history lesson, ahaha~"
    show monika 1m
    mc "What, it's an important piece to the video game culture as a whole!"
    show monika 1j
    "Monika just giggles some more as she leans over and kisses me on the cheek."
    m 1e1 "I'm joking."
    extend 1n".. {i}mostly...{/i}"
    show monika 1e
    "Monika's smile helped curb my protest and we set up our controls."
    show monika 1a
    "I dreaded playing with keyboard aiming, but that's the only way we could both play at the same time."
    "With our keys set, we both took our positions on the keyboard."
    "I couldn't help but notice Monika's leg rubbing up against me once again."
    show monika 1d
    mc "Monika, you don't have to sit this close to me to use that side of the keyboard."
    m 1b "But it's more comfortable this way!"
    m 1e1 "And maybe I wanna snuggle up with my boyfriend for a little, hmm?"
    show monika 1j
    "Monika moved her seat ever so closer to mine, her leg and shoulder firmly pressed against me."
    show monika 1m
    mc "Fine, but you can't cheat like last time. We're at school you know."
    m 3l "Me? A cheater? Nooo, that must be one of your other girlfriends."
    show monika 1j
    "Monika laughs, but quickly tries to change the subject."
    m 1d "Ooo, can we play on that map?"
    show monika 1c
    mc "Sure, don't be mad when I beat you though. That's my go to map to play."
    m 1h2 "Alright, bring it on!"
    show monika 1h1
    "A wide grin covered my face, this is gonna be fun."
    stop music fadeout 2.0
    scene bg class_day 
    with wipeleft_scene
    play music t7
    "The game was close the whole way through, with a score of 50 to reach and the standings being me in the lead 39 to 36."
    "Monika was putting up a good fight too, she quickly got the hang of moving around the map and using it to her advantage."
    "A rocket frag here, a quick shotgun blast there, and the score got ever closer to the winning number."
    show monika 1h2 at t11
    m "Come back here [player], I got a present for you!"
    show monika 1h1
    mc "Nuh-uh, take this!"
    m 1l "Dang it! I'll get you for that!"
    show monika 1h1
    mc "Ah ha ha- Oh come on."
    show monika 1k
    m "Ahaha~! Told you!"
    show monika 1a
    "With frag after frag, the game was reaching its final moments."
    "A quick blast from the twin barrel put me at 49 kills, just one more to do it."
    m 1i "No no, don't you dare!"
    show monika 1h1
    "Monika fought back hard, cheesing me with a rocket launcher for her 48th kill."
    mc "You can't stop the inevitable Monika, just come to me."
    m 1h2 "No! I won't let you!"
    show monika 1h1
    "She makes me give chase, leading me into a close hallway where she turns on me and hits me with a twin barrel of her own."
    m 3k "Yes! Just one more!"
    m 1h2 "Look out [player]! Here I come!"
    show monika 1h1
    mc "Come at me!"
    "I spawn back in and move to grab the rocket launcher."
    "As I grab it and turn to the main area of the map, a thought pops up in my head."
    "{i}Maybe I should just let her win this one, make her happy.{/i}"
    "As I run towards where Monika is on the map, I make my decision."
    menu:
        "I decide to..."
        "Take the hit":
            "Yeah, just give her the win [player]. What's one deathmatch anyway."
            "I meet Monika in a room I knew very well."
            "She charges me with a twin barrel, but I duck behind some of the pillars in the room on instinct."
            "I fire one rocket and damage her a bit and decide to put my plan into action."
            "I go against all my instincts and charge out of safety towards Monika, fists out and swinging wildly."
            stop music fadeout 5.0
            "My poor guy never stood a chance against the power of a twin barrel at such close range and Monika lays me out for the final kill."
            play music t2
            m 3k "Yay! I won!"
            m 1h2 "I told you [player], I told you I'd beat you in the end!"
            show monika 1h1
            mc "Damn, got me good with that last shot."
            m 3k "Yup! Ran right up to you and just {i}KAPOW!{i}"
            m 1b "That was a lot of fun though!"
        "Show no mercy":
            "No, I'm not gonna take a loss on {i}my{/i} map."
            "I meet Monika in a room I knew very well."
            "As she moves in with the twin barrel, I take cover behind a row of pillars."
            "It blocks the shot perfectly, and I jump out and fire back with the launcher."
            stop music fadeout 5.0
            "It only takes a few times, but I juked around the poles and gibbed Monika for the final kill."
            play music t2
            m 3k "Aww, I was so close!"
            m 2n "All it took was one move though. darn."
            show monika 1e
            mc "I warned you, didn't I?"
            "I couldn't help but kick back in my chair, hands behind my head and a wide grin for maximum smug."
            m 3k "Still, I was pretty on par with the self proclaimed \"King of the Map\"."
            show monika 1e
            "Monika lightly punched me in the stomach, nothing that would hurt me but enough to get me out of my pose."
            show monika 1j
            mc "Hey! What was that for!"
            m 2n "Oh come on, that didn't hurt and you know it."
            m 1b "But that was fun anyway, even if you won in the end."
    show monika 2a
    mc "Yeah it was close but fun none the less, GG Monika."
    m 1c "Hmm?"
    "Monika looks at me puzzled and I get just as confused."
    mc "What?"
    m 3d "What did you say? GG?"
    show monika 1c
    mc "Yeah, it means good game. You say that at the end of an online match to everyone in the lobby after a fun game."
    m 1n "[player], what did I tell you about the gaming lectures? Ahaha~"
    show monika 1m
    mc "What?! You asked what it ment!"
    m 1l "I know, I'm just teasing you."
    m 1e1 "It's cute when you nerd out sometimes."
    show monika 1e
    mc "What's that supposed to mean?"
    show monika 1j at face 
    with dissolve
    "Monika just giggles and wraps her arms around me."
    "Just as I wrapped mine around her, the bell rang for the end of the period."
    m 1e1 "I guess this is goodbye for now [player], until club time."
    show monika 1e
    mc "Until club time."
    show monika 1j at t11 
    with dissolve
    pause .5
    show monika at lhide
    hide monika
    "Monika gives me one more kiss before putting on her bag and walking out the door while I shut down the computer."
    "I grab my things and try to stiffle my big stupid grin before I looked like an idiot in the hallway but I couldn't help it."
    "She really did bring me too much joy sometimes."

#C12
    stop music fadeout 2.0
    scene bg corridor 
    with wipeleft_scene
    play music t3
    "The day seemed to take even longer than usual, the minutes turning into hours."
    "But finally the last class ended and I was making my way to the club room."
    "As I got closer to the room I could feel myself smiling more and more."
    "I just couldn't help but get excited at the prospect of seeing Monika again."
    "After enough walking I finally rounded the last corner and made it to the door."
    scene bg club_day 
    with wipeleft_scene
    mc "Hey guys, I made it."
    show monika 1b at l11
    m "There you are [player]!"
    show monika 1a at h11
    "Monika nearly spun around from her desk and ran over to me."
    m 4k "Now we can finally see what Natsuki brought!"
    show monika 2a
    mc "What Natsuki brought?"
    show monika at t21
    show natsuki 5l at t22
    show natsuki at f22
    n "Yeah, I brought something for everyone dummy."
    n 5q "And if you didn't take so long we would have been done with them by now."
    n 3d "Come on, let's get some desks pushed together."
    show natsuki at lhide
    hide natsuki
    show monika 1e at t11
    "I looked over to Monika and she just shrugged her shoulders."
    scene bg club_day 
    with wipeleft_scene
    "After a few minutes we finally got the desks arranged into one large table."
    show monika 1a at t41 zorder 3
    show sayori 4r at t42 zorder 2
    show natsuki 3j at t43 zorder 2
    show yuri 2a at t44 zorder 3
    show sayori at t42
    s "Ooo, did you bring cupcakes again Natsuki! I love when you bring cupcakes!"
    show sayori 1o at t42
    show natsuki 3l at f43
    n "No, not cupcakes today, but..."
    n 4z "Cookies!"
    show natsuki 4j at t43
    show monika 2d
    show sayori 4n
    show yuri 1e
    "In a dramatic fashion Natsuki lifted the foil from a plate of neatly arranged heart shaped cookies."
    "Each one was carefully decorated with sprinkles and frosting so they all were unique in some way."
    show monika 2a
    show yuri 1j at f44
    y "My my, these look fantastic Natsuki."
    show yuri 2i at t44
    show sayori 4m at f42
    s "Yeah! They look so yummy and cute!"
    s 4p "I just wanna eat them all up!"
    show sayori 1n at t42
    show natsuki 5t at f43
    show yuri 1a
    n "I-it's nothing, these were super easy compared to the cupcakes I usually do."
    n 4s "I just didn't have the ingredients for those so I made due with what I had."
    show sayori 1b
    show natsuki 4k at t43
    mc "Well you did good with decorating these too, they look adorable."
    show natsuki 3t at f43
    n "Oh just shut up and eat them already you guys, jeez."
    show natsuki 3a at t43
    show sayori 3q
    "We all laughed as we each grabbed a cookie from the platter, mine being covered in pink frosting and red sprinkles."
    "I took a bite and was immediately hit with the wave of sweetness that came with Natsuki's baking."
    show monika 4b at f41
    m "Gosh, these are excellent Natsuki! Thank you so much for bringing these in for all of us."
    show monika 2a at t41
    show natsuki 2d at f43
    n "Oh it was nothing, I just figured since it was a holiday I should at least bring something."
    show monika 2m
    n 1t "Even if there is only like two people actually celebrating it here."
    show monika 4n at f41
    show natsuki 2s at t43
    m "Well, we still should thank you anyway."
    show monika 2e at t41
    show yuri 3t at f44
    show natsuki 2c
    y "Maybe I should put some tea on as well.."
    extend 3q "I think I know the perfect match for these cookies."
    show yuri 2a at t44
    show sayori 3r at f42
    show natsuki 1j
    s "Yay! Tea and cookies!"
    show sayori 1a at t42
    show yuri 1m
    "Yuri stepped over to the closet and pulled out her tea set."
    show yuri 1c at lhide
    hide yuri
    show monika at t31
    show sayori at t32
    show natsuki at t33
    "She placed the cups around the table and then went off to fill her kettle with water."
    show sayori 2x at f32
    show monika 2c
    s "Sooo what else are we gonna do today Monika?"
    show sayori 2a at t32
    show natsuki 2k at f33
    n "Yeah, is there any new special we have to be working on?"
    show monika 4l at f31
    show natsuki 1j at t33
    m "Not that I know of, no. For now we can just relax and enjoy today."
    show monika 1e at t31
    show monika at t41
    show sayori at t42
    show natsuki at t43
    show yuri 1a at l44
    pause .5
    show yuri 1b at f44
    y "I'm back. Did I miss anything?"
    show monika 3b at f41
    show sayori 1n
    show natsuki 2k
    show yuri 2e at t44
    m "Nope, I was actually just about to congratulate you all on a job well done."
    show monika 1a
    "Yuri set her kettle to boil and sat back down at the table with us."
    m 4k "The newspaper club was super grateful for our contributions to today's special edition."
    m 2b "They wanted me to tell you all they say thank you for all the work we've been putting in to help them."
    show monika 2a at t41
    show yuri 1j at f44
    y "That's very kind of them, I'm so glad we get to work along with them with our writing."
    show yuri 2e at t44
    show natsuki 4d at f43
    n "I mean why wouldn't they want the best writers in the school working with them?"
    show natsuki 4a at t43
    show sayori 4x at f42
    s "Yeah! We totally got the best section in the whole paper!"
    show sayori 2q at t42
    show monika 3n at f41
    m "Easy girls, let's not get too ahead of ourselves now."
    m 2e1 "Let's just take today to enjoy ourselves and worry about the paper when we come back on Monday, okay?"
    show monika 2e at t41
    show sayori 4r at f42
    s "Yay, free day again!"
    s 1x "Thanks Monika!"
    show sayori 1q at t42
    show monika 3l at f41
    m "Your welcome Sayori, now let's finish up these delicious cookies."
    show monika 1a at t41
    show yuri 1j at f44
    y "Ah, the tea is ready too!"
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    "Yuri jumps up from her chair and quickly takes the kettle off of the heater and starts to pour us all a cup of tea."
    "Everyone thanks her and we continue to enjoy the tea and cookies as a club."
    show monika 1j at face 
    with dissolve
    "As we're all conversing I could feel Monika scoot up against me and place her head against my shoulder."
    show monika 1c
    mc "Getting comfy?"
    m 1e "Mhmm~"
    extend 1e1 " Best seat in the room right here."
    show monika 1j at thide 
    with dissolve
    hide monika
    "I wrap my arm around her waist and tune back into the conversation."
    show natsuki 2e at t21
    show yuri 2u at t22
    show natsuki at f21
    n "And I said, \"Well if you actually read the manga you would understand the subtle references in the anime!\", but she refused to listen to me!"
    show natsuki 5g at t21
    show yuri 2q at f22
    y "Well, you point them out anyway so I don't really need to read them."
    show yuri 1g at t22
    show natsuki 1v at f21
    n "But still! If I gotta point it out it ruins the magic!"
    show natsuki 5s at t21
    show yuri 1e
    mc "Wait, what anime are we talking about?"
    show natsuki 5r at f21
    show yuri 3o
    n "Parfait Girls! Yuri doesn't get half the references in the show cause she won't read the manga!"
    show natsuki 3i at t21
    show yuri 2q at f22
    y "Well, I just have a lot on my reading list and all."
    show yuri 2e at t22
    show natsuki 3g
    mc "Wait wait wait, your watching an anime with Yuri?"
    show natsuki 3h at f21
    n "Yeah, what about it?"
    show natsuki 4g at t21
    mc "I don't know, just didn't expect it I guess."
    show yuri 1f at f22
    y "Me neither, but Natsuki convinced me to watch a few episodes with her when we had a chance."
    y 2h "And I suppose-"
    show natsuki 1t at f21
    show yuri 3n at t22
    n "She totally loves the show. But I wish she'd read the manga to get the full experience!"
    show natsuki 2a at t21
    show yuri 3q at f22
    y "Well it's not a bad show, but like I said I have a lot to read already."
    show natsuki 2d at f21
    show yuri 2e at t22
    n "Fine, we'll just have to make time then! Come on!"
    show natsuki 1a at t11
    show yuri 2o
    "Natsuki stands up and takes Yuri by the hand."
    show natsuki 1l at f11
    n "We probably have enough time to get through at least one chapter of the manga by the end of club."
    show natsuki 1j at t11
    show yuri 2p at f22
    y "Natsuki wait!"
    show natsuki at lhide
    hide natsuki
    show yuri at lhide
    hide yuri
    "But she didn't, and Natsuki dragged Yuri over to the closet."
    "Quite the dynamic, seeing little Natsuki pull along a taller girl like Yuri."
    show monika 2e1 at t11
    m "I'm glad those two are getting along a lot better now."
    show monika 2e
    "Monika lifted herself off my shoulder and streched her arms out over her head."
    m 2n "I was worried they would stay fighting like cats and dogs forever since you got here [player]."
    show monika 2e
    mc "Well, I guess things change over time."
    m 4k "Yup!"
    show monika 2c
    s "Yeah, it's nice seeing them not fight."
    show monika at t22
    show sayori 1y at l21
    "I look over to Sayori who's still sitting at her seat at the table."
    "She kept looking over her half eaten cookie without taking a bite."
    show sayori 1b
    mc "Is something wrong with that one Sayori?"
    show sayori 2l at f21
    s "Huh? Oh, no it's fine! I guess my eyes were bigger than my stomach today, ehehe~"
    s 2d1 "But um... I'm gonna run to the ladies room real quick okay?"
    s 2r "I'll be back!"
    show sayori at lhide
    hide sayori
    show monika at t11
    "Sayori quickly gets up and steps out of the room before I could even react."
    show monika 1f
    mc "Sayori..."
    "I felt as though I should go after her, but a tug against my jacket kept me seated."
    m 1e1 "I'm sure she's fine [player], don't worry about her."
    show monika 1o
    mc "Are you sure? She never leaves food unfinished like this.."
    m 3n "She just has to go to the bathroom, nothing wrong with that."
    m 1e1 "But while we have a moment..."
    show monika 1j at face 
    with dissolve
    scene black 
    with close_eyes
    "Monika suddenly takes my chin in her hand and plants her lips on mine."
    "After the initial shock I let myself sink into the kiss and wrap my other arm around Monika."
    "Even if we've done this a bunch, it never seemed to get old."
    scene bg club_day 
    with open_eyes
    show monika 1e1 at face 
    with dissolve
    m "I wish everyday was like today, love in the air and nothing pressing on our minds."
    m 1k "Oh wouldn't it just be wonderful, [player]?"
    show monika 1e
    mc "Yeah, I wish we could just stay like this forever."
    m 1e1 "Yeah, me too."
    show monika 1j
    "And there we sat, wrapped in each other's arms until the end of club came."
#C13
    stop music fadeout 2.0
    scene bg bedroom_sunset 
    with dissolve_scene_full
    play music tmonika
    "I stood in the mirror and looked myself over for the tenth time in the last five minutes."
    "This stuffy outfit was absolutely awful to wear but Monika had insisted it was a perfect outfit way back when she went through my closet on a Sunday."
    "I checked the time one more time and took a long, deep breath."
    scene bg livingroom_sunset 
    with wipeleft_scene
    "I made my way downstairs and grabbed the bouquet of flowers I had sitting in a vase for safe keeping."
    "They were beautiful roses, probably the best I had seen in a long time."
    "I made sure to count them one more time to make sure that there were thirteen of them in total."
    "As stupid as the tradition sounded, I didn't want to mess it up and give her an even number of them and doom myself from the start of the date."
    "Today had to be perfect, no matter what."
    "I checked my pockets for everything I needed and stepped out into the world."
    scene bg residential_sunset 
    with wipeleft_scene
    "The setting sun made for a beautiful deep orange haze in the sky as I walked toward the bus station."
    "The walk wasn't long to the bus stop, and thankfully there was a bus close by when I sat on the bench."
    "Though getting on a bus while dressed in my best outfit and holding a bouquet of roses did make me feel a bit self conscious about myself."
    "I just ducked my head down and kept my eyes on my phone."
    scene bg h_residential_sunset 
    with wipeleft_scene
    "Finally I made it to the stop for Monika's place and stepped off the bus."
    "I made my way down the street rerunning the memory of Christmas in my head along with the map I double checked to get to Monika's house."
    "After a short walk I finally made it to the front gate of the house."
    "I know I've been here before, but I still couldn't help but feel a tad bit nervous."
    "Stifling my anxiety, I walked up the pathway and up to the door."
    "I pushed the doorbell and stood back from the door, swallowing some spit and adjusting my tie."
    m "Coming~!"
    "Just the sound of her voice made my heart stop for a second."
    "I heard the click of the lock and I tucked the roses behind my back as the door swung open."
    show monika 1de at t11
    "I could barely believe my own eyes."
    show monika 1dm
    "Monika stood at the doorway in one of the most adorable dresses I had ever seen and I felt myself gasp."
    "She was just... so beautiful..."
    m 3dn "You know, you look really handsome in that tie, [player]."
    show monika 1de
    mc "O-oh, thanks... You look wonderful too, Monika."
    m 2dl "Thank you, it's really nothing though. This is a dress I've had for a long time now."
    m 2dn "I always imagined myself wearing it on a special date so.."
    extend 2de1 " I decided today was as good as a date as ever."
    show monika 2de
    mc "Well I'm.. glad I was the one to have that special date with you."
    m 1de1 "Oh stop it you."
    show monika 1dj at face with dissolve
    "Monika stepped out from the doorway and wrapped her arms around my neck, and I moved my arms around her waist."
    m 1de1 "Come on, we should get going. Wouldn't want to miss our dinner reservation."
    show monika 1dc
    mc "True, but first.."
    show monika 1dd at t11 with dissolve
    "I leaned back a little to show Monika the roses I had in my hand."
    m 1de1 "Oh [player], these are beautiful!"
    m 2dn "Thank you, you really didn't have to."
    show monika 1de
    mc "Well, you shouldn't go on a date without bringing the girl flowers. At least, that's what Dad likes to tell me."
    m 3dl "Ahaha~ Well, he must know how to make your mom happy then."
    show monika 1de
    mc "I'd say he does a pretty good job at it."
    show monika 1da at lhide
    hide monika
    "We both laughed as Monika took a second to put the roses inside, placing them in a vase of her own."
    show monika 3db at l11
    m "Alright, we should probably get going now or else we're going to be really late."
    m 5da1 "Come on, this way."
    scene bg h_residential_sunset 
    with wipeleft_scene
    show monika 1dj at l11
    "We stepped back onto the sidewalk and made our way back to the bus stop."
    show monika 1dm at t11
    "The cool February air wrapped around us and forced us to clutch to our coats tightly."
    "The walk to the bus stop wasn't too bad, but once we stopped moving and sat at the bench the cold started to get to me."
    show monika 1de
    "I pulled Monika in tightly against me in an attempt to keep her warm, and she returned the notion with a hug of her own."
    m 1de1 "Your so warm [player], can we stay like this?"
    show monika 1dm
    mc "Of course, I don't want you to catch a cold."
    show monika 1dj
    "Monika rested her head against my shoulder as we waited, and soon enough another bus came to pick us up."
    scene bg downtown1_night 
    with wipeleft_scene
    show monika 1dc at l11
    "Soon enough we made it into downtown just as the sun finally set."
    "The city lights illuminated our eyes and the area around us."
    m 1dd "Wow, it all looks so pretty at night, no matter how many times I see it!"
    show monika 1da
    mc "I know! It's all so mesmerizing."
    show monika 3dl
    m "Well don't get too caught up in it, we need to go!"
    show monika 1de
    "Monika grabs my hand and we start making our way toward our venue."
    if dinnervar == 1:  #<-- Sapphire Star
        scene bg downtown2_night 
        with wipeleft_scene
        show monika 1dj at l11
        "As we walked along the main strip, the Sapphire Star glowed a deep shade of blue in the distance."
        m 3dk "Oh [player], I can't wait! I've waited for this moment for what feels like forever!"
        m 1db "Come on, come on!"
        show monika 1dj
        mc "Okay, okay! We don't have to run!"
        "She didn't listen one bit and kept dragging me along with her."
        "I found myself just smiling and laughing as we made our way closer."
        show monika 1dc
        "As we approached the building we found a large line leading out the door of the building."
        m 1dd "Wow, it's really busy here tonight..."
        show monika 2dc
        mc "Yeah, but I got an ace up my sleeve. This way."
        show monika 1dc
        "I took Monika's hand and walked towards the door."
        "I ignored the line and made my way to the door beside the line guarded by one employee with a tablet."
        show monika 1de
        mc "Hello sir, I'd like to check in for a reservation."
        $ s_name = "Door Bouncer"
        s "Name please?"
        mc "[player]."
        show monika 1dd
        s "Splendid, just in the nick of time sir. Please follow me."
        "The gentleman opened the door and waved us inside."
        m 1dg "[player], I thought reservations were super expensive here..."
        show monika 1de
        mc "Don't worry about it, I've got it covered."
        "I tried to pull off as smug as a smile as I could and Monika just shook her head and laughed."
        "It may have taken some serious convincing, but the extra funds from Mom and Dad were really going to come in handy today."
        scene sastar 
        with wipeleft_scene
        show monika 1dd at t11
        "As we entered the building I was completely blown away by the interior."
        "The large aquariums scattered around the dinning area were a sight to behold, all teeming with life."
        "The dining floor also teemed with life, with so many people eating at every table."
        m 1db "Wow~"
        $ s_name = "Waitress"
        show monika 1dc at h11
        s "First time here you two?"
        "A waitress came around behind us and gave us a wide smile."
        m 3dk "Yes actually, this place is so amazing!"
        show monika 2dm
        s "Yeah, we hear that a lot from first time patrons."
        show monika 1da
        s "Well follow me, I'll take you two over to the special student seating area we have."
        "As the waitress and Monika started to walk I felt myself panic slightly."
        "What if there's anyone there that would say something?"
        menu:
            "I decide to..."
            "Stay Quiet":
                "...bite my tongue and follow the two ladies."
                "I mean, who's gonna really start something here of all places."
                "The waitress takes us over to a roped off seating area full of younger faces."
                show monika 1dj at s11
                "We take a seat at one of the open tables, set with red roses and pink upholstery."
                show monika 1da
                s "I'll leave you two with the menus for a minute but first would you like anything to drink?"
                mc "I'll just take a water, please."
                m 1db "Same for me as well."
                show monika 1da
                s "Excellent! I'll be right back."
                show monika 1de
                "She then bows to us, then walks away. I look over to Monika, seeing her smiling warmly at me."
                m 1db "Wow! It's really like how everyone said it was!"
                m 1dk "All the fish swimming around, all the cute decorations! Gosh it's almost overwhelming!"
                show monika 1dj
                mc "That it is, everyone wasn't kidding about this place."
                m 3dp "If you had told me you were bringing me here I would have helped with the reservation though, I feel bad leaving that on you!"
                show monika 1de
                mc "And ruin the surprise? I wouldn't have it."
                show monika 1dd
                "Our waitress returns with our two waters on a small saucer, placing them in front of us."
                show monika 1da
                mc "Thank you very much!"
                s "It's my pleasure. Have you had a chance to look over the menu?"
                m 1dn "I'm still looking... What do you recommend?"
                show monika 1de
                s "Well..."
                show monika 1da
                "She then rattles off all the specials for the night, almost all of them with some kind of romantic name."
                m 3dl "Gosh, that's a lot to choose from..."
                show monika 1dm
                mc "Maybe just a few more minutes?"
                s "Of course. Please, take your time."
                "And with that, she makes haste to another one of the tables."
                "Monika and I mulled over the menu. Hoping for something to catch our eyes."
                m 1de1 "Anything jumping out at you, [player]?"
                show monika 1de
                mc "Nothing immediately..."
                show monika 1dm
                "Of course there were a bunch of safe bet meals like burgers and steaks, but I was trying to find something Monika could eat."
                "Didn't help that half the menu contained something with meat in it."
                show monika 1da
                "I kept flipping through the menu, until a few voices from behind me caught my attention."
                stop music fadeout 45.0
                $ n_name = "Female Voice"
                $ y_name = "Male Voice"
                n "Oh my god. Is that Monika?"
                y "Huh?"
                y "Woah! It is! I wonder what she's doing here?"
                show monika 1dc
                n "Yeah, and who's that with her?"
                y "Who knows..."
                "I tried to block it out by focusing harder, but my mind had dialed into their conversation now."
                show monika 1df
                "Monika must have seen my contorted face and leaned over to me and whispered."
                m 1dg "Are you okay, [player]?"
                show monika 1df
                mc "Yeah, I'm fine. Just fine."
                show monika 1do
                n "Whoever that is, Monika's WAY too good for him."
                y "Tell me about it! He looks like a loser!"
                show monika 1dq
                n "Maybe Monika is pity-dating him?"
                show monika 1do
                "That fucking bitch..."
                m 1dg "[player], please..."
                y "Ha, what a little-"
                show monika 1dq
                play music t7
                mc "Hey, shut the fuck up will you?"
                "I whipped my head around and looked straight at the two sitting a couple tables away."
                "Almost every table in a 5 foot radius immediately went quiet as I stared down the guy."
                y "Oh ho ho, so he was listening the whole time?"
                n "Brad... can we not do this right now?"
                "We both stared each other down for a long 20 seconds before the guy turned back toward his date."
                n "{i}Fuckin' loser...{/i}"
                "I tried to take a deep breath but Monika was already whisper screaming at me too."
                m 1di "{i}[player]! What was that for!{/i}"
                show monika 1dh
                mc "I'm.. sorry, I just couldn't stand them talking like that."
                m 1dr "[player]..."
                show monika 1dq
                "Monika seemed to sink into her seat and I started to notice the new spotlight on us."
                "Everyone seemed to be staring at us now and I could feel my cheeks heat up as I looked down at the menu."
                "{i}Nice going [player], had to make a scene huh?{/i}"
                s "Is everything okay here?"
                show monika 1dc
                "Our waitress seemed to appear out of nowhere, looking around with a confused face."
                m 1dl "Oh no, nothing is wrong everything is fine! Ahaha~"
                s "Wonderful! So, have we decided on what to get tonight?"
                show monika 1dm
                mc "I'll just do the house special burger..."
                "We tried to enjoy our dinner, but the pressing feeling of everyone watching our every move was crippling."
                stop music fadeout 2.0
                scene bg downtown2_night 
                with dissolve_scene_full
                play music t8
                show monika 1dq at l11
                "It felt like as soon as we got in, we were done eating and back out onto the sidewalk."
                m 1di "[player]."
                show monika 1dh
                mc "I know, I know, I'm sorry."
                m 1di "Sorry isn't gonna cut it! Why did you do that?!"
                show monika 1dq
                mc "I was mad, okay?!"
                mc "I'm so sick of everyone talking behind our backs like that! Saying we aren't meant for eachother!"
                mc "I just..."
                m 1dr "I know, I heard them too and I wasn't terribly happy to hear it either but I didn't try and start a fight with them!"
                m 1dp "Let's just go."
                show monika 1dq at lhide
                hide monika
                "Monika started off ahead of me toward the main station."
                mc "Monika! Come on!"
                jump e2bad
            "Say Something":
                "...clear my throat and call out to the waitress."
                show monika 2dc
                mc "Um.. actually miss, could we maybe sit in the regular dining area?"
                s "Oh! Well of course, if that's what you two want to do."
                m 2dg "Um.."
                show monika 2df
                "Monika looks at me confused, with a face of, \"What do you mean?!\"."
                show monika 1de
                "I squeeze her hand in a way of saying, \"Trust me\"."
                m 1de1 "Yes, regular dining would be great please."
                show monika 1de
                s "Okay, let me go check with the seating chart to see what's open."
                show monika 1do
                "The girl walks off and Monika turns to me."
                m 1dp "But why are we-"
                show monika 1dd
                mc "Trust me, I just want to avoid anyone from school for tonight."
                show monika 1dc
                mc "I want to spend time with you, just you."
                show monika 1dm
                "Monika stops for a moment and contemplates."
                m 3dn "Your right, we should probably avoid anyone for tonight."
                m 1de1 "Nice quick thinking, [player]."
                show monika 1dj
                "Monika gives me a kiss on the cheek just as the waitress comes back over."
                show monika 1da
                s "I just got a table clean for you two if you would follow me please."
                "Monika and I followed, now holding hands along the way."
                show monika 1dj at s11
                "The waitress guided us to the main dining area, decorated lightly with hearts and pink all around."
                "Definitely not as much as the student area looked to be, but that's fine with me."
                show monika 1da
                s "Alright! What can I get you to drink?"
                m 1db "I'd like a water, please."
                show monika 1dj
                mc "Same for me, thank you."
                s "No problem! I'll be right back."
                "The waitress then leaves us, grabbing our drinks."
                show monika 1dd
                "Monika looks around the restaurant with warm eyes and a face of pure curiosity."
                m 3dk "Gosh, its all so pretty!"
                m 1dl "All the fish swimming around, all the cute decorations! Gosh it's almost overwhelming!"
                show monika 1de
                mc "It really is, everyone wasn't kidding about this place."
                m 1dp "If you had told me you were bringing me here I would have helped with the reservation though, I feel bad leaving that on you!"
                show monika 1dm
                mc "And ruin the surprise? I wouldn't have it."
                show monika 1dc
                "Our waitress returns with our two waters on a small saucer, placing them in front of us."
                show monika 1da
                mc "Thank you very much!"
                s "It's my pleasure. Have you had a chance to look over the menu?"
                m 1dl "I'm still looking... What do you recommend?"
                show monika 1de
                s "Well..."
                show monika 1da
                "She then rattles off all the specials for the night, almost all of them with some kind of romantic name."
                m 3dn "That's a lot to choose from..."
                show monika 1dm
                mc "Maybe just a few more minutes?"
                s "Of course. Please, take your time."
                "And with that, she makes haste to another one of the tables."
                "Monika and I mulled over the menu. Hoping for something to catch our eyes."
                m 1de1 "Anything jumping out at you, [player]?"
                show monika 1de
                mc "Nothing immediately..."
                "Of course there were a bunch of safe bet meals like burgers and steaks, but I was trying to find something Monika could eat."
                "Didn't help that half the menu contained something with meat in it."
                m 1db "Hmm... that cauliflower parmesan looks pretty good, maybe I'll have that."
                show monika 1dc
                mc "Alright, I'll have that as well."
                m 1dd "You don't have to [player], I wouldn't want to stop you from getting something you want."
                m 3de1 "What about their steaks? Those burgers sounded really delicious too if they had the vegan-friendly burgers."
                show monika 1de
                mc "But I want to try something vegetarian with you today, it's not everyday we get to share a fancy meal like this."
                m 1de1 "[player], that's really sweet of you."
                m 1dl "Gosh your gonna make me blush, ahaha~"
                show monika 1dm
                mc "I try my best, and I'll trust your instincts on what is good this time."
                m 1de1 "I just hope you like it though, I'd hate to have you get something you don't like."
                show monika 1de
                mc "I'll get something else in that case, no big deal."
                "My wallet cried out silently as I said that, but I just ignored it."
                show monika 1dc
                "Soon enough the waitress came back around to us."
                s "So, have we decided?"
                m 3db "Yes! Can we have two orders of the cauliflower parmesan please?"
                show monika 1da
                s "Sounds good! Will there be anything else with that?"
                mc "No thank you, that will be all for now."
                show monika 1dj
                s "Perfect, I'll get that right out to you two!"
                "She then grabs our menus and leaves."
                m 1de1 "I promise [player], your gonna love it!"
                show monika 1dm
                mc "I know, if your having it the dish must be good."
                "At least, I hope it is..."
                show monika 1dj
                "The parmesan actually wasn't as bad as I had expected."
                show monika 1db
                "We ate our meal and happily chatted all through the cozy night."
                show monika 1dk
                "Monika had even convinced me to split a special Valentine's day cheesecake with her, against my wallet's protests."
                "But the look of joy on her face from it now made it all worth it"
                scene bg downtown2_night with wipeleft_scene
                show monika 1dj at l11
                "Back out into the city streets, we happily strolled through the crowd without a care in the world."
                m 3dk "Oh that was just wonderful [player]! Like I had always dreamed of this place!"
                m 1de1 "Thank you, thank you, a thousand times thank you!"
                show monika 1dj at face with dissolve
                "Monika basically jumped on top of me, giving me a huge hug."
                mc "Your welcome Monika, I should be thanking you for making my night too."
                show monika 1de
                mc "It probably would have been another night in front of the computer if you weren't with me."
                m 1de1 "Aww, stop [player]! I wouldn't want my perfect boyfriend to be alone on Valentine's Day!"
                show monika 1db at t11 with dissolve
                m "Come on, let's head back to my place!"
                show monika at lhide
                hide monika
                "Monika grabbed my arm and started walking toward the bus station."
                "Wait, did she say her place?"
                jump e2good
    else:
        scene bg downtown3_night 
        with wipeleft_scene
        show monika 1dj at l11
        "As we moved away from the main strip the crowds started to fizzle out."
        "This made our walk to the little brick building just that much easier."
        m 4dk "So we ended up coming here after all, huh? Ahaha~"
        show monika 2de
        mc "It's a good place! And a lot easier to get into than the Sapphire Star."
        m 2dn "True, I guess it would be pretty crowded over there tonight."
        show monika 2de
        mc "But here we can enjoy the night together, without all the hassle."
        m 2de1 "Yeah today is about us, not whatever silly restaurant we go to."
        show monika 1da
        mc "Exactly, it's about us tonight."
        show monika 1dj at face 
        with dissolve
        "I wrap my arm around Monika as we close the distance and she returns the hug."
        scene bg g55 
        with wipeleft_scene
        show monika 2dd at l11
        "As we make our way through the door we were greeted with a wave of noise and the smell of fresh cooking."
        "The place was busy no doubt, with people eating and laughing all around."
        "A stout woman comes over to us as we enter, greeting us with a hearty voice."
        $ s_name = "Waitress"
        show monika 1dc at h11
        s "Welcome, welcome! Did you make a reservation or has the love in the air brought you two lovelies in?"
        show monika 1dm
        mc "Reservation actually, it's under [player]."
        show monika 1de
        s "Let me see here then sweetheart."
        s "Hmm... nope, nope, ah! [player]! Yes, here you are."
        show monika 1da
        s "Follow me you two, right this way."
        scene bg g55c 
        with wipeleft_scene
        show monika 1dc at l11
        "The woman leads us into a side room that's filled with a couple tables but not sat in by anyone."
        s "My, I guess you picked the right time to come! You two have the whole room to yourselves!"
        show monika 1da at s11
        s "I'll leave you two with the menus for a moment. What shall I get you two to drink, a bottle of red or white wine perhaps?"
        m 3dn "Oh um, maybe just water for me please, ahaha~"
        show monika 1dm
        mc "Me too, we're uh.."
        s "Oh my, you two are so big I almost thought you were adults! My oh my, kids grow so big nowadays!"
        show monika 1de
        s "My apologies, I'll grab you some water then."
        "The waitress starts to go toward the door out of the room, but stops just before leaving."
        show monika 1dc
        s "But I'll still leave the offer if you two want just a little."
        "She leaves the room laughing and closes the door behind her."
        m 3dn "Gosh, what an interesting person, huh [player]?"
        show monika 1dm
        mc "Yeah, very interesting I guess."
        show monika 1de
        "I feel my eyes wander around the room and find it's covered in all kinds of pictures, news articles, and memorabilia."
        "Headlines reading \"Romagnian Air Force dominates the skies!\" and \"Fighter Ace Lucchini wins hearts and minds over Romagna!\" scatter the walls."
        "Accompanying the articles were black and white pictures of old fighter planes and the same young girl in almost all of them."
        m 3de1 "Admiring the decor, [player]?"
        show monika 1de
        mc "Huh? Oh yeah, just taking it in."
        m 1dk "I could tell, ahaha~!"
        m 1db "It all looks like it's from one of the big wars way back when."
        m 3dd "And that girl there.."
        show monika 3dc
        "Monika points to a large portrait of the girl from all the pictures."
        m 1dd "She must have been really important back then."
        show monika 1dc
        s "Important is an understatement my dears."
        "We both nearly jumped up as the waitress came back and set out drinks down on the table."
        show monika 1dm
        s "Oh! Sorry to startle you two like that, I couldn't help but listen in on your conversation."
        show monika 1dc
        s "That there is who we like to call Little Miss Lucchini, one of the biggest names in the family."
        m 1dd "Oh, what did she do?"
        show monika 1dc
        s "Well, she was in the war way back when. One of the few women able to fly back then, and fly something fierce she did."
        s "Made the news back then all the time back in Romagna, helped win hearts and minds of everyone back home."
        show monika 1da
        s "After the war she moved here and started up this little abode, but never hung up her flying gloves for a minute."
        s "Her flying stunts made this place the talk of the city. No one could say they hadn't tried out Little Miss Lucchini's cookin'."
        m 1db "Wow, that's amazing!"
        show monika 1df
        s "It sure was, but sadly before your time hun. I'm sure you both would've loved to see her fly in person."
        s "But enough with the sappy story, what am I gonna get you two from the kitchen?"
        show monika 1de
        mc "Oh um..."
        m 3dn "Gosh, I think we spent all this time looking at the decorations."
        show monika 1dm
        s "No worries, take your time. I'll go check on my other tables and come right back."
        show monika 1de
        "The waitress walked off again and we were left to ourselves."
        m 1de1 "So, is there anything that catches your eye [player]?"
        show monika 1de
        mc "Huh, I'm not sure..."
        "The menu contained mostly pasta dishes that sounded fancy yet unfilling at best."
        "I'm tempted to pick from their small list of burgers that sounded okay."
        m 1db "Ooo, this looks good [player]!"
        m 3db "It's called the \"Giro di Romagna\", it has a small dish of almost everything!"
        m 3dk"That sounds perfect for tonight!"
        show monika 1dj
        mc "Oh, let me look."
        "I flipped over to the first page and looked over the meal."
        "{i}A tour of the wonderful homeland! A choice of 5 dishes that will show you cuisine from all over Romagna!{/i}"
        "The dishes sounded good but I was a little hesitant on the price of the meal."
        "It was priced pretty high, more than I was originally ready to spend tonight."
        "I'll have to ask Mom and Dad for a little more money to cover it all."
        "They'd probably give me hell if I asked for more money tonight..."
        "Though as I look up at Monika I can't help but feel guilty for thinking that."
        "Valentine's only comes once a year right? But still..."
        menu:
            "I guess I'll just..."
            "Get the meal":
                show monika 1da
                mc "Yeah, that sounds great! We can get that."
                m 1dk "Really? Oh your the best [player]!"
                show monika 1dj
                "Monika's smile immediately extinguished any worry I had."
                "I'd take the fall any day to see her smile like that."
                "I quickly slid my phone out of my pocket and typed out a quick message to Dad while we waited."
                "He wasn't terribly happy to hear I needed more money, but I promised I'd do some extra work around the house to make up for it."
                "As soon as Dad agreed, our waitress came back."
                show monika 1da
                s "So, have we got our minds made up?"
                m 3db "Yes, we'd like to get the Giro di Romagna please, but without the meat in the lasagna if you could."
                show monika 1da
                s "My my, you two have taste! I'll put it in right away."
                s "I'll also tell the chief about the lasagna for you dear, he does have a lovely cheese recipe so I'll tell the boys to make that for you two if that's okay?"
                m 1db "Yes, that would be wonderful, thank you!"
                show monika 1da
                s "No problem dear, now let me get these out of your way here."
                "The waitress happily took our menus and made her way out of the room once again."
                m 1dk "Thank you [player], this is gonna be so delicious!"
                show monika 1dj
                mc "Anything for you Monika, it is a special occasion after all."
                m 3de1 "Oh stop, you're too much."
                show monika 1de
                "I rested my hands up on the table and Monika lifted up her's to meet them."
                show monika 1db
                "We talked for a while admiring the decorations again until the food was ready."
                show monika 1dj
                "And it was worth the money, all of it as delicious as could be."
                "The fall I'll take for this will be most certainly worth it."
                scene bg downtown2_night 
                with wipeleft_scene
                show monika 1dj at l11
                "I paid the bill and we happily made our way out to the street again."
                m 4dk "Oh what a lovely night it's been, hasn't it [player]?"
                show monika 1da
                mc "Yup, couldn't have asked for a better night with the girl I love."
                m 2de1 "Me neither!"
                show monika 1dj at face with dissolve
                scene black with dissolve
                "Monika wrapped her arms around me and planted her lips square on mine."
                "I felt myself melt into the kiss and that all too familiar feeling came rushing back."
                "The warmth of her lips against mine, the way we held each other so tight."
                "It just made the moment that much better."
                scene bg downtown2_night 
                with dissolve
                show monika 1de at face 
                with dissolve
                show monika 3dl at t11
                m "You know, your lips tasted a little like pasta sauce, ahaha~"
                show monika 1de
                mc "Oh, whoops. Guess I missed a spot huh?"
                m 2dn "Don't worry, I got it for you silly."
                m 1db "Come on, let's head back."
                show monika 1dj at lhide
                hide monika
                "Monika took my hand in her's and we started to make our way back to the bus station."
                jump e2good
            "Go with something cheaper":
                show monika 1dc
                mc "Oh ..um.. how about something else Monika?"
                m 1dg "Hmm? Why something else?"
                show monika 1df
                mc "Well... I don't know, I think the plates are gonna be too small to really enjoy and for that much.."
                m 1dp "Oh, alright I'll try something else then."
                m 3de1"I'll keep the price in mind for you too, [player]."
                show monika 1dm
                mc "You don't have to do that, I just..."
                m 1dn "It's okay, I understand."
                show monika 1dm
                "We looked at the menu a bit more, but I couldn't help but feel a bit guilty."
                "It's not my fault the price is so high! But still..."
                show monika 1dc
                "Our waitress finally came back through the door and walked over to us."
                show monika 1da
                s "So my dears, what will you be having?"
                m 3db "I'll have the Islander Parmigiana please."
                show monika 1da
                mc "And I'll take the.. uh.."
                mc "Glamorous Burger, I guess."
                s "Alright, I'll get that right over to you two!"
                show monika 1de
                "The waitress took our menus and happily walked out of the room once again."
                show monika 1do
                "I looked over at Monika and noticed a slight frown."
                mc "The parmigiana sounded good, what's in it?"
                m 3dn "Oh, just some eggplant, cheese, and tomato sauce."
                m 1dp "It sounded okay, I guess..."
                m 1de1"Your's sounded interesting too."
                show monika 1de
                mc "Oh, yeah I guess just went with something meaty."
                show monika 1df
                mc "Probably shouldn't have but..."
                m 3dg "What do you mean? If you wanted it then there's nothing wrong with getting it."
                show monika 1de
                mc "I know, but it was more force of habit than anything."
                show monika 1do
                "I had wanted to get something vegetarian to impress Monika but it completely slipped my mind."
                "Just one bad choice after another, God damn it all."
                "After a while we got our food, but the atmosphere just seemed to sour the taste of it all."
                "Monika seemed uninterested in her meal and I just felt guilty with mine."
                "The joy that we had before seemed to have vanished."
                scene bg downtown2_night 
                with wipeleft_scene
                show monika 2do at l11
                "I paid the bill when we were done and made our way out to the sidewalk."
                "Monika had been cheery with the waitress as we left, but once we were alone she kept a slight frown on her face."
                show monika 1dc
                mc "Hey, is something up?"
                m 2dn "Huh? Oh it's nothing [player], really."
                show monika 1dm
                mc "Are you sure? You just look a little upset I guess.."
                m 4de1 "No I'm fine, just a little tired is all."
                m 4dk "Why don't we head back now, get out of this cold?"
                show monika 1dm
                mc "Oh, okay.."
                show monika at lhide
                hide monika
                "Monika started to make her way to the station, just staying a little bit ahead of me."
                jump e2bad
label e2good:
    scene bg h_residential_night 
    with dissolve_scene_full
    "The ride back was nice and comfortable, with Monika keeping me warm as she layed her head on my shoulder and wrapped herself up in my arm."
    play music t6
    show monika 1dj at face 
    with dissolve
    "I felt myself look at her and my mouth opened without a thought against it."
    show monika 1de
    mc "Monika, can I ask you something?"
    m 3de1 "Hmm, yeah what's up [player]?"
    "I can't help but speak the burning question on my mind."
    stop music fadeout 1.0
    play music t9

    show monika 1dc
    mc "Why did you pick me of all people."
    mc "You had the world at your fingertips and you choose a guy like me."
    m 1dg "What do you mean [player]?"
    show monika 1bf
    mc "Just...{w=.85} why {i}me?{/i}"
    mc "You were such an icon at school, almost everyone knew who you were."
    mc "And you knew so many different people."
    mc "So many better looking and smart talking guys."
    mc "So many guys adored you, would have done anything to get your affection."
    show monika 1dm
    mc "But you chose a nobody like me."
    mc "And I've caused you enough problems as it is."
    m 1bn "[player]..."
    show monika 1de
    mc "I've never really understood it Monika."
    m 1dn "Well...{w=1.0} it's because you were different [player]."
    show monika 1de
    mc "How? How could someone like me be different?"
    m 1dn "I'll be honest, there has been a lot of guys, gosh even some girls who tried to ask me out."
    m 1dp "But even when they asked me, it all felt so cold and uncaring."
    m 1dr "They wanted me because I was this treasure everyone wanted to have, a goal to gloat about to the rest of the student body."
    m 1dp "No one cared to learn about me, to really understand my dreams and asperations. They just went surface deep to get what they wanted."
    m 1de1 "But when I met you [player], I saw something different."
    show monika 1de
    mc "What could you have possibly seen in me, Monika?"
    m 1dk "I saw a passionate and kind person, someone who cared about the things he loved."
    m 1de1 "Someone that took the time to really meet the people around him."
    m 3dk "[player], do you remember the first time we met?"
    show monika 1dj
    mc "Yeah, that one class we had together last year."
    "It's a hazy memory, that year there hadn't been anything that memorable to me."
    "But I guess there was things that I should have remembered better."
    "I mentally kick myself for letting it slip."
    m 2dn "You were such a sweetheart to me, and you never treated me like I was someone you couldn't approach."
    m "It was just so,{w=.75} refreshing to say the least."
    show monika 2dc
    mc "But I was just being myself and being respectful."
    mc "Hell, I was probably shaking in my shoes subconsciously, I wasn't being anything special."
    m 1de "And that's what made you seem so nice [player], you were genuine where so many others were not."
    m 1dn "And over time I just..."
    show monika 1dm
    mc "Just.. what, Monika?"
    m 1dn "I kind of...{w=.75} grew a bit of a crush on you, even back then."
    m 1dl "Ahaha~"
    "I can't even believe my own ears."
    "She had even liked me before I had ever joined the club?"
    "But I was so...{w=.5} average."
    mc "B-but why didn't you ever talk to me more than in class then?"
    m 1dg "Well.. I was scared [player]."
    m 1dr "You've heard what rumors have spread about us over these past months."
    m "I didn't know if I could do it back then."
    m 1dp "Put that reputation I had held to such a high standard at risk."
    m "All for some crush on a boy I barely even knew at the time."
    m 1be1 "But when you joined the club, and I learned more about you, and you even wrote poems for me..."
    show monika 1de
    "A small tear starts to grow in each of her emerald eyes."
    m 1de1 "I just couldn't handle it anymore. I just had to tell you how I felt."
    m 1bp "I didn't want to be...{w=.5} alone anymore."
    m "I didn't want to lose you to the others."
    m 1dn "You had known Sayori for so long I was sure you would have just grown closer and closer and eventually become a couple."
    m "And if that didn't happen, I thought Yuri's more mature...{w=.75} nature {w=.5}or Natsuki's cuteness would have grabbed your attention."
    m 1bp "I was scared I was still the unapproachable popular girl I had made myself out to be."
    m 1bg "That I would have to sit and watch someone I truly came to love move to someone else."
    mc "Monika..."
    scene black
    with close_eyes
    "I pull her into a tight embrace."
    m "I love you so much [player], I'm so glad I had the chance to tell you how I felt, to be with you by your side."
    m "You mean so much to me."
    "Her voice breaks and she starts to silently sob into my chest."
    "They weren't tears of sadness, but ones of pure unbridled happiness."
    "Those same tears made their way streaming down my face as well."
    mc "I love you so much Monika, you truly are the light of my world."
    mc "What did I ever do to deserve you."
    "We stay locked like this, softly wiping the other's tears away until they pass."
    "When I could finally feel the waterworks end, I leaned in and gave Monika one more kiss."
    "She really was a match made in the stars for me."
    "That's the only way this could have ever happened."
    scene h_residential_night 
    with open_eyes
    show monika 1de at face 
    with dissolve
    "After what feels like forever and an instant both at once, we pull our lips apart but stay intertwined in each others arms."
    show monika 1dc
    "The bus intercom made a small beep, reminding us that we were still on our way back to Monika's house."
    mc "Gosh, any longer and we would have missed our stop."
    m 1dn "That wouldn't have been so bad, spending a little more time cuddled up here."
    show monika 1de
    mc "Yeah, maybe just a little more."
    "We both snuggled up for a bit more until we finally reached our stop."
    show monika 1dj at t11 with 
    dissolve
    "It was almost painful to have to get up and walk back out into the cold after being warm for a while."
    "Thankfully the walk wasn't too long and soon enough we made it to Monika's place."
    show monika 3db at l11
    m "Come on [player], this way."
    show monika 1da
    mc "Wait, we're going inside?"
    m 4dn "Yeah, Mom and Dad are away tonight. Probably out in some casino suite for the night drinking and gambling the night away."
    show monika 2dm
    mc "B-but would they be happy if I-"
    m 5da1 "Shh [player], it's fine. Trust me."
    show monika 1dj at lhide
    hide monika
    "Monika giggled as she opened the door and we went inside."
    scene bg h_livingroom_night 
    with wipeleft_scene
    show monika 1dj at l11
    "We made our way into the living room and finally got rid of those bulky coats."
    m 3de1 "Hey, why don't we watch a movie? Something romantic and cheesy?"
    show monika 2dm
    mc "Never took you for someone who watched those Monika."
    m 2dn "I usually don't, they're so predictable and boring if I'm being honest."
    m 4dl "But its Valentine's Day! We're supposed to do cheesy stuff, ahaha~!"
    show monika 2de
    mc "Yeah, I guess your right on that one."
    show monika 1dj at s11
    "Monika giggled as we sat down on the couch, flipping on the television and looking through all the romance movies."
    show monika 1da
    "We finally settled on some overly cheesy Valentine's Day movie and we got comfortable."
    show monika 1de at face 
    with dissolve
    "Monika made sure to get nice and comfy on me, nearly laying on me while holding onto me tightly."
    "I couldn't complain, it all felt so surreal I almost couldn't belive it."
    show monika 1dj
    "Spending Valentine's Day with Monika like this, I could have only dreamed of it only a few months ago and now it was my reality."
    "I couldn't have asked for anything more if I tried."
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    stop music fadeout 2.0
    jump Monika4 #<-- This will be used if we skip the lewd scene. If we do get the lewd scene comment out the jump here and use the lines below \/
    "I nearly nodded off to sleep before I felt Monika get up from me."
    m "Hey, I'm just gonna run upstairs real quick."
    m "Just keep an ear out for if I call you, okay?"
    mc "O-oh, okay Monika."
    m "Okay! Stay right here, ahaha~!"
    "Monika quickly got up and scooted upstairs, sheepishly hiding her face."
    "What is she plotting now?"
    "I decided to tab back into the movie for a little bit, the story was pretty boring but it helped keep my attention away from Monika for a bit."
    m "Oh [player], can you come here~?"
    "I couldn't help but chuckle to myself at the sound of Monika's voice."
    "What is she planning now?"
    "I shook my head and stood up from the couch."
    jump m_lewd2
label e2bad:
    scene bg h_residential_night 
    with dissolve_scene_full
    "The ride back was awkward at least, and almost unbearable at most."
    show monika 1do at t11
    "Monika was nearly unresponsive on the ride home, keeping a small but painfully noticeable distance between us."
    "I tried to talk to on the bus but she only answered with short answers, shooting down any conversation."
    "After a short walk from the bus stop we finally reached Monika's place"
    m 1de1 "Well.. thank you for taking me out tonight [player]."
    show monika 1dm
    mc "Ah.. your welcome Monika, I'm.. glad you came with me. Even if..."
    m 1dp "Yeah.."
    show monika 1do
    "An awkward silence gripped the air between us, almost choking the life from me."
    mc "I guess.. I should head back home now."
    m 1de1 "Wouldn't want you to get cold, or make my parents mad by having a boy over ahaha~"
    show monika 1dm at face with dissolve
    "I extend my arms for a hug and Monika returns the hug, but there was an obvious awkwardness to it."
    show monika 1de at t11
    mc "I guess.. I'll see you at school then?"
    m 1de1 "Yup, I'll see you there, [player]."
    m 1dp "..Take care."
    show monika 1do at lhide
    hide monika
    "Monika turns around and walks up to her door, entering and closing it behind her without looking back."
    "I sigh and start my way back to the bus."
    "{i}Good fucking job [player], went and screwed up the whole night like you knew you would.{/i}"
    "{i}Way to ruin a day like today up so spectacularly.{/i}"
    "I refrained from yelling out in anger at myself as I walked, I didn't need to make myself look even worse to any onlookers."
    "I sink my hands into my pockets and slink back towards the bus stop, looking back to Monika's place for a moment."
    "Next time Monika, I promise I won't mess it up."
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    stop music fadeout 2.0
    jump Monika4