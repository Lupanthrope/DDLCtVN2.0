label Natsuki2:
    $ karma = 0             #control for direction of the ending
    $ is_end = False        #control to insure player does not recieve multiple endings in one playthrough
    $ jerk = False          #1st control for scene 8
    $ tens_check = ""       #2nd control for scene 8 - Y or S
    $ date_choice = ""      #control for scene 7 - M, D or C
    $ end_dir = ""          #control for the direction of the ending - YN or SN
    $ y_name = "Yuri"
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ m_name = "Monika"

#Scene 1 - Tension(1):
    scene black
    play music t12
    "It's morning."
    "Pale, impossibly bright sunlight filters into my room between the blinds and directly onto my shut eyes. Even so, it manages to wake me up."
    mc "Ngh..."
    scene bg bedroom_dawn
    with dissolve_scene_full
    "I open my eyes, wincing as the light fills my vision. After the intial pain fades, I try to sit up, but fail."
    "Looking to my left, I find Natsuki lying beside me. Her arms wrapped around my midriff and my arm is underneath her."
    "I have long since lost any feeling in the limb, but I barely notice as I watch Natsuki."
    "Her eyes are closed and her mouth is slightly parted as she breathes slowly and evenly."
    "She looks so peaceful. And, well... {w=0.25} cute of course."
    "..."
    "And naked."
    "I don't mean to gawk at her like this. It's just... {w=0.5} she looks so innocent and pure that I can't bring myself to look away."
    "I love her so much."
    "Another minute passes and then, Natsuki begins to stir and mumbles something incoherently."
    show natsuki dbla2 at t11 zorder 2
    n "Mmm... [player]?"
    "I hesitate."
    mc "Good morning, Natsuki."
    n "How long have you been awake?"
    mc "A couple of minutes, actually."
    show natsuki dblai
    "She sits up and looks at me with a somewhat annoyed expression. Whether because of me or just being woken up isn't clear."
    n dblah "Were you watching me sleep?"
    show natsuki dblai
    mc "I, uh... {w=0.25} Y-yes? Sorta?"
    n dblah "That's creepy, [player]."
    "I start to defend myself, but before I can even get a word out, she cuts me off."
    n dblal "I'm teasing. God, you're easy."
    show natsuki dblaj
    "I frown. It's too early for jokes."
    "Or much of anything else really."
    n dblak "What time is it?"
    mc "5:35 a.m."
    mc "Don't worry, we've got some time before school."
    n dblad "So breakfast then?"
    show natsuki dblaa
    mc "Sounds good to me. I'm not sure what I have, though."
    show natsuki dblaz
    "Natsuki grins at me as if I had just challenged her ability to make something delicious from scraps."
    n dblal "Trust me, you'll love whatever I whip up."
    n dblae "You'd better, anyways, or I won't make breakfast for you ever again."
    show natsuki dblag
    mc "Fair enough. But we should probably get dressed first, right?"
    n dblab "Well, duh."

    scene bg kitchen
    with wiperight
    stop music fadeout 5.0

    "Turns out I had more than I thought. Bread, eggs, cinnamon, butter, flour, and a few other things."
    "Natsuki really outdid herself."
    "I tried to help, of course. But since I'm not really much of a cook, all I really did was end up making a mess. Oh well, at least one of us will clean it up later"
    "Right now, I've got a massive plate with two huge slices of french toast, scrambled eggs, and hash browns on it. And right next to the plate, I have a large glass of fresh orange juice."
    "Natsuki has a nearly identical plate as well, on the other side of the table."
    "I don't think I've eaten this well since... well, ever really."

    play music t6

    show natsuki 4y at t11 zorder 2
    n 4y "Don't just stare at it. Eat it, dork."
    show natsuki 2j
    "Natsuki's words snap me back to the present and I meet her eyes. She hasn't eaten any of hers yet either."
    mc "Ah, sorry. It's just a lot more than what I was expecting, to be honest."
    show natsuki 2k
    mc "It smells and looks really good, though."
    show natsuki 1j 
    "Natsuki seems pleased by the praise."
    show natsuki at thide
    hide natsuki
    "I pick up the fork and cut off a small piece of toast. It's covered in maple syrup and oozing off the fork."
    "I shove the square in my mouth and chew."
    "..."
    "....."
    show natsuki 1n at t11
    "Natsuki is watching me closely as I chew, presumably looking for some sort of reaction, positive or negative."
    "I swallow and take a sip of orange juice."
    n 1m "Well?"
    mc "Well, what?"
    n 1n "Do you like it?"
    "I look down at my glass as if thinking hard about the question."
    mc "It's alright, {w=0.25} I guess."
    show natsuki 4o
    "Natsuki looks like she's going to punch me."
    "I grin."
    show natsuki 4c
    mc "I'm joking, Natsuki. I love it {i}almost{/i} as much as I love you. You're a really good cook."
    show natsuki 4s
    "Natsuki blushes and looks down at her plate."
    n 3t "I-idiot. I'm glad you like it so much."
    show natsuki at thide
    hide natsuki
    "Relative silence filled the room as we finish eating our meals. We decide not to talk about last night, which was probably for the best. It would just end up being awkward."
    "After we've eaten our fill and put the dishes in the sink to be washed later, Natsuki and I split up to finish our separate tasks before school."
    scene bg residential_day
    with wipeleft_scene
    "A few minute later, Natsuki and I are standing on the street corner outside my house, waiting for Sayori."
    "There's a slight nip in the air, so Natsuki is shaking beside me obviously not pleased with the weather."
    show natsuki 1b at t11 zorder 2
    n 4b "Why are we waiting for her exactly?"
    show natsuki 1f
    "Her tone was rather sharp, but her temper probably came from being forced to stand around in the cold rather than directed at Sayori herself."
    mc "Sayori and I always walk to school together."
    show natsuki 4g
    "Natsuki stares at me. I wilt under her gaze."
    mc "Well, usually, anyway. When she wakes up on time."
    mc "Besides, she still has a few minutes."
    n 4i "..."
    n 4h "You really do care about her, don't you?"
    "I pause. It was a simple question with a simple answer. But for some reason, I feel like this is some sort of test."
    "Of what, however, I have no clue."
    mc "Of course, I do. I mean, we've been friends since kindergarten at least."
    show natsuki 4s
    mc "Sure, she has her flaws. We all do. But she really turns any bad or boring day bright and cheerful just by being there."
    show natsuki 4u
    "Natsuki looks down at her feet, thinking about my words."
    show natsuki 2a
    "Finally she looks up and nods."
    n 2a "I see what you mean. She really has been the heart of the club, in her own way, even more so than Monika."
    "Silence once again fills the air while we wait, but it only lasts for a second."
    n 1k "What do you think my flaws are?"
    mc "I'm sorry?"
    show natsuki 1m
    n 4k "You said \'we all have flaws.\' What are mine?"
    "I hesitate. It seems I've accidentally set myself up for this."
    menu:
        "Should I be honest, or should I assure her that it doesn't matter?"
        
        "Be honest":
            #Scene 1a
            $ karma += 1
            n "Honesty is always the best policy, I think."
            mc "Well... um..."
            "Natsuki looks at me expectantly. I can see she's scared of what I might say."
            "I clear my throat and then speak."
            show natsuki 1n
            mc "Natsuki, you know I would only say this because I love and respect you."
            "{i}Not to mention the fact that you asked me for it{/i}."
            mc "But I guess you can come off as sort of...{w=0.5} abrasive at times."
            n 4m "Abrasive?"
            show natsuki 4n
            "She doesn't sound angry or particularly upset about it. Just a little... put down."
            "I feel a little bad, but she seems to want to know what I mean by that."
            mc "Just in how you deal with new people and experiences. I know you and I didn't exactly get along at first."
            n 4o "W-well! That was because...{w=0.25} b-because I..."
            show natsuki 42b
            "She breaks off and turns her gaze towards nothing in particular."
            show natsuki 42b
            "I step closer and put my hands on her shoulders in what I hope in a comforting way."
            mc "It's alright, I'm not saying that it's necessarily a bad thing."
            mc "Some people might disagree, but I never will."
            show natsuki 42a
            "Her eyes dart back to me warily."
            mc "Honestly, I like that side of you. It's what attracted me to you in the first place."
            n 42c "Not because you just thought I was cute?"
            "I smile and shake my head."
            mc "Okay, maybe I did think you were kind of cute, but that isn't the point."
            show natsuki 42a
            mc "I admire your tenacity and honesty."
            mc "You've never been afraid to say what you think or how you feel about those closest to you."
            show natsuki 4h
            mc "I wanted to be one of those people. One of the few you let your guard down around, even if I had to wade through waves of insults to get there."
            show natsuki 4m
            mc "What I'm trying to say is, I knew there had to be a good person behind that wall of solitude, and I proved that there is."
            show natsuki 4i
            mc "But it wouldn't hurt to let that side of you show more often."
            "I hold Natsuki at arm's length for a few moments as she considers my words."
            n 4b "No offense."
            n "But that sounds like a load of crap."
            show natsuki 1g
            "I suppress the urge to sigh and let my arms drop to my sides."
            "That was pointless."
        
        "Avoid the topic":
            #Scene 1b
            $ karma -= 1
            mc "Natsuki..."
            show natsuki 1c
            "She looks at me, clearly attentive to what I'm about to say."
            show natsuki 1a
            "I slide closer and put my arms around her petite frame. She blushes slightly but doesn't react otherwise."
            show natsuki 1c
            mc "It doesn't matter what I think or what anybody else thinks."
            mc "You know you best and I love everything about you. I wouldn't change a single thing if I could."
            show natsuki 1a
            "A small grin breaks across her face as she looks up at me."
            n 1l "You wouldn't even wish I was taller?"
            "Now it's my turn to smile."
            mc "Nope."
            n 1d "Why?"
            mc "Because you look cuter when you're tiny."
            show natsuki 1e
            "Instantaneously, she breaks away from me and whips around to deliver a swift punch to my shoulder."
            "There wasn't enough force behind it to leave a mark and it's obvious she meant it as a joke."
            show natsuki 1v at d11
            n "I'm {i}not{/i} cute!"
            show natsuki 1y
            "I grin more as I rub the sore spot on my shoulder."
            mc "I'm teasing, of course."
            mc "{w=0.25}But you are totally cute."
            show natsuki 4y
            "She huffs in mock annoyance and the subject is dropped altogether."

    "A few minutes pass and I glace at my watch. It's two minutes past the time we were supposed to leave already. Natsuki must be aware of the time too."
    n 1b "Look, [player], I don't think Sayori's coming any time soon."
    n 1d "So let's go before {i}we're{/i} late."
    "I want to argue, and know that I probably should, but I can't think of any good reason to wait longer, so I just nod and agree."
    show natsuki at thide
    hide natsuki
    "She turns away and starts walking down the street, so I jog to catch up to her." 
    "After a few moments, Natsuki remembers that she doesn't know her way around this part of town very well yet, so
    she lets me take the lead the rest of the way."
    "I tell her that she'll learn the route pretty quickly since there are very few turns and it's mostly straight for half a mile after that."

    stop music fadeout 4.0

    scene bg school
    with wipeleft_scene
    "We arrive a few minutes before the bell rings, indicating the start of a new school day."
    "On the one hand, I dread the upcoming classes."
    "But on the other hand, at least there's the literature club after school."
    "I let the thought sink in. I actually look forward to the club meetings these days."
    "It's only been a few weeks, but I've noticed a massive turnaround in my view on the club."
    "I make a mental note to thank Natsuki for those cupcakes on my first day. I probably wouldn't have met her otherwise."
    "The thought saddens me, but also seems utterly foreign at the same time."
    "I can't imagine life without her now."
    "Is that what happens when you meet someone special?"
    show natsuki 4e at t11 zorder 2
    n "Hey, [player], are you spacing out again?"
    mc "Sort of. But it's not important. What's up?"
    show natsuki 4f
    "I can tell Natsuki is a little annoyed."
    n "I said \'I'm gonna go to class.\'"
    show natsuki 4h
    mc "Okay, but before you go-"
    show natsuki 4i
    "I beckon her, and she steps closer with an impatient expression."
    show natsuki 4b

    play music t5_natsuki

    "I kiss her without warning."
    "I can sense her tensing for a moment before she relaxes and reciprocates the gesture."
    "It's not very long, nor is it particularly intense, but the passion and warmth is there."
    show natsuki 4d
    "It's only a moment later when Natsuki pulls herself away and I immediately find myself longing for the sensation once again."
    show natsuki at thide
    hide natsuki
    "Out of the corner of my eye and off in the distance, I notice a gaggle of classmates standing around and staring at us."
    "They're entirely female and, as I recall, among the more popular students."
    "But not the type of popular that Monika is."
    "I seem to remember Monika even mentioning them specifically. \"They're the sort of people I can't stand,\" she said, or something to that effect."
    "I decide not to mention anything to Natsuki to prevent ruining the moment."
    "If they want to judge and make snarky comments, that's their choice. It has nothing to do with me or Natsuki."
    show natsuki 1h at t11 zorder 2
    "Natsuki, on the other hand, is blushing furiously and struggling to keep any sense of indifference on her face."
    mc "You're cute when you're flustured."
    n 1r "S-shut up! I'm leaving now."
    show natsuki at thide
    hide natsuki
    "With that, she turns away and walks briskly into the school building and I'm left with a horde of faceless students on all sides."

    stop music fadeout 1.0

    scene bg class_day
    with wipeleft_scene
    "Classes are over for the day."
    "Sayori wasn't in class today."
    "As worried as I am about it, I manage to push the thought into the back of my mind."
    "I instead focus on my..."
    "{i}My girlfriend{/i}."
    "It's still kind of strange to think of her like that."
    scene bg corridor
    with wipeleft
    "We talked in science class. Not about anything in particular. Just talked."
    "And later, during lunch, we ate together."
    "Even after all that, I still find myself craving her company. It's like when she's gone, I'm missing a part of myself."
    "It feels lonely."
    "That's another thing."
    "I wonder if I really had been lonely before and now I'm just starting to notice it."
    "There is a saying, \"Ignorance is bliss.\""
    "It's hard to say where I stand on that."
    "Was I happy before?"
    "I know I'm not unhappy now."
    "And I wasn't unhappy back then."
    "But I do fully recognize that I wasn't living the most... {w=0.25}exciting of lives."
    "The Literature Club, Natsuki, and all the girls around me have pulled me out of my comfort zone."
    "But how long could I have gone without knowing Natsuki or Yuri or Monika before I would've felt something different?"
    "Would I ever stop being unhappy?"
    "I shake the heavy thoughts from my head as I reach the clubroom door."
    "I wonder if I should wait for Natsuki before I go inside. I don't really want to bring a lot of attention to ourselves."
    "However, the decision is made for me when Natsuki approaches me from my right."

    play music t5

    show natsuki 4d at r11 zorder 2
    n "Hey~!"
    mc "Hey! How was your day?"
    n 1s "It was fine. I was thinking about you a lot, though. I wish we had more classes together."
    mc "Yeah, same here."
    mc "But we live together, so I guess we can't complain too much."
    mc "Maybe the distance at school isn't the worst thing in the world."
    show natsuki 1b
    mc "I wouldn't want to get sick of you so easily. Ehehe..."
    show natsuki 1v at d11
    "Natsuki slugs me in the arm."
    n 5n "Dummy."
    mc "So... this is our first club meeting since we became {i}official{/i} official."
    mc "Do you think the girls will notice something is different?"
    n 4j "Nothing's different, [player]."
    mc "Well... we did... do... {w=0.5}{i}that{/i}."
    show natsuki 1z
    "Natsuki snickers."
    n 3d "Do you think the other girls are like sharks when it comes to pheromones or something?"
    mc "Ehehe... I guess I'm just nervous about how I'll come off."
    n 1a "Don't be. We'll be fine."
    "Natsuki takes my hand, asserting that she wants the other girls to notice us."
    "I don't complain, and I open the clubroom door, walking inside with Natsuki."
    show natsuki at thide
    scene bg club_day
    with wipeleft_scene
    show yuri 1e at t11 zorder 2
    "We quickly notice Yuri sitting there, expectedly."
    show yuri 1k
    "What we don't expect, however, is the look she throws our way as we walk in and head for the closet."
    show yuri at thide
    hide yuri
    show natsuki 1a at t11 zorder 2
    mc "D-did you notice Yuri looked at us kinda dirty there?"
    n 2t "N-no, I didn't see that."
    "Someone's bad at lying."
    scene bg closet
    with wipeleft_scene
    show natsuki 1s at t11 zorder 2
    "Natsuki grabs a random manga carelessly, which is odd considering she's usually very careful about how her volumes are handled."
    "She nearly killed me over it when we first met."
    "She seems a little absent-minded."
    "As we sit down and open the book to read it, someone else walks into the room."
    show natsuki at thide
    hide natsuki
    scene bg club_day
    with wipeleft_scene
    show sayori 4r at t11 zorder 2
    s "Hi, everybody!"
    show sayori 4a at t21 zorder 2
    show yuri 1e at f22 zorder 2
    y "Hello, Sayori."
    show sayori 4b
    y 2h "Do you mind if we speak, privately? There's something I'd like to discuss with you."
    show yuri at t22
    "That sounds a little sketchy."
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    "I shrug it off and start to read some more, then try to get Natsuki's attention so she can turn the page, but when I look at her she's not even paying attention to the book."
    show natsuki 2u at t11 zorder 2
    mc "Natsuki?"
    n 2k "H-huh?!"
    mc "Are you okay?"
    n 2t "Y-yeah, I'm just fine."
    n 2l "Let's keep reading! I really like this volume."
    mc "... Uhm yeah. Me too."
    show natsuki at thide
    hide natsuki
    show monika 2l at t31 zorder 2
    show sayori 3l at t32 zorder 2
    show yuri 1g at t33 zorder 2
    "A moment later, Monika, tardy as always to her own club, enters the room, and is quickly beckoned by Yuri to join in on her and Sayori's conversation."
    "This congregation on the other side of the room is making me anxious. It's very suspicious that Yuri wanted to talk to everyone in the club except Natsuki and me."
    "I stand up to address this situation."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show natsuki 1o at t11 zorder 2

    stop music fadeout 1

    n "[player], wait, don't--!"
    show natsuki at thide
    hide natsuki
    mc "Hey, uh, is there something going on here you'd rather we not be in the know about?"
    show monika 1o at t11 zorder 2
    m "..."
    show monika 1o at t21 zorder 2
    show yuri 3g at t22 zorder 2
    show yuri at f22
    y "..."
    show yuri at t22
    show monika 1o at t31 zorder 2
    show yuri 3g at t33 zorder 2
    show sayori 1k at t32 zorder 2
    show sayori at f32
    s "..."
    s 3l "Hey, [player]!"
    show sayori at t32
    "At least Sayori's cheeriness is still all-present."
    mc "Hi, Sayori. Do you care to fill me in on what's going on here?"
    show yuri 1w
    show sayori 1k
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show monika at f11
    m 3p "Uh, [player], let's talk outside for a minute, just one on one."
    show monika at thide
    hide monika
    "I look at Yuri, who's still yet to say a word to me, then look at Sayori, who's looking back and forth between myself, Natsuki sitting on the other end of the room."
    "As I walk out the door with Monika, I notice Sayori sit down and start rubbing an eraser up and down the desk."
    scene bg corridor
    with wipeleft_scene
    "Monika and I leave the room and close the door behind us, and she starts to speak up."
    show monika 1r at t11 zorder 2
    m "Listen, [player], I want to preface this by saying, I'm not taking anyone's side here."
    m 2g "If i'm being honest, I think Yuri is being a little bit too... reactive?"
    m 4d "But she's concered."
    show monika 4c
    mc "About...{w=0.25} what?"
    show monika 4r
    "Monika sighs."
    m 2r "She's concerned about how you're influencing Natsuki."
    show monika 2q
    mc "Excuse me?"
    mc "I'm gonna give that purple-haired shit a piece of my mi--{nw}"
    m 2g "Hey, hey, relax."
    show monika 2h
    "Monika grabs me by the arm to pull me back to my previous spot and calm me down."

    play music t8

    m 2d "Look, she's being very vague. But essentially, she's worried about the impact you and Natsuki's relationship will have on club affairs."
    m "I don't want you to think I'm trying to get between you and Natsuki, but I think it'd be best to take things a little more subtly while the club is in session."
    show monika 2c
    mc "Really? You're trying to supress our relationship just because Yuri is kind of uncomfortable?"
    m 1r "Its...{w=0.5} not just Yuri."
    show monika 2q
    mc "What are you...{w=0.25} oh..."
    "I think about the way Sayori looked a minute ago. I wonder if she's being affected by this too."
    m 1g "Look, I want you and Natsuki to be happy. But this club is important to me, and I don't want it to fall apart at the seams."
    show monika 1e
    mc "It sounds like you don't trust us."
    m 2i "I'd appreciate it if you didn't put words in my mouth, [player]."
    show monika 2h
    mc "S-sorry..."
    "Something about that shift of tone is her voice was very alarming and intimidating."
    m 4b "As club president..."
    m 4n "A-and as your friend..."
    m 2p "I just want what's best for everyone in the club."
    m 2d "And like I said... I'm not taking sides here. I'm looking at things objectively, not emotionally."
    show monika 2e
    "I absord what Monika says, and as long as she's speaking purely objectively, I guess I can't argue with her."
    "I'll do whatever she thinks is right, so that the club can stay intact."
    show monika at thide
    hide monika
    scene bg club_day
    with wipeleft_scene
    "Monika and I return to the room and catch sight of Yuri and Sayori now minding their own business, while Natsuki waits impatiently for my return."
    "I give Monika a nod of understanding, then walk over to Natsuki."
    show natsuki 4n at t11
    "I feel like Natsuki should know about what Monika and I just talked about, but I know how she can be and I don't want her to snap in the middle of the club meeting."
    "I want to heed Monika's advice, so maybe it'd be best to spend the time with someone else during the club meeting today."
    mc "Hey, Natsuki, listen..."
    mc "You and I spend a lot of time together, right?"
    n 2t "Pfft, yeah, duh."
    show natsuki 2s
    mc "Well, club is the one time we have where we can do something a little different."
    mc "Why don't we take advantage of that and each spend some time with someone else?"
    n 2m "Y-you don't want to read with me?"
    mc "No! That's not it!"
    show natsuki 2n
    mc "I'd love to read with you, but I think we should expand our horizons a little bit, you know?"
    mc "I don’t want us to forget that we have more people in our lives than just each other."
    show natsuki 2s
    mc "Everyone here really cares about each other so let's let them know we care about them."
    show natsuki 2t
    "Natsuki forces a smile at first, but soon it looks genuine."
    n 3l "Sure, I'd like to do that."
    n 4z "I wouldn't wanna get sick of you so easily. Ahaha~!"
    mc "Heh, you little jerk."
    "Natsuki smiles at me."
    n 3d "S-so who are you going to spend time with?"
    show natsuki 3a
    mc "Hmmm..."

    menu:
        "Who {i}am{/i} I going to spend time with?"

        #scene 1c
        "Sayori":
            mc "I can spend time with Sayori today, I'm sure she misses me."
            n 3m "O-okay, I'll go hang out with Yuri then."
            show natsuki 1n
            "She seems hesitant, but before I can speak up and see if she wants to switch places, she stands up and walks toward Yuri."
            show natsuki at thide
            hide natsuki
            "Well, guess there's nothing left to do except kick it in with Sayori."
            "I stand up and walk over to the desk next to Sayori, then take a seat."
            show sayori 1k at t11 zorder 2
            mc "Hey, Sayori!"
            s 1r "Oh, hi [player]!"
            s 2a "How are you doing?"
            mc "Pretty good, how about you?"
            s 2k "I'm...{w=0.25}" 
            s 4l "... Good! R-really good!"
            mc "Glad to hear that."
            s 3c "What are you doing here? Aren't you supposed to be reading with Natsuki?"
            show sayori 3b
            mc "Nah, we decided to do something else. So i'm gonna spend my club time with you."
            s 4d "Aw, that's so sweet, [player]!"
            s 1y "I've missed you, to be honest."
            "Called it."
            mc "So have I."
            show sayori 1s
            "I smile at Sayori and she beams back at me."
            mc "So, what do you wanna do?"
            s 1a "Well, recently I've started getting into musicals."
            mc "Really? That's super cool."
            "The only musical I've ever seen Sayori watch before this point has been one we watched as kids together."
            "But it was a movie, not a live show."
            s 4q "Uh huh!"
            s 4a "And I think that musicals are a super cool form of literature!"
            mc "That's really cool, Sayori. So what do you wanna do today to celebrate that?"
            s 2x "I was gonna try looking for a script to a musical I like and read lines."
            s "I think acting would be fun! Do you wanna help me?"
            show sayori 2a
            mc "You want me to read lines with you?"
            s 4r "Yeah!"
            show sayori 4q
            "I've never acted before in my life, but this could be fun."
            mc "Sure thing! So what musical is it? Something silly like the one we watched as kids?"
            s 1l "N-no, actually, it's a little bit of a heavy one."
            mc "Oh?"
            s 1d "It's about a guy with social anxiety who tried to make the family of his recently departed classmate believe he was his best friend."
            s 3k "And he has to carry a lie for months on end to this family because he doesn't want to break their hearts, and also because he finally found people who accept him for who he is, which 
            he's wanted for his whole life."
            "..."
            "Holy crap."
            show sayori 1g
            mc "Sayori, that {i}is{/i} really heavy."
            mc "I wouldn't think you'd be into something like that."
            s 1a "Me either, but it was so awesome when I first watched it."
            s 2q "So, let me find the script and we can run lines together!"
            mc "Sounds great to me! This should be fun."
            show sayori 1a
            "Sayori finds a portion of this show's script to read lines from, and she and I assign roles."
            "I quickly realize that Sayori is actually a very good actress, at least compared to the driftwood-esque performance I'm giving."
            mc "Sayori, have you ever thought about trying out for school plays? I think you'd be really good at it!"
            s 5b "Y-you think so?"
            s 5a "I wouldn't wanna embarrass myelf, but if you really think I'm good at it then maybe I'll give it a shot."
            mc "I think you'll do awesome."
            s 2d "Thanks for the support, [player]. You're so great."
            mc "You're welcome, Sayori."
            show sayori at thide
            hide sayori
            "Soon after, the club meeting ends, and Monika dismisses the four of us."
            scene bg corridor
            with wipeleft_scene
            show natsuki 2j at t11 zorder 2
            "I meet Natsuki outside of the clubroom, then take her hand and swing our arms back and forth as we walk and talk."
            n 2i "So, how'd it go with Sayori?"
            show natsuki 2j
            mc "It was great! I learned Sayori's actually a very good actress."
            n 2l "Really? That's so cool."
            n 2q "I could never get on stage in front of people, I'd be so nervous."
            show natsuki 2s
            mc "Sayori said the same thing, but I'm encouraging her to put herself out there and audition for the school play."
            n 1j "You're really supportive. I'm glad to have someone like you behind me."
            mc "I'll always be happy to support you, Natsuki."
            mc "How'd it go with Yuri, by the way?"
            n 1t "Uh... it was okay, I guess. We had some tea together."
            n 3s "But... somehow she knew we were living together, which threw me off. Did you say anything?"
            mc "No, I didn't, but that's really strange."
            n 2q "She was also really quiet."
            mc "Yuri's always quiet."
            n 1u "Yeah but... I dunno, I might be overthinking. I hope I didn't do anything to offend her."
            mc "I'm sure you didn't, Natsuki."
            "... Is what I'm telling myself and her so I don't make her nervous..."
            show natsuki at thide
            hide natsuki

        #scene 1d
        "Yuri":
            mc "I can talk to Yuri, I think that'd be best for both of us."
            n 3z "Okay, cool, so then I can go hang out with Sayori!"
            show natsuki at thide
            hide natsuki
            "Natsuki excitedly stands up and trots over to Sayori, and they sit together, chatting like old pals."
            "I actually wonder how close the two of them really are. I might have to ask about that at some point."
            "I figure I've wasted enough time, so I stand up and walk toward Yuri."
            show yuri 1g at t11 zorder 2
            "I clear my throat to grab her attention."
            mc "Good afternoon, Yuri."
            y 1h "... Good afternoon, [player]."
            mc "So... whatcha doin'?"
            y 1k "I'm reading, evidently."
            "She sure is. She has her book out in front of her and everything."
            show yuri 1g
            "Looks like reading to me."
            "Wait, why am I having this inner monologue?"
            mc "Uh, well, would you like to read with me? I'd like to hear more about the book you're enjoying."
            y 2k "To be honest I'm not enjoying it very much. It seems a little...{w=0.5} I don't know, unwelcomed, in a few places?"
            mc "Yeah, I hate stuff that feels unwelcomed."
            show yuri 1e
            "Yuri gives me a blank gaze."
            mc "..."
            mc "Am I bothering you?"
            y 1q "Uh..."
            y "I wouldn't necessarily say you're bothering me, but..."
            y 3u "I was hoping for some alone time."
            y 3w "B-but I’m sorry if I made you feel offended."
            "That was a weird personality shift, but I’ll let it go."
            y 1b "H-how about you and I share some tea?"
            mc "O-oh, sure, that sounds great!"
            y 1a "Very well. Would you like to accompany me to get some water?"
            mc "Yeah, totally."
            "Yuri stands up and marks her page, then reaches into her bag and grabs her pitcher, then the boiler."
            "She plugs it in and sets it on the desk, then beckons me to follow her out into the hallway."
            show yuri at thide
            hide yuri
            scene bg corridor
            with wipeleft_scene
            "Yuri and I walk down the hall in silence for a few moments until, surprisingly, she speaks up."
            show yuri 1b at t11 zorder 2
            y "So, how is your and Natsuki’s relationship progressing?"
            show yuri 1a
            "I can’t tell what she’s trying to convey with that question, but nonetheless I owe her an answer."
            mc "I-it’s been great. Excellent, as a matter of fact."
            mc "We’ve spent a lot of time together, and she nursed me back to health when I got sick recently."
            mc "I really enjoy her company."
            y 1b "I’ve heard that you’re living together as well."
            show yuri 1a
            "My heart drops slightly hearing this, as I wasn’t aware this was public info yet."
            mc "Y-yeah, th-things haven’t been the best for her at home, so I decided to take her in."
            y 1f "Doesn’t that seem a bit irresponsible this early in your lives, and in your relationship?"
            "... That really isn’t Yuri’s business."
            show yuri 1a 
            mc "Well, I wouldn’t say so. I think we both know what we’re getting into, so it’s okay."
            y "You say that now, but perhaps you won’t feel that way in a few weeks."
            y 3h "I’ll just say this... tread lightly."
            show yuri 3i
            mc "R-right... {w=0.25}thanks..."
            "{i}For the unsolicited advice, that is.{/i}"
            "Yuri and I find the water fountain, fill up the pitcher, then return to the clubroom and share some tea together."
            show yuri at thide
            hide yuri
            scene black
            with wipeleft_scene
            "It may have been the most uncomfortable cup of oolong I’ve ever drank, but it at least tasted good."
            scene bg club_day
            with wipeleft_scene
            "Soon after, the club meeting ends, and Monika dismisses the four of us."
            scene bg corridor
            with wipeleft_scene
            show natsuki 1a at t11 zorder 2
            "I meet Natsuki outside of the clubroom, then take her hand and swing our arms back and forth as we walk and talk."
            show natsuki 1b at f11 zorder 2
            n "So, how were things with Yuri?"
            show natsuki 1a at t11 zorder 2
            mc "Uh... {w=0.25}hard to say."
            show natsuki 2g at t11 zorder 2
            mc "She seemed nice to an extent, but she was also being a little cold."
            mc "I dunno, maybe I’m just not super used to talking to her. I feel like I haven’t gotten to know her as well as I could’ve since I joined the club."
            show natsuki 2d at f11 zorder 2
            n "Ehehe~! Yeah, Yuri’s a tough nut to crack, but don’t worry. I’m here to help you bash her open to get to the goodies inside."
            show natsuki 2a at t11 zorder 2
            mc "... Remind me to never let you near my zipper again."
            show natsuki 1l at d11 zorder 2
            "Natsuki slugs me in the shoulder."
            show natsuki 4j at t11 zorder 2
            mc "Oogh!"
            show natsuki 5z at f11 zorder 2
            n "Ahaha~! Dummy!"
            show natsuki at t11 zorder 2
            "She thinks it’s funny, but those punches hurt..."
            mc "What did you and Sayori do together?"
            show natsuki 3b at f11 zorder 2
            n "She talked to me about this musical she’s really into. It’s kinda dark and depressing."
            n 3c "Not really my style, but I’m glad she talked to me about it."
            n 3b "Then I told her about me and you and how things are going."
            n 5e "She seemed supportive, but when I brought you up, she...{w=0.5} didn’t really seem to wanna look at me all too much."
            show natsuki 5g at t11 zorder 2
            mc "Huh. Weird."
            mc "Maybe you dating her childhood best friend is kinda awkward to her, still."
            mc "I wouldn’t think too much about it."
            show natsuki 2d at f11 zorder 2
            n "Yeah, you’re right."
            show natsuki at thide
            hide natsuki
        
    scene bg house
    with wipeleft_scene
    "Walking for a bit longer, Natsuki and I finally arrive back home after what felt like the longest literature club meeting of our lives."

    stop music fadeout 2

    scene black
    with fade
    pause(1)
#End scene 1

#Scene 2 - A Momento:
    scene bg livingroom
    with dissolve_scene_full

    play music t12
    "At home, Natsuki and I are prepared to put the day behind us and look ahead to tomorrow."
    "Or more precisely, ahead to tonight, as at around 5:30, Natsuki decides that she wants to start making dinner."
    mc "What do we have? I haven’t shopped in a little while."
    show natsuki 5g at t11 zorder 2
    n "You don’t say?"
    "She says that sarcastically as she opens a very painfully empty cabinet, letting the wind flow out of it."
    mc "S-sorry."
    n 4z "Hehe~! I’m just picking on you. I’d be happy to start making grocery runs for us."
    n 3d "You know, just as long as you learn how to clean after yourself better."
    show natsuki 3a at t11
    "Naturally I think back to the tornado, also known as me, that blew through my kitchen this morning when I tried to make breakfast."
    mc "Alright, I get it, no need to pick on me so much."
    n 1k "Did I hurt your feelings?"
    show natsuki 1n at t11
    "She says that with sincere concern."
    mc "No! Don’t worry!"
    n 1q "O-okay, good. I just don’t wanna actually hurt your feelings."
    show natsuki 1s at t11
    "A tsundere who {i}doesn’t{/i} want to insult me? Which slice-of-life manga did I wake up in this morning?"
    show natsuki at thide
    hide natsuki
    "I let Natsuki take control of the kitchen for the time being while she magically conjures up a dinner using nothing but instant noodles and soy sauce."
    "I remember that I left the bedroom a bit of a mess this morning and I adjourn to it to fix it up."
    scene bg bedroom
    with wipeleft_scene
    "I walk in and see mementos of our little experience and immediately start to get hormonal."
    "However, I choose to push the feelings down so I can focus on my chores."
    "Still..."
    "It’s weird knowing I’m not a virgin anymore."
    "I still feel just about the same, and I feel like Natsuki must feel the same way, too."
    "It’s not something I ever particularly cared about, but it’s comforting knowing I finally got to experience one of life’s greatest wonders."
    "And sharing that moment with a girl like Natsuki is something I’ll always treasure."
    "Once and for all I stop thinking about having sex...heh, awesome...then I start to pick stuff up off the floor."
    "Natsuki’s clothes sit on the ground and I pick them up, then throw them in the hamper to be washed."
    "I look at the box of belongings Natsuki brought with her and realize that this outfit I just picked up is just one of very few she managed to fit into it."
    "I ought to sacrifice some of the money from my parents’ stipend to let Natsuki go shopping soon."
    "Not to mention she might need some self-maintenance products like razors, shampoo, and other...feminine things."
    "I’m sure she has a lot of stuff at home, but I think she and I can both agree that we don’t want to venture back to her old house."
    "Her father must be infuriated with her and I both. I don’t want to see what happens if I were to see him face to face."
    "I’m scared I’d punch the son of a bitch in his mouth."
    "I finish picking up our dirty clothes, then I frustratingly attempt to make the bed."
    "Once these tasks are completed and the room is more liveable, I decide to take a break. I leave my bedroom and reunite with Natsuki."

    stop music fadeout 1

    scene bg kitchen
    with wipeleft_scene
    "She’s in the kitchen cutting vegetables and boiling some water on the stove."
    "I have to give her credit, she’s doing a whole lot with very little at the moment."

    play music t6 fadein 2

    mc "What are you working on?"
    show natsuki 1b at t11 zorder 2
    n "Trying to make some noodles with steamed veggies."
    n 2d "Your pantry is not doing me any favors, but I can work some magic. Just trust me."
    show natsuki 2a at t11
    mc "I do trust you, Nats. Where’d you learn to cook so well anyway?"
    n 2t "Uh... it was... {w=0.25}my mom who taught me!"
    show natsuki 2s
    mc "Your mom? You haven’t mentioned her before, have you?"
    n 2u "..."
    mc "What's she like?"
    n 1q "Hey, uh, I don’t really want a lot of distractions right now, so do you think you could, like..."
    show natsuki 1s
    mc "O-oh, s-sure, no problem. Sorry to disturb you."
    n 1h "It’s okay, [player]. You should be finishing your chore too, you know?"
    show natsuki 1g
    mc "Well pardon me for wanting a break! Ahaha."
    n 5w "We don’t take breaks in this house! We take action!"
    show natsuki 5g at t11
    mc "You don’t decide what we do in this house!"
    n 5y "Give it time. You’ll learn that I can be {i}veeery{/i} persuasive."
    mc "Heh, I’ll hold you to that."
    show natsuki at thide
    hide natsuki
    "I leave the kitchen then return to the bedroom prepared to return to my tasks."
    scene bg bedroom
    with wipeleft_scene
    "I walk up to the box Natsuki brought with her and sift through it for a few moments, mentally preparing places where her belongings can be safely stored."
    "As I’m looking through, I catch sight of something at the bottom."
    "I reach into it and it feels dense, with the texture of worn leather."
    "I wrap my fingers around it, then pull it out, careful not to inadvertently let anything above it spill out onto the floor."
    "Extracting the curious item, I see that it’s a large leather-bound book, which appears to be several decades old."
    "I open the front cover, and written in very well-preserved calligraphy, it reads, {i}The Shimizu Family Cookbook.{/i}"
    "Huh. I wonder what’s inside."

    play sound "sfx/pageflip.ogg"

    "I very delicately flip through the pages of the book, as it seems any careless motion can tear one of these ancient pages."
    "It’s filled with dozens of noodle, rice, meat, and seafood dishes, as well as lots of desserts."
    "I notice that the handwriting has some variation, implying that this has been written in by multiple people."
    "Sometimes there are notes in the margins in different handwritings on the same recipe, with suggestions for ingredient substitutes or different portion sizes."
    "From what I can gather, this is a cookbook spanning several generations of women in Natsuki’s kin."
    "I even see one or two cupcake recipes that Natsuki herself seemed to write into this book."
    "This is incredible! I have to ask her more about this."
    scene bg kitchen
    with wipeleft_scene
    "Cookbook in hand, I power walk my way back to the kitchen to smell some noodles and vegetables being cooked to perfection."
    "I feel extra encouraged to try Natsuki’s home cooking now that I’ve been acquainted with this book."
    "Natsuki turns toward me and smiles."
    show natsuki 1a at t11 zorder 2
    n 2l "Dinner’s almost rea--{nw}"

    stop music fadeout 1

    show natsuki 1v at d11
    n "HEY!"
    "She notices the book in my hand, then dashes toward me, and instinctively I pull it away and above her head so she can’t reach."

    play sound "sfx/slap.ogg"

    hide natsuki
    show natsuki 1v at d11 zorder 2

    "At that moment, Natsuki knees me in the stomach, forcing me to lower the book toward my chest, and she snatches it from me."
    mc "Natsuki!"
    mc "What the hell!"
    n 1h "Oh my god! [player] I’m so sorry!"
    n 1m "I didn’t mean to do that! Are you hurt?"
    show natsuki 1n
    "The wind is a bit knocked out of me, but I regain my composure and take a deep breath and settle myself."
    mc "I-I’m fine."
    "Natsuki grabs my hand apologetically, then sets the book down on the table beside us."
    n 1u "I’m sorry. I just...don’t like other people touching this."
    mc "I’m sorry... I happened to look through it a little bit."
    mc "My curiosity got the best of me."
    n "No, it’s... fine."
    mc "Is there something you’re trying to hide from me, Natsuki?"
    n 1q "N-n-no! It’s nothing."
    n 1s "It’s just an important family heirloom and I wouldn’t want anyone damaging it."
    show natsuki at thide
    hide natsuki
    "The implication with those words is that she doesn’t trust me, but it’s not important."
    "I’m more zeroed in on the hesitation she had when I asked if she was hiding something."
    "I can tell that, in fact, she is, and won’t spill it."
    "I’ll ask her about it after dinner and the table is prepared, because it seems to be something important."
    "After Natsuki and I set the table, I examine all the food she’d prepared for us."
    "Delightful rice, noodles with some nose hair-singing spices, and steamed vegetables."
    "She also managed to prepare some miso soup, which I’m about 90 percent certain I didn’t have the ingredients for."
    "She definitely did some wacky voodoo stuff while I wasn’t looking, but as long as we’re eating good, I won’t complain."
    "Once we divvy up the dishes, Natsuki and I sit and eat in a pronounced silence for several minutes."
    "I look at her, but she’s not making eye contact with me. She looks at the book beside her after every other bite she takes."
    "Natsuki finally does look up at me and sees my utensil-less right hand and empty mouth."
    show natsuki 1k at t11 zorder 2
    n "How come you aren’t eating?"
    show natsuki 1j at t11
    "I take a deep breath, trying to gather all the thoughts I need in order to say what I have to say as delicately as possible."
    "However, Natsuki seems extremely worried."
    n 1m "I... didn’t do a good enough job for you, did I?"
    show natsuki 1n at t11
    "Wait what?"
    n 1u "I’m sorry, I should’ve known you wanted meat with all of this."
    n 12e "I wish I could’ve prepared something else, I..."
    show natsuki 42f at t11
    "Natsuki begins to well up, and I’m close to panicking."
    "I know that Natsuki has had trouble with confidence in the past. She gets this hopeless look in her eye when she feels like she isn’t good enough."
    "I’ve seen it when she’s shared poems with me, and I was always happy to assure her that I think very highly of everything she does and sets out to do."
    "Right now will be no different."
    mc "No, no, Natsuki, I promise you it’s all great!"
    mc "I couldn’t ask you to do much more than this, you did an incredible job here."
    mc "I just..."
    show natsuki 42h at t11

    play music t9 fadein 2

    mc "Natsuki, I’m worried about you."
    mc "You seem really tense about this cookbook thing."
    mc "And... you got very distant when I brought up your mom earlier."
    mc "If there’s something you need to talk to me about, just know I’m right here, and I want to know what’s going on."
    "Natsuki maintains the concerned expression on her face, then speaks up."
    n 42i "I don’t want you to worry about me."
    n "I don’t want you seeing that side of me, [player]."
    n 42f "I don’t want to be abandoned again..."
    mc "Natsuki I will never abandon you."
    mc "I’m taking the responsibility, a-as your boyfriend, to listen to your problems and understand you on a deeper level."
    mc "Please help me out here."
    n 42h "..."
    n 42e "You’re so...special to me."
    n "You mean the world to me, [player]."
    n 12g "I’m so grateful to you, so I won’t keep this in anymore."
    show natsuki 3u at t11
    "Natsuki puts her left hand on the recipe book, and strokes her fingers across it, as if she’s trying to absorb its aura."
    n 3q "This book..."
    n "It belonged to my Mama."
    n "And her mama before her."
    n "It's been passed down and passed around for generations for a few decades now."
    n "My mom was the last person to own it before me."
    n "I just don’t like to talk about her, because it...hurts me, and I’m scared you’ll think I come with way too much baggage and you’ll leave me, which would hurt me even more."
    show natsuki 2n at t11
    mc "Natsuki, I’m your boyfriend. I vow to you that I’ll never leave you because you’ve been through hard stuff in the past."
    mc "I want you to tell me about your mom. As long as you’re comfortable with it."
    n 3u "..."
    n 3q "I wasn’t super comfortable with it before, but..."
    n 3m "You changed that really quickly."
    n 1m "So I'll go ahead and tell you."
    show natsuki 1u at t11
    "Natsuki takes a deep breath, as if she requires all the oxygen in this room for what she’s going to say next."
    n 1h "My mom was...the best lady I knew."
    n "And... {w=0.25}when she was with my dad..."
    n 1n "My dad was a good person."
    n 2q "And... their marriage wasn’t perfect, but... {w=0.25}they loved each other, and they loved me."
    n 2u "And I loved both of them so much."
    show natsuki 12d at t11
    "Natsuki clenches her eyes closed, trying to block off any tears from escaping."
    show natsuki 12g at t11
    mc "Natsuki, you don’t have to feign strength for me. I promise I won’t judge you for crying."
    show natsuki 12f at t11
    "As I say this, Natsuki starts to sob and take rapid breaths for several moments before regaining her composure."
    show natsuki 12d at t11
    "She sighs, then continues."
    n 1u "So... {w=0.25}when I was eight years old, my parents and I took a road trip together."
    n 1q "Everything was... going fine, but..."
    n "It was late at night, and my parents were both tired and cranky from being on the road."
    n 1u "One thing... {w=0.25}led to another, and eventually..."

    stop music fadeout 1

    n 1q "We crashed."
    n 1u "My Mama..."
    n 42d "..."
    n 42e "She didn't make it."
    n "She died on impact."
    show natsuki 42f at t11
    mc "Natsuki..."
    show natsuki at thide
    hide natsuki
    scene black
    with fade
    "I stand up and walk over to her, letting the horrific tale she just told me enter my brain."
    "It’s hard to process, but I’m trying my hardest."
    "I give Natsuki a hug as she cries into my chest."
    mc "It's okay, Nats..."
    mc "You can stop there for tonight."
    mc "I don't want you to feel too hurt."

    play music t10

    mc "But I’ll be here to comfort you tonight, and every night for the foreseeable and unforeseeable future."
    n "[player]..."
    mc "Yeah?"
    n "I already told you... no nicknames."
    "Her sobs start to slowly fade into giggles, and I squeeze Natsuki tighter."
    mc "Don’t play with fire, or you’ll get burned."
    "Natsuki and I share a laugh as we continue to hug."
    mc "I hope you aren’t mad at me for prying so much."
    n "N-no... {w=0.25}you weren’t..."
    n "I’m glad I told you."
    n "You gave me the strength I needed to take this step with you."
    n "I feel like we can trust each other so much more now that I told you my secret."
    mc "Do you have more to tell me?"
    n "..."
    n "Yes. But not right now."
    scene bg kitchen
    with dissolve_scene_full
    "I return to my seat and finally begin eating Natsuki’s delicious food."
    "I’m in pure bliss with every bite, and I’m so lost in it that I don’t notice her leave the room."
    show natsuki 2u at t11 zorder 2
    n "I was just... putting the book in a safe spot."
    n 2s "Thank you again for being so understanding..."
    n 2d "And not pressing charges for me kicking you in the stomach."
    show natsuki 2a at t11
    mc "Ahaha, this amazing food is enough recompense for what you did."
    n 2z "Ehehehe~!"
    n 2l "You’re a dork."
    n 1j "And... {w=0.5}I love you."
    mc "I love you too, Natsuki."
    show natsuki at thide
    hide natsuki
    "I continue to eat, and so does Natsuki."
    "Whether she wants to admit it or not, she and I are each other’s family now."
    "And I treasure getting to have a family dinner with her."
    "Like I treasure every moment the two of us share."
    "Natsuki... I will hold onto you and never let go..."
    "She and I are going to continue to thrive in this home..."
    scene black
    with fade

    stop music fadeout 2
    pause 1.5

    "In {i}our{/i} home."
    pause(1)
#End Scene 2

#Scene 3 - Regression
    scene black
    play music t16


    scene black

    # As the previous scene ends on a black I need this pause to make the scene transition more "obvious".
    pause 2

    play music t16

    "It's dawn outside."
    "There's a pitter-patter of rain on the roof."
    "The lights from the highway flash by."
    "Faster than the eye can see."
    "I try to chase the droplets on the window."
    "I’m too tired to keep up..."
    "But the noise keeps me up."
    "The noise..."
    "The voices."
    "They're noisy."
    "And they’re coming from up front."
    $ y_name = "Voice 1"
    $ s_name = "Voice 2"
    y "Katashi, I told you our exit was coming up!"
    s "I know."
    y "Then why did we miss it?"
    s "Maybe because {i}someone{/i} can’t stop talking for five minutes."
    y "I only-"
    "I give up on listening in."
    "This always happens."
    "They get angry at the slightest thing."
    "Like when mom forgets to do something around the house."
    "Or..."
    "Or when dad comes home barely standing up."
    "Parents are funny like that."
    "It’s hitting the top and front of the car."
    "It’s making more noise."
    "But it's calmer."
    "It makes me wanna sleep because of how..."
    "P-"
    "Pers..."
    "Because of how long it lasts."
    "It’s like a drawing made of stars on the glass."
    "Almost like if I could reach out and grab it."
    "I reach out, but to grab nothing in particular."
    "I'm bored."
    $ n_name = "???"
    n "M-Mom?"
    n "D-Dad?"
    "The noise stops for a second."
    "My mother turns around and looks at me."
    $ y_name = "Mom"
    y "What is it, sweetie?"
    n "How long is it going to be ‘til we get home?"
    "My dad looks away from the road."
    $ s_name = "Dad"
    s "As long as the traffic is good, we should be there any s-{nw}"

    stop music
    play sound "sfx/smack.ogg"

    y "{i}OH MY GOD, Katashi!{/i}"
    "But..."
    "It was only a second..."
    "He only took them off for an instant."
    "This is so..."
    "Unfair..."
    $ y_name = "Yuri"
    $ s_name = "Sayori"
    $ n_name = "Natsuki"

    scene bg bedroom_night
    with dissolve_scene_full
    "I'm shaken up."
    "And awake."
    "All I can feel is the darkness of the room and Natsuki's grip on my body."
    mc "Natsuki?! What’s wrong?"
    "She shakes around and hits me with her foot."
    "She doesn’t seem to hear me."
    n "Mommy!"
    "I turn back to the girl in my bed and cradle her comfortingly."
    mc "Hey, hey."
    mc "Calm down."
    mc "Everything is okay."
    mc "I'm here."
    "The girl shakes around some more."
    "I can see an expression of horror on her face."
    "Her eyes suddenly open, with a shimmering look to them."
    "..."
    "She settles down eventually and turns towards me."
    n "It was..."
    mc "..."

    play music t10

    n "It’s all my fault."
    mc "What is, Natsuki?"
    "She doesn’t respond at first."
    "A look of almost disgust appears on her face."
    "She thinks for a second, and eventually turns around."
    mc "Uhm..."
    mc "So-{nw}"
    n "You probably already guessed."
    n "I had a nightmare."
    n "Sorry I woke you up."
    n "It’s really nothing important... I-"
    "I’m surprised by how sudden her speech is."
    "I can’t help but be curious about it."
    mc "Don't worry about it..."
    mc "So..."
    mc "Maybe you wanna talk about it..?"
    "There’s a pause and I half expect her to say no."
    n "I..."
    n "I would like to."
    n "Please."
    "Her voice gets really soft."
    "I scoot closer to hear her better."
    "A wave of relief flies over her delicate body."
    n "So..."
    n "You know how when I was younger, my mom... died in a car crash?"
    mc "Yeah, I do."
    n "Well..."
    n "It was late one night and..."
    n "My dad, h-he looked away..."
    n "For {i}one{/i} second..."
    n "We..."
    n "We drove into a tree..."
    "At this moment, Natsuki bursts into tears."
    "My breath catches in my throat. She was in a car accident?"
    "I can somewhat tell where this story is going."
    n "I didn’t remember much from that point on..."
    n "I was brought to my house."
    n "My babysitter was there."
    n "She cried and hugged me, but I couldn't understand why."
    n "I was scared."
    n "Then the next day a man with a blue uniform showed up..."
    n "I think he was a police officer."
    n "He started talking with my babysitter, and a minute after she was crying again..."
    n "She started hugging me, and I was scared and confused."
    n "They told me Papa was fine. But I didn't care about him..."
    n "I asked where my mom was."
    n "They wouldn't tell me at first, they just kept saying \'it's okay, your dad will be here soon.\'"
    n "I got even more scared and a little angry."
    "In the midst of her story, Natsuki slips her hand into mine. I take it and squeeze it reassuringly."
    n "I couldn't understand why they wouldn't tell me anything about Mom."
    n "I guess I must have pushed enough that they finally relented."
    n "The officer bent down on one knee and told me my mother wasn't coming."
    n "He explained that she died in the hospital from her injuries."

    stop music fadeout 1

    n "And the last thing she said was, \'Tell my princess... {w=0.5}I love her.\'"
    show natsuki nbla2f at t11 zorder 2
    "I feel Natsuki’s grip on my hand tighten."
    "I’m speechless. I can’t think of anything to say. What would one say in this sort of situation, anyway?"
    "She sniffs and reaches for my box of tissues."
    n nbla2i "She wanted to give me a present, because my birthday was coming up."

    play music t10 fadein 2

    n "And she wanted to give me... {w=0.5}That book."
    show natsuki nbla2f at t11
    "It all makes sense now. I understand why she didn’t want to talk about it and why she got angry when I had it."
    "I can sense Natsuki’s waiting for me to say something."
    "I’m still trying to process all this. It’s very surreal for me to think about."
    "How would I feel if I lost a family member in an accident like that? Let alone a parent."
    "And at such a young age."
    "It’s moments like these when I begin to question the existence of a fair and all-loving deity watching us from the clouds."
    "What god would find it appropriate to rip away something so crucial to a young girl so violently, so maliciously?"
    "It just seems so sensless."
    "But I can’t get lost in my personal feelings on death and religion. Natsuki needs me now."
    "I shake my sorrow off and summon the will to speak."
    mc "I still don’t understand why you said it’s all your fault."
    mc "From what you told me, it wasn’t anyone’s."
    "Natsuki pushes my arm away."
    n nbla2h "It {i}is{/i}. I was selfish and it cost me everything."
    mc "Is that what you think?"
    "She doesn't respond."
    n nbla2i "What?"
    mc "I think that's a dumb way of thinking."
    show natsuki nbla2a at t11
    "Natsuki stiffens and gives me a scathing look."
    mc "Let me explain."
    mc "You had no way of knowing that would happen."
    mc "And, if anything."
    show natsuki nbla2b at t11
    mc "It was your father's fault for not keeping his eyes on the road."
    mc "Ad the driver, he's liable for whatever happens."
    mc "But he lost just as much as you."
    mc "That's what I think."
    show natsuki nbla2d at t11
    "We’re silent again for a few moments, sitting on my bed, shoulder-to-shoulder."
    "It’s been quite a day so far. But, on the positive side, I think I’m beginning to know even more about Natsuki than before." 
    "These... {w=0.15}\"complications\" seem to be drawing us closer together."
    "I wonder if she’s ever mentioned this to someone else."
    "My guess would be Yuri, but they haven’t been on best terms lately."

    stop music fadeout 2

    "I think for a few seconds while the mood settles down."
    "A thought occurs to me."
    "Has her father..."
    mc "Hey, Natsuki."
    show natsuki nbla2a at t11
    mc "Did you father ever get violent in front of your mother?"
    "Natsuki shook her head."
    n nbla2c "No."
    n "He would have never."
    n "He did get angry sometimes, but..."
    n nbla2b "Never to the point of hitting me or my mother."
    n "Well, after my mom died he started drinking again."
    n "Heavily."
    n nbla2c "He didn't take proper care of me, and it lasted up until recently."
    n "At first my babysitter would come pretty often."
    n "She'd stay late, despite my father's threats to stop paying her."
    n "Eventually she stopped coming, which is when I learnt he fired her."
    n "\'I won't pay someone who can't leave when they're told to\' he said."
    show natsuki nbla2d at t11
    "Natsuki takes a deep breath, and continues her story."

    play music t10 fadein 2

    n nbla2c "Well..."
    n "It just got worse afterwards."
    n nbla2b "He lost his job, and had to be a part-time mechanic for a whie."
    n "He would come home late, reeking of beer."
    n "If I didn't maker dinner for him, or if it wasn't good enough, he'd call me names."
    n "He'd throw my food out and make me go to sleep without it."
    "My jaw tightens. The more I hear about Natsuki’s dad, the less respect I have for him."
    "And I didn’t have much in the first place."
    n nbla2a "And then, for after I learned how to cook and clean like Mom used to, things calmed down a bit."
    n "He'd still yell sometimes, but not as much."
    n "Then one day..."
    n nbla2d "I had to stay late at school for a class project."
    n nbla2c "I lost track of time and didn't start heading home until it was dark out."
    n "Even at thirteen, I knew I was in trouble because I wasn’t home in time to cook dinner or clean anything and Papa would be waiting for me."
    n "When I got there, he was angrier than I had ever seen him."
    n nbla2e "{i}That{/i} was the first time he ever hit me."
    n "He slapped me across the face and accused me of sneaking around with a boy."
    show natsuki nbla2g at t11
    "She gestures across her face, indicating where he slapped."
    n "I tried telling him I wasn't and that I was sorry that I was late."
    n "He wouldn't listen."
    n nbla2e "It was just another night of no food and early bed."
    n "It went on for years."
    n "He was so controlling. The only time I got away from him was when I went to school."
    n "And summer was the worst."
    show natsuki nbla2b at t11
    "She pauses and leans against me, nesting her head between my shoulder and chin."
    n nbla2c "But then, a girl in my class found me on the roof of the school and told me about a club..."
    n "I didn’t care what kind of club it was, all that mattered is that it would be small enough that I could fit in and meant more time away from Papa."
    show natsuki nbla2b at t11
    mc "Any chance that girl was Sayori?"
    "I can feel Natsuki give a half-hearted chuckle."
    n nbla2c "Of course, stupid. We just weren’t super good friends yet."
    n "But I joined anyways and started going to the meetings everyday."
    n "The only one I recognized was Monika."
    n nbla2a "We’ve been friends since middle school. But I never took her as the type to take an interest in literature."
    n "I mostly kept to myself at first. But Sayori and Monika tried really hard to get me invested with the club and getting me comfortable with them."
    mc "What about Yuri?"
    n nbla2d "She was there too, we all have been since the beginning."
    n "But she was just as quiet and bashful then as she is now. So it wasn't easy."
    n "Long story short, though, I ended up feeling like I found the one place I truly belong and where I was accepted for who I am."
    n "..."
    n nblau "And then {i}you{/i} came along."
    mc "Hard to see that as any sort of compliment."
    n nblan "Hush, let me finish."
    mc "Okay."
    n nblaq "Yeah, I was upset."
    n "I wasn't expecting a boy."
    n "I though having one would ruin the club."
    show natsuki nblas
    mc "How so?"
    n nblat "Well, Sayori talked about you a lot. She said she was bringing {i}someone{/i}, but she didn’t say it would be you."
    n "If I didn’t know any better, I would’ve thought you were her boyfriend."
    n nblau "And if you weren’t it would only be a matter of time before someone tried fighting over you."
    n nblat "But, I guess I did think you were kind of cute, in your own clueless way."
    "I decide to take that as a compliment."
    n nblar "Then Monika decided to start sharing poems."
    n "I figured you’d just treat me like a kid like everyone else."
    n nblas "Then..."
    n nblaq "Then I read your poem. It wasn’t what I was expecting."
    n "It was almost like you wrote it for me."
    n nblan "And, well, the rest is history."
    n nblal "I can’t thank Monika enough for forcing us to get to know each other."
    show natsuki nblaj at t11
    mc "Yeah, me too."
    "I look at the clock, it’s now almost 1:00."
    mc "We should probably go back to bed, school’s in another few hours."
    n nblak "Okay, yeah."

    stop music fadeout 6

    show natsuki at thide
    hide natsuki
    "We shuffle back into our original positions and I hit the light."
    n "Hey, [player]."
    mc "Yeah?"
    "I yawn my reply and Natsuki sounds exhausted too."
    n "Thank you for... listening."
    "Through my fatigue, I work up a weary smile even though I know she can’t see it."
    mc "Of course, I love you, Natsuki. I’d do anything for you."
    n "Anything, huh? Bold words."
    n "But..."
    n "I just want you to do one thing."
    mc "What is it?"
    n "Promise me you won't ever leave."
    "The words leave my mouth before I even think about the question."
    mc "I promise. I will never leave you alone if I can help it."
    n "Hmph, good enough."
    n "Good night, [player]."
    mc "Good night, Natsuki."
    scene black
    with fade
    pause(1)
#End Scene 3

#Scene 4 - Tension (2)
    scene bg corridor
    with dissolve_scene_full
    "It's another day at school."
    "After all the drama and philosophical thoughts of yesterday, I’m actually glad for the subtle routine of academic study for once."
    "Natsuki and I made it to school on time, and Sayori even caught up with us along the way."
    "Words cannot express how relieved I am to see her in her usual state of good cheer and childish naïvete."
    "She was a welcome addition to the trek, even if she spent most of her time speaking with Natsuki about some sort of science project."
    "I guess it’s easy to take the little things for granted when they happen every day."
    "Maybe the low times are just fate’s way of putting the simple and dull in perspective; to make us appreciate them more."
    "I let that thought sink in."
    "It seems my way of thinking and expressing myself has gotten more philosophical and poetic as of late, I’ve noticed."
    "It could be the literature club rubbing off on me, I suppose."
    "But I’m more inclined to believe that it’s the people in it rather than the club itself."
    "Particularly a certain short-haired, endearing girl I’ve been spending a lot of time with."
    "But I’m sure Monika and Sayori also had a hand in that."
    "Yuri too."
    "I arrive outside of the clubroom and open the door to enter."
    scene bg club_day
    with wipeleft_scene

    play music t5

    "The scene in front of me is comforting in its familiarity."
    "Monika’s at her desk, reading a small book with what appears to be classic poetry."
    "Yuri’s sitting alone, nose deep in another book." 
    "This one is different from the last one, I notice, but I don’t linger on it."
    "Instead, my vision shifts to Natsuki in the back, rummaging around in the closet, evidently looking for her manga."
    "Everything looks safe; normal."
    "Wait."
    "My eyes drift to the spot where Sayori usually sits, but it's missing a Sayori."
    "Okay, I {i}know{/i} she was here today. Why isn't she at the club?"
    "I turn towards Monika and her eyes meet mine. She glances at Sayori’s desk and then moves her gaze back to me."
    "I get the message, so I shuffle over to her desk."
    show monika 2d at t11 zorder 2
    m "[player], have you seen Sayori today?"
    "I nod."
    m 1d "When?"
    mc "When Natsuki and I were walking to school. Sayori met up with us and went to class."
    mc "She hasn't said anything to you?"
    "Monika sets down her book and closes her eyes."
    m 1g "No, unfortunately."
    m 1f "Did she seem ill or something?"
    mc "No, I don't think so."
    m 2f "Hmm..."
    "Monika falls quiet for a moment and appears to be deep in thought."
    m 2o "I wonder..."
    "A moment passes and then she opens her eyes and gives the most serious look I’ve ever seen from her."
    m 3g "Listen, [player]. I'm really concerned by Sayori's continued absence. It isn't like her."
    "I nod, because to be honest, so am I."
    m 1p "She won’t talk to me. I’ve tried."
    m 1i "So I’m going to have to ask you to check up on her."
    "I should’ve done that when she first started not showing up, I think to myself."
    "But, with Natsuki and everything that happened yesterday, I just didn’t think much about it."
    "I kick myself a bit, because Sayori deserves better than that."
    m 1g "After today’s meeting, can you go to her house and see how she’s doing?"
    mc "Of course, but if she won’t talk to you what makes you think she’ll talk to me?"
    show monika 1m at t11 zorder 2
    "Monika gives me a weary smile."
    m 1e "I {i}know{/i} she will."
    m 2e "You've been her friend longer than I have."
    m 2m "And..."
    m 2p "Well..."
    m 1r "Let’s just say I have my suspicions and leave it at that."
    "I want to ask what she means by that, but I can guess Monika won’t elaborate."
    "I have no choice but to nod in agreement and understanding."
    m 3h "Let me know how it goes. You have my number."
    mc "Okay, will do."
    show monika at thide
    hide monika
    "With our exchange concluded, I step away from Monika’s desk as she turns her gaze towards the window, apparently still lost in thought."
    scene bg closet
    with wiperight
    "It’s nearing the end of the meeting and I’m busy putting away Natsuki’s manga for the day."
    "We barely made it through one chapter this time around."
    "My heart was in the right place, but my mind kept drifting to Sayori."
    "What am I going to say when I see her?"
    "How could Monika be so sure she’ll talk to me?"
    "What exactly was going on with her? And how does the club factor into that?"
    "Even Natsuki could tell my mind was somewhere else."
    "She asked once and I declined to talk about it. I assured her that I was simply tired and I guess she bought it."
    "I’m putting the last box back in place when I hear Natsuki and Yuri talking behind me."
    "I perk up my ears, surprised to hear from Yuri at all."
    "I can barely hear what's being said, but it seems to be something about poetry."
    "From what I can tell, it seems like Natsuki is asking Yuri to keep trading poems with each other."
    "I’m more than a little surprised by that."
    "Given how often they fight, I got the impression they didn’t like each other and that Yuri didn’t like me by association."
    "Or maybe Natsuki just feels bad about those past disagreements and is offering an olive branch of sorts."
    "As I back out of the closet, Yuri replies."
    "Again, I'm too far away to make out the exact words, but I can hear the tone."
    "It's not very pleasant and sharp. The only word I hear is Yuri spitting out my name venemously."

    stop music fadeout 1

    "Uh-oh."
    scene bg club_day
    with wipeleft_scene
    "I turn around on a dime and I see Yuri grabbing her stuff off the desk before hotly marching out of the clubroom."
    "Natsuki is staring after her and I can see the smaller girl struggling between expressions of confusion, fury, and dolor."
    "Monika is still seated at her desk and evidently watched Yuri leave in a huff as well."
    "She turns her gaze from the closed door and raises an inquisitive eyebrow at Natsuki and me."
    "I don’t fully understand what happened between Yuri or Natsuki either, so I’m no help and I avert my gaze with a half-hearted shrug."
    "Natsuki growls and whips her head away, catching me in her sight. She’s visibly distraught and frustrated."
    show natsuki 1n at t11 zorder 2
    n 1n "So..."
    n 1m "What did you overhear?"
    mc "Not much"
    "I can see she’s calming down slightly. Her hands are still balled up in fists, but her expression is softening."
    "She’s still frustrated, but not necessarily angry."
    "I wait for her to explain what happened."
    "Or, rather, what was said."
    "My patience is rewarded a few breaths later."
    n 2s "I just..."

    play music t9

    n 2m "I just asked her if we could start sharing poems again and she got really upset."
    n 1m "I know we’ve had our disagreements in the past, but…"
    "She pauses and looks down at her feet."
    n 3r "Apparently she thinks that since I have a boyfriend now I’m somehow rubbing it in her nose."
    "I'm silent for the time being. That explains Yuri's issue with me, I guess."
    n 4s "I was just trying to be friendly."
    mc "It was a nice gesture."
    "Natsuki looks back up at me."
    n 4m "Look, I may not say this a lot, but I like Yuri."
    n 2m "Before you, she and Monika were the closest thing I had to having friends."
    n 2u "Seeing her like this..."
    n 1m "It makes me feel sad."
    n 1q "And maybe even a little guilty."
    show natsuki 4s at t11 zorder 2
    "She pauses to place her hands on her hips."
    n 4r "But she won’t even give me a chance to explain I still want to be friends."

    stop music fadeout 2

    "I can only imagine where this is going."
    "Natsuki suddenly gives me a flirty look."
    "That all but confirms my hunch."

    play music t5_natsuki

    n 1k "Hey, [player], do you think you could talk to her?"
    n 1c "She might be more willing to listen to you if you approached her first."
    n 1i "...{w=0.25} Alone, obviously."
    "I hesitate. This seems like a really bad idea."
    "Natsuki isn't relenting."
    n "I can really make it worth your time."
    "Her voice is heavy with seduction."
    "Damn, she's really not making this easy."
    "On one hand, Monika asked me to check up on Sayori, and my instinct tells me that's the right thing to do."
    "But if I patch things up with Yuri and Natsuki, it'll make Natsuki happy."
    "Plus, it might even make the club feel whole again."
    "After all, Sayori usually springs right back. Thats her talent..."
    "Right?"

    stop music fadeout 2

    menu:
        "Right?"
        
        "Check on Sayori":
            #Send to scene 5a
            $ tens_check = "S"
            call Natsuki5a
        
        "Check on Yuri":
            #Send to scene 5b
            $ tens_check = "Y"
            call Natsuki5b
    
    jump Natsuki3
    
#End Scene 4


label Natsuki5a:
    #Start Scene 5a
    "It's a tough call, but I have to be there for Sayori if she needs me."
    "We've been friends since elementary school."
    "If something was up with me, I'd want her to be the first to check up on me."
    mc "I-"
    mc "I'm sorry, Natsuki, but I already promised Monika I'd check up on Sayori."
    mc "She was absent from the club again today and that worries me."
    "I’m confused by Natsuki’s reaction. She looks like she was just splashed with cold water."
    n 4o "M-Monika?"
    n 4p "Sayori?"
    "She repeats the name and a look of pure rage crosses her face."
    show natsuki 4f at t11 zorder 2
    "I'm taken aback at the sudden change."
    n 4g "Fine."
    "She spits the word like acid and I instinctively recoil."
    n 4h "I’ll try to talk to Yuri myself then."
    show natsuki at thide
    hide natsuki
    "I open my mouth to counter, but Natsuki has already turned on her heel and is rapidly heading out of the clubroom, leaving me and Monika behind."
    "I glance at the other person in the room and she gives me a puzzled look?"
    mc "I’m gonna just get my things and then go check on Sayori."
    "It's unbelievably awkward."
    "It feels like I made the wrong choice."
    "But I know what is best for Sayori."
    "It's my job to take care of her."
    "Always has been."
    "I discreetly rush out of the classroom."
    scene black
    with fade

    play music t12

    scene bg residential_day
    with fade
    "After a few minutes, I arrive in front of her house."
    "I take a deep breath and enter."
    "I enter her room."
    scene bg sayori_bedroom
    with wipeleft_scene
    mc "Sayori?"
    "A slight moan lets me know she's here."
    "I go towards her bed. She's atop it, resting."
    "I don't want to approach her too abruptly."
    mc "Hi Sayori. {w=0.5}...How was your day?"
    "After a small pause, Sayori turns around, and sits up on the edge of her bed."
    show sayori 1bk at t11 zorder 2
    s "Alright, I guess."
    mc "Well, it doesn't look like it."
    mc "Considering you didn't come to the Literature Club."
    "Sayori looks down at her feet, embarrassed."
    s "Ehh..."
    s 1bg "W-why would you ask that..."
    mc "Well, if you couldn't tell..."
    mc "I care about you."
    mc "A lot."
    show sayori at thide
    hide sayori
    "Sayori turns away from me and looks out her bedroom window."
    s "I thought you already knew {i}why{/i}."
    "Am I supposed to know the answer?"
    
    menu:
        "Am I supposed to know the answer?"

        "Tell the Truth":
            #Scene 5a-I
            $ karma += 1
            show sayori 1bi at t11 zorder 2
            mc "I don't."
            s 1bk "{i}Oh{/i}."
            "Or at least I don't remember."
            mc "T-that's why I'm here."
            s 1bl "Heheh..."
            s 1by "You can't know me perfectly..."

            stop music fadeout 4

            s 1bd "...{w=0.25}Right?"
            mc "..."
            s 1be "What?"
            mc "Let's get serious here."

            play music t9

            mc "Sayori, I {i}really{/i} care about you."
            mc "I need you to tell me what's the matter."
            s 1bk "..."
            mc "It's important."
            s 2bl "You know, [player], there have been some things I haven't told you."
            s 2bk "A-about myself."
            s 1bk "It wasn't so much of an issue before, but lately it's been getting worse and worse and worse."
            s 2bk "I've even thought about s-"
            s 2bv "..."
            s 1bk "S-sad things."
            mc "Why..."
            mc "Why didn't you tell me before...?"
            "Does she not trust me?"
            "I can't fathom the thought of not being trusted by her, but then again, I shouldn't jump to conclusions."
            "I should just let her finish."
            s 4bh "Are you okay [player], I hope I'm not boring you with my-{nw}"
            mc "No you're not. Please, continue."
            s 1bf "Alright..."
            s 1bl "Well, the thing is, [player], I've been dealing with really bad depression since..."
            s 1bk "Well, a long time now."
            show sayori 1bt at t11 zorder 2
            "Sayori pauses briefly as if to give me a chance to react, but it’s hard for me to take it."
            "I mean, how does one viably react to hearing something like that?"
            "To find out that your bubbly, sunshiny childhood best friend has been dealing with something like this for so long…"
            "It's a hard pill to swallow."
            "Sure, I’ve noticed Sayori hasn’t been all there as of late, but I never expected something this serious to be the root of it all."
            "Sayori gives up her attempts at getting a reply from the apparent mute standing in front of her and continues to speak."
            s 2bl "Are you impressed with how well I've hid it from you until now?"
            s 2bd "Admit it, because I would be, too."
            s 3be "But recently it's been harder and harder for me to keep it locked away like I;ve wanted."
            s 1bv "A-and I think a big reason for that is..."
            s 3bf "Well, it's because of you and Natsuki."

            stop music fadeout 1

            mc "W-what?"
            "I manage to produce words for the first time in what feels like many minutes and that's all I have to offer."
            "For some reason, I feel a heavy sense of embarrassment becuase of this."
            s 1bk "S-seeing you and Natsuki together, it's... probably the most conflicted I've ever been in my life."
            s 4bh "Don't get me wrong, I mean, I'm so happy to see both of my best friends so happy, but every time I see Natsuki holding your hand..."
            s 2bv "Or seeing her hug and kiss you..."
            s 1by "Even just seeing you sit on the floor with her, resting her head on your shoulder reading manga together..."
            "Sayori pauses, like she's afraid to continue this thought."
            s 1bt "To me, [player], all my life I've thought of you as my special \'what if?:\'"
            s 2bl "As we grew up I would think so myself, \'What if [player] and I started dating?\'"
            s "\'What if [player] and I got married?\'"
            s 4bt "\'What if [player] and I had a nice house together?\'"
            s 2bd "And that \'what if?\' stuck with me up until I got you to join the Literature Club."
            s 1be "When I introduced you to my clubmates, and when you started getting close to Natsuki."
            s 1bv "I realized that I might miss my chance to act on my \'what if?\'"
            s 2bu "And when that happened..."
            "Sayori starts sobbing lightly then feebly falls down onto the edge of her bed."

            play music t10

            s 2bv "When that happened, I lost my \'what if?\', and the rain clouds started pouring in."
            s 1bv "And [player]..."
            s 4bw "That was the worst rain cloud I've ever had!"
            s 4bv "When I realized that you had Natsuki and didn't need me anymore..."
            s 1bu "I started to feel so worthless knowing the most important, special person I've ever known pretty soon would have no use for me."
            s "And the same goes knowing Natsuki, my best friend in the club before you probably wouldn't want anything to do with me anymore."
            s 1bw "All because I brought you to the Literature Club and blew it."
            "Sayori continues to cry, and I take a seat next to her."
            "I'm getting choked up myself at this point."
            "Nobody ever waked up thinking they're going to heat this kind of stuff from their best friend."
            show sayori 1bu at t11 zorder 2
            mc "Sayori, please, don't say things like that."
            mc "You are the furthest thing from useless to me as anything or anyone could be."
            mc "I mean, who would I go to whenever I needed a good laugh or a big smile?"
            mc "Who would I go to when I'm feeling kinda lonely and want some company?"
            s 1bi "Natsuki."
            s "You have Natsuki now."
            s "Natsuki could do all those things for you, and more."
            "I pause. I have trouble responding to this."
            "She's right, to a very minimal extent, but she seems well beyond convinced at this point that she's lost all value as a human being."
            "To the point where I struggle to find the right words to sway her thoughts in the other direction."
            mc "Sayori..."
            show sayori 1be at t11 zorder 2
            mc "Do you trust me?"
            show sayori 1bg at t11 zorder 2
            "Sayori pauses for a few moments before looking at me and nodding her head, \'yes.\'"
            mc "Then you need to trust me when I tell you this..."
            show sayori 1bv at t11 zorder 2
            mc "{i}You'll always be my dearest friend{/i}."
            mc "You will always be one of the most important people in my life, and I would be crushed if I ever lost you somehow."
            mc "Nobody, not Natsuki, not Yuri, and not Monika could ever do or say anything to change my mind."
            s 2bv "[player], I..."
            s 1bk "I need time to think."
            s 1bg "Can you please, just..."
            s 1bk "Leave me be for a little while?"
            "I almost feel like I messed up, like I didn't say the right words, but as self-loathing thoughts start floating into my mind, Sayori speaks up once more."
            s 1bt "Thank you."
            "Sayori then pulls me in for a hug, and I reciprocate."
            "In a vacuum, this is a harmless platonic gesture, but something tells me that Natsuki would not be happy knowing what I’m doing right now."
            "However at this point, Natsuki’s jealousy is far down on my list of concerns."
            "My best friend needs my support, and I will give it to her however I can."

            stop music fadeout 2

            scene black
            with fade
            return


        "Lie to Sayori":
            #Scene 5a-II
            $ jerk = True
            $ karma -= 2
            mc "Well... Of course I know why..."
            mc "I-I just wanted to check, t-thats all!"

            stop music fadeout 2

            s 1be "..."
            s 1bg "Sure."
            s 1bd "I-it's really good to have friends that {i}really{/i} care about me."
            "{i}Gulp{/i}"
            "This was a bad idea."
            mc "Y-yeah, it is."
            s 2bf "Thank you anyways."
            "I don't respond, not knowing how to or simply being being afraid to say something stupid."
            "I lied, now I gotta assume the consequences."
            "..."
            "Just kidding, I definitley won't."
            show sayori 1bb at t11 zorder 2
            mc "Oh, Natsuki is {i}calling{/i} me. I think I'd better go!"
            s 2bd "Oh, alright."
            s 2bt "{i}Sayonara{/i}, [player]."
            "Well, that was quick and cold."
            "Natsuki will be so very pissed. Lying to her isn't an option, she'll see right through me."
            scene black
            with fade
            pause(1)
            return
    #End Scene 5a


label Natsuki5b:
    #Start Scene 5b

    play music t5_natsuki fadein 2

    "Damn, Natsuki really doesn't make it easy on me."
    mc "I, uh, well..."
    "Natsuki stares at me, clearly waiting for my response."
    mc "I sorta promised Monika I'd check in on Sayori."
    "Natsuki blinks and looks confused."
    n 1c "Sayori?"
    "She pauses then takes a look around the room."
    "Her gaze then settles back on me."
    n 1q "That's right, she wasn't here at the club today."
    "She frowns."
    n 2q "But she came to school, we walked with her."
    show natsuki 2s at t11 zorder 2
    "I nod."
    mc "Yeah, that's the part that really worried me."
    mc "I think she might be avoiding us."
    mc "Like, collectively."
    "The smaller girl pauses and thinks for a moment."
    "And then she responds."
    n 2k "What if I check on Sayori for you while you see if you can talk some sense into Yuri?"
    show natsuki 2j at t11 zorder 2
    mc "Yuri? Check oh her? I hesitate. Yuri and I haven't exactly been the best of friends since we met, but..."
    "Uh, do I really have a choice?"
    "Er, I suppose so."
    mc "But do you think she'll listen to whatever I have to say?"
    "Natsuki firmly places her arms on her sides and shoots me a determined look."
    n 4e "She'd better."
    "Despite her assertive stance, a flash of uncertainty crosses her delicate features."
    n 4c "Or, I hope so anyways."
    show natsuki 4g at t11 zorder 2
    "Holding back a resigned sigh, I nod."
    "Natsuki smiles and her moment of weakness passes as quickly as it arrived."
    n 3l "And don't worry about Sayori. I'll make sure she's fine as fresh cheese by tonight."
    show natsuki 3j at t11 zorder 2
    "Her chest swells with pride and confidence."
    "Before I'm able to mention she used the wrong idiom, her eyes narrow and she speaks one more time."
    n 1e "What are you waiting for, A letter of recommendation? Go!"
    mc "Alright! Sheesh..."
    "I prepare to take my leave and head for the library wherein Yuri most likely searched for solitude before Natsuki speaks up one more time."
    n 1d "By the way, when you do talk to her, be assertive."
    n "Don't be a wimp."
    mc "H-hey, don't call me a wimp!"
    n 1b "Then don't {i}be{/i} a wimp!"

    stop music fadeout 2

    scene black
    with fade
    scene bg bookstore
    with fade
    "Finally."
    "It took me forever to find the library around here."
    "Admittedly, I've never really had to use it all that much."
    "But I fiugred Yuri had to be here."
    "If not... {w=0.25}well..."
    "A glimpse of purple catched me eye from one of the rows of shelves."
    "Gee, I wonder who that could be."
    mc "Yuri, you here?"
    "Silence greets me for a few seconds before a faint voice follows it."
    y "Don't shout in a library."
    y "And go away, please."
    "Leave it to Yuri to treat an empty storeroom for books like some sort of mausoleum."
    mc "Sorry, no can do."
    "I wait for a few moments of silence, listening for any sort of reply."
    "When none came, I headed for the row I saw the trail of hair dissapear in."
    "The horror section, I notice."
    "Unsurprisingly, no one's there when I reach it."
    mc "C'mon, Yuri, don't make me play hide and seek. I just want to talk to you."
    "Silence, then..."
    y "Why? Shouldn't you and your- your... {w=0.25}your {i}girlfriend{/i} be sucking each other's faces of somewhere?"
    mc "Sounds pretty disgusting when you put it that way."
    y "G-good."
    "A pause punctuates her reply."
    y "S-sorry."
    mc "No need to apoloigize."
    mc "Could you please show yourself? I'd rather talk to your face to face."
    "I see Yuri put her book down."
    "She starts walking over to me, head at a low angle."
    show yuri 4c at t11 zorder 2
    y "{i}sniff{/i}"
    y 4b "S-sorry, [player]."
    y "I-I've been in a bad mood this week."
    y "{i}Anyway...{/i}"
    y 4a "Why did you come here?"

    menu:

        "Tell Yuri the Truth":
            #Scene 5b-I - Truth
            $ jerk = True
            "I should just tell her the truth."
            "That's what any good friend would do."
            mc "I came here because Natsuki was worried about you."
            show yuri 3g at t11 zorder 2
            "Her head jerks up, suddenly angry."
            "Her eye twitches slightly."
            y 1r "Oh so you only care about me when y-your {i}girlfriend{/i} is worried?"
            mc "What? No, I-{nw}"
            y 3v "That's so shallow, [player]."
            y 1w "We're done here."
            show yuri at thide
            hide yuri
            "Ouch."
            "She turns around, sobbing, and leaves."
            scene black
            with fade
        
        "Tell Yuri I was Worried":
            #Scene 5b-II - Hope
            $ karma += 1
            "No harm in a little lie."

            play music t9

            mc "I came here because I was worried about you."
            y 4c "Really?"
            mc "Y-yeah, you haven't been yourself lately."
            mc "And I was concerned about you."
            y 4b "Oh... {w=0.5}I s-see."
            "{i}What else should I be saying?{/i}"
            mc "Um..."
            show yuri 3e at t11 zorder 2
            "Yuri gives me a curious look as if I actually have something profound to say."
            mc "Yuri, we're friends, right?"
            y 1h "Yes, I suppose we could use that term by this point."
            show yuri 1g at t11 zorder 2
            mc "W-well, I hope you know that as your friend, I'm willing to listen when something is bothering you."
            y 1h "Oh? And what led you to that decision?"
            y "As far as I can recall you haven't exactly shown me the friendliest of concern since we've known each other."
            show yuri 1g at t11 zorder 2
            "Crap, she might be onto me."
            "I do wish I could magically come across the right words to say in this situation, because things are getting more awkward with each passing breath."
            mc "I'm sorry you feel that way, but if you're willing to give me a chance to prove that I care then I'll do what I can to change your mind."
            "Yuri looks skeptical, and I can't blame her."
            "Even I don't feel sincere in what I'm saying."
            y 1k "{i}Sigh{/i} Well if the offer is on the table, I might as well take advantage of it to air my grievances."
            y "Though I don't believe the device of communication is ideal."
            "{i}D-does she mean me?{/i}"
            y 2j "Truthfully, I've felt quite irritated being stuck around you and Natsuki so consistently."
            y 2q "The way you act toward one another, the public displays of affection, they manage to make everyone exceedingly uncomfortable."
            "{i}Make \'everyone\' uncomfortable, or just you?{/i}"
            mc "Uh, well, I'm sorry about that, Yuri. If you want, I can tell Natsuki to be a little less forward with me during clubtime."
            mc "D-does that sound like a reasonable compromise?"
            "Why did I say that? Does talking to Yuri just make me use more big words?"
            "Yuri seems to plaster a smile on her face before scoffing lightly."
            y 1j "You don't seem to get it, [player], do you."
            show yuri 1i at t11 zorder 2
            mc "Know what, Yuri, I guess I don't."
            "That came out sounding crabbier than I'd intended, causing Yuri to obtain a sour expression."
            y 1r "I believe you and Natsuki have a toxic relationship, and at some point in the future, it's going to hurt everyone around you."
            y "Including yourselves."
            "She did not just say what I think she said."
            mc "So... let me get this straight."
            mc "I save Natsuki from her home life, I care for her, we tend to a house together, and we also happen to share some affection for one another around our friends."
            mc "And you see that as toxic?"
            "Yuri scrunches her nose for a moment, telling me that I may have been on point, or at the very least struck a nerve."
            y 1l "[player], trust me, I've seen this plenty of times in my books."
            y "When two people get attatched too soon, everything starts to fall apart at the seams."
            mc "Well, newsflash, Yuri, this isn't one of your books."
            mc "It's real life, with your real friends, and this is a {i}real{/i} relationship you're bashing on."
            mc "Maybe if you stepped back into reality one of these days, you;d realize how insane you're acting."
            "Yuri has a deep look of disdain for me now."
            "She takes a few shallow breaths out of frustration, then slams her book down onto the table before storming out of the room."
            show yuri at thide
            hide yuri
            "Once the heavy air of our tension is lifted from the library, I sit down in a chair beside me and think about what just happened."
            "I can't believe I snapped at Yuri like that."
            "I mean, I wasn't in the wrong, I don't think. She was saying things that were crossing a line."
            "She has no right to talk about me and Natsuki's relationship that way."
            "I slouch in the chair underneath me and try to find a way to relax, if only for a few minutes."
            "Pretty soon I find myself growing weary of the library and decide to walk out."

            stop music fadeout 2

            scene black
            with fade

    scene bg club_day
    with fade
    "After the encounter with Yuri, I go back to the Club."
    "Once I get there, I notice that the doors are closed, and all of the lights are off."
    "Nobody is around, not even Natsuki."
    "Suddenly I hear footsteps behind me."
    mc "Who's the-{nw}"
    n "{b}{i}NYAH!!!{/b}{/i}" 

    play sound "sfx/fall.ogg"

    with vpunch
    "We both tumble to the ground."
    mc "Ow... What was that for?"

    play music t5_natsuki

    n "Hehe~ I just wanted to surprise you, idiot."
    "She's still on top of me, a few seconds after she tackled me."
    mc "Hey get off me! My leg is sore now."
    "I crawl to my feet while Natsuki jumps up quickly."
    show natsuki 5y at t11 zorder 2
    n "Weakling."
    show natsuki 5j
    "She helps me up, with a mocking expression on her face."
    mc "Thanks."
    n "Don't mention it."
    n 2b "Want to get some coffee? I'm hungry and tired."
    show natsuki 2a at t11 zorder 2
    mc "You're always hungry Natsuki, but sure."
    mc "Where do you want to go?"
    n 1g "..."
    n 1d "How about that little cafe by our house?"
    show natsuki 1a at t11 zorder 2
    "My heart jumps a beat when she says {i}our{/i} house."
    n 4b "Something wrong?"
    n "You turned pale and kinda spaced out for a second there."
    show natsuki 4g at t11 zorder 2
    mc "No, I'm good."
    "I'm sure she noticed my hesitation."
    mc "Just hungry. Let's go to that cafe."
    show natsuki at thide
    hide natsuki

    stop music fadeout 2

    scene black
    with fade
    scene bg road_sunset
    with wipeleft_scene
    show natsuki s1j at t11 zorder 2
    n s1l "How was-{nw}"
    mc "How was-{nw}"
    n s1k "You can go first."
    mc "No, you can. You spoke first."
    n s1l "Okay then. {nw}"

    play music t2

    n s1l "Okay then.{fast} How was your day?"
    show natsuki s1j at t11 zorder 2
    mc "Mine was decent, some stressful parts as you know. Tired mainly."
    mc "How was yours?"
    n s2q "Pretty crappy to be completely honest."
    n s2m "I'm just happy that you're with me."
    show natsuki s1n at t11 zorder 2
    "She looks up at me, and pulls me into a sideways hug."
    show natsuki at thide
    hide natsuki
    "I hug her back, and she rests her head on my shoulder."
    pause(2.0)
    scene bg cafe_in
    with wipeleft_scene
    "We stay like that for a few minutes while we walk into the coffee shop."
    "We get there, and it's not busy."
    "An older couple is in the back, and there is only one server."
    show natsuki s1c at t11 zorder 2
    n "Want to get a table for us? I'll get our orders."
    mc "Alright. Can you get me a decaf coffee and a muffin? Thanks."
    n s4d "Sure thing. Get a good table near the window."
    show natsuki at thide
    hide natsuki
    "Natsuki walks off, and I go get us a small table near the window."
    "I put our bags down and take a seat."
    "The cafe is warm inside, but the chairs are still cold."
    show natsuki s1d at t11 zorder 2
    n "Here you go [player]. They ran out of lids so it has an open top."
    show natsuki s1a at t11 zorder 2
    "She sets the coffe and muffin down in front of me."
    mc "Thanks, Nat, I really appreciate it. No sweat about the lid either."
    "She sits down across from me, and starts sipping her hot chocolate."
    mc "Nothing to eat, Natsuki? I thought you were hungry."
    n s2d "I was really hoping I could get some of that muffin there."
    show natsuki s2a at t11 zorder 2
    "She smiles cutely and looks at me."
    mc "Oh sure."
    mc "Do you want my coffee too.?"
    n s4e "I don't want your backwash."
    show natsuki s4g at t11 zorder 2
    mc "Oh fine, guess we won't be kissing again anytime soon."
    n s1p "Nooo, I didn't mean it!"
    show natsuki s1n at t11 zorder 2
    mc "Mhm, that's what I thought."
    "We share a laugh, then sit in silence while I drink in my coffee and she eats my muffin."
    show natsuki at thide
    hide natsuki
    show black
    with fade
    pause(1)
    scene bg cafe_in
    with fade
    show natsuki s4a at t11 zorder 2
    "As soon as it started, it ends."
    mc "Hey, we've been here for 30 minutes. Want to head out?"
    mc "We're finished with our stuff."
    n s4d "Yeah sure, can you get our stuff while I get the trash?"
    mc "On it captain!"
    show natsuki at thide
    hide natsuki
    "She smirks as she walks away."
    scene bg road_sunset
    with wipeleft_scene
    "I meet her outside the coffee shop after everything is closed up." 
    show natsuki s5c at t11 zorder 2
    n "Ready to go?"
    show natsuki s5a at t11 zorder 2
    mc "You know it. Let's go home."
    mc "The sun is starting to set and I'm pretty tired."
    n s2d "I completely agree. Let's go."
    show natsuki s1a at t11 zorder 2
    "We walk home is silence, with Natuski leaning into me the whole time there."
    show natsuki at thide
    hide natsuki

    stop music fadeout 2

    scene black
    with fade
    scene bg kitchen_night
    with fade
    "We get home right as the sun starts to go below the horizon."
    show natsuki n4k at t11 zorder 2
    n "I'm really tired. Want to just head to bed?"
    show natsuki n4i at t11 zorder 2
    mc "Yeah sure, let's do it."
    mc "Tomorrow is the weekend, so let's make it count."
    show natsuki at thide
    hide natsuki
    scene bg bedroom_night
    with wipeleft_scene
    "We go up to the bedroom, and start getting ready for bed."
    "I slide in, then Natsuki turns off the light and cuddles next to me."
    mc "Good night, Natsuki."
    "I say as I embrace her."
    n "Good night, [player]."
    scene black
    with fade
    pause(1)
    return
    
    #End scene 5b
