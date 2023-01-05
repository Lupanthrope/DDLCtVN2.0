label Monika4:
    stop music fadeout 2.0
    play music t2
    scene bg bedroom
    with dissolve_scene_full
    #Delete before release =================================
    $ MonikaVar = 0  #This is here to test things
    #=======================================================

#C1
    "Another morning has me waking up bright and early for school."
    "I stretch my arm over to my nightstand, tapping around where I left my phone to silence the alarm."
    "With enough blind flailing, the alarm finally stops so I turn back in my sheets."
    "Even in the comfort of my bed, it feels as if something is missing."
    "I look over to the other side of the bed, which has been left empty for the night."
    "A smirk creeps across my face as the memory of those special nights comes flooding back."
    "I never thought a night of sleep wouldn't be complete without someone else sharing my bed with me."
    "Never thought I'd really be dating a class star like Monika either, but I really had struck gold with her."
    "With a smile on my face I get up throwing on my uniform to start the day."
    scene bg kitchen
    with wipeleft_scene
    "I decide a quick breakfast would hold me over until lunch today."
    "These muffins I picked up yesterday should do the trick"
    "Looking over to the clock on the wall, it seems I'm running ahead of schedule."
    "Good, no need to rush then."
    "I might even catch Sayori walking to school. For awhile I haven't been able to catch up with her."
    "Usually I try and meet up with Monika in the morning, but today she had to meet up with a friend."
    "Hopefully I haven't missed my chance to catch up with Sayori."
    scene bg residential_day 
    with wipeleft_scene
    "The cool morning air mixed with the warm rays of sun help jumpstart my legs for the day."
    "Looking to the street I see different groups of students, but no red bow in the crowd."
    "I turn my gaze to the house adjacent mine just in time to see the door swing open"
    show sayori 1k at t11 zorder 1
    "Sayori starts to trudge toward her house gate, her eyes fixed on the ground ahead of her."
    "She'll walk right past me if she keeps that up!"
    show sayori 4n at h11
    mc "SAYORI!"
    "I shout waving my hand in the air running toward her, trying to get her attention."
    s 4m "[player]?!"
    s 1o "What are you doing up so early?"
    show sayori 1n
    mc "I could ask you the same question silly."
    s 2l "Well uh... {w=.75}I uhhh.."
    s 5a "I need to eat breakfast early...{w=.25} and I just happened to finish early."
    s 5b "Ehehe..."
    mc "Well, I guess I got lucky seeing you then."
    "I won't call her on the weak bluff just yet, it's much too early in the morning anyways."
    s 4r "Yeah!"
    s 1l "What about Monika though, isn't she waiting for you down the street?"
    show sayori 3b
    mc "No actually, she had to catch up with a friend. It's just us two like old times."
    s 2l "Yeah, just like old times..."
    show sayori 1b
    mc "Hey, I got something for you actually."
    show sayori 4n
    "I hand her the extra muffin I had brought with me."
    s 2r "You didn't have to [player] ehehe!"
    show sayori 1q
    mc "Well I thought you would enjoy it. It's even your favorite type."
    s 3m "Oh my gosh it's chocolate chip!"
    show sayori 3q
    "She devours the muffin as we walk to school."
    "Her enthusiasm in eating makes me wonder if she did actually eat breakfast this morning."
    s 1y "You really are too nice to me [player]."
    mc "What are best friends for Sayori."
    s 1l "Yeah...{w=.75} ehehe..."
    show sayori 2e
    mc "Sayori are you alright, you seem off today."
    s 2x "Of course I'm fine."
    show sayori 1q
    "She beams a bright smile at me, but I've seen that smile once before."
    mc "Seriously Sayori, is-{nw}"
    s 4p "Aaah! I almost forgot!"
    s "I need to talk to my teacher before class starts!"
    s 5a "Sorry [player], I gotta go!"
    s 2r "See you at the club!"
    show sayori at lhide zorder 1
    hide sayori
    "And like that, she runs off onto the school grounds."
    mc "Sayori wait!"
    "But she's already too far to hear me."
    mc "Damn it Sayori..."
    "What has gotten into her?"
    scene bg schoolgates 
    with wipeleft_scene
    "By the time I make my way onto the school grounds, she's nowhere to be seen."
    "The morning crowd is too thick with students to pick her out."
    "I guess it wouldn't hurt to get to my class a little early as well."
    "Start this day on the right foot."
    "Before I can even move however, a pair of arms wrap around me from behind."
    m "Hi [player]~"
    show monika 5a at l11 zorder 4
    "Monika swings around to my front, glowing a light shade of pink."
    mc "Good morning Monika~"
    show monika 1j
    "I pull her into a hug and give her a peck on the cheek"
    m 3l "Gosh [player], you don't have to make such a scene."
    show monika 2m
    mc "Hey, you started it. I'm just returning the favor."
    m 4n "I guess you got me there. Ahaha."
    m 5a "I just get really excited when I see you, I can't help it sometimes."
    mc "Well I'm glad I was here in time to see you before class."
    show monika 2c
    mc "By the way, did you get to see that friend of yours?"
    m 2d "Oh that, yeah I saw them already."
    m 1i "But that doesn't matter right now."
    show monika 2h
    mc "Oh uh.. {w=.5}sorry I brought it up then."
    m 3i "Yeah, the only important thing right now is..."
    m 4k "That you're here. Ahaha~"
    show monika 2j
    "Monika seemed pleased with her acting."
    show monika 1f
    "My worry must have been written all over my face, however."
    m 2g "I didn't make you nervous did I [player]? I'm sorry."
    show monika 2f
    mc "It's alright Monika, just hard to tell when you're teasing and when you're being serious about something."
    m 4n "I'll try to keep the teasing to a minimum then, ehehe."
    show monika 2m
    mc "You just wouldn't be the Monika I know without it though."
    m 5a "You're so sweet [player]."
    show monika 1j
    "She leans over and gives me a quick kiss before grabbing my hand."
    m 2b "Come on, we'll be late if we stay here."
    show monika at thide zorder 1
    hide monika
    scene bg class_day
    with dissolve_scene_full

#C2
    "After a long day of classes, hearing the sweet chime of the final bell was a breath of relief."
    "I take my time packing my notebooks and wait for the rest of the class to leave."
    "Looking to the door, I hope that Sayori might be waiting outside."
    "Just like old times."
    scene bg corridor
    with wipeleft_scene
    "Seems my hopes were for naught, as she is nowhere to be seen."
    "Well if she's not here she must be at the club right?"
    "I start my long walk up to the clubroom past the exiting students."
    "On my way up the stairs I come across a trio of girls conversing in the corner of the stairwell."
    "As I approach closer, one of the three turns and looks directly at me."
    "I hear a faint {i}\"that's him\"{/i} as she turns back around."
    "By the time I'm only a few feet away, all three are staring directly at me."
    "I nod as a greeting and continue up the stairs."
    "Even as I walk however, I can feel their gaze burn holes into my blazer."
    "Whatever their deal is, I want no part in it."
    "I've got a club to go to."
    with wipeleft_scene
    "Finally, the clubroom door comes into sight."
    "Coming up to the door, I can faintly hear voices coming from the clubroom."
    "I slow down to a tiptoe and crouch just below the door window so no one on the inside would know I'm there."
    n "{i}Sayori what are you trying to do there?{/i}"
    s "{i}I'm gonna scare the next person who comes in!{/i}"
    y "{i}Sayori! What if a teacher walks in! W-we would get in so much trouble!{/i}"
    s "{i}I know what I'm doing, trust me! It's gonna be super funny!{/i}"
    y "{i}O-oh dear, I have a bad feeling about this...{/i}"
    n "{i}Whatever, I'm goin' back to the closet.{/i}"
    "So Sayori wants to lay a trap for me huh?"
    "Well Sayori, the game is on and you're playing on my terms."
    "I crouch-walk to the other side of the door and grab a hold of the door handle."
    "Deep breath [player]."
    "Sliding the door open, I stay low by the door just out of sight."
    s "RAAA-{w=1.25} wait...{w=.5}Who's there?"
    "And she took the bait, hook line and sinker."
    scene bg club_day
    with wipeleft_scene
    show sayori 4m at t11 zorder 4
    mc"RRAAAAHHHHHHHWWWWW!"
    s 4p "AAAAHHHHHH!"
    show sayori 1p at s11 zorder 4
    play sound fall
    "Sayori jumps straight into the air and lands flat on her butt."
    s 3w "Ow!"
    show sayori 1u
    mc "Oh my god Sayori, I'm so sorry, I didn't mean to make you jump like that."
    show sayori 1v
    "I quickly drop to my knees to see if she's hurt."
    s 2w "H-how did you know I was there [player]?"
    show sayori 1u
    mc "I {w=.75}kinda heard you talking to the others through the door."
    s 2l "Oh...{w=.75}ehehe..."
    show sayori 1e at t11
    "I reach my hand out to her and gingerly help her back to her feet, wiping the tears from her eyes."
    s 1y "I'm sorry for trying to scare you [player]."
    mc "I'm sorry I scared you that bad Sayori."
    mc "Should have just let you have your laugh.."
    show sayori 1d
    "I pull her into a hug of reassurance."
    s 2l "Yuri was right, this was a bad idea ehehe!"
    show sayori at thide zorder 1
    hide sayori
    show natsuki 4z at t21 zorder 3
    show yuri 3n at t22 zorder 3
    "Looking over Sayori's shoulder I could see Yuri and Natsuki looking over the scene."
    "Yuri had a look of pure shock across her face while Natsuki was laughing so hard she was propping herself up with a desk."
    show 2y natsuki at f21
    n "Ahaha! Oh man [player] you got her {i}good!{/i}"
    show yuri at f22
    show natsuki t21
    y 2p "N-natsuki this isn't funny! Sayori got hurt!"
    show natsuki 2w at f21
    show yuri 2o at t22
    n "Oh it's not that bad, she just fell over."
    show yuri 4d at f22
    show natsuki 3g at t21
    y "B-but what if she hurt her tailbone, or bruised something when she fell, or what if..."
    show natsuki 3c at f21
    show yuri 4b at t22
    n "Well she seems to be standing fine, so it can't be that bad."
    show yuri 4a at f22
    show natsuki 3j at t21
    y "I{w=.25} suppose your right Natsuki."
    show yuri 1f at t22
    show natsuki 1k
    m "Am I interrupting something?"
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri

#C3
    show monika 1f at t11 zorder 4
    "Turning to look behind me, I see Monika standing in the doorway."
    m 2g "If you two need a minute, I suppose I can wait."
    show monika 2c
    mc "No, no it's fine Monika."
    show monika 1e
    "I let go of Sayori and grab both of Monika's hands, pulling her into the clubroom."
    mc "We were just uh, pulling pranks on each other and Sayori fell down and bumped herself."
    show monika 2e at t21
    show sayori 5d at t22
    show sayori at f22
    s "It was still [player]'s fault though.."
    show sayori 5d at t22
    mc "You were gonna jump up and scare me first!"
    show sayori 5b at f22
    s "Ehehe..{w=.75} well I um.."
    show sayori 1d at t22
    show monika 4n at f21
    m "Whatever the case was, we really shouldn't be getting each other hurt over silly things like this."
    m 2l "I'd rather not have to send anyone to the nurse over a prank gone wrong in a literature club."
    show monika 2e at t21
    show sayori 2h at f22
    s "Sorry Monika, it won't happen again."
    show sayori 1d at t22
    mc "Yeah, we're sorry."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show yuri 1i at t21
    show natsuki 5c at t22
    show natsuki f22
    n "Jeez, what a bunch of pushovers."
    show natsuki 3g at t22
    show yuri 2h at f21
    y "Natsuki, apologizing for making a scene doesn't make you a pushover."
    show yuri 2e at t21
    show natsuki 3h at f22
    n "Still, why does [player] make it sound like they commited a huge crime."
    n 5q "It's just dumb."
    show yuri 2g
    show natsuki 5s
    m "Come on guys, let's get started on our pieces for the papers!"
    show natsuki 3q at f22
    n "Why did I ever agree to this paper thing, I'd rather just read right now."
    scene bg club_day 
    with wipeleft_scene
    "After a bit of writing I leaned back in my seat, taking a moment to stretch my arms out."
    "This new poem I had in mind wasn't translating to paper as well as I thought it would."
    show sayori 2c at t11
    s "You doing alright there, [player]?"
    show sayori 2b
    mc "Yeah I'm fine, just some writer's block."
    #11111111111111
    s 3c "Me too, Mr. Sun is being too bright today."
    show sayori 3b
    mc "Mr. Sun?"
    s 2r "Yeah! Look how bright this light is!"
    show sayori 1q
    "Sayori points down to her desk, which is coated in sunlight from the window."
    s 2l "He looks so happy out there, letting all that light in here."
    show sayori 1b
    mc "It has been a nice day out today, too bad we were stuck in here all day."
    s 2x "But we get to walk home soon though!"
    s 4r "We can enjoy some of it then, on our way home."
    show sayori 1n at h11
    m "We could, right [player]?"
    show monika 1a at l21
    show sayori 1y at t22
    "Monika seemed to magically appear next to us, moving a chair over and sitting beside me."
    m 4k "It's such a nice day for it, I can't wait!"
    show monika 1j
    show sayori 1d
    "She shifts closer to me in her chair as she says this, leaning her body against mine."
    mc "W-well yeah of course, I can't either."
    show monika 1a
    show sayori 1y
    "Monika takes my half finished poem in her hands and starts to look over it."
    "Sayori seems to shrink in her chair, fidgeting with her pencil."
    m 3b "It's coming along great [player], but maybe this here should be a bit more dramatic."
    show monika 2b
    mc "Thanks, I'm still trying to figure out what I really want to convey this time."
    show sayori 2e
    mc "Sayori, why don't we look at yours? Maybe it could help both of us out of this block."
    if SayoriVar > 2:
        show sayori 2l
        s "Oh, uh.. sure [player]."
        s 1h "Though it's probably not much compaired to what you have.."
        show sayori 1g
        mc "I'm sure it's plenty, come on."
        show sayori 1y
        "Sayori slides over her rough draft, a sweet intro of a poem that morphs into doodles halfway down the page."
        mc "It's good, I can't wait to read the rest when it's done."
        s 2s "Thanks, even if you don't mean it!"
        show sayori 1q
        mc "I do though!"
        "Sayori chuckles to herself as she takes the poem back."
        show sayori 1b
        show monika 1c
        mc "Say, why don't we all walk home together today?"
        m 4n "Oh, that would be.. fun, yeah!"
        show monika 1e
        s 3m "Really? You two wouldn't be bothered?"
        show sayori 2e
        mc "Of course not, we're all friends here!"
        m 2k "Yup!"
        show monika 2j
        "I could feel Monika push herself harder onto me as she said that."
        show sayori 4x
        s "Well, alright. If you two say so!"
        show sayori 4q
        "Sayori beamed at us and I couldn't help but smile a little too."
    else:
        show sayori 2h
        s "N-no I'm sure it's not really good enough for that."
        s 3l "It's just some disconnected scribbles, I wasn't really focused at all."
        show sayori 1y
        "Sayori quickly snatched her paper up and out of reach from us, holding it to herself."
        m 4e1 "Well, even if you're not comfortable sharing yet, I'm sure it's great."
        show monika 2e
        s 1l "T-thanks Monika.."
        show sayori 1b
        show monika 1c
        mc "Hey, why don't we all enjoy a bit of Mr. Sun after club together?"
        s 2e "Well I uh.. I don't know.."
        m 4g "I thought we were going to-{w=.75}{nw}"
        show monika 2f
        mc "Come on, it'll be fun! Please Sayori?"
        show monika 1c
        "I take Monika's hand into mine and give it a little squeeze. Please trust me on this one."
        show monika 1e
        s 2l "Well okay, if you want I can come with you two."
        show sayori 1d
        mc "Great, it'll be a nice change of pace."
        m 3k "Yeah, it'll be nice!"
        show monika 1j
        "Monika dug herself deeper into my side as she said that."
        "I silently pray that it will be a good time and not a nightmare."

#C4
    scene bg residential_day 
    with wipeleft_scene
    show monika 1a at t43
    show sayori 1a at t31
    "With the club finally over we started our walk."
    "Monika stayed close by my side while Sayori kept a small but noticeable distance from us."
    "Most of the conversation had consisted of the newspaper and different opinions we had heard about the latest issue."
    "Looking down the street, a small light caught my attention."
    show monika 2c
    show sayori 2n
    mc "Hey you two, do you see that light over there?"
    show sayori 2m at f31
    s "Oh wow, that's really bright [player]!"
    show monika 4d at f43
    show sayori 1b at t31
    m "It must be something reflecting the sunlight."
    m 2b "Let's go see what it is!"
    show monika 1a at t43
    show sayori 1a at t31
    "Monika tugs on my arm and we all head in the direction of the shining light."
    scene bg residential_day
    with wipeleft_scene
    "Getting closer to the source of the light reveals more than just a shiny street sign."
    "Tables line the sidewalk covered in a range of different items, with colorful signs promoting low prices on everything we see."
    "An old man sits by the gate of the house the tables are in front of, an umbrella set over him to provide shade."
    "He silently greets us as we approach his wares."
    show sayori 1n at t11
    "Sayori's attention had been focused on the light that we had followed."
    "A shiny chrome toaster sat angled on one of the outer tables, just in a way for the sun to bounce off it's surface."
    s 4c "[player], come look at this!"
    show sayori 4q
    "Sayori grabs the toaster and turns to me and Monika."
    mc "S-sayori! Careful with that!"
    show sayori at t31
    show monika 4n at f43
    m "We don't want to break any of this man's things."
    show sayori 4r at f31
    show monika 2m at t43
    s "I know guys! I'm being super careful, I promise!"
    show sayori 4q at t31
    "Putting the toaster down, she wanders off to look at another table."
    show sayori at lhide
    hide sayori
    show monika 4l at t11
    m "We should probably keep an eye on her [player]."
    m 2n "Don't want her breaking anything behind our backs ahaha~"
    show monika 2e
    mc "Yeah I'd rather not have to pay for anything we don't want."
    m 3d "There's so much here too, I wonder what we could find."
    show monika 1a
    mc "Well let's browse around, we don't need to be anywhere soon right?"
    m 4l "Even if we did, I don't think Sayori would have cared ahaha~"
    m 5a "Ooo these look interesting."
    show monika at lhide
    hide monika
    "Monika lets go of my hand and wanders over to a couple of tables covered in an assortment of clothing."
    "I suppose I should take a look around as well."
    "I'll start from the opposite end and work my way down."
    "I take quick peaks between the items and Sayori on the way down."
    show sayori 2r at panic
    "She's quickly bouncing between tables to see everything, and luckily nothing has broken."
    show sayori at thide
    hide sayori
    "Turning my attention away from her I spot a table covered in jewelry."
    "Looking closer I spot a golden necklace that seems to glow at me."
    "It has a single charm, an emerald colored gemstone set in a gold trim."
    "The price he has here isn't too bad either."
    "Making sure Monika isn't looking, I grab the necklace and the box it comes with."
    "I'll check out the rest of the sale and then purchase this."
    "Looking back to the last table in the row, and something odd sticks out to me."
    "I see the top of a large bag leaning against the fence."
    "As I draw near it's not just a bag, but an aging guitar case."
    "I drop down to one knee and brush some of the dust off."
    "The case seemed solid, even with the signs of a long life sitting neglected in a closet somewhere."
    "Finding the zipper, I open up the main compartment."
    "Inside lies a pristine-looking acoustic guitar, as if time had not reached inside it's case."
    "I pull the guitar from its resting place, handling it like a glass sculpture."
    "Even the body still has-{nw}"
    $ n_name = "???"
    n "Found something you like young man?"
    mc "Gah!"
    "I had been so focused on the guitar the voice had made me jump."
    "Looking over to the source of the scare, the old man stands over me seemingly just as shocked as me."
    $ n_name = "Old Man"
    n "Oh I'm so sorry to startle you young one. My apologies."
    mc "I-its alright sir, just didn't hear you walk up to me."
    "He nods and smiles."
    "Motioning to the guitar in my hand, he begins again."
    n "It's been well taken care of, just has not seen the light of day for quite some time."
    mc "Why is that sir?"
    n "It was my son's. He's long since grown up and purchased another."
    n "He used to play for many hours, it was his calling as I liked to think."
    mc "Are you sure he wouldn't want it back?"
    n "I am sure of it. I've asked him many times, says it's gotten too old for him."
    mc "I suppose so, if he's bought something new for himself."
    "Still, wouldn't you want to keep something like this?"
    "I continue to look over the guitar, moving up the strings."
    "Coming to the top, something catches my eyes."
    "A heart with an {i}M{/i} at its center is carved into the wood in the center of the many different knobs that hold the ends of the strings."
    "I run my thumb over the engraving subconsciously."
    n "Oh, I almost forgot about that. I'm so sorry if that changes your mind about it."
    n "My son had that done when he was still dating his wife."
    n "Many nights he would play endlessly for that girl."
    n "Match made in the stars really, I couldn't have seen him marrying any other girl than that one."
    n "I can understand if you do not want the guitar because of that mark young one."
    mc "Actually sir..."
    "I look over to Monika."
    "She was still looking through the clothes the man had for sale."
    "Just seeing her made me smile, the sun perfectly landing on all the right places."
    "She really did enjoy learning piano."
    "I wonder how difficult it would be."
    n "Ah, so her name starts with an M as well?"
    mc "Yes sir."
    n "She seems like a good girl young man."
    n "Maybe being a father once has let me have that insight."
    "He chuckles to himself."
    mc "Yeah, she really is something."
    n "Well, stay the course and everything will go just fine."
    "He claps me on my shoulder, and we both have a laugh."
    "I think I've made up my mind."
    mc "So, about the guitar."
    n "Ah yes."
    "He then gives me a price much lower than I had anticipated."
    mc "A-are you sure sir? That seems far too cheap."
    n "I'm sure of it."
    n "I'm not concerned about the money young man."
    n "It's more about cleaning out this house of mine."
    "With a price like that, how could I say no?"
    "Even if I don't end up learning the guitar, I could sell it off for a good price."
    "But I'm going to learn it."
    "For her."
    mc "Well sir, you have yourself a deal."
    mc "Oh, and also this here."
    "I pull the necklace from my blazer's pocket."
    n "Ah, trying to steal from me now?"
    mc "N-no sir, I-{nw}"
    n "I know young man, I was watching the whole time!"
    "He chuckles again while I try to recompose myself."
    "He leans into my ear and whispers."
    n "That necklace will serve as a fine gift."
    n "She'll love it."
    "He pulls away and smiles."
    mc "Thank you sir."
    "I pay for the guitar and necklace and we shake hands."
    show monika 2b at t11
    m "Hey [player],{w=.5} I'm all-{nw}"
    m 4d "Oh wow, what's that?"
    show monika 3b
    "She points to the large guitar case."
    show monika 2c
    mc "Well actually, it's a guitar Monika."
    mc "I think I'm going to try learning it."
    m 4b "Wow really?! You're going to learn guitar?!"
    m 2k "That's great [player]!"
    m 5a "I can't wait to see what you can do."
    show monika 2c at t22
    show sayori 4n at l21
    show sayori at f21
    s "Whoa, what's that [player]?"
    show sayori 1o at t21
    mc "It's a guitar Sayori."
    show monika 2a
    mc "This nice gentleman gave me a great price on it."
    show sayori 4m at f21
    s "So your going to learn it?!"
    s 3r "That's super cool [player]!"
    show sayori 1q at t21
    mc "Yeah, hopefully it's not too difficult."
    mc "Well I'm all set, did you two find anything?"
    show monika 3b at f22
    m "Actually I did!"
    show monika 1a
    "She lifts up a couple different new outfits from her arms."
    show sayori 1y
    mc "They look great Monika."
    m 5a "Thanks [player]."
    "She gives me a peak on the cheek before reaching into her school bag."
    show monika 2a at t22
    show sayori 1a at t21
    "The old man looks over to me for a moment and chuckles."
    n "Well young lady I hope you find them comfortable and stylish."
    m 3b "Thank you sir."
    show monika 2c
    s 2l "I didn't find anything I liked ehehe~"
    mc "Well that's alright Sayori. Besides, the fun in yard sales is you never know what you may find."
    s 4r "Yeah! You never really know ehehe~"
    show sayori 1a
    show monika 2a
    "With Monika's things paid for, we all thank the old man."
    n "Any time young ones, thank you for stopping by."
    "We wave as I pick up my new guitar and start off down the road."
    $ n_name = "Natsuki"
    scene bg residential_day
    with wipeleft_scene
    "As we reach our houses, Monika turns to me and Sayori."
    show monika 5a at t11
    m "I'm so glad we all decided to walk together."
    show monika 2a at t22
    show sayori 2x at f21
    s "Yeah, it was so much fun!"
    show sayori 1a at t21
    show monika 4b at f22
    m "Well I gotta keep heading this way."
    m 5a "I'll text you later [player]~"
    mc "I'll be waiting Monika."
    show monika lhide
    hide monika
    show sayori 1d at t11
    "With a quick kiss she's back to walking down the road, whistling a tune as she goes."
    "Turning my attention over to Sayori, I see her watching Monika go with a somewhat pained expression."
    mc "Something on your mind Sayori?"
    s 1b "Hmm?"
    s 2c "Oh it's nothing."
    show sayori 1e at t11
    mc "Sayori seriously, is something on your mind?"
    s 1y "N-no, it's fine. Really."
    s 3s "I was just thinking how cute Monika was ehehe~"
    s 3l "She really is lucky to have someone like you [player]..."
    show sayori 1d
    mc "Well.. thanks Sayori, that means a lot."
    show sayori 2y
    mc "I'm also lucky to have a friend like you."
    s 2d1 "Me too, [player]."
    s 4s "Now go learn that guitar! I wanna hear you play a pretty song!"
    show sayori 1q
    mc "It's going to be a while before I can play anything like that Sayori."
    s 2x "I can wait, just make sure it's super good [player]!"
    s 4r "See you tomorrow!"
    show sayori at lhide
    hide sayori
    "And with that she skips off to her house."
    "I watch her make it to the door before I sigh and make my way into my own home."
    scene bg living room
    with wipeleft_scene
    "Setting my book bag down next to the door, I take a seat on the couch and place the guitar case at my feet."
    "Opening the case once again, I take my new instrument in my hands."
    "Rummaging through the rest of the case I find a stash of guitar picks."
    "Taking one in my hand, I set it just above the strings and strike it across."
    #play sound "mod_assets/openstrum.ogg"
    "The sound echoes through the house."
    "An eager smile grows across my face."
    "You can do this [player]."
    "Setting the guitar down, I pull out my phone in search of online tutorials."
    "A new message from Monika appears, saying she got home safe and sound."
    "The rest of the day is spent flipping between talking to her and surfing the web for this new endeavor."

#C5
    scene bg kitchen 
    with dissolve_scene_full
    stop music fadeout 1.0
    play music t6
    "With the rest of the week behind me Sunday has finally rolled around."
    "Monika had asked me to get up extra early today, said we had to tackle the day as soon as it started."
    "She knows I'm not a morning person on the weekends, these are the days I can sleep in a bit!"
    "Why does she insist she comes over as the sun rises?"
    "I'm having trouble choosing something to even eat for breakfast."
    "I had ended up using twice as many muffins than I had hoped, as Sayori was keen on eating one every morning."
    "Without those, I'm at a lose at what to eat."
    "Just as I open the fridge for a second time, I hear a knocking at the door."
    scene bg livingroom
    with wipeleft_scene
    mc "No one is home."
    m "Very funny [player], come on open the door."
    m "Please~"
    mc "I'm coming, I'm coming don't worry."
    show monika 3ba at l11 zorder 4
    "Opening my door, Monika immediately steps in and gives me a kiss."
    "With her is a long canvas bag in her hand and her school bag slung over her shoulder."
    "She also has a cardboard tray with two cups sitting side by side."
    "I catch a glimpse behind her and see a parked in front of my house, her dad's hand waving out of the window to us as he pulls away."
    show monika 3bc
    "I offer to take the long bag from her and nearly dropped it as it hit my hand."
    "This thing weighs a ton!"
    mc "Monika, what do you have in here?!"
    m 4bl "It's my piano! I thought it would help with today."
    show monika 4bc
    mc "Is that why your dad brought you this time?"
    m 4bl "Well yeah, how else would I have gotten it here?"
    show monika 3be
    mc "Magic spells I would guess? Come on in."
    m 3bl "Spells? I'm not a witch silly."
    show monika 1ba
    "I lead her inside, setting her piano down in the living room."
    "She places her school bag on the couch and the tray on the coffee table."
    m 4bb "We stopped at a cafe on the way here to grab some coffee and I got some for the two of us!"
    m 2bl "They had a special on this really tasty sounding iced coffee, so I got that."
    m 1bn "I probably should have asked you what you would have wanted rather than just picking for you, sorry [player]."
    show monika 2bm
    mc "It's fine Monika, if you think it will be good I trust your judgement."
    mc "Besides I've always liked an iced coffee over a hot one."
    m 1bk "Well I hope I got the best one there for you then!"
    show monika 1bj
    "I give her a quick kiss and take one of the cups that looks to be more full."
    "A rush of caffeine mixed in caramel and cream spreads over my taste buds as I take my first sip."
    show monika 2ba
    mc "Wow, this is really good!"
    mc "See, I knew I could trust you."
    m 3bk "Aww thanks~"
    show monika 2bc
    mc "Still, this would go really well with something to eat."
    mc "I haven't even had breakfast yet."
    m 4bn "Actually, me neither [player]."
    show monika 1bo
    mc "You didn't? That's not like you at all."
    m 1bp "I know, I just really wanted to get here and I forgot all about it."
    m 3bn "Even when I was at the cafe I didn't even think to grab anything."
    m 3be1 "Maybe we could...{w=.5} share some together?"
    show monika 1be
    mc "You know, that sounds like a wonderful idea Monika."
    m 2bb "Really? I'm so glad you think so!"
    scene bg kitchen 
    with wipeleft_scene
    show monika 1bj at t11
    "We both go into the kitchen in search of what to make for breakfast."
    "I still have no idea what we should eat though."
    "Plus the thought of sharing breakfast with Monika makes me a bit anxious."
    "Should I try and do something special or just a simple regular one."
    "Would it even matter to her?"
    menu:
        "Well, I suppose I should do a..."
        "Simple Breakfast":
            "Something easy would be nice, I think."
            "We could get to the rest of the day sooner anyway."
            "I look to the cupboards and find my supply of cereal."
            "This will work."
            show monika 1bc at t11 zorder 4
            mc "Hey Monika, how about cereal?"
            m 4bl "Well it's not what I had in mind but I suppose I'm not opposed to it."
            mc "Oh, well I mean we could do something else."
            m 2bd "It's fine, really [player]"
            m 4be "It's more about spending the time together anyway."
            m 4bk "Anything I do is better when your around!"
            show monika 2bj
            mc "Alright, if you say so."
            m 3bb "I know so."
            show monika 3ba
            "I chuckle to myself and grab an assortment of boxes to offer her."
            show monika 1bj
            "Making two bowls, we sit together at the table."
            "Monika moved her chair extra close to mine, but I don't really mind."
            "Just her presence brings a little smile to my face."
            "Even the seemingly boring event of eating cereal is made into something enjoyable with her."
            show monika 1bb
            "It's mostly quiet, with small conversations popping up here and there."
            show monika 1ba
            "Once we're done, we head back into the living room."

        "Elaborate Breakfast":
            #$ MonikaVar += 1  <-- We'll wait on that
            "Yeah, I should do something special for her."
            "Simple enough to pull off and do well enough to impress her."
            "I open the fridge yet again and spot my carton of eggs."
            "Yeah, these should work."
            show monika 1bc at t11 zorder 4
            mc "Hey Monika, how does an omelet sound?"
            m 4bb "That sounds great [player]!"
            m 2bk "We could even make them together!"
            m 2bb "I even know a really good recipe we could try."
            show monika 1ba
            mc "Well you've surprised me once already today, so I'm interested."
            m 2bb "I know you'll just love it!"
            m 3bn "If we have all the ingredients we need that is."
            show monika 2bm
            mc "Well, lets see what I've got in stock."
            show monika 1ba
            "Looking through my fridge and cupboards, we surprisingly manage to find everything we need."
            "Monika has her recipe pulled up on her phone for reference."
            "It's an omelet filled with veggies, not my first choice but it couldn't be too bad."
            "Besides, she wouldn't even eat a typical French omelet I would have made."
            "That special diet of her's wouldn't allow it."
            "She does have some unique choices for meals however, and trying them is always an adventure in and of themselves."
            show monika 1bb
            "The kitchen is transformed into a whirlwind of movement as we work our way through the recipe."
            "After a while of cooking eggs and cutting vegetables, the omelets are complete."
            m 3bb "Wow, they look amazing!"
            m 3bk "Good work [player]!"
            show monika 1bj
            mc "You too Monika, I couldn't have done it without you."
            m 2bk "Your welcome! It was really fun cooking with you [player], we should do this more often."
            show monika 1ba
            mc "Yeah, this was really fun. I'm gonna look forward to it."
            mc "These things smell delicious, let's eat! I'm starving!"
            show monika 1bj
            "Monika laughs as we set the two meals on plates and make our way to the table."
            "She places her seat extra close to mine, but I don't mind it."
            "The omelet tastes incredible, different from my usual choices but delicious nonetheless."
            "Even without meat, she really can make a great meal."
            "Finishing up breakfast and finding that much more time had gone by then we had thought, we head back into the living room."
    scene bg livingroom
    with wipeleft_scene
    show monika 1ba at t11
    "As we make our way back Monika beats me to the couch and takes a seat."
    show monika 1bb at s11
    m "So [player], have you been practicing your guitar?"
    show monika 2bc
    mc "Well uhh..."
    show monika 1bh
    mc "To be honest with you Monika, I haven't really touched it."
    show monika 2bf
    mc "Between homework and stuff I haven't found the time, and I can't seem to find good enough lessons online."
    m 3be "Well today I think you should try and learn a bit."
    m 2bk "And your girlfriend will help you do that!"
    show monika 2bj
    mc "Is that why you brought your piano?"
    m 4bk "Yup! I think I could use it to help!"
    m 1bn "And it would be fun to just play for you a bit ahaha~"
    show monika 2bm
    mc "Well I'm always up for listening to you play, you really are a talented player."
    m 4bn "Your too sweet to me [player], now go grab your guitar so we can start."
    show monika 2bl
    mc "Well excuuuse me princess."
    show monika 1bj
    "Giving her a peck on the forehead, I head up to my room."
    scene bg bedroom
    with wipeleft_scene
    "Now where did I put this thing?"
    "Not under the bed."
    "Not next to my desk."
    "Not in the closet."
    "Where the actual-{nw}"
    "Oh here it is, propped up near my door."
    "Grabbing it, I head back downstairs to Monika."
    scene bg livingroom
    with wipeleft_scene
    show monika 1bj at t11 zorder 2
    "Stepping back in the living room I find Monika setting up her piano in front of one of the kitchen chairs."
    m 4bb "Ah, there you are [player], What took you so long?"
    show monika 2bc
    mc "Couldn't find my guitar for a while, forgot where I put this thing."
    m 3bl "Well at least you found it ahaha~"
    m 2bn "Wouldn't want to be the odd one out here."
    show monika 2bm
    mc "I wouldn't mind a little piano show."
    m 4bl "Hey, this is about you today, not me!"
    show monika 1ba
    "I take a seat on the couch and start to take the guitar out of its case."
    m 3bb "So you haven't really found any good lessons right?"
    show monika 1ba
    mc "Nope, not a single one."
    m 4bk "Well I may have a solution to that!"
    show monika 1ba
    "She reaches into her bookbag and pulls out a large softcover book."
    m 3bb "A friend of mine from the debate club actually learned guitar once and used this book."
    m 2bb "He said that the book plus the disc inside helped him a lot."
    show monika 2ba
    "I take the book in my hand and a small CD in a plastic sleeve falls into my hand."
    "The book seems well used, with the edge of the pages folded and fraied from use."
    "Turning to the inside cover I see the name of Monika's friend scribbled into the paper."
    "I smirk, either I'm gonna be thanking this guy for the help or cursing him for lending Monika a terrible lesson plan."

#C6 - Actually learning some stuff
    stop music fadeout 1.0
    play music tmonika 
    "Picking up the book and DVD from the floor I make my way to my TV."
    "Opening the tray on my player I take the DVD out of the sleeve and place it in the groove."
    "With a few beeps from the aging machine the program starts to appear on the screen."
    m 2bb "Hey it works!"
    show monika 4ba
    "Monika grabs my remote from beside her on the couch."
    m 4bb "Let's find the first lesson."
    show monika 3ba
    "With some scrolling through the many menus the disk had, she finally finds the first set."
    m 2bi "Huh, {i}Tuning your Guitar{/i} is the first lesson."
    m 2bl "Well that is an important part ahaha~"
    m "Why didn't I think of that."
    m 1bd "[player], did that guitar come with a tuner at all?"
    show monika 2bc
    mc "Can't say I've seen one in here, let me check again."
    "Rummaging through the case again, I find an odd looking device with a clip on one end."
    mc "This thing?"
    m 4bb "Yeah! That's perfect!"
    show monika 2ba
    "I turn the device on as Monika begins the video on the TV."
    "A man with a guitar appears on screen and greets the camera."
    "After a short quip about the book and the program as a whole, he points our attention to the first section of the book."
    "Unsurprisingly the section is titled {i}Tuning your Instrument{/i}."
    "The instructor continues on about the importance on tuning and how this controls the sound of the instrument."
    "He then invites us to play a chord without using our fingers on the neck to compare how our guitar sound to his."
    "Pick in hand, I strike it down the strings."
    #play sound "mod_assets/openstrumoot.ogg"
    show monika 2bl
    "The sound is wildly different from the sound the instructor plays."
    "Monika giggles as the sound reverberates through the room."
    m 2bn "Sorry sorry! It was just too funny."
    show monika 2bm
    "It even got a chuckle out of me because of how bad mine had sounded compared to the instructor's."
    show monika 1ba
    "Focusing back to the TV the instructor points to a device just like mine that now sits clipped to the head of his guitar."
    "The tuner can supposedly listen when a single string is played and tell whether the sound is too low, too high, or on key."
    show monika 2bc
    "He also points out that if I found myself without a tuner in hand, I could possibly use another instrument to tune."
    "He notes that the piano is an excellent reference if one is available to use."
    show monika 1bb
    "I could see Monika's face light up at the notion."
    m 4bb "We should definitely do that [player]!"
    show monika 1ba at s11
    "She quickly pauses the video and takes a seat at her piano."
    show monika 1bc
    mc "Monika, hold on a second."
    m 1bd "Hmm? What's the matter?"
    show monika 1bc
    mc "Do we even know what notes we are supposed to match on there?"
    m 2bn "Gosh your right ahaha~"
    m 4bl "I'm really getting ahead of myself here."
    m 1bn "Sorry [player]."
    show monika 1bm
    mc "It's alright, besides I'm glad your enthusiastic about all this."
    mc "It's just the motivation I need."
    m 4bk "I'm glad we're both on the same page ahaha~"
    show monika 3ba
    "Monika picks up the remote and resumes the video."
    show monika 1bc
    "The instructor starts to demonstrate how he sets up his tuner."
    "I try to follow along as best I can, we don't have the exact same one but they're pretty similar."
    "Once that's done he points to the top, thickest string of the set."
    "That one is named E, while the others are named A,D,G,B,E going down the set."
    show monika 3ba
    "Monika pauses the video yet again."
    m 1bb "Perfect, we only have to tune 6 notes!"
    show monika 1ba
    mc "I hope it's easy, I'd rather not listen to these terrible notes longer than I have to."
    m 4bk "Of course it will be silly!"
    m 2bd "Now where was E again..."
    m 3ba "Ah, found it!"
    m 3bk "Are you ready [player]?"
    show monika 2bj
    mc "Uhhh..."
    "I know she really wants to help me learn this thing, but I should probably learn how to use this tuner first."
    "I mean, she's not gonna be around with her piano {i}all{/i} the time."
    "Maybe just one or two strings then we can use her piano."
    "But I don't wanna sour her mood either."
    "What if she takes it the wrong way?"
    menu:
        "Think [player], think!"
        "Use the Piano":
            $ tuner = 0
            mc "Yeah, I'm ready Monika."
            "I'll just look it up later."
            "Can't be that hard right?"
            "Besides, that smile is too happy and bright to dampen over something so small and trivial."
            "Setting my pick on the E string, I strike it across."
            #play sound "mod_assets/EgOot.ogg"
            show monika 2bl
            "The terrible note spreads throughout the room."
            "Monika giggles again at the sound."
            #play sound "mod_assets/Ep.ogg"
            show monika 1ba
            "Collecting herself, she plays the same note on her piano."
            m 4bb "So to me your guitar sounds too sharp."
            m "That means the pitch was too high."
            m "Now to fix that you..."
            m 3bn "You..."
            show monika 2bm
            "She quickly leans over and picks up the book from the arm of the couch."
            "Scanning over the section, she puts the book down again."
            m 3bk "Loosen the string! Ahaha~"
            show monika 2bj
            "Shaking my head, I find the knob the E string was wrapped around and loosen it a bit."
            show monika 1ba
            "It took me several adjustments to get my E to match hers."
            "Constant minor adjustments to the knob and playing the string a ton to compare sounds."
            m 3bb "Alright [player]! Sounds good!"
            m 4bk "Now time for the rest!"
            show monika 2bl
            mc "Uugghh."
            m 2bi "Hey, what's the big deal."
            show monika 1bc
            mc "Oh nothing."
            show monika 2be
            mc "Was just thinking that I might not hear your piano playing after we tune."
            m 2bl "Oh [player], I'm sure I can play for you in a bit."
            m "Ahaha~"

        "Use the Tuner":
            $ tuner = 1
            mc "W-wait Monika."
            m 1bc "Hmm?"
            m 1bd "What's up?"
            show monika 2bc
            mc "Can I use the tuner first?"
            show monika 1bf
            mc "J-just for the first string?"
            m 1bp "Oh... alright [player]."
            m 3bn "You really should be learning how to use it ahaha~"
            show monika 1bo
            "Even with that, I can still see that she was disappointed."
            show monika 1bf
            mc "Hey, don't look so down Monika."
            show monika 2be
            mc "I still want to learn this with you."
            show monika 1bm
            mc "I just want to learn how to use this thing a bit, you understand right?"
            m 2bn "I'm sorry [player], I understand."
            m "I just got ahead of myself yet again."
            m 2bl "Gosh this whole thing has messed me up today ahaha~"
            show monika 2bm
            mc "It's fine Monika, one step at a time though."
            show monika 1bj
            "I move over to her and give her a peck on the cheek."
            show monika 2ba
            "Adjusting the guitar in my hands I place my pick above the top string."
            #play sound "mod_assets/EgOot.ogg"
            "Plucking the string rings out a tone sounding very wrong even to me."
            "The tuner claims it is in fact an E but its reading too high."
            m 4bb "That means the note is too sharp [player]."
            show monika 2ba
            mc "Sharp huh."
            "I look over to the book lying open on the couch."
            "It says to turn the E knob to loosen the string."
            "That will lower the pitch of the note."
            "Turning the knob and playing again the tuner reads E again and much closer to the correct pitch."
            "After a few more attempts of adjusting, playing, and checking the tuner, I get the E string tuned."
            m 3bk "Sounds perfect [player]! Good job!"
            show monika 2bj
            mc "Thanks Monika, but now comes the fun part."
            m 2bd "Oh, what part is that? We've only tuned one-{nw}"
            m 2bb "Oh I know!"
            m 4bk "We get to tune together now! Ahaha~"
            show monika 1bj
            mc "Yup you guessed it."
            m 2bk "Yay!"
            "Her enthusiasm is just intoxicating sometimes."
    show monika 2ba
    "Moving down the rest of the strings was simple enough."
    "Tuning with Monika even made the task that much more enjoyable."
    if tuner == 1:
        "Though stealing a peek at the tuner just to check how close we were helped speed things along."
    m 4bb "Well [player] that's all of them!"
    m 4bk "Give them all a try again!"
    show monika 2ba
    "Setting the pick at the top once again, I run it across the six strings."
    #play sound "mod_assets/openstrum.ogg"
    "The revitalized sound brings a grin to my face."
    "Now we could really learn something."
    m 3bk "That sounds perfect!"
    m 2bb "Let's get back to the lessons then!"
    show monika 3ba
    "Picking up the remote again she ends the first lesson and sends us back to the menu."
    "The next lesson is titled {i}The Basics of Chords.{/i}"
    show monika 2ba
    "The same instructor welcomes us back and points us to the new chapter of the book."
    show monika 2bc
    "This time it's all about playing a set of strings in what's called a chord."
    "They make up the base of guitar playing and learning the more advanced parts."
    "The instructor points to the neck of the guitar, specifically the small metal dividers."
    "They were called frets and depending on where I put my fingers on the strings between these frets it would change the sound."
    "In the book there was a huge chart with a bunch of different pictures."
    "These told me where to put my fingers along the guitar neck to play the different chords."
    "I guess I'll just start wi-{nw}"
    m 2br "Oh come on!"
    show monika 1bd #<-- We need something with more surprise than d
    "I felt like I jumped ten feet off the couch when she yelled that out."
    m "Oh my gosh [player], I'm so sorry."
    mc "I-it's ok Monika. What happened?"
    m 4bn "Well... my mother just texted me."
    m 2bp "She says she needs me home so we can go and pick up some things for the house."
    show monika 1br at t11
    m "So I guess I need to get going."
    m 1bg "I really wish I didn't though."
    show monika 1be
    mc "Hey, it's alright Monika, I had a load of fun today."
    mc "And there's always another Sunday just a week away, and club all in between that wait."
    m 2bn "Your right, but I still hate to leave on such an abrupt note."
    show monika 2be
    mc "Don't worry about it, your mom needs help and you gotta go. I understand."
    mc "I'll help get you packed up as best I can."
    show monika 1bc
    "And with that, I start at disassembling her piano."
    m 2de1 "Would it be okay if I left it here [player]? I don't know if I can bring it all the way back myself."
    m 4bb "You can hold on to the book and DVD too, it'll let you keep learning."
    show monika 2ba
    mc "Yeah of course, but are you sure about the book Monika? Your friend wouldn't mind?"
    m 4bl "He hasn't touched that book in forever, I doubt he'd mind you keeping it for a bit."
    show monika 2ba
    mc "If you insist."
    show monika 1bo
    "I leave the piano in the living room and walk Monika to the door."
    m 1bp "I still really wish I didn't have to leave so soon."
    show monika 1be
    mc "Me neither Monika."
    show monika 1bj at face 
    with dissolve
    "Putting down the piano, I pull her into a hug and give her a kiss."
    show monika 1ba at t11 
    with dissolve
    mc "I love you Monika, and say hi to your mom for me."
    m 2bk "I love you too [player], and I definitely will!"
    show monika at thide
    hide monika
    "After watching her go, I make my way back into the living room."
    # I have no idea what this section is for
    # roday is never initialized or changed
    # =======================================================================================================
    if roday == 0:
        "Checking my phone for the time, it reads it's getting near dinner time and the end of the day."
        "It didn't even feel like we spent the whole day together, but it seems we almost did."
        "Still, even a minute more would have been nice."
        "But her mom needed her, I can't argue with that."
        "I slump over on the couch again, grabbing the remote on the way down."
        "Looking to the TV screen once again the lesson still sits paused on the screen."
        "I really should continue the lesson, but I've been at it all day to begin with."
        "I'm just too tired to focus on it, and without Monika I have even less motivation to focus."
        "I'm just gonna take a quick little nap."
        "I put my phone next to me just in case Monika texts me."
        "Propping my feet up and letting out a yawn, I close my eyes."

    elif roday == 1:
        "The day was still far from over though, plenty of time to do stuff."
        "I wish Monika could have been here to spend it with me."
        "Her mother needs her though, I can't argue with that."
        "But what to do with my time?"
        if tuner == 0:
            "You know, I could practice using the tuner."
            "Taking a seat on the couch, I mess with the knobs on the guitar a bit to knock it out of tune."
            "I play the first lesson once again and follow along."
            "Simple enough, I have the guitar back to perfect order in a few minutes."
            "Though I'm sure without that video I would have never understood this thing."
            $ tuner = 1

        elif tuner == 1:
            "Taking the guitar in my hand, I try out some of the chords."
            "I can't tell if they sound right however."
            "They seem to, but without someone to critique I can't tell."
            "I don't even have the motivation to continue the lessons either."
            "It feels like something I should save for when Monika is here."
            "Or when I have more motivation to learn."
            "The early morning is starting to catch up with me, even with the coffee."

        "Setting the guitar back in it's case, I decide to catch up on my shows while I have some time."
        "Getting comfy on my couch, I roll the latest episodes and drift into another world."
    # =======================================================================================================

#C7 - Clubroom
    stop music fadeout 2.0
    play music t3
    scene bg club_day 
    with dissolve_scene_half
    "Another boring day at class has finally ended, and I was back in the club room."
    "The room had been in full writing mode for the school paper the whole time with a deep silence over the room."
    "As for me though, I wasn't really in any mood to write anything today."
    "My focus was still on the guitar and everything else from yesterday."
    "I had even brought the lesson book Monika had given me from her friend."
    "Though reading all this without a guitar to practice on isn't really helping me a whole lot."
    "Monika was busy proof reading some things and filling out paperwork for the club, so talking to her was out of the question."
    "I'm sure she wouldn't mind me bothering her, but I'd rather her finish that stuff on time."
    "I'll just kill the last couple of minutes flipping through the book."
    "Oh this looks interesting, it's talking abou-{nw}"
    n "WHAT ARE YOU DOING DUMMY!"
    show natsuki 4f at i11
    "Natsuki's yell snaps me out of my focus and nearly scares my pants off."
    n 4e "Your supposed to be {i}writing{/i} [player], not reading a book!"
    n 4w "Monika! Tell your stupid boyfriend to get working!"
    show monika 2i at l21
    show natsuki 3g at t22
    show monika at f21
    m "Natsuki why are you yelling at [player], you've disrupted everyone's writing."
    show monika 2h at t21
    show natsuki 4e at f22
    n "He's hiding over here slacking off while we're all working our butts off to meet the deadline."
    show monika 2c
    show natsuki 4g at t22
    mc "Look I really don't have any motivation to write today, I'm drawing a blank here."
    show natsuki 3p at f22
    show monika 2h
    n "That's because you're reading that STUPID BO-{nw}"
    show natsuki 4o at t22
    show monika 4i at f21
    m "Enough Natsuki."
    m "You don't need to shout about it."
    show natsuki 4w at f22
    show monika 2q at t21
    n "Well I'm sorry I'm the only one keeping him in check!"
    n "You just let him do whatever cause he's your {i}boyfriend{/i} while we all suffer the consequences."
    n "I won't be dragged down cause of his lack of motivation."
    show natsuki 1x at lhide
    hide natsuki
    show monika at t11
    "And with that, she storms out of the club room."
    "Looking around, it seems the rest of the club are just as confused to the current events."
    show monika 2c at t22
    show yuri 3o at l21
    show yuri at f21
    y "Um, m-maybe I should go after her. Try and calm her down a bit."
    y 3n "We wouldn't want her s-stomping all around the school like that."
    show monika 2e at f22
    show yuri 2q at t21
    m "Thank you Yuri, that would be great if you could."
    show monika 1e at t11
    show yuri 1m at lhide
    hide yuri
    "Yuri quickly takes her leave from the room, leaving just three of us left."
    show sayori 2p at l21
    show monika 2c at t22
    show sayori at f21
    s "I'm so confused, why was Natsuki so mad all of a sudden?!"
    show sayori 1o at t21
    show monika 2p at f22
    m "I'm not really sure Sayori, she didn't have to get so hostile over a bit of reading."
    show monika 2c at t22
    show sayori 2c at f21
    s "What were you reading anyway [player]?"
    show sayori 1b at t21
    show monika 2m
    mc "Just a book on learning my guitar. I was having really bad writers block today."
    show sayori 4m at f21
    s "Oh my gosh, I almost forgot about that!"
    s 3n "Can you play any pretty songs yet?"
    show sayori 1o at t21
    mc "Not yet Sayori, I'm still learning the basic stuff."
    show monika 4b at f22
    m "You'll have to play for the club once you finally learn something [player]."
    show monika 2c at t22
    show sayori 4r at f21
    s "You two could do a duet!"
    s "That would be soooooo cute!"
    show sayori 1q at t21
    show monika 3k at f22
    m "You know, that sound like a great idea Sayori!"
    m 2l "Why didn't I think of that Ahaha~"
    show monika 2l at t22
    "Oh no, I really don't think I could do a duet with Monika."
    "At least... anytime soon that is."
    "I barely even get this basic stuff, nevermind play a song with her!"
    show sayori 1n
    show monika 2d at f22
    m "Oh gosh would you look at the time, it's already getting late."
    m 4n "Guess Natsuki picked a good time to leave."
    m 2r "Though the drama was a bit unnecessary of her."
    show monika 1c at t22
    show sayori 2c at f21
    s "Maybe she was having a frustrating time today, or maybe she was a bit hungry."
    s 2l "I know I get a bit cranky when I'm hungry, Ehehe~"
    show sayori 1g at t21
    show monika 3r at f22
    m "Still, it didn't need to be directed at poor [player]."
    show monika 1e at t22
    show sayori 1a
    mc "It's alright Monika, besides, I really should have been working anyway."
    mc "I just couldn't get myself to write anything though."
    show monika 3e at f22
    m "Writer's block happens to the best of us, nothing to beat yourself up about."
    m 2b "But as long as you come back strong with fresh ideas I have no problems with anyone taking a creative break."
    show sayori 1y
    m 5a "So, shall we be going [player]~?"
    show monika 2c at t22
    show sayori 2l at f21
    s "I uhhh... {w=.75}gotta go to a store a different way than what we usually walk today guys."
    s "I'll catch up with you guys tomorrow, okay?"
    show sayori 1d at t21
    show monika 2d at f22
    m "Aw really? That's a shame."
    m 3k "We'll see you tomorrow Sayori!"
    show sayori 1a at lhide
    hide sayori
    show monika 2a at t11
    "Sayori waves and briskly walks ahead of us out of the clubroom and down the hall."
    show monika 5a
    "Monika does a quick walk around the clubroom and picks up the papers from Natsuki and Yuri's desk."
    m 2d "Oh dear, they left their book bags here."
    m 4n "Can't lock up the clubroom with them here."
    show monika 2c
    mc "Let's take them with us then, we can give them to those two when we find them."
    mc "That way we aren't stuck waiting for them here."
    m 3b "Good idea [player], we can enjoy the fresh air for a bit."
    show monika 2a
    "We both grabbed one of the bags and headed for the door."
    scene corridor 
    with wipeleft_scene
    show monika 5a at t11
    "Monika quickly locked up the room and we started down the hallway."
    "She immediately wrapped her arm around mine and stayed as close as she could to me."
    show monika 1c
    "She still had the papers from the other girls in her hand and was reading through them as we walked."
    m 1p "Sayori was right, Natsuki {i}was{/i} having a rough day today."
    m 1g "She barely has anything written down here, and what she does have has all been scribbled out."
    show monika 1f
    mc "Bad writer's block too huh."
    m 1n "Seems like it."
    m 1p "I really shouldn't have snapped at her like I did."
    m 2r "I just couldn't stand her yelling at you, nevermind her disrupting everyone else."
    show monika 1e
    mc "You had to be the club president for a bit, nothing wrong with that."
    mc "No big argument started, so I'd say it went better than it could have."
    m 2l "Can't argue with you there."
    m 2g "Still... I could have went about it a little better."
    show monika 1e
    mc "Well she really didn't give you much room to talk to her anyway. She was gone about as fast as it had started."
    show monika 1m
    mc "Trust me Monika, you did the best thing you could have done at the time."
    mc "Don't beat yourself up over it."
    m 1e1 "Thank you, [player], I really needed to hear that from you."
    show monika 1j at face
    pause .3
    show monika 1j at t11
    "Monika leans over and pecks me on the cheek"
    show monika 1c
    mc "Oh would you look at that, there they are!"
    show monika at thide
    hide monika
    show natsuki 42f at t42 zorder 3
    show yuri 3m at t11 zorder 4
    "The two of them had found a lone bench far away from the stream of students leaving the school grounds."
    "Yuri had Natsuki firmly wrapped in a hug as we approached them."
    show yuri 3f at h11
    "Yuri noticed us approaching and made a small wave to us behind Natsuki's back."
    show yuri 3e
    "I lifted the backpack off my shoulder toward her and pointed to an adjacent bench."
    show yuri 3a at s11
    pause .2
    show yuri at t11
    "She nodded in agreement and we placed the bags as close as we could to Yuri and Natsuki without disturbing them."
    show yuri 3c
    show natsuki 42h
    "Waving our goodbyes, we started our walk back home."

#C8 - Parental Blockade
    stop music fadeout 2.0
    scene bg residential_day 
    with wipeleft_scene
    play music t8
    show monika 5a at t11
    "The long hike home has always been a bit better with Monika by my side."
    "The warm spring air seems to keep a pep in her step as we walk along the sidewalks towards the crossroads that we usually split off at."
    show monika 1m
    "Monika seemed to be lost in thought as we walked, and without Sayori there wasn't a conversation constantly going between all of us."
    "The silence between us along with the sounds of our footsteps and the city around us gave off an aura of peace."
    m 2n "Hey [player], can I ask you something?"
    show monika 1m
    mc "Hmm? What is it?"
    m 2n "Well, I know we always split here and go our separate ways home..."
    m "And that we only really spend time together on Sundays..."
    m "I was just thinking that maybe we could-{nw}"
    show monika 1b
    mc "Do you want to come over to my place today?"
    m 4k "YES!"
    m 2l "O-oh gosh did I yell that out? Ahaha~"
    m 1n "Sorry, I just wasn't expecting you to actually suggest it."
    m 1b "But you really wouldn't mind me coming over today?"
    show monika 1a
    mc "Well the house may be a tad bit messy but of course, I would love to have you over Monika."
    m 1k "Oh [player], your the best!"
    show monika 1j at face 
    with dissolve
    "Monika practically jumps on me and gives me a passionate kiss."
    "Gosh, did she really think I wouldn't want to have her over on weekdays?"
    show monika 3b at t11
    m "I just have to call my mom and let her know I'll be at your place."
    m 2n "She would be pretty worried if I didn't show up at home without an explanation, Ahaha~"
    show monika 2a
    "Monika wastes no time dialing up her mother and putting the phone to her ear."
    show monika 4b at h11
    m "Hi Mom! Hey I had-{w=.75}{nw}"
    m 3d "What, no Mom I'm perfectly fine."
    show monika 4c
    pause 1.5
    m 4l "Yes I'm fine Mom, I wasn't calling about anything like that."
    m "I just wanted to ask you something."
    show monika 3m
    pause 1.5
    m 4n "Well I was just wondering if I could..."
    m "Maybe... go to [player]'s house instead of coming home right away?"
    show monika 3c
    pause 1.5
    show monika 3o
    pause 2.5
    m 3p "Please Mom, I promise I'll get my homework done and..."
    show monika 3f
    pause 2
    m 3g "I know, I won't be out for long."
    m 4d "Wait."
    m 4b "Do you want to talk to [player]? He'll even tell you the same thing!"
    show monika 4e
    "Monika pulls the phone from her ear and motions it to me."
    m 3e1 "Please [player], just say I...{w=.75} needed help on homework or something."
    m 2e1 "Anything to get her to say yes."
    show monika 1j
    mc "Ugh, the things I do for you."
    "Dramatically plucking the phone from Monika's hand, I put it up to my ear."
    show monika 2a
    mc "Hello Ma'am."
    $ y_name = "Monika's Mom"
    y "[player]? [player]! How have you been sweetheart?"
    show monika 2c
    mc "Very well, how about yourself?"
    y "As well as an old woman like me can be."
    "She chuckles to herself through the receiver."
    y "Now, what is this nonsense that my little Monika is asking about?"
    y "She knows how I feel about her galavanting around when there is school work to be done."
    show monika 2e
    mc "Monika just wanted an extra hand on an assignment we got today... and I thought I could help her out."
    y "Why would she need help on an assignment, she's the smartest girl in that school."
    mc "Of course she is, but even the greatest need help along the way at some points."
    "At this point I'm pulling things from thin air."
    "I look over to Monika with a face that screams \"Help me please\"."
    show monika 1j
    "Monika shoots me a big smile that helps calm my nerves."
    show monika 2a
    mc "I promise that Monika will be home before dark ma'am with the assignment complete."
    y "Hmph, I will hold you to your word [player], she is still {i}my{/i} daughter above all else."
    mc "I know that ma'am."
    y "Lest you forget. Tell her that dinner will be in the fridge when she gets home."
    "And with that, the call disconnects."
    $ y_name = "Yuri"
    m 1b "Did she say yes?!"
    show monika 1c
    mc "Yeah, but you have to be home by sundown."
    m 1k "Oh you’re just the best boyfriend I could ever ask for [player]!"
    show monika 1j at face 
    with dissolve
    "Monika throws herself again into my arms and passionately kisses me all over my face."
    mc "Hey, Hey! We're gonna spend all our time here if we don't start walking soon."
    show monika 2l at t11
    m "I know I know, sorry! I'm just really happy right now!"
    m 5a1 "Come on, lets go!"
    show monika 5a at lhide zorder 1
    hide monika
    "Monika takes me by the hand and practically starts dragging me as she runs toward my place."
    scene bg residential_day 
    with wipeleft_scene
    show monika 5a at l11 zorder 4
    "As we make it to my place she finally lets go of my hand and I get a chance to catch my breath."
    m 2l "[player], it wasn't {i}that{/i} far of a jog, Ahaha~"
    show monika 2m
    mc "Easy for you to say, I'm not the athletic one of the two of us."
    m 4l "Well I'm sure with enough work you could be just as athletic as I am."
    show monika 2e
    mc "Maybe, who knows."
    "I silently plea to every deity I know that she won't actually subject me to that."
    show monika 2a
    "As we walk to the front door and I fumble for my key, a thought comes to mind."
    show monika 2c
    mc "Monika, do you even have any homework to do or anything?"
    m 3n "No, not really, Ehehe~"
    m 2n "I just wanted to spend some time with you, it just gets so boring at home."
    m 1p "And waiting till Sunday is like torture sometimes."
    show monika 1a
    mc "Well I would love to have you over more often Monika."
    show monika 2e
    mc "We'll just have to convince your mother on the idea."
    m 2n "Yeah, she would need some convincing."
    show monika 5a
    "Finally finding my key in my bag, I open the door and wave her inside."

#C9
    scene bg livingroom 
    with wipeleft_scene
    show monika 5a at l11 zorder 3
    "Depositing our bags and shoes by the door, Monika makes her way to the couch."
    show monika 4b at s11
    m "So [player], do {i}you{/i} have any homework to do?"
    show monika 2a
    mc "Surprisingly not, thanks to you I have everything covered so far."
    "I'll keep the essay that I still have to review out of the picture for now, I'd rather not waste a rare occurrence like this reviewing essays."
    m 3k "That's great, I'm so glad to hear it!"
    m 2e1 "You know how much I hate seeing you behind in classes."
    m 3l "Well if your all set on schoolwork, what do you have in mind to do [player]~"
    show monika 1c
    mc "I'm not really sure to be honest."
    "Besides not expecting to have her over today, I didn't really have any plans today to begin with."
    "I was just gonna push the essay off and watch anime and play games."
    show monika 2a at t11
    "Monika looks over to the other side of the room and spots something, prompting her to get up."
    mc "W-what is it Monika?"
    show monika at lhide
    hide monika
    "She walks to the other side of the room without a word and reaches for something next to the other couch."
    show monika 4a at l11
    "Turning back to me, she's holding my guitar case up."
    m 4b "How's about a bit of guitar practice [player]?"
    show monika 4a
    mc "Sure, I really should get back into that."
    m 3g "Have you not been practicing?"
    show monika 3f
    mc "Kinda, it's just..."
    "Those sad puppy-dog eyes are not helping me form any sort of counter statement at all."
    show monika 4a
    mc "T-the more practice the better right?"
    m 4k "Right!"
    show monika 1j at lhide
    hide monika
    "Monika sets the guitar case in front of me while she goes over to the TV to set up the lessons."
    "Taking up the guitar in my hands again, I feel kind of guilty I haven't been practicing this thing."
    "I picked this up with her in mind and yet I haven't even touched it since last Sunday."
    "That really needs to change..."
    show monika 3d at l11
    m "So we were only on the second lesson right?"
    show monika 1c
    mc "Yeah, we didn't really make it that far last time."
    m 4b "Well we have loads of time today, we can make a bunch of progress!"
    show monika 3a at s11
    "Monika takes a seat next to me while scrolling through the menus on the disc to find where we left off."
    "I flip back to the page full of pictures detailing the chords I was going to learn."
    show monika 1a
    "The lesson begins and the instructor greets us once again."
    show monika 1c
    "We listen through the beginning of the lesson again just so I can refresh myself."
    "As we reach the point where we left off last time, the instructor explains the basics of reading the chord diagrams."
    "For now, I only needed to use the top three strings to begin with..."
    scene bg livingroom_evening 
    with wipeleft_scene
    "Time seemed to fly by as we worked through the lesson."
    "It took a bit of practice to get used to moving my fingers around the guitar and hitting the right points, but I seem to have it mostly down."
    show monika 1j at s11
    "After finishing the final practice song of the lesson, I look over to Monika."
    m 1k "That was good [player], you're really catching onto this!"
    show monika 1a
    mc "Thanks Monika, this is actually really fun."
    m 3b "I'm glad you're enjoying it, that makes it easier to learn right?"
    show monika 1j
    mc "Right."
    show monika 1c
    mc "Hey it's getting kinda late Monika, you should probably get going to make it home on time."
    m 1n "Gosh it is getting late, isn't it."
    m 1p "And I was just getting comfortable too..."
    show monika 1j at face 
    with dissolve
    "She leans into my side and nudges her head into my shoulder."
    mc "I know, but I promised your mother you would be home before sundown."
    mc "We'd both have to hear it if you aren't home by then."
    m 1l "Oh alright, you win."
    show monika 2e at tll
    "Laying the guitar on the couch, I help Monika up onto her feet."
    m 2e1 "Thanks for having me over today [player], it was a really nice change of pace for a school day."
    show monika 2e
    mc "It was my pleasure, and thanks for helping me out today."
    mc "I really needed that push to practice again."
    m 4k "Anytime [player], I know you'll be a great guitar player soon."
    show monika 2a
    "Helping her grab her things, I lead her out the door."
    scene bg residential_evening 
    with wipeleft_scene
    show monika 5a1 at t11
    m "Are you sure I can't stay just a {i}little{/i} longer [player]?"
    show monika 5a
    mc "You know I would love you to, but you need to be home on time Monika."
    m 2l "When did you become the bossy one [player]? Ahaha~"
    show monika 1j at face 
    with dissolve
    "Shaking my head, I pull her into a hug and kiss."
    show monika 5a1 at t11
    m "Bye [player], see you tomorrow!"
    show monika 5a
    mc "See you tomorrow Monika."
    show monika at lhide
    hide monika
    "With one more peck on the cheek, she's off again back to her house."
    "As I turn back to my door, something catches my eye."
    "A flash of red ribbon in the window next door, hidden quickly behind the curtains."
    "..."
    "Maybe I should pay her a visit..."

#C10 - Confrontation
    "Locking my door, I make my way over to Sayori's place."
    "I can't see Sayori in the window anymore as I walk over, she must have walked away from it."
    "Reaching her front door, I give it a hard knock so that she could hopefully hear it."
    "After a short while of no response, I slowly open the door."
    "We would always do this when we were young because we were as close as family."
    "At least, I hope that hasn't changed in the last couple of years..."
    stop music fadeout 2.0
    scene bg livingroom_sunset 
    with wipeleft_scene
    "Entering the house, it seems eerily quiet."
    mc "Sayori? It's me, [player]."
    "..."
    "No response."
    mc "I just wanna talk to you for a bit."
    "..."
    "Still nothing."
    "I feel bad just barging into her house like this, but this isn't like Sayori."
    "She'd usually answer the door and greet me with a big smile, not ignore me like this."
    "Well if she isn't down here, she must be in her room still."
    "I'll just head upstairs and-{nw}"
    show sayori 1bv at s11
    mc "S-sayori?!"
    "Sayori sits at the top of the staircase looking down at me."
    "I could see the light glissen off her cheeks even from down here."
    play music t9
    s "Hi...[player]..."
    s 1bt "It's so nice to see you, it's been a while since you've been over hasn't it?"
    mc "Yeah... but it's nice to be over again."
    mc "Maybe even as messy as I remember it, heh."
    s 1by "Yeah, usually you would be the one to help tidy up, ehehe~"
    s "But it's been a long time since that's happened."
    mc "Yeah..."
    show sayori 1bv
    "I move up the staircase and take a seat next to Sayori."
    "Her eyes are red and puffed up while her cheeks are still slick with tears."
    mc "Sayori, what's wrong."
    s 1bt "What do you mean [player], I'm perfectly fine. See?"
    show sayori 4bs
    "Sayori flashes me a wide smile, but I can already see how hard it is for her to hold it on her face."
    show sayori 1bu
    mc "Sayori please, did something sad happen to you just now? Is it anything we can talk about?"
    s 2bt "Its nothing, really. Just a passing raincloud is all..."
    show sayori 1bu
    mc "Raincloud? What do you mean Sayori?"
    s 4bw "I...It's nothing!"
    s "It's nothing [player], you can go home!"
    show sayori 3bp
    "Sayori tries to shunt me off the stairs in an attempt to get me to leave."
    "She knocks me off balance and nearly sends me tumbling back down the stairs."
    "Luckily I catch myself on the handrail before I hurdle down the flight of stairs, banging up my hand in the process."
    s 2bw "I-i'm sorry, I didn't mean to..."
    s 1bu "Oh this is all my fault..."
    show sayori at t11
    show sayori at lhide
    hide sayori
    mc "Sayori, wait!"
    "Sayori quickly gets up and storms into her room, slamming the door behind her."
    "I quickly follow and put my head to the door."
    mc "Please Sayori, I want to help you. You're my best friend."
    s "{i}You’re just making it harder [player]...{/i}"
    "I can hear her begin to sob again through the door."
    "Gingerly taking the doorknob in my hand, I enter the room."
    scene bg sayori_bedroom_sunset 
    with wipeleft_scene
    show sayori 1bv at s11
    "Sayori is balled up on her bed, crying into her knees."
    "Tip toeing over to her bed, I take a seat on the opposite edge."
    s 1bu "Why are you still here..."
    mc "Because you're my best friend Sayori, I can't just leave you here like this."
    mc "I want to help you anyway I can."
    s 2bw "There is no way to help me [player]."
    s "This is how I am, a sad, selfish girl."
    s 1bu "Its...{w= .75} what I deserve."
    show sayori 1be
    mc "No Sayori, that's not right at all."
    mc "Did something happen? There must be something, that's the only explanation for this."
    s 1bt "Nope, nothing at all. This is just how I am."
    s "For a very long time, almost as long as I can remember I've been like this."
    mc "What do you mean Sayori? You've always been a happy ball of sunshine for as long as we've been friends."
    s 1bk "No...{w=.75} it's just easy to pretend around you, [player]."
    s "I don't even have to try and smile when I'm around you."
    s 1bv "But when you're not around, it's so hard to keep the rainclouds away."
    s "And when I see you with her..."
    s 3bw "Why was I so stupid! Why did I bring you to the club!"
    s "All I ever do is hurt myself!"
    show sayori 1bv
    mc "Sayori!"
    menu:
        "I finally snap out of my daze and..."
        "Pull her into a hug":
            show sayori 1be at face 
            with dissolve
            $ c10e = 1
            "Crossing the bed, I pull Sayori into a tight hug."
            "A bolt of pain shoots up my arm, but I wince it away and try and forget about it."
            "My sudden movement made her jump a bit, but she relaxes slightly in my arms yet doesn't return the hug."
            "What has gotten into her?"
            "This wasn't Sayori at all..."
        "Squeeze her hand":
            show sayori 3be
            $ c10e = 0
            "Moving myself closer to Sayori, I take one of her hands in both of mine in an attempt to soothe her."
            "My hand is still sore from earlier, but I brush off the pain and focus on her."
            "She doesn't recoil away from me, but an inner conflict is starting to show on her face."
            "What could have possibly upset her like this?"
    mc "Please, just tell me what's wrong Sayori. We can fix it together."
    s 1bt "I wish it was that easy [player], but it's so much harder than that."
    s 1bk "I tried to drag you into something you didn't even want to do and all I've done is hurt myself."
    s 2bl "And in the end, I let my emotions control me and mess everything up, ehehe~"
    show sayori 1bu
    mc "Sayori this isn't like you at all, what can I do to help, really."
    s 1bv "Disappear..."
    "The cold seriousness in her voice sends a shiver through my body."
    "Disappear? But..."
    s 1bw "B-but at the same time, I don't want you to go anywhere."
    s "It all just... hurts."
    if c10e == 1:
        show sayori 1by
        "I pull her tighter to my chest."
        "What is she saying right now? This can't be how she feels..."
    elif c10e == 0:
        show sayori 1bv
        "I try to caress her hand a bit to calm her down."
        "I've never heard her talk like this before, what has gotten into her?"
    s 1bu "[player]...{w=.75} you know what depression is, right?"
    mc "Y-yeah of course, but..."
    "Sayori? Depressed? That couldn't be..."
    "She's always been so happy and energetic."
    s 2by "I've had it since I was just a little girl, [player], even way back when we were kids."
    s 1bk "It was tough, having this sad feeling in my head all the time."
    s 1bt "But when I met you, everything seemed ok back then."
    s 2by "It was so easy to be happy around you, [player]."
    s 1bk "But then we just...{w=.5} fell apart."
    s "We didn't talk for ages, I was so worried I had lost my one true friend."
    s 1bl "But I didn't, you're still here, a-and I'm really happy about that."
    s 1bt "I was really happy when you joined the club too, it was like a dream come true."
    s "Seeing you make all new friends and have fun with everybody."
    s 1bu "B-but you started getting so close to Monika and..."
    s 1bv "I felt like I was being stabbed a million times in the heart."
    s 1bw "I let my feelings get in the way and now look what happened!"
    s "I'm just making you worried about me when you should be with her!"
    s "I don't deserve any of this!"
    if c10e == 1:
        show sayori 1bu at t11
        "Sayori jerks herself out of my hug and balls up against the wall."
    elif c10e == 0:
        show sayori 1bu
        "Sayori pulls her hand away from mine and moves away from me."
    mc "Sayori, you’re my bestest friend in the whole world. Of course you deserve to be cared about by your friends."
    s 2bu "Not when I'm just a useless, selfish nobody..."
    mc "Sayori please, you aren't any of those things."
    mc "You’re such a sweet and caring girl and everyone loves to have yo-{w=2.0}{nw}"
    #Scene Check#
    stop music fadeout 1.5
    play music t9
    s 3bv "I love you, [player]."
    "Her statement stops me in my tracks."
    s "I love you, like, really love you."
    s 1be "I-i didn't really realize it at first, and I didn't want to make you have to spend all your time with me and not anyone else."
    s 1bk "And everyday in club you would spend more and more time with Monika..."
    s 2bl "It was really obvious to the rest of us, ehehe~, we would joke around about how you guys would finally start dating when you weren't around."
    s 4bs "We had some really fun ideas, ehehe~"
    s 3by "I wanted to be happy for you, that you finally found someone that you could be with."
    s 1bk "But I started to realize I felt this way about you, and by then it was too late."
    s "I wanted to pull you away, but I just couldn't bring myself to do it."
    s 1bv "Y-you l-l-loved her..."
    s 4bw "YOU LOVE {i}HER,{/i} NOT {i}ME!!{/i}"
    s 3bp "Why did I do this to myself, [player]?!"
    s 2bw "Why can't I make the rainclouds go away?!"
    s 2bt "I just want to see you happy..."
    s 1bv "But it all just...{w=1}hurts..."
    s 3bw "Maybe if I just disappear, everything would just..."
    show sayori 1bu
    mc "Sayori, no! Please..."
    mc "Everything is going to be fine..."
    "I take a second to breath and catch my thoughts."
    "So those times in the club before me and Monika dated where she wasn't herself, it was because of...me?"
    "I just thought she was being a really good friend all the time, but if she had these feelings..."
    "I had been so focused on chasing Monika, I didn't even stop to notice the people around me..."
    s 1bv "[player], would you have loved me if I wasn't like this?"
    show sayori 1bu
    mc "I don't think of you any lower because of how you feel Sayori. You're still my best friend."
    s 1bv "What did I do wrong then?"
    s 1bu "Why didn't you like me as you like Monika?"
    s 2bw "Am I just that unlikeable that even my closest friend wouldn't even fall in love with me?"
    show sayori 2bv
    mc "Sayori please, you're not unlikeable at all. I'm sure there are hundreds of people wanting to meet you."
    mc "They would all see how much of a wonderful person you are."
    mc "Things were just...{w=.5} different with me and Monika..."
    mc "I didn't think anyone like her would fall for a guy like me, but things just kinda...{w=.5} worked I guess."
    s 2bt "How couldn't she? You're such a caring and thoughtful person, [player]."
    s 3by "Not to mention very cute too..."
    s 1bs "She's the happiest girl I've ever seen when she's with you, it really makes me happy to see her so full of joy."
    s 2bk "But then that happiness for you two goes away, the rainclouds come back."
    s 3bt "It's what I deserve though, isn't it?"
    show sayori 1bv
    mc "No, not at all Sayori. You deserve to be just as happy as her."
    show sayori 1bt
    mc "You’re such a fun ball of sunshine and everyone you meet is a little happier after they talk with you."
    mc "Most importantly though, you’re my best friend. I would be devastated if I lost you, you've been there for me for as long as I can remember."
    show sayori 1by
    mc "I-i know its not really the ideal situation... but I wouldn't want to break our friendship."
    mc "You’re still one of the closest people to me and no one could ever take that place, not even Monika could break our friendship."
    s 4be "B-but you love her so much, w-what if she got really mad one day? More than she ever has?"
    show sayori 1bv
    mc "Then I'll cross that bridge when I reach it, she can't fully control the people I wanna have in my life."
    show sayori 1by
    mc "And I wanna keep you in my life for as long as I can Sayori, you're just that special to me."
    s 3bl "You know just how to make a girl blush, [player]."
    show sayori 3by
    mc "O-oh I didn't mean to make it worse..."
    mc "I was just saying how I felt and...{nw}"
    s 1bd "I know [player], and thank you."
    s 2bd "I really don't deserve a friend like you, you are truly one of a kind."
    show sayori 1by
    mc "I'm sure there are others just like me Sayori, and they would see what a wonderful girl you are and fall head over heels."
    s 1bd "If you say so, [player]"
    mc "I know so."
    "I stretch my arms out to Sayori."
    "As I reach, I feel my phone vibrate in my pocket."
    show sayori 1bq at face 
    with dissolve
    if c10e == 1:
        "I pull Sayori into another hug, this time she returns the motion."
        "She even holds me tighter than I had before."
        "I look over her shoulder at her wall clock and see there is still some time left in the day."
        mc "Hey Sayori, why don't we watch TV or something, like old times."
        s 1br "That sounds like fun, [player]!"
        show sayori 2bx at t11
        s "I'll set up the movie!"
        show sayori 2bq
        "Sayori hops up from the bed and moves over to her TV."
        "Her mood seems to have swung back into the happy one I'm so used to."
        show sayori at s11
        "After getting the TV set up, she takes a seat nudging up next to me."
        s 1bs "Aahhhh, so comfy~"
        "Sayori nests herself into my side as the show she picked starts to play."
        "I just hope she isn't getting any ideas..."
        "My phone vibrates again, and I switch it over to silent mode with the external switch."
        "Stupid mobile game notifications most likely."
        s 2bd "Thanks for staying today, [player]."
        s 2bl "You didn't have to or anything..."
        show sayori 1by
        mc "Well I wanted to stay, we haven't done anything like this in a long time."
        mc "What are friends for?"
        s 3bl "R-right, ehehe~"
        show sayori 1bq
        "I sink into the bed and focus on the show for a bit."
        "It feels like time just slips out from under me..."
        show sayori 1by
        "Soon enough however the credits roll for the episode and I Sayori sits up from her spot."
        s 2bl "Thank you again, [player]. That was really nice."
        s 4be "But it wasn't too much right? I didn't make you uncomfortable at all?"
        show sayori 1bd
        mc "Not at all Sayori, I would do this anytime. You don't have to worry."
        s 2bs "Okay! If you say so!"
        s 1by "But really.. thank you, [player]."
        s 3bm "Oh jeez it's getting really late! You should get going or you arn't gonna get enough sleep!"
        show sayori 2bn
        mc "Yeah I guess time flies, but if you need anything.."
        s 2br "I ask you, I know!"
        s 3bh "So for my sake and yours, don't jepordize your sleep. I'd feel bad if I kept you up."
        show sayori 1bf
        mc "Alright, I'll get some sleep then. Goodnight Sayori."
        s 4br "Goodnight [player]!"
        show sayori 1bq
        "I lift myself off the bed, giving one last wave to Sayori and head out the door."
    elif c10e == 0:
        "I move myself over to Sayori and offer her a hug that she accepts."
        "Even as she wraps her arms around me, I can tell that she is trying to hold herself back ever so slightly."
        s 1bl "You should probably be home working on homework and stuff right now, [player]."
        s 1bd "I wouldn't wanna keep you from important things."
        mc "Sayori your happiness is just as important to me, I don't mind spending as long as I need here."
        show sayori 4bx at t11
        s "I'm feeling just fine, look!"
        show sayori 4bq
        "Sayori beams a smile that, to me, seems genuine."
        "Maybe letting all this pressure off her chest really did help."
        mc "Alright, but you'll tell me if you're feeling down right? I'm always here to help when you need it."
        s 2bd "Yeah, of course."
        s 4br "Go have fun with your video games or your new guitar!"
        s 1bx "Bye, [player]!"
        show sayori 1ba
        mc "Bye Sayori, I'll catch up with you tomorrow."
    scene bg residential_evening 
    with wipeleft_scene
    "As I step into the cool evening air, my phone vibrates again."
    "I pull it from my pocket and look at the notification."
    "It's a message from Monika, multiple messages in fact, that she must have sent when I was with Sayori."
    m "{i}[player] im boooooorrreedddd, i wanna see u again <3{/i}"
    m "{i}Y r u @ Sayori's place, I can see u on our messaging app...{/i}"
    m "{i}...{/i}"
    stop music fadeout 1.5
    play music t7
    "Oh no..."
    "I start typing as quick as I can."
    mc "{i}Monika pls, something just came up and I had to go over 4 a bit{/i}"
    mc "{i}Sayori had an issue and I was helping her, ok?{/i}"
    "The messages almost immediately go from {i}Sent{/i} to {i}Read{/i}."
    "Three little dots appear as she types a response."
    m "{i}Sure she did.{/i}"
    "Perfect capitalization and punctuation, she's definitely upset."
    mc "{i}She rlly did though, it was serious Monika{/i}"
    "She immediately opens the message again, but no set of dots come up on the screen."
    "As I unlock my door to my house, I dial her number."
    scene bg livingroom_evening 
    with wipeleft_scene
    "The phone rings once before going straight to voicemail."
    mc "Come on Monika, please..."
    "I dial it again, and I'm brought to voicemail once again."
    "I hang up before it can record anything and chuck my phone at my couch."
    mc "God damn it Monika! What has gotten into you?!"
    "Sinking into the couch with my face in my hands, all I can do is think."
    "She doesn't think..."
    "No god please..."
    "Surely she knows I’d never do something like that."
    "I’m the school loner, for Christ’s sake, jeopardizing a relationship as good as this would be more than stupid of me."
    "I clutch my hair in my fists in panic, beads of sweat forming on my forehead."
    "My breathing speeds up to a noticeable high."
    "Afraid of pulling my hair out, I let go and take up my phone once more."
    mc "{i}You know how much I care for you. Sayori needed help, I promise that’s all it was.{/i}"
    mc "{i}Please, just talk to me. Giving me the silent treatment isn’t going to solve anything.{/i}"
    "I was too forward."
    "She’ll see that as aggressive or defiant."
    "As I move my finger towards the delete button, I see the three dots appear once more."
    "Oh no."
    "She’s seen it already. No going back now."
    "All I can do is brace myself for the response…"
    "{i}...{/i}"
    "{i}...{/i}"
    "{i}...{/i}"
    m "{i}Alright, I’ll talk.{/i}"
    "Thank Christ for that, I feel myself breath again."
    m "{i}I want you to tell me the truth. I want you to swear that your answer to my next question will be true.{/i}"
    "Oh boy, this is gonna be a tough one."
    "Nonetheless I will answer truthfully."
    mc "{i}I swear.{/i}"
    m "{i}Alright.{/i}"
    m "{i}Are you and Sayori involved in any way?{/i}"
    "I can’t believe she’d really think that, does she not trust me?"
    "I should reply quickly, she won’t take kindly to waiting for a response."
    mc "{i}Of course not.{/i}"
    mc "{i}She’s my close friend and she was having a bad day.{/i}"
    mc "{i}We sat down and talked together, I let her vent what was on her mind, and I listened.{/i}"
    mc "{i}I promise that’s all that happened.{/i}"
    "The dots return once more."
    m "{i}I believe you.{/i}"
    "I feel a weight lift off my chest, thank the stars above."
    "Just as I take a deep breath, my phone starts to ring."
    "I look down to see just who I thought was calling."
    "I tap the answer button and put the phone to my ear."
    stop music fadeout 3.0
    mc "Hey."
    play music t10
    m "Hey.."
    mc "Monika, I-{w=1.5}{nw}"
    m "I'm sorry [player], I'm.. I.."
    "Her voice is shakey over the phone, and I feel myself sit up a bit."
    mc "Monika wait, is something-{w=1}{nw}"
    m "I'm sorry I'm like this [player], I just.."
    m "I don't know why I get like this, I don't mean to..."
    m "I don't want to be overbearing or mean or anything like that!"
    m "But when you didn't answer like usual.."
    extend " and then I saw you were with Sayori.."
    m "Please don't hate me [player].. I know that-{w=1}{nw}"
    mc "Monika, I could never hate you."
    mc "You've done so much for me that I could never thank you enough."
    mc "I know things didn't look good when you tried to text me, and I'm sorry that I scared you like that."
    mc "But please, just remember this.."
    mc "I love you Monika, and no one else."
    m "[player]..."
    "A warm silence falls between us as I hold the phone."
    m "I'm sorry I got mad at you, I was just so scared for a time there.."
    m "I just get so scared..."
    mc "I’ll help, I promise I'll help make everything better."
    m "Gosh, that’s what I mean when I say you’re a sweetheart, [player]."
    m "You're always willing to help people, even with stuff like this."
    m "That's why I love you, [player]."
    mc "And that's why I love you too, Monika."
    "I hear a russle of a blanket against her phone and I let out a sigh of relief."
    mc "All tucked into bed I'm guessing?"
    m "Yeah, though I'm glad I'm going to bed happy now rather than angry or upset."
    mc "I'm sorry, I didn't mean to.."
    m "Come on, we've both said that too many times now, ahaha~"
    m "How about we say something else more, I'll start."
    m "I love you~"
    mc "I love you too."
    m "Goodnight [player], love you."
    mc "Sleep tight, love you too."
    m "Sleep.. tight.."
    m "Love.."
    extend " you..."
    "I listen closely till I'm sure she's asleep."
    "Finally my arms fall to my sides and I take a long drag of fresh air."
    "I love her so, so dearly but I can't deny anymore that she's been almost too much when she gets like this."
    "But I'm serious when I said I’d help, to her and to Sayori."
    "Monika's emerald eyes are too pretty to be tainted by envy, and Sayori's not fit for tears of pain."
    "She was right, maybe I do always jump in to help people."
    "I can't help but chuckle as I let the last of the stress dissipate."
    "Looks like I'll be pushing off that essay for another day yet again."

#C11
    scene bg corridor 
    with dissolve_scene_full
    play music t3
    "Classes are over once more, and it’s time to head to the clubroom."
    "As always, the halls are fairly crowded with students heading either to their clubroom or home."
    "I’ve managed to cram in a few more days of guitar practice."
    "Honestly, it feels great, I feel like I’m making actual progress."
    "If it wasn’t for my fingers aching, I’d say it did nothing but good for me over the past few days."
    "The teacher on the videos actually said that callouses in my finger tips actually improves my ability to pluck and strum strings."
    "I just wish they would develop faster-"
    show monika 1d
    m "Woah!"
    extend 2i " [player]!"
    show monika 2h
    mc "Ah!"
    "In my daydream I’d nearly walked past the clubroom door and straight into Monika, who was standing just outside."
    m 2g "Are you alright [player]? You looked like you were out of it for a second there."
    show monika 1c
    "She takes a second to straighten my blazer and run her hands over me looking for anything out of the ordinary."
    mc "Yeah, sorry, I must’ve gotten lost in my thoughts."
    m 2e1 "Well don't go so deep in them next time, you'll hurt yourself if you're not paying attention."
    show monika 2e
    "Monika gives me a peck on the cheek before beckoning me in."
    scene bg club_day 
    with wipeleft_scene
    show monika 2b at l11
    m "Funnily enough, you’re not the last one to show up."
    show monika 2a at l21
    show yuri 2h at t22
    y "You’re right, Natsuki isn’t here yet."
    y "How odd…"
    y 2g "It's not like her to be this late to a meeting, she's usually one of the first here."
    y 2l "She could be held up in a class but she would have told us, or at least me, that she'd be behind."
    y 3p "Ah, I’m rambling again..."
    y 2v "Sorry.."
    show monika 2e
    show yuri 4b
    "She clutches one of her purple locks, and looks down at the paper on her desk."
    show monika at t31
    show yuri 4a at t32
    show sayori 2h at t33
    show sayori at f33
    s "Hey, it’s okay Yuri!"
    s 1x "I like your rambling."
    show monika 1c
    show sayori 1a at t33
    show yuri 4d at f32
    y "S-Sayori?!"
    show yuri 4a at t32
    show sayori 3r at f33
    s "Yeah, they make me feel smarter!"
    show monika 1c
    show yuri 2u at t32
    show sayori 1q at t33
    "How does that even work?"
    "Yuri seems to shuffle out of her uncomfortable look and puts on a smile as Sayori beams her own."
    show monika at f31
    m 4g "Hmm, she’s still not here, and the hallways are almost empty."
    m 2g "Maybe she went home early today.."
    show monika at t31
    show yuri at f32
    y 2w "But I was sure I saw her earlier.."
    show yuri 2o at t32
    show sayori at f33
    s 2h "Yeah, so did I!"
    show sayori 1g at t33
    show monika 2p at f31
    m "Strange..."
    show monika 2o at t31
    "Natsuki had been acting strange recently, I hope everything is alright."
    "She isn't the type to go out without someone knowing, so I don't think she'd flake on us.."
    "But with no one knowing the real answer we could only guess."
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    "After a moment we all went back to our spots and began our writing pieces for the newspaper."
    "The deadline for this next piece is soon, I should really pull my weight especially after finding myself dragging behind."
    "And of course, as I sit down a wave of discomfort comes over me."
    "I needed to head to the bathroom."
    scene bg corridor 
    with wipeleft_scene
    "I excuse myself and make my way outside the club room."
    "The hallways are near dead empty now, save for the ambiant noises of the school and other clubs in the distance."
    "It's a peaceful sound, almost soothing as I think of things to write when I get back."
    scene bg h_corridor 
    with wipeleft_scene #<-- May want to import DDLC+ Staircase here
    "When I finally finish my business, I take a moment to freshen myself up at the sink."
    "With a new found energy I take a step out of the bathroom into the hallway once again."
    "However as I start back to the club room, I notice someone right across from me."
    show natsuki 1s at t11
    show natsuki at s11
    "Natsuki is seated on a bench right by a vending machine, tapping away at her phone."
    "She doesn’t seem to notice me as I approach."
    "Or perhaps she does and is trying not to show it."
    mc "You know Natsuki, the club is worried about you."
    n "..."
    "I sigh and take a seat next to her, keeping a good space between us just in case."
    mc "You can tell us if something is bothering you, we're here to listen."
    n 1q "Why do you care?"
    stop music fadeout 2.0
    show natsuki 1s
    play music t9
    "She seems to bury herself deeper into her phone."
    mc "Because you’re out here on your own during a club meeting."
    n 1r "Why do you decide to care now?"
    n 1t "Are you trying to police my actions or something?"
    n 1u "Just a minute ago you didn’t even acknowledge my existence."
    mc "What do you mean? I would never-"
    n 2m "When you first got here, I waved at you before you went into the bathroom."
    n 2n "You didn’t even look my way."
    mc "I-I’m really sorry Natsuki, it was an honest mistake I swear."
    mc "I really haven't been well focused today it seems.."
    n 2q "Yeah, well that seems to be a common trend as of recently."
    n 22c "Actually, who am I kidding, people haven’t seen me my whole life."
    n 12a "And when I finally find a place where I feel seen, some romance shows up and I’m back to being invisible."
    show natsuki 12b
    mc "Natsuki.."
    n 1r "Look, I don't want the pity party okay?"
    n 1q "I just wanted some time to myself.."
    show natsuki 1s
    "Natsuki seems to tap harder at her phone, and I find myself looking at the ground."
    "A hard silence surrounds us, almost crushing me with an unbearable pressure."
    mc "You arn't invisible in the club, you're far from it."
    n 1r "So why the hell does Monika latch on to you like a damn parasite then. It's a struggle to get her to talk to anyone else besides you when you're around."
    n 1x "Sayori has been a worse space cadet since you two started, and Yuri is the only one that hasn't fallen apart yet."
    n 22c "I knew something like this would happen if a boy got involved with us."
    n 22e "I knew..."
    extend 12f " "
    extend 12i "we didn't stand a chance in hell."
    show natsuki 12f
    "Natsuki lets her phone fall into her lap, as tears start to roll down her face."
    mc "Natsuki I.. I don't understand, I-"
    n 12i "I always knew Monika would steal you away from us... from me.."
    n "I didn't want to be right, but I was."
    n 12c "Why did she get to have the happy ending, huh?"
    n 1p "Why couldn't it have been me?!"
    n 12i "Why couldn't it have been fuck'n me?"
    show natsuki 12f
    "It felt like a swarm of icicles pierced through me as I sat in awe."
    "Her too? Did they all fight for my attention in the beginning?"
    mc "Natsuki I..."
    extend " I'm sorry.."
    n 12i "You always say that [player], it's always I'm sorry."
    n 12c "Sorry just doesn't cut it."
    show natsuki 12f
    "I feel utterly powerless sitting here."
    "I sat in awe as a girl next to me, someone I'd call a genuine friend, sits covered in tears and I could do nothing."
    mc "Please Natsuki what can I do to make things right, to make you feel seen?"
    n 12h ".{w=.75}.{w=.75}.{w=.75}"
    show natsuki 12f at face 
    with dissolve
    play sound fall
    "Without a word of warning Natsuki closes the distance between us and wraps her arms around me, burying her face against my chest."
    n 12i "Just let me be selfish for a bit. I don't care if you hate me after."
    n "I just.. want to feel noticed."
    show natsuki 12f
    "I was beyond suprised by all this, but after looking around to assure myself no one was looking on I slowly placed one arm around Natsuki and another on her head and ran my hand through her hair."
    show natsuki 12h
    mc "As long as you don't tell anyone, I just want things to be okay again."
    n 12i "If Monika found out, she'd kill us both anyway."
    show natsuki 12d
    mc "I'm sure I could try and explain it all."
    n 1m "I'm serious, you know her better than anyone."
    show natsuki 1n
    mc "I know, but right now I'm doing my best to help you."
    n 1h "You're just enabling me, you're not even fighting back."
    show natsuki 1u
    mc "I know, but you've calmed down at least."
    show natsuki 12b
    "We stay in this awkward hug for a short while until I felt Natsuki shifted herself under me."
    show natsuki 1q at t11
    n "I still can't go back to the club today. I still.. want to go through my thoughts."
    show natsuki 1n
    mc "That's okay, I won't force you to do anything."
    n 1m "You won't tell the other's you saw me right?"
    show natsuki 1n
    mc "If you don't want me to I won't. Promise."
    n 2q "Alright, that's good.."
    n 2u "..."
    n 2m "[player], does this mean.."
    show natsuki 2n
    mc "Mean what Natsuki?"
    n 2q "That you.. "
    extend "well.."
    show natsuki 2n
    "Oh, I see what she's getting at."
    mc "Natsuki, I love Monika with all my heart."
    mc "You're still an amazing friend and someone I would trust wholeheartedly with anything."
    show natsuki 12a
    mc "But saying that, you have to understand that its diffrent with her. I care about everyone in the club but with Monika.."
    n 12c "I know, its diffrent. I wouldn't expect you to change your heart with one stupid hug."
    n 2y "Hell, I'd be really pissed at you if that's all it took to make you fall for a girl."
    n 2q "I'll be fine, I'll figure this out and get over it. I have to at this point."
    show natsuki 2n
    mc "Just don't leave your friends out of helping you. We care about you Natsuki, I promise."
    n 2t "I get it, I get it. Just let me be edgy with my feelings once and a while."
    n 4y "Now get going, before they send the hound out to get you. Then you'll really be in trouble."
    show natsuki 4a
    mc "Alright, take care Natsuki."
    n 3d "See ya, [player]."
    show natsuki at thide
    hide natsuki
    "I pick myself up off the bench and start my way back to the club room."
    stop music fadeout 3.0
    scene bg corridor 
    with wipeleft_scene
    play music t3
    "As I walked back I felt a wave of thoughts pour over me."
    "It already felt awful to have Sayori cry to me about how she felt, but now Natsuki had felt the same as well."
    "It's not like I wanted to make them sad, I wouldn't do that on purpose."
    "Everything is just so damn confusing..."
    show yuri 1f at t11
    y "[player], there you are!"
    y 1b "I was starting to get worried when you took so long."
    "Just as I was getting close to the club room, Yuri came around the corner."
    show yuri 2e
    mc "O-oh, hi Yuri. Sorry, I didn't realize how long I was gone."
    mc "I guess I should thank you for being concerned about me."
    y 3q "I-it was nothing [player], I-I just happened to notice is all."
    y "I wondered if there was something wrong, a-and I came out to go check on you but here you are."
    show yuri 2s
    mc "I'm fine Yuri, just took my time I guess.."
    y 1j "And there's nothing wrong with that, I guess I jumped to a silly conclusion in my head is all."
    show yuri 2e
    "Yuri starts to turn towards the club room, but she stops herself and stares at my chest."
    y 2f "Ah..."
    y 3o "S-sorry, I just.."
    mc "Hmm? What's wrong?"
    y 2p "N-nothing!"
    extend 2q " I just.. noticed that spot on your shirt there.."
    y 4d "I-I'm sorry, I don't mean to be rude!"
    show yuri 4c
    "Confused, I look down and find a sizable wet spot in a skin tone color on my shirt at chest level."
    "After a second I realized how that could have got there."
    show yuri 4a
    mc "O-oh! This, well I just.. splashed some water on my face and it got on my shirt is all!"
    mc "Haha, silly me not noticing."
    y 2q "Oh.. well that's a relief it's just water."
    y 1d "Try to be more careful next time!"
    show yuri 1c
    "Yuri chuckles to herself and I feel myself doing the same as I try and subconsciously wipe the spot off my chest."
    show yuri at thide
    hide yuri
    scene bg club_day 
    with wipeleft_scene
    "After club finished we all packed up our things and started to clean up the clubroom for the weekend."
    "As I started to do my part, the events of today started to slip into my mind again."
    "How Natsuki latched onto me, and that horrible feeling of being powerless to help her."
    "I couldn't stand by and do nothing, I needed someone's help."
    "I ushered at Yuri and pointed out the door."
    scene bg corridor 
    with wipeleft_scene
    show yuri 1f at t11
    y "What's the matter, [player]?"
    show yuri 1e
    mc "Well.."
    "I know I probably shouldn’t say this, but Natsuki is her friend too."
    mc "Natsuki is here, in school."
    mc "Or at least she was, she might have left by now though."
    show yuri 1g
    mc "Point is, I found her sitting on one of the benches when I went to the bathroom."
    mc "She seemed upset at something, and I tried to talk to her."
    mc "One thing lead to another and she.."
    y 1h "..let her emotions finally slip."
    show yuri 1g
    mc "U-uh.. yeah.."
    y 1l "I see."
    y 1b "Well I'm glad she's not sick or missing or anything like that."
    y 2h "But if she's still hurt over all of this.."
    show yuri 2e
    mc "Wait, you knew Yuri? About how.. she felt?"
    y 2q "W-well I.. um.."
    y 2v "Yes, I had known for a while."
    y 3q "I guess it's only natural, when you get involved with a bunch of girls like us for a time things are bound to spark."
    show yuri 2s
    mc "I-I guess.. but I didn't mean to hurt her like this.."
    y 2l "[player], you shouldn't blame yourself for this."
    y 1h "There's only so much you can do to make everyone happy."
    y 1b "I know she understands, but this will just take time."
    y 2h "Yeah.. time heals all wounds."
    y 1f "Do you know if she's still here? Maybe I can talk to her."
    show yuri 1e
    mc "I'm not sure actually.."
    mc "But she told me not to tell anyone! So please if you do see her don't tell her that you know I saw her!"
    y 1b "Alright I won't let her know that we spoke, though I wouldn't put it past her to have suspicions."
    show yuri 1a
    mc "I hope not, thank you."
    y 1b "Thank you, [player], for letting me know. I won't let you down."
    show yuri thide
    hide yuri
    "Yuri grabs her bag from the club and makes her way down the hallway."
    "I feel a slight relief as I turn back towards the club room."
    scene bg club_day 
    with wipeleft_scene
    show monika 2e
    "Monika is waiting for me by the door, leaning on her broom."
    mc "Hey, sorry I got distracted."
    m 2n "It's fine, thought I almost thought you were gonna walk home with her or something."
    show monika 2m
    mc "Come on, you know I wouldn't leave you high and dry like that."
    m 4e "I know, I know, but I can still worry."
    m 2b "Anyway, Sayori finished her stuff and left already so that just leaves us."
    show monika 2a
    mc "Yeah, I suppose it does. We should probably wrap this up and get going too."
    show monika 1j
    "We put the last of the cleaning supplies away and lock the room, linking arms with each other as we walk to the street."
    scene bg residential_day 
    with wipeleft_scene
    show monika 1j at l11
    "A strong breeze fills our hair, and the air is much cooler."
    "Despite the sun still being up, it feels like twilight as it hides behind a thick layer of clouds."
    show monika 1m
    "As a result, everything feels far heavier."
    "Inhaling almost takes effort."
    m 1n "So.. what were you and Yuri talking about earlier?"
    show monika 1e
    "She looks at me with a soft face but her eyes told a diffrent story."
    "They knew something was up, but I promised Natsuki.."
    mc "We were..."
    extend " talking about Natsuki."
    m 1d "Hmm? What about her?"
    show monika 1c
    "Monika seemed to perk up as I said it."
    mc "Well.. Yuri seemed pretty concerned about Natsuki throughout the club meeting."
    show monika 1e
    mc "So I decided to check in with her, ya know? See if she might know what was going on with her."
    m 1m "Mhmm.."
    "Monika turned her head a bit as we walked for a bit farther."
    mc "Hey, is something-{w=1.5}{nw}"
    m 1p "You know it's not fair to just tell Yuri the truth but not your girlfriend."
    show monika 1o
    "We both came to a hault as I turned to Monika confused."
    mc "W-what do you mean? I just-{w=1}{nw}"
    m 1g "I'm sorry, I didn't mean for that to sound mean."
    m 1n "But..when you were talking with Yuri I couldn't help but listen through the door.."
    m 1g "Did something happen when you were gone from club today?"
    show monika 1f
    mc "Monika, I.."
    "Crap, caught right in the lie."
    "I sigh, sorry Natsuki but she's got a bite on me and won't let go."
    mc "I'm sorry too, I just.. had wanted to respect Natsuki's wish to not tell anyone."
    mc "But it was all so much I just.. I had to tell someone."
    m 2g "But why not tell me then?"
    show monika 2c
    mc "Well just cause.."
    extend " ah well you know.."
    m 2p "It was something about me then, right?"
    show monika 2o
    mc "Yeah, kinda..."
    "We both stand in the sidewalk, Monika looking to the ground and me feeling like a wall fell on me."
    m 1r "So what happened then?"
    show monika 2q
    mc "Well nothing too much, just-{w=1}{nw}"
    m 1i "[player], I saw the makeup on your shirt eariler and I know Yuri saw it too."
    m "What did Natsuki and you do?"
    show monika 2h
    mc "Monika, she.."
    "Monika stared me down as I tried to find the words I wanted to say."
    "As I tried, those moments creeped back into my mind and the emotions with them."
    "I felt myself loose any hold I had on my own feelings"
    show monika 1d
    mc "She cried, Monika! She cried.."
    show monika 1f
    mc "She cried and it was all my fault.. I hurt her and I didn't even mean to.."
    "I could feel my voice quiver and a pressure building in me"
    mc "How did I not see how she felt, it should have been obvious.."
    m 1g "[player]..."
    mc "Her, Sayori, you! I can't stop making everyone upset!"
    mc "I never wanted to make anyone feel this way.. especially not any of you girls.."
    "At that point I felt the first tear roll down my cheek."
    play music fall
    show monika 1e at face 
    with dissolve
    "Monika took a step forward, wrapping me in her arms as she looks into my eyes."
    m 1e1 "[player], I meant what I said before, about you being such a wonderful person."
    m "You try and make everyone happy, even in their worst hour."
    m "I really couldn't ask for a better partner."
    m 1n "Even if I do get a little jelous about it from time to time."
    m 1g "But it breaks my heart seeing you hurt like this."
    m 1e1 "You can always come to me if things feel like they're too much."
    m "I'll always come to understand, even if I seem mad at first. I promise."
    show monika 1e
    mc "Monika.."
    "She takes her hand and wipes my cheeks and eyes clear, keeping a warming smile beaming off her face."
    mc "I'm sorry, It's just been so much. I'm sorry.."
    m 1e1 "Hey, what did I say about saying sorry too much."
    show monika 1e
    mc "Fine.. "
    extend "I love you."
    m 1e1 "I love you too."
    show monika 1j
    scene black 
    with close_eyes
    "She closes the distance between us and we lock lips for a bit."
    "The pressure finally feels lifted off me and I could breath again."
    scene bg residential_day 
    with open_eyes
    show monika 1e at face 
    with dissolve
    m 1e1 "Now come on, we'll catch a cold if we stay outside like this."
    m "Let's enjoy the walk together like we always do."
    show monika 1e
    mc "Okay.."
    show monika 1j at tll 
    with dissolve
    "Monika takes my hand and we start again down the road."
    "I try and straighten myself out, hoping I don't look like an idiot as we walk together."

#C12
    scene bg bedroom 
    with dissolve_scene_full
    "Another Sunday.."
    "My clock tells me it’s nine o’clock in the morning."
    "Monika should be here pretty soon."
    "I stretch out my arms and allow my legs to spasm slightly."
    mc "Guuah!"
    "The covers feel slightly lighter today as I peel them off."
    "I'm.. not tired right now?"
    "That girl has really changed my internal clock, huh?"
    "I chuckle to myself as I stand up and put on some half decent outfit for the day and head downstairs."
    scene bg kitchen 
    with wipeleft_scene
    "I assemble a small breakfast for myself, another humble bowl of cereal."
    "Just as I'm scrolling through videos to eat to, a text pops up on my screen."
    m "{i}Good morning! I’ll be leaving in a few minutes, see you in a bit!{/i}"
    "I can't help but grin as I tack out a response."
    mc "{i}Good morning 2 u too! I’ll be here waiting{/i}"
    scene bg livingroom 
    with wipeleft_scene
    "I wrap up my breakfast and move into the living room."
    "Should probably pick up some of the junk lying around here."
    "As I walk over to the couch I notice the guitar case tucked at it's side and pull out the instrument."
    "Plucking a few strings, I feel the notes ring out around the room."
    "The feeling of progress also rings in my head, who would've thought I'd figure this thing out in just a couple weeks."
    "Granted I'm no pro, but I can get a few basic songs out."
    "I find myself sitting down on the couch and running through one of those basic songs once again."
    scene bg livingroom 
    with wipeleft_scene
    "About twenty minutes later, I hear my favorite knock."
    mc "Just a sec!"
    "I set down the guitar on the couch and make my way over to the front door."
    "The locks click over and I swing the door open."
    show monika 2bb
    m "Heya, [player]!"
    mc "Heya, come on in."
    show monika 2bj
    "I show Monika inside and we make for the couch."
    m 2bb "Ah I was right, I thought I heard you playing this."
    show monika 4ba
    "She grabs my guitar from the couch and sits down with it across her lap."
    show monika 1ba
    mc "Mhm, figured I could practice a bit before you got here."
    m 3bk "My [player] being studious in extracurricular activities? I never thought I'd see the day!"
    show monika 1bm
    mc "Hey! I can enjoy playing this in my free time, it's why I got it!"
    m 1bl "I know, I know, I'm joking silly."
    show monika 1bj
    "Monika carefully sets the instrument down on the coffee table in front of her."
    show monika 1bm
    "She then averted her gaze a bit from me, figeting with her hair a bit."
    mc "Monika, what's wrong?"
    m 1bn "Nothing, just um.."
    extend 1bp " don't get mad at me right away, okay?"
    show monika 1be
    mc "Well when you put it like that I can't help but be worried now."
    m 3bn "It's nothing bad, but since I want us to be honest with each other after school the other day.."
    m 1be1 "Well I got in touch with Natsuki after we got home that day."
    show monika 1be
    mc "O-oh.."
    m 3bn "Well, I had to play a bit of telephone with Yuri to get to even talk with her but it all worked out."
    m 1be1 "But we got to talk a little at least."
    m 3bn "She was kinda mad at first cause she figured I'd get involved at least a little bit, ahaha~"
    m 1bg "And Yuri kinda "


    mc "So, you said you had a plan for today?"
    "She gets up and opens the bag, beginning the setup process, unfolding the stand and the like."
    m "Yeah, something different to our usual practice."
    "Her words and sentences have pauses between them, filled by grunts of exertion as she lifts her remarkably heavy piano."
    mc "Need a hand there?"
    m "It’s fine I’m almost…"
    "A dull click is heard as the instrument is affixed onto its stand."
    m "...Done."
    "Despite having known her for as long as I have, her physical capability never fails to impress me."
    "She’s far stronger than I am, and a long time ago that embarrassed me."
    "Now, though, it doesn’t, in fact I’d go so far to say that I’m proud of it."
    "It means she sees something in me that isn’t my physical appearance or my body, and has decided she wants to stay because of it."
    "That’s absolutely something to be proud of."
    "I realize my head has gone higher than the giant beanstalk, and pull it back down to earth."
    mc "So, what’s your plan?"
    mc "Have you found another instructor?"
    "She pokes a few keys to make sure everything is in order."
    m "Actually, we’re not doing any tutorials today."
    "No tutorials?"
    m "I thought we’d give your skills a test drive, see how they are and what needs to be improved."
    "We have been at this for a while, so that is a sound idea."
    mc "Alright, what’s your plan?"
    m "A duet!"
    "So that’s why she brought her piano."
    m "Well, what do you think?"
    "I realise that I’d been silent for a good five seconds."
    mc "Sure, that sounds like a good idea."
    mc "It gives you an opportunity to hit a few keys yourself, so that’s never a downside."
    mc "What will we be playing?"
    "She takes a small stack of papers from her bag, and sorts them into two piles."
    "I take one, and she holds onto the other."
    m "What you have is the guitar component of the song, and I have the piano component here."
    "The papers show the notes I’ll be playing in the duet, no doubt the same goes for her."
    m "Don’t worry, it seems long but it’s fairly simple, there’s not a lot of intense chord work going on."
    mc "Hang on, this looks familiar."
    "During my practice, I gained a limited ability to read music."
    "She looks over to me, visibly pleased that I recognise her work."
    m "Yep, it’s an extension to the song I wrote all those months ago, on the first week we met."
    "This works great for me, I’ve got a lot of happy memories associated with this song."
    mc "Well, are you ready?"
    m "Not just yet, I don’t have a chair."
    "Ah."
    "I rush over to the table and pull a chair over to where she’s standing."
    "She sits down before her piano, cracks her knuckles and places her fingers atop her starting keys."
    "The guitar sits firmly within my arms, my fingers already pressing against the frets I’ll open with."
    m "Ready?"
    "I nod in response."
    m "Alright, three, two, one, and…"

    #Cutting out the minigame that was supposed to be here. Just insert a time skip

    "That honestly went way better than I expected it to."
    "Monika takes a deep breath and removes her hands from the keys."
    "She seems pleased with how that turned out."
    m "You were great, [player]!"
    mc "So were you, you really blew it away."
    m "Well, I’ve been practicing for longer."
    m "You’ve only been at this for a couple of weeks and you’re already doing well."
    m "I’m proud of you."
    "A small smile grows across my face."
    mc "Yeah, so am I."
    "Monika’s eyes seem to light up at this."
    m "Confidence is where half a musician’s talent comes from."
    m "You’d do well to remember that."
    mc "Hah, thanks, will do."
    "She raises an eyebrow and smirks."
    m "And I don’t think you’re quite there yet."
    mc "Oh?"
    "Damn, she’s onto me."
    m "I know just the thing to fix that, or at least help."
    mc "What’s that then?"
    "Something tells me I’m not going to like this."
    m "We perform a duet for the club!"
    "Nail on the head."
    mc "Ah, I’m not sure, Moni-"
    m "Nonsense, you’ll do great!"
    m "You impressed me just now, no doubt the others will be impressed too."
    "I know two things."
    "The first is that doing this will almost certainly embarrass me beyond belief."
    "The second is that refusing will break Monika’s heart."
    "It looks like I have no choice."
    "Here goes."
    mc "Alright, I’ll do it."
    m "You will?"
    mc "Yeah, I will."
    m "No strings attached?"
    mc "None at all"
    "She pauses for a moment, then leaps from her seat onto my lap, and wraps me in her arms."
    m "Thank you, thank you!"
    "I definitely made the right decision."
    "Any degree of humiliation is worth seeing her this happy."
    m "You have no idea how much this means to me."
    mc "You’ve given me a pretty good ballpark."
    mc "Now, if we’re gonna perform for them, we better make sure everything is on point."
    mc "I slipped up a couple of times during our duet, we should practice some more."
    mc "Are you down with that?"
    m "Yep, definitely!"
    "We practiced a few more rounds of the duet until we decided we had it in the bag."
    "I helped Monika pack up her things and bid her farewell as she left."
    "Man, I’ve put a lot of work into preparing for that fateful day."

    #[Wipe to black]
    #[Wipe to generic classroom, day]

    "And now that day is upon me."
    "Monika had dropped by for an hour or so over the past few days to cram in some more practice, as well as some solo warmups I did myself."
    "The guitar is safely in the clubroom."
    "I’m as ready as I’ll ever be."
    "My maths class just ended, and my final class before the club begins, computing, is about to begin."
    "One upside of this fact is that Monika shares this class with me."

    #[BG: Hallway, day]

    "As I approach the classroom, it doesn’t look like any teacher is present."
    "Well, there aren’t any looming exams or anything, so that’s not really a problem."
    "I enter the classroom and take a seat next to Monika."
    "She already has her books out, and a blank page that is soon to be filled with python code sits before her."
    mc "Hey."
    m "Heya!"
    "I let out a sigh as I lean back into my chair."
    "After a few seconds, Monika touches one of my hands."
    m "What are you doing?"
    "Without my knowing, I had been mimicking the strums and plucks I need to remember for the duet."
    "Damn, I’ve shown my hand."
    m "Are you still nervous?"
    mc "A little…"
    m "Our teacher isn’t in, I have a plan that’ll take this of your mind."
    mc "What’s your plan then?"
    "She alt+tabs over to a browser game of battleships."
    m "Bring up the same game on your computer and we’ll connect and have a game!"
    m "Sound fun?"
    "This is...not really like her."
    mc "Yeah, but don’t we have work to do?"
    m "As far as I’m concerned, not now we don’t"
    m "Besides, what are you gonna learn when you’re all stressed out like this?"
    "I’ll take a game of battleships over an hour of schoolwork any day."
    mc "Sure, give me a couple of minutes to set up."
    "I boot up the school computer in front of me."
    "As always, it’s using an OS that became outdated almost a decade ago."
    "It takes longer than I’d hoped to get everything ready, but by the end I’m seated in front of a prompt for a code."
    m "Alright, let me start up a lobby."
    m "Nice."
    "She shows me the 5 digit code for me to enter."
    "42069"
    mc "Nice."
    "We’re both in the lobby, and she starts the game."
    m "Remember, no peeking!"
    "Her screen is obscured as she turns her monitor away from me."
    "I follow suit and do the same."
    mc "Alright, get your ships ready."
    m "Already on it."
    "I put my ships in odd places, none near the middle, a few near the edges."
    "Once all my ships are down, a small green ‘Ready’ button flashes."
    "Monika is already ready."
    mc "Begin."
    m "Your turn, you go first."
    "B7 seems like a good place to start."
    m "Missed!"
    "One of the squares on my screen turns white."
    mc "No luck for you, I’m afraid."
    "The game continues with us both fairly neck-and-neck."
    "That eventually breaks when she finds my four-pin ship."
    mc "Damn.."
    "It appears that the curse wasn’t as obscured by my breath as I had intended."
    m "Found a big one, haven’t I?"
    mc "No comment."
    $s = teacher
    "The door swings open."
    s "Alright, everyone, sorry I’m late."
    s "Actually, there’s only about ten minutes left of the lesson."
    s "Staff meetings are a pain, but regardless I’m here now."
    "Our teacher has arrived, a tall, pale-skinned woman wearing formal attire."
    "She begins to walk around the room."
    "I begin to panic slightly as she approaches us."
    "Just as I’m about to tab out, Monika places her hand upon mine."
    m "I’ve got this."
    s "Monika, are you playing Battleships?"
    m "Yes, Miss, I am, with [player]."
    s "I don’t need to remind you that using the school network for non-educational purposes is against the rules, do I?"
    m "No, Miss, you don’t, but we’ve both finished our work and done extra, see?"
    "She opens a pair of books to reveal enough work to fill three lessons, even by our teacher’s standards."
    "One is hers, the other is a seemingly perfect forgery of my own."
    "I’m both impressed and humbled by her dedication."
    "Not to mention her ability to create such a convincing replica."
    m "We decided that if we carried on with the curriculum, we’d be too far ahead of the class."
    m "Neither of us wanted to put you through the frustration of making new resources for the minority."
    m "Plus, [player] here has a musical exam tonight, so I thought I’d play a game of Battleships to help him de-stress."
    s "That’s very noble of you, Monika."
    s "Good luck with your exam today, [player]."
    s "I can imagine it takes a lot to impress Monika, so if you’re half the man I think you are you’ll do great."
    s "I am, however, going to have to ask you to cancel the game."
    s "Mainly because the lesson is over in about two minutes."
    m "Will do, thanks Miss!"
    mc "Cheers, Miss, and I’ll let you know how it went."
    s "Please do!"
    "The bell goes shortly after, and everyone begins to pack up their things."
    s "Alright, everyone, I’ll set today’s classwork as homework and we’ll pick up from there tomorrow!"
    "I bundle everything into my bag and stand up in a hurry."
    m "I would’ve one that."
    mc "Nah, we gotta finish that game sometime."
    "We each go our separate ways as we head to our final class of the day."
    $s = Sayori

    #[Wipe to black]
    #[Wipe to hallway, day]

    "Lessons are over, and it’s time for the club."
    "Oh hell."
    "I actually have to perform in front of people."
    "It’s only three people, but that’s more than I’ve performed in front of before."
    "If I screw up, I won’t be able to go back in there."
    "Natsuki will pout and say I was stupid or incompetent."
    "Yuri will give me the silent treatment and feel horrible about it."
    "Sayori would start laughing halfway through at how bad I am."
    m "[player]!"
    "I turn around to see Monika behind me."
    "In my anxiety, I’d walked past the clubroom."
    "She walks up to me looking concerned."
    m "Still anxious?"
    mc "Yeah…"
    m "Come on in, they’ll love it."
    mc "Will do…"
    #Clubroom, day
    "Everyone is already here."
    s "Heya, [player]!"
    s "Monika said you were performing for us today!"
    s "Good luck!"
    y "Yes, I am looking forward to it."
    y "I’ve always loved the guitar as an instrument."
    y "The art of plucking a string to create a melody is one I find quite mesmerising."
    y "Ah, I’m really sorry, I-I’m rambling again…"
    "Sayori comforts her as Natsuki pipes up."
    n "A performance would be a nice change from all this writing."
    n "I know this is the Literature Club, but still, variety brings fresh air."
    m "See?"
    m "They’re all looking forward to it."
    m "So let’s get ourselves set up."
    "I head over to the corner of the room and unpack my guitar."
    "Monika is at the front, clipping the pieces of her modular piano together."
    "Everyone else is waiting patiently."
    s "What will you play?"
    m "Something I wrote up a few months back, you might recognise it."
    "I take a seat next to Monika, and strum all six strings."
    "It’s horribly out of tune."

    #If you learn tuner

    "No matter, I know how to tune a guitar."
    "All that practice didn’t go to waste."
    "Within a minute, the strums give a perfect noise."

    #If you don’t learn tuner

    "Damn."
    "I really should’ve learned how to use a tuner."
    "Oh hell."
    "This is bad."
    "This is really bad."
    "This is really really bad."
    "They’re all gonna hate me."
    "Monika seems to notice my freaking out, and begins to play each note under the guise of testing her own device."
    "After a few minutes of awkward silence and out of tune plucks, I’m ready."
    m "Okay, everyone, we’re ready!"
    s "Go for it!"
    n "Good luck."
    y "I look forward to it."
    mc "Let’s begin."

    #Again, cutting a minigame that was supposed to be here. Insert a time skip instead.

    "That honestly went far better than expected."
    "Everyone, including Monika, gives a small round of applause."
    "I quickly jump in and begin clapping too."
    s "That was really good!"
    n "Yeah, not bad."
    y "To learn such a complex instrument in such a short amount of time is an impressive feat."
    m "He really has learned a lot."
    m "He’s learned at a faster rate than me!"
    mc "I suppose I have, yeah."
    "I’m feeling really good about this."
    "Maybe I really did learn an instrument."
    scene black 
    with fade
    jump Monika5