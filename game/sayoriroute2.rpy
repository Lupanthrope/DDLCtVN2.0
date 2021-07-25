label sayoriroute2:
    scene black
    s "..."
    s "..."
    s "..."
    s "...{i}someday I'll wish upon a star{/i}…"
 
    call sayoriroute21
    call sayoriroute22
    jump sayoriroute3


label sayoriroute21:
    scene bg bedroom
    with wipeleft
    play music t5_sayori

    #MC wakes up
    "{i}Whew{/i}."
    "What a night!"
    "Sayori seems to still be asleep."
    "It's been 4 months since Sayori and I..."
    "You know..."
    "...Anyways, after what happened last night, I really should do something nice for her."
    "I'll make her breakfast in bed! I hope she'll like it."


    scene bg kitchen
    with wipeleft

    "Hmm, what should I make?"
    "Uh... what do I have?"
    "After a little aimless searching, I find a half-empty bag of chocolate chips."
    "Sayori likes chocolate chip pancakes, right?"
    "I rummage through my cabinets for some pancake batter."
    mc "Jackpot!"
    "I quickly put my hand over my mouth and stay quiet."
    "I hope I didn't wake her up..."
    "I mix up the batter with some water as the stove heats up."
    "After the pan is hot enough, I begin to make her pancake."
    "I make hers before I make mine."
    "I'm used to barely eating in the morning, since most days I brush my teeth for breakfast."
    "After a few minutes, the pancake is done. It's a little burnt on one side, but it looks fine to eat."
    "I put the pancake on the plate."
    "I pour a glass of orange juice for Sayori, and bring her plate and glass back up to her on a tray."


    scene bg bedroom
    with wipeleft

    show sayori pjx at t11 zorder 2
    show sayori pjx at t11 zorder 2
    s "Oh, hey, [player]."
    s "I was just-"
    s pjm "Oh my god... Are those chocolate chip?"
    s pjr "That's my favorite!"
    show sayori pjq at t11 zorder 2
    "I anxiously wait for her to take a bite of the pancake."
    show sayori at h11 zorder 2
    s pjr "I LOVE IT! It's so nice and fluffy!"
    mc "I'm glad you like it!"
    mc "Anyways, you were saying something?"
    s pjb "Hm?"
    mc "It sounded like you were saying something at first."
    s pjk "Oh, it was nothing."
    "When have I heard this before?"
    mc "Sayori..."
    s pji "Don't worry so much!"
    s pjj "I was saying that I was just getting ready."
    "I struggle for words. I guess I was overreacting."
    mc "Sorry, Sayori..."
    s pjx "Aww. Don't worry about it."
    s pjx "It still means so much to me that you look out for me!"
    mc "Well, in any case, we'll be late for school if we don't leave soon."
    s pjs "Hey, wait, one thing before we do…"
    "Curious, I turn back toward her, then walk up to her."
    scene black
    "Suddenly, Sayori plants a long kiss on me, and I gladly accept it."
    "However she starts getting particularly handsy, and she places her hand on my waist."
    "Reluctantly I stop the kiss."
    scene bg bedroom
    show sayori pjy at h11 zorder 2
    mc "Eheheh, easy there, cowgirl."
    mc "We'll have plenty of time for this later, but we have to get going."
    "Sayori blushes and then clears her throat."
    s pjs "Eheheh~"
    s pjs "Okay, let's go then!"
    show sayori at thide zorder 1
    hide sayori 
    stop music fadeout 1.5


    scene bg house
    with wipeleft_scene
    play music t2
 
    show sayori 1c at t11 zorder 2
    show sayori 1c at t11 zorder 2
    s "[player], can I tell you about my dream last night?"
    mc "Yeah, I'd love to hear about it."
    s "I dreamt that I was in the arctic."
    s "I was wearing my normal school uniform, but I wasn't cold at all."
    s "I looked around and then, suddenly, out of nowhere"

    show sayori at h11 zorder 2
    show sayori at h11 zorder 2
    s 4n "A bunch of penguins came appeared and started to walk toward me!"
    s "Then the leader of the penguins"
    s "Who was like, my height"
    s 4o "Came up to me and introduced himself as Reginald and he talked with a British accent, and he told me"
    s "{i}You, Mistress Sayori, are worthy to be our queen!{/i} "
    show sayori at h11 zorder 2
    show sayori at h11 zorder 2 
    s 4x "I told him that just \"Sayori\" was fine, and that I was super happy."
    s 1o "I asked him then if that meant I had to marry him."
    s 1n "He said, {i}Of course not, darling. You just need to prove yourself to be the best at sledding.{/i} "
    s "He took me by the hand, and we went over to the biggest hill in Greenland!"
    mc "I'm sorry to burst your bubble Sayori, but..."
    mc "Penguins don't exist in the arctic, and they definitely are not in Greenland."
    mc "And Greenland is most certainly NOT the Arctic!"
    show sayori 5d at t11 zorder 2
    "...Maybe I shouldn't have pointed out her mistake, but I had to tell her before she started spreading misinformation about penguins."
    s "That doesn't matter!"
    s 5c "What matters is what happened!"
    mc "Okay, I'm sorry, continue."
    s 1x "So he took me to the biggest hill, and he let me hop on his back."
    s 1r "We sledded down that hill for hours, it was so much fun!"
    s "Then, he officially named me \"Queen of The Penguins\"."
    s "So, how 'bout them apples? You're officially dating a queen!"
    show sayori 1a at t11 zorder 2
    "I really don't want to take this happy moment from her, so I had to come up with a response and change the topic."
    mc  "That's so cool, my girlfriend is the Queen of The Penguins..."
    "...Does that make me the King?"
    "As we get to school, I remember that I had to ask Sayori something important."
    show sayori at thide zorder 1
    hide sayori


    scene bg corridor
    with wipeleft_scene

    show sayori 1a at t11 zorder 2
    show sayori 1a at t11 zorder 2
    mc "Hey, Sayori?"
    mc "I was wondering... Would you like to go somewhere after school?"
    mc "As a date, of course."
    s 4s "Of course I would! A date sounds nice!"
    s 1s "I'll see you soon, then, huh?"
    show sayori 1y at t11 zorder 2
    mc "Yeah.. I'll see you then."
    show sayori 1y at thide zorder 2
    hide sayori
    "We exchange a quick kiss on the cheeks before going to our classes."
    stop music fadeout 1.5 


    scene bg class_day
    with wipeleft_scene

    "Math."
    "One of my {i}favorite{/i} hours of the day."
    "I usually just sleep through the hour, but a big test is coming up next week, and my grades in this class need a face lift."
    "I can't help but let my mind wander a little."
    "God, my first ever actual official date."
    "Never in my life would I ever imagine it would be with Sayori…"
    "Never in my life would I ever imagine doing a lot of the things i've done with Sayori.."
    "Especially.."
    "{i}Huh?{/i} A Note?"
    "It's from Sayori, she slid it under my elbow while I was distracted by myself."
    "I turn to look at her."
    show sayori 4wink at t11 zorder 2
    "She's winking at me…"
    "It now suddenly feels like I'm in the Mojave desert."
    "I feel a bead of sweat form on my forehead as I recall last night's events."
    mc "{i}Gulp.{/i}"
    "I unfold the paper to read what she wrote."
    show sayori at thide zorder 1
    hide sayori

    python:
        s21_poem1 = Poem(
        author = "sayori",
        title = "Hey {}!".format(player),
        text = """\
Thanks for a wonderful Sunday evening! 
Oh, and for letting me sleep over and making me breakfast! 
I really just wanted to say that I'm really looking forward to tonight!
I hope it's just as fun as last night! ;)
    
    - Love,
        Sayori <3

P.S: Where are we going for the date?"""
        )

    call showpoem(s21_poem1, music=False)

    "I look back at her."
    "She's writing in her notebook like nothing happened."
    "I decide to write back to her."

    python:
        s21_poem2 = Poem(
        author = "mc",
        title = "",
        text = """\
Well if I tell you about it, it'll ruin the surprise! 
Just wait patiently for the time to come, I promise it'll be worth it."""
        )
    
    call showpoem(s21_poem2, music=False)

    "I slide the note to her just like she did."
    "I watch as she reads the note."
    show sayori 3i at t11 zorder 2
    "She looks my way and pouts when she's done reading."
    show sayori at thide zorder 1
    hide sayori
    "We go back to listening to the teacher as quickly as possible."
    "I can't begin to imagine the hell the teacher would give Sayori and I if she caught us passing notes."
    "And especially what we're talking about in them!" 
    "{i}*Shrudder*{/i}"

    scene bg corridor
    with wipeleft_scene
    play music t3

    "Sayori and I head to the clubroom together like most days."
    "On our way we talk a little bit about the night ahead of us."
    show sayori 1x at t11 zorder 2
    show sayori 1x at t11 zorder 2
    s "So where were you planning on taking us again?"
    mc "Hmmm."
    "How shall I give the big reveal?"

    menu:
        "Playful":
            "I take a brief second to think about how to word it."
            mc "Well…"
            mc "It's a place…"
            mc "Where you can drink-"
            s 4n "The bar!"
            mc "What? It's n-"
            s 1j "[player], we're too young for that!"
            mc "No, it's not the bar, Sayori."
            mc "You didn't let me finish."
            s 5a "Sorry."
            mc "It's a place where you can drink hot cocoa."
            s 1m "Oh!"
            s 4r "I get it now!"
            s 1wink "..."
            s 5d "..."
            "She whispers"
            s 3c "It's the cafe, right?"
            "I whisper back."
            mc "It's the cafe."

        "Upfront":
            mc "It's the cafe."
            s 1r "Oh, cool!"
            s 4r "I've always thought that was a cute place!"
            s 3r "Can't wait for tonight!"


    show sayori at thide zorder 1
    hide sayori
    "Before we know it, we're at the clubroom."
    "..."
    "The door's closed?"
    "There's a note on the door."
    "It's from Monika."
    "I take the note out of the door to read it."
    
    python:
        s21_poem3 = Poem(
        author = "monika",
        title = "Literature Club Cancelled",
        text = """\
Dear Sayori, Yuri, Natsuki, and {},

Sorry for not getting to you all personally, but I have to inform you that the Literature Club will \
be cancelled today. This is due to personal reasons I am currently unable to say. \
However the club should return tomorrow!

Sincerely,
    Monika""".format(player)
        )

    call showpoem(s21_poem3, music=False)

    show sayori 1b at t11 zorder 2
    show sayori 1b at t11 zorder 2
    s "Well? What does it say?"
    mc "It says the Literature Club is cancelled today."
    s 4p "Aww, what!"
    s "Why?"
    mc "Monika said it was just personal stuff."
    mc "We can ask her what it was next time we run into her"
    s 4k "True."
    s "I hope everything is ok with her."
    mc "So what now?"
    s 1b "Believe it or not, this actually works out for me. "
    s 5a "I could use the extra time to get ready for our date tonight."
    "Extra time?"
    "Is she planning something?"
    "She doesn't take that long to get dressed into something casual when she's excited…"
    mc "Fair enough. Ready to walk home?"
    s 1r "Of course! Let's go!"
    show sayori at thide zorder 1
    hide sayori
    stop music fadeout 1.5


    scene bg house
    with wipeleft_scene

    show sayori 1x at t11 zorder 2
    show sayori 1x at t11 zorder 2

    s "Hey, just to let you know, I may take a bit to get ready."
    s "Just meet me there, okay?"
    s 2r "If I'm not there in time, just get me a big hot cocoa with whipped cream, alright?"
    mc "Duly noted."
    show sayori at thide zorder 1
    hide sayori
    "We give each other a small kiss before we return to our homes to change and get ready."


    scene black
    with dissolve_scene_full

    "I put on some casual clothes and a slight hint of cologne I happened to find."
    "Following Sayori's wishes, I head out for the cafe without her."

    scene bg cafe
    with wipeleft

    "I arrive at the cafe, which used to be a house, but was bought and repurposed..."
    "As I wait for Sayori, I find myself wondering why she wanted extra time to get ready."
    "I also realize that this is our first \"official\" date, since the festival didn't turn out too well."
    "Of course, I don't count her coming to my place every Sunday as dates."
    "As I lose myself in thought, I'm suddenly jolted back to reality{nw}"

    show black
    "As I lose myself in thought, I'm suddenly jolted back to reality{fast} as a pair of hands cover my eyes from behind."
    s "Guess whooo?"
    mc "I know it's you, Sayori."
    hide black

    show sayori 1fa at t11 zorder 2
    show sayori 1fa at t11 zorder 2
    play music t8

    s 1fx "So, how do I look?"
    mc "You look amazing."
    s 1fs "Really? I'm so glad!"
    mc "So should we head in?"
    s 1fx "Yeah, let's go!"
    "We head into the cafe and take a seat inside."
    show sayori 1fx at thide zorder 2
    hide sayori


    scene bg cafe_in
    with dissolve_scene_full

    show sayori 1fq at t11 zorder 2
    show sayori 1fq at t11 zorder 2

    "A waitress asks us what we want, I order a caramel latte, and Sayori gets her hot cocoa."
    "I try to think of something to say while we wait for our drinks, but nothing comes to mind."    
    "Weird, I never had a problem talking to Sayori before."
    "I need to say something to break the awkward silence that is growing between us…"
    "Hold on…"
    "Is that perfume?"
    $flag = False
    menu:
        "Smooth":
            mc "Sayori."
            show sayori 1fa at t11 zorder 2
            mc "I think you look nice today."
            mc "It means a lot that you dressed up and everything for this."
            s 1fx "Awww, thanks."
            s "Since this is technically our first date, I wanted it to be special."
            s "That's why I decided to wear this old thing."
            s 1fl "I haven't worn it since the Homecoming incident."
            mc "Homecoming incident?"
            "What does she mean by -"
            "{i}Oh.{/i}"
            "{i}That.{/i}"
            "I still have no idea how they were able to get a live squid in there…"
            s 1fx "I also convinced Yuri to give me some exotic perfume she never used."
            s "She's really into aromatherapy or something, and said this stuff would be perfect for a date."
            s 1fc "I think it was called Jazz Man?"

        "Normal":
            "I take a light whiff of the air."
            mc "Sayori?"
            s 1fx "Yes, [player]?"
            mc "Did you put on perfume for this?"
            s 1fl "Haha, yeah, I did."
            s "I thought it was appropriate for the occasion."
            s "And I wanted to try out a perfume Yuri gave me."
            s "She told me she never got to try it out, and just gave it to me!"
            s "She said it was some exotic flower."
            s 1fh "Jazz man, or something like that?"

        "Observant":
            $ flag = True
            "I smell an unfamiliar scent in the air, it seems to be coming off of Sayori."
            "{i}*sniff*{/i}"
            mc "You smell different than usual today Sayori, is that a new perfume?"
            s 1fh "Umm, what?"
            s 1fl "Yes...Yuri gave me one…"
            mc "Oh…"
            s 2fo "Wait, have you memorized my \"normal\" smell?"
            mc "Umm…"
            show sayori 2fl at t11 zorder 2
            "Sayori laughs awkwardly"
            s "It's okay, it's nice that you have this attention to detail."
            mc "What's the scent?"
            s 2fc "Yuri said something about a jazz man?"
            mc "Jasmine?"
            s "Yeah, that!"
    
    s 3fx "So."
    s "Do you like it?"
    mc "Yeah, it suits you well."
    
    

    if flag:
        s 4fl "Thanks, ehehe…"
        "Thankfully, the waitress breaks the awkward conversation by arriving with our drinks."
    else:
        s 4fs "Thanks, ehehe…"
        "Soon after, the waitress arrives with our drinks."
    
    mc "So how's your day going?"
    s 4fx "My day was great!"
    "Something about the way she said that…"
    "I don't want to pursue it, for fear of ruining the moment."
    s "I've been waiting for this all day!"
    mc "Me too."
    show sayori 1fy at t11 zorder 2
    "I grasp for a topic to keep conversation from stalling."
    mc "Do you remember the day you first introduced me to the literature club?"
    s 1fx "Yeah, it seems so long ago, doesn't it?"
    mc "It sure does."
    show sayori 1fq at t11 zorder 2
    "We sit in silence for a moment."
    mc "Back then"
    mc "Did you think we'd end up in this relationship?"
    show sayori 1fm at t11 zorder 2
    s 1fe "Honestly, I thought you were probably going to end up with Monika or Yuri."
    s 1fc "But ever since we started dating…"
    show sayori 3fq at t11 zorder 2
    "..."
    s 4fs "Those rainclouds haven't been looking so dark lately…"


    scene bg cafe_in_night
    with fade

    "As we finish up our drinks, I notice that it's getting late."
    mc "You ready to head home?"
    show sayori 1fc at t11 zorder 2
    show sayori 1fc at t11 zorder 2
    s "Yeah, sure."


    scene bg residential_night
    with wipeleft_scene
    "We walk home hand-in-hand."
    "Even though I only recently saw Sayori as more than a friend…"
    "I feel like I always have, and just now realized."


    show sayori 1fx at t11 zorder 2
    show sayori 1fx at t11 zorder 2
    s "Thank you, for a wonderful date." 
    show sayori 1fy at t11 zorder 2
    stop music fadeout 4.0
    "Something in the way she spoke doesn't seem right."
    "It's giving me the same feeling as when she was talking earlier."
    "She's hiding something from me again."

    menu:
        "But what do I do?"

        "Make sure everything is fine":
            mc "Hey Sayori…"
            s 1fc "Yeah?"
            show sayori 1fb at t11 zorder 2
            mc "Are you sure you had fun?"

            play music t9

            s 1fh "What do you mean?"
            show sayori 1fg at t11 zorder 2
            mc "Something about the way you said some things earlier..."
            mc "It didn't sit right with me."
            s 1fx "Don't worry about me [player]."
            s "I was just nervous was all."
            show sayori 1fd at t11 zorder 2
            "If there's one thing I learned about her in the past few weeks of being closer with her, it's that not everything is as it seems…"
            mc "Tell me what's really wrong."
            s 1fh "It's nothing, really."   # was 4dh
            s 1fx "I promise I was just nervous."   # was 4dz
            show sayori 1fd at t11 zorder 2     # was 4dd
            mc "We both know that's not true, Sayori."
            s 1fv "Please, just drop it."
            show sayori 1fu at t11 zorder 2
            "I can tell through the tone of her voice that whatever it is , she finds it incredibly distressing."
            "I'll save it for another time."
            mc "I'm sorry, Sayori."
            show sayori 1fn at t11 zorder 2
            mc "Goodnight, then, I guess."
            s 1fp "No, wait!"   # was 2dp
            s 1fk "Can I…"  # was 2dd
            s 1fc "Stay at your place again, [player]?"  # was 2dz
            show sayori 1fb at t11 zorder 2
            mc "Yeah, sure, just go change into something a bit more comfortable first."
            s 1fr "Okay!"   # was 4dr
            show sayori 1fq at t11 zorder 2   # was 4dq
            mc "Want me to wait for you in your house, my house, or right here?"
            s 1fl "You can wait at your place, I...actually have something to do."
            s 1fc "I'll be over in like thirty minutes, okay?"
            show sayori 1fb at t11 zorder 2
            mc "Hm? What do you have to do?"
            s 1fl "It's nothing you have to worry about, I promise."
            s 1fr "See you in a little while, okay?"    # was 4dr
            "I shrug my shoulders."
            mc "Sure thing. See you."
            stop music fadeout 1.5
            show sayori at thide zorder 1
            hide sayori


            scene bg bedroom
            with wipeleft_scene

            "I wait about a half hour before Sayori enters my house like any other Sunday."
            show sayori 1br at t11 zorder 1
            show sayori 1br at t11 zorder 1
            play music t5_sayori
            s "Hey, [player]!"
            show sayori 1bq at t11 zorder 2
            "And she has a mysterious bag with her?"
            mc "What's in the bag?"
            s 1bc "Oh, it's nothing, really…"
            s 4bx "Just some homework we both haven't done yet."
            mc "Oh...okay."
            mc "So I assume you wanna get to work on that now?"
            s 1bq "Uh-huh."
            "I have to admit I'm a little worried about what she was keeping mum about earlier."
            "But I also admit that handling someone's feelings, especially someone in Sayori's condition, is a pretty foreign concept to me."
            "I decide that the best thing would just be to get this homework finished, and then sleep it off."
            mc "So, what's first on the agenda?"
            s 1bc "Math, naturally."
            show sayori 1bb at t11 zorder 2
            "{i}Where's the nearest cliff?{/i}"
            s 1bc "I actually got a lot of it done in class, but there's this one that's been tripping me up."
            s "I hope we can put our heads together to figure it out."
            "I sigh involuntarily."
            show sayori 1bb at t11 zorder 2
            mc "Alright, let's see...number 22...the square root of x over 2 plus 4 equals the cube root of 2x plus 8…"
            "…"
            "....."
            "...I think I've gone brain dead already."
            s 4bj "Hey! [player]! Snap out of it!"
            show sayori 4bi at t11 zorder 2
            mc "Uh, Sayori, do you think you'd wanna do something else?"
            s 4bh "[player], we have a test coming up soon, we need to focus."
            show sayori 4bg at t11 zorder 2
            mc "I know I know, but we just got done with a date."
            mc "Isn't it a little weird to wash down a nice date with homework?"
            mc "Not exactly my chaser of choice."
            s 2bj "[player], we're too young to drink."
            show sayori 2bi at t11 zorder 2
            mc "It's just a figure of speech."
            "Sayori thinks on it for a few moments."
            s 1bx "Yeah, okay. We can do something else for now."
            show sayori 1ba at t11 zorder 2
            mc "Cool, thanks."
            mc "So, any ideas?"
            s 5bb "Well, there is one thing I'd kinda like to do…"
            mc "Uh…"
            "I have a feeling I know where she's going with this, but honestly…"
            "I'm not exactly in that kind of mood."
            "For some reason, being around Sayori has gotten me all nostalgic."
            "..."
            "There's something!"
            mc "Or!"
            mc "H-how about we play a game from when we were kids!"
            s 5ba "O-oh...okay, that sounds fun!"
            show sayori 5bd at t11 zorder 2
            "She seems disappointed, but quickly forgets about it."
            "I think she actually likes the idea."
            hide sayori
            "I go to my bedroom closet and open the door, then try to climb my way upward in order to reach the board games from my childhood."
            "Kind of ironic that they're so high up, and partially inconvenient."
            show sayori 2bc at t11 zorder 2
            show sayori 2bc at t11 zorder 2
            s "What do you have in there, anyway?"
            show sayori 2bb at t11 zorder 2
            mc "Hm, let's see…"
            mc "We got...Connect 4, Candy Land, Chutes and Ladders, Battleship…"
            mc "And that's about it. Take your pick, I'm cool with whatever."
            s 2bc "How about...Battleship?"
            mc "That's perfectly fine with me."
            show sayori 2bb at t11 zorder 2
            "I power my way to the top, then stumble from the pressure of everything pushing me down."
            show sayori 2bn at t11 zorder 2
            "I trip and fall forward onto my face, but luckily I land on a pile of old clothes and bedsheets."
            mc "Pfffth, crap!"
            s 4bm "[player], are you alright?!"
            show sayori 4bn at t11 zorder 2
            mc "Y-yeah, I'm fine, this closet was just never meant to be opened or interacted with by humankind."
            "Regaining my balance, I decide to brute force everything."
            "In one swift motion, I rise to the top of the closet and grab the Battleship box, which was luckily on the very top of the stack of games."
            mc "Yes! Got it!"
            s 1br "Good job!"
            show sayori 1bq at t11 zorder 2
            "Sayori and I sit on the floor of my bedroom, then I open the game and sort out all the pieces."
            "Sayori wants to be red, so I take the blue pieces."
            
            
            scene bg bedroom
            with wipeleft_scene

            "I read the small rulebook pamphlet, which is miraculously still in the box after about a decade."
            "As I refresh myself on a few of the rules, I relay them to Sayori."
            "When I finish reading, I look up at her."
            show sayori 1be at t11 zorder 2
            show sayori 1be at t11 zorder 2
            mc "Any questions, Sayo--"
            stop music fadeout 4.0
            "I look up at her and see a bit of a saucy expression on her face."
            mc "W-w-why are you looking at me like that?"
            s 1bc "I have an idea."
            "{i}I'm almost too nervous to ask…{/i}"
            s 1bl "So, I know that you didn't wanna...you know...earlier, but…"
            s 5ba "I was thinking that we could make this game a little bit more interesting?"
            mc "Define…{i}interesting{/i}."
            s 5bb "Well...I was thinking that maybe...after every time we each sink one of each other's boats…"
            play music t7
            s 5bd "We could take off an article of clothing?"
            "..."
            "I don't have the mental capacity to fully register this suggestion."
            mc "Y-you mean like...strip poker?"
            s 4bs "Yeah exactly! But like...Strip Battleship, instead! Ahahaha~!"
            show sayori 4bq at t11 zorder 2
            mc "S-Sayori, I don't…"
            mc "Where did this come from?"
            show sayori 1bn at t11 zorder 2
            mc "I never imagined you acting this way."
            s 1bk "I...I'm sorry...do you not like it?"
            mc "Well I didn't say that, it's just...super unexpected."
            show sayori 1by at t11 zorder 2
            mc "But...heh, screw it, this could be fun."
            "I'm signing myself up for some level of trouble if I'm not careful."
            "Guess I should just play some top notch Battleship!"

            scene black
            with fade
            "Sayori and I each make sure that we have an equal number of clothes to be taken off."
            "I had to put on a light jacket to even things out, so we each had on five articles of clothing to match the number of ships."
            "Sayori counted her bow, and I insisted that was the first thing she'd be forced to remove."
                        
            scene bg bedroom
            with wipeleft_scene

            "We begin playing Battleship."
            "True to the rules we've established, each time I get a ship sunk, I take something off."
            "And every time Sayori loses a ship, she also takes something off"
            "It ends up being a lot more fun than I expected!"
            "Despite the circumstances, the sexuality of the situation kinda gets diffused by how much fun we have picking on each other."
            "That is until I notice Sayori has nothing but her bra and panties on, and I sink her aircraft carrier."
            show sayori 1ux at t11 zorder 2
            show sayori 1ux at t11 zorder 2
            s "Ehehe~, it's your choice, [player], what do you wanna see first?"
            show sayori 1uq at t11 zorder 2
            "Sitting here with nothing but my boxer shorts on, I think she can tell I'm getting very excited."
            "I'm really not super sure how to respond."
            "I saw Sayori nude not super long ago, but this level of playfulness starts to take a toll on my male instincts."
            mc "B-b-b-b…"
            "I'm stuttering like an idiot."
            s 1ur "Ehehe~! Spit it out!"
            show sayori 1uq at t11 zorder 2
            mc "Boobs…"
            mc "I MEAN, BRA."
            mc "T-take off your bra, next, please, madame, if you don't mind."
            s 3us "Pffft, you're so silly, [player]."
            s 4ul "You'll really get to see how much bigger they've gotten!"    # was 4sx
            s 4us "As you wish, it's coming off~!"
            "Sayori begins to move her hands toward her bra, but then she stops suddenly."
            s 2uc "Oh, but first…"    # was 2sc
            s 1ux "D8." # was 2sx
            show sayori 1uq at t11 zorder 2
            "..."
            "She sunk my battleship."
            mc "No way, you have to take it off before you make your next move!"
            s 1uj "Hey I came up with the game, so I say this is totally within the rules!"
            show sayori 1ui at t11 zorder 2
            mc "That's so bogus!"
            s 1ur "I'm waitiiiing~!"  # was 4ss
            "Damn, she really got me with this one."
            mc "Fine, you win, congratulations."
            show sayori 3uq at t11 zorder 2   # was 4sq
            "It finally hits me that now I have to take off my boxers and show Sayori my private parts."
            "Which, admittedly, I don't necessarily have a problem with, but regardless, this is awkward."
            show sayori 3ud at t11 zorder 2   # was 4sq
            "I slowly stand up and then look at Sayori, biting her lip waiting for me to proceed."
            "The look on her face is getting me very aroused, and I know I won't be able to conceal my excitement from Sayori."
            "I rip off the band-aid, so to speak, then pull down my boxers and show Sayori everything."
            show sayori 4us at t11 zorder 2   # was 4sq
            "Sayori begins to clap."
            s "Bravo, [player], bravo! He's glorious! Ahahaha~!"  # was 4ss
            mc "Well, here we are, then."
            mc "Game's over."
            mc "I'm naked, you're almost naked."
            mc "Where do we go from here?"
            s 2ub "I think…"  # was 2sa
            s 1ur "It's time to do some math."    # was 2sx
            mc "What?!?!"
            s 1ux "Let's get dressed again, [player], we got homework to do."
            show sayori 1ua at t11 zorder 2
            "..."
            "I hate everything about this."
            "I didn't even wanna take things too far tonight, but it's hard to ignore my urges when you're so close to the light at the end of the tunnel!"
            "Well, I guess she's right."
            "Better just suck it up and accept defeat like a man."
            stop music fadeout 1.5
            $ battleship_played=True


            scene bg bedroom
            with wipeleft_scene
            play music t5_sayori

            "A couple of hours go by, and Sayori and I have mercifully completed a majority of the math homework we needed to finish."
            "{i}You wouldn't believe how much doing math completely kills your sex drive{/i}."
            "She and I make some instant meals together and eat them by candlelight that evening."
            "Eventually, we end up in bed at around 10: 30, as I let the TV in my room run to lull us to sleep."
            mc "You ready to call it a night, Sayori?"
            stop music fadeout 6.0
            show sayori 1bh at t11 zorder 2
            show sayori 1bh at t11 zorder 2
            s "No, not yet."
            s "I needed to say some stuff first."
            s 1bk "You were right."
            "I knew it…"
            mc "Sayo--"
            s 1be "Please."
            s "..."
            s 1bg "I just…"
            s 4bw "I just feel like I don't deserve it sometimes."
            s 1bv "Especially tonight."
            s "I don't know what I did to deserve you."
            s 1bv "All I did was tie you down like an emotional anchor."
            show sayori 1bu at t11 zorder 2
            mc "Sayori stop."
            mc "You aren't a burden."
            mc "If I was in any way unhappy with us being in a relationship, I wouldn't be here."
            mc "Trust me."
            play music t10
            mc "I love you."
            "Even though I'm not yet used to saying that to Sayori.."
            "It feels right."
            s 1bv "I…"
            s 1bv "I'm sorry."
            s 1bw "I love you too!"

            scene black
            with dissolve_scene_full

            "Suddenly, I feel my lips against hers."
            "But I was the one to pull her in for the kiss this time." #(keep this)
            "I can feel the passion on her end."
            "I wrap my arms around her and pull her closer."
            "She groans softly, and I can tell she's enjoying this as much as I am."


            scene bg bedroom
            with dissolve_scene_full

            show sayori 1by at t11 zorder 2
            show sayori 1bv at t11 zorder 2
            s "[player]..."
            s "That was nice..."
            show sayori 1bt at t11 zorder 2
            "My face is as red as a beet, and my heart is beating like a drum."
            "I have a strange feeling about this…"
            mc "Yeah, that was…"
            mc "Special."
            stop music fadeout 2.0

        "Say goodnight":
            mc "Yeah, no problem…"
            mc "Well then, goodnight, Sayori."
            s 2fc "Actually, I was hoping I could stay over at your place tonight…"
            show sayori 2fb at t11 zorder 2
            mc "Alright then, but let's stop by your place so you can get changed."


            scene bg kitchen 
            with wipeleft_scene
            play music t5_sayori

            show sayori 1ba at t11 zorder 2
            "Once Sayori is done changing, we head back to my house."
            "I notice Sayori holding a strange red bag in her arm."
            mc "So, what's in the bag, Sayori?"
            s 2bx "It's a secret."
            show sayori 2bwink at t11 zorder 2
            s "For now."
            "As usual, that wink makes me feel like I'm standing on the Sun."
            show sayori 1ba at t11 zorder 2


            scene bg bedroom
            with wipeleft

            show sayori 1ba at t11 zorder 2
            mc "Alright then, you ready for bed?"
            s 1bx "Yeah."
            mc "You can have the bed, I'll take the couch."
            s 1bc "Why don't we just share the bed?"
            mc "Uh, yeah. Sure"
            stop music fadeout 2.0

    scene black
    with dissolve_scene_full
return

label sayoriroute22:

    scene bg bedroom
    #MC wakes up with eye open visual effect.

    "I wake up, groggy as I've ever been."
    "Despite this, I still feel good. Proud, in fact."
    "I had a very good time with Sayori yesterday, and we even got some homework done."
    "I remember our little game, at which point I lift my head up off my pillow and look at the floor."
    "There, I see our game of Battleship, still scattered across the floor."
    "I should clean that up soon."
    "But, not right now. Right now, all I ought to do is appreciate my surroundings."
    "Specifically, I should appreciate the ball of sunshine huddled into my shoulder, with her arms wrapped around mine like it's a teddy bear."
    "I feel so warm inside seeing her so comfortable. And I'm the reason for that."
    "If that doesn't make a person feel good, I don't know what would."
    "I observe Sayori and appreciate the light she's radiating."
    "There's so much purity coming from her. It's enough to intoxicate someone."
    "I smile at my girlfriend, who's still lying there lightly snoring."

    scene black

    show sayori_bed

    "There's only one word to describe her."
    "Amazing."
    "I never realized how cute Sayori looked until now."
    "I mean, I always knew she was cute,"
    "But I wasn't conscious of it until now."
    s "Mmfff..."
    "Sayori stirs."

    show sayori_bed_one_eye

    s "Hey there~"
    "God."
    "I recall last night's events, and the night before?"
    "Despite us not going all the way last night, our impromptu game of Strip Battleship was…"
    "Undeniably sexual in nature."
    "{i}What's going on?{/i}"
    "{i}I'm not even that attractive!{/i}"
    mc "Good morning."
    s "*{i}giggles{/i}*"
    s "Good morning to you, too."
    "This position we're in…"
    "It feels so nice."
    "I never want to leave."    
    "It's been nearly a year, and I still can't believe I ended up with Sayori of everyone."
    "But I wouldn't trade her for the world."
    mc "I'm surprised to see you up so early."
    s "Oh really? What time is it?"
    mc "Let me check."
    "I take a brief glance at my wrist watch…"
    "..."
    "That I apparently never took off…"
    "And also forgot I even had."
    "It's 8:30, class starts in 45 minutes."
    mc "Sayori, I hope you have your uniform, because we've got to hurry."
    s "Haha, yeah…"
    s "About that.."
    mc "Please don't tell me…"
    s "Yup."
    s "Gotta go back to my place to get my stuff."

    scene black

    "We don't even have enough time to have breakfast or brush our hair before running off to school."

    scene bg corridor
    with wipeleft
    
    "I'm here after school like almost every day."
    "The club's already started."
    "I can hear Sayori inside talking to Monika about something."
    "I can't make out what they're saying, though."
    "So, I enter the club room to see what everyone's up to."

    scene bg club_day

    show monika 1i at t21 zorder 2
    show monika 1i at t21 zorder 2
    show sayori 1g at t22 zorder 2
    show sayori 1g at t22 zorder 2

    m "So the reason I had to put the club on hiatus was--"
    s "Oh!"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    s "Hi, [player]!"
    m "Oh! Uh, hey, [player]."
    m "Sayori, we'll talk later, okay?"
    s "Oh, okay!"

    show monika at thide zorder 1
    hide monika

    "Monika hurries off to go talk with Yuri about something, leaving me and Sayori alone."
    mc "Sayori.."
    s "Yes?"
    mc "I forgot to write a poem today.."
    s 4c "Uh oh!"
    s "I would give you mine for the day, but.."
    s 5b"It's pretty personal to me."
    mc "Wait, how did you write one?"
    s 1c "Huh?"
    mc "You slept at my place last night, how could you have written a poem?"
    "I almost immediately regret saying that."
    "I can practically feel the other girls staring at me."
    "I don't even need to look at them to know that they're whispering."
    "Sayori doesn't seem to notice them."
    s 1x "Oh!"
    s 1r "I got that done in class before I got here!"
    mc "I guess I don't have a poem today then."
    s 1a "It's ok, the others will probably understand."
    "I half expect one of the girls,"
    "Specifically the one with the pink hair who shall remain anonymous"
    "To mockingly yell something along the lines of \"Yeah we will!\""
    "…"
    "So that didn't happen."
    "We all get ready to share our poems, at least those of us who wrote one."

    show sayori at thide zorder 1
    hide sayori
    #Screen black left to right 
    #BG is still the doki's literature club
    #what, i don't get what you mean-jan
    "I opt out of reading poems today."
    "I watch Yuri read Sayori's poem,"

    show yuri 1c at t21 zorder 2
    show sayori 1a at t22 zorder 2

    "Yuri seems to really like it…"
    "I try to tune in, but I get a visit from a little certain someone."
    "A certain small-framed someone."

    show yuri at thide zorder 1
    hide yuri
    show sayori at thide zorder 1
    hide sayori
    show natsuki 1e at t11 zorder 2

    n "Slacking off again?"
    mc "No, I'm just tapping out for the day."
    n "If that's what you tell yourself."
    n "But rumor has it you didn't write a poem today."
    "Of course she overheard…"
    mc "Yeah?"
    mc "What about it?"

    show natsuki 1d at t11 zorder 2

    "A devious grin breaks across her face."
    "I immediately get nervous. That smile can't mean anything remotely pleasant for me."
    n "A little birdie also told me Sayori slept over at your place the last couple nights…"
    "I break out in a cold sweat."
    n "So tell me…"
    n "What exactly {i}were{/i} you doing last night?"
    mc "I.."
    "I'm put on the spot."
    "I don't even know how to properly respond to that."

    $flag = False
    menu :
        "Tell the truth" :
            $flag = True
            mc "Well, uh…"
            mc "Sayori and I have just wanted to spend a lot of time together lately."
            mc "We've been getting really...close."
            "I lower my voice as much as possible."
            "I don't want anyone else hearing this…"
            "At least not yet."
            "I lean in, and so does Natsuki."
            mc "One thing kinda just.."
            mc "Led to another, and, we…"
            "Natsuki steps back."

            show natsuki 1h at t11 zorder 2

            "She knows what happens next."
            "Not another word needs to be shared."
            "I follow suit to find her red as a tomato."
            "We just sit in silence for a few moments."

            show natsuki 1q at t11 zorder 2

            n "I…"
            n "I won't tell anyone."
            "It's strange, getting such a response from Natuski."
            "I'm used to her general brash attitudes."
            "She whispers something."
            n "No offense, but I gotta do this."
            n "Everyone else will get suspicious."
            "Suspicious?"
            "What does she-"

        "Avoid the question" :
            "Oh boy."
            "I'm not in the mood today."
            mc "What's it to you?"
            n 4l "I just wanna hear if the talk of the town is true at all."
            n "Did you and Sayori do...{i}that{/i}?"
            "She said the last bit a little louder than the rest."
            "Perhaps intentionally…"
            "I turn red."
            mc "I-I uh.."
            mc "We were just.." 
            "I surrender."
    n "Ha!"
    n "I knew it!"
    n 1v "You and Sayori were totally making out last night!"

    if flag : 
        "Oh. So that's what she meant. "
        "My face turns beet red."
        "The other girls turn towards us."
        mc "I-It's not what you guys think! We only had a sleepover, we've been doing that since we were kids!"
        n 1d "Suuuuurrreee. Is that what they're calling it now-a-days? A sleepover?"

    show natsuki 1d at t21 zorder 2
    show yuri 2r at t22 zorder 2

    y "Natsuki!"
    "Yuri is visibly angry."
    y "That's unbelievably rude!"
    y "[player]'s and Sayori's personal life is none of your business!"
    y "It doesn't matter how intimate they became, it's-"
    n 1f "And there you go."
    n "Ruining my fun again."
    n 1d "I wasn't serious, I was just teasing him!"
    n "Maybe you need to learn how to take a joke."
    #Yuri-saltsanity
    #what do you mean-jan
    y "Maybe you need to shut up and act your age once in a while."
    "I start to stand up."
    "I don't feel too good…"
    "Monika practically sprints over."

    show natsuki 1d at t31 zorder 2
    show yuri 2r at t32 zorder 2
    show monika 4b at t33 zorder 2

    m "Ladies! Ladies!"
    m "That's enough!"
    m "You should {i}not{/i} be talking like this, about anyone!"
    m 4k "Especially in front of their faces!"
    "Due to my sensory overload, I completely forgot Sayori was involved."

    show natsuki 1d at t41 zorder 2
    show yuri 2r at t42 zorder 2
    show monika 4k at t43 zorder 2
    show sayori 1f at t44 zorder 2

    "She shuffles into the group."
    "She looks like she's about to cry."
    "The girls dive back into arguing as Sayori tugs on my sleeve."

    show natsuki at thide zorder 1
    hide natsuki
    show yuri at thide zorder 1
    hide yuri
    show monika at thide zorder 1
    hide monika
    show sayori 1f at t11 zorder 2

    s "Hey.."
    s "Can we please leave?"
    mc "But what about everyone else?"
    s "They'll cool down eventually.."
    s "They'll understand why we left…"     
    s "But please, we need to go.."
    "I nod as I take Sayori's hand in mine and leave the clubroom."

    scene bg corridor
    with wipeleft

    "We both walk together, still holding each others' hands."
    "She just stares down at her feet as we walk."
    mc "Sayori."
    "Sayori just grumbles."
    mc "Sayori~"
    "I say it with a more playful tone, but she just grumbles a little louder."
    "I sigh."
    mc "Sayori, I know that what happened in the club is bothering you."
    mc "It wasn't your fault."
    mc "It wasn't really any one person's fault."
    mc "It was just a dumb tease that went overboard a little."
    "Sayori barely squeaks out a response."
    s "[player], i-it was because of me."
    s "I showed Natsuki my poem and she knew it was about you."
    s "She teased me a little bit, too, but I should have known that would have eventually caused her to go to you and tease you, too."
    mc "I may not know if that was 100 percent true or not."
    mc "But even if it was, it wasn't your fault."
    mc  "Besides, Yuri seemed to like it quite a bit."
    mc "I never got to read your poem, you know."
    "She slowly unfolds a little piece of paper she kept in one of her blazer pockets and hands it to me slowly."
    "I take it."

    python:
        s21_poem3 = Poem(
        author = "sayori",
        title = "Warm Inside",
        text = """\
    A gentle breeze flows,
    fluttering in through my window.
    The rising sun leaps & bounds through the cracks,
    It makes me feel warm inside.

    He steps outside his house, 
    A dull expression of mourning glee,
    I cheer him up every day,
    But it never seems to stay.

    It doesn't matter, because when I see his smile,
    his beautiful...
    ..Face.
    It makes me feel warm inside.

    I just want to see him.
    I want to hold him.
    I want to hug him.

    Because he makes me feel warm inside."""
        )

    call showpoem(s21_poem3, music=False)

    "I start to tremble."
    "I knew she made this for me."
    "I just.."
    mc "I just.."
    "I can't control myself as my lips meet hers."

    scene black
    with dissolve_scene_full

    "I can tell she was surprised by the gesture, as shown by a surprised grunt."
    "She quickly eases into it as we continue to pull ourselves closer."
    "I can feel her breaths quicken."
    "I think she might be crying now…"
    "I pull away."

    scene bg corridor
    with dissolve_scene_full

    s 1k "..."
    s "I…"
    "We're both at a loss for words for what seems like hours."
    s 1e "Take me home.."
    "She says that in a way I can only say as \"whimsical.\""
    "We both know, and want, what comes later."
    "And we both know it's my house."

    scene bg custom living room
    with wipeleft

    "When we get home, we're both pretty much burnt out."
    "Neither of us have changed out of our school clothes."
    "I flop down onto my couch with an audible thump."
    mc "Bluh.."
    "Sayori joins me and we wrap a blanket around ourselves to get comfortable."
    mc "So what do you want to do now that we're home?"
    s "I dunno~"
    s "Got any ideas?"
    mc "Wanna sleep on the couch?"
    "Sayori looks confused."
    s "What for?"
    mc "I dunno, just thought it'd be fun, you know?"
    s "Oooh! I see what you mean!"
    s"Easy cuddles, yeah?"
    mc "Exactly!"
    "Actually I just thought of that but why ruin Sayori's fun?"
    "I love cuddles."
return
