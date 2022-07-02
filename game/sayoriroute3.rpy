label sayoriroute3:
    scene black
    with fade
    s "..."
    s "..."
    s "..."
    s "...{i}once in a lullaby..."
    call sayoriroute31
    call sayoriroute32
    call sayoriroute33
    jump sayoriroute4
return

label sayoriroute31:
    scene black
    with fade
    "It's been about 2 months since I've noticed something change in Sayori..."
    "Almost every night she comes over to cuddle and sleep."
    "I'm not complaining about that, not at all."
    "In fact, I've noticed I've been in a much better mood in general since she started to because of that."
    "Can't figure out why she does. Maybe she's just so used to it since the first time?"
    "Or maybe she's just so used to me..."

    "Again, I'm not complaining."
    "Well, not too much, at least."
    "Who am I to deny her, of all people, that sense of joy?"
    "I feel myself start to wake back up from my slumber."
    mc "Mhh..."

    scene bg bedroom
    with dissolve_scene_full

    "I open my eyes to look at the clock and calendar."
    "It's nine o'clock on a Sunday."
    "That means no school."
    "Just Sayori."
    "I look over to the other side of my bed."
    "Where she used to be the night before, there's an empty spot."
    "I start to get dressed to see if she needed to go do something like use the bathroom."
    "I can't imagine she ran off during the night..."
    "Almost as soon as I'm done getting dressed, I hear the fire alarm go off."
    "I rush to the kitchen to see what happened only to find Sayori crying over some burnt eggs."

    scene bg kitchen

    show sayori 1bv at t11 zorder 2

    mc "Sayori!"

    show sayori 4bm at t11 zorder 2

    "Shock replaces her look of depression almost instantly as she looks up from the eggs and toward me."

    s "[player]!"
    s "I'm so sorry!"
    s 4bp "I just wanted to make you a delicious breakfast like you do for me and..."

    "I hug her to calm her down before she gets too flustered."
    mc "It's okay. The thought is what counts."

    show sayori at thide zorder 1
    hide sayori

    "I release my grip and toss out the charred eggs."
    "I make some new ones for her and I just how we like them."
    "We sit down at the dining room table across from each other to eat."
    "I start to dig in to my egg, but I don't even need to look up from my plate to know that Sayori isn't eating."
    "I hear her silverware tink against the ceramic plate."
    "She's clearly just prodding at it."
    "Before I even put the egg in my mouth I set my fork down and look up."
    "My suspicions were absolutely correct."

    show sayori 3bk at t11 zorder 2

    mc "Something on your mind?"
    s 3bh "I guess I just, kinda feel bad about earlier is all..."
    mc "Don't worry. You didn't do any harm."
    mc "I still have the house, after all."

    show sayori 3bd at t11 zorder 2
    "She smirks slightly."

    s 1bx "Thank you..."

    show sayori 1bd at t11 zorder 2

    "I can hardly tell if she's hiding her sorrow or if she's being genuine."
    "I guess that's progress..."
    "We finish our breakfast without a hitch after that."
    "After we're done, we both plop back on the couch."

    s 1be "So..."
    s 1bc "What is it you want to do?"

    mc "Hmm.."

    "I take a second to think."

    s "I heard there's been a lot of good movies that were released recently."

    mc "Wanna go catch a movie at the theater?"

    show sayori 4bs at h11 zorder 2
    s "Of course!"

    mc "Alright, when should I pick you up?"

    s 1bc "Let's see..."
    play music t6
    s 1bx "There's one movie that I really want to go see that has a screening at 8. So we can have supper and head out by 6:30?"

    mc "Works for me, see you then, Sayori."

    scene bg theater
    with wiperight

    "The dinner went well."
    "If the definition of well is that someone put too much mayo on Sayori's burger."
    "Oh and they burnt mine, too."
    "But at least we have the movie here."

    show sayori jacq at t11 zorder 2

    mc "So, which movie is it you wanted to see?"


    s jacr "Eheheheh..."
    s jacl"I..."
    s "Actually didn't have one in mind."
    s jacs "I just wanted an excuse to go out."

    "I instinctively sigh."
    "Classic Sayori."

    show sayori jacr at h11 zorder 2
    s "So, you can pick whichever movie you'd like."

    mc "Hmm..."

    show sayori jacr at thide zorder 2
    hide sayori

    "I look around a little bit and see a bunch of the posters, weighing my options."

    "Sayori is looking in the opposite direction of me. She seems to be enamored by a poster of a movie I can't quite make out since she's in the way."

    "Though I do see some yellow bricks and some girl's feet with red shoes on them."

    "Eh, whatever."

    "I continue to search for something good to watch."

    "This theater has a few movies running at 8."

    $flag = False

    menu:
        "But which one would we like to see?"
        "Comedy":
            $SayoriVar += 1
            mc "Ooh!"
            mc "How about this one?"

            "I point at a poster for this old comedy movie from Britain."

            "I'm surprised they even have it playing."
            "Must be the anniversary."

            mc "Sayori!"

            "She walks over."

            show sayori jacx at t11 zorder 2
            s "Yeah?"

            mc "This look any good to you?"

            s jacr "That looks awesome!"

            mc "So, that's a yes?"

            show sayori jacr at h11 zorder 2
            s "Absolutely!"

            show sayori jacr at thide zorder 2
            hide sayori

            scene black
            with wiperight

            "We buy our tickets, which are actually surprisingly cheap for the movie."
            "We  have enough money left over for a large popcorn and a couple large sodas."
            "Our movie is in theater 13."

            scene bg theater_in
            with wiperight

            "Sayori and I manage to find some really good seating."
            "The theater isn't really packed, even though the movie has a serious cult following."
            "The movie follows an old British king portrayed by an old, but popular British comedian as him and his band of crusaders embark across europe looking for the Ark of the Covenant."
            "Of course with comedic results and antics."
            "I'm in the dead center of the theater, and Sayori is on my right."
            "The opening credits roll."

            s "This looks old!"
            s "And British!"

            mc "That's because it IS British."

            "I notice a couple of greasy looking guys a few seats down looking back up at us."
            "They aren't happy."
            "I turn to Sayori."

            mc "Sorry, could you keep it down a bit for the..."

            "I feel the men's glare burn through my soul."

            mc "Errr... wonderful gentlemen in front of us?"

            "Sayori flushes red and nods."
            "I put my arm around her to soothe her out."
            "Seemingly content, the men turn around."
            "Despite the rough start to the film, what with the greasy diehard fans, the rest goes really smoothly, actually."
            "Sayori laughs harder than I've ever heard her laugh before at some of the jokes."
            "The greasy fellows in front of us gave off a more approving presence in regard to Sayori, as opposed to the more confrontational aura from earlier."
            "It's almost as if they're silently saying 'we've converted her,' amongst themselves."
            "And I can't really blame them for being happy either."
            "Seeing Sayori genuinely enjoy herself, especially with everything..."
            "The rain clouds."
            "The depression."
            "It makes it all seem so foreign."
            "It makes me..."
            "..."
            "The kiss on the cheek I give Sayori felt instinctual."

            show sayori 4bm at h11 zorder 2
            "She falls silent almost instantly, and turns a beet red."

            s 4bh "[player]..."
            show sayori 4be at t11 zorder 2

            mc "S- sorry..."
            mc "I... couldn't help it."

            s 1bc "It's fine.."
            s "Thank you.."
            s 1bx "But please."
            s 3bwink "Keep it down for the men in front!"

            $ y_name = "Greasy Guy"
            y "You tell him, sister!"
            $ y_name = "Yuri"

            show sayori 4br at t11 zorder 2

            "Their entire group erupts in laughter, as if they were a bunch of drunken knights singing some sort of song in a bar,"

            show sayori 4br at thide zorder 2
            hide sayori

            "Well, that also is what's happening in the movie now."
            "Perhaps life imitates art after all."
            "The movie finally ends, and when the credits roll, Sayori is in tears from the laughter."
            "I can tell she really enjoyed herself tonight."
            "As the credits roll, Sayori and I get up and leave the theater and head for the outside."

            scene bg theater_evening
            with wipeleft

            "Sayori is still giggling 10 minutes after the movie ended."

            show sayori jacr at t11 zorder 2
            s "Hahah, that movie was amazing!"
            s "I really had a good time tonight!"
            s "I can't tell you the last time I laughed that hard!"

            show sayori jact at t11 zorder 2
            "She takes a moment to collect herself"

            s jacr "Woo-ee!"
            s jacx "This may be odd to ask, but..."
            s "Is it ok if we go back to my place?"

            show sayori jaca at t11 zorder 2

            mc "I don't see a problem with that."
            mc "So, sure."

            #Sleep at Sayori's house
            $flag = True
            scene bg sayori_bedroom_evening
            with wipeleft

            "Almost as soon as we get through her room door, Sayori and I plop into bed."

            show sayori 4bh at t11 zorder 2
            s "Hey, uh, before we get to sleep..."
            s 3bc "I want to thank you for the wonderful evening."
            play music t9
            s 3br "I really had fun."
            s "I felt at ease watching that movie with you."

            show sayori 3br at thide zorder 2
            hide sayori

            "I wrap my arms around Sayori."

            mc "I..."
            mc "I don't know what to say..."

            s "Don't say anything more..."

            "I feel her start to clutch for my shirt."

            mc "No, not tonight.."
            mc "Let's just cuddle."

            "I can't help but feel like she didn't like my answer."

            s "Okay."

            "That answer doesn't sit well with me. But I take it."

            mc "Goodnight, Sayori."

            s "Goodnight, [player]."
            s "I love you."    
    
        "Romance":
            $SayoriVar += 1
            "I take a moment to scan the posters."
            "I see one for a romantic movie that came out just last week."
            "My rep could be ruined if I actually pay money to go watch this, but at this point, being the only guy in an all girls literature club, I think I'm pretty secure with my masculinity."

            mc "Sayori."
            mc "What do you think about romantic movies?"

            show sayori jacc at t11 zorder 2
            s "I've never seen one before."
            s jacx "But I'd be willing to try it out, if you want to!"

            mc "Alright, then, it's a deal."

            show sayori jacx at thide zorder 2
            hide sayori

            scene black
            with wiperight

            "We get the tickets and a tub of popcorn."
            "I'm not too sure on this one, she might like it, or she might not. Who knows?"
            "We are located at theater 15."


            scene bg theater_in

            mc "Theater 15, here we are"

            "It didn't take us long to find our screen, and we're sat down in our allocated seats within five minutes, even with Sayori going to the bathroom beforehand."

            "The theatre is fairly crowded, this is a popular movie, after all."

            s "So what's this movie about?"

            mc "Well, I don't know the details, but I think it's about a poor woman who falls for a rich man, but social differences get in the way of their relationship."

            s "Sounds depressing, I hope they get a happy ending..."

            mc "There's only one way to find out!"

            "With that, the lights dim, the obligatory \"oooh\" rings out among the audience, and the movie begins."
            "We're about twenty minutes in now, and the plot has begun to thicken."
            "Sayori has clearly taken a liking to a character called Goldwoman by the way her eyes light up every time he comes into frame."
            "I'm glad she's enjoying herself, although she's strangely silent for a girl I know to be bubbly beyond belief."
            "I guess she's just that into it."
            "Suddenly, a sex scene erupts from almost nowhere."
            "I look over to Sayori next to me."
            "She seems shocked, but gradually her expression returns to one of subtle appreciation."
            "The scene lasts a surprisingly long time."
            "A few minutes in, I feel a nudge on my arm."
            "I turn my head to Sayori once more."
            "She is looking straight at me with a sly grin and a deep red tint, visible even in the darkness of the theatre."
            "She flashes a small wink, then returns to watching the movie with a look of intent upon her face."
            "Does she mean...wow."
            "I can feel my face heating up and my heartbeat racing, and I almost choke on my own saliva."
            "She appears to notice my hands fumbling, as I hear a quiet giggle from next to me."
            "I had no idea she could be so forthcoming."
            "We return to quietly watching the movie."
            "Certain romance scenes occasionally pop up here and there, often accompanied by slight nudges from Sayori."
            "Her entire mood changes, however, at the end of the movie, where the protagonists have their happy ending."
            "I look over to see Sayori lightly sobbing."
            "Sensing her emotion, I wrap an arm around her and place the other hand on her head, slowly petting her soft hair."
            "Her sobbing quietens as I do so."
            "After a few minutes, she looks up at me with glistening eyes and gives me a little nod, signifying that she feels a little better."
            "I remove my hand from her head and release her from the embrace."
            "We sit side-by-side, leaning on each other's shoulders, as the last few minutes of the movie play out."
            "The movie is over and the end credits roll."
            "Sayori seems to have cleared herself up, and finishes the process by giving me a brief hug and a light squeeze."
            "We walk out of the theatre and back into the foyer, where we each use the bathroom then head out."

            scene bg theater_evening
            with wipeleft

            mc "So, what did you think of it?"

            show sayori jacx at t11 zorder 2

            s "I really enjoyed it. It's not so much what I'm into but it was a nice break from the norm."

            show sayori jaca at t11 zorder 2

            "Huh, that was...a genuine and well-structured answer!"
            "What did this movie do to her..?"

            mc "Glad to hear it. Shall we be off?"

            "Sayori nods"

            s jacx "Oh, by the way, I wasn't nudging you for no reason, you know..."

            show sayori jacq at t11 zorder 2
            "She flashes her now infamous sly grin."
            "Once again I feel the heat of entire universes being born upon my face."

            show sayori jacq at thide zorder 2
            hide sayori
            mc "Yeah, let's go.."

            "Sayori giggles and walks beside me."

            scene bg residential_night
            with wipeleft

            "We stroll along the illuminated sidewalk, arms interlinked and shoulder-to-shoulder."
            "Sayori giggles every so often, with a slight blush across her cheeks, while I remain silent with one arm around her."

            show sayori jacc at t11 zorder 2
            s "Hey, can I stay at your house tonight?"

            mc "Sure, but how come?"

            s jaco "Because."

            mc "That isn't an answer..."

            s jacp "Yes it is!"

            mc "Whatever."

            "I decide to drop the subject, I have no qualms about her staying over, and carrying on this conversation would only make things awkward later on."
            "We continue to walk together, exchanging a few words here and there."

            scene bg kitchen
            with wiperight

            "It doesn't take us long to reach my place, and we step inside into the warm air."

            scene bg bedroom_night
            with wiperight

            show sayori 5bb at t11 zorder 2

            s "Hey, about that movie.."

            mc "Yeah?"

            s "Some parts were pretty lewd, right?"

            mc "Yeah..?"

            "I'm starting to sense where she's going with this."

            s 5ba "We could try-"

            "I decide to stop her there."

            mc "I'm afraid that's a no from me, I'm just not feeling up for it right now. I'm sorry."

            s 5bc "But-"

            mc "You're welcome to share a bed, but nothing more, nothing..."
            mc "...lewd"

            s 5bd "Okay..."

            "She looks a little down, but I'm sure some cuddles will help fix that."

            show sayori 5bd at thide zorder 2
            hide sayori

            "We both climb into bed after changing and otherwise getting ready."

            mc "Goodnight, Sayori."

            s "Night, [player]!"
      
        "Drama":
            "I glance at the posters."
            "Nothing in particular strikes my eye in any way."
            "Eenie..."
            "Meenie..."
            "Minie..."
            "Moe..."
            "Hm, this one is actually pretty well known."
            "I heard it was a wholesome life story of a man with an intellectual disability."
            "Even I know the quote, \"Life is like a box of chocolates.\""
            "..."
            "Eh."
            "What's the worst that could happen?"
            "I approach Sayori and point at the poster."
            mc "Hey, Sayori, how does this movie sound?"

            show sayori jacc at t11 zorder 2
            s "What's it about?"
            "Probably should have told her that before asking."
            mc  "It's a story of a mentally disadvantaged man trying to lead a normal life. Sound good?"
            s jacr "Okay!"
            "Sayori flashes her million-dollar smile."
            "Unlike most other things, it doesn't lose a penny of its value despite the fact that it's seen everywhere."
            mc "Alright, in we go then."

            show sayori jacr at thide zorder 2
            hide sayori

            "I calmly stroll into the lobby, and Sayori gleefully skips beside me, almost bounding with a spring in her step."
            "I can't help but smile at her bubbly nature"
            
            scene black
            with wiperight
            scene bg theater_in

            "We take our seats just as the pre-movie advertisements finish. As a glimpse of some cheesy horror flick fades out of the screen, the title card plays"
            "As the first half an hour of the movie go by, Sayori never takes her eyes off the screen."
            "That is, except to reach for more popcorn"
            "The movie doesn't seem all that interesting, really"
            "The main character is, as the poster said, about a mentally disadvantaged man trying to lead a normal life."
            "It seems like an alright movie, and the casting was pretty good."
            "That being said, a lot of the movie seems aimless, and he keeps chasing the same girl who constantly rejects him."
            "That hits a little too close to home with the manga I read"
            "As I halfheartedly enjoy the movie, I glance over to sayori every few minutes."
            "She seems kind of torn up about this, but I don't want to bother her."
            mc "At least she seems to be really enjoying this movie"
            "I say to myself, unthinkingly"
            "Sayori doesn't even seem to notice I said anything, and at this point is even leaning forward in her seat"
            "Once the credits begin rolling, I glance over at sayori yet again"
            "Is she...?"
            mc "Woah, Sayori. Are you- crying?"
            "Sayori sniffles a little and wipes her eyes"
            show sayori jacv at t11 zorder 2
            s "n- no. The movie was just really sad!"
            "Thinking back, the movie was definitely on the sad side, but I wasn't even close to crying"

            scene black
            with wipeleft
            "As we walk outside, Sayori seems to have rebuilt some of her good mood"

            scene bg theater_evening
            with wipeleft

            mc "So, it seems like you really enjoyed it, huh?"

            show sayori jacg at t11 zorder 2
            s "Well, it was okay, I guess..."

            "I raise my eyebrows"

            mc "Sayori, you were {i}crying{/i} at the end of it."

            show sayori jach at t11 zorder 2
            s "Only a little! And besides, how come the movie didn't have any effect on you?"

            "Seeing how much Sayori seemed to enjoy the movie, I hold my tongue"
            mc "I liked it, I guess I just found it hard to relate with the protagonist."

            show sayori jacq at t11 zorder 2
            "Sayori grins"

            mc "What's so funny?"

            s jacx "Well, I would have thought that you of all people would relate to the struggle of a girl constantly rejecting you"
            mc "I'll have you know you're the first person i've ever asked out, and you said yes. So, I've got a perfect record in the dating world"

            show sayori jacx at thide zorder 2
            hide sayori

            "I smirk"
            "Sayori rolls her eyes and grins again, pushing me playfully"

            scene bg residential_night
            with wipeleft

            "As we head home, however, Sayori starts to look more and more like she did right after the movie."
            mc "Hey, do you want to stay the night at my house again?"

            show sayori jacg at t11 zorder 2
            s "Yeah, if that's okay."
            "I look at sayori with confusion"
            mc "Of course you can stay, why would you think I don't want you to?"
            s jace "I- I'll tell you when we get back to your house."

            show sayori jace at thide zorder 2
            hide sayori

            "We walk the rest of the way home in silence"

            scene black
            with wipeleft
            "We reach my front door an I walk in, with Sayori following close behind me"

            scene bg kitchen
            with wipeleft

            mc "So, what happened during the movie?"

            show sayori 1bg at t11 zorder 2
            s "Well, I guess the main character just got to me."
            "I think for a second. Why would a mentally challenged person be relatable to Sayori?"
            mc "What do you mean?"
            s "It just felt like there was someone out there who knew what its like."
            s 1bh "But it also ended up reminding me of it too."
            s "I already knew there were others out there with problems like mine, but seeing someone deal with them like that was like a reminder"
            "It finally clicks"
            mc "I- I understand."
            show sayori 1bu at t11 zorder 2
            "Sayori looks like she's about to cry again"
            "I move over and put my arm around her"

            show sayori 1bu at thide zorder 2
            hide sayori

            s "I'm just being stupid."
            s "I shouldn't be acting this torn up over some movie"
            mc "It's fine, we all have our problems. Besides, there were a few other people who were crying at the end of the movie, too."
            "Sayori looks at me, confused"
            mc "Well, probably not for the same reasons as you. The movie was pretty sad though."
            mc "In any case, dont worry about it."
            "We sit on the couch for a while and Sayori calms down."
            s "So, do you want to go to bed yet?"
            mc "That sounds great."            

            scene bg bedroom_night
            with wipeleft
            "We make our way to my bedroom and flop onto the bed."

        "Horror" :
            $SayoriVar -= 1
            "Hm...."
            "How about..."
            "No, no, that's lame."
            "Hm, this one could be interesting."
            "Does Sayori like horror, though?"
            "Has she even seen a horror movie?"
            "What's the worst that could happen?"
            "I can just show her something better if she doesn't like this one."

            mc "Well then, how about this one, Sayori?"


            show sayori jacn at t11 zorder 2
            s "A horror movie?"
            s jacl "I don't really like those, because they can be a bit too scary for me..."
            s jacx "But if you're with me, I think I can handle it!"

            scene black
            with wipeleft

            "We buy our tickets and head over to get some snacks."
            "I hear some rather heavy rainfall begin outside, cursing myself for not bringing an umbrella."

            mc "So what do you want to get? Classic popcorn, or something else?"

            s "Ooooh, they added mini cookies to the menu, can I get those?"

            mc "Sure thing."

            "I buy the cookies, popcorn, and drinks."

            $ y_name = "Clerk"
            y "Enjoy your movie."

            mc "You too."

            "Realizing my mistake, I blush and rush over to put extra butter on my popcorn while hoping the clerk didn't notice."

            $ y_name = "Yuri"

            scene bg theater_in
            with wipeleft

            "We enter the auditorium, find our seats, and get ready for the movie to start playing."
            "The movie itself isn't particularly good or scary."
            "It's about a group of teenagers who wander into the woods looking for a wizard but find that a demon haunts it and the demon kills all but one."
            "It's filmed in one of those {i}oh these are my phone recordings that some random dude picked up and played{/i} styles and has a lot of jumpscares."
            "The acting isn't even that good, either."
            "Half the times the 'demon' attacks one of the kids sounds like they're laughing."
            "And the demon looks like some guy in a black skinsuit crawling on all fours."
            "I feel Sayori cling to my arm and jump every time something mildly scary happens, so I guess it's somehow scary?"
            "I don't know, maybe I just don't get it."
            "Maybe I just don't have a high enough IQ to enjoy this movie"
            "I feel Sayori push really hard against my side when the movie comes to a close as the sole survivor of the group is implied to be killed."
            "Once the movie is over, we head out of the auditorium and into the foyer."
         
            scene bg theater_evening
            with wipeleft

            mc "So how'd you like the movie, Sayori?"


            show sayori jacg at t11 zorder 2
            s "The demon looked like it was going to kill me in the end, I was scared."

            mc "Really? The demon of all things?"
            mc "I thought that was the least scary part of the whole movie."

            show sayori jach at t11 zorder 2
            s "Yeah well it was to you!"
            s "You're braver than me!"

            mc "So?"
            mc "Still doesn't change that the movie looked like it had a budget of 4 dollars."
            mc "Maybe 5 for the skin suit the \"demon\" wore."


            s jacp "You meanie!"
            s jacj "Let's just go home, I'm scared now."

            mc "Alright, sorry."

            "I start to worry that I was being a little too harsh on Sayori earlier."


            scene bg residential_night
            with wipeleft

            "I'm about to walk Sayori back, so I give her my jacket to shield from the rain."
            "It's not much, but it seems to help."
            
            show sayori jach at t11 zorder 2
            s "Actually... can you sleep over at my house tonight?"
            s jacl "Y'know... I just want to make sure nothing happens to you."

            "I would ask if she was still scared, but it's a question that I'm already well aware of the answer to."

            mc "Sure thing, Sayori, I don't mind spending the night."
           
            show sayori jacl at thide zorder 2
            hide sayori

            "As we head over to her house, I notice that she keeps on looking around nervously."
            "Lightning flashes and I hear the crack of thunder about 4 seconds after."

            show sayori jacp at h11 zorder 2
            s "EH!?"

            mc "What?"

            "Sayori shouts out, startled. Upon her realization it was just thunder, she calms down a bit."

            s jacl "Oh... it's nothing." 
            s jacm "I'm not scared anymore, so there's no reason to be worried!"

            mc "Come on, Sayori..."

            "She looks away for a minute."


            s jack "Okay... so maybe I still am..."

            mc "Here."


            show sayori jack at thide zorder 2
            hide sayori

            "I put an arm around her and pull her close to me."

            mc "I'll protect you from any horrifying low budget monsters that try to attack us, alright?"
            s "T-thank you, [player]..."

            scene black
            with wipeleft

            "Shortly after, the walk concludes."
            "Sayori unlocks the door to her house and turns the light on."
            "Or, tries to anyway."
            "She flicks the light switch a few times before realizing that nothing's actually changing."
          
            s "Umm..."
            mc "Storm must have knocked the power out."

            "From what I can see of Sayori's face, she's definitely not comfortable regarding this information."
            "I cling onto her a bit tighter and get my phone out, using its screen as a flashlight."

            mc "Let's just go to bed. The power will be back up by tomorrow morning."
            s "O-okay..."

            "We walk up the stairs to her room together."
            "You really do start to notice every creak and noise that comes out of your movements."
            
            #Sleep at Sayori's house
            $flag = True
            scene bg sayori_bedroom_night
            with wipeleft

            "Once in her room, she gets comfy in her bed."

            mc "Better?"

            show sayori 1br at t11 zorder 2
            s "Much better!"


            mc "Well, I'm going to go sleep on the couch downstairs."
            mc "Yell if you need something."

            show sayori 1bm at h11 zorder 2
            s "Wait!"
            s "You don't really have to sleep downstairs, do you?"

            "I realize what she's proposing, and why."
            "I wouldn't really object, but her bed is kind of small..."
            "Ah, what's the worst that could happen?"


            mc "Alright, fine."
            mc "Here, scoot over."

            show sayori 1bm at thide zorder 2
            hide sayori


            "She shuffles over slightly, and it's really not enough room, so she turns over on her side."

            "I lay next to her, also on my side to conserve room and put an arm around her."


            mc "Goodnight, Sayori."

            s "Goodnight, [player]."

            scene black
            with wipeleft

            "We lay silent for a few minutes."
            "Random noises start going off and I can tell by Sayori's breathing that it's not helping her fall asleep."

            mc "Hey, listen..."
            mc "Turn around."

            "She shuffles a bit to be turned to me."
            "I kiss her forehead and pull her closer to my chest."

            mc "Nothing will happen to you, don't worry."
            mc "I'll take care of whatever there is."
            mc "I promise."

            s "Thanks..."

            "Sayori slurs her appreciation."
            "Within the next few seconds, she's fast asleep."
            "I finally settle down and get my rest as well."

    stop music fadeout 1.5
return

label sayoriroute32:
    if flag:
        scene bg sayori_bedroom_morning
    else:
        scene bg bedroom_morning
    with dissolve_scene_full

    "My eyes flutter open"

    mc "That might be the best sleep I've ever had"

    "I say that quietly, just in case Sayori is still sleep"
    "I suppose I didn't realise how tired I was last night"

    "I gently roll over to check"

    "Still sleeping soundly"
    mc "God, you're adorable"

    "I notice Sayori stirring"
    "Best not push my luck any more, time to quietly get up"

    scene black
    with wipeleft

    if flag :
        "I get out of bed, get dressed then leave a writen message to Sayori asking her to come home when she's up."
    else :
        "I get out of bed, have a quick shower and get dressed."

    scene kitchen
    with wipeleft

    mc "What should I make for breakfast..."

    mc "oh I know!"
    "I recently learned to make this really special type of pancake"
    "It's called Okonomiyaki"

    "They're more of a meal food rather than a quick breakfast"
    "But I'd like to treat Sayori to something special"
    mc "Let's get cooking!"

    "The recipe is easier than I remember, and before long I have a plate of Okonomiyaki pancakes"

    # Writers note: I wasn't sure as to whether or not this was a school day or a weekend, if it's a weekend then oof my bad as I am writing this as though it's a week day

    if flag :
        "Hmm, Sayori isn't here yet."
    else :
        "Hmm, Sayori isn't down yet."

    "I suppose she must have been equally tired, if not more."
    "She put in so much effort last night for our little date, I wouldn't be surprised if Sayori slept until midday"
    "But we need to get to school."

    if flag :
        "I lean to my phone and proceed to call Sayori."
        "After some calls, she finally picks up."
    else :
        scene bg bedroom_morning
        with wipeleft
        "I head upstairs and into my room, where Sayori appears to be slowly waking up."

    mc "Sayori..."
    mc "You gotta get up, we gotta eat breakfast and go"

    "Sayori grumbles something unintelligible."

    if not flag :
        show sayori pjq at t11 zorder 2

    s "Hmmf mff... nn breakfast mmf..."

    mc "Sayori?"

    "Suddenly, and without warning, Sayori springs to life!"

    if flag :
        s "BREAKFAST ! COMING !"
        "Sayori yawns"
    else :
        s pjm "I'm AWAKE!"
        s pjr "Breakfast!"
        "Sayori yawns"
        s pjl "Woah sorry..."
        s "You startled me a little."
        s "Hehe..."
        s pjk"I'm sleepy"

    mc "I think you spent all your energy on waking up."
    mc "Go take a shower, same as last time"
    mc "Be quick though, breakfast is waiting"

    if not flag :
        show sayori pjr at t11 zorder 2

    s "Okayyyy!"

    if flag :
        "And she hangs up just like that."
    else :
        "While she's preparing, I'm heading back to the kitchen"
        scene kitchen
        with wipeleft

    "I hope she doesn't take too long..."
    "I want the pancakes to be at least warm by the time we eat them."
    "..."
    "On second thought, this is about making Sayori happy..."
    "It'd be pretty sad if the only way to do that was to make some pancakes..."
    "..."
    "I'll make today great, as best I can!"

    if flag :
        "Before long Sayori knocks on my door, dressed and ready to eat."
    else :
        "Before long Sayori comes down from upstairs, dressed and ready to eat."

    show sayori 1x at t11 zorder 2

    s "What's for breakfast?"
    mc "I made something called Okonomiyaki,"
    mc "They're basically like-"
    s 1o "Oko- Okoya- Okoyakonoma?"
    s 1m "You made me a tongue twister for breakfast!"
    mc "Don't worry Sayori"
    mc "They're basically just healthy pancakes"
    mc "Besides, they're my treat!"
    s 1o "Huh?"
    s 1h "What did I do to deserve a treat?"
    mc "Well, you just put in so much effort during our date last night..."
    mc "I mean, we had such a great time."
    s 1x "Awww [player], you really didn't have to.."
    s 1r "But if it's food I can't say no!"


    # Writers note: Sorry about the okonomiyaki thing, this can be changed if you want, but I had it in my head because I recently learned how to make them. On a nother note, I'm assuming that this is a western society, because of the way the mod is so far and also the original game. 

    scene residential
    with wipeleft

    "After a quick breakfast we head out to school"
    "For once, I actually think we'll be on time"
    "And Sayori seems positively chipper today"

    show sayori 1r at t11 zorder 2
    s "That was so yummy, [player]!"
    s 1x "Can you make them again sometime?"
    mc "Sure..."
    mc "Only if you learn how to say it"
    s 1p "C'mon that's mean!"
    s 1o "Oka- Mako- yaki mangos..."
    "I chuckle softly"
    "Yaki Mangos"
    mc "You'll get there eventually sayori"

    show sayori 1q at t11 zorder 2
    "Sayori smiles"

    scene black
    with wipeleft

    "We arrive at school on time for once."
    "Sayori and I go our separate ways until the dreaded hour known as math."

    scene bg class_day
    with wipeleft_scene

    "Come time for math, my mind is already in a place of pure dread."
    "However, I think being stuck in that class with Sayori at least next to me will make things more tolerable."
    "I walk into the classroom and take my seat where I typically sit, expecting Sayori to sit by me in her usual spot."
    show sayori 1q at t22 zorder 2
    "A few moments later she walks in and smiles at me."
    "I smile back, but instead of her sitting by me, she drops a note on my desk, then takes a spot on the other end of the room."
    show sayori 1q at thide zorder 2
    hide sayori
    "Aw, what the hell!"
    "Finally I open the note and read what she wrote for me."

    python:
        s21_poem4 = Poem(
        author = "sayori",
        title = "{}".format(player),
        text = """
         I'm gonna sit somewhere else for math today. This is for your own good. I know you need to pay attention for the test coming up.
         
         XOXO.
        """
        )

    call showpoem(s21_poem4, music=False)


    "{i}Sayori, you..."
    "Sayori's either the most thoughtful person I know, or the most devious."

    scene bg corridor
    with wipeleft_scene

    "School is as boring as ever today."
    "Not only that but I had to study during morning break."
    "Luckily, it's lunch now."
    "I wonder where Sayori is..."
    
    show sayori 1r at t11 zorder 2
    s "[player]!"
    "I turn around and see sayori, lunch in hand, waving violently at me."
    "I wave gently in return and make my way over to where she is standing."

    s 1x "Hi [player]!"
    mc "Yo, Sayori"
    s "Wanna go for a walk before the bell rings?"

    show sayori 1a at t11 zorder 2

    "My brain already hurts from studying"
    "I have a feeling that walking will make that worse"
    "But I feel like I need to treat sayori today..."

    # Writer's note: Depending on what ya'll think, we could add a choice here: Going or asking to sit somewhere and rest. I don't fully mind.
    
    menu :
        "Go with Sayori":
            $SayoriVar += 1
            mc "Sure thing Sayori, where do you want to go?"

            s 1n "I'm not quite sure..."
            s 1r "Just somewhere around the campus would be fun!"
            s "Like an adventure!"
            s "Wandering wherever we want to go!"
            mc "Sounds great, Sayori!"

            show sayori 1r at thide zorder 2
            hide sayori

            scene black
            with wipeleft

            "Sayori and I grab each other's hands and begin wandering around the school."
            "For once Sayori seems really laid back."
            "It's odd how in normal conversation with Sayori, there was a degree of stress and tension in how she acted that I didn't notice until now."

            scene bg school courtyard
            with wipeleft

            "Sayori leads me to a bench under a lone tree in the middle of our school campus."
            "I've never really been here due to my unfortunate love of indoors..."
            
            play music t2
            "And free library Wi-Fi..."

            show sayori 1x at t11 zorder 2

            s "How has your day been so far [player]?"
            mc "Not too bad Sayori, how has your day been?"
           
            show sayori 1a at t11 zorder 2
            "This is a weirdly normal conversation for Sayori"

            s 1x "Actually not bad."
            "There's an eerie degree of surprise in Sayori's voice when she says that."
            s 1j "I mean, school's boring..."
            s 1x "But nothing bad has happened!"
            s 1r "And I actually understood math for once!"
            mc "Sayori, is there any reason you might be feeling so happy?"

            show sayori 1q at t11 zorder 2
            mc "I mean, not to be negative but..."

            show sayori 1a at t11 zorder 2
            mc "I rarely see you this... well, actually happy."
            s 1h "... but I'm always happy."
            mc "Correction: you're always positive!"
            mc "And that is really great!"
            mc "But there's a difference between happy and positive."
            show sayori 1o at t11 zorder 2
            "Sayori thinks for a moment..."
            "I hope I didn't say anything wrong..."
            s 1r "I guess you're right!"
            s 1x "And to answer your question, I suppose I'm happy for a few reasons..."
            s 5b "The main one is I'm so proud of myself for everything that happened the other day..."
            mc "As you should be, Sayori!"
            mc "You did awesome!"
            s 5a "It took a lot of preparation you know!"
            mc "I could tell, it was really something"
            mc "How did you manage all that?"
            s "Well..."
            s 5b "I had some help... hehe "
            "Before I have time to ask questions, the bell rings."
            "Sayori and I hug, and go to our separate classes."
        "Choose to rest":
            $SayoriVar -= 1
            "I hope this doesn't upset Sayori too much"
            "But personal health is important..."
            "Probably?"
            mc "Listen Sayori."
            s 1h "What's up?"
            mc "I really don't feel great right now so, an adventure isn't really the ideal thing for me right now."
            mc "I hope that's ok!"
            show sayori 1g at t11 zorder 2
            "Sayori looks at me blankly for a moment"
            show sayori 4r at h11 zorder 2
            s "I have an idea!"
            mc "Sayori-"
            s 4x "You wanna go to the library to relax right?"
            mc "I mean... yeah?"
            s "Follow me!"

            scene bg bookstore
            with wipeleft

            "Sayori leads me gently to the library and the up some stairs"


            scene black
            with wipeleft

            "I've never been up here"
            "I see teachers come up here all the time though..."
            "So I hope this isn't a restricted area..."
            "We come to a set of doors labeled 'Reading Room'"
            s "In here!"

            scene bg reading_room
            with wipeleft

            "We walk in a quiet room."
            "It's the same build as the library the books here are more academic"
            "It seems the only people up here are teachers and third-year students studying for college placement exams"
            mc "Wow"
            show sayori 1x at t11 zorder 2
            s "It's pretty soothing right?"
            s "Come this way!"
            show sayori 1x at thide zorder 2
            hide sayori
            "She leads me into the corner of the room"
            "The shelves here are packed with books that haven't been touched for years"
            "Except maybe by teachers"
            show sayori 1r at h11 zorder 2
            s "Right here!"
            s 1x "Sit, the carpet is nice!"
            "I'm in awe"
            "We're alone here with the best view of our town that I've ever seen"
            "..."
            s 5d "C'mon'"
            "Sayori pulls me down onto the floor"
            mc "Hey the carpet is pretty nice"
            show sayori 5d at thide zorder 2
            hide sayori
            "Sayori snuggles up to me"
            "I put my arm around her"
            #Would be nice to have a "Sayori x MC snuggling against a wall" here
            mc "How has your day been so far sayori?"
            s "Actually not bad."
            "There's an eerie degree of surprise in Sayori's voice when she says that."
            s "I mean, school's boring..."
            s "But nothing bad has happened!"
            s "And I actually understood math for once!"
            mc "Sayori, is there any reason you might be feeling so happy?"
            mc "I mean, not to be negative but..."
            mc "I rarely see you this... well, actually happy."
            s "... but I'm always happy."
            mc "Correction: you're always positive!"
            mc "And that is really great!"
            mc "But there's a difference between happy and positive,"
            "Sayori thinks for a moment..."
            "I hope I didn't say anything wrong..."
            s "I guess you're right!"
            s "And to answer your question, I suppose I'm happy for a few reasons..."
            s "The main one is I'm so proud of myself for everything that happened the other day..."
            mc "As you should be, Sayori!"
            mc "You did awesome!"
            s "It took a lot of preparation you know!"
            mc "I could tell, it was really something"
            mc "How did you manage all that?"
            s "Well..."
            s "I had some help... hehe "
            "Before I have time to ask questions, the bell rings."
            "Sayori and I hug, and go to our separate classes."
    
    scene bg corridor
    with wipeleft_scene

    "Ughh..."
    "School is finally over."
    "Time for the Literature club!" 

    scene bg club_day
    with wipeleft_scene


    "I show up at the clubroom a little early."
    "But it looks like Monika and Natsuki are here as well."
    "I swing open the doors and walk in cheerfully."
    "Monika is the first to greet me."

    show monika 1b at t11 zorder 2

    m "Hello, [player]!"
    m "You seem awfully chipper!"
    mc "Haha, thanks."
    "Natsuki turns to me like she's only just now noticed me."
    show monika 1a at t22 zorder 2
    show natsuki 1h at f21 zorder 2
    n "Oh hey, [player]."
    mc "Umm hey, Natsuki"
    "Sheesh..."
    "She seems a little agro today."
    "Best to steer clear I suppose"
    "Without warning Sayori and Yuri walk in simultaneously."
    show monika 1a at t44 zorder 2
    show natsuki 1g at t41 zorder 2
    show sayori 1r at f42 zorder 2
    show yuri 1e at t43 zorder 2
    s "Hey guys!!!"
    show sayori 1q at t42 zorder 2
    show yuri 1f at f43 zorder 2
    y "Good afternoon, everyone."
    show yuri 1e at t43 zorder 2

    "After everyone has greeted each other, we get on to doing our respective activities."
    show monika at thide zorder 2
    show natsuki at thide zorder 2
    show sayori at thide zorder 2
    show yuri at thide zorder 2
    hide monika
    hide natsuki
    hide sayori
    hide yuri

    "I was gonna talk to Sayori, but it seems like she's preoccupied talking to Yuri about perfumes..."
    "Not gonna lie, didn't see that coming."
    mc "God, I'm lucky to have her."
    "I whisper that quietly to myself."
    "I should write a poem about her."
    show monika 1g at t11 zorder 2
    m "You doing okay, [player]?"
    mc "Ah!"
    "I was so stuck daydreaming I didn't notice Monika sneaking up on me."
    mc "Yeah I'm fine thanks..."
    show monika 1j at t11 zorder 2
    "Monika chuckles."
    m 1k "Try blinking!"
    m 1b "Aha, I'm just kidding."
    m "But Sayori would probably be a little uncomfortable if she noticed you staring like that."
    mc "You make a good point."
    show monika 1a at t11 zorder 2
    "You know, maybe it's okay to talk to Monika about Sayori and I."
    "I mean she's Sayori's best friend."
    "And probably the most trustworthy person in the club."
    mc "Well you see it's just..."
    m 1c "Mhmm?"
    mc "Sayori and I went on a date last night and, well it was really good."
    mc "She had perfume, and nice clothes as well."
    mc "Like she really put in a lot of effort."
    mc "I suppose I'm just so proud of her, you know?"
    show monika 1j at t11 zorder 2
    "Monika laughs softly."
    m 1b "You know, [player]..."
    m "That is the most adorable thing I've ever heard."
    m 2k "Hehe~!"
    m 4b "I'll let you in on a little secret..."
    m "I've been giving Sayori tips on dating and fashion." 
    m "I've even lent her a few clothes to try out..."
    "That explains the 'help' Sayori referred to earlier."
    m 2d "She's not too good at returning stuff you know."
    mc "How so?"
    m "Well, I once let her borrow this really nice jacket from me."
    m "It was a varsity jacket of mine."
    m 2l "She's probably forgotten about it by now, hehe."
    m 2n "It really suited her, but I'm unsure as to whether she would actually wear it."
    mc "Huh..."
    show monika 1m at t11 zorder 2
    "A varsity Jacket... like the one she wore last night?"
    "Monika would be a slightly bigger size to Sayori due to the..."
    "Chest area..."
    "And the one from last night was slightly too big for her..."
    mc "Monika, I don't think that Sayori forgot about the jacket..."
    m 1d "What makes you say that?"
    mc "I think she wore it on our date last night." 
    "I send Monika a picture of Sayori from the night before"
    m 1p "Ahh..."
    m "That's the one"
    m 1n "This might be a little awkward but..."
    m "N-no I can't really ask for it back, can I...?"
    m "I mean I would love it back, but I don't think that would be fair."
    mc "I can ask for it back if you want, Monika."
    m 1r "I suppose it's up to you."
    m 1d "I won't stop you, but it was your idea."

    menu:
        "Don't confront Sayori":
            play music t6
            mc "...I know you probably want your jacket back, Monika."
            mc "But if it could at least wait until tomorrow,"
            mc "Sayori is legitimately happy today, and I don't want to wreck that by starting an argument."
            m 1q "..."
            m 1d "Y-yeah that seems fair..."
            show monika 1c at t11 zorder 2
            "Something about Monika's tone tips off to me that she's a little disappointed."
            m 3k "You enjoy the rest of the club today!"
            "Definitely not the right call if I wanted to satisfy Monika..."
            "But I'm glad she wasn't openly angry about it."

            scene bg club_sunset
            with wipeleft

            "The club went on without any more apprehensions."
            "And overall it was a pretty good day!"

            show sayori 1x at t11 zorder 2
            s "Ready to walk home [player]?"
            mc "Let's do it, Sayori!"
            mc "See you tomorrow, everyone!"
            s 1r "Bye-bye, guys!"

            show sayori 1r at thide zorder 2
            hide sayori

            "After the girls give us their respective farewells, Sayori and I wander back home, having our usual cheerfully silly conversations."

            scene black
            with wipeleft

            "When we reach the front of my house later than expected."

            scene bg residential_evening
            with wipeleft


            show sayori 1c at t11 zorder 2
            s "[player]?"
            mc "Yes, sayori?"
            s "If it's ok with you I think I'll stay at my own house tonight."
            s "I mean it's been a while since I've actually slept alone."
            mc "Sounds good, just let me know if you need anything be sure to let me know, ok?"
            s 1x "Yeah, ok. I'll see you tomorrow [player]!" 
            "And with that, I head back home to wrap up my day."

        "Confront Sayori" :
            $SayoriVar += 1
            play music t6
            $sayori_confronted = True
            mc "Yeah I hear you, I'll go talk to her as soon as I can."
            m "I'll come with you"
            show monika 1d at thide zorder 2
            hide monika 
            "Me and Monika walk over to where Sayori is sitting, humming to herself while reading."
            "In truth I'm pretty nervous about this."
            "But it's the right thing to do."
            mc "Hey, Sayori we gotta talk about something."
            show sayori 3c at f21 zorder 2
            show monika 1c at t22 zorder 1
            s "Is everything okay?"
            mc "Yeah, it's nothing too-"
            show sayori 3b at t21 zorder 1
            show monika 1i at f22 zorder 2
            stop music fadeout 2.0
            m 1i "No it's not really okay, Sayori."
            mc "Uhh, Monika?"
            show monika 2h at t22 zorder 1
            "She takes one quick glance at me"
            show sayori 1h at f21 zorder 2
            s "I haven't done anything wrong have I?"
            show sayori 1b at t21 zorder 1
            mc "No you just-"
            show monika 4i at f22 zorder 2
            m "You took something from me and I want it back!"
            show monika 2h at t22 zorder 1
            "Wow, Monika is getting pretty aggressive."
            "She's making it sound like Sayori robbed her."
            show sayori 4m at hf21 zorder 2
            s "What are you talking about?"
            s "I'd never take anything from you!"
            show sayori 4m at t21 zorder 1
            "Monika grabs my phone from my hand and opens it up to the photo I'd shown her a few moments ago."
            show monika 4i at f22 zorder 2
            m "What about this, Sayori?"
            show monika 4h at t22 zorder 1
            show sayori 3o at f21 zorder 2
            s "Huh?"
            s 3h "That's [player] and I on our date night!"
            show sayori 3g at t21 zorder 1
            show monika 4h at f22 zorder 2
            "Monika points to the jacket."
            m 4i "I believe that belongs to me."
            show monika 4h at t22 zorder 1
            "Sayori thinks for a second."
            show sayori 4n at hf21 zorder 2
            s "Oh!"
            s 3l "That's right..."
            show sayori 3l at t21 zorder 1
            show monika 4i at f22 zorder 2
            play music t10
            m "So? How come you haven't returned it yet?"
            show monika 4h at t22 zorder 1
            show sayori 3h at f21 zorder 2
            s "Well, I, uh-"
            "Sayori looks down dejectedly and mumbles."
            s 4k "I forgot."
            show sayori 4k at t21 zorder 1
            show monika 4i at f22 zorder 2
            m "That was a really expensive jacket, Sayori! I need to get it back soon."
            show sayori 4w at f21 zorder 2
            show monika 4h at t22 zorder 1
            s 4w "I promise I'll get it back to y-you."
            "Sayori looks like she's about to cry."
            mc "Hey, Monika. I think she got the message, you don't need to lay into her so much anymore."
            "Suddenly Natsuki walks over to see what the commotion is."

            show monika 2h at t33 zorder 1
            show sayori 4u at t32 zorder 1
            show natsuki 3c at f31 zorder 2

            n "What's going on?"
            show natsuki 3g at t31 zorder 1
            show monika 2i at f33 zorder 2
            m "Well, Sayori borrowed my really nice varsity jacket and wont give it back."
            show monika 2h at t33 zorder 1
            show sayori 3m at f32 zorder 2
            s "Hey! I'm not trying to keep it from you, I just keep forgetting to return it!"
            mc "Yeah, Sayori wouldn't steal anything from you."
            show monika 2i at f33 zorder 2
            show sayori 3f at t32 zorder 1
            m "Is there really a difference, if I don't get it back either way?"
            show monika 2h at t33 zorder 1
            show natsuki 3c at f31 zorder 2
            n "I dont think it's the same thing, it's not like she meant to steal it, she's just a forgetful person."
            "Yuri begins to walk over, seemingly bracing for impact."

            show monika 2i at f44 zorder 2
            show sayori 3f at t42 zorder 1
            show natsuki 3g at t41 zorder 1
            show yuri 1e at t43 zorder 1
        
            m "Exactly. It's my favorite jacket, and I don't want to have to get a new one.."

            show monika 2h at t44 zorder 1
            show yuri 1f at f43 zorder 2
            y "I think Monika has a point too, Intentionally or not Sayori isn't giving something of her's back."
            "Oh great, Yuri's siding with Monika."
            show yuri 1e at t43 zorder 1
            show natsuki 3c at f41 zorder 2
            n "Sayori will give it back at some point, how long has it even been since she borrowed it?"
            show yuri 1f at f43 zorder 2
            show natsuki 3g at t41 zorder 1
            y "It's not about how long it's been, it's about personal property. Monika let her borrow it for a night, not indefinitely."
            show yuri 1e at t43 zorder 1
            show natsuki 3c at f41 zorder 2
            n "She could at least show some decency and not start a fight over a jacket's imaginary late fees."
            show natsuki 3g at t41 zorder 1
            show monika 3i at f44 zorder 2
            m "Excuse me? I have been patient for {i}months{/i}."
            show sayori 4k at t42 zorder 1
            show monika 3h at t44 zorder 1
            "I cast a glance at Sayori, who buries her face further into her hands."
            "Both Yuri and Natsuki fall silent too."
            mc "Okay seriously, that's enough, Monika. It's definitely been too long, and I'll make sure the jacket gets back to you tomorrow."
            show monika 3i at f44 zorder 2
            m "I really hope that you're more responsible than Sayori, [player]."
            "I sigh and look at Sayori again, gesturing for her to say something to Monika."
            show monika 3h at t44 zorder 1
            show sayori 4v at f42 zorder 2
            s "I- It's fine. I'll bring you your jacket tomorrow, I promise."
            show sayori 4f at t42 zorder 1
            show monika 4i at f44 zorder 2
            m "You promise?"
            "There's a look of embarrassed defeat on Sayori's face."
            show monika 4h at t44 zorder 1
            show sayori 4v at f42 zorder 2
            s "Yeah."
            mc "Well it looks like that's finally settled."

            show monika at thide zorder 2
            show sayori at thide zorder 2
            show natsuki at thide zorder 2
            show yuri at thide zorder 2   
            hide monika
            hide natsuki
            hide sayori
            hide yuri



            "Me and Sayori head outside afterwards, as the meeting seems to have reached an unspoken early end."
            scene black
            with wipeleft
            "We walk back home in silence, avoiding discussing the fight."
            scene bg residential_evening 
            with wipeleft

            "As we make it back to our houses, I turn to Sayori"
            play music t10
            mc "Are you okay? I know Monika laid into you pretty hard back there."
            show sayori 1g at t11 zorder 2
            s "I-I'm fine. I guess I'm just a little shaken up. I don't know how I forgot it wasn't my jacket."
            mc "Don't worry about it. We'll give Monika back her jacket tomorrow and it'll all be fine."
            s 1k "Yeah, you're right. I should go, I- have a lot of homework to catch up on."
            mc "Alright. Call me if you want to come over and study at my house."
            show sayori at thide zorder 2
            hide sayori
            "Sayori's already halfway down the street and I hear a quiet \"okay\""
            "I sigh and open my door, heading inside."
            "Today has been rough, and I still have things to do. I can't worry about Sayori all the time."
            "For now, it's dinner and homework."

    stop music fadeout 1.5
return


label sayoriroute33:
    scene black
    with wipeleft
    "The rest of the week passes by without anything noteworthy happening. It is now Sunday."
    "Unlike most days, Natsuki actually texted me and Sayori."

    scene bg livingroom
    with wipeleft

    n "{i}Hey, can I hang out with you guys today?{/i}"
    "Sayori is overjoyed by the idea."

    show sayori 3br at t11 zorder 2

    s "My best friend and boyfriend are going to hang out together!"
    mc "Best friend?"
    s 3bx "Now that we're dating, Natsuki gets to be my best friend!"
    show sayori 3ba at t11 zorder 2
    "I mean, I can't really argue with that." 
    mc "Hey, haven't you known Natsuki longer than me?"
    s 1bx "No, I don't think so. I met her in fifth grade."
    show sayori 1ba at t11 zorder 2
    mc "Really?"
    show sayori 4bx at h11 zorder 2
    s "Yessir! We were both looking for coins under the vending machine!"
    show sayori 4ba at t11 zorder 2
    mc "Well, I guess- {i}what?{/i}"
    s 4br "Yep! I remember it like it just happened..."
    scene black
    with fade
    scene bg corridor_flashback
    with fade
    s "{i}Okay, so, [player] wants me to get him a cookie, and I'll get some apple juice...{/i}"
    "I open my mini purse and stick some coins into the vending machine."
    "One of the coins starts to slip, and it falls."
    "It bounces off my shoe and directly under the vending machine."
    s "Aww, man!"
    "I get down on the floor and start attempting to snatch it up."
    "However, I feel another hand or something grab for the coin as well."
    "I start to scream softly."
    "To my surprise, the other side also screams, and the hand quickly retracts."
    s "{i}Oh god, I don't have to look over there, do I?{/i}"
    "I slowly look over, awaiting the monster on the other side..."
    "Only to see some bright pink hair staring back at me."
    show natsuki 5g at t11 zorder 2
    s "Hello?"
    n 5c "H-hi..."
    show natsuki 5g at t11 zorder 2
    s "I'm Sayori! What's your name?"
    "I extend a hand to the girl."
    show natsuki 5b at t11 zorder 2
    "She at first flinches, but eventually reaches to shake it."
    n 2c "I'm Natsuki..."
    show natsuki 2g at t11 zorder 2
    s "What were you doing under there?"
    n 4e "I wasn't fishing for coins or something, if that's what you think..."
    show natsuki 4g at t11 zorder 2
    "I smile."
    "This girl's a really bad liar."
    n 4w "Um, well it was nice meeting you. Sorry for trying to take your money."
    show natsuki at thide
    hide natsuki
    s "{i}Dang, she left. I really wanted to talk to her more.{/i}"
    s "{i}Oh well, I’m sure I’ll see her around.{/i}"
    scene black
    with fade
    scene bg livingroom
    with fade
    show sayori 4br at t11 zorder 2
    s "And that's how we met. Even though she escaped my clutches that day, I still found her again another time!"
    mc "Wow. When was that other time?"
    s 2bx "Maybe I’ll tell you some other day."
    show sayori 2ba at t11 zorder 2
    "I swear, Sayori seems to remember the most trivial things at times."
    "Before I can give further comment, or ask how she met some of the others, a mass of pink shows up at our door."
    show sayori at thide
    hide sayori
    "Sayori goes to answer it."
    "The two say some things to each other I can't really make out."
    "They both walk over to me."
    show sayori 1bq at t21 zorder 2
    show natsuki 5bd at t22 zorder 2
    n "So, me and Sayori thought over it, and we want to play Never Have I Ever for the first game tonight."
    n "And the loser... has to wear whatever the other two wants him- or, wants them, to."
    show natsuki 5bz at t22 zorder 2
    "I roll my eyes."
    mc "Are we seriously doing this?"
    "I don't know why Sayori thought inviting Natsuki over one day was a good idea."
    "I mean, of all the games to play, 'Never Have I Ever'?"
    show natsuki 5ba at t22 zorder 2
    "It's like she's asking for all 3 of us to be embarrassed."
    s 1bx "Come on, it'll be fun."
    show sayori 2ba at t21 zorder 2
    n 5bd "Pfft, clearly he's just chicken. It's alright, you don't have to play if you're scared."
    show natsuki 5bz at t22 zorder 2
    "Oh, is {i}that{/i} how she wants to play it?"
    mc "Scared? Me?"
    mc "Keep dreaming. I'm in."    
    show sayori 4br at h21 zorder 2
    show natsuki 5bl at t22 zorder 2
    s "Yaaaaay!"
    show sayori at thide
    hide sayori
    show natsuki 5ba at t11 zorder 2
    "Sayori wraps her arms around me, happy."
    "I swear, it's the little things that make her happy."
    n 5bd "Everyone know the rules?"
    show natsuki 5ba at t11 zorder 2
    "Sayori and I nod."
    scene black
    with fade
    "With that, the three of us stand shoulder to shoulder at the end of the hallway."
    "Natsuki seems to have chosen an extra long playing field."
    scene bg livingroom
    with fade
    show sayori 1ba at t21 zorder 2
    show natsuki 2bd at t22 zorder 2
    n "Anyone wants to start?"
    show natsuki 2ba at t22 zorder 2
    "Seeing my easy advantage, I step forward."
    mc "Never have I ever stayed up until three AM to finish a video game."
    show natsuki 2bz at t22 zorder 2
    "Natsuki chuckles."
    n 2bl "How do you get any sleep, Sayori?"
    show natsuki 2ba at t22 zorder 2
    s 2bs "It's okay! I don't sleep very early normally, anyway..."
    show sayori 2bq at t21 zorder 2
    n 2bd "Whatever. I guess that means it's my turn."
    n "Never have I ever done a cartwheel!"
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at h22 zorder 2
    "Natsuki and Sayori both take a step forward."
    "I feel like she's toying with me."
    show natsuki 1ba at t22 zorder 2
    "Sayori goes next."
    s 1bx "Never have I ever..."
    s 1br "Stolen a cookie from Natsuki!"
    show sayori 1br at h21 zorder 2
    "She walks forward, proud of herself."
    n 4be "Hey! That's against the rules!"
    n 4bk "... isn't it?"
    show natsuki 4bg at t22 zorder 2
    mc "I don't know. Seems perfectly legal to me."
    "I smile."
    "It may put me behind Sayori, but seeing the slight anger on Natsuki's face is worth it."
    n 4bk "Alright, fine. [player], it's back to you."
    show natsuki 4bg at t22 zorder 2
    mc "Sweet."
    mc "Never have I ever..."
    show sayori 2bq at t21 zorder 2
    "I stop to think."
    "I don't want to pull the masturbation card just yet..."
    "Partly because I have a functional sense of shame, and partly because I don't want to learn something about these two that I didn't want to know."
    "I need something else specific to my gender, maybe..."
    mc "...used a urinal."
    "I take a step forward, smug."
    n 4bd "Oh yea, well, never have I ever been in a woman's restroom!"
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at t22 zorder 2
    "Natsuki and Sayori both step forward."
    mc "You realize that this still puts Sayori in the lead, right?"
    n 2bg "..."
    "I hear what I assume to be a low growl out of Natsuki."
    "I can tell I'm getting to her."
    n 2bc "Sayori, your turn."
    show natsuki 2bg at t22 zorder 2
    s 1bx "Never have I ever played a guitar!"
    show sayori 1br at h21 zorder 2
    "Sayori alone steps forward."
    mc "Sayori, I've never seen your guitar..."
    n 4bk "Neither have I..."
    s 3bl "Ehehe... I probably shoved it under my bed, or into a closet..."
    show sayori 3by at t21 zorder 2
    "I shrug it off and take my turn without prompting."
    mc "Never have I ever kept my hair dye-free."
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at h22 zorder 2
    "All three of us step forward."
    "Wait, all three of us?"
    show sayori 1ba at t21 zorder 2
    "Sayori and I both stare at Natsuki."
    n 1bb "What? It's completely natural, I swear!"
    "Well, that's a waste of a turn."
    show natsuki 1bg at t22 zorder 2
    "Natsuki realizes that this was a target attack and decides to fire back."
    n 1bd "Never have I ever read a Manga 3 times!"
    show natsuki 1bz at h22 zorder 2
    "Natsuki alone steps forward, putting me behind her and the now tied Sayori."
    show sayori 3bo at t21 zorder 2
    "Sayori, realizing this, tries to come up with something."
    "I pity her, as she was never really the competitive type."
    show natsuki 1ba at t22 zorder 2
    "Although, I guess that's a good thing."
    "Her attitude seems a lot more carefree than mine or Natsuki's."
    "I guess ignorance truly is bliss."
    s 3bx "Never have I ever failed PE class!"
    show sayori 1br at h21 zorder 2
    "She takes a step forward, a bit more proud than she needs to be."
    mc "You don't seem to lack athletic ability, Sayori."
    s 4bl "No, but it was my first period class."
    s "They don't let you in late..."
    show sayori 4by at t21 zorder 2
    "That makes a bit more sense."
    "Natsuki and I stay back, putting Sayori back in the lead. Then Natsuki, then myself."
    mc "Never have I ever swallowed a spider!"
    show sayori 1bp at t21 zorder 2
    show natsuki 1bp at t22 zorder 2
    "I strut to Natsuki's position, confident."
    s "Eek!"
    "Natsuki's face is one of pure disgust."
    mc "I lost a bet when I was nine. I guess it helped me out, in the end."
    n 1bf "Boys are so gross."
    show sayori 1bf at t21 zorder 2
    "Natsuki begins scheming."
    n 1bb "Never have I ever put on lipstick!"
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at h22 zorder 2
    "All three of us step forward."
    n 3bm "Wha- really?"
    "Natsuki looks at me."
    show sayori 1bn at t21 zorder 2
    show natsuki 3bg at t22 zorder 2
    mc "Different bet this time."
    mc "You never said where the lipstick was applied."
    mc "I had to draw a rather phallic shape on my forehead and leave it on for three hours."
    n "..."
    s 1br "Anyway!"
    s "Never have I ever been shoved in a locker!"
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at h22 zorder 2
    "Both Sayori and Natsuki step forward."
    n 1bd "Keep that up Sayori. Keep the eagle in its nest."
    show natsuki 1ba at t22 zorder 2
    "Wait, what?"
    "What kind of expression is that?"
    "It almost sounds like a code word..."
    show sayori 1ba at t21 zorder 2
    "Ah, I'm sure it's nothing."
    "What to do next...?"
    "Natsuki basically stole my wank card."
    "How about..."
    mc "Never have I ever been locked in a closet for an hour!"
    show sayori 1br at h21 zorder 2
    "Me and Sayori step forward."
    "Back on equal footing with Natsuki. Sayori now has a two-step lead."
    "Hopefully, that's not going to come back to bite us later."
    show sayori 1ba at t21 zorder 2
    "We're now almost through the hall."
    n 1bl "Never have I ever... gotten a cupcake thrown in my face!"
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at h22 zorder 2
    "Sayori and Natsuki both step forward."
    mc "... is there a story here?"
    s 1bx "Ooh, Ooh, can I tell it?"
    show natsuki 1bk at t22 zorder 2
    "Before either Natsuki and I can answer, Sayori starts up..."
    #POV change---
    scene black
    with fade
    scene bg sayori_bedroom_flashback
    with fade
    show natsuki 5bd at t11 zorder 2
    n "Well, here they are!"
    n "I wanted to thank you for being my friend by making you these, so... here."
    show natsuki 5ba at t11 zorder 2
    "{i}Aww, this is sweet!{/i}"
    "{i}Natsuki brought me some cupcakes for our sleepover today!{/i}"
    s "Thank you, Natsuki!"
    "I say, and grab one."
    "I take a bite. It's... really good, actually."
    s "I like it!"
    n 5bd "I knew I was a good baker!"
    show natsuki 5ba at t11 zorder 2
    s "It could be better, though..."
    n 5bc "Really?"
    "Natsuki takes a bite out of her own cupcake."
    n "How?"
    s "Simple."
    "I then take the cupcake and push it in her face."
    show natsuki 1bv at h11 zorder 2
    s "It doesn't have enough Natsuki in it!"
    n 1be "Hey!"
    show natsuki at thide
    hide natsuki
    "Natsuki laughs, and reacts by getting revenge using her own cupcake, and my face."
    scene black
    with fade
    "She then grabs another one from her tray and starts chasing me around with it."
    "I run, but all my laughing catches up to me and I eventually double over."
    "She takes it and puts it on top of my head like a hat."
    scene bg sayori_bedroom_flashback
    with fade
    s "Woah, Natsuki..."
    show natsuki 3bk at t11 zorder 2
    n "I didn't go too far, did I?"
    s "...this cupcake makes a really good hat!"
    show natsuki 1bz at t11 zorder 2
    "We both laugh."
    #PoV is back to normal---
    scene black
    with fade
    scene bg livingroom
    with fade
    show sayori 1bq at t21 zorder 2
    show natsuki 4bb at t22 zorder 2
    n "Hey, I never said that last line!"
    show natsuki 4bg at t22 zorder 2
    s 1br "You totally did!"
    show sayori 1bq at t21 zorder 2
    mc "I hate to cut the theatrics short, but it's your turn, Sayori."
    s 2bx "Oh yea!"
    s "Never have I ever gotten a cupcake shoved in my hair!"
    show sayori 1br at h21 zorder 2
    "Sayori takes a three step lead."
    n 4bb "Sayori, come on, eagle in the nest!"
    s 1bn "What? He's still behind."
    show natsuki 1bv at h22 zorder 2
    show sayori 1bw at t21 zorder 2
    n "DON'T SAY THAT OUT LOUD!"
    show natsuki 1bx at t22 zorder 2
    "...I feel like they're conspiring."
    show sayori 1bg at t21 zorder 2
    mc "What's going on?"
    n 1bw "Okay so..."
    n 1bq "We may or not have come up with a plan to put you in last..."
    n "Because we really wanted to see what you looked like in one of Sayori's dresses."
    show natsuki 1bs at t22 zorder 2
    "... seriously?"
    "That's the game plan?"
    mc "Well, now I have to win."
    n 1bp "Not if I have anything to say about it!"
    show natsuki 1bi at t22 zorder 2
    "Natsuki doesn't know the mistake she's made putting my dignity on the line."
    mc "Alright, let's play that game."
    mc "Never have I ever..."
    mc "Read a hentai doujin!"
    show sayori 1br at h21 zorder 2
    show natsuki 1bz at h22 zorder 2
    "All 3 of us step forward."
    "..."
    show sayori 1bn at t21 zorder 2
    show natsuki 1bh at t22 zorder 2
    mc "..."
    n 1bi "..."
    s 1bi "..."
    "A powerfully awkward silence fills the room."
    s 3bl "I was... curious one day, people talk about them in chat rooms all the time, so..."
    show sayori 1bd at t21 zorder 2
    mc "I do it... rarely, but sometimes..."
    "Natsuki refuses to explain herself as I and Sayori do. She instead shoots me a look."
    mc "Desperate times, Desperate measures." 
    n 4bw "Yea, yea."
    n 4bt "Never have I ever slept in a doghouse!"
    show natsuki 1bz at h22 zorder 2
    "Natsuki alone steps forward, beginning to close the gap between her and Sayori."
    show natsuki 1ba at t22 zorder 2
    s 4br "Never have I ever won a game of Never Have I Ever!"
    show sayori 1br at h21 zorder 2
    "Sayori takes a step forward and completes the game."
    "I don't have the heart to tell her that's probably against the rules."
    show sayori at thide
    hide sayori
    show natsuki 1ba at t11 zorder 2
    "At this point, I'm three steps away from the goal. Natsuki is two steps away."
    mc "Never have I ever taken items from the top shelf of a store!"
    "I step forward."
    n 2bb "Ah come on, that was low!"
    mc "You know a lot about low, don't you Natsuki?"
    n 2be "Oh yeah? Never have I ever looked for coins under a vending machine!"
    show natsuki 1bz at h11 zorder 2
    "Damn, that one had exposition to it, too."
    "Natsuki takes her step forward." 
    "I've got to make sure this next one is perfect..."
    mc "Never have I ever slept next to Sayori!"
    "I made sure my wording was perfect as not to imply anything lewd."
    show natsuki 4by at t11 zorder 2
    "Me and Natsuki are neck and neck..."
    show natsuki 1bz at h11 zorder 2
    "Until she takes a step forward."
    "I pause."
    n 1by "Be careful with your wording."
    n 2bl "I've slept next to Sayori too. We've had sleepovers before."
    n "Not in the same bed, but it still counts!"
    show natsuki 2ba at t11 zorder 2
    "... my own wording trick got me."
    "I stand there, one step from the goal, Natsuki and Sayori having already crossed it."
    show natsuki 2bz at t11 zorder 2
    "Natsuki puts on a face so smug it's blinding."
    n 4by "Well, Sayori, you know what that means!"
    n "Go pick out your favorite dress!"
    s "I'll be right back!"
    show natsuki at thide
    hide sayori
    scene black
    with fade
    "Great..."
    "Sayori comes back, dress in hand, and I excuse myself to the restroom to put it on."
    "As soon as I come out, a camera flash blinds my vision."
    scene bg livingroom
    with fade
    show sayori 4br at t21 zorder 2
    show natsuki 2bl at t22 zorder 2
    mc "Hey, no one said anything about pictures!"
    s "Come on, [player]! Can I just put some make up on you? You'd look so cute!"
    n "Stand still, you're making the camera blurry! Remember, you've gotta wear that the rest of the night!"
    "{b}{i}Good grief...{/i}{/b}"
    scene black
    with fade
    
    stop music fadeout 1.5

return
