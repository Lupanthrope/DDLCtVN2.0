label m_event1:
    #C1 16th
    #====TESTING, DELETE BEFORE RELEASE=====
    menu:
        "SayoriVar=1":
            $ SayoriVar = 1
        "SayoriVar=0":
            $ SayoriVar = 0

    #=======================================
    stop music fadeout 2.0
    scene black with dissolve_scene_full
    scene white with open_eyes
    "I wake up to the sun shining through the window directly at my face."
    "I can’t see very well, but I feel something soft against one of my arms."
    play music mend
    scene m_cg1 with dissolve_cg
    "I look over to see a naked Monika sleeping right next to me."
    "I can’t help but gasp in surprise. So that wasn’t a dream."
    "We really...{w=.75} did that, huh?"
    "I inch my arm out from under her body in an attempt to escape, trying not to wake her up."
    show m_cg2 at cgfade
    "The effort was in vain, as she begins to stir and open her eyes."
    show m_cg3 at cgfade
    m "Oh, good morning~!"
    hide m_cg3
    show m_cg1 at cgfade
    stop music fadeout 5.0
    "Her words trail off as she nearly falls back asleep."
    hide m_cg1
    show m_cg4 at cgfade
    "However she bolts back up almost immediately, with a look of sheer terror on her face."
    play music t7
    show m_cg5 at cgfade
    m "Oh... oh no."
    mc "What?"
    m "This is bad."
    mc "What's bad...{w=.75} I don't-{nw}"
    show m_cg6 at cgfade
    m "[player], I’m gonna be in a lot of trouble."
    mc "Wait, what?"
    m "Aside from the fact it’s Monday and I don’t have my uniform, I never returned home last night."
    mc "This can’t be the first time that’s happened, right?"
    m "Well...{w=.75} this is a whole different story."
    show m_cg7 at cgfade
    m "How long do we have until homeroom?!"
    play sound fall
    scene black
    with wipeleft_scene
    "Before I can answer she jumps out of the bed, throwing the blanket over my face."
    m "I’m so sorry [player] I really need to go right now. I’ll text you later!"
    scene bg bedroom with wipeleft_scene
    "Before I can even get the gears in my brain moving and the blanket off my face, Monika is already dressed and bolting out my door."
    "I'm left star-struck in my bed."
    mc "{i}What...just happened?{/i}"
    "Forcing my limbs to move against their will, I slowly prop my naked body from my bed."
    "I check the time, still early enough for breakfast but not much else."
    "The air around me still has a ting of last night's {i}event,{/i} so a shower is definitely in order."
    stop music fadeout 2.0
    scene bg residential_day
    with wipeleft_scene
    play music t8
    "After I finish freshening up and eating my quick and mediocre breakfast, I take to the streets."
    "Sayori is nowhere to be found, and it's usually around the time she walks to school."
    "I shrug it off and make my way to school."
    scene bg class_day with wipeleft_scene
    "The day goes by uneventfully."
    "Monika is tough to find throughout the day like a phantom."
    "Even in our shared classes she seemed to be running some errand for a teacher or just outright missing."
    "The final bell rings and I make my way to the clubroom with hopes of catching this ghost."
    scene bg corridor with wipeleft_scene
    "The crowded hallways pulsed with life as students came and went, but no white bow showed through the masses."
    scene bg club_day with wipeleft_scene
    "I enter to see club activities proceeding as usual. That is, whatever can be considered \"club activities\" when we're not sharing poems."
    "However, there's a sense of emptiness to the room."
    "While Yuri is reading a large book as normal, and Natsuki is reading manga as usual, Sayori is staring into space sitting at the desk Monika normally sits."
    "I decide to approach her about this."
    show sayori 1o at t11 zorder 1
    mc "Hey, Sayori!"
    show sayori at h11
    s 4p "Uwaah~!?"
    s 2o "[player]!?"
    show sayori 1n
    mc "So uh, whatcha doin in the President's seat?"
    s 2h "Oh uh, Monika..."
    extend 1k "she said she wouldn't be able to make it to club."
    s 2l "She was going to cancel it but I thought that'd be a waste."
    s 4x "So as Vice President I thought I should act as Club President for the day and let activities run as usual."
    s 1h "Do you know why she almost cancelled though, [player]?"
    show sayori 1g
    mc "N-not really, I'm just as surprised as you are."
    s 2h "You don't? I hope she's okay..."
    show sayori 1g
    mc "I'm sure she's fine, I saw her a couple times today."
    show sayori at thide zorder 1
    hide sayori
    "I'm...{w=1} sure it's fine..."
    "I take a seat in my normal spot and try to entertain myself."
    "Even as I take out a book Monika recommended me, I can't help but wander off in my mind."
    "What's with all this dodging around, Monika?"
    "What did I do..."
    "After what seemed like forever Sayori dismisses us all for the day."
    show sayori 2x at t11
    s "Hey [player], why don't we walk home together!"
    s 5b "I know that you usually go with Monika but..."
    s 5a "She isn't here and all, and..."
    show sayori 1n
    mc "Yeah sure, I wouldn't mind."
    s 4r "Yay! Ehehe~"
    scene bg residential_day with wipeleft_scene
    show sayori 1y at l11
    "The bright sun helped to keep us warm as we walked along the sidewalk."
    "Sayori was unusually quiet for most of the walk however."
    "She spent most of it trying to dodge my eyes whenever I looked over and sparking short conversations."
    "Soon enough though I could make out our houses in the distance."
    show sayori 2r
    s "Thanks again for walking with me, [player]!"
    s 1x "It feels like it's been forever."
    show sayori 1b
    mc "Well you know you can always walk with us Sayori, I'm sure Monika wouldn't mind."
    s 2y "No no, it's fine. You two look cute together anyway."
    s 2l "I wouldn't wanna ruin it for you..."
    mc "Sayori what do you-{w=1}{nw}"
    s 4r "Oh look, we're home!"
    s 2x "Talk to you later, [player]!"
    show sayori at lhide
    hide sayori
    mc "Sayori!"
    "She's already skipping off to her house by the time I yell out her name."
    "What did she mean by \"ruin it\"?"
    "As I look for my key, I look at my phone once again."
    "Still nothing from Monika today..."
    "Did I mess up that bad last night? Maybe it was too early or..."
    "I just don't know..."
    stop music fadeout 2.0
#C2 17th - Anniversary
    scene bg class_day
    with dissolve_scene_full
    play music t6
    "Monika is silent once again during all of our shared morning classes, I don’t think she spoke a word even once. If she did, I would have remembered."
    "She seemed as if she wasn't in this reality at all, almost like she was in her own little world."
    "And here I was, worried out of my mind of what was wrong."
    show monika 2m at t11 zorder 1
    "Lunch rolls around and without me noticing she came to my side and tugged on my sleeve with a sly grin."
    show monika at lhide
    hide monika
    "She silently takes me with her to a part of the school I tend to avoid."
    scene bg rooftop
    with wipeleft_scene
    show monika 1m at t11
    show monika at s11
    "She sits me down on a bench on the school rooftop and out of her backpack comes about twice as much lunch as she should have."
    m 3n "I've heard about this sort of cliche before in the anime you watch, where the girl pretends she \"accidentally\" made too much lunch and suddenly has to share it with her crush."
    m 3e1 "So I thought I'd try it out for you, to see how you liked it."
    show monika 1m
    "She hands me half of her lunch, and I remain dumbfounded."
    m 1p "You're not...{w=.75} mad at me or anything, right?"
    show monika 1e
    mc "W-what no, no."
    extend " I'm just really surprised is all. Thank you."
    mc "You didn't have to Monika."
    m 2n "I kinda feel like I do, after yesterday."
    m 1r "It was just...{w=.75} one of those days for me."
    show monika 1q
    mc "Oh um, I hope it wasn't...{w=.5} my fault or anything..."
    m 1e1 "No, not at all [player]."
    m 3n "It was actually a pretty good way to celebrate our anniversary."
    show monika 2m
    mc "Wait, anniversary?"
    show monika 1c
    m 3b "Yeah, Sunday was our 4th sunday and therefore 4th week together so one month, but today is exactly one calendar month since we started dating."
    show monika 1a
    mc "Wow, it hasn't even felt like a month."
    m 2n "I know right, I almost forgot about it myself. Ahaha~"
    m 2k "But I'm glad I realized it though, it just makes that night that much more special."
    show monika 1c
    mc "So you don't regret it or anything? I-i didn't mess up at all?"
    m 1d "Of course not! Don't think things like that, [player]."
    m 1e1 "That was one of the best nights of my life so far, spending it so close with the one I love."
    show monika 1f
    mc "M-me too. Sorry, I was just a bit worried..."
    m 1g "Worried about what?"
    show monika 1f
    mc "I don't know, that I maybe had really screwed up our relationship somehow."
    m 1e1"No [player], the only thing you did was..."
    show monika 1k at face with dissolve
    m "Make my love for you stronger~"
    show monika 1j
    "All my worries melt away in her arms as we hold each other against the winter air."
    show monika 1m at t11 with dissolve
    show monika at s11
    "Monika moves away after a while and looks off and thinks for a moment."
    m 1n "Well I imagine it won't be {i}the{/i} best night of my life for much longer."
    m 2l "Still pretty far up there, ahaha~"
    mc "W-what do you mean Monika?"
    m 1b "Did you forget the time of year? [player], Christmas is in a week! Remember, you're going to come over to my house this time."
    show monika 1c
    mc "Wait what, A WEEK?! And when did we say anything about going over?!"
    m 1k "Ahaha~ You're adorable when you get surprised [player]."
    m 1l "Don't you remember, you said you wanted to come over and spend it with me and my family."
    "Did I? I must have just went along with her and wasn't really paying attention."
    "I need to get her a gift too! All of this time and I only now realize this!"
    m 1k "I already have the {i}best{/i} gift ready for you, [player]~"
    show monika 1j
    mc "What!?"
    m 1k "Not telling, ahaha~."
    show monika 1j
    "Monika hums cheerfully, reminding me oddly of Sayori. This is unexpected from her, she must be {i}really{/i} happy today."
    show monika 1c
    "She turns back to me with a curious expression on her face."
    m 3d "Something on you mind dear?"
    show monika 1e
    mc "Ah- no, I'm just.. thinking about how happy I am to be with you."
    show monika 1a
    "Monika beams a warm smile at me, but I can tell she saw through me."
    m 1c "{i}Hmm…{/i}"
    "My newly found anxiety must be showing on my face, even as I desperately try and play it cool."
    m 1d "If there's anything wrong you know you can talk to me about it, right?"
    show monika 1c
    mc "I know, I'm fine right now though."
    m 1q "..."
    m 1d "Oh!"
    mc "Huh?"
    "She looks as though something just clicked in her head."
    m 3k "I see.. I see~! I gotcha now!"
    show monika 1j
    mc "Huh? What are you talking about?"
    m 4k "Nothing~"
    show monika 1l
    "If she really figured me out that fast, I'm in real trouble."
    "The rest of our lunch is spent peacefully eating the food she packed, my own lunch is entirely forgotten."
    scene bg class_day
    with wipeleft_scene
    "We seperate for our classes after lunch, and all of my doubtful thoughts are finally gone."
    "Monika is back to her normal self and today is gonna be a lot better than I had thought it would have this morning."
    "I feel like I can finally breath again and smile."
    scene bg corridor with dissolve_scene_full
    "Soon enough my favorite class of the afternoon comes into view, computer science."
    "Not necessarily because I'm hugely invested in the subject, but..."
    scene bg class_day with wipeleft_scene
    show monika 1j at t11 zorder 2
    pause .75
    show monika at s11
    "As if on cue Monika suddenly appears by my side and pulls back her chair, taking a seat next to me."
    m 3k "Hi [player], nice to see you again! Ahaha~"
    m 2b "How'd your other classes go this afternoon?"
    show monika 2e
    mc "Uh...they sure were classes alright."
    m 2n "Uh huh, I bet they were."
    show monika 2m
    "She smirks slightly and shakes her head."
    m 4e1 "Just make sure you at least pass [player]."
    extend 2l " It would be a little awkward if you got stuck here for another year."
    show monika 2e
    mc "Don't you worry, I'll get the most respectable C- possible in all of them, maybe even a C+ if I feel extra enthused."
    show monika 2m
    "I chuckle a bit, but still a part of wonders if I should take school a little more seriously."
    "After all, what would it say about me if I can't do at least decent while she's the schools' valedictorian?"
    m 3k "Well not in this class you won't, I better not catch you slacking!"
    show monika 1c
    mc "Oh really? A little ironic of you to say considering I tanked my grade on the last project in this class to save your butt."
    m 1n "Oh right, that project..."
    extend 3e1 "you're still the best boyfriend ever for that, by the way."
    m 2b "I'll make it up to you I promise,"
    extend 3k " and I'll start by telling you to quit that game you're tabbed out of!"
    show monika 2j
    "Damn, she knows I already got that open and the class just started."
    mc "Alright, alright, I'll actually do some work today."
    show monika 1a
    "I close the game and bring up my work for the next big project I'm supposed to be working on."
    "It's supposed to be our final project, a culmination of everything we've learned this year."
    "Thankfully we got to choose how we wanted to use all of our knowledge in the form of our own project."
    "Me being the model student of my time, I took the absolute easiest route with a simple logic program that could take votes and make a desision."
    "However our teacher wanted us to make a proposal to her about the project to get her approval."
    show monika 1c
    "Even with my genius plan, I'm reminded that my current progress consists of my name and the class number in the top right corner of the proposal."
    show monika 1e
    "Monika glances over at my screen and sighs a bit."
    m 3e1 "You know [player] I'd be happy to help you out if you'd like."
    show monika 1e
    "That would probably be for the best...but would I really concentrate on work with Monika helping me?"
    "Eh, not like I can ever focus on it anyways."
    mc "Um, I'll think about it Monika, for now I'll just get started with my prompt though."
    m 2b "Okay sounds good."
    extend 1k " And remember,{w=.5}{nw}"
    extend 3e1" no video games."
    m 2k "I'll be watching you, [player]."
    show monika 1a
    mc "Yeah yeah, I know."
    show monika 1j
    "We both turn back to our monitors and get to work."
    "After a little while I actually manage to make some progress with my prompt."
    "But as I'm working I can't help but sneak a few glances at Monika."
    show monika 1m
    "She's facing slightly away from me with her own work open on her computer."
    "Her project so far seems to be coming along quite well, with impeccable organization and effort that anyone would expect from her"
    "Except…"
    "It seems to be coming along a little slower than usual at the moment."
    "In fact as I continue to watch, I notice she hardly ever types anything or changes tabs."
    "Instead she mostly just seems to be fidgeting with her binder."
    "Which is a little bizarre considering we almost never get any paper handouts in this class."
    "What the heck is she up to?"
    "Unable to resist my curiosity, I slowly lean over to my side towards her."
    "I still can't really see what she's doing so I decide to lean a bit closer, making sure to keep quiet so she doesn't notice me"
    "At this point my head is only mere centimeters away from hers."
    "Her familiar perfume fills my nose and I couldn't help but smile, that perfect aroma I'm so used to but always seems to impress me."
    "I snap out of my trance and take another good look at her binder and realize..."
    "She's on her phone."
    "The perfect class star is texting in class, and trying to hide it from the teacher."
    "I smirk to myself."
    show monika 1j at face with dissolve
    "Before I even have time to remark to myself, Monika tilts her head to the side pinning my head between hers and her shoulder in a sort of head lock."
    show monika 1k
    "She giggles softly."
    m 1n "You know it's not very nice to just stick your head in someone's personal space, [player]."
    show monika 1j
    "I instinctively try to pull back but she just wraps her arms around my arm and pulls me even closer."
    m 1k "Good thing you're someone I like in my personal space though, ahaha~"
    show monika 1j
    "I immediately feel all flustered, I can't believe she'd do this right in the middle of class."
    "I want to try and think of something snarky to say but my mind draws a blank."
    "I quickly stop trying to resist and just decide to enjoy the moment."
    "Sitting here, resting against Monika and focusing on her breathe over the clacking of keyboards and student chatter."
    "It really seems to take my mind off of everything else."
    "I relax my arm that she's holding, and it slowly begins to slide down until my hand is resting on her thigh."
    "She moves one of her hands down and rests it on top of mine, gently massaging it while nuzzling against me some more, purring happily."
    "Times like this make me wish it was just Monika in my life."
    "We remain like this for a few more moments before I hear some other kids snickering behind us."
    "The fact that we're in class finally finishes sinking in, a small class albeit but a class with other people around nonetheless."
    show monika 1c
    "I finally pull back and sit up in my chair, blushing softly."
    show monika 1m
    "Monika must have heard them too."
    show monika 1n at t11
    pause .25
    show monika at s11
    m 1n"Aww, but I was having so much fun."
    extend 1e1 " I guess we'll have to pick up from there later then."
    m 1h2 "And since you \"so rudely,\" interrupted me, I think it's only fair that you owe me a little extra next time."
    show monika 1h1
    mc "But it wasn't even my fault!"
    show monika 1k
    "She winks at me and giggles more."
    "And though I can't see it for myself, she gives me the distinct impression that my blush has intensified."
    show monika 1j
    mc "Ah... and do you really have to say this stuff so loud?"
    "In retrospect I think she actually whispered it but my embarrassment is making me think otherwise."
    m 1e1 "I guess not, but it is just way too fun to look at your face right now."
    show monika 2e
    "I rest my head in my arms on my desk and face away from her."
    "Only then does my slow head remember why any of this even happened in the first place."
    "I sit back and look at her."
    show monika 2c
    mc "Hey you might have distracted me for a bit but not anymore."
    mc "What the heck was the all wonderful class star herself doing texting on her phone?"
    show monika 2m
    mc "I thought it was time to take work seriously."
    "I smile deviously and cross my arms, I could finally tease her about something."
    m 1n "W-what do you mean? I wasn't texting anybody or anything like that."
    show monika 1m
    "She tries to discreetly move her arm to further block my view of where I know her phone is."
    mc "Uh huh nice try, I saw it already."
    mc "I'm an expert on sneaking peeks at my phone during class, you can't fool me."
    show monika 1l
    "Monika sighs and shakes her head."
    m 3e1 "Fine you caught me, and for the record that isn't exactly a skill I'd go bragging about."
    show monika 1m
    mc "Well it sure is a useful one."
    mc "Anyways come on spill it, I'm {i}dying{/i} to know just what could be so important as to make the great Monika break an official classroom rule for it."
    "I put a little extra emphasis on that last part."
    m 2n "Well I'm only human after all, I got a little excited okay."
    m 4e1 "I was going over some plans a friend of mine proposed."
    m 2k "I think I've got an interesting idea for the club coming up."
    show monika 2a
    "A development in the club? Come to think of it we haven't really done anything significant since the festival disaster."
    mc "Well you've certainly got my attention now."
    mc "What are we going to do?"
    m 5a "Hmm... "
    extend 5a1 "well you'll just have to wait and see."
    m 2n "I'm still working out the details and everything so its not set in stone yet."
    m 3b "And I want to surprise everyone at club at the same time."
    show monika 1m
    mc "Oh come on you can't even tell me?"
    mc "After Sayori I'm basically the vice vice president."
    show monika 1l
    "Monika raises an eyebrow when I say this then laughs."
    m 3n "Maybe, though I wouldn't be so sure about it."
    show monika 1m
    "I raise my eyebrow back."
    mc "Hey what's that supposed to mean?"
    m 3e1 "Well I mean, Sayori is still vice president."
    m 2d "Natsuki is great at getting down to business when we need to."
    m 1k "And Yuri sure knows a bunch about literature, even surprising me sometimes."
    m 5a1 "And I mean, you're in the club too."
    show monika 5a
    "She gives me another one of those taunting winks that she knows presses all of my buttons."
    show monika 2m
    mc "Oh come on, Yuri would never want any power at all except the power to say no to any form of literature presentations."
    mc "And if Natsuki was in charge our headaches after a week would be too severe for us to get any reading or writing done at all."
    mc "I can't possibly be that far down the chain of command."
    m 1e1 "Well, as a word of advice from one current leader to an aspiring one."
    m 4e1 "Smart remarks doesn't usually put you in line for a promotion."
    show monika 2m
    mc "Oh of course how silly of me."
    mc "Please accept my most humble apologies ma'am."
    "There totally was not a speck of sarcasm in my voice there."
    m 2n "Oh [player]..."
    m 2l "Apology accepted for now."
    m 3b "But anyways, there's only a couple hours left of classes."
    m 2k"I guess you'll just have to wait and see."
    show monika 1j
    mc "Fine fine, I'll be patient."
    show monika at thide zorder 1
    hide monika
    "We both return to our work and the bell rings shortly after."
    stop music fadeout 2.0
    scene bg corridor
    with dissolve_scene_full
    play music t3
    "After another few classes the final bell rings and with it comes another glorious day at the literature club."
    "Unfortunately I am a little late to the club though."
    "The teacher for my last class had me stay and talk to her for a bit."
    "Something about...not doing my homework or something?"
    "I don't really know, I sort of just nodded and said \"Yes ma'am\" and \"I'm sorry ma'am\" whenever she expected me to reply."
    show bg club_day
    with wipeleft_scene
    "I quickly move through the door into the club room, excited to hear the announcement from Monika."
    "But instead I walk straight into Natsuki..."
    play sound fall
    show natsuki 1v at face with dissolve
    n "AAAHHH HEY!"
    show natsuki 4x at t11
    "Having nearly fallen over from my bumping into her, Natsuki struggles to regain her balance for a second."
    n 1p "What the heck [player]! Can't you watch where you're going?!"
    n 5p "What's with the rush anyways?!"
    show natsuki 5o
    mc "S-sorry Natsuki, I didn't realize you were there."
    mc "I was just really excited to hear what Monika had to say and-"
    show natsuki 5k at t21 zorder 2
    show sayori 4p at t22 zorder 3
    show sayori at f22
    s "SSSHHH SHUSH SHUSH SHUSH!!"
    s 3o "I've almost got it...hmm…"
    show natsuki 4c
    show sayori at t22
    "I look past Natsuki and notice that Sayori is staring at the white board at the front of the room."
    show natsuki 3z
    "Natsuki clasps her hand over her mouth to stifle a laugh."
    "I stand dumbfounded for a moment untill I put together the pieces."
    "It seemes there was a game of Scribbles up on the board where someone, presumably Natsuki, put a picture and some blank spaces for Sayori to figure out what it was."
    "Up on the board was a crudely drawn little monster with a big cookie in it's mouth and a big red bow on it's head."
    "Sayori had an S at the begining and an I at the end of the blank spaces, solidifying my guess as to what Natsuki had drawn."
    "I just stand there with my hands behind my back trying not to chuckle. Poor Sayori."
    "With a bit of fumbling through diffrent ideas, Sayori finally filled in her own name into the spots and stepped back."
    show sayori 3r at f22
    s "Look, my name fits in the spot! Ehehe~"
    show sayori 1q at t22 zorder 2
    show natsuki 2l at f21 zorder 3
    n "Yup. Congratulations Sayori, {i}you win{/i}."
    show natsuki 2j at t21 zorder 2
    show sayori 4r at f22 zorder 3
    s "HA! Told you I'd win, hehehe!"
    show sayori 1q at t22
    "Sayori stands there with a triumphant grin on her face."
    "I'll never understand how one girl can be so clueless and innocent…"
    "But then it seems to hit her..."
    s 3m "Huh..."
    extend 4m "Hey wait a second!"
    s 4p "Aahh! That's really mean Natsuki, that doesn't look like me at all!"
    show sayori 1f at t22 zorder 2
    show natsuki at f21 zorder 3
    n 4z "Hahaha! Oh come on Sayori learn to take a joke."
    n 5d "Besides, you're still the winner. Remember?"
    show natsuki 5c at t21 zorder 3
    show sayori 2h at f22 zorder 3
    s "[player] don't just stand there like a robot, say something!"
    show sayori 1i at t22
    show natsuki 3a
    mc "Uh I mean...It was kinda funny...just a little bit."
    "Sayori seems as if she's trying to pout some more... "
    show sayori 3s
    show natsuki 3l
    extend "but eventually lets out a few giggles herself."
    show sayori 4s at f22
    show natsuki 3j
    s "Hehe, that's true, and it's totally worth it!"
    show sayori 1q at t22
    "I wonder if it's even possible for Sayori to stay upset with anyone for more than 5 seconds."
    stop music fadeout 2.0
    show sayori 1q at f42 zorder 2
    show natsuki 1c at h21 zorder 3
    play music t7
    "Before I could even open my mouth, Sayori quickly hops over to Natsuki and yanks her into a big hug from behind."
    show natsuki 1o
    "Natsuki visibly blushes and growls."
    show sayori at t42 zorder 2
    show natsuki at f21 zorder 3
    n 1q "Okay okay, we've hugged now that's enough, sheesh."
    show natsuki 1i
    "Natsuki tries to push Sayori off of her but Sayori is much stronger than she is and refuses to let go."
    show natsuki at t21 zorder 3
    show sayori 4s at hf42 zorder 2
    s "Ehehehe, you're the cutest little thing ever Natsuki!"
    show sayori 4q at t42 zorder 2
    show natsuki 1w at f21 zorder 3
    n "For the last time, I am not cute!"
    n 5p "Come on [player], you owe me for bumping into me earlier so get her off!"
    show natsuki 1r
    "Though Natsuki can't see Sayori's face from the position they're in, I can."
    show sayori 4i at t32
    "Sayori's typical giddy smile had transformed into something more devious than I'm used too."
    "The look she is giving me is also giving off a huge, \"stay out of this,\" vibe."
    show sayori 4q at t42
    show natsuki 1o
    "But is it worse than the \"you better do something right now,\" kind of look I'm getting from Natsuki?"
    menu:
        "What should I do?"
        "Help Natsuki with Sayori":
            #If player chooses to help Natsuki…
            "Realistically if I don't help Natsuki now I'll end up in worse trouble sometime down the road."
            mc "Haha, okay Sayori I think she's learned her lesson, better let her go before you suffocate her."
            show natsuki at t21
            show sayori 4j at f32
            s "Hmph."
            show sayori 4q at t42
            "What kind of look was that?"
            show natsuki at f21
            n 5v "I swear Sayori if you don't listen to him I will hurt you, I don't care how goofy or innocent you think you are!"
            show natsuki 1r at t21
            mc "Okay let's just take it easy girls, please!"
            "I move over to them and start trying to pry Sayori's arms off of Natsuki, which is sort of like trying to defuse a bomb at the moment."
            "This girl is actually a lot stronger than she looks…"
            "I start trying to use a little more force while the two of them keep whining."
            show sayori at t43
            show natsuki at t32
            "Sayori starts to back up to get me away and we follow her..."
            "Until Sayori slips on some loose paper on the floor and we all go tumbling down."
            show sayori 1p at s43
            show natsuki 1v at s32
            play sound "sfx/fall2.ogg"
            $ m_name = "Sayori and Natsuki"
            m "AAHH!"
            $ m_name = "Monika"
            show sayori 1d at t43
            show natsuki 1g at t42
            "We all fumble around on the ground for a bit before getting up and collecting ourselves."
            show natsuki 1h at t21 zorder 2
            show sayori 1e at t22 zorder 3
            "Natsuki immediately dashes behind a few desks to put something between her and Sayori, taking deep breaths the whole time."
            mc "Whoa! Okay, that got a little crazy."
            mc "Is everyone okay at least?"
            show sayori 1y at t33 zorder 3
            show natsuki 1i at t32 zorder 3
            show yuri 3n at l31 zorder 3
            "Yuri suddenly runs over to see what happened."
            y 3p "What just happened?! Is anyone hurt?"
            show yuri 3u
            mc "We're fine, at least Sayori and I are, what about you Natsuki?"
            show yuri 3s at t31 zorder 2
            show natsuki 5h at f32 zorder 3
            n "I'm…{i}pants{/i}... I'm okay, I just need some personal space for a bit."
            show natsuki 5q at t32
            show yuri 3o
            "Natsuki trembles a bit and just focuses on breathing."
            show natsuki 1p at f32
            show yuri 3n
            show sayori 1e
            n "What the heck was that all about Sayori!"
            n 1w "You didn't have to attack me over a stupid game of Scribbles!"
            show natsuki 2i at t32
            show sayori 2l at f33
            show yuri 2g
            s "I was just giving you a hug silly! Nothing bad!"
            show sayori 1b at t33
            show natsuki 4h at f32
            n "That was no hug and you know it."
            show natsuki 4g at t32
            show sayori 2j at f33
            s "Well you were the one being a meanie! That picture wasn't very nice!"
            show sayori 1i at t33
            "This is getting serious, I need to say something.."
            show natsuki at t31
            show yuri 2k at f32
            y "Ladies please, this is getting quite out of hand."
            "Wait, did she just read my mind?"
            show sayori 1n
            show natsuki 1c
            y 2r "Whatever happened here was quite ridiculous, and you all could have been hurt!"
            y "No more rough housing from now on!"
            y 1l "Fighting will only make things worse so maybe we should try making amends over each others mistakes instead?"
            show yuri 1m at t32
            show natsuki 1k
            show sayori 1c
            "We all stand there a little stunned."
            "It's so rare to see Yuri so vocal and stern, we all stop and gape at her."
            show yuri 2p at f32 zorder 2
            y "Uwah.. did I just yell all that? I'm sorry, I was just so concerned I..."
            show yuri 3o at t32
            mc "No, it's fine Yuri. We were just suprised.."
            show sayori 2h at f33 zorder 3
            s "Natsuki... I'm really sorry I made you upset."
            s 1k "I don't know what came over me, I just..."
            show sayori 1e at t33 zorder 2
            show natsuki 1m at f31 zorder 3
            n "It's..."
            extend 2q "it's okay, no worries Sayori."
            extend 2u " I suppose I sort of deserved it anyways, I'm sorry too."
            show natsuki 2n at t31 zorder 2
            show sayori 2d1 at f33 zorder 3
            s "No worries to you too."
            s 4r "Time for a make up hug!"
            show natsuki 1p
            show sayori 4p
            show yuri 2p
            "Natsuki quickly dashes behind another desk and I grab Sayori by the arm."
            show sayori 5d at f33
            show natsuki 1i
            show yuri 2u
            s "Sheesh, I was just kidding you guys."
            show sayori 5b at t33
            "I can't help but chuckle at Sayori's devious giddiness."
            mc "Haha, yeah, very funny Sayori."
            show yuri 2q
            show natsuki 4t
            "We all share an admittedly somewhat awkward laugh then move towards the center of the club to sit together."
            stop music fadeout 1
        "Stay out of this":
            #If player choices to stay out of the situation…
            $ SayoriVar += 1
            mc "Uh… you know, I just remembered that I have some very important club duties to attend to right now so... talk to you later!"
            show natsuki 1v at thide zorder 1
            hide natsuki
            show sayori 4r at thide zorder 1
            hide sayori
            n "You traitor! You bastard!"
            "I turn away and make my way towards the farthest point from the front of the room."
            "That would maybe help drown out the threats and obscenities I'm hearing from Natsuki at the moment."
            show yuri 2i at t11
            "However before I get very far I notice Yuri sitting in her usual corner of the room."
            "She's reading from some new book I don't recognize."
            "I decide to see how she's doing."
            "I wonder if she even noticed any of what was going on with Sayori, Natsuki, and me."
            "We got pretty loud so I really don't see how anyone so close could have tuned us out entirely."
            "Then again, it is Yuri and she is reading."
            mc "Hey Yuri. How's it going?"
            show yuri 3p at h11
            y "Ah!"
            show yuri 3n
            mc "Oh gosh, I'm sorry! I didn't mean to scare you like that."
            y 2w "I-Its okay [player], I was just really enjoying my book and didn't notice you walking up."
            y 1q "Anyway, how are you?"
            show yuri 2s
            mc "I'm doing alright, I guess. Might not be later if Natsuki ever gets free but I'll just have to keep my fingers crossed haha..."
            y 1q "Oh right, I couldn't help but overhear a bit of...whatever that was."
            y 2v "Natsuki sounded quite irritated."
            show yuri 2g
            "Hmm, I guess even Yuri's concentration is only so powerful then."
            show yuri 1e
            mc "Ah she'll live, she always gets over stuff quick-ish."
            y 2h "I-I suppose…"
            show yuri 2g
            "Yuri's voice trails off a bit and she averts her gaze."
            "She also seems to be stuttering more than usual and she's breathing somewhat heavily."
            show yuri 2e
            mc "Hey Yuri are you feeling okay? You seem a little off."
            y 2n "O-off?"
            y 3p "{cps=*1.1}{i}I'm sorry if I'm acting too weird or making you uncomfortable, I don't mean to I just sometimes can't help myself please don't-{/i}{/cps}{nw}"
            show yuri 3o
            mc "Yuri, Yuri slow down a bit."
            "I put my hand on her shoulder."
            show yuri 2n
            mc "Yuri, you aren't weird and I feel fine. You just seem a little tense that's all."
            mc "Did something happen?"
            show yuri 2w
            "Yuri takes a few deep breaths and seems to relax a bit."
            y 2j "I see…"
            y 1v "It's nothing really, I just had to give a really long oral report for history which was my last class."
            y 2w "It was a pretty serious project that my class had been working on for awhile."
            y 2t "It had me stressing out for week after week after week and I had to present after a few kids from the speech and debate club."
            show yuri 2s
            mc "Jeez, that does seem a little uncomfortable."
            mc "But hey, at least it's all in the past now right?"
            y 2w "Yes I suppose it is."
            y 1t "I just hope my grade doesn't suffer from my awful performance though."
            y 1v "The vocal presentation counted for almost half the grade."
            y 3w "And I kept stuttering and looking away from everyone."
            y 4d "Aaahhh, it was so embarrassing!"
            show yuri 4b
            mc "I'm sure you did fine, the presentation might have been a little rough but everyone knows you're a genius."
            mc "From my point of view it's a safe bet that the content of the presentation more than compensated."
            show yuri 4a
            mc "And besides we all get nervous sometimes, but not all of us can look good when it happens."
            show y 4e at t11 zorder 2
            "Yuri shys away a bit and blushes, though I can still notice a faint smile growing across her lips."
            "I just meant to lighten the mood but somehow I feel that I just brought in a different kind of uncomfortable."
            y 3q "You know [player], you shouldn't say things like that so casually."
            y 2j "What if Monika just so happened to walk in while you were speaking and you didn't notice."
            show yuri 2a
            mc "Uhh…"
            "I hold my breath and very slowly turn around…"
            show yuri 1m
            "And quite fortunately for me, Monika is nowhere to be seen."
            "I do however notice that Sayori has finally shown some mercy and freed Natsuki from her death grip."
            "The two of them seem to be chatting about something but I can't tell what."
            "My train of thought is suddenly interrupted by more giggling from Yuri."
            y 2d "Hahaha, I guess you were right then [player], we all do feel anxiety at times."
            show yuri 1c
            "Only now do I realize how red my face must be."
            "What the heck is going on today?"
            "First Monika teasing me like that in class…"
            "Then Natsuki's pictionary scheme, followed by Sayori's wicked revenge…"
            "And now Yuri's cunning manipulation."
            "Everyone really is just embracing their inner evil genius today I guess."
            show yuri 2i
            mc "Okay, okay, I'll give you that one Yuri."
            show yuri 1c
            "She smiles happily, with a tint of pride."
            y 1d "Why thank you for allowing me to take pleasure at your expense."
            y 1b "I hope you hold no grudge for it."
            show yuri 1a
            mc "Don't worry Yuri its fine. Water under the bridge."
            show yuri 2e
            mc "And speaking of Monika, where is she?"
            "I check my phone and realize almost half of the time for the club has passed since I arrived."
            "I also haven't received any texts from Monika."
            mc "It's not unheard of for her to be late but we've all been here for awhile now."
            y 1f "Hmm, now that you mention it this is rather perplexing."
            y 1h "Are we sure she didn't have to cancel-"
            show yuri 1f at t32 zorder 2
            show natsuki 3a at l31 zorder 2
            show sayori 3a at l33 zorder 2
            "Yuri is abruptly cut off by Natsuki and Sayori as they walk over and take seats in the tables next to us."
    play music t3
    show natsuki 2b at f31 zorder 3
    show sayori 1b
    show yuri 2e
    n "Hey what gives? We've been here forever so where the heck is Monika? I thought something important was supposed to happen here today?"
    show natsuki 2g at t31 zorder 2
    show sayori 1h at f33 zorder 3
    s "Yeah, I was really excited to hear the news! She kept teasing about it in class earlier."
    s 1c "Did she tell you where she is or what this is about, [player]?"
    show sayori 1b at t33
    mc "No she didn't mention a thing to me aside from what you said, just subtly hinted at something happening during the club meeting."
    show sayori 1k at t33 zorder 2
    show natsuki 3r at f31 zorder 3
    show yuri 2g
    n 3r "I swear if I was club president I'd have her writing a dozen extra poems a day just to make up for this."
    show sayori 1b
    n 5y "And yeah nice try [player] but I'm not buying that for one second."
    n 3r "Sayori is right, she kept blabbing that she was excited about something today but refused to spill it. It was written all over her face that she wanted to though."
    n 5h "There is no way she didn't tell you with how obsessed you two have been with each other lately."
    show natsuki 5g at t31 zorder 2
    show yuri 1h at f32 zorder 3
    y "Hmm...Natsuki does have a point."
    extend 1j " Monika did seem quite giddy about something in our class earlier."
    y 1h "Though I don't think [player] would lie, Natsuki."
    show yuri 1i at t32 zorder 2
    show natsuki 3q at f31 zorder 3
    n "Hm, I guess you're right Yuri."
    n 3d "Besides what am I thinking? It's not like he's persuasive at all, he's practically her pet."
    show natsuki 3a at t31
    show sayori 1y
    mc "Hey! We have a perfectly balanced relationship."
    "Natsuki gives me a punch on the arm."
    show natsuki 4t at f31
    n "Yeah okay, you keep trying to convince yourself that you didn't throw your personal life and freedom out the window."
    mc "I mean it's not like she-"
    play sound closet_open
    show sayori 1n at t44 zorder 1
    show yuri 1f at t42 zorder 2
    show natsuki 1k at t43 zorder 3
    show monika 3k at l41 zorder 4
    show monika at f41
    m "Hi everyone so sorry I-!"
    show monika 1c at t41 zorder 2
    show natsuki 2d at f43 zorder 3
    n "Well jeez the club president finally shows herself."
    n 2y "I was starting to wonder if you actually existed."
    show natsuki 2s at t43 zorder 2
    show yuri 1h at f42 zorder 3
    y "It has been quite some time Monika, we were wondering if you cancelled again."
    show yuri 1s at t42 zorder 2
    show monika 2n at f41 zorder 3
    m "Cancel? Oh no, no, no, I absolutely would have notified you all ahead of time."
    show monika 2m at t41 zorder 2
    show sayori 2h at f44 zorder 3
    show natsuki 5g
    s "Well then what took you so long we don't have too much time left for the club?"
    show monika 2e
    s 4m "And what is this big announcement supposed to be?"
    show sayori 1n at hf44 zorder 3
    "Sayori gasps, seemingly remembering the main reason we're all here."
    show natsuki 5c
    show monika 1c
    show yuri 1f
    s 4p "{cps=*2}You know what nevermind I don't care what you were doing, just tell me what it was you kept teasing about earlier!{/cps}"
    s "{cps=*2}I've been waiting for so long I feel like I'm going to pop AAAHHH.{/cps}"
    show sayori 1e at t44 zorder 3
    "Sayori seems to realize that we're all looking at her a little funny and calms down a bit."
    show sayori 5b at f44
    s "And as club vice president, I demand to know right this instant."
    show sayori 1y at t44
    mc "Yeah and I also demand to know 'cause I'm your boyfriend so you uh… have to tell me about these things."
    show natsuki 5z
    "Natsuki chuckles into her hand and smirks."
    show natsuki 5j
    show sayori 1a at t44 zorder 2
    show yuri 1a
    show monika 2n at f41 zorder 3
    m "Okay fine, but only if you all promise not to hurt me after."
    m 2e1 "And better yet I'll explain where I was and what's going on at the same time."
    m 4b "I have just finished arranging our next club project!"
    show monika 2a at t41 zorder 4
    show natsuki 1g at t43 zorder 3
    show yuri 1e at t42 zorder 2
    show sayori 1n at t44 zorder 1
    "We all raise a suspicious eyebrow but keep listening attentively."
    "She's clearly peaked everyone's interests."
    show monika 2b at f41
    m "After the..."
    extend 2n " less than successful festival event we held..."
    extend 3e1 " I figured it would be good for us and for the club to do something to put ourselves out there again."
    m 2d "Not necessarily to recruit new members, I know that we all agreed that we like the ways things are."
    m 4b "Its more so to just grow our reputation, let people know that we're the literature club,"
    extend 4n " and not the \"literal-drama\" club."
    m 2b "So I started brainstorming some ideas before a friend of mine texted me earlier today to make a proposition."
    m 4b "She's the president of the school newspaper club and she asked if we'd be interested in coming up with some sort of literature publication to add to the newspaper!"
    m 3k "It sounded so perfect to me so we texted back and forth for a bit and after class I went to see her to confirm everything, which is why I just showed up."
    m 2n "Admittedly it took a lot longer than I thought, but it was worth it!"
    m 2k "And with all the writing we do, we're going to design a creative writing portfolio with it!"
    m 3b "It's going to be a big collection of some of our best poems or short stories or anything else that we write in the next few months!"
    show monika 2a at t41
    show natsuki 2m at t43 zorder 3
    show yuri 1g at t42 zorder 2
    show sayori 1b at t44 zorder 1
    "Monika stands there with a big smile on her face but everyone else seems a little hesitant."
    show monika 1c at t41 zorder 3
    show natsuki 5q at f43 zorder 4
    n "So let me get this straight."
    n 5k "You started another big group project for us,"
    extend 5q " {i}again{/i}..."
    show monika 1o
    extend 5h "without asking us,"
    extend 5r " {i}again{/i}..."
    extend 5f "and you didn't stop to think that this might be a little uncomfortable for us,"
    extend 4e " {i}AGAIN!{/i}"
    show natsuki 4i at t43 zorder 2
    show monika 1p at f41 zorder 3
    m "Well I just-"
    show monika 1f at t41 zorder 2
    show yuri 2o at f42 zorder 3
    y "I also would have preferred some advanced notice..."
    y 3v "Sharing my work at first was hard enough, now I have to show it to everyone in the school."
    y 2w "Its a lot to take in at once..."
    show yuri 2e at t42 zorder 2
    show monika 1o at f41 zorder 3
    "Monika sighs and droops her head toward the ground."
    m 1p "Gosh, I should have talked to you all about this before going through with it."
    m 1r "I'm really sorry everyone, I didn't mean to make any of you uncomfortable."
    m 1n "We don't have to do this publication if it's too stressful. Like we said, the club is fine as is."
    m 2p "I'll just talk things out with the Newspaper club and everything will be fine."
    show monika 1m at t41
    "Monika gives a small smile to try and lighten the mood but the rest of us stay quiet."
    show monika 1c at t41 zorder 3
    show natsuki 5q at f43 zorder 4
    n "Well..."
    extend 5t "I was really only upset that you went ahead with this idea without telling us."
    n 3d "But I think you ment it when you said you're sorry, and I guess it isn't such a bad idea overall."
    n 3t "It'd be a nice change to show everyone my writing instead of just you guys."
    show natsuki 3j at t43 zorder 3
    show monika 1d at f41 zorder 4
    m "Wait, you mean..."
    show monika 1c at t41 zorder 3
    show natsuki 3k at f43 zorder 4
    n "What do you think Yuri?"
    show natsuki 3j at t43 zorder 3
    show monika at t41 zorder 4
    show yuri 3u at t42
    "Yuri still seems a little on edge about this but not nearly as much as she did Monika told us about the festival plans."
    show yuri 3v at f42 zorder 4
    y "Well Monika did give a sincere apology..."
    extend 3t " and I suppose it wouldn't be so bad."
    y 2h "Yes, but maybe I could leave my poems anonymous. That way if I don't like the work I can deny my involvment."
    y 1j "I could even use a pen name, then if I do like my work I can still take credit for it."
    show yuri 1i at t42
    "We all stand there stunned for a second."
    "Yuri really just agreed to something like this entirely on her own, no peer pressure at all."
    show yuri 2a
    show monika 2e
    mc "You know it does sound sort of fun to do."
    mc "We'd actually be working toward something rather than just sit around like we usually do."
    mc "I say we give it a shot, and if we don't like it we can always stop."
    show natsuki 5a at t43 zorder 3
    show yuri 2a at t42 zorder 2
    show monika 2e1 at f41 zorder 4
    m "Thank you everyone, I'm certainly glad that you all feel that way."
    m 4d "But what about you Sayori, how do you fe-{nw}"
    show monika 1c at t41 zorder 2
    show natsuki at t43 zorder 1
    show yuri at t42 zorder 3
    show sayori 4r at h44 zorder 4
    show sayori at f44
    s "YES! Eeheh!~"
    "Sayori had been pretty quiet for a bit  but can't seem to control her excitement now."
    show monika 2a
    s "I really want to do this, it sounds super fun!"
    s 4l "I was just waiting to see if Yuri and Natsuki would be okay with it..."
    extend 3r " but since they want to do it too I'm super excited!"
    s 1x "It feels like its been forever since we got to work on something together, this will be so much fun!"
    show sayori 2q at t44 zorder 2
    show monika 2e1 at f41 zorder 4
    m "Well then that settles it."
    extend 4b " The first official Literature Club writing publication is now offical!"
    show monika 2a at t41 zorder 4
    show sayori 4r at h44 zorder 2
    s "YAY! Ehehe!~"
    show sayori 3q at t44 zorder 1
    show yuri 2d at f42 zorder 3
    y "With that amount of excitment, I can't help but feel fired up too."
    show yuri 1c at t42 zorder 2
    show natsuki 5l at f43 zorder 3
    n "Yeah, we can do this girls!"
    extend 4d " We'll write the best poems this school will ever see!"
    show natsuki 4a at t43 zorder 2
    show sayori 4r at f44 zorder 3
    s "Ahh I can't help it! Club hug!"
    show sayori 4q at t11 zorder 4
    show yuri 1p at t21 zorder 3
    show natsuki 1p zorder 2
    show monika 1d at t42 zorder 3
    "Sayori runs over and pulls the three of them into a big group hug."
    $ m_name = "Yuri, Nat, and Monika"
    m "Huh?!"
    $ m_name = "Monika"
    show monika 1l
    show yuri 1q
    show natsuki 1s
    "Yuri and Monika seem a little surprised by the sudden hug, but eventually start to laugh along with Sayori."
    "Natsuki was still a little angry about hugs..."
    show natsuki 1t
    extend "but finally gave into the spirit of the group."
    show sayori 4a
    show monika 1a
    show yuri 1a
    show natsuki 1a
    "They all slowly turn to look at me."
    m 1e1 "Well [player], are you just going to keep standing there awkwardly or you going to get over here and join us?"
    show monika 1a
    "She gives me a quick wink."
    mc "Uh...of course!"
    show monika 1j
    show sayori 4s
    show yuri 1d
    show natsuki 1z
    "I walk over and squeeze between Monika and Sayori to join the big hug fiesta."
    "I can't help myself from laughing and eventually we all breakdown into a fit of laughter."
    "I'm glad I decided to stay in this club all those months ago, with members like these girls who wouldn't want to stay."
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    show yuri at thide zorder 1
    hide yuri
    show sayori at thide zorder 1
    hide sayori
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t8
    "We spend a little bit of time brainstorming ideas for the portfolio but it quickly becomes time for everyone to head home."
    "Yuri, Natsuki, and Sayori say their goodbyes and head home."
    show monika 1a at t11 zorder 2
    "Monika and I stay behind to lock up the clubroom."
    m 2k "Gosh this turned out to be such a good day [player], I'm so happy everyone is so excited about the newspaper!"
    show monika 2a
    mc "Yeah it was awesome, I can't wait to read some of the poems we come up with!"
    show monika 2m
    "Monika smiles still but sighs a little bit."
    m 1n "Yeah me too, I just feel a little bad though."
    show monika 1m
    mc "How come?"
    m 2p "Natsuki was right, I didn't think about anyone else again."
    m "I'm the club president, the needs and comfort of my members are supposed to come first."
    m 1g "Its my job to consider them in every choice I make for the club."
    m 2r "But I just went ahead with pushing something I wanted to do before asking anyone."
    m 1g "Am I... just a selfish person [player]?"
    show monika 1f
    mc "No, no of course not Monika!"
    mc "Everyone gets a little selfish sometimes Monika there isn't anything wrong with that."
    show monika 1e
    mc "Besides, you gave a very honest apology and were just excited in the first place."
    mc "No one is mad at you, you're still the only club president we'd want."
    m 1e1 "Thank you [player], I really needed to hear that from you."
    show monika 1j at face with dissolve
    "Monika stepped over to me and wrapped her arms around me, and I happily returned the hug."
    m 1n "Still though, I'll try harder to keep my suprises for you guys to a minimum."
    show monika 1e
    mc "And we'll try and be more understanding."
    m 1k "Gosh, I'm so lucky you're my boyfriend, I don't know what I'd do without you."
    show monika 1j
    scene black with close_eyes
    "She then leans in and grabs my uniform tie, yanking me into a deep kiss."
    "I felt myself melt against her warmth, her lips interweaved with mine."
    scene bg club_day with open_eyes
    show monika 1e at face with dissolve
    "After what felt like an eternity to me, we finally pulled away from each other."
    m 1e1 "So you better not even think about leaving me, okay?"
    show monika 1e
    mc "I couldn't imagine a reason I would want to."
    m 1k "Good, Ahaha~"
    show monika 2j at t11
    "Monika gave me one more peck on the cheek before slipping out of my arms and grabbing her things."
    "I couldn't help but smile as I grabbed mine and lead her out the door."
    show monika at thide zorder 1
    hide monika
    #

#C3 - 19
    scene bg residential_day with dissolve_scene_full
    play music t2
    "Another winter morning has me making my way to school."
    "Sayori has disappeared yet again into the crowd of students walking to school and I can't find her anywhere."
    "I curse under my breath against the bitter cold and trudge to school."
    scene bg corridor with wipeleft_scene
    "On my way to homeroom I hear a passing conversation about Christmas gifts and that sinking feeling hits me again."
    "I need to get her a god damn gift still."
    scene bg class_day with wipeleft_scene
    "Lessons blur together as my mind goes into a panic thinking of potential gifts."
    "Ideas come and go, some seeming like they have some merit to them."
    "Others I dismiss just as fast as I thought of them."
    "I barely even notice the day coming to an end and have to nearly sprint out of class to make it to club."
    scene bg corridor with wipeleft_scene
    "As I step closer to the club, I can feel my anxiety getting worse."
    "{i}Why am I freaking out over a stupid gift?{/i}"
    scene bg club_day with wipeleft_scene
    show yuri 3t at t41 zorder 1
    show sayori 4e at t42 zorder 2
    show monika 1f at t43 zorder 4
    show natsuki 4n at t44 zorder 3
    "It appears my distress is visible to the other club members as I finally enter the room."
    "Everyone has their eyes turned to me, compounding my already unstable state."
    show monika 4g at f43 zorder 4
    m "[player], are you alright?"
    show monika 2f
    mc "Y-yeah, I'm all good."
    mc "Just a...{w=.75} bad last class is all."
    show yuri 2e
    show monika 2c
    show sayori 1b
    show natsuki 2c
    mc "Hey um, the uhhh..."
    extend "Student Council wanted to see you, Monika."
    m 2d "Huh? That's news to me."
    show monika 2c
    mc "Yeah, i-it seemed pretty urgent to me."
    mc "But I guess their goons found me first so they wanted me to pass on the message, haha..."
    mc "Must have known I would see you."
    m 2n "Uh...{w=.75} right.. {w=.75}alright.."
    m 4l "Well, if they need me I better go see what's up."
    m 5a1 "Sayori, you're in charge while I'm gone. It should only be a moment."
    show monika 5a at lhide zorder 1
    hide monika
    show sayori at thide zorder 1
    hide sayori
    show yuri at t21 zorder 3
    show natsuki at t22 zorder 3
    "Monika flashes me a smile before leaving the club room."
    show natsuki 4m at f22 zorder 4
    n "What was that about, [player]?"
    show natsuki 4n at t22 zorder 3
    stop music fadeout 1.0
    play music t7
    mc "Gaaahhh, I need help guys!"
    show yuri 3f at f21 zorder 4
    y "Oh dear, what's wrong [player]?"
    show yuri 3e at t21 zorder 3
    mc "Christmas is coming up soon and I haven't gotten Monika anything!"
    mc "I'm so lost as to what to actually get her."
    show yuri 3k at f21 zorder 4
    y "Hmm, that is quite a problem..."
    show yuri 3e at t21 zorder 3
    show natsuki 4e at f22 zorder 4
    n "Ok, but why did you lie to her so blatantly and send her out like that?"
    n "Only an idiot like {i}you{/i} would fall for a lie like that."
    show natsuki 4g at t22 zorder 3
    mc "I have no idea why she actually went along with it, but I'll take it."
    show natsuki 4e at f22 zorder 4
    n "Well, your sure outta luck here. Your relationship is {i}your{/i} concern, not ours."
    show natsuki 4g at t22 zorder 3
    show yuri 3h at f21 zorder 4
    y "Natsuki, we shouldn't just ignore our friend's problem."
    show yuri 3h at t21 zorder 3
    show natsuki 4e at f22 zorder 4
    n "If he can't figure out what she wants on his own, he's no good as her boyfriend."
    show natsuki 4g at t22 zorder 3
    mc "Ah, well uh-{nw}"
    show yuri 3r at f21 zorder 4
    y "Natsuki!"
    show yuri 3r at t21 zorder 3
    show natsuki 4k at f22 zorder 4
    n "What?"
    show natsuki 4k at t22 zorder 3
    show yuri 3r at f21 zorder 4
    y "You could have worded that in a less harsh manner, [player] is already distressed enough."
    show yuri 3r at t21 zorder 3
    show natsuki 4r at f22 zorder 4
    n "Well harsh is the only way to get things through his thick skull." #--
    n 2h "Why don't you help him, huh Yuri? You got any ideas for gifts?"
    show natsuki 2g at t22 zorder 3
    show yuri 4c at t21 zorder 3
    y "..."
    "Yuri seems to have locked up under her question."
    show natsuki 2e at f22
    n "Exactly. Anyway, don't expect help from me."
    n 4w "This is {i}your{/i} problem [player]."
    $ _history = False
    n 4t "{cps=*1.25}{i}Glad you're not my boyfriend [player], I'd be super upset{/i}{/cps}{nw}"
    $ _history = True
    show natsuki 1p
    mc "What Natsuki?"
    n 1v "Nothing!"
    show natsuki at lhide
    hide natsuki
    show yuri at t11
    "Natsuki storms off in a huff, leaving me with Yuri."
    stop music fadeout 1.5
    play music t2
    y 4d "I-i'm sorry I couldn't think of any advice [player]."
    y 4a "I'm...{w=.75} not really good under pressure."
    show yuri 4b
    mc "It's alright Yuri. Besides, it really should be me figuring out this problem anyway."
    y 1k "A little help never hurts though, and second opinions may help your decision."
    y 2v "But it also shouldn't be us picking your gift for her."
    show yuri 1u
    mc "Of course not! I'm just bad at the whole gift thing sometimes, I don't wanna mess this one up."
    mc "Any kinda help would be a huge blessing at this point."
    show yuri 3e at h11
    s "Uh...{w=.75} er..."
    show yuri at thide zorder 1
    hide yuri
    show sayori at t11 zorder 1

    if SayoriVar >= 1:
        s 5b "I...{w=.75} I have no plans on Saturday, so if you want I can help you look for something then."
        show sayori 1e
        mc "Really? Oh my gosh your the best Sayori!"
        s 2y "Yeah, ehehe~"
        show sayori at lhide zorder 1
        hide sayori
        "Sayori nearly darts to Monika's seat, covering her face."

        $ shoppingvar = 1

    elif SayoriVar < 1:
        s 2e "Ah...{w=.75} I..."
        s 4p "I gotta go to the bathroom!"
        show sayori at lhide zorder 1
        hide sayori
        "Sayori barrels out of the classroom away from the conversation, snuffing out my last light of hope."

        $ shoppingvar = 0
    "As I take my seat in my spot again, Monika returns to the clubroom."
    show monika 4b at l11 zorder 1
    m "Hey, I'm back everyone! Thanks [player] for letting me know about the Student Council needing me."
    show monika 2a
    "Did she actually go all the way over there? I thought my lie was pretty piss poor."
    mc "Uh.. yeah, no problem Monika."
    m 2n "You know, it could have been bad if I didn't get there when I did."
    show monika 2m
    mc "Is everything alright?"
    m 2l "Yup, everything is all sorted out over there."
    show monika 2j
    "I can't tell if she's just humoring me or if there was something they actually needed from her."
    "At this point I'll take any kind of help I can get at this point."
    "Natsuki and Yuri don't wanna help me with the gift, and Sayori..."
    if shoppingvar == 1:
        "At least she's willing to tag along with me shopping for a gift."
        "I knew at least Sayori would pull through and help me out with this."
    elif shoppingvar == 0:
        "Not even she wants to help me with my dilemma, why?"
        "I thought we were best friends..."
    m 4b "Anyway, it's time for poems!"
    show monika 2a
    "B-but I didn't write one?!"
    stop music fadeout 2.0
#C4
    scene bg class_day with dissolve_scene_full
    play music t8
    "The next day was more of the same in class."
    "Though now I wasn't worrying about Monika's silence, but her Christmas gift."
    if shoppingvar == 1:
        "At least I have Sayori to count on tomorrow to provide some help."
        "Yuri was also slightly supportive of helping too, maybe I can convince her..."
        "I've still got a chance at this yet."
    elif shoppingvar == 0:
        "My last ditch effort to get some help yesterday was in vain, no one in the club wanted to help me."
        "Yuri was the only one even slightly sympathetic to me, but she didn't really want to get involved."
        "Man am I ever screwed."
    "The bell rings signaling the end of the day, and the swarm of students make their exodus from their classes."
    "For me, I make my way back up to the club room."
    scene bg corridor with wipeleft_scene
    "As I make my way to the club room, I spot the door open."
    show monika 2a at l11
    "Monika steps out of the club room, humming to herself."
    show monika 2d at h11
    m "Oh [player]!"
    m 2n "I didn't expect you to be here so soon, ahaha~"
    show monika 2m
    mc "Hey, I'm not always {i}that{/i} late."
    show monika 1j at face with dissolve
    "I pull Monika into a hug that she gladly returns the notion."
    show monika 4b at t11
    m "I just have to run down to the Student Council again, shouldn't take too long."
    show monika 2e
    mc "Oh really? That kinda stinks."
    m 2e1 "It isn't so bad, I know a lot of them from my Debate club days."
    m 5a1 "Don't miss me too much [player]~"
    show monika 5a at lhide
    hide monika
    "Monika gives me a quick kiss before making her way down the hallway."
    "This can't be a coincidence that they actually need her two days in a row."
    "Maybe she really is onto my antics..."
    "She really doesn't need to play along though, but I guess I shouldn't look a gift horse in the mouth."
    scene bg club_day with wipeleft_scene
    stop music fadeout 1.5
    play music t3
    "The club room is about how I expected it, with everyone in the same spots that they usually are."
    "Well, besides Natsuki that seemed to notice that I had walked into the club room."
    show natsuki 2y at t11
    n "Ha! I {i}knew{/i} he was too chicken to pull off something like that!"
    mc "Wait, pull off what Natsuki?"
    n 4t "Skip club with Monika and..."
    n "Well..."
    n 1v "You know what, never mind!"
    show natsuki at lhide zorder 1
    hide natsuki
    "Natsuki hides back in the closet again."
    "What on Earth was she going on about?"
    y "Um.. Hi [player]."
    show yuri 3s at t11
    mc "Oh hey Yuri, do you know what Natsuki was on about?"
    y 3q "O-oh well, we should probably not talk about that."
    show yuri 2u
    "Oh? Now I'm {i}really{/i} curious what she was talking about."
    y 1k "Anyway.."
    y 2t "How is the gift dilemma coming along?"
    show yuri 2s
    mc "Still at the same place I was yesterday sadly."
    if shoppingvar == 0:
        mc "At least I have Sayori tomorrow to help me out a bit though."
        "I look over to Sayori, who has her head tucked into her curled arms on Monika's desk."
        y 1d "I'm sure she will be wonderful help [player], her and Monika are great friends."
        show yuri 2s
        mc "I hope so, she tends to get distracted though whenever we used to go shopping for anything."
    elif shoppingvar == 0:
        mc "I was planning on heading to the mall tomorrow and trying my luck there."
        y 1h "It may be very busy tomorrow, with the holidays right around the corner."
        y 2w "All those people..."
        show yuri 3u
        mc "Yeah, would be nice to have at least {i}someone{/i} by me but I'll manage."
    y 2g "You know, I don't really have anything too pressing to do tomorrow..."
    y 1h "And it does get a tad bit dull sitting around the house..."
    show yuri 1e
    mc "Wait, would you wanna help tomorrow?"
    y 3q "W-well I'm still not sure and all, I was just t-thinking out loud and..."
    show yuri 3n
    n "Is he {i}still{/i} talking about that {i}stupid gift?!{/i}"
    show yuri at t22
    show natsuki 1p at l21
    show natsuki at f21
    n "What did I tell you yesterday?! None of us care!"
    show natsuki 1o at t21
    show yuri 1r at f22
    y "Natsuki! There is no need to yell!"
    show natsuki 3r
    y "[player] is our friend, and friends help each other."
    show natsuki 4s
    y "Is [player] not your friend Natsuki?"
    show yuri 1g at t22
    show natsuki 4w at f21
    n "No, he {i}is{/i} my friend."
    show natsuki 4s at t21
    show yuri 1h at f22
    y "Well he is not going to want to continue being your friend if you continue to yell at him constantly."
    show natsuki 4u
    y "Is that what you want Natsuki? For [player] to stop being your friend?"
    show yuri 1g at t22
    show natsuki 2r at f21
    n "No, I just..."
    show natsuki 2n at t21
    show yuri 2e
    mc "Guys it's ok, I get it. I'll figure it out myself."
    mc "I don't want to turn the club room into a battlefield over it."
    show yuri 2v at f22
    y "We don't want to see you fail [player], we understand this is very important to you."
    y 2w "And this also involves another close friend of ours as well, so we should not just leave this situation when we can help."
    show yuri 2u at t22
    show natsuki 4q at f21
    n "Yeah, I'd hate to see Monika in a sour mood if her holiday was ruined."
    n 4t "And I guess I've known her long enough to understand some of her tastes."
    n 2h "It still shouldn't be my problem though."
    show natsuki 3g at t21
    mc "I know, I know. I just need some guidance is all, what makes a good and a bad gift."
    show yuri 1j at f22
    y "Well the best help would be beside you looking through gift ideas tomorrow."
    show natsuki 1c
    y 3p "I-if your okay with that, I was just deducing the best course of action."
    show yuri 3o at t22
    mc "That would be such a big help Yuri."
    show yuri 2u
    show natsuki 2a
    if shoppingvar == 1:
        mc "With you and Sayori we'd be sure to get the perfect gift."
    elif shoppingvar == 0:
        "I'm gonna get some help after all tomorrow, alright!"
    show yuri 1j at f22
    show natsuki 2c
    y "What about you Natsuki? Would you like to join us tomorrow?"
    show yuri 1i at t22
    show natsuki 2q at f21
    n "Why would I want to go out tomorrow? It's gonna be a madhouse at the mall."
    show natsuki 2s at t21
    mc "It would get you out of the house at least, it's up to you."
    show natsuki 2u
    show yuri 2g
    "Natsuki slightly recoils to my suggestion but quickly recovers herself."
    show natsuki 2t at f21
    show yuri 2e
    n "Yeah you know what, maybe I will join your little trip tomorrow."
    n "Could even restock on some baking supplies on the way back."
    show natsuki 2a at t21
    mc "Really? That would be great Natsuki, thank you!"
    show yuri 1b at f22
    y "I'm glad you changed your mind Natsuki."
    show yuri 1a at t22
    show natsuki 2t at f21
    n "Yeah don't mention it."
    show natsuki 2a at t21
    mc "Did you hear that Sayori? Yuri and Natsuki are..."
    show yuri 2u
    show natsuki 1k
    "I turn to look at Sayori, but she's fast asleep at the president's desk."
    show natsuki 1z at thide
    hide natsuki
    show yuri 1d at thide
    hide yuri
    "We all chuckle and return to our normal places in the club."
    if shoppingvar == 1:
        "Now I have all three of the girls on board to help me out tomorrow."
        "There is no way I could mess this one up!"
        "I thank every lucky omen I can think of under my breath."
    elif shoppingvar == 0:
        "I'm gonna get some help after all tomorrow, alright!"
        "Yuri and Natsuki should know Monika's interests pretty well to be able to help pick the perfect gift."
        "I just wish Sayori would have tagged along too, maybe I can convince her tomorrow."
    "The rest of the day is pretty standard as the anticipation for tomorrow grows."
#C6
    stop music fadeout 2.0
    scene bg mall_u with dissolve_scene_full
    play music t6
    "As expected, the mall is completely mobbed today as last minute shoppers like myself scramble to finish their shopping lists."
    if shoppingvar == 1:
        $ y_store = None
        $ n_store = None
        $ s_store = None
        "We made it to the mall by mid day as we had to wait for Sayori to catch up with us."
        "She had slept in again and we were stuck waiting outside her place while she tried to get ready."
        show yuri 1ba at t31 zorder 3
        show sayori 4bs at t32 zorder 4
        show natsuki 4ba at t33 zorder 3
        show sayori at f32
        s "We made it! Wow, look at all the cute decorations!"
        s 1bx "It's all so festive, isn't it [player]?"
        show sayori 1bq at t32
        mc "Yeah it really is, I've never seen this place so dressed up."
        show natsuki 5bk at f33
        n "I've never seen it this full. We better get moving if you want to find a good gift before they're all gone."
        show natsuki 3bn at t33
        show sayori 2bg
        show yuri 2bv at f31
        y "Natsuki's right, if we don't get moving soon we may never find the perfect gift."
        y 3bw "And then what will we do..."
        show natsuki 1bk
        show yuri 1bu at t31
        show sayori 2bj at f32
        s "Don't worry Yuri, I'm sure we'll find the most bestest gift in the whole world for Monika!"
        show natsuki 1bj
        s 4br "We got this! Ehehe~"
        show sayori 3bq at t32
        mc "Yeah, we got this. Let's just start walking and see if we see anything I guess."

        scene bg mall_i with wipeleft_scene
        show sayori 1ba at t32
        show natsuki 2bj at t33
        show yuri 1ba at t31
        "The crowd enveloped us as we walk into the heart of the mall."
        "So many stores to choose from, all with their own selection of things to buy."
        "It all just feels so overwhelming..."
        "Then all at once, the three girls turn to me and talk."
        show natsuki 3bl at f33
        n "Hey [player], what about that store!"
        "Natsuki points towards a book store tucked away in a corner lot."
        show yuri 1bf at f31
        y "That store looks promising [player]."
        "Yuri points towards a small antique store across from the book store."
        show sayori 2bn at f32
        s "Ooo, look over there [player]!"
        "Sayori points towards a small table close to the indoor fountain, fading in and out of view as the crowd of people walk around us."
        show natsuki 1bp at t33
        show yuri 3bp at t31
        show sayori 1bo at t32
        "Just as fast as everyone exclaimed their findings, they all fall silent..."
        show natsuki 1bz at h33
        show yuri 2bd at h31
        show sayori 4br at h32
        "...and then burst into laughter."
        show natsuki 2ba at t33
        show yuri 2bb at f31
        show sayori 2ba at t32
        y "Well it seems we have a lot to choose from, [player]."
        show yuri 1ba at t31
        mc "They all seem like really good choices too."
        "But where to go first?"
        menu:
            "I guess we'll start with..."
            "Yuri's Store":
                $ y_store = True
                $ shopping = 1
                call y_storeA
            "Sayori's Table":
                $ s_store = True
                $ shopping = 1
                call s_store
            "Natsuki's Store":
                $ n_store = True
                $ shopping = 1
                call n_storeA
        label y_storeA:
            "Yuri's suggestion looked interesting, so I suppose we'll head over there."
            mc "Why don't we head over to that antique store? We might find something cool there."
            show yuri 1bj at f31
            y "I've been to this store a few times with my family, they always seem to have a good selection to choose from."
            y 2bo "I just hope they have something fitting for a gift, I wouldn't want to waste your time..."
            show yuri 2bs at t31
            mc "I trust your judgement Yuri, I'm sure they will have something."
            show yuri 1ba
            #
            "We make our way through the crowd and into the store."
            "The walkway and walls were lined with shelves packed with old trinkets and collectible items."
            "An older woman sits at the register at the door, greeting us as we enter."
            show sayori 4bn at f32
            s "Woah, there is so much cool stuff here!"
            s 2br "I wanna see all of it!"
            show sayori at lhide zorder 1
            hide sayori
            show natsuki 1bk at t22
            show yuri 2bn at t21
            show natsuki at f22
            "Sayori starts to make her way towards the back of the store."
            n 3br "Sayori be careful!"
            n 3bq "I'll go keep an eye on her, I'll holler if I see anything."
            show natsuki at lhide zorder 1
            hide natsuki
            show yuri 3bn at t11
            "Natsuki sets off to catch up with the bull we just let loose in this poor shop."
            y 3bq "I-I guess it's just us now.."
            show yuri 3bu
            mc "Seems so, but hopefully this will help us to find anything that would make a good gift."
            y 2bj "Yes, we'll cover more ground like this."
            y 2bg "But where to start..."
            show yuri 1be
            mc "Well there doesn't seem to be much organization to the shelves, so let's just take a look around."
            y 1bj "Yes, I suppose your right [player]."
            show yuri 1bi
            "Scanning through the shelves as we walk, my hope starts to dwindle."
            "There were a lot of fancy porcelain figurines and old looking desk trinkets, but nothing gift worthy for Monika."
            "As we round a corner to check on of the last aisles, an item catches my eye."
            "A small but beautifully decorated wooden box sits perched on the shelf, seemingly crying to be picked up."
            show yuri 2be
            mc "Hey Yuri, come look at this."
            "I take the box from its shelf and bring it over to her."
            y 2bf "That's quite the ornate box [player], what's inside?"
            show yuri 2be
            mc "I'm not sure, I just thought it looked pretty."
            y 2bf "Well why don't we open it then and see if it contains anything?"
            show yuri 2be
            "I undo the latch and carefully open the lid."
            "Set inside the box is a strange mechanical device I can't put my finger on."
            "There was a wind up key protruding from the device, so I try turning that a few times."
            play music mos
            show yuri 1bm
            "The small drum of the machine starts to turn and a song plays from the device."
            "It's a music box!"
            y 2bd "My my, what a pretty melody!"
            y 1bb "I think that would make a wonderful gift for Monika, [player]. Good find!"
            show yuri 1ba
            mc "Thanks, I think this would be a really good gift too."
            mc "I'm gonna wait on it though, just in case there's something better."
            mc "We should go find the others though, I'd hate to leave Natsuki alone with Sayori."
            y 2bq "Oh yes, yes we should go see if everything is okay with them."
            stop music fadeout 1.5
            show yuri 1bi
            "I place the music box back on it's shelf and we head back into the store"
            play music t6
            show yuri 1bo at t31
            show sayori 4bl at t32
            show natsuki 4br at t33
            "We track down the other two girls to find Natsuki scolding Sayori."
            "She had apparently nearly knocked over a shelf of items in her excitement."
            show sayori 1ba at t32
            show natsuki 2bj at t33
            show yuri 1ba at t31
            if shopping == 3:
                "After calming Natsuki down and reassuring Sayori everything was okay, we headed back to the center of the mall."
                call backA
            else:
                menu:
                    "After calming Natsuki down and reassuring Sayori everything was okay, we decided to head to..."
                    "Natsuki's Store" if n_store == None:
                        $ n_store = True
                        $ shopping += 1
                        call n_storeA
                    "Sayori's Table" if s_store == None:
                        $ s_store = True
                        $ shopping += 1
                        call s_store

        label s_store:
            "The table Sayori had pointed to looked interesting enough to check out."
            mc "Lets head to where you were suggesting Sayori."
            show sayori 2bl at f32
            s "O-oh okay! I just thought it looked interesting, I'm not sure they even have anything..."
            show sayori 1bd at t32
            mc "It's okay Sayori, let's go see if they do."
            show sayori 1bn
            show natsuki 2bk
            show yuri 1bg
            "We make our way through the crowd towards the fountain again, finding ourselves in front of a large collapsible table manned by a pair of older women."
            "Signs for the local church line the sides of the table, while a range of boxes filled with shiny metal objects protrude from them."
            "Upon closer inspection, I can make out a whole selection of jewelry from rings to earrings to necklaces."
            show yuri 3bd at f31
            y "Oh how nice! It's a used jewelry sale for the homeless shelter, how sweet."
            show yuri 1ba at t31
            show natsuki 3bd at f33
            n "They got a whole bunch of everything too! I'm sure there's something even Monika would like."
            n 4bh "B-but you need to be the one to find it [player], this still is your problem after all."
            show natsuki 4bi at t33
            mc "Well with a selection like this, I'm sure I'll find something."
            "I hope..."
            show natsuki at thide
            hide natsuki
            show yuri at thide
            hide yuri
            "We start to split up as we look through the selection of jewelry, but Sayori sticks by my side still starstruck by the sight."
            s 1by "It all looks really pretty [player], I'm sure she would like any of this from you..."
            show sayori 2be
            mc "I guess, but none of it really seems like {i}the one{/i} to me, you know?"
            s 2bl "Well you do know her the best, ehehe~"
            s 1bl "You are her boyfriend after all."
            show sayori 1bf
            mc "Yeah but I still need help finding something for her, maybe I'm just not cut out for this..."
            s 2bh "[player], of course you are!"
            s "I know you really care about her and want to make this the best Christmas ever."
            s 3bc "Even if we don't find anything here, we're sure to find the perfect gift somewhere."
            s 1bd "And even if we don't get her anything, I'm sure she'd be happy just to..."
            s 1by "...spend the day with you..."
            mc "Thanks Sayori, that... means a lot to me."
            show sayori 1bd
            mc "But I still want to at least try for a gift today."
            s 2bx "There's still a lot to look at!"
            s 1bo "Ooo, what about that shiny one [player]?"
            "I follow Sayori's gaze to a necklace hanging from one of the displays."
            "Its shiny golden exterior reflects the mall lighting in just the right way to make it glissen."
            "At the bottom of the chain sat a small golden musical note."
            s 4br "Oh my goosshhh its so {i}cuuuttteeee~{/i}"
            "I can't help but agree with her on that one, it seemed to call out to me."
            s 1bx "You should totally get it for Monika! She'll love it!"
            show sayori 1ba
            mc "Maybe, I wanna wait till we've checked out everything though."
            s 2bh "Aww, but it looks so cute. Why pick anything else?"
            show sayori 1bf
            mc "I wanna be sure I pick the best thing Sayori. I'm not saying I don't like it, I just want to see all the different gift ideas."
            s 2bg "Well okay, if you say so [player]."
            s 2br "I might come back and steal it for myself though, so you'll have to make up your mind soon~"
            show natsuki 2bc at t33
            show yuri 1be at t31
            show sayori 1ba at t32
            "Calling over Natsuki and Yuri, I show them the necklace me and Sayori had found."
            show yuri 2bb at f31
            y "It's very nice [player], I think it suits her well."
            show yuri 1bg at t31
            show natsuki 2bd at f33
            n "Yeah, you may not be as brainless as I thought [player]."
            show yuri 1bu
            show natsuki 2bz at t33
            show sayori 2bl
            mc "Hey!"
            show yuri 2bl at f31
            y "Anyways, is this what you're going to get her [player]?"
            show sayori 1bd
            show natsuki 2ba
            show yuri 1ba at t31
            mc "Well um...{w=.75} I'm not sure yet."
            mc "Let me give it some thought first."
            show yuri 1bb at f31
            y "That's perfectly fine [player], we still have plenty of time."
            show yuri 1ba at t31 zorder 3
            show sayori 4ba at t32 zorder 4
            show natsuki 4ba at t33 zorder 3
            if shopping == 3:
                "Moving away from the table, we headed back to the center of the mall to find a seat."
                call backA
            else:
                menu:
                    "Moving away from the table, we decided to make our way towards..."
                    "Natsuki's Store" if n_store == None:
                        $ n_store = True
                        $ shopping += 1
                        call n_storeA
                    "Yuri's Store" if y_store == None:
                        $ y_store = True
                        $ shopping += 1
                        call y_storeA

        label n_storeA:
            "The book store Natsuki pointed out seemed like a solid choice considering we're all in a literature club."
            mc "Let's head over to that book store you suggested Natsuki, might have something good."
            show natsuki 4by at f33
            n "Well of course it does, that's why I suggested it."
            n 2bd "Let's get moving lazy bones!"
            show natsuki 2ba at t33
            "Natsuki takes the lead as we follow her into the small store."
            show natsuki 2ba at t33
            show yuri 1be
            show sayori 1bn
            "As we enter there are shelves packed with books of all kinds from the floor to the ceiling."
            "We're all taken aback at the sheer amount of books in this place."
            show yuri 2bf at f31
            y "Wow, there is certainly a wide variety to choose from here."
            y 1bh "I wish I had known about this place sooner..."
            show yuri 3bo at t31
            y "{i}Oh but all these people in the mall...{/i}"
            y "{i}If they saw someone like me alone...{w=.5}here...{/i}"
            show yuri 4bb
            "Yuri seems to delve into her own world of thoughts, though not without Natsuki noticing."
            show natsuki 2bm at f33
            show sayori 1bf
            n "Yuri what's wrong? You look sad all of a sudden."
            show yuri 4bd at f31
            show natsuki 1bn at t33
            y "I-it's nothing, just a...{w=.75} passing thought is all."
            show yuri 4bc at t31
            show sayori 2bh at f32
            show natsuki 1bc
            s "Aww, cheer up Yuri! There's nothing to be sad about here."
            s 3br "Why don't we go look through the books together! We can try and find some more of that Portrait of Marton you like so much!"
            show natsuki 2ba
            show sayori 1bq at t32
            show yuri 2bq at f31
            y "It's Markov, Sayori, Portrait of Markov."
            show yuri 2bu at t31
            show sayori 2br at f32
            s "Yeah that! Come on, let's go!"
            show yuri 2bo
            show sayori 1bq at t32
            show sayori at lhide
            hide sayori
            show yuri 2bp at lhide
            hide yuri
            show natsuki 4bz at t11
            "Sayori takes a hold of Yuri's hand and starts to pull her deeper into the store."
            y "Sayori wait! Slow down!"
            "I turn to Natsuki who is still giggling at the sight."
            n 2bd "I have to say, Sayori does know how to lighten the mood a bit."
            n 5bq "Still, I guess I'm stuck with you on this one."
            show natsuki 5bc
            mc "What's that supposed to mean?"
            n 4bh "N-nothing, let's just find something to save your butt already."
            show natsuki 1bg
            "We start making our way through the shelving, looking through the collection of books for sale."
            "As we look though, it quickly becomes apparent that we both don't have any real direction of what to look for."
            n 2bc "Gosh there are so many here, we need to decide at least what {i}kind{/i} of book we're looking for here."
            show natsuki 2ba
            mc "Well...{w=.75} Monika does love her poetry, maybe we can find a collection of them or something."
            n 2bd "Yeah, you might actually be onto something there. Lets see if they have a section for that."
            show natsuki 1ba
            "We move deeper into the store, looking through the shelves for any sort of poetry books."
            "Soon enough we find a small lone shelf dedicated to such books."
            n 3bl "Perfect! Now, just to pick one."
            n 3bj "..."
            n 3bn "..."
            n 3bm "Um, what kind of poetry does she like again?"
            show natsuki 1bk
            mc "Well um...{w=.75} she really likes to write in that freeform style, maybe we can find stuff like that?"
            n 2bc "Yeah she really does like that stuff."
            $ _history = False
            n 4bq "{cps=*.8}{i}Even if it makes no sense.{/i}{nw}{/cps}"
            $ _history = True
            show natsuki 4bs
            mc "Hmm?"
            n 4bq "Nothing."
            n 3bb "Anyway, do you know any specific authors she likes?"
            show natsuki 3bg
            mc "Uhhh..."
            extend"well..."
            extend"maybe..."
            extend"uhh..."
            n 3bh "You have no idea, do you [player]?"
            n 3bx "Ugh I should have seen this coming, useless as ever."
            n 3bw "And it's too late to figure it out now, huh?"
            show natsuki 3bs
            mc "Kinda, she'd probably be even more suspicious."
            "I'm surprised she even believed my excuses why I wouldn't be able to spend any extra time with her, unless she's on to me somehow..."
            "Well I don't need to be giving her any sort of confirmations anyway."
            n 3bq "I guess we'll just have to take a shot in the dark then."
            show natsuki 1bs
            "Natsuki takes out her phone from her purse and starts typing furiously."
            "I can't help but notice the glitter and general cutesy manner her phone is decorated in."
            n 2bb "Here, take a look at this list and see if anything rings a bell."
            show natsuki 4bs
            "Natsuki hands me her phone with a web page open to a list of names."
            "The page describes each of them as different famous poets that have written in free verse, which must be the technical term for that kind of poem."
            "As I look through the names, I notice how battered and cracked her screen is."
            "Which seems odd for someone like Natsuki, considering how she treats her precious Parfait Girls manga set."
            "I push the thought to the side, nothing to worry about right at this moment."
            "The names all seem so meaningless though, no one I've ever heard of till..."
            mc "Ah! This guy!"
            n 2bk "You got one?"
            show natsuki 2bj
            mc "Yeah, I remember this guy. Monika talked about him this one time and I remembered his name cause of how weird it was."
            n 1bl "Perfect, we'll look for anything by him then."
            n 2bb "And I'll be taking {i}this{/i} back thank you."
            show natsuki 2ba
            "She snatches the phone from my hands, setting it back in her purse."
            "Looking through the shelves, I almost lose hope in ever finding even one book amidst the rows of other collections."
            "As I near throwing my arms up in defeat, I spot a familiar name on the binding of one of the books."
            show natsuki 2bc
            mc "I got one Natsuki!"
            n 4bd "Oh thank God, I was gonna lose it if we didn't find anything on this shelf."
            n 2bd "So are you getting that one?"
            show natsuki 2bk
            mc "I'm not really sure...{w=.75} I wanna weigh my options first."
            n 4bq "Fine, lets go get the others then."
            show natsuki 2ba at t33 zorder 3
            show sayori 4bn at t32 zorder 4
            show yuri 1bd at t31 zorder 3
            "And find them we do, browsing the horror section of the store of all places."
            "While poor Sayori looked like she was scared out of her mind, Yuri seemed as if she was enjoying herself."
            if shopping == 3:
                "After grouping back up and exiting the store, we decide to head back to the center of the mall where we had started."
                call backA
            else:
                show sayori 1ba at t32 zorder 4
                show yuri 1ba at t31 zorder 3
                menu:
                    "After grouping back up and exiting the store, we head to..."
                    "Yuri's Store" if y_store == None:
                        $ y_store = True
                        $ shopping += 1
                        call y_storeA
                    "Sayori's Table" if s_store == None:
                        $ s_store = True
                        $ shopping += 1
                        call s_store

        label backA:
            show yuri 1bm at s31
            show sayori 1bq at s32
            show natsuki 1bj at s33
            "We all take a seat at an empty table, relieved to take a break from walking."
            s 2br "That was really fun guys! We should do this more often!"
            show sayori 1bq
            n 4bt "You know even if it was kinda chaotic, it was nice to get out of the house for a change."
            show yuri 1be
            n 4bq "I guess I should thank Yuri for...{w=.75} helping me change my mind."
            n 4bh "Its not like I really needed it, but..."
            show natsuki 4bs
            y 2bq "Well thank {i}you{/i} for coming with us Natsuki, you didn't have to but you joined us anyway."
            show natsuki 2bc
            show yuri 2bs
            show sayori 1bn
            mc "If anything I should be thanking all three of you for agreeing to come with me at all today."
            mc "I don't know what I would have done without your help today."
            s 3bx "We're always here to help you out [player], cause we're your friends."
            s 4br "Right everyone!"
            show sayori 4bq
            y 2bj "Exactly Sayori, we're always here to help our friends."
            show yuri 2ba
            n 3bt "Yeah."
            show yuri 1be
            show sayori 1bb
            n 2bd "So [player], what is your final pick for your big gift?"
            show natsuki 4ba
            mc "Well uh..."
            "I'm still on the fence about it."
            "All three of them seemed like good options to me."
            "The music note necklace would look gorgeous on Monika but..."
            "That book of poetry seems like something she would enjoy, but at the same time..."
            "The music box was so beautifully decorated and sounded so nice..."
            "Decisions, decisions..."
            menu:
                "I'm going to get her the..."
                "Necklace":
                    $ gift = 2
                    "Yeah, it's just too nice to pass up."
                    mc "I think the necklace I found with Sayori is the best thing we've found today."
                    s 2br "Aha, I knew you liked that necklace too much to leave it! Ehehe~"
                    s 1bx "It's just too pretty to pass up."
                    show sayori 1ba
                    n 3bt "It was a pretty cute necklace, not gonna lie."
                    show natsuki 4bj
                    y 2bj "That it was, I think Monika would love it [player]."
                    show yuri at thide
                    hide yuri
                    show sayori at thide
                    hide sayori
                    show natsuki at thide
                    hide natsuki
                    "And with that confirmation from the three of them, we headed back to the fundraiser table."
                    "The women even had specialty gift boxes to go along with the necklace, making my life that much easier."
                    jump c6s
                "Music Box":
                    $ gift = 3
                    "Of course, Monika loves music almost as much as literature. The perfect gift."
                    mc "I choose the music box Yuri and I found, its a perfect fit."
                    y 2bb "I totally agree with you [player], I think she'll love it."
                    show yuri 2ba
                    s 3br "Yeah, it looked and sounded so pretty~"
                    s 1bx "I think she'll love it too."
                    show sayori 1ba
                    n 3bt "It was pretty cute, not gonna lie there."
                    n 3bl "See, I don't think you needed us at all [player]."
                    show natsuki 3ba
                    show yuri 2bd
                    show sayori 2br
                    mc "Well I don't know about that one..."
                    show yuri at thide
                    hide yuri
                    show sayori at thide
                    hide sayori
                    show natsuki at thide
                    hide natsuki
                    "We went back to the antique store as a group and I purchased the music box and a big gift ribbon to place on top."
                    "Even with all the other choices, I feel confident this gift will be the perfect one for our first Christmas."
                    jump c6s
                "Poetry Book":
                    $ gift = 1
                    "Poetry by one of her favorite authors, a perfect gift for a literature club president."
                    mc "I'm gonna go with the poetry book Natsuki and I found in the book store."
                    n 4bl "See, I told you I knew what would be best."
                    n 4by "I'm just too good like that."
                    show natsuki 4bz
                    s 2bs "Monika does love poetry, almost as much as she loves you [player]!"
                    show sayori 1by
                    y 3bq "I think Sayori might be right with that one."
                    y 1bb "It will be a wonderful gift, I'm sure of it."
                    show yuri at thide
                    hide yuri
                    show sayori at thide
                    hide sayori
                    show natsuki at thide
                    hide natsuki
                    "Heading back to the book store, we pick up the book and a gift ribbon to wrap it in."
                    "I'm confident in this book, even if it isn't as flashy as the others I know Monika will love it."
                    jump c6s
            label c6s:
                show yuri 2bv at f21
                show natsuki 2bk at t22
                y "Well, with that all set I suppose I should be heading home."
                y "It is getting late and my family would be worried if I missed dinner."
                show yuri 1be at t21
                show natsuki 4bu at f22
                n "Hey uh.. Yuri.. could I walk with you on the way back?"
                n 4bq "I just don't wanna be bored and alone while I walk..."
                show natsuki 4bs at t22
                show yuri 1bb at f21
                y "Of course Natsuki, I would love the company as well."
                y 1bf "Oh dear look at the time, we best get going then Natsuki."
                y 2bd "Take care you two!"
                show yuri 1bc at t21
                show natsuki 1bd at f22
                n "Later Sayori, later [player], see you at the club on Monday!"
                show natsuki 1ba at lhide
                hide natsuki
                show yuri at lhide
                hide yuri
                show sayori 4br at t11
                s "Bye guys! See you at club!"
                show sayori 1bq
                "We wave to Yuri and Natsuki as they take off into the crowd and disappear from view."
                s 2bx "So do you think Monika will like your gift [player]?"
                show sayori 1by
                mc "I hope she'll love it, I think I picked a good one."
                s 2bl "I know she will..."
                s 2bs "Hey uh.. while we're still here, maybe we can just go regular shopping for a bit?"
                s "Just us, without anyone else?"
                show sayori 1by
                mc "Sayori..."
                "I hadn't really been planning to spend the rest of the day here at the mall."
                "I had told Monika I'd try and video call her when I got home, but if I'm out so late I'm not sure I would have the time."
                "At the same time, me and Sayori haven't really been able to spend time together as friends like we used to..."
                menu:
                    "I'll tell her..."
                    "Sure, lets go!":
                        "I'm sure I'll have enough time to call Monika later, and we have Sunday too."
                        show sayori 1bc
                        mc "Okay, I've got some time to kill. You lead the way Sayori."
                        s 4bs "Yay! I can't wait!"
                        show sayori 1bs at face with dissolve
                        "Sayori pulls me into a surprise hug, catching me off guard."
                        s "Thanks [player]~"
                        s 1by "This means a lot to me."
                        mc "Y-yeah, no problem Sayori."
                        show sayori 2bx at t11
                        s "Come on, let's go see that store over there [player]!"
                        show sayori at lhide
                        hide sayori
                        mc "Wait Sayori, jeez!"
                        "Sayori takes my hand and drags me into the heart of the mall once more."
                        $ SayoriVar += 1
                        jump e1c7
                    "Sorry, I can't.":
                        show sayori 1bv
                        mc "I wish I could, but I promised Monika I would try and call her as soon as I could."
                        mc "I'm sorry Sayori."
                        s 2be "Oh okay [player], I understand..."
                        show sayori 2by
                        mc "Hey, don't look so upset. I'll still walk back with you, okay?"
                        s 2bl "O-okay, that can still be fun."
                        show sayori 1bb
                        mc "Yeah, I'll race you out of the mall!"
                        s 4bp "Hey no fair! You had a head start!"
                        show sayori at lhide
                        hide sayori
                        "We take off through the crowd back home, laughing as we ran."
                        "Even if we didn't spend the day at the mall, I can still spend some time with my best friend."
                        #$ SayoriVar -= 1 <-- Debaitable
                        jump e1c7

    elif shoppingvar == 0: #-------------------------------
        $ y_store = None
        $ n_store = None
        "The crowd isn't as bad as it could be however, as Yuri made us all meet at the mall as they opened."
        "Even if I am tired, I'm grateful for her foresight."
        "Though since we left so early, Sayori wasn't answering her phone. She's most likely sleeping in today."
        show yuri 1bb at t21
        show natsuki 2ba at t22
        show yuri at f21
        y "I'm glad you both were able to make it so early."
        y 2bv "I know I'm not much of a morning person myself, but I figured we needed plenty of time and..."
        show yuri 1bu at t21
        show natsuki 2bd at f22
        n "It's alright Yuri, besides I wake up early anyway."
        n 5by "Though I can't vouch for lazy bones over here."
        show natsuki 5t at t22
        mc "Hey, I wasn't even that late!"
        show natsuki 4bs
        show yuri 1bg
        mc "But uuhh, do you guys have any idea where to start?"
        show natsuki 2bt at f22
        show yuri 1be
        n "Nope, but if we start walking I'm sure something will catch our eye eventually."
        n 1bl "So let's get moving!"
        show yuri 1ba
        show natsuki 2ba at t22
        mc "Yeah your right, let's take advantage of the smaller crowds while we can."
        "Making our way inside, we're surrounded by the decorations and the atmosphere of the holidays."
        "Even as the joyful spirit fills the air, I'm still as anxious as ever."
        "This is my only good shot at finding this gift..."
        "As we move toward the center of the mall, both Yuri and Natsuki point in opposite directions and speak at once."
        show natsuki 3bl at f22
        n "Hey [player], what about that store!"
        "Natsuki points towards a book store tucked away in a corner lot."
        show yuri 1bf at f21
        y "That store looks promising [player]."
        "Yuri points towards a small antique store across from the book store."
        show natsuki 2bp at t22
        show yuri 2bn at t21
        "They both pause and look at each other and..."
        show natsuki 3bt at t22
        show yuri 2bq at t21
        "Start to laugh."
        show natsuki 3ba
        show yuri 2bq at f21
        y "Well [player], I guess we have some options already."
        show yuri 1ba at t21
        show natsuki 3bd at f22
        n "Yeah, where to first [player]?"
        n 3be "We don't got all day you know."
        show natsuki 4ba at t22
        mc "Alright alright, well..."
        menu:
            "I guess we'll start with..."
            "Yuri's Store":
                $ y_store = True
                $ shopping = 1
                call y_storeB
            "Natsuki's Store":
                $ n_store = True
                $ shopping = 1
                call n_storeB
    label y_storeB:
        "Yuri's suggestion looked interesting, so I suppose we'll head over there."
        mc "Why don't we head over to that antique store? We might find something cool there."
        show yuri 1bj at f21
        y "I've been to this store a few times with my family, they always seem to have a good selection to choose from."
        y 2bo "I just hope they have something fitting for a gift, I wouldn't want to waste your time..."
        show yuri 2bs at t21
        mc "I trust your judgement Yuri, I'm sure they will have something."
        show yuri 1ba
        "We make our way through the crowd and into the store."
        "The walkway and walls were lined with shelves packed with old trinkets and collectible items."
        "An older woman sits at the register at the door, greeting us as we enter."
        show natsuki 1bc at f22
        n "Well, this is quite the place..."
        n 2bd "Aright, any idea of what we're looking for [player]?"
        show natsuki 2bg at t22
        mc "Well uh, not really..."
        show natsuki 1be at f22
        show yuri 1bo
        n "Not a single clue what to get your {i}girlfriend?!{/i}"
        n 1br "God you are so useless sometimes [player]."
        n 1bw "I'll just go find something then while u sit around being useless."
        show natsuki at lhide zorder 1
        hide natsuki
        show yuri at t11
        "Natsuki bolts off into the store away from Yuri and I."
        y 3bq "Well I...{w=.75} guess it's just us now.."
        show yuri 3bu
        mc "Seems so...{w=.75} why did she have to blow up like that?"
        y 2bv "I'm not really sure myself to be honest."
        y 2bw "{i}I'll have to ask her later...{/i}"
        y 2bf "At any rate, we can look through the store a lot faster now that we've split up a bit."
        y 2bg "But where to start..."
        show yuri 1be
        mc "Well there doesn't seem to be much organization to the shelves, so let's just take a look around."
        y 1bj "Yes, I suppose your right [player]."
        show yuri 1bi
        "Scanning through the shelves as we walk, my hope starts to dwindle."
        "There were a lot of fancy porcelain figurines and old looking desk trinkets, but nothing gift worthy for Monika."
        "As we round a corner to check on of the last aisles, an item catches my eye."
        "A small but beautifully decorated wooden box sits perched on the shelf, seemingly crying to be picked up."
        show yuri 2be
        mc "Hey Yuri, come look at this."
        "I take the box from its shelf and bring it over to her."
        y 2bf "That's quite the ornate box [player], what's inside?"
        show yuri 2be
        mc "I'm not sure, I just thought it looked pretty."
        y 2bf "Well why don't we open it then and see if it contains anything?"
        show yuri 2be
        "I undo the latch and carefully open the lid."
        "Set inside the box is a strange mechanical device I can't put my finger on."
        "There was a wind up key protruding from the device, so I try turning that a few times."
        play music mos
        show yuri 1bm
        "The small drum of the machine starts to turn and a song plays from the device."
        "It's a music box!"
        y 2bd "My my, what a pretty melody!"
        y 1bb "I think that would make a wonderful gift for Monika, [player]. Good find!"
        y 2bj "Music boxes always make a nice desk ornament and can have a lot of meaning attached to them."
        show yuri 1ba
        mc "Thanks, I think this would be a really good gift too."
        mc "I'm gonna wait on it though...{w=.75} just in case there's something better."
        mc "We should go find Natsuki though, she's been gone for a while."
        y 2bq "Oh yes, yes we should go see if everything is okay with her."
        show yuri 1bs
        "I put the music box back on it's shelf and we look back through the store."
        stop music fadeout 2.0
        show yuri 1bf at t21
        show natsuki 1bp at t22
        "We track her down to a shelf loaded with second hand baking equipment."
        show natsuki 4br
        show yuri 1bj
        "Even with her insisting she was looking for any gifts, we both knew she had been looking through here for a while."
        if shopping == 2:
            "After calming Natsuki down, we headed back to the center of the mall."
            call backB
        else:
            "After calming Natsuki down, we headed toward the exit deciding on our next destination."
            $ n_store = True
            $ shopping += 1
            call n_storeB
    label n_storeB:
        "The book store Natsuki pointed out seemed like a solid choice considering we're all in a literature club."
        mc "Let's head over to that book store you suggested Natsuki, might have something good."
        show natsuki 4by at f22
        n "Well of course it does, that's why I suggested it."
        n 2bd "Let's get moving lazy bones!"
        "Natsuki takes the lead as we follow her into the small store."
        show natsuki 2ba at t22
        show yuri 1be
        "As we enter there are shelves packed with books of all kinds from the floor to the ceiling."
        "We're all taken aback at the sheer amount of books in this place."
        show yuri 2bf at f31
        y "Wow, there is certainly a wide variety to choose from here."
        y 1bh "I wish I had known about this place sooner..."
        show yuri 3bo at t31
        y "{i}Oh but all these people in the mall...{/i}"
        y "{i}If they saw someone like me alone...{w=.5}here...{/i}"
        show yuri 4bb
        "Yuri seems to delve into her own world of thoughts, though not without Natsuki noticing."
        show natsuki 2bm at f22
        n "Yuri what's wrong? You look sad all of a sudden."
        show yuri 4bd at f21
        show natsuki 1bn at t22
        y "I-it's nothing, just a...{w=.75} passing thought is all."
        show yuri 4ba at t21
        show natsuki 1bm at f22
        n "That didn't look like a passing thought to me, seriously Yuri is something the matter?"
        show natsuki 2bn at t22
        show yuri 2bq at f21
        y "I'm fine, really."
        y 2bs "Thank you for your concern though Natsuki."
        y 1bq "I-if you two don't mind, I think it would be best if we maybe split up to look around."
        y 3bq "I-if that's okay with you of course."
        show yuri 3bn at t21
        mc "If you think it's a good idea, then I'm all for it. I trust your judgement on books Yuri."
        show yuri 2bq at f21
        y "O-okay, I'll take a look in this section over here."
        show yuri at lhide zorder 1
        hide yuri
        show natsuki 3bm at t11
        n "I really hope she wasn't just saying she was fine to get away from us."
        n 3bu "{i}I guess I'll just have to check with her later...{/i}"
        n 5bc "Still, I guess I'm stuck with you on this one."
        mc "What's that supposed to mean, I could look for something myself?"
        n 4bh "N-nothing, let's just find something to save your butt already."
        show natsuki 1bg
        "We start making our way through the shelving, looking through the collection of books for sale."
        "As we look though, it quickly becomes apparent that we both don't have any real direction of what to look for."
        n 2bc "Gosh there are so many here, we need to decide at least what {i}kind{/i} of book we're looking for here."
        show natsuki 2ba
        mc "Well...{w=.75} Monika does love her poetry, maybe we can find a collection of them or something."
        n 2bd "Yeah, you might actually be onto something there. Lets see if they have a section for that."
        show natsuki 1ba
        "We move deeper into the store, looking through the shelves for any sort of poetry books."
        "Soon enough we find a small lone shelf dedicated to such books."
        n 3bl "Perfect! Now, just to pick one."
        n 3bj "..."
        n 3bn "..."
        n 3bm "Um, what kind of poetry does she like again?"
        show natsuki 1bk
        mc "Well um...{w=.75} she really likes to write in that freeform style, maybe we can find stuff like that?"
        n 2bc "Yeah she really does like that stuff."
        $ _history = False
        n 4bq "{cps=*2}{i}Even if it makes no sense.{/i}{nw}{/cps}"
        $ _history = True
        show natsuki 4bs
        mc "Hmm?"
        n 4bq "Nothing."
        n 3bb "Anyway, do you know any specific authors she likes?"
        show natsuki 3bg
        mc "Uhhh...{w=.75} well...{w=.75} maybe uhh..."
        n 3bh "You have no idea, do you [player]?"
        n 3bx "Ugh I should have seen this coming, useless as ever."
        n 3bw "And it's too late to figure it out now, huh?"
        show natsuki 3bs
        mc "Kinda, she'd probably be even more suspicious."
        "I'm surprised she even believed my excuses I wouldn't be able to spend any extra time with her, unless she's on to me somehow..."
        "Well I don't need to be giving her any sort of confirmations anyway."
        n 3bq "I guess we'll just have to take a shot in the dark then."
        show natsuki 1bs
        "Natsuki takes out her phone from her purse and starts typing furiously."
        "I can't help but notice the glitter and general cutesy manner her phone is decorated in."
        n 2bb "Here, take a look at this list and see if anything rings a bell."
        show natsuki 4bs
        "Natsuki hands me her phone with a web page open to a list of names."
        "The page describes each of them as different famous poets that have written in free verse, which must be the technical term for that kind of poem."
        "As I look through the names, I notice how battered and cracked her screen is."
        "Which seems odd for someone like Natsuki, considering how she treats her precious Parfait Girls manga set."
        "I push the thought to the side, nothing to worry about right at this moment."
        "The names all seem so meaningless though, no one I've ever heard of till..."
        mc "Ah! This guy!"
        n 2bk "You got one?"
        show natsuki 2bj
        mc "Yeah, I remember this guy. Monika talked about him this one time and I remembered his name cause of how weird it was."
        n 1bl "Perfect, we'll look for anything by him then."
        n 2bb "And I'll be taking {i}this{/i} back thank you."
        show natsuki 2ba
        "She snatches the phone from my hands, setting it back in her purse."
        "Looking through the shelves, I almost lose hope in ever finding even one book amidst the rows of other collections."
        "As I near throwing my arms up in defeat, I spotted a familiar name on the binding of one of the books."
        show natsuki 2bc
        mc "I got one Natsuki!"
        n 4bd "Oh thank God, I was gonna lose it if we didn't find anything on this shelf."
        n "So are you getting that one?"
        show natsuki 2bk
        mc "I'm not really sure...{w=.75} I wanna weigh my options first."
        n 4bq "Fine, let's go find Yuri then."
        show natsuki 2ba at t22 zorder 3
        show yuri 1bq at t21 zorder 3
        "And find her we do, browsing the horror section of the store."
        "Yuri must have gotten wrapped up in the selection they had."
        if shopping == 2:
            "With two gift choices in mind, we headed back to the center of the mall."
            call backB
        else:
            show yuri 1ba at t31 zorder 3
            "We pry Yuri from her books and back to the main hallway."
            $ y_store = True
            $ shopping += 1
            call y_storeB

    label backB:
        show yuri 1bl at s21
        show natsuki 2ba at s22
        y "Oh what a relief it is to finally sit down for a rest."
        show yuri 1bm
        n 4bl "All this walking got you tired Yuri?"
        show natsuki 4bj
        y 2bh "Quite tired actually, I'm not used to this much running around on a Saturday."
        show yuri 2be
        n 1bd "Well it's almost over anyway, [player] over here just has to buy his gift and we can go home."
        n 2bc "You do know what your getting her, right?"
        show natsuki 2ba
        mc "Well uh..."
        "I'm still on the fence about it."
        "Both of them seemed like good options to me."
        "That book of poetry seems like something she would enjoy, but at the same time..."
        "The music box was so beautifully decorated and sounded so nice..."
        "Decisions, decisions..."
        menu:
            mc "I'm going to get her the..."
            "Music Box":
                $ gift = 3
                "Of course, Monika loves music almost as much as literature. The perfect gift."
                mc "I choose the music box Yuri and I found, it's like a perfect fit."
                y 2bb "I totally agree with you [player], I think she'll love it."
                show yuri 2ba
                n 3bt "It was pretty cute, not gonna lie there."
                n 3bl "See, I don't think you needed either of us at all, [player]."
                show natsuki 3ba
                show yuri 2bd
                mc "Well I don't know about that one..."
                show yuri at thide
                hide yuri
                show natsuki at thide
                hide natsuki
                "We went back to the antique store as a group and I purchased the music box and a big gift ribbon to place on top."
                "Even with all the other choices, I feel confident this gift will be the perfect one for our first Christmas."
                jump c6ny
            "Poetry Book":
                $ gift = 1
                "Poetry by one of her favorite authors, a perfect gift for a literature club president."
                mc "I'm gonna go with the poetry book Natsuki and I found in the book store."
                n 4bl "See, I told you I knew what would be best."
                n 4by "I'm just too good like that."
                show natsuki 4bz
                y 3bq "Yes, just too good like that..."
                y 1bb "Well it will be a wonderful gift, I'm sure of it."
                show yuri at thide
                hide yuri
                show natsuki at thide
                hide natsuki
                "Heading back to the bookstore, we pick up the book and a gift ribbon to wrap it in."
                "I'm confident in this book, even if it isn't as flashy as the others I know Monika will love it."
                jump c6ny
    label c6ny:
        show yuri 2bv at f21
        show natsuki 2bk at t22
        y "Well, with that all set I suppose I should be heading home."
        y "It is getting late and my family would be worried if I missed dinner."
        show yuri 1be at t21
        show natsuki 4bu at f22
        n "Hey uh.. Yuri.. could I walk with you on the way back?"
        n 4bq "I just don't wanna be bored and alone while I walk..."
        show natsuki 4bs at t22
        show yuri 1bb at f21
        y "Of course Natsuki, I would love the company as well."
        y 1bf "Oh dear look at the time, we best get going then."
        y 2bd "Take care [player]! Have a safe trip home!"
        show yuri 1ba at t21
        show natsuki 1bd at f22
        n "See you back at club on Monday [player]!"
        show natsuki 1ba at lhide
        hide natsuki
        show yuri at lhide
        hide yuri
        "I wave as the pair head back into the growing mob of people and fade from view."
        "Clutching my gift in my hand, I make my own way to the exit and back home."
        "I had promised Monika I'd try and video call her as soon as I was home, so there's no time to waste."
        "Wouldn't want to keep her waiting."
        jump e1c7
#C7
    label e1c7:
        stop music fadeout 2.0
        scene bg class_day with dissolve_scene_full
        play music t3
        "The last day of school before a long break is always the worst."
        "Time seems to drag on forever as the class collectively begs for the final bell to ring."
        "Even the teacher has taken a break from teaching, opting to sit at their desk for the final minutes of class."
        "Soon enough the bell gives in and rings, sending a cheer through the classroom as students pile out into the hallway."
        scene bg corridor with wipeleft_scene
        "The surge of students moving to the main exit of the school almost pull me with them, but I find my way out of the crowd and up the main staircase."
        "While most of the clubs had cancelled today, Monika had one last club meeting in mind before the winter break."
        "Finally reaching the clubroom, I step inside."
        scene bg club_day with wipeleft_scene
        show monika 2k at t11
        m "Ah [player], you're finally here!"
        show monika 1j at face with dissolve
        "Monika practically jumps on me as I enter the room, ensnaring me in a tight embrace."
        mc "Ahaha, it's good to be here Monika."
        show monika 4b at t11
        m "Now we can finally get this party started, ahaha~"
        show monika 2a
        mc "Party, What do you mean?"
        show monika at t21
        show natsuki 2y at t22
        show natsuki at f22
        n "You can thank me for that, [player]."
        n 2d "I had some extra baking supplies from our..."
        show monika 2c
        n 1t "Ahh...{w=.5} I mean from when I was out on a supply run."
        show monika 2a
        n 2z "But anyway, I made some festive treats for everyone!"
        show natsuki at t22
        show monika at thide
        hide monika
        show sayori 4r at t21
        s "Yay! Can we finally see them now!"
        s 2j "Natsuki wouldn't let us see them before everyone was here."
        show sayori 1y at t21
        show natsuki 4e at f22
        n "That's because you would have eaten them the second I took the lid off."
        show natsuki 4g at t22
        show sayori 2l at f21
        s "Noo~"
        s 5b "Why would you get that idea Natsuki, ehehe~"
        show natsuki 3k
        show sayori 4r at hf21
        s "Anyway let's eat, let's eat!"
        show sayori 1q at t21
        show natsuki 5l at f22
        n "Alright, alright, we can eat now."
        show natsuki at lhide
        hide natsuki
        show sayori at lhide
        hide sayori
        "Natsuki makes her way to the closet, presumably where she locked the goodies up away from Sayori's prying hands."
        "She calls for help to bring them over, and Sayori happily joins Natsuki."
        show yuri 3q at t11
        show yuri at f11
        y "Well um, if we're having those treats now I suppose I should make some festive refreshments to go along with them."
        y 1j "I had found some peppermint tea with a bit of chocolate mixed in for the season and have been waiting to try it out. "
        y 3o "Thats if... {w=.75}anyone wants any today, I can totally understand if..."
        show yuri 3u at t11
        mc "Of course Yuri, we always have tea when Natsuki brings in some baked goods."
        mc "It just wouldn't be the same without it."
        mc "Besides, this new flavor sounds like a perfect fit for today."
        show yuri 3f at f11
        y "Really?"
        y 2d "Well in that case, I better go get some fresh water for the kettle then."
        show yuri 1c at lhide
        hide yuri
        "Yuri takes her pitcher from the closet and makes her way out of the clubroom to the water fountain."
        show monika 2b at t11
        m "It's so nice to not have to worry about the school newspaper, even for a day."
        m 2n "It probably wouldn't have been fair to work everyone to the last minute before break."
        show monika 2m
        mc "So you planned this whole thing out, cupcakes and all?"
        m 4n "Not all of it, I was just gonna give everyone a free day like how we've had in the past."
        m 2l "Though I was praying that Natsuki would bake something for the last day before break, and that seems to have payed off, Ahaha~"
        show monika 2j
        mc "Even if we didn't have the pastries, a free day in club with you is always a treat."
        m 2e1 "[player]..."
        show monika 1k at face with dissolve
        m "I feel the same way!"
        show monika 1j
        "Monika pulls me into another hug that I gladly return."
        "Any day I get to spend time with her is something to cherish."
        show monika 1c
        n "Ok love birds, break it up! It's time to eat!"
        show monika 2h at t11
        "Monika breaks from our hug and turns with a glare at Natsuki."
        show monika 1c
        "I take her hand in mine to try and calm her down a bit."
        show monika 1e
        "She turns and gives me a reassuring smile as we make our way over to the rest of the club."
        show monika 1a at t42 zorder 4
        show natsuki 4j at t43 zorder 3
        show sayori 1a at t44 zorder 2
        show yuri 2a at t41 zorder 3
        "We all gather around the makeshift club table Natsuki and Sayori had made with a group of student desks, with Yuri holding the fresh pitcher of water she just brought back."
        "Natsuki stands proudly in front of the container full of her festive treats."
        show natsuki 4l at f43 zorder 4
        show monika zorder 3
        n "Ready everyone!"
        show natsuki 4j
        "We all give her a nod, and she removes the lid in as a dramatic fashion she could muster."
        show monika 1d at t42
        show natsuki 3j at t43
        show sayori 1n at t44
        show yuri 1e at t41
        "We all look in awe at the sight that greets us."
        "A tiny evergreen tree of frosting covered in colorful sprinkles and topped with a big sugar star sits in the center of the tray."
        "Surrounding the tree are five colored cupcakes, each looking like a wrapped gift with little strips of frosting emulating wrapping paper and ribbon."
        show sayori 4r at f44
        show monika 2a
        show yuri 1a
        s "Oh my gosh Natsuki! These are so {b}{i}CUTE!!!{/i}{/b}"
        s 3n "Which one to pick, which one!"
        show sayori at t44
        show natsuki 2k at f43
        n "Hold your horses Sayori, everyone has a special one just for them."
        n 1d "Here, this one is yours."
        show natsuki 1a at t43
        "Natsuki grabs one of the present cupcakes, this one with a blue color and red ribbon-work, and hands it to Sayori"
        show sayori 4r at f44
        s "It's so cute, thank you Natsuki! You're the best!"
        show sayori 2q at t44
        show sayori at s44
        "Sayori takes her cupcake and sits at her chair, diving into the frosting of her gift."
        show natsuki 5t at f43
        n "Well of course I am, what else is new."
        n 3l "Anyway, here you go guys."
        show natsuki 1j at t43
        "Natsuki starts to deal out the rest of the cupcakes to us, starting with a purple one for Yuri."
        show yuri 2b at f41
        y "Thank you Natsuki, this does look delectible."
        y 2d "You even matched the color of my hair, how adorable."
        show yuri 2c at t41
        show yuri at s41
        show natsuki 2t at f43
        n "Yeah that shade of purple was a nightmare to try and get, so you're welcome."
        n 2d "Here you go love birds, enjoy!"
        show natsuki 3j at t43
        show monika 2b
        "Natsuki hands Monika and I a set of cupcakes from the tray as we take a seat, one with a green color and white ribbon and another white with red ribbon."
        show monika 2a at s42
        show natsuki 5m at f43
        n "I wasn't really sure what color to make yours [player], so I just went with white. Sorry."
        show natsuki 3j at t43
        mc "That's okay Natsuki, I'm sure they all taste great any color you paint them."
        show monika 2c zorder 4
        show natsuki zorder 3
        "I look at mine more closely, noticing half of a red heart on the top."
        "Looking over at Monika I notice her looking at a similar sight on her cupcake."
        show monika 1d
        "I lift mine up to hers, and she gives me a confused look for a moment."
        show monika 2b
        "Almost in an instant though, she gets a bright look on her face and puts her's next to mine completing the heart."
        m 2k "Oh Natsuki that's so sweet of you, thank you for that extra little decoration!"
        show natsuki 3t at f43
        n "Yeah, no problem Monika. I thought you might have liked it..."
        show monika 2j
        show natsuki 3u at t43
        show natsuki at s43
        "After everyone was served, Natsuki grabbed her own cupcake."
        "It was especially decorated, with a pink color covered in white ribbon that was shaped into cat ears."
        "As she pulled it away from us and onto her own table though I noticed a few spots of red on her cupcake, seemingly like something was scraped off and frosted over."
        show natsuki 3s
        "It's not long though till she takes a bite out of the cupcake, forever burying the spot in her stomach."
        "I mentally shrug and move my own cupcake into my mouth, biting into the sugary frosting and soft cake inside."
        show natsuki 1k
        mc "Wow Natsuki, I think you really outdid yourself this time. These are amazing!"
        show sayori 2r
        s "Yeah Natsuki, these are {i}soooo{/i} good!"
        show sayori 2a
        show yuri 2b
        y "Yes yes, they may be the best ones you've brought to club yet!"
        show yuri 1a
        show monika 4b
        m "Thank you for bringing these in Natsuki, they were a wonderful way to celebrate our last club meeting before break."
        show monika 2a zorder 3
        show natsuki 4t zorder 4
        n "J-jeez guys you don't all have to praise me at once."
        n 5t "But I mean I'll take it while you're still dishing it out."
        show natsuki 3j zorder 3
        show monika 2l zorder 4
        show yuri 1m
        show sayori 3r
        "We all chuckle as we try to finish up the cupcakes and enjoy the tea Yuri had made."
        show monika 1a at t42
        "Monika stands up and looks at us with a bright smile."
        show sayori 1a
        show yuri 1a
        m 4b "Thank you again Natsuki for the wonderful treats and Yuri for the delectable tea."
        m 2b "I wanted to thank you all for coming in today and wish everyone here a wonderful holiday break."
        m 4k "Also you are all free to head home when you like! Me and [player] will handle the cleanup for today."
        "Wait what did she just say?!"
        show sayori 4r at t44
        s "Aww, you too Monika! I hope you have a super fun break!"
        show sayori 4q at t32
        show natsuki at t44
        show monika 1l
        "Sayori gets up from her chair and pulls Monika into a big hug."
        m 1n "Ahaha~, thank you Sayori, thank you."
        show monika 2a
        show sayori 1a at t43
        show natsuki 5d at t44
        n "Well if you and [player] volunteer for clean up duty, I guess all I gotta do is take my tray back."
        n 3q "Still... I was planning on being here longer today..."
        show natsuki 3s
        show yuri 3h at t41
        y "Me too, but I also had some errands to run on the way home today."
        y 2b "If you would like to accompany me Natsuki you are more than welcome to."
        show yuri 1a
        show natsuki 4t
        n "Well I..."
        n 3d "I guess it couldn't hurt to get in some extra walking today. Sure, I'll tag along."
        show natsuki 3a
        show yuri 2d
        y "Wonderful, thank you."
        y 3b "I suppose we should be heading out then, goodbye everyone!"
        show yuri 2a
        n 3d "See ya later guys, happy holidays!"
        show natsuki at lhide
        hide natsuki
        show yuri at lhide
        hide yuri
        show monika 2a at t21
        show sayori at t22
        "Natsuki and Yuri take their leave, leaving me with Monika and Sayori."
        show sayori 5a at f22
        s "Well, I didn't really have anything to do today either, maybe I can help with the cleanup today."
        show sayori 5b at t22
        show monika 4n at f21
        m "Oh no, its okay Sayori. Me and [player] have everything under control here."
        show monika 2q at t21
        show sayori 2h at f22
        s "But I don't wanna leave you two with all this work..."
        extend "and it's my duty as vice presi-{nw}"
        show sayori 1g at t22
        show monika 2r at f21
        m "I said, it's fine Sayori."
        m 2i "[player] can catch up with you later."
        m "I need to speak with him for a little while, okay?"
        show monika 2h at t21
        show sayori 1e at f22
        s "O-oh...{w=.75} okay..."
        s 2k "I'll just go then..."
        show sayori 1k at lhide
        hide sayori
        show monika 2q at t11
        "Sayori packs up her things and exits the clubroom with her head hung low."
        "I turn to Monika still speechless to the conversation that happened just then."
        m 2r "Just a moment of peace. That's not too much to ask, is it?"
        show monika 2f
        mc "But Monika, that was not the way to ask for it from her."
        mc "Did you not see how she reacted?"
        m 1p "Can't she see I just wanted some alone time with you? Why did she have to insist on butting in on our time."
        show monika 1o
        mc "Maybe she just wanted to spend some time with her friends on the last day of school and didn't want to leave."
        show monika at face with dissolve
        "I move closer to Monika, pulling her into a hug with one hand while taking her cheek into my other."
        m 1p "But I wanted to spend some alone time... with you."
        m 1g "Am I just a... bad person [player]?"
        show monika 1f
        mc "What no, no of course not Monika!"
        show monika 1e
        mc "You're such a wonderful person to be around, and a great friend that really cares about others."
        m 1n "Even when I yell at them to leave huh, ahaha~"
        show monika 1m
        mc "Yes, because I know you don't always feel like that."
        mc "Promise me you'll apologize to her today though okay? It doesn't have to be right now but today."
        m 1e1 "I promise [player]."
        show monika 1e
        mc "Good."
        show monika 1j
        pause .25
        show monika at t11
        "I give her a kiss and let our hug fall apart but still hold both of her hands in mine."
        mc "Now, what did you need me here alone for anyway?"
        m 1n "Well I just wanted to tell you about how we're going to spend our holiday together."
        m 1b "I did a bit of bargaining and convincing with my parents and they've finally let me have you over!"
        show monika 1a
        mc "Oh that's great Monika! I guess I'll finally get to meet them."
        m 2k "Yep! I know they'll just love you [player]."
        m 2n "I'm surprised they even agreed to letting you stay the night, ahaha~"
        show monika 2c
        mc "Wait, overnight? You mean..."
        m 2b "Sleeping in my house for the night, yeah!"
        m 1e1 "Oh [player] wouldn't it be just wonderful? Spending such a magical night in each other's arms?"
        m 2k "I just get so excited thinking about it!"
        show monika 2c
        mc "They're really letting me sleep over? Wouldn't they be worried about..."
        m 2d "Hmm? Worried about what?"
        show monika 2e
        mc "N-nothing. Maybe I'm just a bit nervous is all.."
        m 2e1 "You don't need to be worried, they're the nicest people I know."
        m 4k "I'm almost positive they'll welcome you into the family with open arms! Ahaha~"
        show monika 2m
        mc "Almost huh?"
        m 2l "Hey, people are unpredictable sometimes you know?"
        show monika 2j
        mc "I know, but I'll still love every second of those days together even if things don't go the smoothest with your family."
        m 4e1 "I'll make sure it goes as smooth as possible [player]."
        m 2n "You know, we should actually clean up this room. I don't want facilities to get mad at us for stopping them from locking up the school for the break."
        show monika 2m
        mc "Right, I had almost forgotten about the surprise work you made for us."
        m 2l "It was important, okay!"
        show monika 2e
        mc "I know, just remember the promise you made for today."
        m 2e1 "I know, I'll give her a call when I get home."
        show monika 1a at lhide
        hide monika
        "And with that, we work our way through cleaning up the last club meal before winter break."
        stop music fadeout 2.0
#C8
        scene bg livingroom_sunset with dissolve_scene_full
        play music t8
        "It feels like this winter break has been flying by faster than any of the other ones over the years."
        "It was already Christmas Eve, but it felt as if it had come out of nowhere."
        "Though, I could probably pin the reason to it all on..."
        show monika 1bj at face with dissolve
        "...the girl I was currently holding in my arms."
        "She really has become such a big part of my life now that days just seem to go by in the blink of an eye."
        "Monika had come over again to pick me up and bring me to her place for the night."
        "Just the thought of tonight makes my heart race, having to meet her parents for the first time."
        "Not to mention spending another night together..."
        "No no you can't think like that all the time [player], you're better than that."
        m 1be1 "H-hey [player]?"
        show monika 1be
        "Monika stirs from her little nap, her voice still a bit tired."
        mc "Yes Monika?"
        m 1bn "Do we have to go back to my house? I just want to stay like this forever~"
        m 1bk "You're just so warm and comfy here and I don't want to get up."
        show monika 1bm
        mc "But what about the big dinner you were talking about earlier?"
        mc "Not to mention what your parents would think of me, keeping you here on a night like tonight."
        mc "Besides, we have all night to cuddle for as long as you like."
        m 1bl "Okay, okay, you win [player]."
        show monika 1be at t11
        "Monika reluctantly breaks away from my arms and gets up from the couch."
        m 4bn "We should get going then, it's getting close to the time I said I'd be home with you."
        show monika 2bc
        mc "So much for Miss On-Time huh?"
        m 4bn "Hey! That's Mrs. On-Time for you!"
        m 2bl "Just go get your bag already so we can catch the bus!"
        show monika 2be
        "Monika gives me a playful shove as I laugh and make my way to the stairs."
        scene bg bedroom_sunset with wipeleft_scene
        "I walk over to the stuffed backpack on my bed."
        "I hope I grabbed everything I need for tonight..."
        "Something to sleep in tonight, spare clothes for tomorrow, my whole hygiene kit..."
        "The wrapped box sitting safely in the center of it all..."
        "Yup this should be everything I'll need."
        m "{i}[player] come on, we're going to be late!{/i}"
        mc "I'm coming, give me a sec!"
        "I swing the bag onto my back and look to the other side of my room."
        "My reflection stares back at me from the mirror on the wall."
        "I feel like Monika picked out the stuffiest outfit I had, even if she kept saying I looked cute in it."
        "Have to look my best for her parents I guess, first impressions are important."
        "I feebly try to loosen my tie a tiny bit as I make my way back the stairs."
        scene bg livingroom_sunset with wipeleft_scene
        show monika 2ba at t11
        mc "Ta-da."
        m 2bb "There you are, let's get going then!"
        m 4bk "I can't wait for you to meet my family [player], I know they'll just love you."
        show monika 1bj
        "Monika takes my hand and tugs me to the door."
        scene bg residential_sunset with wipeleft_scene
        show monika 2bo at t11
        "We make our way out to the sidewalk and towards the bus stop, trudging through the late December air."
        "I can feel Monika's hand shaking as she clutches onto mine, getting worse with every gust of wind that passes."
        show monika 1bd at face with dissolve
        m "Huh?"
        "I pull her closer to me, shielding her against the wind as best I can."
        m 1be1 "I'm not that cold [player], I swear."
        show monika 1bc
        mc "Sure you aren't, that's why you've got icicles forming under your nose."
        m 1bd "Icicles? What are you-{w=.5}{nw}"
        mc "These!"
        show monika 1bl
        "I grab Monika's nose between two of my fingers, trying to rub some heat back into it."
        m "[player] cut it out!"
        extend" Come on, stop~!" #<-- Make a side to side movement for this
        show monika 1be
        mc "There, I fixed the icicles for you."
        m 1bn "You're such a tease [player], jeez."
        show monika 1bm
        mc "I learned a few tricks from the devil herself."
        show monika 1bj
        "I can't help but laugh and give her a peck on the cheek just as we reach the bus station."
        scene bg h_residential_sunset with wipeleft_scene
        "We ride the bus for a while until Monika pulls me off the bus at her stop."
        "The neighborhood welcomed us with the sounds of birds chirping in the trees and the low hum of family celebrations from almost every house."
        show monika 2bb at t11
        m "Come on [player], it's just a short walk this way!"
        show monika 1bj
        "Monika grabs my hand and leads me down the road."
        "I can feel my heart start to race in my chest as we walk."
        show monika 1bc
        "I'm really going to have to meet her parents tonight huh? Will they even like me? Are they going to ask me a ton of questions? Will I say the right answers?"
        m 1bd "[player], are you okay?"
        show monika 1bc
        mc "Y-yeah, just peachy. Totally fine."
        m 2be1 "It's okay to be nervous [player], I understand."
        show monika 2be
        mc "I just hope I say all the right things and they like me..."
        mc "I just don't wanna leave a bad impression, you know?"
        m 2be1 "I'm sure they'll come to like you, you're too good of a person not to like."
        show monika 2be
        mc "Thanks Monika, I hope you're right."
        m 2bk "I know I'm right on this one."
        m 4bb "My house is just around the bend here, not too far!"
        show monika 1ba
        "Monika pulls me along as she makes her way over to the front of her house."
        "Even with her little pep talk, I can still feel my heart racing."
        m 4bb "We're here [player]!"
        show monika 2ba
        "She stops me in front of a big house covered in Christmas lights."
        mc "Wow, is this really your place?"
        m 4bk "Yup, this is the place I call home, ahaha~"
        m 2bb "Come on, they're waiting for us inside!"
        show monika 2ba
        "I say my prayers and take a long drag of the fresh air as Monika and I step through the front door."
        scene bg h_livingroom_sunset with wipeleft_scene
        show monika 2bb at t11
        m "Mom, Dad, I'm back!"
        show monika 2ba
        $ y_name = "Female Voice" #<-- Name changes just an FYI
        $ n_name = "Male Voice"
        y "Oh you're just in time dear! We're in the kitchen just finishing up this dish!"
        show monika 1bm
        n "What took you so long, your mother and I told you to be back for dinner."
        y "Oh hush she made it back in time, have some heart hun."
        show monika 2be
        n "Hmmph"
        m 1bb "Come on [player], this way."
        show monika 1ba
        "Monika takes hold of my hand and guides me to the kitchen."
        "Every step towards that door added to the anxiety growing in my chest."
        "I didn't think my heart could ever beat this fast."
        "Lord let me get through this dinner in one piece."
        scene bg h_kitchen_sunset with wipeleft_scene
        show monika 1bb at t11
        m "Mom, Dad, this is [player]!"
        show monika 1bj
        mc "H-hello Ma'am, Sir, it's a pleasure to meet you."
        "I give a wave while trying to focus on keeping myself from shaking into pieces in front of everyone."
        $ y_name = "Monika's Mother" #<-- Name change again
        $ n_name = "Monika's Father"
        "Both of them definitely look the part to be Monika's parents."
        "Her mother has the same long coral brown hair and green eyes I had fallen in love with in Monika."
        "She was in a flashy cocktail dress along with her apron from the kitchen."
        "Her father stood arms crossed in a suit vest just outside the kitchen area, staying out of the cook's way while she brought out the last of the dinner meal."
        "He also had the same green eyes but his hair had started to fade into a dark shade of grey."
        y "[player], it's so good to meet you! We've heard so much about you!"
        show monika 2bm at t42
        "Monika's mother sets down the plate she had in her hands and pulls me into a tight hug."
        y "Sorry dear, I'm a big hugger if you can't already tell. Ahaha!"
        "She gives a hearty laugh into my ear as I ease into the hug."
        m 2bn "Sorry [player], probably should have warned you about that."
        show monika 2bm
        y "Oh he's being a trooper about it Monika, no need to fret."
        y "Now like I was saying, Monika has told us so much about you [player]. I've been looking forward to meeting you myself!"
        y "Please make yourself at home, dinner is just about ready."
        "She motions towards the dinner table, packed with plates full of delicacies."
        m 1bb "Come on [player], you can sit next to me."
        show monika 1ba at t42
        show monika at s42
        "Monika takes my hand and pulls me to the table, taking a seat in a set of chairs on one side of the table."
        "Her father takes a seat on the opposite side and her mother soon joins him after depositing her apron in the kitchen."
        n "I do believe you've outdone yourself this year hun, and this isn't even the big day."
        y "Well I didn't want to disappoint our guest today, and there's always far more cooking to do for tomorrow's dinner."
        y "But we can worry about it when we get there, let's enjoy this meal today."
        show monika 1bj
        "And with that, we all delve into the food and load our plates with a bit of everything."
        "I try to limit myself on the food to look as best as I can, but I can't help but find myself going back for more."
        show monika 1ba
        mc "This food is delicious ma'am, thank you so much for having me over tonight."
        y "Oh thank you! It's nothing really, I've become quite the cook over the years."
        show monika 1bm
        y "But we really wanted to have you over tonight to get to know our daughter's new..{w=.5} partner."
        "I can feel my heart rise up to my throat."
        "So this is the part they interrogate me huh?"
        show monika 1bc
        n "So what are you going to study when you finally graduate [player]?"
        "Monika's father starts the questioning, leaning forward toward me."
        mc "Well um, I-I'm not really sure yet. I'm still trying to sort out my options."
        mc "I've always been around computers so it's something that interests me the most."
        show monika 1ba
        n "Well I could tell you all about that, Hahaha!"
        "He puffs up his chest and a broad smile appears on his face."
        m 3bb "My dad works for one of the biggest tech companies in the city [player], he's the head of the R&D team."
        show monika 1ba
        n "That's right. If you need someone to tell you what you need to make it in the real world, look no further than me."
        n "It's a booming industry, and a gold mine I want my family to prosper from."
        show monika 1bm
        y "Don't forget it's also the place you found your source of happiness hun~"
        n "Y-yes dear.."
        y "Ahaha, we met each other through our work [player]."
        y "Only took one lucky meeting on that special business trip in the tropics and the rest is history."
        y "I mostly work from home while he works in the city and travels around from time to time."
        show monika 1be
        mc "That sounds amazing, you two must be so lucky to be where you are today."
        n "Not luck, but the hard work me and my wife put in everyday got us to where we are today."
        show monika 1bm
        n "And that's something I try to teach Monika everyday as well."
        m 1bn "Yes Dad, I know."
        show monika 1bm
        y "Well, I think that's enough life lessons for one dinner."
        show monika 1bc
        y "So, what do you do in your free time [player]?"
        y "I've learned you can tell a lot about a person by what they do with themselves when they're bored."
        mc "Oh well, I mostly used to just play games and um..{w=.75} read..{w=.75} in my spare time."
        show monika 1be
        mc "But ever since I joined your daughter's Literature Club and started having her over, I've been finding myself doing a lot more."
        show monika 1bm
        y "That's wonderful to hear! I'm glad to know she keeps you busy, ahaha!"
        m 1bn "Well I don't like to be kept cooped up all the time you know."
        show monika 1bm
        y "That is very true, did you know that one winter little Monika-{w=.75}{nw}"
        m 3bl "Ahh would you look at that, it seems like it's time for dessert Mom!"
        show monika 1be
        y "Oh gosh your right, it seems like everyone is done."
        show monika 1bc
        y "Could you help me grab the desserts from the cellar Monika? I couldn't fit all of them in the fridge up here."
        m 1bd "Oh um, sure Mom."
        show monika 1ba at t42
        "Monika gets up from her chair and starts to move to her mother's side."
        show monika 1bc
        "I flash her a look of pure terror. She was really gonna leave me alone with her {i}Dad?!{/i}"
        show monika 2be
        "She tries to comfort me with a smile as she fixes her skirt."
        show monika 1ba at lhide zorder 1
        hide monika
        "And like that, she disappears with her mother around the corner."
        "{i}Oh god, I did not sign up for this.{/i}"
        n "You don't have to look so nervous there [player], it's not like I'm going to hurt you.{w=2.5} Not yet anyway..."
        "The look on my face must have been priceless, because he immediately burst into laughter."
        n "Relax relax, I'm only joking."
        stop music fadeout 2.0
        n "But on a more serious note, the little stunt you pulled with my daughter a few weeks ago did leave a sour taste in my mouth."
        "He leans into the table again, focusing solely on me."
        play music t7
        "{i}Is he referring to...that day?{/i}"
        "{i}When she...when we...{/i}"
        mc "I-I'm very sorry sir, we had just lost track of time that night and um.. we..."
        n "No need to come up with an excuse now, I'm sure you know what I'm referring to."
        "He gets up from his chair, still leaning into the table square at me."
        n "Normally I would have beaten the life out of anyone that wanted to touch my daughter, but {i}you...{/i}"
        "Oh no, this really is where I die."
        "Strangled to death by my first girlfriend's father."
        "Well it's been a good run I guess."
        "Goodbye Monika, I'll miss you..."
        stop music fadeout 1.5
        n "But..."
        "He sighs, falling back into his chair."
        play music t9
        n "To put it bluntly [player], she speaks very highly of you."
        n "I've never seen her look so happy in such a long time."
        "I can feel all the fear in me wash away as her father's shoulders slump down."
        n "As her father, it makes me smile to see her so full of joy and happiness."
        n "Everytime your name comes up in a conversation, I can see her eyes just light up."
        n "I believe only the best deserve to be accepted into this family [player], and I hope my daughter has seen the best in you."
        n "That said, if I {i}ever{/i} find out you hurt her [player]..."
        mc "N-No Sir, I intend to make her the happiest girl alive. You have my word."
        n "Good, you better. I'm starting to like you [player], you know that?"
        n "There's something about you that tells me she's in good hands."
        "He gives me a hearty laugh and I find myself joining him."
        "It feels like a valve of anxiety had been released inside me."
        "I've at least gained the approval of one parent, and her father no less."
        stop music fadeout 2.0
        "I guess you could say I'm pretty damn lucky."
        play music t8
        show monika 3bb at l11
        m "We're back, sorry it took so long."
        "Monika and her mother appear from their expedition, hands full of small desserts and what seemed like a large cherry pie."
        m 3bl "Mom had all the stuff buried in the cellar fridge somehow."
        show monika 3bm
        y "Too much stuff in this house I swear."
        show monika 2ba
        "They set all the desserts around the table, with the pie taking the center of the table."
        show monika at t42
        pause .25
        show monika at s42
        "Monika takes her place in the seat next to me, and I feel as if I can finally breathe normally again."
        y "Now [player], I implore you to try the pie first. It's a special family recipe."
        m 3bb "Yeah [player], it's probably the best pie you'll ever eat!"
        show monika 1ba
        mc "Well if everyone insists..."
        "Monika's mother slices a piece and hands it to me on a smaller dessert plate."
        "I dig my fork into the oozing mound of cherries and pie crust, pulling a chunk from the mass."
        "Bringing it to my mouth, a wave of sweet cherry flows over my tongue."
        show monika 1bj
        mc "Wow, this really is amazing ma'am. It's one of the best I've ever had by far!"
        y "Oh hush dear, you're going to make an old woman blush."
        y "Thank you though, it's a recipe every woman on my side of the family has learned to bake."
        show monika 1bm
        y "Well, except a certain young lady I know."
        y "Anyway, please don't be shy [player]. Try a little of everything!"
        mc "Thank you, I sure will."
        show monika 1bj
        "And try everything I did, despite me trying to look like a well fed child."
        "It's the holidays though, no one can judge on the holidays."
        "After everyone finished, Monika's parents started removing plates and bringing them over to the sink."
        m 2be1 "Hey [player]..."
        show monika 2be
        "Monika nudges and whispers to me."
        m 2be1 "Why don't we head to my room, just us two."
        show monika 2be
        mc "Oh, alright Monika."
        show monika 1bb at t42
        m "Mom, Dad, I'm gonna show [player] up to my room."
        show monika 1ba
        y "Okay dear, we'll be down here if you need us."
        show monika 2bm
        n "I'm sure you won't though."
        m 2bn "Come on, this way."
        show monika 2bm at lhide zorder 1
        hide monika
        "Monika takes my arm and starts to pull me towards the stairs."
        "I thank her parents again for the meal as I grab my bag and follow Monika."
        stop music fadeout 2.0
#C8
        scene bg mroom with wipeleft_scene
        play music t6
        show monika 2be1 at t11
        m "Well, here we are."
        show monika 2be
        "I look around her room, my eyes darting from here to there."
        #=======================================================================
        #Testing- REMOVE BEFORE RELEASE
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause(.25)
        hide screen tear
        show noise zorder 4:
            alpha (1.0)
        menu:
            "vcall=1":
                $ vcall = 1
            "vcall=0":
                $ vcall = 0
        hide noise
        #=======================================================================
        if vcall == 1:
            "It looks just as it did when we video called all those Sundays ago."
            "Well, a bit better in person rather than the terrible video quality."
            "I feel as though I'm home, even if I've never really been here before."
            mc "It's nice to be here in person for once rather than being on your phone."
            m 2bl "I know, though at least then I could control what you could see."
            m 2bn "Though I'm sure I cleaned up enough for you to come over.."
            show monika 2be
            mc "It would have been fine, even if there was a little mess."
            m 1bn "Maybe, but I have to make a good impression too you know."
        elif vcall == 0:
            "Her walls were lined with inspirational posters and classic canvas wall art."
            "Not my sort of decoration taste, but for some reason I feel it suits Monika."
            "A perfect student like her needs an inspiration room to keep her motivated."
            mc "It's very you Monika, I'll give it that."
            m 2bn "Hey, what's that supposed to mean?"
            show monika 2be
            mc "It means I love it."
            m 2bl "Oh gosh [player], ahaha~"
        m 4bb "Well, you can put your bag over here. That way its out of the way."
        show monika 2ba
        "She points me to a far corner of the room where I place my bag."
        m 2bk "And now that we're home, I can finally get out of this stuffy outfit."
        show monika 2bj
        mc "What do you mean Moni-"
        show monika 1bj
        "I turn my head towards Monika just in time to see her start working on unbuttoning her shirt."
        show monika at thide zorder 1
        hide monika
        "I quickly whip my head back forward, shielding my eyes from trying to turn back."
        mc "Jeez Monika! At least warn me next time!"
        m "What? I'm just gonna change into my pajamas."
        mc "And your just gonna undress in front of me?!"
        m "[player]..."
        "I can hear her footsteps getting closer to me, and the sound of a shirt thrown across the room makes my eyes widen."
        m "{i}It's not like you haven't seen me like this before~ hehehe~{/i}"
        "Monika wraps her arms around me from behind, taking me by surprise."
        "I can feel the warmth of her skin through my dress shirt as she presses against me."
        mc "M-Monika..."
        "My mind was confused trying to figure out if I should feel upset at her or aroused by her."
        m "Fiinne, if you don't wanna look then that's your choice. But no peeking now~"
        mc "O-Okay..."
        "I can hear her giggling as she gets up and moves over to her dresser I would assume."
        "I try and focus on digging through my bag to find my sleepwear, but I can't help but want to turn my gaze even a little bit."
        "{i}No, you're better than that [player]. You're not going to look.{/i}"
        "{i}You shouldn't be looking at her like that anyway...{/i}"
        "{i}Gaaaahhh hurry up Monika please!{/i}"
        "It feels like an hour passes while I mindlessly go through my bag."
        m "Okay, I'm all dressed [player]. You can look now~"
        "I turn my head slowly to face Monika, still hesitant to any tricks she might try."
        show monika 5pa at t11
        mc "Wow Monika, you look adorable in those!"
        m 2pl "Aw, thanks [player]."
        m 4pn "They're just pajamas though, nothing that special."
        show monika 2pm
        mc "Maybe you just make everything cute then."
        m 2pl "What, that's just silly. Ahaha~"
        m 2pn "Why don't you get changed, I'm sure that outfit is far from comfortable for you."
        show monika 2pm
        mc "Fine, but no peeking yourself then."
        m 2pl "Okay, okay, no peeking."
        show monika 1pj at s11
        "Monika takes a seat on the edge of her bed, covering her eyes with her hands for dramatic effect."
        "I can't help but smile at her while I finish fishing out my own pajamas."
        "Far from fashionable, just a basic white tank top and some fleece pants."
        "I can't help but feel her eyes trying to look through her hands though, so I try to change as fast as I can."
        "I know we've already done.. {w=.75}those kinds of things.. {w=.75}but it all still feels weird to me."
        "Maybe I'll get used to it one day, seeing her like that casually."
        "But for now, I'd like to at least be modest with her as best I can."
        mc "Alright, I'm all done."
        m 1pd "..." #<--extra blush
        mc "Um...{w=.75} is there something wrong Monika?"
        m 2pn "Nono, i-it's fine! Ahaha~" #<--extra blush
        m 1pe1 "Just come over here already."
        show monika 1pj at t42
        show monika at s42
        "She shifts herself over in the bed and outstretched her arms towards me."
        show monika 1pj at face with dissolve
        "I happily obliged, taking my new spot on the bed and in her arms."
        m 1pk "Your so warm [player], I would stay like this all winter long if I could."
        show monika 1pj
        mc "Me too, maybe even all year long."
        m 1pk "I would if you wanted too!"
        show monika 1pj
        "We pull each other closer and stay like this for a while."
        "I couldn't complain though, I felt happy in her arms."
        m 1pb "Hey, why don't we watch some classic holiday movies!"
        m "Me and my parents always do that every Christmas Eve before we go to bed."
        show monika 1pa
        mc "Well sure, that sounds like fun."
        m 1pk "Yay! Let me see if I can find any!"
        show monika 3pj at t42
        pause .1
        show monika at s42
        "Monika rolls away from me, grabbing the remote for the television and opens up her Webflux."
        show monika 3pc
        mc "Why don't we grab a snack or something before we start? Even if its something small we cou-{w=1.5}{nw}"
        m 1pn "Umm, I actually don't think we have anything right now [player]."
        m 3pl "Let's just stay up here, we don't {i}really{/i} need anything down there anyway."
        m 2pk "We have everything we need right up here! Ahaha~"
        show monika 1pc
        mc "Oh..{w=.5} okay..{w=.5} is everything okay Monika?"
        m 1pe1 "What do you mean? Everything is great!"
        m "We're here together, enjoying this magical night so close."
        m 1pk "What more could a girl ask for on a night like this?"
        show monika 1pj at face with dissolve
        "Monika hops back into my embrace and happily wraps her arms around me."
        "The movie starts to play on the television and the sounds of holidays fill the room."
        show monika 1pa
        "It's definitely an older film, one I've seen countless times over my lifespan."
        show monika 1pm
        "It has a special sort of feeling only a holiday film can create though, one that doesn't go away even after all this time."
        "A spirit of family and happiness the season is known for."
        show monika 1po
        "Even still, I can only be surprised by the same scenes so many times."
        "I feel my gaze lower to Monika, who's resting her head on my chest."
        "To my surprise though instead of an expression full of joy, she looks as though she's contemplating something."
        menu:
            mc "Is this about earlier? What is going on in her head..."
            "Ask her what is wrong":
                $ e1c8 = 1
                "I can't just let whatever it is to continue upsetting her all night."
                "I want her to be happy tonight, not worried about anything."
                mc "Hey, is something bothering you Monika?"
                m 1pc "Hmm?"
                m 1pd "What are you talking about [player]?"
                show monika 1pc
                mc "It looked like something was bothering you, and I wanted to make sure you were okay."
                m 1pn "N-No, I'm totally fine [player]."
                show monika 1pc
                mc "Are you sure? It really looked like something was bothering you."
                show monika 1pq
                mc "I just want to make sure your okay and-{w=1.5}{nw}"
                m 1pr "[player]."
                m 1pi "It is nothing."
                show monika 1ph
                "I feel my sentence fall apart as Monika looks sternly into my eyes."
                m 1pi "It's nothing for you to worry about."
                show monika 1ph at t11
                pause .2
                show monika 1pq at thide zorder 1
                hide monika
                "Monika rolls off my chest and onto her side of the bed and turns away from me."
                "Great, now you just upset her more [player]."
                "Just great."
                "I turn my gaze away from Monika and up to the ceiling."
                "Nice job ruining tonight with this."
                mc "I'm sorry Monika..."
                "I look over to her, only to find her back turned to me."
                "She stays silent, with nothing but the rustling of the blanket and the television making noise."
                "I look back up to the ceiling, feeling defeated."
                "I guess I should just get some sleep then, maybe she'll be in a better mood tomorrow..."
                mc "I'm... gonna get some sleep. I love you Monika."
                "I try to settle myself comfortably for the night."
                "Tomorrow is another d-{w=1.5}{nw}"
                show monika 1pg at face with dissolve
                play sound "sfx/fall.ogg"
                m "No I'm sorry [player]!"
                show monika 1pf
                "Monika had practically jumped on top of me, clutching me as tight as she could."
                "Her face sat only inches from mine and I could feel the heat from her face on mine."
                m 1pp "I just..."
                m 1pg "I'm scared [player]."
                show monika 1pf
                mc "Scared of what Monika? What's wrong?"
                m 1pp "Well, when my mom brought me downstairs earlier... she talked to me a bit..."
                m 1pg "...about you, [player]."
                m "She said stuff about how she doesn't think your any good for me."
                m 1pg "Stuff about how I could do so much better than you..."
                show monika 1pf
                mc "B-But she was so nice to me at dinner, I thought she..."
                m 1pn "She's good at hiding her true feelings sometimes."
                m "She can put on a good mask in front of people, giving the impression she feels one way..."
                m 1pp "...but in reality, feels the opposite."
                m 1pp "I just wish it wasn't the case for you though..."
                m 1pr "What if she convinces Dad your a bad person and they..."
                show monika 1pq #<-- Edit in tear sprites
                "Tears start to form under her eyes."
                m 1pr "...what if they make me stop seeing you? What if we can't be together anymore?"
                show monika 1pq
                "Her head falls into my chest as she starts to cry."
                mc "Monika, hey, I'm not going anywhere."
                "I run my hand through her hair in an attempt to sooth her."
                mc "Even if she ends up not liking me in the end, I will still love you with all my heart Monika."
                show monika 1pe
                mc "And even if she forces you to stop seeing me I'll always find a way to get to you, like a Romeo to his Juliet."
                m 1pl "Oh [player], ahahaha~"
                show monika 1pe
                "Monika shifts herself so we're laying on our sides eye to eye as she wraps one arm around my neck and another around my waist."
                "I find myself holding her just as close and wiping the rest of the tears from her face, resting my hand on her cheek."
                "It seems Saint Nick was helping with the moonlight tonight as well, because I felt myself get lost in her emerald eyes."
                show monika 1pj
                "Before I can even react s in closer, planting her lips onto mine."
                scene black with dissolve
                "I feel the world wash away as we embrace and lock lips, time slipping away from my mind."

            "Don't press her about it":
                $ e1c8 = 0
                "Whatever it is, pushing for information may not be the best course of action."
                "It may just make it worse and upset her."
                "I wouldn't want to ruin a night like tonight over something that may not even be bothering her."
                show monika 1pc
                "I run my hand through her hair, pushing a bang out of the way of her face."
                "I can't help but smile as Monika turns her emerald green eyes to me."
                show monika 1pe
                "My hand moves from her hair to her cheek, slowly caressing it with my thumb."
                "Maybe it was the magic of tonight, but it felt like Monika looked so beautiful right now."
                show monika 1pj
                "She takes the initiative next, closing the gap between us and planting her lips on mine."
                scene black with dissolve_scene_full
                "We stayed interlocked for what seemed like forever, letting sleep overtake us as we stayed in each other's arms."
                "Whatever it was, it must not have been too serious."
                "I thank the stars above for that at least..."
#C9
        scene bg mroom_morning with dissolve_scene_full
        "I stir from my sleep in a daze, rubbing my eyes as I sit up."
        "I feel myself panic as I start to look around the room, wondering why I wasn't in my own bedroom."
        "Where the heck..."
        m "Oh, [player], your finally awake!"
        show monika 2pb at t11
        m "I thought you were gonna sleep the whole morning silly, come on!"
        show monika 2pa
        mc "Right, sorry..."
        "In a moment everything came back to me, I was at Monika's house for the night and today was..."
        "Oh gosh that's right now! I can't be in bed right now!"
        "I hop out with a new found energy and move over to my bag to grab my outfit for today."
        m 4pl "[player], you don't have to worry about getting dressed yet. We always do presents in our pajamas!"
        show monika 2pe
        mc "Right right, gosh I'm all messed up this morning."
        m 2pn "That's alright, I'm not rushing you or anything am I?"
        show monika 2pm
        mc "No, no Monika of course not. Let me just grab this then."
        show monika 1pc
        "I fish through the remainder of my bag for my hygiene items and grab the wrapped box from the depths of it's protective shell."
        m 2pk "Well, I wonder who {i}that{/i} is for [player]~"
        show monika 2pj
        mc "I guess we're going to find out huh?"
        m 4pb "Come on then, the sooner we eat breakfast the sooner we can open it!"
        show monika 2pa
        "I chuckle as I put on my deodorant and a bit of cologne before I follow Monika downstairs, present in hand."
        scene h_livingroom with wipeleft_scene
        show monika 1pa at l11
        "Monika takes me into the living room first before we head to the kitchen."
        m 1pk "Good morning Mom, good morning Dad!"
        show monika 2pa
        "Monika's mother and father both sit on the couch beside the Christmas tree wrapped in each other's arms."
        "Under the tree sat an assortment of colored boxes in a whole range of sizes."
        "Monika's mother turns to us and sits up, a festive red hat on her head and a wide smile on her face."
        y "Good morning you two! Did you sleep well [player]?"
        mc "I did, thank you."
        if e1c8 == 1:
            "I found myself focused on her smile, the conversation of last night creeping into my mind."
            "Does she really not like me? I haven't done anything wrong yet to upset her, have I?"
            "Why didn't she think I was good enough for Monika..."
        elif e1c8 == 0:
            "I gave her a big smile and nod, trying to emulate the same energy she had."
            "The holiday spirit had seemingly intoxicated everyone, making all of us happy and full of energy so early in the morning."
        show monika 1pd
        y "Monika dear, I left some of breakfast out for you two. We already ate so you two are free to have whatever you like!"
        m 2pb "Okay, thanks Mom!"
        m 2pk "Come on [player], this way."
        show monika 1pj
        "Monika takes my hand once again and guides me into the kitchen."
        scene h_kitchen with wipeleft_scene
        show monika 1pj at l11
        "As we entered the kitchen I was hit with a wave of aromas, a mix of all sorts of breakfast dishes sat displayed on the countertop."
        show monika 2pa
        mc "Whoa, there's so much stuff here!"
        m 4pb "Yup, we like to have a big breakfast so we aren't as hungry throughout the day."
        m 2pl "Mom likes to have dinner later so she has time to cook and prepare the house a bit before the rest of the family comes over."
        show monika 2pa
        mc "That's totally different than how we do it."
        m 3pb "Maybe next year you'll actually get to show me how you do it at your place!"
        show monika 2pa
        mc "Oh yeah! That sounds like a plan to me."
        m 2pk "Then I can't wait then, ahaha~"
        m 2pl "But anyway, let's focus on this Christmas instead of next year."
        show monika 2pe
        mc "Right, right. Gosh I don't even know where to start with all this."
        m 3pb "I could give you some pointers, there's a couple things you just {i}have{/i} to try!"
        show monika 1pj
        mc "By all means, take it away."
        show monika 3pk at h11
        "And so she did, pointing out a whole assortment of dishes."
        "Just with her recommendations my plate was more full than I had planned, but a little extra breakfast never hurt anyone."
        show monika 1pa at s11
        "With our plates loaded we sat down to eat..."
        show monika 1pk
        "...but a slow, relaxing meal was not what I got."
        "Monika was so excited she was practically shoveling the food into my mouth to get me to eat faster."
        "I just smiled and ate as fast as I could, how could I stay annoyed at her when she was so happy and excited anyway?"
        m 1pb "Are you done [player]? Come on let's go, let's go!"
        mc "Okay okay Monika, I'm done."
        show monika 2pk at t11
        m "Alright! Let's head back into the living room!"
        show monika 1pj
        "Monika grabs my hand and pulls me from my chair."
        mc "Monika slow down a bit!"
        show monika 1pj at lhide zorder 1
        hide monika
        "My cry falls on deaf ears however, as she seemingly goes even faster."
        "I just sigh internally and hold her gift tightly to my side."
        scene h_livingroom with wipeleft_scene
        show monika 4pb at l11
        m "Okay, we're all done!"
        show monika 2pa
        y "My, that was quick. are you sure you had enough to eat?"
        m 2pk "Yup, and [player] really liked all of it!"
        show monika 2pj
        mc "Yes it was all very delicious Ma'am, thank you."
        y "Well, I'm glad you enjoyed it [player]."
        y "Now, come take a seat you two. I think it's about time we opened presents!"
        show monika 1pj at t42
        show monika s42
        "Monika leads me over to a spot next to the tree while grabbing a pillow from the couch and takes a seat on the floor."
        "I follow suit, grabbing a pillow of my own and take a seat next to her."
        show monika 1pc
        n "You know [player], it's not going to be much fun for you since there isn't anything under this tree with your name on it."
        y "Hmm, that is true. Sorry about that dear."
        m 1pn "Well, that's not entirely true..."
        show monika 1pm
        n "Oh ho, snuck something under the tree yourself did you?"
        n "Well, the more the merrier I say!"
        y "Of course! It is the season of giving after all."
        show monika 1pj
        "Her dad lifts a glass in his hands and gives a hearty laugh."
        "I can't imagine that it's not just eggnog in that glass..."
        "Also, when did Monika put my gift under the tree?"
        "There hadn't been any gifts under the tree when I got here and I had been with her all day yesterday."
        "Huh..."
        show monika 1pa
        y "Why don't you start with your stocking Monika?"
        m 1pb "Okay! [player], can you hold it for me?"
        show monika 1pa
        mc "Of course, lets see here.."
        "Monika's mother hands me a large red stocking, a large red M is stitched into the top."
        show monika 1pj
        mc "Let's see what's inside this then."
        "I lean the opening towards Monika, and she starts to work through the large stocking."
        show monika 1pk
        "Candies and small gifts all come pouring out one by one, each receiving a smile and thank you from Monika."
        "Soon enough however, the gifts ran dry and Monika was left reaching her whole arm into the stocking."
        m 1pl "Well I guess that's everything in there, ahaha~"
        m 3pb "Thank you for being my assistant [player]."
        show monika 1pa
        mc "Any time, that was actually kinda fun!"
        mc "I guess we can get to the bigger boxes now."
        m 3pl "And just before 12:30, I never thought we'd have such a late gift opening, ahaha~"
        mc "Wait..."
        show monika 1pc
        "Oh crap..."
        "Oh man, oh god damn it..."
        m 1pd "What's wrong?"
        show monika 1pf
        mc "I told my parents I'd be back to help cook today, and it's already past noon! I'll be late if I don't start back now..."
        y "Oh my, you best be going then if you want to get home at a decent time."
        m 1pg "Do you really have to go [player], we were just getting to the good part..."
        show monika 1pf
        mc "I know I'm really sorry, I didn't mean to sleep so late into the morning this time..."
        show monika 1pe
        mc "Let me get dressed real quick, maybe I can still be here for a couple of gifts before I leave."
        m 1pe1 "Alright, but hurry please!"
        show monika 1pe
        mc "I will, just give me a moment."
        "I quickly jump up from my seat and nearly race back upstairs."
        scene bg mroom_morning with wipeleft_scene
        "God I'm such an idiot, I'm so used to being woken up early on Christmas that I didn't even do it naturally."
        "Let me just get these pants on, and my shirt buttoned up..."
        m "[player]? Can I come in?"
        mc "Monika?! Y-yeah sure, I'm just buttoning my shirt."
        show monika 1pe at t11
        "Monika steps into the room, a set of colorful boxes in her hands."
        mc "Monika, I'm really sorry. I thought we'd have enough time in the morning, but I overslept and..."
        m 1pl "Its okay [player], you don't need to apologize so much for it."
        m 1pn "I'm not mad at you or anything, I know you have your own family to spend today with."
        m 1pe1 "But before you left, I want to make sure you got to open this."
        show monika 1pe
        "Monika hands me one of the boxes, wrapped in a shiny silver paper."
        m 4pl "And you forgot this downstairs too, ahaha~"
        "Monika holds up the other box, donning the same emerald green wrapping paper I had used."
        m 2pe1 "I wanted to open it with you, not after you had left."
        show monika 2pf
        mc "Yeah, I wanted to open these with you too. Gosh I really messed this all up..."
        m 2pe1 "Stop, you haven't messed anything up [player]."
        m 4pb "I'd actually say this is a bit better..."
        m 2pn "Downstairs I feel like my parents would react weird seeing me give you a hug or a kiss."
        if e1c8 = 1:
            m 2pp "Especially my mom..."
        m 2pb "But up here, they aren't around to say anything."
        show monika 2pa
        mc "I guess it is better, always one step ahead Monika."
        m 2pl "Oh stop, just open your gift already."
        show monika 1pc
        mc "No, I want you to open yours first."
        m 1pd "Really, are you sure?"
        show monika 1pe
        mc "Yup, I want to see your reaction first."
        m 2pl "Well, if you insist~"
        show monika 1pj at s11
        "Monika takes her gift and sits down on her bed and I sit beside her with my gift in hand."
        if gift == 3:
            show monika 1pc
            "The small square box seemed to intrigue Monika, as she kept flipping it over and over."
            mc "Well we'll never know what's inside till we open it."
            m 1pl "I can guess before I open it, can't I?"
            m 1pb "Fine, let's see what's inside!"
            show monika 1pa
            "Monika tears away the paper to reveal..."
            show monika 1pc
            mc "Aw cool, a little cardboard box!"
            m 1pl "Very funny, [player]"
            m 1pb "But the real gift is inside here..."
            show monika 1pa
            "She picks away my poor taping job and slowly opens the cardboard box."
            show monika 1pd
            "A small gasp escapes her mouth as she lifts the ornate wooden box from it's cardboard shell."
            m "[player], it's so pretty! But what..."
            show monika 1pc
            mc "Here, turn this key a few times and pull this lid up a bit."
            "I show her the winding key and with a few turns it's fully wound."
            "Monika unlatches the lid and slowly opens the top."
            play music mos
            show monika 1pd
            "The brass drum slowly turning inside the ornate box plucking the metal combs."
            "It's song echos through the room, filling our ear's with a sweet lullaby."
            m 1pe1 "[player], this is..."
            m "It's so beautiful, everything about it is so beautiful!"
            m 1pd "Where did you even find something like this?"
            show monika 1pc
            mc "Well uhh..."
            show monika 1pe
            mc "I may have had a little help..."
            m 1pl "Just a little huh? Ahaha~"
            m 1pn "Well, you can tell your helpers I said thank you for their work."
            m 1pe1 "But I know you saw something in it personally and picked it out for me."
            m 1pk "It's so perfect, thank you so much [player]!"
            show monika 1pj at face with dissolve
            "Monika leans over and wraps her arms around me."
            show monika 1pa at t11
            show monika at s11
            $ mbend = 1
            $ MonikaVar += 2
            stop music fadeout 1.5
            play music t8
        elif gift == 2:
            "Monika holds the long box to her ear, giving it a light shake."
            m 1pl "Hmm, I can't tell what it is."
            show monika 1pm
            mc "Open it! You'll see what it is then."
            m 1pk "But I like to guess first."
            m "I'm going to say..."
            m 1pb "A fancy piece of jewelry?"
            show monika 1pa
            mc "Maybe, just open it all ready."
            show monika 1pj
            "I try and hide my slight panic at her accurate guess with a big smile."
            "Monika tears away the wrapping paper to reveal the festive box."
            show monika 1pc
            "Lifting off the lid slowly, Monika's eyes grow wide."
            m 1pd "Gosh [player], this necklace..."
            m 1pb "It's so cute! It even has a little note charm on the bottom!"
            m 1pd "Where did you find this?"
            show monika 1pc
            mc "Well uhh..."
            show monika 1pe
            mc "I may have had a little help..."
            m 1pl "Just a little huh? Ahaha~"
            m 1pn "Well, you can tell your helpers I said thank you for their work."
            m 1pe1 "But I know you saw just how beautiful it would be on me!"
            m 1pk "Thank you so much [player]!"
            $ MonikaVar += 1
        elif gift == 1:
            show monika 1pa
            "Monika turns her gift over in her hands, looking at it from different angles."
            m 1pl "Well, I think I could give a pretty good guess as to what this is ahaha~"
            show monika 1pe
            mc "Well, maybe it isn't what you think it is. There is always that possibility."
            m 1pa "A surprise, maybe..."
            m 1pk "Let's find out!"
            show monika 1pj
            "Digging her nails under the paper, she tears the wrapping paper away."
            show monika 1pd
            m "Oh!"
            m 1pl "Oh my gosh, [player]! Ahaha~"
            mc "What? Is it bad?"
            m "No no, it's really sweet of you to get me such a nice poetry collection."
            m 1pn "It's just, do you remember what I told you about this poet, [player]?"
            show monika 1pe
            mc "Yeah um... you said..."
            "I try my hardest to remember that conversation but my memory is failing me big time."
            m 1pl "I said that I was never really a fan of his work, you just remembered his name didn't you?"
            show monika 1pe
            mc "I uh, no... I thought I remembered you... saying that you..."
            mc "Gosh I'm sorry, I thought it was a poet you liked.."
            m 1pe1 "[player], don't look so upset. I still really appreciate you spending the time trying to find me a gift."
            m 1pk "It's the thought that counts, right?"
            show monika 1pj
            mc "Yeah, but..."
            m 1pe1 "It's also really heartwarming you remembered that little talk we had, I would have thought it went in one ear and out the other."
            m 1pn "I never said I {i}hated{/i} his poems either, maybe I'll see them in a new light now."
            m 1pe1 "It's still a wonderful gift, [player], thank you."
            show monika 1pe
            mc "Really? Are you sure?"
            m 1pk "Yup."
        m 1pb "Now it's your turn, [player], open your gift!"
        show monika 1pa
        mc "Okay okay, let me see here.."
        "I take the gift into my hands and find myself hesitating."
        show monika 1pe
        "Looking at the shape of the gift, it's not anything I could immediately guess. It's strange pyramid shape almost seemed like there was multiple things tucked inside."
        m 1pl "Come on [player], open it already!"
        show monika 1pm
        mc "Hey, I wanted to guess too though."
        m 1pn "Okay fine you can guess."
        show monika 1pe
        mc "It's fine, I didn't have a clue anyway."
        show monika 1pa
        "I dig my fingers into the paper and tear it away."
        show monika 1pl
        "The contents of the package spill into my lap as I try to not let them fall."
        show monika 1pe
        mc "Oh wow..."
        "In my lap sat the newest couple of volumes for my favorite manga and a new copy of Ring: The Captain's Collection."
        mc "Thank you Monika, these are amazing!"
        m 3pe1 "Oh its nothing [player], I'm really glad you like them."
        m 1pb "I heard that game was kinda similar to the one we played you know."
        m 3pk "So we definitely need to play that on a rainy day, ahaha~"
        show monika 1pj
        mc "Definitely, but no cheating like last time though."
        m 1pn "I didn't {i}cheat{/i} last time, I was just playing the game."
        m 1pe1 "And besides, I think we both liked the outcome of that anyway~"
        show monika 1pe
        "Well she does have me there, but still..."
        if gift > 1:
            m 3pn "I also had a little bit of help tracking down those books, ahaha~"
            m 1pn "I guess we both have to thank the club for their help this Christmas."
            show monika 1pe
            mc "Yeah, I guess we will."
        elif gift = 1:
            m 3pn "Those manga volumes were a whole different story though."
            m 1pl "I had no idea they were so hard to find, ahaha~"
            m 1pn "So I had a tiny bit of help finding the right ones for you."
            show monika 1pe
            mc "Oh really, well I guess I don't feel so bad now for getting help."
            m 1pe1 "Oh it's alright [player], we'll both thank the girls for helping out this Christmas."
            show monika 1pc
            mc "Wait, you knew I asked them?"
            m 3pl "Well it {i}was{/i} pretty obvious, ahaha~"
            show monika 1pl
            mc "Yeah, I guess it was..."
            "Damn, so she was on to me that whole time..."
        m 1pb "[player], open the card that I put in there too!"
        show monika 1pa
        mc "What card..."
        "I flip over the game case and find a red envelope stuck to the back."
        "I peel it off the case and into my hands."
        show monika 1pm
        "The front has my name written inside a large drawn heart."
        "I flip the envelope over and try to gently open the flap."
        show monika 1pa
        "With enough patience the envelope opens and I remove the card."
        call showpoem (poem_m5, track= t6, revert_music=False, where=truecenter)
        show monika 1pe at t11
        "Once I finish reading, I feel a new found warmth growing in my chest as I turn to Monika with a smile."
        m 1pe1 "I really do mean all of that [player], this Christmas has been everything I've ever wanted and I'll always remember it."
        m "Thank you, truly, for spending yesterday and today with me."
        show monika 1pe
        mc "Monika, I wouldn't have wanted it any other way."
        show monika 1pj at face with dissolve
        "I move over to Monika and pull her into a hug."
        "Her lips moved to mine and we locked together in heated passion."
        scene black with close_eyes
        "It felt like the whole world melted away as we kissed."
        "I really couldn't be more thankful for her being right beside me."
        "It just wouldn't have been the same without her."
        "From here on out, I don't think any Christmas will be the same without her."
        scene mroom with open_eyes
        show monika 1pe at face with dissolve
        mc "I love you Monika."
        m 1pe1 "And I love you too, [player]."
        m 1pn "Gosh I wish we could stay like this forever."
        show monika 1pm
        mc "Me too, I really wish I didn't have to leave so soon."
        m 1pe1 "It's okay, I understand. I'm happy we got to spend the night together and share gifts at least."
        show monika 1pe
        mc "Yeah but still..."
        m 1pe1 "There is always next year, and the year after that."
        m "I wouldn't want to look bad by keeping you from your family, [player]."
        m 1pk "Come on, I'll walk you downstairs."
        show monika 1pa at t11
        "Monika gets up from the bed and reaches one hand out to me."
        "I gladly take it and rise to my feet."
        show monika 2pa
        "I pack my clothing and gifts into my bag and sling it over my shoulder, taking extra care not to bend or crease the poem."
        "Once everything is packed I take one last look around the room."
        "Part of me is looking for anything I may have forgotten and another trying to take in every detail before I leave."
        "I know I will see this room again, but I still try to remember everything regardless."
        "Monika tugs my hand after a few moments, and I take it as we head back downstairs."
        scene bg h_livingroom with wipeleft_scene
        show monika 1pa at t11
        "We return to the living room to find Monika's parents exchanging gifts of their own."
        y "Ah there you are! Me and your father were just opening a few gifts while you two were upstairs."
        y "I'm really sorry you have to leave so early, [player]. I'm sure we'll have another time to get more acquainted, ahaha!"
        "Monika's mother gets up from the couch and makes her way over to us."
        show monika 1pm at t41
        "She wraps her arms around me in another hug, and I try to return the favor as gracefully as I could."
        if e1c8 == 1:
            "Even as she hugged me so passionately, I couldn't help but think of what Monika said last night."
            "Did she really not like me being Monika's boyfriend? Was she really hiding it under this mask of friendliness?"
            "Whatever it was, I'm gonna show her I'm better than any other guy she could have brought home."

        elif e1c8 == 0:
            "With all this hugging and praise, I think I got both parents on my side."
            "I never thought it'd be that easy to do, with all the stories I've heard."
            "I celebrate in my head as Monika's mother squeezes the life out of me."
        show monika 1pe at t42
        "After what seemed like forever, she finally released me and I finally breathed air again."
        y "It was a pleasure meeting you [player], please have a safe trip home."
        show monika 1pm
        n "Yes, have a safe trip home [player], I wouldn't want to hear I won't be seeing you around any time soon."
        "Monika's father gives me a pat on the shoulder after he walks over from the couch."
        mc "Of course, it was nice meeting you two. I hope we meet again soon."
        "I give a small bow and smile to show my gratitude. They do seem like nice people, and getting to know them better will only help me in the long run with Monika."
        show monika 2pe at t11
        mc "I guess this is the part where I make my leave."
        m 2pn "If you really want it to be, I mean you could stay if you wanted to..."
        show monika 2pn
        mc "I would if I could, but I can already feel my mother wondering where I am."
        m 2pe1 "I know, I'm just giving you a hard time."
        m 1pe1 "Come on, I'll walk you out."
        show monika 1pe
        "I follow her to the front door, giving one last wave to her parents."
        scene bg h_residential with wipeleft_scene
        $ y_name = "Yuri"
        $ n_name = "Natsuki"
        "As Monika reaches the door and opens it, I take a step out the door to take in the cool air."
        show monika 4pe1 at t11
        m "Another green Christmas, I was really hoping for snow last night."
        m 2pe1 "It would have made it that much more special..."
        show monika 2pe
        mc "Maybe next year, and it was still one of my best Christmas Eve's to date."
        mc "Thank you for having me over."
        m 1pe1 "Oh [player]..."
        show monika 1pj at face with dissolve
        "Monika steps out from the door and into my arms."
        mc "Monika, it's freezing out here! You'll catch a cold!"
        m 1pk "Not while I'm covered up in your warmth!"
        show monika 1pj
        "We stay like this for a few moments more, standing in the cold wrapped in each other's arms."
        mc "Come on, your gonna get sick if you stay out here any longer."
        m 1pg "But I want you to stay here, with me."
        show monika 1pm
        mc "We have all the time in the world Monika, I'm sure I'll be seeing you tomorrow, and the day after that, and the day after that."
        m 1pn "Okay, okay, I really am just holding you hostage at this point."
        show monika 1pe at t11
        "Monika unwraps herself from me and retreats back to the warmth of the door."
        m 2pe1 "I'll see you tomorrow, okay [player]?"
        show monika 2pe
        mc "I'll be patiently waiting for you then."
        mc "I love you Monika, see tomorrow."
        m 3pk "I love you too [player], see you tomorrow!"
        show monika 2pa at thide zorder 1
        hide monika
        "I watch her close the door behind her and start to make my way back to my house."
        "We both must have forgotten that the buses don't run on holidays, and Mom and Dad were stuck cooking with the rest of the family."
        "It's fine, I dug my own grave on this one. I need the exercise anyway."
        "I try to distract myself from the long walk home with a festive playlist."
        "As the songs fill my ears, I can't help but drift back to last night and today."
        "I never did think I'd ever spend a Christmas with a girl, nevermind someone like Monika."
        "I still don't know how or why we're a thing and why she loves me so much, but at this point I never want it to end."
        "I march on with the sweet memories of last night and this morning dancing in my head."
        scene black with dissolve_scene_full
        jump m_event2
