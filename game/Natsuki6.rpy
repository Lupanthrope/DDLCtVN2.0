label Natsuki6:
#Start Scene 11 - Never What it Looks Like

    # Good Ending
    if ((karma >= 4) and (is_end == False)):
        $ is_end = True
        call Natsuki64
    
    # Bad Ending
    elif ((karma < 0) and (is_end == False)):
        $ is_end = True
        call Natsuki61
    
    else: # (0 <= karma < 4)
        # Sayori Ending
        if ((end_dir == "SN") and (is_end == False)):
            $ is_end = True
            call Natsuki 62
            
        # Yuri Ending
        elif:
            if ((end_dir == "YN") and (is_end == False)):
            $ is_end = True
            call Natsuki63
            
        # Good Ending (failsafe)
        else:
            $ is_end = True
            call Natsuki64

    "Thank you for playing DDLCtVN Natsuki Route!"
    return


label Natsuki61:
#Start Scene 11a - Bad Ending
    scene bg bedroom
    with dissolve_scene_full
    "And so this is Christmas."
    "Well, rather, it's the day before Christmas."
    "For being the most wonderful time of year..."
    "I gotta be honest, it kinda just feels like any other day."
    "I guess some of that magic gets sapped out when you've got to do all the responsibility stuff on your own."
    "My parents are supposed to be back tomorrow though, so hey, I guess that's something I can look forward to."
    "Speaking of looking forward to things, I spit out my toothpaste, wipe my mouth, and head downstairs where I find breakfast waiting for me on the counter."
    scene bg kitchen
    with wipeleft_scene
    "Oddly enough, though, no sign of the cute girl who's responsible for it."
    n "Look who's finally up."
    "I turn my gaze over to her."
    play music t5_natsuki
    show natsuki 1bg at t11 zorder 2
    "She's got her food on the table, and she's sitting down, though it seems she hasn't eaten yet."
    mc "Merry Christmas to you too, Nats."
    "We stare at each other for about a second. A smile breaks out on her face, which kills the tension in the room."
    n 2bl "Merry Christmas, [player]! Ahaha~"
    "I grab my own plate and take the seat across from her, as usual."
    "I take the time to observe what's been laid before me."
    "Chocolate pancakes, inside of which there appears to be crushed up candy canes."
    "Natsuki can make anything taste good, so I take a bite with full confidence."
    "True to my expectation, it's delicious."
    n 2bd "Well? How are my world famous Christmas Peppermint Chocolate pancakes?"
    mc "Have I ever told you anything you've made was anything less than excellent? ‘Cause if I did, I was lying."
    mc "If it ever happens that something you made doesn't taste amazing, I'd think my tongue has gone bad before I'd assume the food was bad."
    "Her smile only widens, giggling a bit at my unusual compliment."
    n 5bz "Maybe I'll bake something gross next time then. I've always been looking for an excuse to cut off that tongue of yours!"
    "As if it'd be able to get the job done, she holds up her butter knife and points it at me."
    "Her giggles turn into a full on laugh as I pretend to be threatened."
    mc "Well, other than cutting off my tongue, what's the plan for today?"
    mc "Not a bunch of cheesy romance anime, I hope."
    show natsuki 4bg
    "The smile wears off on her face and turns to a look more stoic."
    "She pulls out her phone and lays it on the table."
    n "I got a text from Monika. We're expected at the literature club."
    n 4bh "For what, I'm not certain, but..."
    mc "She's crazy. It's negative five hundred degrees outside and it's Christmas Eve."
    mc "Isn't school closed...?"
    n 3bb "You'd think, right? No, apparently it stays open through holidays so kids who don't have food otherwise can get some to eat."
    mc "Those poor kids...if starving is zero, then school lunch is a negative number."
    mc "Talk about being between a rock and a hard place."
    n 2bk "Hey, when we first met, you had no problem downing that stuff."
    mc "Yeah, but that was before I started dating a world class chef."
    n 2bl "Hah, good point."
    n 1bb "Well, anyway, I don't really think we should blow Monika off."
    n "If she's gonna call us in today of all days, it's probably real important."
    n 5bc "What do you think?"

    menu:
        "I think..."
        "We should go.":
            mc "Yeah, you're probably right."
            mc "I wonder if she's gathering the entire club, though."
            mc "She certainly didn't text me about it."
            "Natsuki shrugs."
            n 5bz "She probably thinks you're a beta."
            mc "How does that make any sense?"
            n 5bl "It's not a beta's place to ask questions."
            mc "I might throw something at you."
            n 1bz "Ahaha~!"
        

        "We should stay.":
            mc "Nah, you know what? Like I said, it's Christmas Eve."
            mc "If it's that important, she can come over here."
            mc "And I doubt that it's that important, because she didn't even send me a text about it."
            "Well...at least, my phone didn't buzz."
            "Natsuki shrugs."
            n 5bz "She probably thinks you're a beta."
            mc "How does that make any sense?"
            n 5bl "It's not a beta's place to ask questions."
            mc "I might throw something at you."
            n 1bz "Ahaha~!"
            n 5bt "But honestly, we should probably just suck it up and go."
            n "What's the worst that can happen?"
            mc "I guess you're probably right."
    
    n 4bj "Then it's settled."
    n "Should we go now?"
    mc "Yeah, we should at least get it out of the way."
    mc "That way, the rest of Christmas Eve is open for us two to do whatever we want together."
    n 1ba "Sounds like a plan!"
    show natsuki at thide
    hide natsuki
    "She arises from her chair, and I do the same."
    stop music fadeout 1.5
    "The two of us go change into our school uniforms, grab some warm coats, and make our way to the school."
    scene bg club_day
    with wipeleft_scene
    play music t3
    "Well, I didn't expect to be back here, but the clubroom looks how I remember it."
    "Mostly, anyway. Seeing it in this light makes things feel a little different. A bit less...stuffy, than usual."
    "Walking through the familiar doorway, I find only Monika is there to greet us."
    show monika 1b at t11 zorder 2
    m "[player], Natsuki. Glad to see you two could make it."
    mc "Yeah, and it's especially nice that we didn't lose our fingers trying to get here."
    mc "Is it just us three, or...?"
    m "We're missing one more person, but she should be on her way."

    if (end_dir == "YN"):
        m 2d "Actually, I'm surprised Sayori didn't tag along with you two."
        "For some reason, it feels like that's a dig at me, for not checking in on Sayori."
        "Though maybe that's just guilt."
        mc "Knowing her, she's probably still sleeping."
        mc "If Yuri gets here first, I guess I'll try calling her."
        show monika 1f
        m 1g "Yuri..."
        m "Yuri left the club, remember, [player]?"
        mc "Oh, yeah..."
        "Man, I completely forgot about that."
        "Now I really feel guilty, seeing as that was sort of my fault."
        mc "I'll try to get a hold of Sayori right now, then."
        m 1e "Alright, that works well enough. You can sit down, by the way."
        show monika at thide
        hide monika
        "That sounds good to me. I turn around and notice Natsuki has already sat down, and I take the desk next to her."
        "I pull up my phone and call Sayori."
        "After twenty seconds, she answers."
        "Judging by the sleepiness in her voice, I woke her up."
        "I inform her she's expected at the literature club, and remind her to wear warm clothes."
        "She tells me she'll be there in a bit and hangs up the phone."
    else:
        m 2c "Though, honestly, it being Yuri, I'm shocked she isn't here already."
        m "I guess maybe I should try giving her a call."
        m 2a "Meanwhile, [player], you can give your legs a break and sit down."
        mc "Eheh... right."
        show monika at thide
        hide monika
        "With that, I take the seat next to Natsuki."
        "Monika calls Yuri up."
        "I don't really pay attention, but afterward she relays to us that Yuri should be here in about fifteen or twenty minutes."
        "After that it's total silence."
    
    "Another awkward moment passes the three of us by as we all just sit here."
    "Monika acts like she's busy, but she's pretty much just taking papers out of a cabinet and putting them in another one."
    "Thinking of nothing else to break the ice with, I decide to ask Monika what's going on."
    mc "So, what did you call us all here for, anyway?"
    show monika 1g at t11 zorder 2
    m "It's regarding the club."
    m 3d "You see, in order for a club to qualify officially in the eyes of the school, it has to have at least five members, as of this upcoming semester."
    m 3n "Administration recently caught wind that our club has been narrowed down to only four."
    m "Essentially, they've told me that until I rectify this, the Literature Club won't be recognized."
    m 1n "They're expecting an answer, well..."
    m 1r "By the end of the day today."
    m 2p "I might've procrastinated a bit..."
    mc "This...isn't something that could have been talked about over a group text?"
    m 1n "Well, it might've been, but I'd have to be here to tell them in person anyway."
    m "I thought I might as well have everyone here so we can have a full conversation."
    "I don't really get the thought process."
    "Then again, I seldom understand what goes on in Monika's head."
    "Natsuki's face shifts to one of anger."
    "Realizing how this might end, I pull her in and whisper to her."
    mc "Hey, Nats..."
    mc "I don't really understand Monika's logic either."
    mc "But there's no use complaining about it when we're already here."
    mc "Might as well just calm down and wait."
    stop music fadeout 1.5
    "She doesn't take the courtesy of whispering back."
    show monika 1o at t21 zorder 2
    show natsuki 2e at f22 zorder 3
    n "Yeah, well, you know what, I think there is use complaining about it."
    n "The use is that I'm mad and it should be known why."
    n 5x "Seriously, dragging us out because you had to be here?"
    n 5e "You know, the kind of thing you take on your shoulders when you sign up to be the president of a club?"
    show natsuki 5g at t22 zorder 2
    show monika 1q
    "Monika looks down, seemingly ashamed."
    "I feel the need to stick up for her."
    mc "C'mon, Natsuki, be more fair."
    mc "We're the whole reason she's in this mess as it is..."
    show natsuki 4e at f22 zorder 3
    n "Really? You don't think it's the fault of the person who left for no reason? Because she hated me?"
    n 1o "Or do you think she was right to hate me, huh?"
    n "And that's justification enough for Monika to drag us all the way out here in the freezing cold for something we could have done over a text?!"
    show natsuki at t22 zorder 2
    mc "Listen, it's not that I'm blaming you, it's just..."
    "Monika chimes in."
    show monika 1d at f21 zorder 3
    m "I dunno, to me it sounds like you are..."
    "Wait, whose side are you even on?"
    m 3d "I mean, the only reason she left in the first place was because of Natsuki."
    m 3h "Clearly, you can see that too, can't you, [player]?"
    show monika 1h at t21
    mc "That's not what I..."
    "Natsuki's anger quickly devolves as tears begin to leak out of her eyes."
    show natsuki 12h at f22 zorder 3
    play music t10
    n "Is...is that how you really feel?"
    n 12i "Do you even like me at all, [player]?"
    show natsuki 12h at t22 zorder 2
    mc "Of course I do! Why would I let you live with me if I didn't?"
    show natsuki 12i at f22 zorder 3
    n "I don't know, why would you sit there and tell me you forgave me when you clearly never did?"
    n 12f "Has anything you've ever said to me been true?"
    show natsuki at t22 zorder 2
    mc "Natsuki, please, you're overreacting--"
    show natsuki 42a at f22 zorder 3
    n "You know what I've realized, [player], just now?"
    n 42c "The thing that made her leave wasn't me. It was you."
    n "An entire friendship, gone, just because you showed up."
    n "And now you're about to take the club with you."
    n 42g "Instead of taking the blame for it, you use me as a scapegoat."
    n 12f "I don't think I can share a house with a guy like that, or spend my life with a guy like that."
    show natsuki at t22 zorder 2
    "It felt as if those words were being delivered in slow motion. The rest of the world suddenly disappeared, all I could process was Natsuki saying them."
    "Without another word, she runs out of the club, and the world begins to move again."
    show natsuki at thide
    hide natsuki
    show monika at t11 zorder 2
    mc "..."
    mc "What...what just happened?"
    m 2i "For starters, I think we lost another member of the club."
    "...if she wants to make jokes like that, that's gonna be two members of the club she loses."
    mc "I just...why'd she react like that?"
    mc "Or rather, why didn't she let me talk to her...?"
    mc "Normally I can console her when we're arguing..."
    m 1g "Honestly, it's probably just that she already felt betrayed."
    m 4g "I have no doubt this is a sensitive subject for her."
    m 2p "Sorry, I..."
    m "I was hoping that if I agreed with you, she might recognize that she's the only person in the room who feels the way she does."
    m 2o "And that she might change her mind..."
    "It probably only made her feel cornered, and had her lash out further."
    "It doesn't surprise me that Monika made a mistake like that. She's not exactly the most comforting friend around."
    m 2i "You have a very judgmental look on your face right now, [player], and I don't appreciate it."
    mc "Well I don't appreciate you getting in the middle of my relationship again, Monika."
    m "I'd watch my tone if I were you."
    mc "Oh really, so I'm on thin ice now?"
    mc "Just because you've done nothing but shower us with empty support and want me to take responsibility for {i}your{/i} selfishness?!"
    m 4i "I'm not one to coddle anybody. I try to look at disputes from an unbiased perspective, and I will not apologize for that."
    "I look at Monika with disdain."
    mc "You're so robotic, Monika. You don't understand anyone's feelings whatsoever."
    mc "And your apathy might have just ruined my life."
    mc "Merry Christmas. I'm getting out of here."
    m 1h "Oh so now you're just going to leave the club too, and destroy something important to me?!"
    m 5b "The literature club means everything to me! And now you're going to ruin it!"
    m "I'm not the selfish one here, [player]!"
    "Maybe in her mind she's the victim, and in my mind I am."
    "To someone neutral, we might've both been in the wrong."
    "But I'm not going to stand here and act like I'm not pissed."
    mc "This is goodbye to you and the club, Monika."
    mc "You pushed us away. I hope you're happy with yourself."
    show monika at thide
    hide monika
    scene bg corridor
    with wipeleft_scene
    "I rush my way out of the club, hoping to catch up with Natsuki. However, it doesn't seem like she's anywhere around."
    "I guess my best bet would be to try and meet up with her at my house."
    
    if(end_dir == "YN"):
        scene bg house
        with wipeleft_scene
        "Before I can enter my house, I'm stopped by someone."
        show sayori 4p at t11 zorder 2
        s "[player]!"
        mc "H-hey, Sayori."
        s 1h "Is everything alright?"
        s "I saw Natsuki storm in, and she looked angry..."
        s 2g "Said she and you got into a fight and that she was leaving..."
        mc "Is she still in there? I want to try talking to her."
        s 1k "I didn't see her leave, so..."
        show sayori at thide
        hide sayori
        "We both rush into my house."
        scene bg livingroom
        with wipeleft_scene
        "When we get in, there's no sign of Natsuki anywhere."
        "I check the entire house, even my room, nothing. Though, her box is gone, and so is most of her stuff."
        "It's only when I check the back when I notice the rear door is open, and that her key was dropped on the ground in front of it."
        mc "I can't believe she managed to clear out this quickly..."
        "I stand in my living room, staring at nothing in particular."
        show sayori 1e at t11 zorder 2
        s "So..."
        s "What exactly happened?"
        mc "Well..."
        show sayori at thide
        hide sayori
        scene black
        with fade
        scene bg livingroom
        with fade
        show sayori 4o at t11 zorder 2
        mc "And then she just up and left."
        mc "It must've been a few minutes before I finally got up and went after her. That's when I caught up with you."
        s 3k "I see..."
        s "Gosh, it sounds..."
        s 3v "Like she kind of just snapped..."
        mc "I don't get it, either..."
        mc "Did I...was I a bad boyfriend?"
        mc "Damn it, I wish I could've gotten the chance to talk to her."
        show sayori at thide
        hide sayori
        "I wish I could have gone back to where this all started and did things differently."
        "Unfortunately, it's not like real life has some sort of save-and-load feature."
        "Sayori gives me a hug, to try and comfort me."
        "It doesn't really help."
        "It makes me start to miss her..."
        "God, how am I going to explain to my parents that I lost my girlfriend the day before Christmas?"
        "This isn't the way any of this was supposed to turn out."
        "I pull myself away from Sayori gently and sink into my couch."
        "There I sit, and begin staring again."
        "No thoughts are in my mind. Just staring, for what feels like an eternity."
        "An eternity..."
        "An eternity I can be spending with the girl I love."
        "I'm not taking this lying down."
        "I stand up and wordlessly leave Sayori where she sits, then put on my shoes and walk out the door."
        
    else:
        scene bg livingroom
        with wipeleft_scene
        "When I get in, there's no sign of Natsuki anywhere."
        "I check the entire house, even my room, nothing. Though, her box is gone, and so is most of her stuff."
        "It's only when I check the back when I notice the rear door is open, and that her key was dropped on the ground in front of it."
        mc "I can't believe she managed to clear out this quickly..."
        "I stand in my living room, staring at nothing in particular."
        "I drop myself hopelessly onto my couch, a whirlwind of emotions running through my head."
        "Pained."
        "Frustrated."
        "Useless."
        "Pathetic."
        "What could I have done differently?"
        "Can I truly put the blame entirely on Monika?"
        "There has to be more to it than that."
        "I could've handled some things so much more delicately, and more sensibly."
        "I feel like a politician who was given too much power too quickly, and now I've ruined everything in my wake."
        "Did I...was I a bad boyfriend?"
        "Damn it, I wish I could've gotten the chance to talk to her."
        "I wish I could have gone back to where this all started and did things differently."
        "Unfortunately, it's not like real life has some sort of save-and-load feature."
        "God, how am I going to explain to my parents that I lost my girlfriend the day before Christmas?"
        "This isn't the way any of this was supposed to turn out."
        "I pull myself into the living room and sink into my couch."
        "There I sit, and begin staring again."
        "No thoughts are in my mind. Just staring, for what feels like an eternity."
        "An eternity..."
        "An eternity I can be spending with the girl I love."
        "I'm not taking this lying down."
    
    scene black
    with fade
    scene bg residential_day
    with wipeleft_scene
    "To the best of my abilities I navigate myself to a place I never hoped I'd have to venture to."
    "Natsuki has very few options outside of me, and I recall an encounter she and I had recently."
    "A certain someone had offered to let her come home if she ever felt up to it."
    "This is the same someone whose actions led to Natsuki living with me in the first place."
    "Soon enough, I find myself in front of Natsuki's childhood home."
    scene bg cafe
    with wipeleft_scene
    "Heart pounding, I walk up the steps of this place, and ring the doorbell."
    "A moment later, it opens."
    show katashi 1a at t11
    "..."
    k 5d "...oh. It's you."
    mc "Is Natsuki here?"
    k 5f "She is. But she'd rather you leave her alone."
    mc "Please, I need to speak to her."
    k 1e "I'm going to say this once and only once..."
    k 2g "Get off my property, and leave my daughter alone."
    k 1h "That isn't me saying that as someone who's trying to control her, either."
    k 5d "That's me respecting my daughter's wishes for the first time in her life."
    k 5j "I've done what I could to change for her."
    k 1k"And I'm not jeopardizing my second chance with my princess just to give you yours."
    k 1l "Leave. Now."
    show katashi 1l at thide
    hide katashi
    "He shuts the door on me."
    "I don't want to give up, but I know what this man has been through."
    "He worked hard to win his daughter back."
    "I don't have that strength, or that resolve."
    "Without Natsuki, I'm nothing."
    "Without Natsuki, I'm a shell of myself."
    "{i}Without Natsuki, I can't win back Natsuki.{/i}"
    "I'm at the end."
    "I've lost her."
    "And I've lost everything that came with her."
    "I'm back at square one, back to being a zero."
    scene black
    with fade
    "{i}This wasn't supposed to happen.{/i}"

    scene bg ending_h
    with dissolve_scene_full
    window hide
    pause(5)
    scene black
    with fade

    return
#End Scene 11a - Bad Ending
#{ END OF NATSUKI ROUTE - BAD ENDING ACHIEVED }
#NO SECOND C(H)ANCES


label Natsuki62:
#Start Scene 11b - Sayori Neutral Ending
    scene bg bedroom
    with dissolve_scene_full
    "It's Christmas Eve."
    "It's been a few weeks since my relationship with Natsuki hit a bit of a roadblock."
    "A roadblock named Sayori..."
    "This is a very awkward situation for me, because Sayori and I haven't talked once in all that time."
    "Monika told me she'd handle this situation with Sayori while I make sure to mend my relationship with Natsuki."
    "I think I've done a decent job of doing so, having taken her to see the Christmas lights and then going with her to visit her mom's grave."
    "I've done my best to redeem myself in her eyes, and she and I are mostly back to being on the same page."
    "However, the Sayori predicament is still hanging over us."
    "We never even talk about her or what happened on that day, but when Natsuki and I are together I feel like there's still a bit of tension between us."
    "I mentioned that it's an awkward situation, and it is, because Sayori and I give each other something for Christmas every year."
    "This year I haven't bought her anything, and I feel really bad about that. But the worst part is that I have no idea if she got me anything."
    "I leave my bedroom and walk to the kitchen, still thinking about Sayori."
    scene bg kitchen
    with wipeleft_scene
    play music t5_natsuki
    "Natsuki is in the kitchen making something that smells heavenly."
    mc "Good morning, Nats, Merry Christmas."
    show natsuki 4bl at t11 zorder 2
    n "Merry Christmas!"
    "She walks up to me and wraps her arms around me, then she stands on her tippy toes to give me a kiss."
    mc "Making something special for us?"
    n 3bj "Sure am!"
    n "They're my famous Christmas Peppermint Chocolate pancakes."
    mc "Wow. That sounds incredible."
    n 5bz "You better believe it. It's gonna blow you away. Hehe~!"
    mc "Heh, I don't doubt it..."
    n 5bn "..."
    n "[player], are you okay?"
    n "You look down."
    mc "..."
    mc "Eheh, I do?"
    mc "Well, that is..."
    stop music fadeout 1.5
    mc "Natsuki, we need to have a talk."
    n 4bt "A-about what?"
    mc "I think you know what, Natsuki."
    show natsuki 4bg
    "Natsuki looks at me in such a way that affirms my assumption."
    "She knew it was coming sooner or later."
    mc "We've avoided talking about Sayori for way too long now."
    n 2bh "[player]..."
    n 2bi "I don't want to--"
    mc "Nats, we have to."
    mc "It's too huge to just forget about."
    play music t10
    mc "I let Sayori kiss me."
    mc "I royally, royally screwed up."
    mc "I wish I could say I'm sorry every second of every day until you forgive me."
    n 3bk "[player], I do forgive you."
    mc "B-but that night you said that nothing would be the same again."
    mc "I want to believe what you say, but I don't feel like I faced enough repercussions for what happened that day."
    n 1bm "[player], please trust me."
    n "I meant what I said that night about things never being the same, but..."
    n "I didn't mean that I wouldn't forgive you."
    n 2bn "I..."
    "Natsuki begins tearing up."
    show natsuki at thide
    hide natsuki
    stop music fadeout 1.5
    "She then walks over to the stove and turns it off."
    "Thankfully she hadn't begun cooking the batter yet."
    mc "Nats?"
    "Natsuki wordlessly walks by me, but grabs me by the hand and starts walking me toward the front door."
    "I'm alarmed at her suddenness and also the strength with which she pulls me that I simply begin to slide across my living room floor."
    "Without letting either of us even put shoes on, Natsuki opens the door and walks out, and she continues to lead me."
    scene bg house
    with wipeleft_scene
    mc "Nats, where are we going?"
    "She doesn't answer me, but using context clues I'm able to figure out where the two of us are headed."
    "I can't believe we're actually doing this."
    "A moment later, Natsuki and I are approaching a familiar front door, one I've become very well acquainted with over the last several years, but estranged with over the last several weeks."
    "Natsuki knocks on the door and a few moments pass without hearing anything."
    "I decide to take the liberty of opening the door and walking inside, since Sayori doesn't seem to be responsive at the moment."
    scene black
    with fade
    scene bg sayori_hall
    with dissolve
    "I feel so awful, is it possible she's been down for four straight weeks?"
    "I really wish I could've been there for her."
    mc "Sayori? Are you awake?"
    "I don't hear a response."
    "Natsuki and I walk together toward Sayori's bedroom."
    show natsuki 1bu at t11
    mc "Sayori, are you here?"
    "I put my ear to the door, and listen. I can hear some light snoring coming from inside, but something tells me they're fake."
    mc "Sayori, I can tell you're not asleep, could you answer me please?"
    s "[player]?"
    "I'm comforted to finally hear her voice."
    mc "S-Sayori, could you let me in?"
    show natsuki 2bc at d11
    "Natsuki nudges me with her elbow, and I realize it's because I've been saying 'me' and not 'us.'"
    "We don't want Sayori too caught off guard if she realizes Natsuki is here."
    "I clear my throat."
    mc "Natsuki and I want to talk with you."
    s "..."
    s "I don't wanna see her."
    n 1bq "S-Sayori? Why?"
    play music t10
    s "Because you hate me!"
    s "I ruined your life..."
    s "You shouldn't have to look at me ever again!"
    n "Sayori..."
    n 1br "I don't...hate you."
    s "And I don't believe that."
    n 1be "Listen to me!"
    n 4bw "I said I don't hate you! But that doesn't mean I'm not upset with you, of course I am!"
    n 5br "But if I've learned anything lately is that people deserve second chances, and I won't get anywhere by pushing people away the second they wrong me."
    n 5bs "I just wanna talk so we can sort this out. Can we do that?"
    "..."
    "There's a marked silence between the two rooms for a solid ten seconds before one side decides to break it."
    s "Come in."
    scene bg sayori_bedroom
    with wipeleft_scene
    show sayori 1bk at t21
    show natsuki 5bi at t22
    "We walk in and Sayori and Natsuki instantly lock eyes with each other."
    "It's one thing speaking on two sides of a door, but I have to imagine looking each other in the eye right now is quite a task given what happened the last time they shared a room."
    "I...really wish I'd have done something differently then."
    "If I put the blame wholly on Sayori I'd be a real piece of crap."
    show sayori 1bg at t21
    "Sayori then looks at me briefly."
    "I force an uncomfortable smile. I look at my reflection in Sayori's bedroom mirror and realize how much shame I have in my face."
    show natsuki 4bi at f22 zorder 2
    n "So..."
    show natsuki at t22 zorder 2
    show sayori 1be at f21 zorder 3
    s "Yeah...here we are."
    s "Now what?"
    show sayori 1bi at t21 zorder 2
    show natsuki 5bk at f22 zorder 3
    n "Well, we talk, naturally. That isn't something we've had trouble with over the years."
    show natsuki 5bg at t22 zorder 2
    show sayori 2bh at f21 zorder 3
    s "But it's so different now. I did something awful."
    show sayori 2bg at t21 zorder 2
    show natsuki 1bm at f22 zorder 3
    n "You don't have to keep reminding me."
    n "The more you do that the more likely it is that I'll never forgive you. I can't let you sabotage yourself like that."
    show natsuki 1bn at t22 zorder 2
    mc "N-neither can I."
    mc "Sayori, we made a huge mistake that day."
    mc "But it was just as much my fault as it was yours."
    mc "But Natsuki granted me another chance. You should let her do the same for you."
    show sayori 1bk
    "Sayori looks at the ground until she takes a few steps backwards and sits down on her bed."
    show sayori 1bk at f21 zorder 3
    s "This is hard for me."
    show sayori at t21 zorder 2
    mc "Then explain why so we can make it easier."
    show sayori 1bf at f21 zorder 3
    s "..."
    s 1bh "[player], it's because..."
    s "You were my 'what if,' but now you'll always just be my 'never.'"
    show sayori 1bg at t21 zorder 2
    mc "I'm...not sure what you mean."
    show sayori 3bk at f21 zorder 3
    s "I always wanted to tell you how I feel, but never had the guts, and that's when Natsuki made the move I was always too scared to make."
    s 3bl "I blew it, and now I'll never know what could've been."
    s "That's why...that day...I chose to do something just for me, for the first time ever in my miserable life."
    s 4bj "I made you pity me, and I kissed you."
    s "That was the first and only time I'll ever act selfishly, but it was enough to ruin all of the relationships in this room."
    show sayori at t21 zorder 2
    show natsuki 1bk at f22 zorder 3
    n "Sayori, that isn't tru--"
    show natsuki at t22 zorder 2
    show sayori 4bw at f21 zorder 3
    s "HOW?! How isn't it true?"
    show sayori 4bv at t21 zorder 2
    show natsuki 1bm at f22 zorder 3
    n "Because what you did strained our relationship, but it didn't ruin it! I told you, I want to give you another chance!"
    n 4bs "But...since we're at this point..."
    n "I should probably tell you what I was thinking that entire day."
    n "..."
    n 5bb "If I'm being completely honest, I wanted to run in there and tear your lips off your face, Sayori."
    show natsuki 5bg at t22 zorder 2
    show sayori 1bu at f21 zorder 3
    s "..."
    show sayori at t21 zorder 2
    show natsuki 5bb at f22 zorder 3
    n "And I wanted to give [player] a piledriver. That's how upset I was."
    "...yeesh..."
    n 2bq "I felt like I was being betrayed and thrown away and disregarded again, but this time by the two most important people in my life."
    n "The love of my life and my best friend in the world."
    show natsuki 2bc at t22 zorder 2
    show sayori 2bv at f21 zorder 3
    s "I'm...I {i}was{/i} your best friend?"
    show sayori at t21 zorder 2
    show natsuki 3bs at f22 zorder 3
    n "Of course you were, Sayori, and still are."
    n "I wouldn't be the person I am today, or be in the position I am in my life now if it weren't for you."
    n 3bh "You and I have such fond memories with each other, so now you understand why it hurt so bad seeing what you did."
    n 3bu "I...trusted you, Sayori."
    n "And...you, of all people, decided to hurt me."
    show natsuki at t22 zorder 2
    show sayori 1bk at f21 zorder 3
    s "N-Natsuki, I'm--"
    show sayori at t21 zorder 2
    show natsuki 1br at f22 zorder 3
    n "I know, Sayori, I know how sorry you are."
    n 1bn "It'll take some time to forgive you, but as long as you help me out here, I know I can do it."
    n 4bt "But you need to first forgive yourself."
    n 4bm "Sayori...I love you so much, you're a wonderful person and I'm proud to call you my friend."
    n "I want us to be better. To each other, and as people."
    n "I...don't want to lose someone so dear to me."
    show natsuki 4bn at t22 zorder 2
    mc "Neither do I, Sayori."
    mc "I don't know what I'd do without you in my life for good."
    show sayori 1bf at f21 zorder 3
    s "..."
    s 1bj "You have each other."
    s 1bi "I think that should be enough."
    show sayori 1bu at t21 zorder 2
    show natsuki 12ba at t22
    "Natsuki and I are left speechless."
    "The tone of her voice suggests that Sayori's already made up her mind."
    "She doesn't want our help, and she doesn't want our friendship."
    "I wish more than anything that she could see things the way Natsuki and I do, and I'm about to say that before Sayori walks over to her closet."
    show sayori at thide
    hide sayori
    show natsuki 1bm at t22
    "She opens the closet, reaches inside, and pulls out what appears to be a Christmas present."
    mc "S-Sayori...?"
    "Sayori walks up to us."
    show sayori 1bu at t21
    "She looks down at the ground, closes her eyes, and starts tearing up."
    "Soon she begins to sob, and I see her pain-filled tears pour out of her eyes and drop straight onto the carpet below us."
    "Without looking up at us, she holds the present up and presses it into my chest."
    "It's a light, feathery feeling."
    mc "Sayori, what is this?"
    show sayori 1bv at f21 zorder 3
    s "It's...my Christmas gift for you this year."
    s "It'll be...the last one I give you."
    s 1bt "I hope you like it."
    s 1bj "Now would you both please leave?!"
    show sayori 1bi at t21 zorder 2
    "I feel gutted, hearing something so direct, jarring, and intense from Sayori."
    mc "Sayori, please don't say things like th--"
    show sayori 1bw at f21 zorder 3
    show natsuki 1bp at t22
    s "I'M NOT TAKING NO FOR AN ANSWER, NOW LEAVE BEFORE I HURT YOU MORE."
    show sayori 1bv at t21 zorder 2
    show natsuki at thide
    hide natsuki
    show sayori at t11 zorder 2
    "All I can do is stare, but Natsuki must have another agenda, as she starts crying and sprints out of the room."
    mc "..."
    mc "It didn't have to end this way, Sayori."
    s "..."
    s "Yes."
    s "It did."
    show sayori at thide
    hide sayori
    "With that...I take my leave."
    scene black
    with fade
    scene bg bedroom
    with wipeleft_scene
    "I return home, Sayori's present carelessly swinging around in my hand, to the point where I'm surprised the wrapping paper doesn't tear."
    "I walk into my bedroom to see Natsuki lying on her stomach, sobbing into her pillow."
    mc "N-Nats..."
    show natsuki 42bi at t11 zorder 2
    n "Why?! Why does she have to be so stubborn?!"
    n "She doesn't have to be such a self-destructive dummy all the freaking time!!"
    n 42bf "Why wouldn't she let me help her?!"
    "I go over to Nats and hold her tightly, shushing her and kissing her on the forehead, doing my best to comfort her despite the pain I feel myself."
    mc "There's one thing she said in there that I agree with, that me and you have each other."
    n 42bi "Yeah, then she went and said that that's all we need!"
    n 42bf "{i}Why doesn't she realize how important she is to me?!{/i}"
    "I well up with tears hearing this from Natsuki. I almost resent Sayori for saying what she said to us."
    "Sayori said that kissing me was her first and last selfish act, but that isn't true."
    "{i}What she just did to us was far more selfish."
    "Natsuki and I hold each other closely, sharing this pain with one another for several minutes."
    "I suddenly remember that I've been holding this gift in my hand while I've been cuddling with Nats."
    "I say nothing, and with Natsuki's head on my chest, I try my best to open the gift with my left hand."
    "I eventually free the present, and suddenly the feathery weight makes much more sense, as it's revealed to be a Santa hat."
    "I examine it more closely, and turning it around a hundred eighty degrees I see some embroiderment in the rim of the hat."
    "It reads..."
    "‘{i}Natsuki's Man.'"
    "I show it to Natsuki, and for the first time in what feels like several hours she smiles, if a little weakly."
    n 1bu "She's...always been thoughtful."
    n "I'm going to miss that."
    mc "Me too..."
    "I put the hat on my head, and urge Natsuki to look at it."
    "Her expression breaks, and she starts to chuckle."
    "Then she starts to laugh, and then she starts to crack up."
    n 2bt "It looks so silly, but...I really love it."
    n "I'm sure I'll be laughing like a dummy every time I see it."
    show natsuki 2bn at t11
    mc "You know...I bet that's the point."
    mc "Sayori doesn't want to be in our lives, so she left this gift so that..."
    mc "She's always able to make us smile."
    show natsuki 12bf at t11
    "Natsuki starts to sniffle, and cries again."
    n 1bm "I'll miss her, but..."
    n 1bn "I'm so happy to have you."
    mc "So am I."
    mc "I love you, Nats."
    n 1bj "I love you, too, [player]."
    show natsuki at thide
    hide natsuki
    "Natsuki's lips lock with mine, and as we give each other a kiss only fitting for Christmas, I can't help but think of the red bow on a mistletoe."
    scene black
    with fade
    "And when I think of red bows, there's only one other thing that comes to mind."
    "{i}Thank you, Sayori."

    scene bg ending_e
    with dissolve_scene_full
    window hide
    pause(5)
    scene black
    with fade
    
    return
#End Scene 11b - Sayori Neutral Ending
#{ END OF NATSUKI ROUTE -- SAYORI NEUTRAL ENDING ACHIEVED }
#RAINBOW SHAP(E)D VOID


label Natsuki63:
#Start Scene 11c - Yuri Neutral Ending
    scene bg bedroom
    with dissolve_scene_full
    play music t5_natsuki
    "It's Christmas Eve."
    "A day full of preparations, food, and time well spent."
    "...at least that's how I always spent it."
    "I'm not expecting it to go differently, but..."
    "I definitely have a bad feeling."
    "Natsuki's already downstairs, she's probably making a godlike breakfast."
    "I hastily wash myself in the bathroom and put on some better clothes."
    n "[player], hurry up!"
    scene bg kitchen
    with wipeleft_scene
    "I rush to the kitchen thanks to the sweet smell of... peppermint?"
    show natsuki 4bg at t11 zorder 2
    n "Hmph."
    n "You always take so long."
    mc "Yeah, yeah."
    mc "The smell made me come in faster though."
    mc "So what is this magnificent smell I smell?"
    n 5by "This would be my Christmas breakfast."
    n 5bz "Chocolate Peppermint Pancakes with chocolate sauce, whipped cream, peppermint chunks, and a gingerbread cookie."
    "Natsuki puts on a very proud smile on her face."
    mc "You amaze me more every day."
    n 2bt "Eheh... thanks."
    "She forces a smile and turns back toward the stove."
    "Did I say something wrong?"
    "There's like..."
    "A weird aura floating in the room."
    "The lights are on, but the badly opened blinds cover the sunlight up."
    "Natsuki looks like she didn't get much sleep."
    "She's doing her best to try and be cheerful."
    n 1bv "Waaah, it's so hot in there."
    mc "That makes two hot things in the house."
    n 2bq "Yeah, I guess the water heater is also hot."
    "Tch. She's not receptive today."
    "I can see her bags, and her hair isn't done."
    "She probably tried to make the household happier by cooking up such a big meal."
    "But I can see something's wrong."
    mc "Is it ready yet?"
    n 4be "Yeah yeah, sit down and get ready to eat!"
    "Natsuki proceeds to set two plates of heavenly decadent pancakes on the table."
    "They look great enough to eat already, and I prepare to start digging in."
    n 3bd "Hey, hey, easy there, it isn't quite perfect yet."
    "Natsuki walks over to the stove once again and grabs a pan, full of what I can only assume is melted chocolate, enough to make me drool."
    stop music fadeout 1.5
    show natsuki at thide
    hide natsuki
    "As she's walking back to the table, however, disaster strikes, as Natsuki trips over her own foot, and drops the pan, spilling chocolate all over her legs and feet."
    show natsuki scream_casual at t11
    n scream_casual "{i}AGGGHHHH!!{/i}"
    n 1bv "It hurts, it hurts, it hurts, it hurts, it huuuurts!!"
    mc "Natsuki!"
    "I rush to the kitchen and grab a rag, douse it in ice cold water, and put it on her legs."
    n 12bd "[player]..."
    n "I'm so sorry, I'm worthless..."
    n 12bf "I-it hurts..."
    "She starts sobbing violently."
    "The pain isn't coming from her legs."
    "It's coming straight from her heart."
    n "Freaking...chocolate..."
    n 12be "I hate..."
    play music t10
    n "Freaking...Yuri..."
    "Bullseye."
    "I could tell something was wrong, and I was ready to bet it was about Yuri."
    "It's like Yuri's living rent free in her head."
    "Natsuki was so taken up by her, that she didn't watch out and lost balance carrying the pan."
    n 12bi "I can't stand this anymore!"
    n "I've been nothing but kind and respectful to her since we met!"
    show natsuki 12bh at t11
    mc "I mean...is that really true?"
    mc "You two did get into a pretty bad argument when I first joined the literature club."
    mc "Something tells me this tension has never been too foreign."
    n 12bi "Why are you taking her side?!"
    show natsuki 12bh at t11
    mc "I'm not! I just don't want you to think irrationally, Natsuki!"
    mc "All of the altercations that you've had with Yuri recently, each of you played a part in the conflict."
    mc "Nobody here is the good guy or the bad guy. It's not all black and white."
    mc "...that's why I think you, myself, and Yuri need to have a talk, face to face, and sort things out like adults."
    "Natsuki looks at me, first with contempt, but it slowly fades into regret and understanding."
    n 1bs "Then..."
    n "Sure."
    n 1bn "But...how are we gonna do it?"
    "That's a good question."
    mc "I'd go to a café, but if we consider the risk that the discussion will get heated..."
    n 2bq "Yeah, I'd rather not."
    n 2bc "How about here?"
    mc "Here?"
    mc "You mean..."
    mc "In the house?"
    n 5bq "Yep."
    n "That's right."
    n "I think it's the best way to settle this."
    show natsuki 5bs at t11
    mc "But won't this put pressure on her?"
    n 5bw "W-who cares at this point?!"
    n "Does it not put pressure on me, too?"
    n 5br "This isn't easy for anyone..."
    n "I just want to get it over with."
    "Natsuki has a point."
    "But Yuri will need to agree."
    "I'd better try and ask Monika to convince her."
    "I send her a text message, while Natsuki peeks over my shoulder and reads."
    "While I wait for an answer, we decide to clean up the mess that had just happened and sit down to finally be able to enjoy our breakfast."
    "I reluctantly try to appreciate the food, but my stomach is torn up."
    show natsuki at thide
    hide natsuki
    scene black
    with fade
    "Monika responds saying it's settled."
    "But..."
    "With a follow-up."
    m "By the way, [player], there's something I'd like to talk to you about. Concerning you and Natsuki."
    m "I already mentioned it with Yuri. I'll talk it over with you guys once you're done with your little meeting."
    m "Let me know how it goes. Good luck."
    scene bg livingroom
    with fade
    "Hours pass, and it's finally time."
    "Each second feels like an eternity."
    "Finally, the doorbell rings."
    "Natsuki jumps up a bit."
    "I can tell she's nervous."
    mc "Hey, don't worry about it."
    mc "It's gonna be just fine."
    show natsuki 1bs at t11 zorder 2
    n "I know, I know..."
    show natsuki at thide
    hide natsuki
    scene bg house
    with wipeleft_scene
    "I open the door and see an embarrassed Yuri just standing there."
    show yuri 3bq at t11 zorder 2
    y "H-hi."
    mc "Hey, Yuri."
    mc "Come in, right this way."
    show yuri at thide
    hide yuri
    scene bg livingroom
    with wipeleft_scene
    "I lead her to the living room."
    "The instant the two girls see each other, I feel the tension in the room rise up."
    "They don't exchange a single word, until Yuri breaks the silence."
    show yuri 3bs at t11 zorder 2
    y "I-I came here to apologize."
    y "A-and explain myself."
    show yuri at t21 zorder 2
    show natsuki 1bg at f22 zorder 3
    n "I've been waiting for that."
    show natsuki 1bg at t22
    mc "Natsuki."
    mc "Shush."
    show yuri 2bf at f21 zorder 3
    y "No, it's...it's okay."
    y 2bh "I can handle it."
    y 1bl "So..."
    y 1bs "I'm sorry, Natsuki."
    y "I'm really sorry."
    "Her eyes tear up and she goes completely red."
    y 4bb "I'm sorry...for hating you."
    "These words go right through Natsuki's heart."
    "She grabs my hand hard and starts shaking lightly."
    y 1bu "There's nothing I can do."
    y 1bv "You've hurt me, I've hurt you, and..."
    y "I..."
    y 2bw "I don't think we can stay friends."
    show yuri at t21 zorder 2
    "There, she said it."
    "Natsuki tenses up."
    show natsuki 1bn at f22 zorder 3
    n "I--"
    n "But..."
    n "I wanna be friends, Yuri..."
    n 4bu "You were...{i}so, so, so{/i} important to me."
    n "I can't let you go like this."
    show natsuki at t22 zorder 2
    show yuri 1bt at f21 zorder 3
    y "I know it's difficult, but..."
    y "I don't want to be friends anymore."
    "Dead silence falls in the room."
    y 1bs "I've been hurt too much."
    y "I can't cope with it anymore..."
    y 3bq "You and [player]..."
    y 3bo "Being around the two of you isn't easy."
    y 3bu "In short, I don't wanna see you two anymore..."
    y "Whether it's in the street or in the literature club."
    y 1bl "It's why I left."
    y 2bh "And since I can't really leave school or move away, I'd prefer if we cut contact."
    y 1bt "Completely."
    show natsuki at thide
    hide natsuki
    show yuri at t11 zorder 2
    "A quick glance over to Yuri makes her understand that she should leave."
    "I follow her to the door and grab her before she runs away."
    show yuri at thide
    hide yuri
    scene bg house
    with wipeleft_scene
    mc "Hey, Yuri."
    mc "Don't beat yourself up over it."
    mc "I don't think it's for the best, but I respect your decision."
    mc "I hope we can see each other on better terms."
    mc "And if not, I hope your life goes well."
    show yuri 4bb at t11 zorder 2
    y "Yeah."
    y "You too."
    y 4ba "Bye."
    mc "Bye."
    show yuri at thide
    hide yuri
    scene black
    with fade
    scene bg livingroom
    with fade
    "I go back inside slowly and quietly."
    "Natsuki's laying down on the couch with a dry face and red eyes."
    "She seems to have accepted her fate."
    "At least we still got each other."
    "I sit down next to her and embrace her."
    show natsuki 42ba at t11
    mc "Natsuki."
    mc "Don't beat yourself up over it."
    mc "People come, people go."
    mc "It's life."
    mc "Be happy you could say your parting words."
    mc "And be happy that you had such a great friend."
    mc "And..."
    mc "At least we have each other."
    mc "I'll never, ever give you up."
    mc "I have made mistakes, but I will learn."
    mc "And I will love you, more."
    show natsuki 12bg at t11 zorder 2
    n "[player]."
    n "I love you."
    n 12be "I'm sorry for all the trouble I've caused you."
    mc "It's over now."
    n 12bd "Almost."
    "After this, I'm thinking that distancing ourselves from the club could be a good idea."
    "I'm friends with Monika, and Sayori lives next door."
    "I'm sure they'll understand."
    "On that note, Monika calls me."
    show natsuki at thide
    hide natsuki
    m "Hey, [player]."
    mc "Oh, Monika, it's you."
    m "Indeed it is."
    m "How'd it go with Yuri?"
    mc "Yeah..."
    mc "They decided to not be friends anymore."
    mc "It was a forced agreement, but they seem to be over it for now."
    m "I wouldn't believe it so quickly if I were you."
    m "Anyways, can you put me on speaker?"
    m "I'd like to talk to you two about something."
    mc "...Sure."
    "It seems really important."
    "And since it concerns Yuri, I can't help but wonder what it is."
    show natsuki 42bb at t11 zorder 2
    m "So, after my discussion with Yuri, we concluded..."
    m "That she would join back if you two left."
    m "And I think you two should."
    m "[player], Natsuki, I don't hate you."
    m "Quite the opposite."
    m "You two brought a lot to the club."
    m "Especially liveliness."
    m "Maybe even too much."
    m "And I couldn't thank you enough for that."
    m "But times change."
    m "Things go forward."
    m "And maybe, just maybe, after all that has happened..."
    m "You should consider leaving it behind."
    m "It's for the better of everyone, and it can stay as a good memory for everyone."
    show natsuki 42ba at f11 zorder 3
    n "But..."
    show natsuki at t11 zorder 2
    "I hold Natsuki back."
    show natsuki 42bb
    mc "It's the right choice."
    mc "But won't you have a lack of members?"
    m "Actually..."
    m "I already handled that."
    m "I've recruited a few transfer students to join the club."
    m "A year below us, in fact, so the club will love on after I'm gone..."
    m "It's...bittersweet..."
    m "..."
    m "Well, anyway don't worry about me, worry about yourself."
    m "Are you fine with leaving the club?"
    mc "Uh..."
    n "Uhm..."

    menu:
        "My decision..."
        "Stay.":
            mc "I'm sorry Monika."
            mc "We...can't just leave so easily."
            m "I understand."
            m "Well actually, I should be the one apologizing."
            m "I really hoped you'd agree with this on me, but..."
            m "I guess I'll have to kick you out myself then."
            "...wow."
            "I, for sure, did not expect that."
            show natsuki 4bm at f11 zorder 3
            n "Wait, Monika!"
            n 1bn "It's gonna hurt our school record..."
            show natsuki at t11 zorder 2
            m "Well, it won't if you agree with me, and you leave."
            mc "Natsuki, you know..."
            mc "She's right."
            mc "I guess it's for the better of everyone."
            show natsuki 1bo at f11 zorder 3
            n "But--"
            n "[player]...!"
            n 1bn "..."
            n 5bu "Fine..."
            show natsuki at t11 zorder 2

        "Leave.":
            mc "Well..."
            show natsuki 4bn at f11 zorder 3
            n "It's--"
            n "..."
            n 5bu "It's better if we...leave..."
            show natsuki at t11 zorder 2
            "Natsuki?"
            "I didn't expect her to agree with Monika on this one."
            mc "Uh."
            "Will I have to follow along?"
            "It's a hard decision, but I gotta make it."
            "To not hurt Natsuki anymore."

    m "So, is it settled?"
    m "I'm having trouble not regretting this."
    mc "It's...settled."
    m "Great."
    m "Then I'll contact Yuri."
    m "I'll also handle the administrative part."
    m "I'm sorry it had to end this way, but..."
    m "At least we're still friends."
    mc "Yeah, we can see each other outside of the club, after all."
    m "Of course, and I promise I'm just a phone call away."
    m "Well, I'll hang up now."
    m "I've got Christmas stuff to prepare."
    m "This is goodbye, but it's not farewell."
    mc "G-goodbye, Monika."
    show natsuki at thide
    hide natsuki
    scene black
    with fade
    scene bg livingroom
    with fade
    "Natsuki looks down, but also relieved."
    mc "Hey, we should at least enjoy our day."
    mc "How about I take you out to dinner?"
    mc "We can go eat some steak."
    "That's gonna hurt the wallet."
    "But nothing is too expensive for my princess."
    show natsuki 5bm at t11 zorder 2
    n "...really?"
    n "You'd buy me a dinner like that?"
    mc "Of course."
    mc "Anything for the person I love the most."
    n 2bu "[player]..."
    n 4bz "I love you!"
    show natsuki at thide
    hide natsuki

    scene bg ending_g
    with dissolve_scene_full
    window hide
    pause(5)
    scene black
    with fade

    return
#End Scene 11c - Yuri Neutral Ending
#{ END OF NATSUKI ROUTE - YURI NEUTRAL ENDING ACHIEVED }
#A FEW PARTIN(G) WORDS  

label Natsuki64:
#Start Scene 11d - Good Ending
    scene bg bedroom
    with dissolve_scene_full
    play music t5_natsuki
    "Today is Christmas Eve."
    "A day where, no questions asked, you're supposed to spend with your loved ones and feel safe, secure, happy, all that junk."
    "I talked to my mom and dad a few days ago and they said they'd be flying in on Christmas Eve night and they'd be here by Christmas morning."
    "I'm excited to see them again, and I'm excited for them to finally meet Natsuki after all this time."
    "Speaking of Natsuki, over the last couple of days I've gone Christmas shopping for her, and also for Sayori."
    "Sayori and I always end up getting each other something small for Christmas, like a new piece of clothing or some kind of stuffed animal."
    "This year I opted to get Sayori a cute throw pillow with her favorite movie characters on it. She's easy to please so I think she'll really like it."
    "As for Nats, I went on about three different trips to the mall and got her something different on each one."
    "The first few weren't particularly exciting, one was a box of fancy chocolates, and the other was a new Parfait Girls t-shirt."
    "That's why, for the third trip, I made sure it was special."
    scene bg kitchen
    with wipeleft_scene
    "After my morning routine, I go to the kitchen and see Natsuki at the stove preparing what I can only guess are special Christmas pancakes."
    mc "Merry Christmas, Natsuki."
    show natsuki 4bj at t11 zorder 2
    n "Merry Christmas, [player]."
    "She stands on her toes and gives me a quick peck on the lips, but I pull her back in and give her a much longer kiss."
    n 2bt "Yeesh, buddy, there isn't even mistletoe above us. Hehehe~!"
    mc "I don't conform to generic Christmas traditions like that."
    mc "If I wanna kiss my girlfriend I'll do it whenever and however I darn well please."
    n 1bl "I like that."
    mc "So, what is this heavenly breakfast I'm smelling? I swear it smells like--"
    n 4bj "Peppermint? Hehehe, yeah, they're my famous Christmas Peppermint pancakes."
    mc "Son of a..."
    n 5by "I know, sounds amazing, right? It tastes even better than it sounds."
    mc "I just remembered why I started dating you."
    show natsuki 4bi at d11
    "Natsuki slugs me in the shoulder."
    mc "Ow!"
    n 5bh "Don't make dumb jokes like that on Christmas!"
    mc "Okay okay. So are they almost ready?"
    n 2bj "Yup, just about. Set the table for us?"
    mc "I'd be glad to."
    "Natsuki gives me a warm smile, and my heart feels the same warmth."
    show natsuki at thide
    hide natsuki
    "It's like no matter how much time I spend with her, seeing her continues to make me feel fuzzy."
    "I really do love her."
    "I set the table for us, and pretty soon Natsuki brings the skillet over to the table and puts two pancakes on each of our plates."
    "They look like they're chocolate, and I can see crushed up bits of peppermint sitting inside them."
    mc "Nats, you continue to blow my mind."
    "I prepare to start digging in before Natsuki interrupts me."
    show natsuki 2bb at t11 zorder 2
    n "Ah, ah, ah, hold on! I need to add the final touches."
    "Natsuki grabs what appears to be melted chocolate from the stove and then drizzles it on each of our pancakes."
    "She then opens the pantry, and pulls out a box of miniature gingerbread men."
    mc "When did we even get thos--"
    n 2bd "I told you I make shopping runs."
    "Next, Natsuki takes a can of whipped cream from the fridge, then puts some on each of our pancake stacks."
    "Finally, she opens the box of gingerbread men, and carefully places one inside each dollop of whipped cream."
    n 4ba "{i}Voila.{/i}"
    mc "You are an artist, Nats."
    n 5bl "Hehe, I know. You're free to start eating now."
    mc "Hold on, before we do, let me take a picture."
    n 1bl "Okay!"
    scene natsuki_pancakes
    with dissolve_scene_full
    "Natsuki brings her plate of pancakes next to mine, then I open the camera on my phone."
    "I stand on the opposite end of the table and snap a photo of Natsuki in front of the delicious meal she'd prepared."
    mc "Heh, this came out pretty good. You look adorable."
    n 4bz "Hehe~, thank you."
    n 4bc "Alright well we've stalled long enough, I'm hungry."
    "Natsuki takes a seat, and we both finally start to eat her special breakfast."
    "On my first bite I'm taken to another world."
    "The minty chocolate flavored batter is cooked to perfection, and every so often I'll get a bite of a peppermint chunk."
    "This is more akin to a dessert than a breakfast, but if eating this in the morning is wrong, I don't wanna be right."
    "I take my last bite and feel like I'm about to explode."
    mc "That was...something else."
    n "That was definitely the best batch of those that I've ever made."
    mc "You should make them more often."
    n 4bb "Nope, Christmas only. It needs to be a special occasion."
    n 3bd "Plus, making that batter is harder than you'd think."
    mc "I guess you know more than me. But I won't rest until you make that on a day that isn't Christmas."
    n 1bg "Fine fine, I'll make them for you before Christmas next time."
    mc "Really?"
    n 1bl "Yeah!"
    n 2bl "I'll make them on December 23."
    mc "Oh ha ha."
    scene bg livingroom
    with dissolve_scene_full
    "We clean our dishes then go over to the couch in the living room to cuddle."
    "I still feel so good inside whenever I hold her close to me."
    show natsuki 1bk at t11 zorder 2
    n "Hey, [player]?"
    mc "Yeah?"
    n "Why don't we have a Christmas tree?"
    mc "Uh...we do, it's just in the basement."
    n 4be "And why didn't we set it up?"
    mc "..."
    n 1bc "Are you scared of the basement, [player]?"
    mc "You don't know what's down there!"
    n 5bz "Pffft, BAHAHAHA!"
    n 5bj "You're such a baby."
    n 2bt "But uh, I guess it isn't a big deal."
    mc "Glad you think so."
    mc "Do you wanna give each other our presents now?"
    show natsuki 2bu
    "Natsuki blushes a little bit, but in a sort of shameful way."
    mc "What's wrong?"
    n "Well, um..."
    n "It's nothing."
    n 3bt "Listen, um, I know you got a gift for Sayori, so..."
    n "You should go give that to her now."
    n "And I'll just go to your room for a little while. Just, give me some time, and go give Sayori her gift, okay?"
    mc "Wait, Nats--"
    n 4ba "Don't worry about me, [player], I promise I'm fine, I just need to be prepared."
    n 4bw "I'm not taking 'no' for an answer here."
    show natsuki 4bs
    mc "Oh, well alright, Nats, if you're sure. I'll be back soon, okay?"
    n 4bd "Okay. Have fun!"
    show natsuki at thide
    hide natsuki
    "Natsuki disappears into my bedroom and I'm a little confused about her sense of urgency."
    "Nonetheless, she didn't seem like she was really in any bad spirits, so I guess I'll roll with whatever she has planned."
    stop music fadeout 1.5
    "That in mind, I go behind the couch where I put Sayori's gift bag and I grab it, then I leave my house and walk toward Sayori's."
    scene bg sayori_hall
    with wipeleft_scene
    play music t2
    "I knock on her door, then let myself in."
    mc "Sayori, you awake?"
    s "[player]? Is it that time already??"
    mc "Sure is!"
    s "Yay!! Come upstairs!"
    "I walk up to her room and walk inside."
    scene bg sayori_bedroom
    with dissolve_scene_full
    "The second I open the door, Sayori leaps at me and gives me a hug."
    show sayori 4br at t11 zorder 2
    s "Merry Christmas!!"
    mc "Merry Christmas to you too, Sayori."
    "We give each other a little squeeze then end the hug."
    "Sayori looks at my right hand and sees the gift bag."
    s 5bc "A bag, [player]? Really? Where's the fun in that?"
    mc "Trust me, I tried wrapping it, but once you see what it is you'll realize a bag was the better idea."
    s 5bb "Hehe, maybe you're right."
    show sayori at thide
    hide sayori
    "Sayori then opens her closet and reaches around until she finds her gift to me."
    "It looks...weird. I can tell it's not something with a lot of density or shape, but she still decided to wrap it anyway."
    mc "You dummy."
    show sayori 4bj at t11 zorder 2 
    s "I'll never sell out! Wrapping presents for the win!"
    mc "Ahaha. I've missed Christmastime Sayori."
    s 1ba "And I've missed Christmastime [player]."
    mc "Do you wanna open yours first?"
    s 1bq "Yes! Gimme gimme!"
    "Sayori pretty much snatches the bag out of my hand, and I can't help but chuckle."
    "She reaches into it and pulls out the pillow celebrating her favorite movie."
    s 4bs "Ahhh!"
    s "[player], this is the cutest thing ever! Thank you!"
    "Sayori hugs the pillow to her chest."
    mc "You're welcome, Sayori."

    if ((tens_check == "S") and (jerk == False)):
        mc "When we watched it recently it gave me the idea."
    
    mc "I'm glad you like it."
    s 2ba "You're so thoughtful."
    s 1ba "Well, guess it's time for you to open mine."
    "Sayori hands me the abominable attempt at gift wrapping and I laugh at her. It doesn't even keep its shape in my hand."
    mc "I really hope this gift makes me forget about this wrapping job."
    s 5bc "Just open it, you meanie."
    show sayori 1ba
    "I tear it open, and I see a white puffball."
    "I grab it, then pull it out and see it's a Santa hat."
    "I'm a little confused at first at why she'd give me this, but then I look at the rim of the hat and see something sewn into it."
    "It says, 'Sayori's BFF.'"
    mc "Oh my goodness, Sayori, this is the sweetest thing. I'll always treasure this."
    s 1bq "Hehehe~! I'm glad you like it!"
    s 1ba "But turn it around, there's some more."
    "I do so, and see another message sewn into the hat."
    "‘Natsuki's Man.'"
    "I smile a great big smile and look at Sayori."
    s 2bd "I wanted to celebrate you two being so happy together."
    s "This felt like a good way to do it."
    mc "You're so much more thoughtful than I am, Sayori. Thank you so much."
    s 3bl "Oh stop, don't say that."
    s 3ba "I'm lucky to have you as a friend."
    mc "And I'm lucky to have you as a friend."
    stop music fadeout 1.5
    "Sayori and I hug and tell each other Merry Christmas one more time before I leave her house."
    show sayori at thide
    hide sayori
    scene black
    with fade
    scene bg livingroom
    with fade
    play music t6
    "I return to my home and call out for my girlfriend."
    mc "Natsuki, I'm back!"
    n "I'm in the bedroom!"
    scene bg bedroom
    with wipeleft_scene
    "I walk in, and see that nothing's really changed."
    "Natsuki's sitting on the bed and smiles when she sees me."
    "I'm wearing the hat Sayori gave me, and she sees the message she wrote."
    show natsuki 1bj at t11 zorder 2
    n "Sayori's the sweetest girl I've ever known."
    mc "She's pretty awesome, isn't she?"
    n 2bs "Yeah..."
    n 2bn "Um, so, you have some gifts for me, right?"
    mc "Yes, I do."
    show natsuki at thide
    hide natsuki
    "I go to the closet in the hallway briefly, then return with two items, a bag with the chocolates and the t-shirt, and a massive yet flat wrapped box containing the other gift."
    "Natsuki sits up looking very excited to see what's inside."
    "I first hand her the bag, and she reaches inside and examines the chocolates and the shirt."
    show natsuki 1bd at t11 zorder 2
    n "Ahh, this shirt is so cu--"
    n 4bi "Er, awesome. That's the word I was gonna say, nothing else."
    mc "Pft, uh huh."
    n 5bh "Shut it, dummy."
    n 5bm "These chocolates look like they were a lot of money."
    mc "It's okay, I'm sure they were worth it."
    "{i}At least I freaking hope so.{/i}"
    n 1bj "Thank you so much."
    n "So...can I have that last one?"
    mc "Of course. I'm...really excited for you to see this."
    stop music fadeout 1.5
    "Natsuki takes the huge box and starts to tear it open."
    show natsuki 1bh at t11
    "She looks at it and gasps with emotion, then finishes unwrapping it."
    "It's a big 3-foot by 4-foot wooden photo of Natsuki and her mother. It's the same picture that was on her mom's headstone."
    play music t9
    n 1bu "[player]...this is unbelievable..."
    n "I love this so much...I love you so much..."
    "Natsuki starts to tear up, then gently sets it down on the bed, stands up and hugs me."
    n 12ba "Thank you...thank you thank you thank you..."
    "She sniffles and starts sobbing into my shoulder."
    mc "I love you, Natsuki. I wanted to give you something really special."
    "Natsuki tries her best to stop crying, then she looks at the big picture again and smiles warmly."
    n 1bm "...Mama..."
    "She looks back at me, looking a little bit sad."
    n 5bn "So, listen..."
    n "You're gonna be really mad at me."
    mc "Try me."
    n 5bu "Okay, the thing is..."
    n 42ba "I didn't get you anything for Christmas."
    "..."
    "Well that was unexpected."
    mc "O-oh well that's okay. You being in my life is enough of a gift."
    n 42bb "Heh...I can tell from the tone of your voice you're disappointed."
    mc "Well, maybe a little, but I don't care all that much. That breakfast you made was sufficient enough anyway."
    n 12bc "R-right...but the thing is, I got a present for somebody else, but I didn't have enough money to buy gifts for them and for you."
    mc "Really?"
    mc "Well, who was it?"
    n 12bb "..."
    n 12ba "It's...my dad."
    "That was also unexpected."
    mc "You got a gift for your dad?"
    n 42bc "Yeah...are you mad?"
    mc "No, Natsuki, not at all."
    mc "In fact, I'm proud of you."
    mc "Taking steps toward forgiving your dad takes a lot of strength."
    mc "Your mom would be so proud of you."
    "Natsuki starts welling up again, but wipes her soon-to-be tears away."
    n 1bj "Thank you."
    n 1bs "I was...planning on going to my old house for the first time since he kicked me out, and..."
    n "I guess leave the present on his porch."
    n 4bt "I'm still not ready to forgive him to his face, but I still want him to have it."
    n 5bm "Do you think you could come with me to drop this off?"
    n 5bn "I'm...nervous to do it by myself."
    mc "Of course I will. We can go whenever you're ready."
    n 1bu "Um...I think right now is a good time."
    show natsuki at thide
    hide natsuki
    stop music fadeout 1.5
    "Natsuki and I prepare to go drop this present off at her dad's house."
    scene black
    with fade
    scene bg residential_day
    with fade
    play music t13
    "As we're walking toward her old home, I become curious."
    mc "Hey, what did you get your dad?"
    show natsuki 1bk at t11 zorder 2
    n "Oh, um...here, you can look at it."
    "She hands me the small gift bag, and I pull out what looks like a long jewelry case."
    "I open it up and it looks like a locket."
    mc "Is it okay if I take a closer look?"
    n 2bq "Y-yeah, I don't mind."
    show natsuki 2bu at t11
    "I pick up the locket, and look at the front."
    "Engraved in it appears to be the name of Natsuki's mother, Kaiya."
    "I turn it around, and on the opposite side see another engravement."
    "{i}'Forgiveness.'{/i}"
    "I open the locket, and it has that picture of Natsuki and her mom inside it."
    "I close it up, put it back inside the case, and place it back into the gift bag."
    mc "It's beautiful, Natsuki."
    mc "He'll be very happy to have this."
    n 1bh "Thank you, I hope so too."
    scene bg cafe
    with fade
    "We finally approach Natsuki's father's home, and she looks toward the front door, extremely scared."
    "She clutches to my shoulder like she did when her dad appeared at the cemetery."
    n 12bc "I...I can't do this."
    mc "Yes you can, Nats. You've come this far. I believe in you."
    n 12bb "..."
    n 12ba "Okay..."
    show natsuki 1bu at t22
    "Natsuki walks up to the front door, and rings the doorbell."
    "But...she doesn't set the bag down or leave the porch."
    "A few moments later, the door opens, and her dad appears."
    show katashi 1n at t21
    "..."
    show katashi 1o at f21
    k 1o "N-Natsuki?"
    show katashi 1q at t21
    show natsuki 12bb at f22
    n 12bb "*sniffle*"
    show katashi 1q at t21
    n 12bg "Merry Christmas, Papa."
    show natsuki at thide
    hide natsuki
    "Natsuki hands the bag to him, and runs away, then as she passes me grabs my hand and we start running back home together."
    scene black
    with fade
    scene bg livingroom
    with fade
    play music t10
    "Back in my living room, Natsuki is now bawling her eyes out."
    mc "Natsuki, are you okay?"
    show natsuki 42bf at t11 zorder 2
    n "..."
    "I put my arm around her and kiss her on the head."
    mc "You're so brave, Natsuki."
    n 42bi "Am I brave enough to really forgive him?"
    mc "I'm sure you'll find that out in time. But today was a big step."
    n 42bf "..."
    n "You talk a lot about taking steps, [player]."
    n "And it makes me realize..."
    n 12bh "I wouldn't have made any steps if it wasn't for you."
    n 12bi "Thank you."
    n 2bq "I think that because of you, I'm finally taking steps on the path to forgiveness."
    n 2bt "On the path to Kaiya..."
    show natsuki 1bj at thide
    hide natsuki

    scene bg ending_f
    with dissolve_scene_full
    window hide
    pause(5)
    scene black
    with fade
    return
#End Scene 11d - Good Ending
#{ END OF NATSUKI ROUTE - GOOD ENDING ACHIEVED }
#THE PATH TO (F)ORGIVENESS
