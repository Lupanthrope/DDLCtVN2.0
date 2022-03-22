label Yuri2:
    $ y_name = "Yuri"
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ m_name = "Monika"

#For defintions file: Yuri asset references
#Mod Assets: BGs
#Black background
#image bg black = "mod_assets/black.png"

#Player house
#image bg bedroom_dirty = "mod_assets/bedroom_dirty.png"
#image bg livingroom = "mod_assets/livingroom.png"
#image bg livingroom_night = "mod_assets/livingroom_night.png"
#image bg livingroom_sunset = "mod_assets/livingroom_sunset.png"

#School
#image bg school = "mod_assets/school.png"

#Road Shots
#image bg road = "mod_assets/road.png"
#image bg road_sunset = "mod_assets/road_sunset.png"
#image bg road_night = "mod_assets/road_night.png"

#Bookstore
#image bg central_hub = "mod_assets/central_hub.png"
#image bg bookstore = "mod_assets/bookstore.png"
#image bg bookstore_sunset = "mod_assets/bookstore_sunset.png"
#image bg corner = "mod_assets/corner.png"
#image bg bowling_alley = "mod_assets/bowling_alley.png"

#Restaurant
#image bg resturant_front = "mod_assets/resturant_front.png"
#image bg resturant = "mod_assets/resturant.png"

#Yuri's House
#image bg yuri_house = "mod_assets/yuri_house.png"
#image bg yuri_bedroom = "mod_assets/yuri_bedroom.png"
#image bg yuri_bedroom_night = "mod_assets/yuri_bedroom_night.png"
#image bg yuri_bathroom = "mod_assets/yuri_bathroom.png"

#Hotel Scene
#image bg bus = "mod_assets/bus.png"
#image bg hotel_outside = "mod_assets/hotel_outside.png"
#image bg hotel_room = "mod_assets/hotel_room.png"
#image bg frozen_lake = "mod_assets/frozen_lake.png"
#image bg frozen_lake_night = "mod_assets/frozen_lake_night.png"
#image bg hotel_lobby = "mod_assets/hotel_lobby.png"

# Mod Assets: Yuri Arm Cut Images (casual)
#image yuri 2bnc = "mod_assets/yuri_cut/2bnc.png"
#image yuri 2boc = "mod_assets/yuri_cut/2boc.png"
#image yuri 2bpc = "mod_assets/yuri_cut/2bpc.png"
#image yuri 2btc = "mod_assets/yuri_cut/2btc.png"
#image yuri 2buc = "mod_assets/yuri_cut/2buc.png"
#image yuri 2bvc = "mod_assets/yuri_cut/2bvc.png"
#image yuri 2bwc = "mod_assets/yuri_cut/2bnc.png"
#image yuri 3bnc = "mod_assets/yuri_cut/3bnc.png"
#image yuri 3boc = "mod_assets/yuri_cut/3boc.png"
#image yuri 3bpc = "mod_assets/yuri_cut/3bpc.png"
#image yuri 3btc = "mod_assets/yuri_cut/3btc.png"
#image yuri 3buc = "mod_assets/yuri_cut/3buc.png"
#image yuri 3bvc = "mod_assets/yuri_cut/3bvc.png"
#image yuri 3bwc = "mod_assets/yuri_cut/3bwc.png"
#image yuri 3by2c = "mod_assets/yuri_cut/3by2c.png"
#image yuri 3by7c = "mod_assets/yuri_cut/3by7c.png"
#image yuri 3cwc = "mod_assets/yuri_cut/3cwc.png"
#image yuri 4bac = "mod_assets/yuri_cut/4bac.png"
#image yuri 4bbc = "mod_assets/yuri_cut/4bbc.png"
#image yuri 4bcc = "mod_assets/yuri_cut/4bcc.png"
#image yuri 4bdc = "mod_assets/yuri_cut/4bdc.png"
#image yuri 4bec = "mod_assets/yuri_cut/4bec.png"
#image yuri 4cc = "mod_assets/yuri_cut/4cc.png"
#image yuri 4fc = "mod_assets/yuri_cut/4fc.png"
#image yuri 4cnc = "mod_assets/yuri_cut/4cnc.png"
#image yuri 4fnc = "mod_assets/yuri_cut/4fnc.png"

#Mod Assets: Yuri Arm Cut (Uniform)
#image yuri 4ac = "mod_assets/yuri_cut/4ac.png"
#image yuri 4cc = "mod_assets/yuri_cut/4cc.png"

#Mod Assets: Music
#bird chirpings
#define audio.t12 = "<loop 0>mod_assets/12.mp3"
#wind
#define audio.t13 = "<loop 0>mod_assets/13.mp3"
#sunset sounds
#define audio.t14 = "<loop 0>mod_assets/14.mp3"
#define audio.doorbell = "mod_assets/doorbell.mp3"
#heartbeat
#define audio.t15 = "<loop 0>mod_assets/15.mp3"
#define audio.tbc = "mod_assets/tbc.ogg"
#define audio.monikasong = "mod_assets/monikasong.ogg"

#Scene 1    
    scene cg yuri_in_bed
    with dissolve_scene_full
    play music t12
    "..."
    "Woah..."
    "Just..."
    "Wow."
    "Did we... Really do that last night?"
    "This has to be a dream."
    "There’s...{w=0.25} No way I did it with someone this gorgeous."
    "Wait.{w=0.5} What time is it?"
    "I look over to Yuri, still sleeping on the bed."
    "She looks so beautiful."
    "How can I even wake her up?"
    y "Were...{w=0.5} Were you saying something?"
    y "I’m sorry, I didn’t understand."
    "Well, that answers my question."
    "I wasn’t trying to wake her up, but oh well."
    mc "It’s alright, you didn’t miss anything."
    "She yawns lightly, looking up."
    y "What time is it?"
    mc "Around 8 o'clock."
    y "Oh, okay."
    y "That gives us some time to get ready for school."
    scene bg bedroom
    with wipeleft_scene
    show yuri 1a at t11 zorder 2
    #show yuri (blanket custom) at t11 zorder 2    
    "She gets up, trying to cover herself with the blanket."
    stop music
    play music t5
    y "Oh no!"
    "Yuri starts panicking over something."
    "Did I do something wrong?"
    mc "What is it?"
    y "I didn’t plan to stay over. I don’t have my school uniform!"
    "Whew, I'm in the clear."
    "But this is really bad too! What do we do?"
    "Maybe...."
    mc "What if...{w=0.5} I went to your house to grab your school uniform?"
    y "What?!"
    y "Y-You don't need to do that. I'm sure there's another way."
    y "Maybe I can... Uh..."
    y "..."
    "Yuri is drawing a blank, she doesn't want me to go out and run like that, but..."
    mc "I can’t think of anything else right now, Yuri."
    "To calm her down, I get closer, and smile."
    mc "Don’t worry, I’ll be back soon."
    "I say this as unsure as she is."
    y "But, my house is so far away, you’re not going to have enough time."
    mc "Don't worry, I’ll be back on time."
    "{i}I hope.{/i}"
    "I get up, putting on a thick jacket and some fuzzy pants."
    "It’s tacky, but when have I ever cared about what I looked like outside?"
    "As I’m about to leave the room, Yuri shuffles over to the closet, covered by the blanket."
    "She starts rummaging through, emerging after a moment with another jacket and her house keys."
    y "I-I don’t want you to get a cold like last time."
    "I smile."
    "Even when things aren’t going well for her she still thinks of others."
    mc "Thanks."
    scene bg kitchen
    with wipeleft
    stop music fadeout 5.0
    "I head down the stairs. I haven't even started running yet and I can already feel some adrenaline kicking in."
    "To get there and back will take up most of the time before school. I’ll have to sprint on it."
    "I've gotta channel all the energy and athleticism I've got for this one run."
    "Taking a deep breath, I open the door."
    play music t13 fadein 5.0
    scene bg road
    with wipeleft
    mc "OH MY GOD, IT'S COLD!"
    "The freezing cold winds hit like a truck the moment I stepped outside."
    "I could barely stand in it, let alone move."
    "But I don't know what'll be colder, this temperature or disappointing Yuri..."
    "I pressed through the cold and began making my way."
    "..."
    "..."
    "..."
    "How long have I been running now?"
    "I wish I’d brought a watch or something."
    "I don’t go sprinting often.{w=0.5} Or at all..."
    "..."
    "How much further is it?"
    "My muscles are already aching."
    "..."
    "..."
    scene bg road
    with wipeleft_scene
    "After running for a bit longer, I see what appears to be a person ahead of me."
    "Is that…{w=1.0} Natsuki?"
    "Oh no."
    show natsuki 2c at t11 zorder 2
    "Before I could move my face away, it was already too late."
    "I had to rush down the street with Natsuki staring at me."
    "She seemed to have a rather confused expression on her face as I went to look."
    show natsuki 2d at t11 zorder 2
    "But the moment we made full eye-contact, I felt a smug sense of realization come from her."
    "Ah damn."
    show natsuki at thide zorder 1
    hide natsuki
    "I get the feeling I’ll be hearing plenty about this later."
    "But for now, I have to keep going. No point in worrying."
    scene bg yuri_house
    with wipeleft_scene
    "..."
    "..."
    "{i}Huff...{/i}"
    "{i}Puff...{/i}"
    "..."
    "..."
    "Is that...?"
    "Finally!"
    "I'm completely out of breath as Yuri's house finally appears in front of me."
    "I guess that's what I get for only being able to run to the ice cream truck."
    "I insert the keys and enter the house."
    stop music fadeout 5.0
    scene black
    with wipeleft_scene
    "I rummage through the house, feeling each second as they tick by."
    "I can’t see the outfit here."
    "Wait, why would it even be in the living room anyway?"
    "It’s too early to deal with this."
    "I stumble into a random room and hope it's in here."
    scene bg yuri_bedroom
    with wipeleft_scene
    "I have a feeling this is Yuri's room, with the whole book collection and all."
    "A part of me wishes I had time to look around, but I had to move quickly."
    "Now, where is that uniform..."
    "I look over to a closet and open it up."
    "Her closet was filled with many different kinds of intricate outfits."
    "But none of these look like a school uniform. All except-"
    "This one!"
    "I grab the outfit and dash out the front door, barely pausing to lock it."
    "Here we go again..."
    "My legs felt dead at this point, but I start the run anyway."
    scene bg road
    with wipeleft_scene
    play music t13 fadein 5.0
    "..."
    "..."
    "..."
    "Now that I think about it, I wonder what that book I saw was about." 
    "It didn't look like a published product."
    "Maybe it was a diary or something."
    "Hopefully I'll get a better look in the future."
    "Hmmm."
    "..."
    scene bg road
    with wipeleft_scene
    "I keep running on the road, eventually finding another person."
    "Wait a minute..."
    "Oh no."
    "As if my luck could only get worse."
    "Monika?"
    show monika 1a at t11 zorder 2
    "{i}Huff...{/i}"
    "I dash past her, hoping she didn't recognize me."
    show monika 1i at t11 zorder 2
    "As I look back, I could see Monika displaying a confused expression at first."
    show monika 5a at t11 zorder 2
    "But then suddenly, it changed to a smile."
    "Either she’s smiling because I look like a complete doofus..."
    "...Or because she figured out what was going on."
    show monika at thide zorder 1
    hide monika
    "That's two possible talks later..."
    "But not enough time to worry, gotta keep going."
    scene bg road
    with wipeleft_scene
    "..."
    "..."
    "{i}Ha...{/i}"
    "{i}Ha...{/i}"
    "{i}Ha...{/i}"
    "{i}Puff...{/i}"
    "Am I lost? I can’t be. I went in the same direction as before."
    "Is that... My house?"
    "Please…{w=0.5} Let it be my house…{w=0.5} My legs feel like jelly…"
    "Ah yes, it is! Finally..."
    stop music
    scene bg livingroom
    with wipeleft_scene
    stop music
    play music t5_yuri
    "I run through the entrance and see the couch, on which I immediately lie down to catch my breath."
    "I hear Yuri’s footsteps and hold the outfit up."
    mc "I...{w=0.25} {i}huff{/i}...{w=0.25} Have it…{w=0.25} {i}puff{/i}."
    #show yuri (blanket custom) at t11 zorder 2
    y "Oh my gosh! Thank you so much!"
    "She hugs me tightly, my face stuffed between her chest, then she runs upstairs."
    show yuri at thide zorder 1
    hide yuri
    mc "Worth it."
    "Some time passes, and I eventually regain the ability to stand."
    "Scenes from last night start replaying in my mind."
    mc "I still can't believe it."
    mc "Yuri and I... We really did it."
    show yuri 2b at t11 zorder 2
    "My thoughts are cut off by Yuri returning downstairs, now dressed in her school uniform."
    y "Thank you so much [player]!"
    y 2a "You should go upstairs and get dressed now."
    mc "Yeah, right."
    show yuri at thide zorder 1
    hide yuri
    "I head upstairs and enter my room to change into my own school uniform."
    scene bg bedroom
    with wipeleft_scene
    "I look at myself in the mirror."
    "That run really took away my ability to look like a normal person in public."
    "I'm completely drained right now. I really should listen to Monika when she tells me about her exercise tips."
    "Maybe then I'd be able to run 5 seconds without nearly passing out."
    "I grab my comb and fix the mess that is my hair."
    "While getting ready, I look at the bed."
    "It’s weird to think Yuri could have ended it right here, because she wants to be safe."
    "What does she want to be safe from?" 
    "Me? No, that doesn't make sense."
    "The club? No, that doesn't make sense either."
    "Whatever it is, I hope it doesn't come through."
    "I don’t want us to end, I don't want to lose her."
    "She means so much to me."
    "Hopefully what I’m doing now counts for something."
    scene bg kitchen
    with wipeleft_scene
    "I make my way downstairs after getting ready and find Yuri waiting for me."
    "She’s smiling about something, but I can’t tell what."
    show yuri 1u at t11 zorder 2
    y "I... I prepared breakfast while you were gone."
    y 3s "You must be very hungry after all that running."
    y 4e "Just for me."
    "I'm shocked."
    "I never took Yuri as the cooking type."
    "Or, more realistically, maybe I’m the only one out of the group who can’t make breakfast..."
    mc "Oh, thanks Yuri."
    "There on the table lie 2 sunny-side eggs."
    "I wolf them down. They're not perfect, but considering I don't even make myself breakfast, they're great."
    show yuri 1t at t11 zorder 2
    y "Do they taste good?"
    mc "Yeah! No complaints here."
    y 1u "That’s a relief."
    y 1s "I wasn’t too sure what to make."
    y 1h "There wasn't too much to work with."
    y 2n "Not that, uh..."
    show yuri 2e at t11 zorder 2
    mc "Don’t worry about that. I know that I don’t have everything I need."
    "..."
    y 1m "..."
    y "I can get used to this..."
    y "Waking up in the morning and preparing breakfast for you..."
    y 1b "Talking with you..."
    y "Then you go off to work."
    y 2c "And I get to read and write at home."
    y 2s "You come back tired and I tend to you."
    y 2q "You feel relaxed as we stay together..."
    y 4e "...Maybe do a few things."
    mc "..."
    y 2p "Ah, did I-"
    y "I'm sorry, I thought after last night that, oh--"
    mc "{i}Hahaha!{/i}"
    "I let out a soft chuckle in response to her scrambling."
    "I couldn't help it. She's just so cute when she gets like this."
    mc "Don't worry about it, Yuri."
    mc "I...{w=0.5} I feel the same way."
    "We share a sentimental look at each for a few moments before she speaks."
    y 2q "Oh, well...{w=0.25} That makes me happy."
    mc "That makes two of us."
    "I didn’t expect Yuri to go that far." 
    "But it’s calming to know how much she treasures me."
    show yuri at thide zorder 1
    hide yuri
    scene bg residential_day
    with wipeleft_scene
    show yuri 2g at t11 zorder 2
    "We finish eating and wait for Sayori outside."
    y "{i}Brrrgh...{/i}"
    y 2t "It feels so frigid outside today."
    y 1h "We’ve been standing out in the cold for a while now."
    stop music fadeout 2
    y 1f "I wonder what’s taking Sayori so long."
    "..."
    "Sayori sure is taking her time."
    "Is there anything going on?"
    "Maybe something I don’t know."
    y 1t "Are you alright, [player]?"
    mc "What? Oh, sorry. I kinda zoned out."
    mc "It’s just that... Sayori has been acting strange lately so I guess I'm getting worried."
    y 1v "Oh."
    y "..."
    y 1w "You must really care about Sayori."
    "Something about the way she said that doesn’t strike me well."
    show yuri 2v at t11 zorder 2
    play music t9
    mc "W-wait a minute, Yuri it's not-"
    y 2a "Don't worry. I know what you mean. You're a very caring person and just want to see your friends do well."
    y "You're always thinking of your friends, and constantly stick up for them."
    y "Your courage for what you believe in..."
    y 2c "...It's part of the reason I fell in love with you."
    "This girl, she's so understanding. How did I ever get so lucky?"
    "Without even noticing, I began staring at her, this time much longer than the last."
    "Without a single word she starts hugging me, and it's not like I was doing anything else, so I hug her back."
    "It's funny."
    "Even with the freezing cold temperature outside, hugging her just feels, {i}warm{/i}."
    "..."
    mc "How about we head to school now? We’re already set back as it is."
    mc "We could meet up with Sayori later."
    y 3s "Okay."
    show yuri at thide zorder 1
    hide yuri
    scene bg class_day
    with wipeleft_scene
    stop music
    play music t5_yuri
    "The school day continued on normally, despite our lateness."
    "Math, biology..."
    "And now to my ‘favorite’ part of the day: English."
    "The only interesting part here is Yuri though."
    "That sounds like a generic romantic movie, but it’s really true."
    "All I can do is stare at Yuri while she tries to focus on her work."
    "I bet if Natsuki were here she would call me out as a creep."
    "Then Sayori would try to defend me with a story from when we were kids. Monika intervenes with a laugh and teases me, challenging my normality."
    "As much as I would like to deny, I probably wouldn't have a comeback, and Natsuki would do that triumphic face she does as a result."
    "Only in the literature club can I be embarrassed and somehow get through the day."
    "Out of nowhere I’m asked a question by the teacher."
    $ n_name = "Teacher"
    n "[player], what is the purpose of the blood being blue in this chapter?"
    "Crap."
    mc "Um, the purpose of the blue blood is to show the grieving state of the victim. They know that they’re dying, and they're trying to come to terms with that."
    n "Correct."
    $ n_name = "Natsuki"
    "Phew, that’s a load off."
    "I’ve been noticing that after spending so much time with Yuri, it’s getting easier to answer these types of questions."
    "Maybe Yuri is rubbing off on me."
    "I see Yuri giving me a bright, knowing smile. That alone gets me through the remaining classes in a good mood."
    stop music
    play music t5
    scene bg corridor
    with wipeleft_scene
    "The school day finally ends and I go to the door for the literature club."
    "There's a note on the door."
    
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
    
    show yuri 1c at t11 zorder 2
    "At that moment, I see Yuri come up the stairs."
    y "Hello, [player]."
    mc "Hey Yuri, we have a message."
    y 1f "Huh?"
    "I hand the note to Yuri, which she sets back to the door after reading."
    y 1l "I see."
    "In the corner of my eye, I see a pink fluff at the stairs."
    "It’s Natsuki."
    "She looks at Yuri, and then me, turning her face from one of curiosity to one of disgust."
    "It was then that a thought must have struck her, as a huge grin began to grow on her face."
    "This won’t be ending well."
    show yuri 1f at t21 zorder 2
    show natsuki 2d at f22 zorder 2
    n "Hi guys, I just came over for the club today, and seeing the two of you here reminded me of something..."
    n 2y "What were you up to this morning, [player]?"
    show yuri 2n at t21 zorder 2
    mc "Me? Um, I don't know what you're talking about."
    n "Oh really? Because I saw this unassuming, scrawny, worn out guy running across the road this morning and thought you might know something about it."
    mc "Erm, well it can't be me, because I only wear my fuzzy pants at night."
    n 1d "Hey, how did you know he was wearing fuzzy pants? I never mentioned that."
    mc "Er, well…"
    "Crap, she totally has me cornered."
    mc "I was just, uh-"
    mc "Well, what were you doing up so early for school?"
    n "I just happen to walk to school that early."
    n "And how did you know I was even walking to school at the time?"
    n "The only way you would know about that was if-"
    "Oh no, here it comes."
    n "You were the wannabe marathon runner!"
    n "Do you have anything to say for your defense?"
    "Shoot, I have to think of something quick."
    mc "Uhh."
    mc "Hey, did you happen to notice that the club was canceled today?"
    show natsuki 1p at t11 zorder 2
    "Natsuki's face goes pale."
    n "What?!"
    show yuri 2e at t21 zorder 2
    mc "There’s a note on the wall."
    "Natsuki takes the note in a state of panic."
    show natsuki 1r at f22 zorder 2
    mc "Hey, Natsuki, are you alright? You look-"
    n 1u "Err... I... Need to go somewhere."
    show natsuki thide zorder 1
    hide natsuki
    show yuri 1f at t11 zorder 2
    mc "Whew, that was too close."
    y "I agree, but the way she reacted was very strange."
    y 2v "I really hope everything is alright for her."
    mc "Same here."
    "Me and Yuri stand there, thinking of what to say next."
    mc "Well, that gives us the afternoon to ourselves."
    show yuri 2e at t11 zorder 2
    mc "I mean, we don’t usually do stuff on weekdays but... uh..."
    "I'm suddenly overcome by shyness, and for once it's Yuri who breaks the awkward silence."
    y 1c "I’d love to, [player]."
    y 1b "You sounded like myself there."
    mc "I guess I did."
    show yuri 1a at t11 zorder 2
    "Yuri really has been rubbing off on me."
    mc "Now to decide where to go."
    y 2q "I was actually thinking the..."
    y 2s "...Library."
    "The library."
    "Now that I think about it, I haven't gone there in a while."
    "I haven't been there at all as a matter of fact."
    mc "Yeah, that sounds like an interesting place to go."
    mc "Where is it?"
    y 1b "It’s by the mall, east of here."
    y 2g "It’s been a while since I’ve stopped by."
    y 1a "How about we meet at 6?"
    mc "That sounds good to me."
    mc "I still have to clean my room after yesterday’s..."
    mc "...Events."
    show yuri 1q at t11 zorder 2
    mc "..."
    y "..."
    "You really had to mention that, [player]?"
    mc "Anyway, I’ll be heading home now."
    "I get close to Yuri."
    mc "I'll see you later."
    y 1s "I love you."
    mc "I love you too."
    "Yuri seemed like she wanted to do something, but seems to hesitate a bit."
    show yuri thide zorder 1
    hide yuri
    "Not wanting to question it, we start heading out, and part ways once we reached the exit."
    stop music
    scene bg residential_day
    with wipeleft
    play music t2
    "Today has been a somewhat hectic day."
    "First there was this morning which was... Tiring, to say the least."
    "Then there was school."
    "After that the club was just cancelled for the day."
    "And that led to its own mess with Natsuki, who was going to find out if things kept up the way they were."
    "There's nothing really wrong with that, it's just embarrassing I guess."
    "And if Sayori were to find out..."
    "Wait a minute, Sayori wasn’t there."
    "Either meaning she got there before all of us..."
    "Which doesn’t make sense because I surely would have seen her on the way."
    "...Or she didn’t go to the literature club at all."
    "Did she even go to school for that matter?"
    "It's concerning, to say the least."
    "It's just like her to be a little late for school, but to not go to school at all..?"
    menu:
        "What should I do?"
    
        "Go to Sayori’s House":
            $ clean = "sayori_clean"
            "I’ll go see how Sayori’s doing."
            "It has been a while since I’ve last seen her."
            stop music fadeout 2.0
            scene bg black
            with wipeleft_scene
            "The door was open, unusually, and so I made my way in."
            "I hear a faint sound that I can’t quite identify."
            "It sounds like its coming from Sayori's room."
            "I hear it again. It sounds like sniffling."
            "Was that Sayori?"
            "I knock on her door."
            "I hear another faint sniffle before she answers the door."
            s "AH!"
            s "Ah, uh... Give me a minute!"
            play sound closet_open
            "Sayori opens the door to let me in."
            scene sayori_bedroom
            with wipeleft_scene
            play music t5
            show sayori 1ba at t11 zorder 2
            "The door opens and I'm greeted to the usual Sayori smile."
            s "Hey, [player]! What brings you here?"
            mc "Oh nothing, I just wanted to see how you were doing."
            s 1bx "Really? That's so nice of you."
            s 3bd "You haven't been here for a very long time. I was starting to worry you forgot about me."
            mc "That's impossible. I can see your room from the other side of the street."
            s 4bm "What?! Really?! How?!"
            mc "I'm just teasing you Sayori."
            s 2bp "Heeeey! I take back about saying you were being nice."
            mc "Alright, alright. You're not too gullible."
            "Most of the time."
            mc "Anyway, I wanted to talk to you about this morning."
            s 3bb "Why, did something bad happen?"
            mc "Well, you didn't get up for school this morning."
            s 5bb "Oh, about that-"
            mc "Also I didn't see you at school today."
            s 5ba "Well...{w=0.25} Um...{nw}"
            mc "You weren't around for club either."
            s 5bb "Uh...{w=0.25} The thing is...{nw}"
            mc "Did you even know the club was cancelled today?"
            s 4bm "The club was cancelled today?! Why?!"
            "That answers my question."
            mc "Monika wrote a note saying there was a family emergency."
            s 2bk "Oh...{w=0.25} I hope everything is okay for her."
            mc "I feel the same way."
            "There's a brief moment of silence. Neither of us knows how to continue the conversation from here."
            "Wait a minute, didn't I hear sniffling earlier. Why was that coming from Sayori's room?"
            show sayori 1bb at t11 zorder 2
            mc "Hey Sayori, I heard you sniffling earlier. Are you sick?"
            s 5bb "Oh that... I... Uh... Stubbed my toe."
            mc "Classic Sayori. Let me see it to make sure it doesn't get too swollen."
            s 4bm "Wait, don't look at it!"
            "Sayori quickly covers one foot in front of the other."
            s 5ba "It's... Uh... Really gross."
            mc "C'mon, it can't be that disgusting."
            s 3bh "It is too. I saw it changing color and it looks really nasty."
            "I have a feeling that Sayori isn't telling the whole truth, but I let it slide."
            "If it was something important she would have told me already."
            s 2bl "Anyway, what's going on with you? Are you gonna do anything now because the club is cancelled?"
            mc "Well, I'm going with Yuri to the library. But I should head home right now to change and clean my room."
            s 4bc "Wait, clean your room? Your room is dirty?" 
            s "How? It's usually clean."
            "Why do I even speak?"
            mc "Um... I-It's just dirty, okay?"
            s 1bb "Do you need help? I can come over to your house to clean with you."
            mc "Thanks, but that's not entirely necessary-{nw}"
            s 2bc "And you are going on a date with Yuri so there won't be enough time for you to clean."
            mc "It'll be fine Sayori. I'll just clean the rest afterwards."
            s "But what if Yuri comes over? She won't think so well of you if your room is dirty."
            "If only you knew what caused that mess in the first place."
            "Actually, {i}I pray that you never find out what happened there.{/i}"
            s 3bd "Come on. Pleeeeeeeease?"
            "{i}Sigh{/i}. There's no way of talking her out of this."
            mc "Fine, you can clean for me. But don't go snooping around too much."
            s 4br "Yaaaay!"
            show sayori at thide zorder 1
            hide sayori
            scene bg residential_day
            with wipeleft
            show sayori 1bq at t11 zorder 2
            "Something seemed off while walking home with Sayori."
            "For one thing, she had no trouble walking despite the supposed swelling in her toe."
            "And secondly, she seemed less... Sayori than usual."
            "Am I just seeing things? I'm probably overthinking it."
            "I wish I thought this intensely at school."
            show sayori thide
            hide sayori
            scene bg bedroom
            with wipeleft
            show sayori 1ba at t11 zorder 2
            mc "You know where to put everything right?"
            s 1bx "Yeah."
            s 5bb "At least I hope."
            mc "Okay, see ya later Sayori."
            s 4bs "Bye! Have fun!"
            show sayori at thide
            hide sayori
            stop music

        "Prepare for Library":
            $ clean = "player_clean"
            "I’ll go get ready to for the library."
            "I'm probably overthinking about Sayori."
            stop music
            play music t3
            scene bg bedroom
            with wipeleft
            "The room was in slight disarray from the morning before."
            "I try my best to keep it clean, but with everything that happened, I didn't have the time to do it."
            "Probably now was a good a time as any to clean this up."
            scene bg bedroom
            with wipeleft_scene
            "Some time passes, and I finish tidying everything up."
            "That took a bit more time than I thought it would."
            "Granted, I did just throw everything in the washing machine."
            "What time is it anyway?"
            "I look at my clock on my desk, and notice the lotion."
            "I should really hide that thing eventually."
            "It was 6:00, which wasn't a comforting notion."
            "I don’t even know where this place is. I should be heading out now."
            scene bg black
            with wipeleft_scene

    scene bg central_hub
    with wipeleft_scene
    "Where is it? I’m running late."
    "She said it would be east..."
    "Oh! Here it is."
    stop music
    play music t6
    show yuri 1ba at t11 zorder 2
    "I see Yuri coming down the way. Aside from her usual casual get-up, it appears she's carrying a satchel."
    y "Hello, [player]."
    mc "Hi, Yuri."
    mc "Sorry I’m late, I didn’t really know where I was going."
    y "That’s alright, this place is out of the way from busier common areas."
    mc "So, do you visit this place often?"
    y 1bb "Yes, I usually come here after the club ends."
    y "This is where I got the second Portrait of Markov book."
    y 1bt "It’s not very populated, and has been losing visitors recently."
    y 1bv "I’ve been seeing less and less people here."
    "Wow, Yuri really knows this place."
    mc "You seem to know just about everything about this library."
    y 4bb "Eh, I wouldn’t say that."
    y 4ba "I just pick things up from time to time."
    "That reminds me of something."
    mc "Oh, speaking of that copy of Portrait of Markov, why did you get a second copy?"
    y 1bt "W-what do you mean? S-second copy of what?"
    mc "Remember? When I was first introduced to the club."
    y 3bn "Oh, w-well... That. It’s just... I wanted to get you something."
    "This is some deja vu."
    y 2bq "Let’s just... Go inside."
    show yuri at thide zorder 1
    hide yuri
    scene bg bookstore
    with wipeleft_scene
    show yuri 2ba at t11 zorder 2
    y "Isn’t this place just so relaxing?"
    y 2bm "It feels like you’re always accepted here."
    mc "Yeah, it’s a refreshing change from school."
    show yuri 1bc at t11 zorder 2
    "Yuri really seems to be in her element."
    "She’s usually only this calm at home or in the literature club."
    "Especially when we’re close."
    "I turn to the people around me, and feel completely out of place."
    "Everyone just seems... Smarter."
    show yuri 2bf at t11 zorder 2
    "Yuri then starts to look at me."
    y 2bs "Maybe we should take a seat now."
    "Was my expression really that noticeable?"
    "Maybe I just need to adjust myself."
    "Yuri and I take a seat near a window, a bit closed off from everyone else."
    "I take a sniff and smell a hint of Jasmine oil, which oddly makes a bit of sense."
    y 3bt "Is this spot okay? This is where I usually sit."
    mc "It’s fine. It’s very serene."
    y 2ba "Alright."
    show yuri 3bc at t11 zorder 2
    "After that statement, Yuri goes into her satchel and grabs a book we were reading a bit ago."
    "She props it up to how we usually read and we continue reading the book."
    "Of course, we get closer to each other as a result."
    y 1be "Hmmm."
    "I notice that Yuri’s face comes closer to mine, to a point we’re cheek by cheek."
    "She stops paying attention to the book and looks directly at me."
    "Her lips come closer, before being caught away." 
    y 3bp "Ah. I’m sorry."
    y 3bo "This isn’t really the place or time."
    "A bold red rushes across Yuri’s face."
    y 2bq "Let’s just keep on reading."
    mc "Um, Yuri, we already finished the book."
    y 2bp "Eh? {i}We did?{/i}"
    "Yuri really seems to be out of it. What's going on in her head?"
    y 2bn "O-Oh... I-I-I mean, how about you find a book for us to read?"
    mc "Oh okay, sure. I’ll be back soon."
    show yuri thide zorder 1
    hide yuri
    show bg reading_room
    with wipeleft_scene
    "I walk away from the table and wander around a bit to find a good book."
    "I feel like I’m being tested with this. I have to find a book that will impress Yuri."
    "But with so many options, I’m not sure where to start."
    "I decide to try the \"New Release\" section."
    "Surely I’ll be able to find something Yuri hasn’t already read."
    "I scan the spines and pick out some titles that seem interesting."
    "Pulling them out, I stack them up on the side of the shelf and give them each a closer look."
    "The first one, Portrait of John, really reminds me of Portrait of Markov."
    "Aside from the name, they also share the same style for their cover, a different author."
    "It’s practically got Yuri’s name written all over it."
    "The second one, King of Games, is a little more my speed."
    "It’s a manga, but the concept is really interesting, using horror to bring the tension in some teenager's regular life. It’s taking all my self restraint to not jump into it right now."
    "The third one, Captain Bimports, is a blast to the past for me."
    "I remember reading these books as a kid, and I had no idea they were coming out with more. I don’t think Yuri would particularly care for it, though."
    "I wish we could read all of them, but we only have enough time to read one."

    menu:
        "So of course we’re going to read..."   
        "Portrait of John" :
            $ book = 1 
        "King of Games" :
            $ book = 2
        "Captain Bimports" :
            $ book = 3

    if book == 1:
        "Best to play it safe, I think."
        "I take Portrait of John off the shelf and turn around to go back to Yuri, but bump into someone right behind me." 
        stop music fadeout 2.0
        mc "Whoops, sorry, I’ll just go around-"
        $ n_name = "Rude Lady"
        n "Hey, watch where you're going!"
        mc "Sorry, I was just excited is all."
        n "That's no excuse, do you have any idea how busy I am?"
        "If you're so busy then why are you talking to me?"
        mc "Sorry, I'll just keep moving on."
        "Just as I started to move, however, I felt a violent tug on my arm."
        play music t7
        n "What's that book you have? It reminds me of something."
        mc "Oh this? It's the Portrait of John. I picked it up a few seconds ago to read i-"
        "She takes the book out of my grasp to further inspect it."
        n "Well, duh you're gonna read it. I mean what are you doing holding {i}this{/i} book?"
        "The answer I want to give is 'To read it idiot, we're in a library,' but I refrain myself and give her the benefit of the doubt."
        mc "I was interested in what I could get myself into."
        n "Well don't even bother, this book is {i}absolutely{/i} awful."
        mc "Oh, have you read that one?"
        "I haven't heard anything about it after all, maybe it's for a reason."
        n "No, but I saw this post on my social media that said one of the characters was one of those bisexual people or something."
        n "How stupid of the author to include a character like that just to try and get some attention!"
        n "You really should be grateful I was here, stopping you from being infected."
        "Alright, I've hit the limit of my patience, I'm leaving."
        "I take the book back from her hand and try moving past her, but she cuts me off."
        n "Hold up sweetie, I didn't say you could leave yet."
        mc "Hey, what's your deal? I just want to go and read this already."
        n "How inconsiderate of you to just take the book from my hand and try to walk off!"
        n "Let me tell you something. I've lived through a lot in my life and I'm not about to be disrespected by some highschool brat. I'll have you know that my dad is a doctor and knows a lot!"
        "I feel like I'm losing brain cells listening to this person. I just want to get back to Yuri already and forget about this. I avert my eyes to hopefully avoid the chatter."
        n "Hey, don't you go ignoring me, I'm talking to you! You young people need to learn what respect is!"
        "My patience is more dried up than kelp in the desert. I try walking off again but my arm gets seized by the woman."
        n "Hey, stop walking off! I'm just trying to get this disease away from human contact. It would be an absolute nightmare if there was a series of this!"
        mc "Um, are you even aware this book is a sequel?"
        n "That can't be true."
        mc "Why not?"
        n "Because if there were more books like this one I would know them already."
        "My brain feels like it's melting through my ear canals. I wasn't aware this level of self-idealization was possible."
        "She's the complete opposite of Yuri, completely uncaring for the people she speaks with. I just want to be back with Yuri already."
        "My wish is suddenly granted as Yuri walks around a shelf to find my predicament."
        show yuri 1ba at t11 zorder 2
        y "Hey [player], are you there? You've been taking a while and I was wondering if you'd gotten lost."
        show yuri 2be at t11 zorder 2
        "The woman releases her grip from me when Yuri arrives and I grab the book from her hand."
        n "Hey, I didn't say you could have that back."
        "Yuri immediately hears the tone of her voice and gets the same vibe I'm getting."
        y 2bf "[player], is she making you uncomfortable?"
        "I nod my head at her and make my way to Yuri, but more yelling comes from the lady."
        n "Are you really just gonna ignore me like that? I'll just tell this girlfriend you have about how you snatched that book out of my hand!"
        y 2br "[player], did you steal this book from her?"
        "I shake my head no, which was all that Yuri needed."
        "Yuri walks up to the lady, the most fierce I've ever seen her."
        y "Madam, are you aware of how uncomfortable you're making him right now?"
        n "Are you seriously telling me how uncomfortable he is right now? Do you even know how disrespectful he has been to me? He tried to walk away with that horrid book!"
        y "Madam, any attempt to better oneself with new information is admirable. So much can be learned from that which we don't believe we understand."
        y "If we push off what we don't accept just because it's different, we do less for ourselves overall. Are you at all aware of that?"
        n "I'm aware that you're defending this boy with your lovey dovey words. What makes you think I'll just walk away from you now?"
        "This woman won't go away no matter what we do. I rack my brain for ways that Yuri and I can avoid this woman, but Yuri starts going again."
        y "You talk as if our differences only separate and divide us, but what I find to be the truth is that our differences can bring people together." 
        y "Just like it did with me and the administration of this library. So if you would like to be a visitor here, I would suggest you end your foolish behavior."
        "After what feels like forever, we finally get this woman to shut up."
        n "Right... Um, I guess I'll be going now. Have a nice day."
        "The lady leaves at a brisk pace, finally leaving Yuri and I alone."
        stop music fadeout 3.0
        pause 3.0
        $ n_name = "Natsuki"
        mc "Y-Yuri."
        show yuri 3bp at t11 zorder 2
        "Upon hearing my voice, Yuri calms herself."
        y 2bn "I-what?"
        y 1bo "How did I?"
        y 3bp "And when?"
        "It seems even Yuri is unaware of what she has done."
        play music t10 fadein 2.0
        y 3bo "I-I’m so sorry [player], I had no intention to-"
        mc "No, don’t worry about it, you didn’t do anything wrong."
        show yuri 2bn at t11 zorder 2
        y 4bc "But, wasn't I just as terrible as that woman?"
        mc "No Yuri, you really helped me."
        "Yuri is seemingly about to break before speaking once more."
        y "Are you sure I... Did the right thing?"
        mc "Of course."
        y 2bv "W-Well..."
        y 2bu "If you believe so."
        "This date has gotten a lot more tense than I thought it would."
        "Time to finally read this book I guess."
        mc "Let’s head back to our seats now."
        y 1bs "Yeah."
        stop music fadeout 3.0
        scene bg bookstore
        with wipeleft
        play music t5
        show yuri 3be at t11 zorder 2
        "We start reading the book, and Yuri is immediately swept away by it."
        "Her eyes are totally engaged, while keeping in sway with our usual motion."
        y 2bf "Wow."
        y "I had absolutely no idea they had made a sequel to the Portrait of Markov."
        y "I thought I had kept myself up to date with all of the author’s other works."
        mc "Maybe you just missed one."
        y 2bg "Well, perhaps, but I keep myself well informed of any new releases they make."
        "Just then I remembered something from when I was inspecting the book."
        mc "Yuri, this book has a different author."
        y 2bf "What? Really?"
        show yuri 2bg at t11 zorder 2
        "She leaned over and looked, surprised to see the name."
        y 2bf "Oh wow, it is." 
        y "If that's the case, then that probably explains why I haven't heard anything."
        y 2bi "Interesting that they had done that."
        y "I'll have to keep a sharper eye out then."
        "If we can find out who the next author is next time, then it's possible for us to get ahold of another sequel later."
        "Maybe I can find some connections, then-"
        y 2bf "Hey [player], are you okay?"
        mc "Y-yeah."        
        "Looks like I forgot to flip the page."
        show yuri at thide
        hide yuri
        "..."
        stop music fadeout 3.0

    if book == 2:
        "I know Yuri isn’t a huge fan of manga, but I really think she’d like this one a lot."
        "I take King of Games off the shelf and turn around to go back to Yuri, but bump into someone right behind me." 
        stop music fadeout 2.0
        mc "Whoops, sorry, I’ll just go around-"
        $ n_name = "Rude Lady"
        n "Hey, watch where you're going."
        mc "Sorry, I was just excited is all."
        n "That's no excuse, do you have any idea how busy I am?"
        "If you're so busy then why are you talking to me?"
        mc "Sorry, I'll just keep moving on."
        "Just as I started to move, however, I felt a violent tug on my arm."
        play music t7
        n "What's that book you have? It reminds me of something."
        mc "Oh this, it's King of Games. I picked it up a few seconds ago to read i-"
        "She takes the book out of my grasp to further inspect it."
        n "Well duh, you're gonna read it. I mean what are you doing holding {i}this{/i} book?"
        "The answer I want to give is 'To read it idiot, we're in a library,' but I refrain myself and give her the benefit of the doubt."
        mc "I was interested in what I could get myself into."
        n "Well don't even bother, this book is {i}absolutely{/i} awful."
        mc "Oh, have you read the book yet?"
        "Maybe she was just turned off by the game."
        n "No, but I saw this post on my social media and it looked super demonic. This is gonna teach kids how to summon demons!"
        n "How stupid of the author to include that just to get some attention!"
        n "You really should be grateful I was here, stopping you from being infected."
        "Alright, I've hit the limit of my patience, I'm leaving."
        "I take the book back from her hand and try moving past her, but she cuts me off."
        n "Hold up sweetie, I didn't say you could leave yet."
        mc "Hey, what's your deal? I just want to go and read this already."
        n "How inconsiderate of you to just take the book from my hand and try to walk off."
        n "Let me tell you something. I've lived through a lot in my life and I'm not about to be disrespected by some highschool brat. I'll have you know that my dad is a doctor and knows a lot!"
        "I feel like I'm losing brain cells listening to this person. I just want to get back to Yuri already and forget about this. I avert my eyes to hopefully avoid the chatter."
        n "Hey, don't you go ignoring me, I'm talking to you. You young people need to learn what respect is!"
        "My patience is more dried up than kelp in the desert. I try walking off again but my arm gets seized by the woman."
        n "Hey, stop walking off. I'm just trying to get this disease away from human contact. It would be an absolute nightmare if there was a series of this."
        mc "Um, are you even aware of how popular this is?"
        n "That can't be true."
        mc "Why not?"
        n "Because I haven't seen a movie of this. If it was popular, then it would have a movie."
        "My brain feels like it's melting through my ear canals. I wasn't aware this level of self-idealization was possible."
        "She's the complete opposite of Yuri, completely uncaring for the people she speaks with. I just want to be back with Yuri already."
        "My wish is suddenly granted as Yuri walks around a shelf to find my predicament."
        show yuri 1ba at t11 zorder 2
        y "Hey [player], are you there? You've been taking a while and I was wondering if you'd gotten lost."
        show yuri 2be at t11 zorder 2
        "The lady releases her grip from me when Yuri arrives and I grab the book from her hand."
        n "Hey, I didn't say you could have that back!"
        "Yuri immediately hears the tone from the lady's voice and gets the same vibe I'm getting."
        y 2bf "[player], is she making you uncomfortable?"
        "I nod my head at her and make my way to Yuri, but more yelling comes from the lady."
        n "Are you really just gonna ignore me like that. I'll just tell this girlfriend you have about how you snatched that book out of my hand!"
        y 2br "[player], did you steal this book from her?"
        "I shake my head no, which was all that Yuri needed."
        "Yuri walks up to the lady, the most fierce I've ever seen her."
        y "Madam, are you aware of how uncomfortable your making [player] right now."
        n "Are you seriously telling me how uncomfortable he is right now. Do you even know how disrespectful he has been to me? He tried to walk away with that horrid book!"
        "Yuri didn't take that last statement well."
        y "Madam, any attempt to better oneself with new information is admirable. So much can be learned from that which we don't believe we understand."
        y "If we push off what we don't accept just because it's different, we do less for ourselves over all. Are you at all aware of that?"
        n "I'm aware that you're defending this boy with your lovey dovey words. What makes you think I'll just walk away from you now?"
        "This woman won't go away no matter what we do. I rack my brain for ways that Yuri and I can avoid this woman, but Yuri starts going again."
        y "You talk as if our differences only separate and divide us, but what I find to be the truth i that our differences can bring people together."
        y "Just like it did with me and the administration of this library. So if you would like to be a visitor here, I would suggest you end your foolish behavior."
        "After what feels like forever, we finally get this woman to shut up."
        n "Right... Um, guess I'll be going now. Have a nice day."
        "The lady leaves at a brisk pace, finally leaving Yuri and I alone."
        stop music fadeout 3.0
        pause 3.0
        $ n_name = "Natsuki"
        mc "Y-Yuri."
        show yuri 3bp at t11 zorder 2
        "Upon hearing my voice, Yuri calms herself."
        y 2bn "I-what?"
        y 1bo "How did I?"
        y 3bp "And when?"
        "It seems even Yuri is unaware of what she has done."
        play music t10 fadein 2.0
        y 3bo "I-I’m so sorry [player], I had no intention to-"
        mc "No, don’t worry about it, you didn’t do anything wrong."
        show yuri 2bn at t11 zorder 2
        y 4bc "But I-I did something terrible."
        mc "No Yuri, you really helped me."
        "Yuri is seemingly about to break before speaking once more."
        y "Are you sure, I... Did the right thing?"
        mc "Of course."
        y 2bv "W-Well."
        y 2bu "If you believe so."
        "This date has gotten a lot more tense than I thought it would."
        "Time to finally read this book I guess."
        mc "Let’s head back to our seats now."
        y 1bs "Yeah."
        stop music fadeout 3.0
        scene bg bookstore
        with wipeleft
        play music t5
        show yuri 1bg at t11 zorder 2
        "We start reading the book, Yuri being very hesitant before even opening it."
        mc "Is there anything wrong Yuri?"
        y 1bq "P-Pardon."
        mc "You seem to have something stuck in your mind."
        y 2bo "Well."
        y "I wasn’t expecting you would find a book like this for us."
        "Uh oh. Did I mess up?"
        "I really thought this would be a good pick."
        "Better luck next time I guess."
        y 3bo "But you did choose it out, maybe it won’t be as... Childish... As I thought it would be."
        "At least Yuri is giving me a chance."
        y 2bq "I once heard somewhere there was a follow-up to the Portrait of Markov, but maybe it’s just a myth."
        "Wait a minute, maybe I can make it up with finding this \'sequel.\'"
        y 2be "Hey [player], are you there?"
        mc "Y-yeah." 
        "Let’s start this book."
        show yuri at thide
        hide yuri
        "..."
        stop music fadeout 3.0

    if book == 3:
        "This may be {i}really{/i} childish."
        "But, maybe she will give this a chance."
        "I hope."
        stop music fadeout 2.0
        mc "Whoops, sorry, I’ll just go around-"
        $ n_name = "Rude lady"
        n "Hey, watch where you're going."
        mc "Sorry, I was just excited is all."
        n "That's no excuse, do you have any idea how busy I am?"
        "If you're so busy then why are you talking to me?"
        mc "Sorry, I'll just keep moving on."
        "Just as I started to move, however, I felt a violent tug on my arm."
        play music t7
        n "What's that book you have? It reminds me of something."
        mc "Oh this, it's Captain Bimports. I picked it up a few seconds ago to read i-"
        "She takes the book out of my grasp to further inspect it."
        n "Well duh you're gonna read it. I mean what are you doing holding {i}this{/i} book."
        "The answer I want to give is 'To read it idiot, we're in a library,' but I refrain myself and give her the benefit of the doubt."
        mc "I was interested in what I could get myself into."
        n "Well don't even bother, this book is {i}absolutely{/i} awful."
        mc "Oh, have you read the book yet?"
        "I really doubt it, but her excuse for hating it can't be too dumb right, I mean it's for kids."
        n "No, but I saw this post on my social media that said there were nazi symbols in it!"
        n "How stupid of the author to show these racist symbols to children just to get some attention!"
        n "You really should be grateful I was here, stopping you from being infected."
        "Alright, I've hit the limit of my patience, I'm leaving."
        "I take the book back from her hand and try moving past her, but she cuts me off."
        n "Hold up sweetie, I didn't say you could leave yet."
        mc "Hey, what's your deal? I just want to go and read this already."
        n "How inconsiderate of you to just take the book from my hand and try to walk off."
        n "Let me tell you something. I've lived through a lot in my life and I'm not about to be disrespected by some highschool brat. I'll have you know that my dad is a doctor and knows a lot!"
        "I feel like I'm losing brain cells listening to this person. I just want to get back to Yuri already and forget about this. I avert my eyes to hopefully avoid the chatter."
        n "Hey, don't you go ignoring me, I'm talking to you. You young people need to learn what respect is!"
        "My patience is more dried up than kelp in the desert. I try walking off again but my arm gets seized by the woman."
        n "Hey, stop walking off. I'm just trying to get this disease away from human contact. It would be an absolute nightmare if there was a series of this."
        mc "Um, are you even aware of how many people get happy seeing this?"
        n "That can't be true."
        mc "Why not?"
        n "Because those books are meant for little kids! Any mature people should feel embarrassed to like those things."
        "My brain feels like it's melting through my ear canals. I wasn't aware this level of self-idealization was possible."
        "She's the complete opposite of Yuri, completely uncaring for the people she speaks with. I just want to be back with Yuri already."
        "My wish is suddenly granted as Yuri walks around a shelf to find my predicament."
        show yuri 1ba at t11 zorder 2
        y "Hey [player], are you there? You've been taking a while and I was wondering if you'd gotten lost."
        show yuri 2be at t11 zorder 2
        "The lady releases her grip from me when Yuri arrives and I grab the book from her hand."
        n "Hey, I didn't say you could have that back!"
        "Yuri immediately hears the tone from the lady's voice and gets the same vibe I'm getting."
        y "[player], is she making you uncomfortable?"
        mc "I nod my head at her and make my way to Yuri, but more yelling comes from lady."
        n "Are you really just gonna ignore me like that. I'll just tell this girlfriend you have about how you snatched that book out of my hand!"
        y "[player], did you steal this book from her?"
        "I shake my head no, which was all that Yuri needed."
        "Yuri walks up to the lady, the most fierce I've ever seen her."
        y "Madam, are you aware of how uncomfortable your making [player] right now."
        n "Are you seriously telling me how uncomfortable he is right now. Do you even know how disrespectful he has been to me? He tried to walk away with that horrid book."
        "Yuri didn't take that last statement well."
        y "Madam, any attempt to better oneself with new information is admirable. So much can be learned from that which we don't believe we understand."
        y "If we push off what we don't accept just because it's different, we do less for ourselves over all. Are you at all aware of that?"
        n "I'm aware that you're defending this boy with your lovey dovey words. What makes you think I'll just walk away from you now."
        "This woman won't go away no matter what we do. I rack my brain for ways that Yuri and I can avoid this woman, but Yuri starts going again."
        y "You talk as if our differences only separate and divide us, but what I find to be the truth is that our differences can bring people together."
        y "Just like it did with me and the administration of this library. So if you would like to be a visitor here, I would suggest you end your foolish behavior."
        "After what feels like forever, we finally get this woman to shut up."
        n "Right... Um, guess I'll be going now. Have a nice day."
        "The lady leaves at a brisk pace, finally leaving Yuri and I alone."
        stop music fadeout 3.0
        pause 3.0
        $ n_name = "Natsuki"
        mc "Y-Yuri."
        show yuri 3bp at t11 zorder 2
        "Upon hearing my voice, Yuri calms herself."
        y 2bn "I-what?"
        y 1bo "How did I?"
        y 3bp "And when?"
        "It seems even Yuri is unaware of what she has done."
        play music t10 fadein 2.0
        y 3bo "I-I’m so sorry [player], I had no intention to-"
        mc "No, don’t worry about it, you didn’t do anything wrong."
        show yuri 2bn at t11 zorder 2
        y 4bc "But I-I did something terrible."
        mc "No Yuri, you really helped me."
        "Yuri is seemingly about to break before speaking once more."
        y "Are you sure, I... Did the right thing?"
        mc "Of course."
        y 2bv "W-Well."
        y 2bu "If you believe so."
        "This date has gotten a lot more tense than I thought it would."
        "Time to finally read this book I guess."
        mc "Let’s head back to our seats now."
        y 1bs "Yeah."
        stop music fadeout 3.0
        scene bg bookstore
        with wipeleft
        play music t5
        show yuri 2bo at t11 zorder 2
        "Yuri’s face immediately changes when she sees the book’s cover."
        "She keeps looking at me with a questioning expression repeatedly."
        mc "Hey Yuri, is anything wrong?"
        y 3bp "U-Uh, n-no."
        "Yuri, I love you, but I can tell when you’re lying."
        mc "C'mon, tell me what’s wrong."
        y 3bv "W-well, I thought you would get something more mature."
        "Dang it, I was taking too large of a risk with this."
        "Hopefully I can make the right decision next time."
        y 3bt "[player], did you really want to read this book?"
        mc "Of course, something just told me this would be an enjoyable experience."
        y 2bq "A-Alright. I can’t really be mad if you’re making an attempt to... Diversify your range."
        y 4bb "{size=-5}{k=-2}I was just hoping that the sequel was real by any chance.{/k}{/size}"
        "A sequel? To what?"
        "I guess Portrait of Markov, what else?"
        "I’ll look more into this to see if I can surprise Yuri with this."
        y 2be "Hey [player], are you there?"
        mc "Y-yeah."
        "Time to finally open this book."
        "Hopefully it was worth all the shame."
        show yuri at thide
        hide yuri
        "..."
        stop music fadeout 3.0

    scene bg bookstore_sunset
    with wipeleft_scene
    stop music
    play music t14
    "I look outside and see the orange sunset through the window."
    mc "It’s getting darker outside, how long have we been here?"
    "Just then, the intercom makes an announcement."
    $ n_name = "Intercom"
    n "Attention visitors, the library will be closing in approximately five minutes."
    n "Please make your way to the exit. Thank you for coming."
    $ n_name = "Natsuki"
    "Well, I guess that technically answers my question."
    show yuri 1ba at t11 zorder 2
    mc "I guess this is the time to say goodbye, Yuri."
    "Yuri had a worrisome face as I mentioned that."
    show yuri 4bb
    mc "Um, is something wrong Yuri?"
    y 4ba "Oh, uh, it’s just that I was hoping that..."
    y 4bb "I could be with you a little longer."
    "I was not expecting this, what does Yuri want to do?"
    mc "Well, we can go to my house if you’re interested."  
    y 2bj "Oh, I would love to, but I think I need to get home."
    y 2bq "I think I need some alone time to think about a few things."
    mc "Oh, alright. I guess I'll see you later then."
    y "Indeed."
    "Yuri and I head up and walk out of the library. She decided to return the book to the librarian."
    "I think she said she was interested in finding a copy online so that way another person will find the book we were using here."
    scene bg residential_sunset
    with wipeleft
    show yuri 3bs at t11 zorder 2
    "We stood outside and walked a bit after she returned the book."
    "As we neared a cross into the neighborhood, we turned to each other."
    mc "Bye, Yuri. I love you."
    y "I love you too."
    "Before I started the walk, I felt a slight tug on my fingers."
    y 4bb "Hey [player], thanks for the last couple of days. You really made me happy."
    mc "N-No problem."
    scene black
    with wipeleft_scene
    hide yuri
    "Yuri then starts her walk back home, her movement looking stunning to me."
    "I stood there dumbfounded for a minute before walking again." 
    "I asked this earlier today, but it still blows my mind how I got with a girl this great and gorgeous..."
    "I'm glad she was happy today."
    "If only I could know what the future may hold."
    "Only time will tell what will happen next, I suppose."
    stop music fadeout 2.0

#Scene 2
    scene bg bedroom
    with dissolve_scene_full
    play music t12
    "Ugh..."
    "The sun's rays attack my eyes, my weak point for waking up."
    "I shrug and move over on the bed to go back to my realm of dreams."
    "So...{w=0.25} Comfortable."
    "But unfortunately for me, it's already too late, as I hear my phone start to go off with a notification."
    "Do I really have to answer? The pillow called first."
    "I weigh my options to read the notification or go back to sleep, but I suppose the phone will go after me until I read it."
    "Guess it's time for me to start the day."
    stop music
    play music t3
    "I look to the room around me. For some reason I really appreciate it being clean right now."
    if clean == "sayori_clean":
        "I should thank Sayori at some point."
        "She really did me a solid on that."
    "A clean room's always good though."
    "Have to keep on impressing Yuri somehow."
    "Suddenly, another notification goes by, interrupting my thoughts."
    "I cast my arm out to the phone beside me. Unlocking the phone screen aaaaaand..."
    "Oh, I got a text from Yuri."
    y "Hey [player], I'm sorry if I woke you up, but I was wondering if I was able to visit your house today."
    mc "Sure thing."
    y "Great, thank you."
    "Huh, that's kind of weird."
    "Yuri has never really asked me if she could come over through text."
    "She usually just does."
    "I wonder what inspired her to do so?"
    "Eh, it's probably nothing."
    "I get up from the bed to start the day, but then another notification hits me."
    y "I really appreciate you saying yes, I wonder what else you would say yes to..."
    "Did... Did I read that right?"
    "Did Yuri just try to flirt with me?"
    "I'm a bit taken aback by this. Yuri doesn't usually act out to this degree."
    "I get that it's just a text, but this seems very strong coming from Yuri."
    "Perhaps I'm looking too deep into this. It is just a text after all."
    "I should get some clothes on and get the day started."
    scene bg kitchen
    with wipeleft_scene
    "As I'm about to start making breakfast, I decide to ask Yuri if she would like anything when she gets here."
    "What I thought would be a simple response took Yuri at least a minute to respond."
    "She eventually responds with a simple text."
    y "If it's not much, can you set up your console? I want to try a video game again."
    mc "Sure we can do that."
    "I respond calmly and quickly, but in reality, I'm starting to get thrown in a daze."
    "At first she wanted to visit the library, which is normal for her to do."
    "But now it seems she's actively trying to get us to do something."
    "When we did something in the past it's never felt forced, but something just feels different this time."
    "Wait, what am I even saying?"
    "She just wants me to set up a console, why am I being so paranoid right now?"
    "I bet Monika would say to me that there's no need to analyze everything I do, probably teasing me again about how Yuri is affecting me."
    "My thoughts are interrupted once again with another notification. Yuri's on fire today."
    y "[player], I was just wondering. If I were to do something ridiculous, would you still love me?"
    stop music fadeout 1.0
    "I read the message again to make sure my eyes aren't deceiving me." 
    "What does she mean by that?"
    "I quickly respond back to her."
    mc "Of course I'll still love you. You're the greatest thing that has ever happened to me."
    "I usually don't write anything this sappy, but I just wrote the first thing out of my head."
    "It once again takes Yuri a while to respond, but this time when she does so-"
    "There's an image."
    "I tried to open up it up, but by the time I did it was deleted."
    "Now I know something is up. Yuri usually isn't this sporadic with her texting."
    mc "Is there anything going on with her? What can it be?"
    "I try to look at different scenarios."
    "Is she cutting herself again?" 
    "It's possible, but that wouldn't quite explain her recent behavior."
    "Is she experimenting with anything? Maybe she's read a book about something and is trying new things."
    "Whatever it is, I just hope she's safe."
    "Just to make sure, I send her a text."
    play music t5
    mc "Hey, is everything alright?"
    "In a split second, almost right before I could hit send, she replied back."
    y "Yes."
    "Huh, she replied so fast. Was she waiting for me?"
    "Even though she replied yes, I can't help shake the feeling something's going on."
    "I go and retrieve the console for when she comes over, but the thoughts chase after me as I move through the house."
    "I guess I can only find out what's going on when she comes."
    "I use this time to tidy up things around the house, since I can't keep just my room clean after all."
    "Going around the house, I start to remember each separate time Yuri came over."
    "Sometimes it was just to read, and other times we did other things."
    "But each of those memories give me a sense of attachment, that someone in this world really cares about me."
    "I know the others are there for me, but something about Yuri, there's something that sets her apart."
    "Is it her mannerisms? Her kindness? Her beauty?"
    "I feel like I can spend all day trying to figure it out what it is and still not know."
    "But there is one thing I know, and it's that I love her. She's entirely worth it."
    "I'm just hoping she can see that too."
    "Some time passes after I clean the house, I sit down to relax, but then suddenly..."
    play sound "mod_assets/doorbell.mp3"
    "{i}Ding-dong.{/i}"
    "Normally I would be a bit annoyed if the doorbell rang right when I sat down, but I know opening the door won't be a hassle this time."
    "Especially when behind the door stands my fabulous-"
    scene bg livingroom
    with wipeleft_scene
    show yuri 1bc at t11 zorder 2
    mc "Yuri!"
    y 1bd "Hi, [player]. I'm so happy I could come over today."
    y 2bq "Truth be told, I've been a bit worried over a few things."
    mc "Really? Is there anything I should be concerned about?"
    y 2bg "No, nothing major. It's nothing to be afraid of."
    y "I've just been feeling... How should I say it... Off lately."
    "My head jumps back to the thoughts of earlier."
    "Yuri's behavior has been different by text, and she says she's not feeling well, but other than that I don't see anything else wrong with her."
    "She just said to not be worried, but I know I'm gonna keep my eyes open for anything despite what she says."
    "I feel kind of bad, but I'm doing this for her safety."
    y 1bf "[player], are you there?"
    mc "Oh, sorry Yuri. I got stuck in my head there."
    mc "Here, come inside."
    show yuri 1ba at t11 zorder 2
    "Yuri walks into the house and onto my couch. She sets her satchel down beside her."
    mc "Is there anything you would like me to get for you?"
    y 1bb "Water would be fine."
    mc "Water in a cup coming right up."
    "I walk to the kitchen and grab the cup, get some water from the fridge and pass it on to Yuri."
    y 2bb "Thank you."
    show yuri 2bc at t11 zorder 2
    "I try to observe if she was trying to cover up anything with her sleeves while grasping the cup, but everything seems fine."
    "I sit down beside Yuri. I guess now's about the time to engage in small talk."
    show yuri 1be at t11 zorder 2
    mc "So Yuri, nice weather we're having today, aren't we?"
    "Really [player]? it's been at least 6 months and that's all you can say?"
    y 2bg "I suppose it's nice. I haven't been really paying attention outside much."
    y "To be perfectly honest, I've just been at home thinking."
    mc "Really, thinking about what?"
    y 3bi "Well, it's just... Last week I really put myself out there, so I suppose now I'm just trying to figure out how to move on."
    y 3bj "It's weird. I didn't think that I'd get this far, so when I did I guess it only makes sense that I would become my own worst enemy."
    mc "What do you mean?"
    y 2bq "Oh, it's not much. I've probably been rambling about too much anyway."
    y "How about we start playing that game now?"
    mc "Sure thing."
    "I decide not to pressure Yuri about anything. It's probably taken a lot from her to confess this much."
    "Before I start to go up and grab the console, I get a request from Yuri."
    if pickedCorrectYuriGame :
        stop music fadeout 2.0
        y 4bb "Um, [player], if it's not too much to ask, can we play a different game today?"
        mc "Sure thing. Is there anything you prefer?"
        y 4ba "I'm not really sure, it's just that the last game was a bit fast for me."
        mc "Alright Yuri, be back in a jiffy."
        show yuri at thide zorder 1
        hide yuri
        "With that I go to my room to pick up a game."
        scene bg bedroom
        with wipeleft
        "I go upstairs to retrieve the Playbox 64."
        "Pondering on it, I should leave it downstairs after we're done."
        "I haven't used it recently since I've been spending my free time with Yuri."
        "What was the game we were playing again?"
        "I think it was Gone Nuclear: Vegas Blues."
        "Just in the corner of my eye, I see another game."
        "The Flaming Symbol: Four Seasons."
        "It's a JRPG, this one has a lot of story elements as well as strategic battle systems. ."
        "I haven't gotten to play through it much yet because I got it when I started dating Yuri."
        "Almost instinctively, I take the game with me."
        "Maybe Yuri would enjoy the strategic elements and slower pacing."
        scene bg livingroom
        with wiperight

    else :
        stop music fadeout 2.0
        y 2bq "Maybe we can... Play a video game? One that's more story driven than the last one.."
        y 3bo "Those exist, right?"
        mc "Of course they do! In fact, I know a game you would enjoy."
        mc "I'll be back in a second."
        show yuri at thide zorder 1
        hide yuri
        scene bg bedroom
        with wipeleft
        "I can't believe Yuri chose to do that, especially considering what happened last time."
        "I go upstairs to retrieve the Playbox 64."
        "Pondering on it, I should leave it downstairs after we're done."
        "I haven't used it recently since I've been spending my free time with Yuri."
        "I have to choose the right game this time."
        "I go through every game I have in my catalogue."
        "Hmm... No good, there's not a game I can find here that would satisfy Yuri."
        "Then out of magic on the desk I see another game."
        "The Flaming Symbol: Four Seasons."
        "It's a JRPG, with a lot of story elements as well as strategic battle systems."
        "I haven't gotten to play it much yet because I got it when I started dating Yuri."
        "Almost instinctively I take the game with me."
        "Maybe Yuri would enjoy the strategic elements and slow pacing."
        scene bg livingroom
        with wiperight

    show yuri 4bb at t11 zorder 2
    play music t6
    "I go downstairs to see Yuri fidget with her arms. When she sees me she moves her arms very close to her."
    mc "I'm sorry, was I interrupting anything?"
    y 3bp "Uhh, no. I-I just had an itch to scratch!"
    mc "Alright, I'll just get the console set up now."
    show yuri 4ba at t11 zorder 2
    "While putting up the greatest console of all time, I notice Yuri's defining stare target me."
    "There must be something that's on her mind."
    mc "Yuri, is there anything you want to talk about?"
    y 1bf "Huh? No, not particularly. Why do you ask?"
    mc "It's just you were staring at me and I was curious as to what you were thinking of."
    y "Oh, I was just analyzing how you set up the console."
    y 1bh "I really don't know much about electronics."
    y 2bj "The most affiliated I am with devices is my phone."
    mc "Let me guess, the only app you have is an e-book collection."
    y 3bn "Uhhh..."
    y 3bq "Yeah."
    mc "Hehe. Yuri, you're so adorable."
    y 4be "T-thank you."
    "By the time our conversation ends, the console is ready to go."
    "I boot up the game and we're treated with the intro."
    y 2be "It's bringing up that castle a lot, and that woman."
    "The gameplay hasn't even started yet and Yuri is already dissecting the game." 
    "That's got to be a new record somewhere."
    "The file selection shows and I decide to delete my save file."
    y 2bf "[player], why did you do that? Didn't you have a lot of progress?"
    mc "Not really. Besides, I don't mind restarting."
    y 3bs "You're so kind, [player]."
    mc "Well you're not any different. I mean, you reread Portrait of Markov just to read it with me."
    mc "I couldn't imagine restarting a book back then."
    y 3bu "I... Suppose your right."
    "With the save file deleted, the opening cutscene shows, introducing the prologue to the story."
    y 2be "That woman again. I'm curious with her importance to the story."
    "The cutscene plays on and that same woman decapitates some old dude."
    mc "Ouch, that's gotta hurt."
    y 2bl "Yes, that woman is in such seething pain."
    mc "The woman? The guy just got his head sliced off. I don't think it can hurt more than that."
    y 3bt "But don't you see the anger the woman is lashing out?"
    y "She's been waiting for this moment, waiting for her revenge."
    y 3bt "That can only mean she's been in such sorrow while waiting for this moment."
    y "We don't know how much time has passed, but we know by her actions that the pain would never go away until she got his blood across the field."
    y 3bv "I wonder if that's going to be enough to refill her heart from whatever turmoil she's in."
    "Three minutes is all it took for Yuri to understand the plot, where I still didn't get the story until a quarter of the way in."
    "We get to the present time and finally the gameplay begins."
    show yuri 1be at t11 zorder 2
    "Yuri is still just observing at this point while I strategize what to do."
    "I get through the tutorial and a few more characters are introduced."
    "At some point, we have to decide who we're sticking with on our journey."
    mc "I can't really decide who I want, what do you think Yuri?"
    y 1bg "None of them seem particularly trustworthy, but perhaps I'm thinking that because I just don't know them enough."
    mc "What do you mean?"
    y 1bh "Well, when introducing a character, the author- I-I mean writer, addresses what you need to know about them with just their design alone."
    y 2bh "The key features with this art style is in the face. But I can't see their intentions so clearly, which I know was done on purpose by how they contrast with the other characters introduced so far."
    mc "You got all of that just with one level of the game?"
    y 3bn "A-Ah, I'm sorry, was that too much? I shouldn't be talking so confidently."
    y 3bq "I just can't help myself when there's a compelling story."
    mc "Don't worry about it, I really appreciate you being yourself."
    mc "How else would I get to know the real and best of you more?"
    y 3bo "R-right, the real me.."
    "I continue on with the story and get to the next level."
    "While in the middle of my strategy, I hit a roadblock."
    mc "What? How did so many enemy units show up? How do I avoid them all?"
    "As an escape routes go through my head, Yuri gently taps me on the shoulder."
    y 2bf "[player], I think I have an idea."
    mc "Really, what?"
    y 3bf "Well, our units can only get attacked if the enemy is right next to them, right? So, if we put the allies that have more HP in front of the injured units, we can make a barrier and make a counter attack."
    mc "Wow, I never thought of it like that! I was just looking for type matchups."
    "I executed Yuri's plan, with her directing me to put which units where."
    "Very quickly, I'm able to break up the bind I'm in and launch the counter attack."
    "We went from a nearly crushing defeat to a near flawless victory!"
    mc "Yuri, you really helped me out there!"
    y 4bb "Are you sure? I was just thinking out loud really."
    y "I'm sure you would have thought of something else."
    mc "Not really. Strategy games aren't really my forte."
    mc "I end up trapping myself with how I go head-on."
    y 4bb "Well then, I'm glad I was able to help."
    show yuri at thide zorder 1
    hide yuri
    scene bg livingroom_sunset
    with wipeleft_scene
    "We move on a few hours through the game. It went on very similar to the last level, I usually got myself stuck and Yuri found a way out."
    "At this point I might as well hand her the controller, she's the one making the pro-gamer moves."
    "We eventually get through the first chapter of the game, and I notice it's getting a bit dark outside."
    "How long were we sitting here? I mean, we ate snacks a few times while playing, but we really haven't gotten a meal today."
    show yuri 1be at t11 zorder 2
    y "That chapter was much longer than I expected. I thought games were shorter than this."
    mc "RPGs tend to have much longer play hours compared to other games, so it's only natural."
    mc "You really made it speed up though. You were so talented going through it."
    y 2bq "Thank you, but I don't really think I deserve the attention. I was, just having fun."
    mc "But you do deserve it. You looked really happy while playing."
    "Yuri has no comment on this. I don't think she's allowing herself to realize what she can do."
    stop music fadeout 2.0
    "I then notice Yuri's arms start to move, both rubbing against each other."
    y 4bb "I don't know what you mean. I'm just... No that's not it, I know you don't see me like that."
    mc "See you like what?"
    "Yuri's movement becomes more erratic. Her breathing becomes heavier as well."
    play music t9
    y 4bc "Well, like a freak."
    y "You love me despite my apparent flaws."
    y 4bb "I'm just the girl who reads horror books for fun, the weirdo that always needs to excuse herself."
    y "I feel so awkward with myself so often, yet you're so patient with me."
    "Yuri's arms are moving like there's a puppet master controlling her for amusement, shifting so fast across herself."
    y "The part that scares me the most is that this isn't even the first time we've had a conversation like this." 
    y "Will there be more? Will I be able to accept myself like you have?"
    y "Or will you move on to a girl that's more sane, less, less-"
    mc "Yuri!"
    "To stop her thought, I grabbed her arm, but then I remembered the cutting."
    y 3bp "Aaaaaah!"
    mc "Oh my God, Yuri, I'm so sorry!"
    y 3bo "I-It's alright [player]. I was...{w=0.5} Losing myself there."
    "A couple of moments pass while Yuri recovers from the pain."
    stop music fadeout 2.0
    "My doubts came back to me while waiting. I guess now's as good a time as any to get them out."
    scene black
    with wipeleft_scene
    hide yuri
    mc "Yuri, I'm sorry to ask this, because I know that its personal."
    mc "But... I need to see your arms."
    "It takes her a moment to think, but she complies, nodding her head."
    "Slowly, she rolled up her sleeves, revealing her arms to me."
    scene bg livingroom_sunset
    with wipeleft_scene
    play music t10
    show yuri 4bwc1 at t11 zorder 2
    "The scars seem to be healing, but it's still visible that there's pain when pressure is applied."
    y 4bhc1 "I'm sorry for being such disappointment."
    mc "What?"
    y "Even after showing these to you the first time, I... Still get a ride off of the pain."
    y 4by6c1 "I'm still the freak who likes to cut herself. I still feel as if I need to live off the pain."
    y "[player], I'm just so confused right now."
    y 4bnc1 "Because even with you around me, I still can't avoid the rush that pain gives me."
    y 4boc1 "You make me more alive than anything else, but when I'm not with you, what am I?"
    y 4btc1 "These thoughts, they've been entering my head since last week. I've been going out with you more often to see if I can replace it, but for some reason I can't."
    y "I still depend on it, the pain."
    y 4bwc1 "{i}huff{/i} Isn't that poetry? I have the answer right in front of me, yet I still hit a wall..."
    y 4by6c1 "[player], even though it's wrong, I still have to."
    mc "Yuri, have you cut yourself since we last talked like this?"
    y 4bvc1 "No... But I'm not sure I can last any longer."
    mc "Well, you said you want to replace it. What can I do to help?"
    "Yuri pushes her head against my chest."
    scene cg yuri_on_chest
    with dissolve_scene_full
    y "I-I... Want to feel your heat, let it radiate on to me."
    y "I want to feel your heartbeat. I need to know it beats for me."
    y "I want you to surround me with your blood, I need to connect myself with you."
    "I keep my arms around Yuri, the room falling silent."
    "I can only hear our heartbeats now, feel them being synced."
    "I hug her as tightly as I can, but..."
    "Something still feels wrong."
    "What happens when I'm not there? What will she do?"
    "I can't be her only support. She might hurt herself if I'm not there."
    "Well, whatever it is, I can figure it out later. Right now, I need to keep myself with her."
    "..."
    "..."
    "..."
    mc "H-Hey Yuri."
    y "Yes?"
    mc "Do you want any tea to help you feel better?"
    y "Yes."
    scene bg livingroom_sunset
    with dissolve_scene_full
    show yuri 4be at t11 zorder 2
    "Yuri and I break our hug so I can grab the tea."
    show yuri 4bb at t11 zorder 2
    "Yuri stays sitting down on the couch, looking at her arms."
    "I'm trying my best to comfort her, but I'm not a professional. I need to help Yuri so she can safely withdraw from the cutting."
    stop music fadeout 3.0
    "I get some tea from Yuri's pouch and start preparing. Everything stays quiet as I do so, each drop of water echoing through the house."
    "Once the tea is made, I fill up a wooden cup that may assist in comforting Yuri and bring it to her."
    "She takes a sip and begins to feel more relaxed."
    scene bg livingroom_night
    with wipeleft_scene
    "There isn't a conversation that passes by this time."
    "We just sit together, enjoying each others' company."
    "It's dark outside by the time one of us speak."
    show yuri 4ba at t11 zorder 2
    mc "Are you feeling any better, Yuri?"
    y "Just a bit."
    mc "Is there anything I can do to help?"
    y 4be "Well, do you know what that tea you made us was?"
    mc "Uh, I think it was Ginseng tea."
    y "And do you know what it does?"
    mc "Um, maybe. What does it do?"
    y "It helps with what I want to do next."
    scene black
    with dissolve_scene_full
    hide yuri
    "Before I could wonder what she meant, I felt Yuri get closer, giving me a kiss on the lips before climbing on top of my lap."
    "As she layed on top of me, the multitude of feelings and minutes blurred together." 
    "Just as they had before..."
    "..."
    "..."

#Scene 3
    scene bg club_day
    with dissolve_scene_full
    play music t2
    show yuri 1a at t11 zorder 2
    "The week goes by without a hitch."
    "During the club, Yuri and I discuss some books we've rented and read during the week."
    show yuri 1a at thide zorder 1
    y "I'm glad you find yourself agreeing with my assessments." 
    y "Really, he's a great character. I just find a lot of people seem to not give him a chance."
    y "It's a shame. I quite enjoy his arc..."
    y "And the determination on display throughout the entire story..."
    "Before I could get a word in to respond, Monika cuts our conversation short." 
    hide yuri
    show monika 1b at t11 zorder 2
    m "Okay, everyone!"
    m "It's getting late, so I think this is a good time to wrap things up."
    show monika 1c at thide zorder 1
    hide monika
    show yuri 1w at t11 zorder 2
    "Yuri sighs."
    m "Don't be so down, Yuri."
    show yuri 1w at t22 zorder 2
    show monika 1a at f21 zorder 2
    m "Actually, there's something I want to discuss before we take our leave."
    show monika 1a at t21 zorder 2
    show yuri 1e at f22 zorder 2
    y "What is that?"
    show natsuki 1k at t41 zorder 2
    show sayori 1a at t42 zorder 2
    show monika 1a at f43 zorder 2
    show yuri 1e at t44 zorder 2
    m 1b "Lately, I've been thinking about how we don't have many out-of-school club activities."
    m 1l"And by that, I mean the administration is getting a bit upset we haven't done anything like that yet."
    m "Ahaha..."
    s 1l "Wait? They did? Well, they did say something about us wasting too much time..." 
    s "and \'incompetent leadership\'..."
    show monika 1h at t43 zorder 2
    "Monika shoots Sayori a stern glance."
    "Honestly, if I were her, I'd expect this kind of thing by now."
    m 2b "So, I was thinking... How about how about we all go out somewhere tomorrow?"
    m 4k "As a club activity!"
    show monika at t43 zorder 2
    show yuri at f44 zorder 2
    y 3n "Ah! Er...{w=0.1} But-{nw}"
    show yuri at t44 zorder 2
    show sayori at f42 zorder 2
    s 1c "We should go bowling!"
    show sayori at t42 zorder 2
    mc "Sayori, that's uh... A bit random."
    show monika at f43 zorder 2
    m 3a "Well, I wouldn't call it random, [player]."
    m 4a "Sayori and I have been discussing this since the meeting, and well...."
    m 4n "Ever since I brought up the idea, she hasn't really let go of it."
    show monika at t43 zorder 2
    show natsuki 1h at f41 zorder 2
    "Natsuki shoots the pair a confused look."
    n 4e "What the heck does bowling have to do with literature?"
    show monika at f43 zorder 2
    show natsuki at t41 zorder 2
    m 3a "W-well, admittedly not much, but it doesn't have to!"
    m "Just something to get us out of the club room, you know?"
    show monika at t43 zorder 2
    show yuri at f44 zorder 2
    y "I'm sorry, but I must agree with Natsuki! This seems inappropriate!"
    "Naturally, something like this is a worry to Yuri. It's taking her out of her comfort zone by a long shot."
    "Guess it's up to me, then."
    show yuri 2o at t44 zorder 2
    mc "To be honest, it is kind of a weird activity for a club like us to be doing."
    show sayori 4r at f42 zorder 2
    s "Aw c'mon, [player]! You love bowling!"
    show sayori 3c at t42 zorder 2
    mc "Eh? Me? Where are you pulling that one from?"
    show sayori 3q at f42 zorder 2
    s "Yeah! You don't remember? My 10th birthday, silly!"
    show sayori 3b at t42 zorder 2
    mc "You mean the 10th birthday where I got my fingers stuck in the finger holes and ended up flinging myself across the bowling lane?"
    s 5b "Aw, don't be so dramatic! Other than the nosebleed, you had a grin on your face!"
    mc "No, that was seething."
    mc "...Whatever, this is besides the point."
    show natsuki 3d at t41 zorder 2
    "I try to avert putting my total gaze on Natsuki's smirk I could feel in my peripheral vision."
    show natsuki 1c at t41 zorder 2
    show monika at f43 zorder 2
    m 5a "Regardless, we're going bowling tomorrow."
    show monika 1a at t43 zorder 2
    "Monika pulls the brakes on my train of thought."
    show natsuki at f41 zorder 2
    n 4f "Hey! You may have gotten these two on board, but I'm not convinced!"
    show natsuki at t41 zorder 2
    show yuri at f44 zorder 2
    y 3p "Neither am I!" 
    y "At least let me mentally prepare before taking on something so daunting!"
    show yuri at t44 zorder 2
    show monika at f43 zorder 2
    m 5a "Daunting? Yuri, come on. You've breezed through final exams more stressful than a game of bowling."
    show monika 1a at t43 zorder 2
    show sayori at f42 zorder 2
    s 4h "I dunno, Monika. Some people just aren't comfortable with competitive games like that."
    show sayori 4i at t42 zorder 2
    show monika at f43 zorder 2
    m 3a "Which makes it even more important that we do this, all five of us." 
    m "That way, we don't have to be afraid of how well we do!"
    show monika at t43 zorder 2
    show yuri at f44 zorder 2
    y 3n "W-What are you saying?!"
    show yuri at t44 zorder 2
    show monika at f43 zorder 2
    m 4a "If you're afraid to do something, you need to just overcome that fear and have fun!"
    show monika at t43 zorder 2
    show yuri at f44 zorder 2
    y 2r "Monika! That is the most ridiculous, arrog-{nw}"
    show yuri 3r at t44 zorder 2
    show monika at f43 zorder 2
    m 3a "Then it's settled!"
    "Monika explains the details of where we'll meet up and at what time."
    show monika 1a at t43 zorder 2
    "It's a bit strange how pushy she's being about this."
    "Why bowling of all things, especially for a {i}literature{/i} club?"
    show monika at thide zorder 1
    hide monika
    show natsuki 2f at t31 zorder 2
    show sayori at t32 zorder 2
    show yuri 2r at t33 zorder 2
    "Everything I just witnessed went by so quick, I don't even think I remember all the questions I had."
    "I guess I shouldn't expel too much mental energy worrying about it."
    show sayori at thide zorder 1
    hide sayori
    show natsuki 1r at t21 zorder 2
    show yuri 1o at t22 zorder 2
    "Besides, I'm probably just in a paranoid mental state, cause of what me and Yuri just finished reading."
    "I realize Sayori and Monika have already left, before the rest of us could continue questioning them."
    "I guess it's settled. Bowling, tomorrow..."
    n "Could have at least offered laser tag instead..."
    show natsuki at thide zorder 1
    hide natsuki
    show yuri at t11 zorder 2
    "Natsuki leaves, clearly frustrated. Wouldn't have pinned her down for that, but I guess you learn something new every day."
    show yuri at thide zorder 1
    hide yuri
    "Yuri is still processing the information. She sits at her desk dumbfounded."
    "I stay behind as well, but for some reason I don't find myself moving next to her." 
    "I guess I don't know what I could say." 
    "Still, I'm only here because she is."
    "Perhaps I just feel like she'll need someone to vent to once she processes the situation."
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    "A few minutes pass."
    show yuri 1g at t11 zorder 2
    "Yuri finally stands up, takes her things with her, and wordlessly walks out."
    "I follow."
    play music t12
    scene bg road
    with wipeleft_scene
    show yuri 1l at t11 zorder 2
    "We're about halfway home and she still hasn't spoken a word."
    "I decide to break the silence."
    mc "Hey Yuri, is-{nw}"
    y 1r "I can't believe her!"
    "Man, have I managed to get a single complete sentence out today?"
    y "It's a literature club and she's taking us {i}bowling{/i}? I still can't believe it."
    y 1f "I'm being perfectly literal, by the way."
    y 1h "I refuse to believe I understood any of this properly."
    mc "Aha..."
    mc "Yeah, I get you."
    mc "It's not that I mind bowling, but it's bizarre."
    mc "It's like it literally came out of nowhere."
    y 3r "Isn't it?!"
    y 1q "I... I don't mean to be weird in saying this but..."
    y 2t "It feels like this was planned- No... {w=0.25}{i}Designed{/i} against me."
    mc "Wh-what?"
    y 1v "You know I don't handle public places very well."
    mc "...You got along fantastically in the library, though."
    y 1h "Well, yes, but not all of them operate the same way."
    y 1f "In the case of that library, it's a place meant for reading. Nobody bothers you."
    y "Places like that, or like a park, those are fine. It's quiet, and interaction is low."
    mc "What about that lady? Y'know, {i}her{/i}."
    y 1l "She was... A rare and unfortunate exception."
    y 1f "As often as I go there, I'm obviously not familiar with all its regulars." 
    y "It's not what one would consider a great place for socailizing, even more so because you're not meant to talk above a whisper."
    y 1h "Regardless... This whole bowling thing..."
    mc "Right, right. That's what we were talking about."
    y 1f "It's not just that it's a public place, or that it has nothing to do with the theme or purpose of the club."
    y 1q "It's also to do with the fact that it's a physical activity requiring active engagement in said activity."
    y "That just feels very... Wrong to me."
    y 1h "It's not my thing."
    y 1f "Worse still, it's a popular place."
    y 1o "Crowds, physical activities, no reading, no quiet..."
    y 3n "It's sending my anxiety through the roof."
    mc "Hey, come on."
    y 3q "R-Right."
    show yuri 1e
    mc "If it's any consolation, I'll be there too, y'know."
    mc "I can protect you... {size=-5}Or something.{/size}"
    "I sort of mumble that last part."
    y 1u "R-Right."
    "Saying that to someone taller than you, even if by only a few inches, is a bit awkward. I can't imagine it's any less so on her end."
    "Either way, all of this is certainly new information to me."
    "I mean, I should realize by now that Yuri's shy. That's sort of how we met."
    "But I don't think we've ever been gearing up to be in a public setting like this."
    "It's also possible she's exaggerating due to the surprise timing of the announcement."
    "Either way, I'm sure everything will be fine tomorrow."
    show yuri at thide zorder 1
    hide yuri
    "We hit her block, and I wave goodbye as she walks toward her house." 
    "I turn back to mine, apprehensive of what tomorrow brings."
    stop music fadeout 2.0
    scene black
    with wipeleft_scene
    pause 3.0
    play music t6
    scene bg bowling_alley
    with wipeleft_scene
    "I get to the bowling alley Monika was telling us about."
    "Honestly, I didn't want this to be the way I spent my Saturday..."
    "...But here I am, anyway."
    show natsuki 1ba at t41 zorder 2
    "With Natsuki..."
    show sayori 1ba at t42 zorder 2
    "...Sayori..."
    show monika 1ba at t43 zorder 2
    "...Monika..."
    show yuri 3bo at t44 zorder 2
    "...and, of course, Yuri."
    "In total honesty, Yuri's the reason I'm not ditching." 
    "I don't think she could handle being alone like that."
    "Or... Come to think of it, maybe if I didn't come, she wouldn't have either."
    "Especially because, well..."
    hide natsuki at thide zorder 1
    hide natsuki
    show sayori at thide zorder 1
    hide sayori
    show monika at thide zorder 1
    hide monika
    show yuri at thide zorder 1
    hide yuri
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "...?" 
    "{i}[player]!!!{/i}"
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    show sayori 1ba at t21 zorder 2
    show yuri 2bo at t22 zorder 2
    "I wake up to a loud racket coming from outside my room."
    "...And I find Sayori and Yuri being... Well..."
    s "I still don't get it, Yuri. Why come all this way?!"
    show yuri 3bp at h22 zorder 2
    y "C-couldn't I ask you the same?"
    s 1bh "I... I live next door."
    s "You didn't know that?"
    y 1bo "I do, I-I must have forgotten."
    s 1bi "Huh."
    mc "What's going on out here?"
    y 3bp "[player]!"
    y 3bn "I tried texting you, but you wouldn't pick up!"
    y "So I tried coming over, but your door was locked..."
    "I pondered if Yuri didn't also lock her doors before going to bed."
    y 2bo "...So I was standing out here unsure what to do for a good half hour before I decided to start calling your name..."
    y "...That's when Sayori came around and-"
    mc "Let you in. Right, alright, I get it."
    "I gave Sayori my spare key at some point because it was easier than letting her in every time she came over."
    s 1bh "[player], do you know what's going on?"
    s "I mean, I was planning to come here because I knew you were gonna sleep in, but Yuri, too?"
    mc "Huh, so you finally wanted to return the favor for all the times I had to stop you from sleeping in?"
    s "That's different! Going to school sucks! And if you didn't care so much, you'd sleep in too!"
    "She was completely right, and this exact scenario was perfect evidence that I would indeed sleep through something I didn't care about."
    mc "Look, I don't think there's anything \'going on\'."
    mc "She just wanted to see her boyfriend and I was very... Very asleep."
    "Both gave a shocked look."
    s 1bl "Boyfriend... Huh?"
    y 3bd "Boyfriend..."
    "A satisfied smile crept upon Yuri's face."
    "After a bit of silence, I herded the two out of my room and got myself ready."
    stop music fadeout 2.0
    play music t6 fadein 2.0
    scene bg bowling_alley
    with dissolve_scene_full
    show natsuki 1ba at t41 zorder 2
    show sayori 1ba at t42 zorder 2
    show monika 1ba at t43 zorder 2
    show yuri 3bo at t44 zorder 2
    "So... Here we are."
    "On the walk there, I read some texts Yuri sent, and it turns out she actually did want us both to just stay home."
    "I'm sure that would have worked out, even if it'd take some effort to get Sayori off my back."
    "Or maybe I could have had her stay home, too."
    "Leave Natsuki to entertain Monika's whims."
    "I sigh."
    show sayori at f42 zorder 2
    s 3bc "Don't sigh, [player]!"
    s "They say every time you sigh..."
    s "With the air, some of your happiness escapes, too!"
    show sayori at t42 zorder 2
    "Who the hell says that?"
    mc "I guess that explains why you're so happy. You never sigh."
    mc "Despite that name of yours, I guess."
    show sayori at f42 zorder 2
    s 1br "Ehehe..."
    show sayori 1bo
    extend "I don't get it."
    mc "Of course you don't... {i}Sigh{/i}ori."
    "I side grin and give a smug look."
    s 1bb "Why are you emphasizing it like that?"
    "Both the grin and the smug look are defeated with that one sentence."
    mc "You know what, never mind..."
    "Either my joke was stupid, she's stupid, or both."
    "Turning my attention back to Yuri, she seems quite distraught."
    show sayori thide zorder 1
    hide sayori
    show yuri at t11 zorder 2
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    "I get close to her, in an attempt to give some sort of comfort."
    show monika 1bb at t11 zorder 2
    show yuri at thide zorder 1
    hide yuri
    m "Alright, everyone! We need to get our bowling shoes."
    m "I need to know everyone's shoe size."
    show natsuki 1bc at f22 zorder 2
    show monika 1bb at t21 zorder 2
    n "Can't we just buy our own shoes? You're not our mom."
    show natsuki at t22 zorder 2
    show monika 3bl at f21 zorder 2
    m "As club president, it would be irresponsible of me to make my club members spend their own money on club-related activities."
    show natsuki at f22 zorder 2
    show monika at t21 zorder 2
    n "How exactly do you define \'club-related\'?"
    show natsuki at t22 zorder 2
    show monika at f21 zorder 2
    m "We came here as a club activity, that's why everyone's here."
    m "It's club-related."
    show natsuki at f22 zorder 2
    show monika at t21 zorder 2
    n "Really putting the literature in literature club. With... Bowling."
    show natsuki at t22 zorder 2
    show monika 1bh at f21 zorder 2
    m "Look, Natsuki, you've gotta stop with that."
    m "Sometimes we just need to boost morale, and fun, leisurely activities like bowling do the trick."
    show natsuki at t32 zorder 2
    show monika at t31 zorder 2
    show yuri 1bh at f33 zorder 2
    y "Monika... I'm starting to think you don't understand your own club members very well."
    show natsuki at f32 zorder 2
    show monika at t31 zorder 2
    show yuri at t33 zorder 2
    n "I agree. For one, I don't feel particularly morale boosted!"
    show natsuki at t32 zorder 2
    show monika at t31 zorder 2
    show yuri at t33 zorder 2
    mc "Yeah, I... Monika, honestly, I mean, it sounds fun, but only you and Sayori seemed to show any particular interest in this."
    show natsuki at t32 zorder 2
    show monika 1bl at f31 zorder 2
    show yuri at t33 zorder 2
    m "That's not true."
    show natsuki 1bv at f32 zorder 2
    show monika 1bg at t31 zorder 2
    show yuri 1br at f33 zorder 2
    "Nat, Yuri & I" "Yes it is!"
    show natsuki 1br at t42 zorder 2
    show monika 1bo at t41 zorder 2
    show yuri 1bq at t43 zorder 2
    show sayori 1bk at f44 zorder 2
    s "I... I'm starting to have second thoughts..."
    show natsuki at t42 zorder 2
    show monika at f41 zorder 2
    show yuri at t43 zorder 2
    show sayori at t44 zorder 2
    m "You too, Sayori?"
    m 1bi "Look, come on, we're all here. Whether it was a bad decision or not, we might as well make the most of it, right?"
    m "I'm gonna go get the shoes."
    show monika at thide zorder 1
    hide monika
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show sayori at t33 zorder 2
    "We... Never actually gave her our shoe sizes, did we?"
    show natsuki at thide zorder 1
    hide natsuki
    show sayori at thide zorder 1
    hide sayori
    show yuri at thide zorder 1
    hide yuri
    scene bg bowling_alley
    with wipeleft_scene
    "Well, we're in it for the long haul now, I suppose."
    "Everything's paid for, we've got our shoes, our balls, and a lane."
    "Not that the shoes are the right size, since we didn't actually give them to her."
    "Honestly, I'd complain, but I know it'd just make Monika feel worse."
    "I bet she feels terrible right at this moment for how opposed to this situation most of us were."
    "Man though, there's a lot more people here than even I expected. "
    show yuri 1bo at t11 zorder 2
    "I'm sure Yuri isn't too fond of that fact."
    show yuri 1bn at t11 zorder 2
    "Absentmindedly, I grab her hand."
    show yuri 1bq at t11 zorder 2
    mc "Y-you alright?"
    y 1bm "Yes, I-I'm fine, ahah..."
    "Awkward as ever, but it seems to have calmed her nerves a bit."
    show yuri at t21 zorder 2
    show monika 1ba at f22 zorder 2
    m "Okay, everyone! How many of you know how to play?"
    show monika at t22 zorder 2
    "Sayori and I raise our hands."
    show monika at f22 zorder 2
    m 3bb "Oh! [player], you know how?"
    show monika 3bb at t22 zorder 2
    mc "Ah, more or less."
    show monika 1bb at f22 zorder 2
    m "Wow, that's surprising! I'm impressed."
    show monika 1bb at t22 zorder 2
    "Is she insulting me?"
    show yuri at thide zorder 1
    hide yuri
    show monika 1bb at thide zorder 1
    hide monika
    "Monika explains the rules to Yuri and Natsuki."
    "After the explanations end, we enter our names into the system."
    show monika 2bb at t11 zorder 2
    "Monika confidently enters herself into the system first: \"Mon.\""
    show monika 2bb at thide zorder 1
    hide monika
    show sayori 1bq at t11 zorder 2
    "Sayori flutters over next, happily entering a name: \"Say.\""
    show sayori at thide zorder 1
    hide sayori
    show natsuki 4bs at t11 zorder 2
    "Then, stiffly, Natsuki does the same: \"Nat.\""
    show natsuki at thide zorder 1
    hide natsuki
    "It's my turn."

    $bwlnm = renpy.call_screen("bowlingInput","Enter a bowling nickname for yourself").upper()
    if bwlnm == "" :
        $bwlnm = player[:3].upper()

    show yuri 2bo at t11 zorder 2
    "It's Yuri's turn. She again seems all too nervous."
    "She slowly types into the system: \"Y...\" \"r...\" \"i...\""
    show yuri at thide zorder 1
    hide yuri
    "It reads like \"MON,\" \"SAY,\" \"NAT,\" \"[bwlnm],\" and \"YRI.\""
    show monika 1bi at t11 zorder 1
    "After a silent shuffle back to our seats for the rest of us, Monika stands at the lane."
    show monika 2bk at t11 zorder 2
    "She gets a strike on her first try."
    show monika 2bk at t21 zorder 2
    show sayori 4br at f22 zorder 2
    s "Woah! Good job, Monika!"
    show monika 1bn at t21 zorder 2
    show sayori 4bl at t22 zorder 2
    mc "The most athletic one here doing well at a sport? I'm shocked."
    show monika 1bn at t41 zorder 2
    show sayori 4bl at t42 zorder 2
    show natsuki 4bd at t43 zorder 2
    show yuri 3bq at t44 zorder 2
    "Natsuki smirks, as does Yuri."
    show monika 1bj at t41 zorder 2
    show sayori 3bo at t42 zorder 2
    "Her frame being over, she sits down, taking the empty seat next to me. Sayori goes up next, and ends up bowling two gutter balls in a row."
    s 4bm "Uwaah! I used to be better at this..."
    "Wait, wasn't there a thing you could turn on for kids so there's blockers on the gutters?"
    "I guess maybe she always played with those."
    show monika at thide zorder 1
    hide monika
    show sayori at thide zorder 1
    hide sayori
    show natsuki at thide zorder 1
    hide natsuki
    show yuri at thide zorder 1
    hide yuri
    "Play continues to rotate between the 5 of us."
    "After my throw comes Yuri."
    "Who... Isn't here."
    show monika 2bb at t11 zorder 2
    m "Yuri excused herself to the bathroom while you were on your set, [player]."
    "That explains how I didn't notice."
    m 4bn "Man, I expected better from her. It's like she was waiting exactly for you to be distracted so she could leave."
    "What...?"
    "What did Monika mean by that?"
    "Though what she said kind of made sense."
    "I can't help it that the timing seems incredibly coincidental."
    "Maybe she's upset with me because I slept through her text."
    "But if that were the case she'd... Tell me, right?"
    show monika at thide zorder 1
    hide monika
    "As I ponder this, the rotation continues. I take my turn dejectedly and sit back down, and realize Yuri's once again absent."
    mc "She's sure uh, taking a minute, huh? I guess we can skip her again..."
    show monika 3bl at t11 zorder 2
    m "Yeah. It's a shame. She might've even just left by now."
    "Hmmm... Yuri just leaving..."
    "She wouldn't have done that without telling me or anyone of us, right?"
    show monika at thide zorder 1
    hide monika
    "Right?"
    "As I begin to check my phone in desperation, I notice a presence occupying the space next to me."
    show yuri 2bf at t11 zorder 2
    y "[player], are you alright?"
    y "You look a bit worried..."
    "Yuri puts a hand on my back and gently moves it up and down."
    mc "Oh, yeah I'm... I'm alright."
    show yuri 2bc at t11 zorder 2
    "I look into her smiling face and realize I really shouldn't have been so worried."
    "As Monika completes her set, Yuri speaks up again."
    y 2bo "God, these shoes are terrible."
    y 1bj "I'm gonna go up to the counter and see if they'll give me a more fitting size."
    show yuri at thide zorder 1
    hide yuri
    "Before I can give a response, Yuri's already up."
    "I bowl my set, and go to sit back down, and she isn't back yet."
    "A glance toward the counter and I don't see her there."
    "That's... Weird."
    show monika 1ba at t11 zorder 2
    "Monika chimes in."
    m 3bb "Huh... Didn't she tell you she was going to go get a different pair of shoes?"
    "Wait, was she listening to us?"
    m 3bl "I guess she lied to you. Ahaha..."
    "Her laugh sounds more disappointed than joyous."
    "..."
    "I... I guess she did."
    show monika at t11 zorder 1
    hide monika
    "Last time I was just overreacting because she took a while... But how come she wasn't at the counter?"
    "As this idea continues to trouble me, I feel a presence on my right side once again."
    "A tap on my shoulder draws my attention to it instantly."
    show natsuki 3bs at t11 zorder 2
    "It's Natsuki."
    mc "Eh? Natsuki? What's up?"
    "She looks down at the floor at first, but seems to gain the courage to look up at me."
    "It's strange, she... She's kind of acting like Yuri."
    n 3bq "You're worried about her too, aren't you?"
    n "Yuri, I mean."
    "..."
    mc "Yeah, I... I dunno what to think."
    n 3bb "I think you should go look for her. I can take over your bowls if you want, or we can just skip you like we have been for her."
    n 3bq "I knew she'd be against this. I don't like it too much either. But I didn't expect her to take it like this..."
    "This is really weird."
    "I don't recall Natsuki ever talking to me like this."
    "But I'm worried about her, too."
    show natsuki 3bi at t11 zorder 2
    mc "Alright, take over for me."
    show natsuki 1bj at t11 zorder 2
    "Natsuki gives a slight smile and a nod."
    show natsuki at thide zorder 1
    hide natsuki
    "I walk away and head to the front counter, asking the clerk about whether or not he's seen a tall girl with purple hair pass by."
    "He mentions to check over by the food section around the other end."
    scene bg bowling_alley
    with wipeleft_scene
    stop music fadeout 2.0
    show yuri 4bb at t11 zorder 2
    "I head over to where the clerk mentioned, and find Yuri sitting alone at a table."
    "Her arms are on the table, with her hands supporting her head." 
    "I walk up behind and give her a tap on the shoulder, which causes her to jump."
    y 3bp "Ah!"
    "She calms down when she notices me."
    y 2bq "O-oh, [player]."
    y "I..."
    "I take a seat beside her."
    play music t9
    y 4bb "I'm sorry, [player], it's just..."
    y "You know me. I'm not exactly confident in my athleticism."
    y 4bc "I worry I'll embarrass myself..."
    show yuri 4bd at t11 zorder 2
    "I put a hand on one of hers, which seems to surprise her."
    "Honestly, it surprises me too, that I'd do something like that."
    show yuri 4ba at t11 zorder 2
    mc "Hey. C'mon, it's bowling."
    mc "We all suck, probably."
    show yuri 4bb at t11 zorder 2
    mc "Well, maybe except Monika..."
    mc "The point is, its not like we have any right to judge you for it."
    show yuri 4ba at t11 zorder 2
    mc "And besides, we're your friends. Why would we think less of you for something like this?"
    show yuri 4bb at t11 zorder 2
    "She looks away from me for a bit, thinking."
    "A determined look finally forms on her face."
    y 2bu "You're... You're right. Let's get back there, [player]."
    mc "That's the spirit!"
    show yuri 2bs at t11 zorder 2
    "I flash her a smile, and she returns it."
    "Both of us get up and return to the lanes."
    stop music fadeout 2.0
    scene bg bowling_alley
    with wipeleft_scene
    play music t6
    show yuri 1be at t21 zorder 2
    show sayori 3bj at f22 zorder 2
    s "[player]! Yuri! Where did you two go?!"
    "Sayori's {i}warm{/i} welcome is what we both return to, though I felt most of her anger was directed more toward me and not Yuri."
    show yuri 1be at t31 zorder 2
    show sayori 3bj at t32 zorder 2
    show natsuki 2ba at t33 zorder 2
    "Behind her I see Natsuki, sheepishly giving a smile that does actually display some sort of warmth."
    mc "I just took a minute to go track down our missing persons case here."
    mc "We're only... Three, four rounds in?" 
    show sayori 4bn at t32 zorder 2
    "Sayori begins to retort, but her turn starts before she gets the chance."
    "Monika is the only one not to acknowledge either of us, strangely."
    show yuri at thide zorder 1
    hide yuri
    show sayori at thide zorder 2
    hide sayori
    show natsuki at thide zorder 2
    hide natsuki
    "Play rotates as normal, and finally Yuri is present for one of her turns."
    show monika 4bk at t11 zorder 2 
    m "Looks like someone finally-{nw}"
    show monika 4bd at t21 zorder 2
    show natsuki 4bw at f22 zorder 2
    n "Shut it, Monika!"
    show monika 4bd at t41 zorder 2
    show natsuki 4bw at t42 zorder 2
    show sayori 4bn at t43 zorder 2
    show yuri 1bg at t44 zorder 2
    "Natsuki's outburst surprises all of us, except Yuri, who simply walks up and takes her turn."
    show monika 1bd at t41 zorder 2
    show natsuki 1bc at t42 zorder 2
    show sayori 1bn at t43 zorder 2
    show yuri 1be at t44 zorder 2
    "She ends up throwing a spare, 9 and 1."
    "Looks like Monika finally has a challenge on her hands."
    show monika at thide zorder 1
    hide monika
    show sayori at thide zorder 1
    hide sayori
    show natsuki at thide zorder 1
    hide natsuki
    show yuri at thide zorder 1
    hide yuri
    "...And that it ends up being."
    "A couple more rotations, and near the end of the game she's managed to tie things up."
    "It's weird... It's as if that one play threw Monika off her game completely, and she started doing worse than Sayori."
    "And believe me, that's an achievement on its own merits."
    "I begin to lose track, but eventually we're on the last set."
    show monika 1bi at t11 zorder 2
    "Monika is first... Who knocks down a spare."
    show monika 1ba at t11 zorder 2
    "Confident, she strides back to her seat, the game now out of her hands entirely."
    show monika at thide zorder 2
    hide monika
    show sayori 4br at t11 zorder 2
    "Sayori as usual does rather poorly."
    "She definitely seems far more happy about it than Monika though."
    "Something about ignorance is bliss, and all that, I suppose."
    show sayori at thide zorder 1
    hide sayori 
    show natsuki 3bq at t11 zorder 2
    "Natsuki and I, as are typical, don't do anything noteworthy, good or bad."
    show natsuki at thide zorder 1
    hide natsuki
    show yuri 2bh at t11 zorder 2
    "The last throw goes down to Yuri."
    show yuri 2bk at t11 zorder 2
    "Walking back to the seats, I put a hand on her shoulder."
    mc "You alright?"
    y 2bm "Yes. Thank you, [player]."
    y "I couldn't have finished this without you."
    "Once again, she displays an uncharacteristic sense of confidence."
    "She throws the ball and turns around."
    "A...{w=1.0} Perfect strike clashes against the pins as she walks away!"
    "If it were me, I'd be basking in such a power move..."
    "But if I didn't know any better, I'd say she doesn't even realize what she just did."
    "Hell, I honestly can't believe it myself."
    show yuri 2bq at t41 zorder 2
    show sayori 4br at t42 zorder 2
    show natsuki 2bl at t43 zorder 2
    show monika 1bn at t44 zorder 2
    "As Sayori runs up to give her a hug, I can tell Monika's trying to hide the feeling of defeat she's just experienced."
    show sayori 4br at f42 zorder 2
    s "Yayyy! Good job, Yuri! You won!"
    show sayori 4br at t42 zorder 2
    show natsuki 2ba at f43 zorder 2
    n "I wonder if she kept running away to build up her power or something, like in one of those books of hers."
    show natsuki 2ba at t43 zorder 2
    show yuri 2bq at f41 zorder 2
    y "You know I'm not one for those books..."
    show natsuki 2bz at t43 zorder 2
    show yuri 2bc at t41 zorder 2
    "Natsuki laughs, and Yuri gives a smile in response."
    "All's well that ends well I suppose."
    show yuri 3bf at t41 zorder 2
    show sayori 4bn at t42 zorder 2
    show natsuki 1bc at t43 zorder 2
    show monika 4bk at f44 zorder 2
    m "Okay, everyone!"
    "Monika interrupts the festivities, and Sayori releases her grip on Yuri."
    m "A well-played game, and I can tell everyone had a lot of fun."
    m "Literature club bowling day is a rounding success!"
    m 2bj "You guys want to do this again sometime?"
    $ n_name = "Everyone"
    show yuri 3bq at t41 zorder 2
    show sayori 4br at t42 zorder 2
    show natsuki 4bd at t43 zorder 2
    show monika 2bl at t44 zorder 2
    n "Heck no!"
    $ n_name = "Natsuki"
    show yuri at thide zorder 1
    hide yuri
    show sayori at thide zorder 1
    hide sayori
    show natsuki at thide zorder 1
    hide natsuki
    show monika at thide zorder 1
    hide monika
    stop music fadeout 2.0

#Scene 4
    scene bg bedroom
    with dissolve_scene_full
    "...{w}"
    play music t8
    "Eugh..."
    "As the shine of the sun hit my face, I groggily wake up and rub my eyes open to the morning again."
    "After the bowling alley yesterday, all of us seemed pretty exhausted and went straight home."
    "Though it was a bit of a rough start, it was still a pretty fun day overall after we got used to it."
    "Even Yuri, after cheering her up, got into it too, which was great to see for her."
    "Hopefully that gave her a bit of a boost, maybe we can do something like that again."
    "Just the two of us. Like a..."
    "Date..."
    "..."
    "I suddenly got a shaking feeling."
    "Like I'm forgetting something."
    "I grab my phone, and start scrolling through my messages."
    "Monika...{w=0.5} Natsuki...{w=0.5} Sayori...{w=0.5}"
    "Oh, got one from Yuri."
    "Hmm, a link to what looks like some nice looking restaurant, and a message."
    y "This is the place!"
    "Why would Yuri send me this?"
    "Wait..."
    "I vaguely remember, it was just after we had left."
    "Yuri had pulled me aside, I think..."
    "...!"
    stop music fadeout 2.0
    scene bg road_sunset
    with dissolve_scene_full
    play music t6
    show yuri 1ba at t11 zorder 2
    mc "Bowling was a lot more fun than I thought it would be, to be honest."
    show yuri 2bq at t11 zorder 2
    mc "But I think I'm mostly just saying that because of how well you did."
    mc "I still can't believe you beat Monika."
    y "Yeah, I can't believe that either."
    y 2bj "Something just clicked within me after you talked to me."
    y 2bv "But that does make me wish for something."
    mc "Wish for what?"
    y 3bw "Well, for today to just have been for the two of us."
    y 3bu "After what happened in the library and today too, I've been interested in other places we could go."
    y "The idea of going to other places with just you just sounds so... "
    show yuri 4be
    extend "Romantic."
    mc "Well, if you're in the mood for that, I guess we can always go to a restaurant."
    "Even though I have no idea where we could go."
    y 2bb "That sounds great. There's this one place I've always wanted to go with a..."
    y 2bq "Well, with a boyfriend."
    mc "If you already have a place in mind, then I would be happy to go."
    y 3bd "Perfect. I'll make the reservations tonight then, six o' clock."
    y 2bu "Oh look at me, I didn't think I would be so excited over this."
    y 3bc "Good bye [player], I'll see you later."
    mc "Bye, Yuri."
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t8
    "Oh right, Yuri and I have a date today!"
    "Man, guess I was a lot more exhausted afterwards than I thought."
    "I just barely remembered."
    "But huh... An actual date."
    "Not to say the library we went to wasn't one, I suppose."
    "Being with her these past couple of months has been great."
    "We had gotten pretty close, much more than I had thought..."
    "Luckily, we won't meet until the evening, so I have some time till then."
    "I look back at my phone, and look at the restaurant again."
    "Seems pretty fancy. Maybe I should put on something a little more formal than my usual get-up..."
    "Though, do I even {i}have{\i} anything like that?"
    "I get up and start rummaging through my messy and junk-filled closet."
    "I felt like an archaeologist digging through dirt, in search of the golden treasure amongst the rocks and rubble of the site I call my closet."
    "C'mon, I gotta have something in here that looks nice..."
    "At the far end of the closet, I spot a nice shade of grey hanging at the very end."
    "It was a nice collared shirt I must've forgotten I had."
    "It's a bit wrinkled though, but nothing a little iron couldn't fix."
    "I can get it done before I leave. Shouldn't be too hard."
    scene bg livingroom
    with wipeleft_scene
    "After some time passed, getting myself prepped and all, I was ready to go."
    "I grab my phone and type out a quick message to Yuri."
    mc "On my way!"
    "A minute or two passes, and she sends me an \'Okay!\' back immediately."
    "After taking one last look in the mirror and making some last-minute adjustments to my hair, I headed off."
    scene bg road_sunset
    with wipeleft
    "Going down this road, especially with what's going on, gives me some memories."
    "Memories of sprinting through the winter cold, avoiding looks, all for a certain someone's uniform."
    "The weather's definitely gotten warmer since that day, but it's still pretty chilly out."
    "Walking back here at night is gonna be torture."
    "{i}Like a freezing arctic wind, waiting to catch its next victim...{/i}"
    "Hehe. Sounds like something Yuri would say."
    "{i}If only I could replicate that kind of writing on my tests...{/i}"
    scene bg restaurant_front
    with wipeleft_scene
    "After a bit of time walking and following the directions on my phone, the simple and lit sign for the restaurant comes into view."
    "The whole place looks great, like something out of a romantic movie."
    "The photos for display online really lived up to the real thing."
    "Coincidentally, it was also pretty easy to find once I found out it wasn't too far from the library."
    "Staring for a little while, I feel a tap on my shoulder."
    "Slightly startled, I turn around and see Yuri behind me."
    mc "Oh hey Yu-"
    show yuri 2ba at t11 zorder 2
    "I turn to look at her, and suddenly found myself frozen in awe."
    "Perhaps it was just the neon lighting and the sunset light falling in the right place, or the atmosphere of the area itself."
    "But seeing her standing there, she looked absolutely... Breathtaking."
    "It was there I had fully grasped the situation as the feeling hit me."
    "This was our first, planned out, formal, official date."
    "With both of those ideas taking all thoughts in my mind all at once, I now figured out why I could barely even speak."
    mc "H-Hi Yuri."
    y 2bu "H-Hello, [player]. You look very... Handsome."
    mc "Thank you, Yuri. You, ah, look... Wonderful as well."
    "We stand there for a few moments, appreciating each other's appearances."
    "I felt the wind breeze past quickly, catching us from our trances."
    y 2bu "Thank you..."
    "We stood there for a bit, before I decide to break the silence."
    mc "So, this place looks great, Yuri. Very fancy I should say."
    y 1bj "O-Oh, yes. I thought it would be quite nice for a dinner for two."
    "I hold out my arm, and give my most princely smolder I could muster."
    mc "Shall we dine then?"
    show yuri 1bc at t11 zorder 2
    "Yuri giggles at my poor attempt at a posh accent, and she seems to play along."
    y 1bd "Yes, lets."
    stop music fadeout 3.0
    show yuri at thide zorder 1
    hide yuri
    scene bg restaurant
    with wipeleft
    play music t5_yuri
    "Upon walking in, the vibe of the restaurant seemed to change."
    "The interior looked a lot like a fancier family restaurant, in a way."
    "It had a very comfortable, cafe-style kind of feel to it, despite its fancy looks from the outside."
    "On top of that, it wasn't too packed. It felt very lowkey in a way."
    "Probably also why Yuri likes this place."
    "After speaking with the hostess and waiting a couple minutes, a waitress came and escorted us to our table."
    "The place didn't look too full, with maybe a handful of patrons in the whole dining room."
    "Once we got sat down, the waitress handed us some menus and water, and left us to browse."
    show yuri 1bb at t11 zorder 2
    mc "Huh, this place is really nice, Yuri. It has a very nice atmosphere to it."
    y "Yes. It's kind of simple, but I love the food here. As well as being relatively close to the library."
    mc "Oh, I see. That's a really nice touch of coincidence, I have to say."
    y 1ba "It was. I hope eating here is alright."
    mc "Oh it's fine. It'll be great, I'm sure."
    "I look through the menu and see quite a nice selection of things. From different seafoods, meats, salads, pasta, and even omelets."
    mc "So anything that you recommend, Yuri?"
    y 2bn "Me?"
    y 1bo "Ahh... Hmmm..."
    y 1bf "The curry omelet is always a good choice... It's simple, but tastes delicious."
    y 2bb "Their bolognese pasta also is good if you're in the mood for something like that, the sauce has a really nice flavor to it."
    y 1bd "And oh! Their red wine steak platter is also really..."
    "She names off a couple more different dishes with intricate descriptions of their tastes and ingredients, getting more excited with each one."
    y 3bn "Oh... I hope I didn't ramble on too much..."
    mc "Oh no, it's okay."
    y 2bg "Sorry, that tends to happen."
    mc "Don't worry about it, Yuri." 
    mc "You looked really happy, and I didn't feel like interrupting."
    y 1bi "I see. Thank you, [player]."
    y "This place holds a couple of good memories for me, I suppose."
    y "Along with the food, of course."
    mc "Ohh, I see. This seems to be a bit of a go-to place for you, I'm guessing."
    y 1bb "Yes, I guess it kind of is like that."
    y "My parents took me here for many celebrations since I was little. And it was always fun."
    y "Birthdays, good grades, graduations..."
    y 1bc "I'm really glad I was able to come and show this place to you, [player]."
    mc "Hm, it is pretty fitting."
    mc "I suppose the two of us coming here on a date is a celebration in and of itself."
    y 1ba "Hm, I agree."
    y "I... Don't think I would have ever thought of coming here for something like that before."
    y "But, whenever I'm around you, I feel comfortable and happier."
    mc "I'm glad that you are happy, Yuri."
    mc "It'll always be a highlight."
    "The two of us smile at one another for a moment."
    show yuri at thide zorder 1
    hide yuri
    scene bg restaurant
    with wipeleft
    "After a bit, the waitress came by again to take our orders."
    $ n_name = "Waitress"
    n "So one beef java curry, and one red wine steak platter with potatoes, medium rare."
    n "Sounds great! We'll have that out for you in a jiffy!"
    mc "Thank you very much."
    show yuri 1ba at t11 zorder 2
    mc "Hmm, java curry. Like coffee, right? Can't say I have tried that before, interesting."
    y "I've heard of some recipes adding instant coffee to the mix, and coincidentally saw that they were adding it to the menu here." 
    y "I wanted to taste it first before trying to make it myself."
    mc "Oh, I see. You like to cook a lot, Yuri?"
    y 2bq "Oh, just ah... A little bit."
    y "I just follow whatever is in the cookbooks."
    mc "Oh, cookbooks?"
    y 2bo "Y-Yes. Besides novels, I try to read a certain variety of books that can relate to my everyday life."
    y 3bq "I find it quite enjoyable."
    "Hm, I always thought she was only into fiction books. I don't see her reading much else often."
    mc "Yeah, that's pretty cool, cooking things from scratch."
    mc "I'm not much of a cook, but maybe one day we can cook together and taste each other's food."
    mc "That'll be fun."
    y 1bq "Y-yeah. Maybe. I think it will, with the two of us."
    mc "Definitely. We can even have a cookout with everyone too, show off your cooking skills."
    y 2bd "Heh, that sounds like fun as well."
    "The two of us laughed together, chatting a little while just before our food arrived."
    n "Alright, here it is, one beef java curry, and the red wine steak."
    "The waiter set down the steaming hot platters in front of each of us. It all looked really appetizing."
    n "Enjoy!"
    show yuri 1bd at t11 zorder 2
    $ y_name = "Yuri and I"
    y "Thank you for the meal!"
    $ y_name = "Yuri"
    "The two of us immediately got started, and ate to our heart's content."
    "The steak was nice and juicy, and the sauce complimented it quite well."
    y 1bc "Ah, what an interesting addition, so perhaps that's what it does to the flavor..."
    mc "Have a revelation?"
    y  1ba "Oh yes. The curry seems to have a rather richer flavor with the addition of the coffee."
    y "I've always enjoyed it without it, but having it adds an interesting other depth."
    "Yuri immediately gets a spoonful, and offers it to me."
    y 2bb "Here, you should try some."
    "I looked for a couple seconds, wondering, but I instinctively went in to taste it."
    y 2bn "Oh...!~"
    mc "Huh, you weren't kidding. It has an interesting flavor to it."
    mc "Yuri? What's wrong?"
    y 1bo "I offered it and fed you, without realizing it..."
    mc "Oh..."
    "I went in without thinking about it either. I think I may have blushed a little myself after she explained it."
    mc "Ah... I'm sorry about that."
    y 1bj "That's okay... I just got absorbed and didn't think either..."
    y 1bs "Though... We are dating... That's something that couples do, right?"
    mc "Yeah... That's true."
    "After some quick thinking, I cut off a piece of my steak, and put it on my fork."
    mc "In that case, would you like to try some of mine?"
    y 3bn "Eh?!"
    mc "I tried some of yours, so I thought it'd be equal to offer."
    y 3bo "Ah... Umm..."
    "Though with some hesitation, she goes in for a bite."
    show yuri 1bd at t11 zorder 2
    "After a moment of chewing, the nervousness on both of our faces seems to fade away."
    "After a little bit, I feel a smile crack on our faces as the both of us laugh it off."
    "With the moment over, we happily continue and finish up our meals."
    $ n_name = "Natsuki"
    show yuri at thide zorder 1
    hide yuri
    stop music fadeout 3.0
    scene bg yuri_house_night
    with wipeleft
    play music t13
    "After eating and paying the bill, I decide to walk Yuri home."
    "I slightly remember the path from that one morning, but as we got closer, the memories start to come back to me."
    "What a morning that was, for sure."
    "Walking and talking for a little while as I followed her, we finally reached her home."
    show yuri 1ba at t11 zorder 2
    y "Well, this is my stop then."
    y 1bc "I really enjoyed tonight, [player]."
    y "It was really fun coming out with you."
    mc "Definitely, it was a lot of fun. We should definitely do this again sometime."
    "The night really was great as I look back on it."
    "Got to spend some quality time with Yuri, eat at a nice place..."
    "I really wish we didn't have class tomorrow or anything like that."
    mc "Well, it is getting kind of dark out, so I should get go-"
    stop music fadeout 1.0
    "Suddenly, I got a soft feeling on my hand the moment I thought of turning around."
    y 4be "Wait! Ah... [player]."
    y 4bd "I...  Umm... Do you...? Mmm..."
    play music t9
    "It was clear to me Yuri was having a hard time putting her words together, but I think I know what she wants to say."
    mc "Would you like me to come inside with you?"
    show yuri 4bc at t11 zorder 2
    "She simply nodded."
    y "Y-Yes... I would."
    "I could feel my cheeks immediately get flushed at her request."
    "There she goes, putting her charming spells on me again."
    "It was hard to say no, especially since I could immediately read what she wanted from me."
    "As fate would have it though, I felt a cold breeze run through me as we stood there staring at each other."
    "I felt my body visibly shiver, with Yuri feeling the vibration through my hand."
    y 4ba "I... Would also hate if you were to catch another cold..."
    "An incredible woman wants me to come inside her home with her, while I have school tomorrow..."
    "It's either a really good stroke of luck, or misfortune."
    "I felt her warm grip on my hand tighten."
    y 4bb "Please... Don't go yet."
    "I don't have much of a choice, do I?"
    mc "Of course, I'll stay a little longer."
    y 4be "Thank you..."
    "{i}I wonder how much the word 'little' will mean after this.{/i}"
    show yuri at thide zorder 1
    hide yuri
    scene bg yuri_bedroom_night
    with wipeleft_scene
    "As we entered the house, Yuri guided me down from the main hallway into her bedroom."
    "There was a sense of slight familiarity as we went in, reminiscing to the events of that morning again."
    "But now that I had a chance to fully look around now, it's like I'm in a different world entirely."
    "I wonder if this was how Yuri felt when she visited my house."
    show yuri 1ba at t11 zorder 2
    y "Ah, here. Make yourself at home, [player]. I'll go get us something to drink."
    show yuri at thide zorder 1
    hide yuri
    "Yuri went back a little way down the hall as I looked around."
    "Her room was almost a librarian's dream, what with the books all around."
    "Shelves filled with books neatly tucked in, with even some on her desk."
    "The room had a comfortable atmosphere to it, now seeing it in more detail." 
    "The familiar scent of the aromatherapy candles from a while back wafted throughout her room."
    "I glanced at the spines of some of the books, seeing a bunch of familiar and unfamiliar titles all around."
    "If there was ever a title for a literature bug somewhere in the world, I'm sure Yuri would qualify easily."
    "Just then, Yuri appeared with a platter with two cups on it."
    show yuri 1ba at t11 zorder 2
    y "Here's some tea if you'd like some, [player]."
    mc "Oh, thank you very much."
    "I go to grab one of the glasses as I see Yuri going and cleaning up the books on the desk."
    y 1bv "Sorry, I didn't have much time to clean up as I wanted to."
    mc "That's alright. Here let me help you with that."
    y 2bn "Oh it's okay. I can get it."
    "I see Yuri just take a stack and pile it into the shelf very quickly and neatly."
    y 2ba "Ah, there we go."
    mc "I have to say though Yuri, your house is really nice. How long have you lived here?"
    y "For a while, even before I was born. My parents moved here when they were young."
    y 1bb "They did quite a bit of customizing to get a certain \"flavor of life\" as they said."
    y "It took a while to get it right, but they still change a few things here and there all the time."
    mc "Oh, I see. It has a very traditional aesthetic. It's very cozy."
    y 1bd "I'm sure they'll be glad to hear you say that."
    "The two of us laugh, drinking our tea for a moment of silence and rest."
    show yuri 2bi at t11 zorder 2
    "I look up at Yuri as she looks like she's spacing out staring at me."
    "Before I could say a word, I felt her come close to me and put her hands around my waist."
    y 4bb "[player]..."
    y 4bd "Can you... Hold me...?"
    show yuri 4ba at t11 zorder 2
    "I could feel the lustful, but shy energy in her voice and movement as she went up to me."
    "And I happily obliged."
    mc "Of course."
    show yuri 4bb at t11 zorder 2
    "I wrapped my arms around her for a moment, embracing her as I looked down."
    "Immediately, Yuri looks up, and gives me a kiss, causing me to reciprocate it."
    show yuri 4bc at t11 zorder 2
    "We easily get caught up with one another before she pushes me on her bed and lands on my lap."
    "I could feel her warm breathing as she laid against me, her hands rolling over my shoulders and chest."
    stop music fadeout 2.0
    show yuri 1bo at t11 zorder 2
    "But after a minute, she sits up."
    mc "Yuri? Are you alright?"
    y "Ah... Yes..." 
    y "I-I'll be right back, I just have to visit the restroom."
    y "Please just wait here a moment..."
    mc "Oh, okay. That's fine."
    show yuri at thide zorder 1
    hide yuri
    "Yuri immediately went up to the right, up the hall."
    "I sat up and waited for her, but I couldn't help but think about what had just happened."
    "Something was definitely bothering her, but I can't really put a finger on what."
    "I want to at least check up on her, see if everything is okay."
    "Then again, maybe she just needs a moment, and just needed to go to the bathroom."
    "I wouldn't want to impose and put more pressure on her than need be."
    menu:
        "What should I do...?"
    
        "Go check up on her":
            "Shuffling my hands for a couple more minutes, I couldn't help but keep thinking."
            "Eventually, my mind got the best of me."
            "I had to go see if everything was okay, at the very least wait for her outside of the bathroom."
            "I immediately get up and go the direction she had gone."
            scene black
            with wipeleft_scene
            "The hallway was partially dim, but it was still pretty manageable to walk around."
            "I walked slowly, hoping not to run into anything I didn't see."
            "As I made my way further down, I see a sliver of light come through an open door in front of me."
            "I can see Yuri by the restroom's sink, holding onto something as she stood there."
            "As I got closer, I can hear noises coming from her. Like she was heavily breathing."
            "Or...{w=0.25} Crying?"
            "My curiosity and concern were similarly piqued."
            "I walk slowly up to the door, and knock."
            mc "Yuri... Is everything okay?"
            y "...!"
            y "Ah! [player], wait...!"
            scene bg yuri_bathroom
            with dissolve_scene_full
            play music t10
            show yuri 3bpc2 at t11 zorder 2
            "However, the moment I touched the door, it opened up."
            "I was presented to a scene akin to something out of a horror movie."
            "A strip of used bandages laid on the countertop next to a box, as Yuri had a look of shock and fright on her face seeing me."
            "But all I could see was her arms again, her sleeves rolled up."
            "Rows of dried and scabbed cuts adorned them. There were some I had recognized..."
            "And some... Relatively new."
            "A deep pit of worry set in my chest and stomach."
            "It was just like that day she had shown them to me, the memory flashing back and forth in my head."
            "A part of me had a feeling about all this, about Yuri's issues..."
            "That everything wouldn't be fixed after just one talk with her."
            "But to see it for myself right in front of me..."
            "All I could do was stand there."
            "But I had to ask her myself. I had to hear it from her."
            mc "Yuri... Have you... Been cutting yourself?"
            show yuri 5bbc2 at t11 zorder 2
            "She stood silent for a moment, but eventually she spoke."
            y 5bdc2 "Y-yes... I have."
            "I felt my heart sink."
            "She had been holding it all this whole time, bearing through it."
            "Even now, she had the same cloud of shame hanging over her as I looked at her."
            y "[player]... I'm still scared..."
            y "I-I thought after everything, with you that day, that it would be fine then."
            y "Those fears, being alone, it all still lingered around."
            y 5bec2 "But whenever we were together, playing games, reading, in bed..."
            y 4bjc2 "I felt beyond those thoughts, more than I ever had."
            y "I was in my happiest place whenever I was with you."
            y 4bkc2 "But after that, I... They always came back."
            y "The thoughts of being alone again, the doubt of my friendships with the others..."
            y "But the worst thought was the one of about being away from you."
            y 3by6c2 "That's why I wanted you to be here. I couldn't let go."
            y "I couldn't bear losing you, I wanted that thought gone. To hold you and never let go..."
            y "I..."
            show yuri at thide zorder 1
            hide yuri
            "Before she could say another word, I immediately ran to her and wrapped my arms around her, and hugged her as tight as I could."
            "I felt my heart in my throat with everything she said, and I couldn't bear it much more."
            mc "It's okay. I'm right here."
            mc "To think that you were still holding in all of that this entire time..."
            y "[player]..."
            mc "Yuri, do you remember what I told you that day, when you first showed me your arms?"
            mc "When you questioned whether I'd love you even till the day I die?"
            y "O-Of course..."
            mc "I still mean it, and it hasn't changed since then."
            mc "I may not be able to stop you from thinking those things all the time..."
            mc "But just know that I'll always be there to love you if they do."
            mc "Please Yuri, believe in me, rely on me now."
            mc "Even if those thoughts come up again."
            mc "And I'll always be there."
            y "[player], thank you... I will."
            y "I know the thoughts won't go away, but to hear you say it..."
            y "It comforts me all over again."
            y "I love you, [player]."
            scene black
            with dissolve_scene_full
            "We embrace each other one more time, as she looks up at me again, and kisses me."
            y "I... I know I just asked... But can you please stay with me tonight?"
            mc "Of course."
            "With a smile, Yuri and I returned to her room."
            stop music fadeout 2.0

        "Stay and wait for her":
            "It's probably better to leave her alone for a bit."
            "If anything, I could probably talk to her when she got out anyway."
            "I continue to lay down on the bed, twiddling my thumbs for a little while until I heard a door close from down the hall."
            "Yuri walks into the room and closes the door behind her."
            show yuri 1ba at t11 zorder 2
            y "Sorry that took a while."
            mc "It's okay, don't worry about it."
            "I look at her for a moment as she looks around the room almost listlessly."
            "She seemed to be lost in thought again, rubbing her sleeves in contemplation." 
            mc "Is everything okay, Yuri?"
            y 3bn "H-huh? Oh no, it's nothing." 
            y 3bo "Just thinking about some things, that's all..."
            "She immediately lays down next to me, the two of us snuggling up closely to one another."
            "I held her as she slowly came closer to me, and the two of us went back into the same position from before."
            "She laid on my chest, her head cradled against me without a word."
            y 1bi "I'm... Very happy to have you here with me, [player]."
            y "It calms me down whenever I can be near you. The world just... Stops."
            y 3bm "And when I can feel you like this, every bad thought I had before just goes away..."
            y "It makes me glad I could be with you like this."
            y "And I cherish every moment."
            mc "I'm... Glad you see me like that. And it makes me happy that you are happy."
            "I drew her closer to me, the two of us being able to see eye to eye now."
            "There was a lingering thought in my head as we laid there, as if this was coming from something."
            mc "...If there is something bothering you, Yuri, we can talk about it."
            mc "You can always lean on me if you need it."
            y 3ba "I... Just had a lot on my mind lately."
            y "Those thoughts from before, and such."
            y "But... I feel a lot better now with you. I don't need to worry anymore that you are here now."
            scene black
            with dissolve_scene_full
            "I felt her plant a kiss on my lips as she got closer."
            mc "Yuri..."
            y "Please. Take me, and never let go..."
            stop music fadeout 2.0
    "I kept her company for the rest of the night."
    "I wanted to make sure she knew she was cared for. That what I said, I fully meant."
    "But I know those feelings can be fleeting."
    "But for now, this is what she wanted, and I was here for her."
    
    

#Scene 5
    scene bg club_day
    with dissolve_scene_full
    play music t8
    "With another day at the club wrapping up, Yuri and I were lost in conversation discussing our book together..."
    "The time we spend together, just like this, is always magical."
    "With what happened the other night, it's great things are seemingly all together at least."
    show monika 2a at t11 zorder 2
    m "Okay everyone! I've got an exciting announcement!"
    "Monika popped up from her desk, clearly enthused about her surprise."
    m "I thought since graduation is right around the corner, we should celebrate with a weekend activity!"
    show sayori 1b at f21 zorder 3
    show monika 2a at t22 zorder 2
    s "What did you have in mind? Writing poems together?"
    show natsuki 1b at f31 zorder 3
    show sayori 1b at t32 zorder 2
    show monika 2a at t33 zorder 2
    n "No way! It's probably some dumb sleepover or something."
    m 4b "Unfortunately, you're both wrong. I've gotten us a weekend getaway at a mountain lodge!"
    "Natsuki and Sayori were startled at the news. Yuri quickly spoke up, I could see the shock across her face as well."
    show yuri 1f at f41 zorder 3
    show natsuki 1b at t42 zorder 2
    show sayori 1b at t43 zorder 2
    show monika 4b at t44 zorder 2
    y "W-What? H-How on earth did you get tickets for that sort of place?"
    show yuri at t41 zorder 2
    show monika at f44 zorder 3
    m 5a "Well... I kinda won a contest on the radio! Ahaha~."
    mc "Wait. A radio contest? I didn't hear anything about that..."
    m 4k "It must've been a station you don't listen to."
    m "But the point is, I won five tickets, and I thought it would be a nice way to spend the weekend!"
    show monika at t44 zorder 2
    "Monika smiled at all of us. Sayori being the first to show her enthusiasm."
    show sayori at f43 zorder 3
    s 4r "Well, I think it's really cool! Thanks Monika!"
    show sayori at t43 zorder 2
    show natsuki at f42 zorder 3
    n 2z "Yeah, that sounds kinda neat, actually!"
    show natsuki at t42 zorder 2
    y 3g "..."
    show monika at f44 zorder 3
    m 1d "Everything okay, Yuri?"
    show monika at t44 zorder 2
    show yuri at f41 zorder 3
    y 3t "O-Oh, yeah. Thanks, Monika."
    show yuri at t41 zorder 2
    mc "Hmmm, its a little out there, but sounds kinda nice. Thanks."
    "With all of us agreeing in the end, it looks like our weekend is set."
    show monika at f44 zorder 3
    m 4b "We'll all meet up in front of [player]'s house. How about tomorrow morning at, say, seven?"
    mc "Ah, sure, that could work."
    show monika at t44 zorder 2
    show sayori at f43 zorder 3
    s 4x "Sounds good to me!"
    show sayori at t43 zorder 2
    show natsuki at f42 zorder 3
    n 4z "See you guys there!"
    show natsuki at t42 zorder 2
    mc "Bye guys."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    hide sayori
    hide monika
    hide natsuki
    show yuri 3w at t11 zorder 2
    "As the others left the room, Yuri and I stayed behind."
    "She quickly turned to me, concern clearly in her eyes."
    y 4a "I-I... I really don't want to do this..."
    mc "I know what you mean. I'd much rather... Y'know..."
    y 2q "R-Read instead?"
    mc "...Yeah."
    y 3u "It's the same with me... I never really liked hotels to begin with, but now spending a weekend in the mountains? Uhh..."
    mc "Same here. But, it might not be good to skip out."
    mc "At least too, we could have some alone time up there, catch the scenery, just the two of us maybe?"
    "I spoke reassuringly to Yuri, but also to myself."
    "It sounded like a great opportunity for the two of us to spend some alone time together."
    y 3g "I-I suppose you're right."
    y 3u "But... I'm looking forward to that alone time... We should read while we're up there."
    mc "Absolutely."
    show yuri at thide zorder 1
    hide yuri
    "After our discussion, Yuri and I left."
    "Monika had met with us to lock the door behind us, but otherwise left us alone while we were in there."
    "I wonder if she heard, but she seemed to have walked away without saying anything."
    "Well, if she did, at least we sort of figured it out, and she left us alone about it."
    "For now, hopefully she won't meddle too much if she decides to."
    stop music fadeout 2.0
    scene bg bedroom
    with wipeleft_scene
    "As I was packing my things, getting ready for the trip tomorrow, I was sifting through the things I thought we would need, and the stuff Yuri and I would want."
    mc "Clothes... Coat... Toiletries... Books... I think I'm good!"
    "While telling myself that, I got a notification on my phone."
    "Yuri had sent me a text."
    y "Monika says that ice-skating is a possibility, so if you want, feel free to bring skates."
    "Skating? I've never really done that... But if Yuri is interested, then maybe."
    "I caught myself imagining myself skating with Yuri."
    "The two of us gliding across the ice, hand in hand."
    "It sounded like magic."
    "I quickly texted back, saying I'd bring them. Yuri then sent another message."
    y "I'm still uneasy about all of this...?"
    "I smiled to myself, before sending my reply."
    mc "No need to worry, it'll all work out. Trust me."
    "I knew she can be really nervous. But, it was also kinda cute."
    "Still... She's got a point. How will things play out?"
    "And why do I now have a bad feeling about this?"
    "..."
    "I'm overthinking things."
    "I shake my head violently, forcing the thoughts out."
    "It'll be fine. A weekend with Yuri in the mountains..."
    "It sounds like a dream come true."
    "I get back to packing the rest of my bags."
    scene bg bus
    with dissolve_scene_full
    play music t6
    "The drive up was... Normal."
    "More normal than I had anticipated. I was sure that something was going to happen, but nothing."
    "Since this was technically a club activity, Monika was able to, somehow, get the school to send a bus for us."
    show yuri 1bb at t11 zorder 2
    y "Hey, [player]?"
    mc "Yeah?"
    y 1bf "D-Did you want to keep reading?"
    mc "O-Oh yeah. Sorry."
    show yuri 1bi at t11 zorder 2
    "Yuri and I had been reading our book on most of the drive."
    "It wasn't a long drive, but it was the perfect excuse to catch up on reading."
    "A part of me still dreamed of the idea."
    "Yuri and I, alone, all cozy by a fire."
    "Just the two of us sitting, reading, and drinking tea."
    "Now that would be a good way to close out the year."
    show yuri at thide zorder 1
    hide yuri
    show monika 3bb at t11 zorder 2
    m "Okay everyone! We're almost there!"
    m "Make sure you have everything, because this bus isn't coming back for at least two days."
    show monika 3bb at t21 zorder 2
    show sayori 4br at t22 zorder 2
    s "Okay!~ Thanks again Mr. Bus-Driver!"
    show sayori at thide zorder 1
    show monika 3bb at thide zorder 1
    hide sayori
    hide monika
    "The driver simply nodded at us from his seat."
    "I can tell he's tired."
    show natsuki 1bb at f21 zorder 3
    n "Hey Monika, are there any rules that we should know about?"
    show natsuki at t21 zorder 2
    show monika 2ba at f22 zorder 3
    m "Well... Nothing too important. Just be respectful, don't make a mess..."
    m 4bk "And have fun, I guess. Ahaha~"
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    hide monika
    hide natsuki
    show yuri 3bv at t11 zorder 2
    y "I-It's almost time..."
    y 3bv "I-I'm still a little uneasy..."
    mc "I know what you mean. But it won't be that bad."
    y 2bt "H-How can y-you be so sure?"
    mc  "If anything, we can just go to the room and read. Who's going to stop us?"
    y 2bw "I-I... I guess..."
    show yuri at thide zorder 1
    hide yuri
    scene bg hotel_outside
    with wipeleft_scene
    "We were now outside the hotel. Despite it's public nature, it's surprisingly quiet."
    "Anyone we see wandering around looked much older than us, but just keeping to themselves."
    show natsuki 4be at t41 zorder 2
    n "THIS is the place? Ugh. It's just old people everywhere!"
    show sayori 2bq at t42 zorder 2
    s "Ehehe~ It's not THAT bad. Everyone looks so nice!"
    show monika 2bk at t43 zorder 2
    m "Well, I'm glad you like it, Sayori."
    m 1bj "Alright! Here's my plan: For today, we can all just take it easy!"
    show natsuki at f41 zorder 3
    n 3bz "Sweet!"
    show natsuki at t41 zorder 2
    show yuri 3bm at t44 zorder 2
    y "Thank goodness..."
    m 3bl "Tomorrow, the day is pretty stacked, so don't make too many plans. Aha~"
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide monika
    hide natsuki
    hide yuri
    "Some free time for the rest of the day..."
    "This was the perfect chance for Yuri and I to spend some time alone."
    scene bg hotel_room
    with wipeleft_scene
    "Monika checked us all in and showed us to our room."
    "It was small, which meant the girls would have to share the beds, but it was nice."
    show sayori 1bo at t41 zorder 2
    s "Hey... Why are there only two beds?"
    show monika 1bd at t42 zorder 2
    m "Actually, it's customary for hotels to only have two full sized beds. But, I'm sure the couch unfolds into a bed."
    mc "Say no more, I'll take the couch bed."
    show yuri 3bo at t43 zorder 2
    stop music fadeout 1.0
    y "A-Actually... U-Umm..."
    show natsuki 1bb at t44 zorder 2
    n "Huh? What's up Yuri?"
    show yuri at f43 zorder 3
    y 4bc "I-I... I-I-I a-actually have a hard t-time sleeping in a bed... A-As in not MY bed..."
    y 4bb "A-And I-I think t-that [player] would help..."
    show yuri at t43 zorder 2
    show sayori 1be at t41 zorder 2
    show natsuki 4bp at t44 zorder 2 
    show monika 1bh at t42 zorder 2
    play music t7
    "We all stared at her in shock."
    "Yuri was tumbling over her own words more than ever, and yet the things she was saying..."
    show monika at f42 zorder 3
    m 1bh "Look. Yuri. We know you and [player] are close, but that is extremely inappropriate." 
    m "We're still on a school trip."
    show monika at t42 zorder 2
    show yuri at f43 zorder 3
    y 3bv "I-I know that... It's just..."
    show yuri at t43 zorder 2
    "Sayori jumped in to save the day. But even her suggestion..."
    show sayori at f41 zorder 3
    s 1bj "I'll take the couch! That way, Natsuki and Monika have one bed, and Yuri and [player] have the other!"
    "We were all dumbfounded by Sayori's suggestion."
    stop music fadeout 2.0
    show sayori at t41 zorder 2
    show monika at f42 zorder 3
    m 2bf "Sayori, I-"
    show monika at t42 zorder 2
    show sayori at f41 zorder 3
    s 1bi "No, seriously. I insist."
    show sayori at t41 zorder 2
    show natsuki at f44 zorder 3
    n 4bq "Dude, but-"
    show natsuki at t44 zorder 2
    show sayori at f41 zorder 3
    s 4bp "I-If you guys say no, then... I-I'll never forgive you!"
    show sayori at t41 zorder 2
    "The room filled with an uneasy silence. We stood dumbfounded."
    show monika at f42 zorder 3
    m 4br "Alright, fine. You win."
    show monika at t42 zorder 2
    show sayori at f41 zorder 3
    s 1bl "Good. Now, let's get to relaxing."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show yuri at thide zorder 1 
    show natsuki at thide zorder 1
    hide sayori
    hide monika
    hide yuri
    hide natsuki
    "With little to no choice, we finally let Sayori take the couch."
    "Natsuki simply shrugged, and everyone finally began unpacking their stuff on the beds."
    show yuri 1ba at t11 zorder 2
    mc "Hey Yuri? Did you want to go looking around after we're done unpacking?"
    "Yuri was thinking about my offer, before quietly responding."
    y 3bq "As long as we have the chance to read today, I-I'm fine with that..."
    mc "Sure, sounds good."
    "Perhaps with how stressed she seemed, a little exploration alone time might help a bit."
    "Unpacking my bag, I took a seat, and relaxed for a little while."
    show yuri at thide zorder 1
    scene bg frozen_lake
    with wipeleft_scene
    play music t6
    "After Yuri and I finished unpacking, we left the room to go explore the hotel a bit."
    "Natsuki and Sayori were interested in coming with us, but Monika intercepted them."
    "We simply shrugged and thanked Monika, leaving to go look around."
    "All of the snowy nature was a nice change of pace compared to the school."
    show yuri 2bd at t11 zorder 2
    y "Wow...!"
    "Yuri let out an astonished noise, and I quickly followed suit."
    mc "This... Is beautiful..."
    "The lake near the hotel was covered in a thick layer of ice. Next to it was a sign posted by the hotel staff."
    mc "\'Ice thick enough for skating. Please use caution and have fun!\'"
    mc "Huh..."
    show yuri 4ba at t11 zorder 2
    "I could see Yuri fidgeting, she clearly wanted to say something."
    mc "What's up Yuri?"
    y 4bb "U-Um... D-Do you think..."
    y 4bc "W-We could... G-Go skating?"
    "Yuri was being incredibly cute. I just about melted from her shy request."
    mc "I-I'd love to. We can go later, if you'd like."
    y 3bd "Yay!~"
    show yuri at thide zorder 1
    hide yuri
    scene bg hotel_room
    with wipeleft_scene
    "Yuri and I returned to the room after our discovery."
    "We sat and read for a few hours, waiting around as we were excited to go out and skate."
    "We had silently agreed that sunset would be the perfect time to go skating."
    "The more I thought about it, the more I was convinced: This was definitely another date."
    show yuri 1bb at t11 zorder 2
    y "Are you ready, [player]?"
    mc "Yup! Let's do this."
    y 3bd "Ehehe~ I'm so excited!"
    scene bg frozen_lake_night
    with wipeleft_scene
    "After renting out some ice skates from the hotel, Yuri and I made our way to the frozen lake."
    "Skates in hand, we were ready for our quiet skating date."
    "I was silently hoping that my walk with Yuri would calm my own nerves though."
    "Not for our date, I had that in the bag. I was hoping that Yuri wouldn't learn my secret..."
    show yuri 2bd at t11 zorder 2
    y "[player]! Let's get started!"
    "I love seeing Yuri so comfortable."
    "I'm glad her and I got to the point where we can be like this. It's like bliss."
    show yuri at thide zorder 1
    "Yuri skated away, leaving me to catch up."
    mc "Coming!"
    "I laced up my skates, and started making my way to the ice."
    "It was a bit awkward to walk, but I was managing."
    "I just had to keep this up once I reached the lake."
    mc "Whoa!"
    "In no time flat, I tripped up and fell, making a fool out of myself."
    "Yuri came rushing over to me."
    show yuri 3bp at t11 zorder 2
    y "[player]!? A-Are you okay?"
    mc "I'm fine... Yuri, I... I've never..."
    "I was stumbling over my own words, trying to explain myself to Yuri."
    "I think my secret had let itself out."
    y 1de "Ehehe~"
    mc "Y-Yuri?"
    y 2bj "I-I didn't mean to laugh, but..."
    y 2bb "Have you never gone skating before?"
    mc "..."
    mc "So, you found me out... I'm sorry, Yuri..."
    y 3bp "D-Don't apologize! I-I'm not upset..."
    show yuri 3bn at t11 zorder 2
    "Yuri looked down at me, her eyes softening. My heart was melting just looking at her."
    y 2bs "I... I-I wouldn't mind... T-Teaching you how..."
    "My heartrate shot straight up. Learning how to skate? Taught by Yuri?"
    "Perfection."
    mc "I-I would love that! P-Please teach me!"
    y 3bc "Ehehe~ Then, let's get started!"
    show yuri at thide zorder 1
    hide yuri
    stop music fadeout 2.0
    scene bg frozen_lake_night
    with wipeleft_scene
    "Yuri led me through trying to keep my balance, teaching me how to skate."
    "It was bliss."
    "What's better than having your girlfriend teaching you how to ice-skate?"
    "She seemed to be really getting into it too, just like with bowling."
    "For someone who doesn't see herself as the athletic type, she knew quite a bit, and looked like a natural."
    "Not to mention a great teacher too."
    "As Yuri was continuing teaching a lesson on walking, I suddenly heard a familiar voice behind us."
    $ m_name = "Voice"
    m "Hey guys!"
    "Huh?"
    $ m_name = "Monika"
    show monika 4bk at t42 zorder 2
    play music t6
    m "Yuri! [player]! What's up?"
    show yuri 2bp at t41 zorder 2
    y "E-Eh? M-Monika? What are you doing here?"
    "Monika glided across the ice towards us. She had her own pair of skates, and a suspcious look in her eye."
    show monika at f42 zorder 3
    m 2bb "Oh, nothing. It's just that we found this frozen lake, and thought we'd go skate for a bit as well! Ahaha~."
    "As much as I think it wasn't coincidence, I shouldn't be too surprised, to be honest."
    "Monika was the one that did mention ice-skating, and this place is right next to the hotel..."
    "I suppose I was a bit too lost in thought thinking we could be alone."
    show monika 2bb at t42 zorder 2
    show sayori 4br at t43 zorder 2
    s "Hi [player]~!"
    show natsuki 4bz at t44 zorder 2
    n "Alright! Let's get this party started!"
    show yuri at f41 zorder 3
    y 3bo "Sayori and Natsuki are here too?"
    show yuri at t41 zorder 2
    mc "Yeah. Yuri and I, we were just ah, getting some alone time, and..."
    show monika 2bb at f42 zorder 3
    m 3bg "[player], that almost sounds like you want us gone? But that couldn't be right."
    m "We're here for a school trip, right?"
    m 2bk "I believe as club president, we should spend as much time as possible together!"
    m "You know, to help strengthen the bonds of the club!"
    mc "That's not what-"
    show monika at t42 zorder 2
    show yuri at f41 zorder 3
    y 1bh "I-It's fine, [player]..."
    "I could see a look of both frustration and sadness crawling around her face."
    "But, I could also tell that she is trying to endure her anxieties at the sudden change."
    "I just nodded to her, putting my hand on her shoulder."
    show yuri at t41 zorder 2
    show sayori at f43 zorder 3
    s 1bx "Yay! Come on [player], let's skate!"
    "Sayori quickly went on the ice, before slipping almost immediately."
    show sayori at t43 zorder 2
    s 4bp "Whoa!"
    show natsuki at f44 zorder 3
    n 1bp "You okay, Sayori?"
    show natsuki at t44 zorder 2
    show sayori at f43 zorder 3
    s 2bl "Yeah... I just got so excited, I forgot I've never gone ice-skating before! Ehehe~!"
    show sayori at t43 zorder 2
    show natsuki at f44 zorder 3
    n 4br "H-How could you forget something like that!?"
    show natsuki at t44 zorder 2
    show monika at f42 zorder 3
    m 3bb "Say, Yuri. Weren't you just showing [player] how to skate? Maybe you could help Sayori!"
    show monika 3bb at t42 zorder 2
    show yuri at f41 zorder 3
    y 3bp "U-Um, but...!"
    "I know what she's about to say: What about helping [player]?"
    show yuri at t41 zorder 2
    show sayori at f43 zorder 3
    s 4bj "I-It's okay, Monika! I can figure it out!"
    show sayori at t43 zorder 2
    show monika 3bb at f42 zorder 3
    m 1br "Hmm... But knowing you Sayori, You'd probably need more than one person..."
    "Monika feigned deep thought, popping up an idea after a litte bit."
    m 3bk "Okay! Natsuki and Yuri will help Sayori, and I'll help [player]~!"
    show monika at t42 zorder 2
    show yuri at f41 zorder 3
    y 2bn "B-But-!"
    show yuri at t41 zorder 2
    show natsuki at f44 zorder 3
    n 4bz "It'll be okay Yuri, we've got this!"
    show natsuki at t44 zorder 2
    show yuri at f41 zorder 3
    y 3bv "T-That's not the-!"
    show yuri at t41 zorder 2
    show sayori at hf43 zorder 3
    s 4br "Yay! Let's start now!"
    show sayori at t43 zorder 3
    show sayori at lhide zorder 1
    show yuri at lhide zorder 1
    show natsuki at lhide zorder 1
    hide sayori
    hide yuri
    hide natsuki
    show monika at t11 zorder 2
    "Just like that, the other three left, leaving me with Monika."
    "I kind of had a feeling of what she was doing, but I couldn't and didn't want to say anything out loud."
    "Its just another roadblock. Its better just to try and enjoy our time here."
    m 4bb "Okay, [player]! Let's get to work~!"
    "Monika and I skated slowly for a little while."
    "She actually was trying to help me, and it was kinda fun."
    "But even though I didn't want to think it, I could sense a darker intention to her burst of sudden kindness..."
    stop music fadeout 3.0
    m 3bj "I really enjoy skating with you, [player]... It's almost like we're on a date~..."
    "Oh no..."
    mc "...Y-Yeah. Hmm. Funny that."
    show monika at thide zorder 1
    hide monika
    "I was trying to get the point across, but failed. She just put on her trademarked Monika smile."
    show yuri 3bv at t31 zorder 2
    show sayori 4bq at t32 zorder 2
    show natsuki 3bl at t33 zorder 2
    "I looked over at the others as we skated around."
    "Sayori was trying her best to learn, almost tripping over herself. Natsuki seemed like she was enjoying teaching, while Yuri would shoot glances my way."
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show sayori at thide zorder 1
    hide natsuki
    hide yuri
    hide sayori
    play music t10
    show monika 1be at t11 zorder 2
    "Suddenly, I felt a finger rest under my chin, pulling my gaze back to Monika."
    m "[player]. There's something I need to tell you."
    m "It actually works out very well that we're alone for a moment."
    mc "Y-You don't say? What's up...?"
    "Monika had a look of nervousness swim across her face, before trying to pull herself together."
    m 1bl "It's... Well, I guess I really like you, [player]..."
    mc "..."
    m 2be "Ever since you joined the literature club, I've always liked you..."
    m "I've really wanted to tell you sooner, but never had the perfect moment..."
    m 2be "Until now."
    "Monika leaned in close, putting her voice down to a whisper."
    m 1be "[player]... Will you go out with me?"
    show monika at thide zorder 1
    hide monika
    "I was in shock at Monika's sudden confession."
    "This is what she's been planning?"
    "I should have known by what she's been doing..."
    "Monika was bold, but this... This was something else."
    "I was about to respond to her, until I saw a sight that made my heart drop..."
    show yuri 3bp at t11 zorder 2
    y "...!"
    y 4bc "..."
    show yuri at lhide zorder 2
    hide yuri
    "Upon seeing us, Yuri was now off the ice, quickly running off."
    "I looked at Sayori and Natsuki, seeing them looking worried."
    "This couldn't have been happening."
    "I turn to her and shook my head."
    show monika 1bg at t11 zorder 2
    mc "A-Absolutely not! I'm going out with Yuri!"
    show monika 1bo at t11 zorder 2
    "Monika looked crushed. I didn't even give her a chance to respond before continuing."
    mc "And thanks to this stunt you just pulled, that might not be for long!"
    stop music fadeout 3.0
    m 1bg "[player]! Wait!"
    show monika at thide zorder 1
    hide monika
    scene black
    with dissolve_scene_full
    "I didn't listen. I rushed off the ice, ripped off my skates and ran to the hotel."
    "People gave me worried looks as I ran through the halls, but I didn't care."
    "I knew what Yuri must have been thinking, seeing the two of us..."
    "And I had a deep, dark feeling I knew what she was about to do..."
    scene bg hotel_room
    with wipeleft_scene
    play sound "sfx/closet-open.ogg"
    "I burst the door open, frantically looking around."
    mc "YURI!?"
    "There was a small trail of clothes and things on the floor from a knocked over suitcase, leading to the bathroom." 
    "The door was closed, and the light underneath was on."
    "I tried to open it, but it was locked."
    mc "Yuri!? Yuri, open the door! Let me talk to you!"
    "..."
    "No response. But I knew she was in there."
    mc "Yuri, if you don't open the door, I-I'll have to break it down!"
    "Unsure, but knowing I had to do something, I stepped back, readying my shoulder."
    "As I was ready to charge in, I heard Yuri speak."
    y "W-Wait! I-I... I'm opening the door..."
    "After a short while, Yuri turned the lock and pushed the door open..."
    play music t10
    show yuri 4bd at t11 zorder 2
    "She was okay. But I did see what was in her hand..."
    "A pocket knife, more than likely one she brought with her."
    y "I-I'm sorry, but... I-I just saw y-you and M-Monika a-and assumed the w-worst..."
    y 4bc "P-Please don't hate me..."
    "I didn't let her say anymore. I put her hand with the knife down toward the sink counter, and hugged her."
    "The clang of the handle hitting the surface of the counter rang out as she let go of it."
    mc "I will never hate you. And I would never pick Monika over you..."
    y 3bw "[player]... I-I..."
    "Yuri hugged me back, tightly wrapping her hand around me."
    y 3bm "T-Thank you, [player]... I-I love you..."
    mc "I love you too, Yuri. Now, and forever."
    scene black
    with dissolve_scene_full
    "Yuri and I tidied up the room and everything we had in the bathroom, including the knife, and laid in bed."
    "I held her against me as she gently went to sleep, tightly holding my arms."
    "I heard the others come in, but I didn't move."
    "I didn't want to discuss anything right now."
    "I heard them muttering to each other about something, then they all went to sleep."
    "I knew that this wasn't over. I knew Monika and I would talk tomorrow..."
    "But, at least for now. This was good. I was at peace."
    "And I could tell Yuri was as well."
    stop music fadeout 2.0
    scene bg hotel_room
    with dissolve_scene_full
    "When morning broke, I sat up slowly in bed."
    "The thoughts of last night's... Events... played through my head."
    "Despite everything that happened, how terrible it all went down, I couldn't really feel angry."
    "Just more... Tired, if I had to think about it."    
    "We were all still a club, friends."
    "And a part of me couldn't bear just ending that here like this."
    "But, it wasn't something to just push away either."
    "I knew when I saw Monika, we had some things to talk about."
    "I pushed the covers off and slowly pulled myself away from the warm mattress."
    "Yuri was still asleep, but I decided to let her be for now."
    "If she wanted to talk with Monika about what happened last night, I'll let her decide when."
    "As I heard my stomach start to rumble, I got dressed, and headed out."
    scene bg hotel_lobby
    with wipeleft_scene
    play music t6
    "I walked into the hotel lobby, scoping out the dining area."
    show natsuki 1bs at t11 zorder 2
    "There, I saw Natsuki sitting at a table, having some breakfast."
    "She looked exhausted as I walked up and got a better look at her."
    "Seems like she didn't sleep well..."
    n 2bg "Hey, [player]... How's Yuri?"
    mc "Hey, Natsuki. She's doing well. She's still asleep after everything that happened."
    n 1bq "That's good..."
    show natsuki at thide zorder 1
    hide natsuki
    "As I was about to sit and eat, I heard the clicking of shoes behind me."
    show monika 1bi at t11 zorder 2
    stop music fadeout 2.0
    m "[player], Can... Can we talk?"
    mc "..."
    "I motioned to one of the seats at the table."
    show monika 1bo at t11 zorder 2
    "Monika looked at me sadly as she sat down. I could tell she was upset..."
    play music t9
    m 2bf "W-Well... I just wanted to apologize."
    mc "...Really?"
    m 1bg "Of course."
    m 1bf "I never intended to hurt Yuri or you. Though, knowing what I wanted to say, I should have known it would..."
    m 1bo "To be honest, I was jealous, seeing you with Yuri, all this time..."
    m "I didn't really think much of it. I kept myself in check."
    m 1bf "But I let my emotions get the better of me the other day." 
    m "And then, this whole thing happened."
    m 1bl "Now I can see that my ah, \"plan\"... Didn't go so well."
    m 1br "Well, there's no way to change that."
    m 1bi "I dug this grave. Now I have to lay in it."
    mc "... Heheh..."
    m 1bd "Hm?"
    mc "S-Sorry. Just... That was poetic."
    mc "I thought it was fitting for the literature club president to apologize with such a dramatic line."
    m 1bl "Haha... I guess so."
    mc "I appreciate the apology, Monika. And as crazy as it was, I forgive you."
    mc "It's been a crazy time with everything, you, Yuri, Natsuki, Sayori."
    mc "And I still see us as friends."
    m 1bd "I..."
    m 1be "Thank you, [player].
    mc "But, I'm not the only one to apologize to."
    m 1bi "I know. I'm going to go up in a little bit."
    m "Give her some time, and mentally prepare myself as well."
    m "I don't think she'd want to see me yet. But I have to explain myself, or at the very least, apologize to her."
    mc "Thank you."
    show monika at thide zorder 1
    hide monika
    "It was nice seeing Monika the way she was. It seemed everything was going well..."
    stop music fadeout 2.0
    mc "Hey... Where's Sayori?"
    show natsuki 5bs at t11 zorder 2
    n "O-Oh... Right."
    mc "Huh?"
    n 5bm "W-Well... After you and Yuri left, Sayori, Monika and I talked."
    n 42bb "After she found out about what Monika was planning, she got really down."
    n "It really hit her depression hard. I felt really bad..."
    n 2bh "I asked if she wanted breakfast, but she said she wasn't hungry."
    mc "Hmm... That doesn't sound good."
    mc "I'll be right back then. I'll go see how she's doing up there."
    n 1bg "We'll probably try to come up in a little bit then."
    mc "For sure."
    show natsuki at thide zorder 1
    hide natsuki
    scene bg hotel_room
    with wipeleft_scene
    "I made my way back up to the room and thought about it all."
    "This whole incident definitely rocked worlds, beyond Yuri and I."
    "To think Sayori was this worried enough, it made me a bit worried about her."
    "As I approached the door, I could hear Sayori and Yuri's voices from the other side."
    "It seems that they were both awake now."
    "Knocking a couple times, I gently open the door to see Sayori and Yuri sitting on the bed, talking."
    play music t9
    show yuri 1bf at t21 zorder 2
    show sayori 1bb at t22 zorder 2
    y "Oh, good morning, [player]."
    s "Morning."
    mc "Good morning to you two as well."
    mc "I uh... Didn't see you two downstairs for breakfast and figured you were all back here."
    mc "I just wanted to see if you two were alright."
    mc "Is everything okay?"
    show yuri 1bv at t21 zorder 2
    show sayori 1bk at t22 zorder 2
    "After that statement, the slight reluctance in their responses made me worried."
    "I knew how strong Sayori could be. But I can knew there was more written on the walls, so to speak."
    show sayori 1bd at t22 zorder 2
    "But as they looked at one another, Sayori took a deep breath."
    show sayori at f22 zorder 3
    s "Yeah, we're okay."
    s 1bk "We just talked about what happened yesterday, and well... Everything about it."
    mc "Oh... I see."
    show sayori at t22 zorder 2
    show yuri 1bv at t21 zorder 2
    "I looked toward Yuri, and could see the slight pain within her face as well, a sight not all that alien to what I had seen before."
    "But as if they acknowledged their presence together, Yuri and Sayori's faces calmed."
    show sayori at f22 zorder 3
    s "I had no idea about Monika's plan, but after she explained it..."
    s "I didn't know what to feel anymore..."
    s "But what made it worse was this was almost like how I had felt when you and Yuri started getting close."
    "The statement hit me like a bag of bricks."
    "I suppose I was denying it to myself that it wasn't happening, but to hear her..."
    s 1bg "We've known each other for so long... And Yuri has been great too."
    s "I can't lie and think to be a little... Well..."
    s "But you were both my friends. I wanted to support you both."
    s "That's why I traded out the couch with you."
    s "And then when Monika went and did all that... "
    s 1bf "My body just shut down, and it all just... Came tumbling down."
    s "It was just like what happened, that I would have to stay on the sidelines like this again."
    s "But I think what scared me the most was losing the both of you because of it."
    s "I love the both of you, the friendship that we all shared, and to lose that..."
    s 1bu "I couldn't bear it."
    mc "Sayori..."
    s 1bd "But, after discussing it with Yuri, to lay it all down like this, it made me feel a lot better."
    s "What you told her, and what she told me..."
    s "I'm glad I was able to tell her this."
    s "I'm happy for the both of you, that you two got so close."
    s 1bj "[player], you treat her right, okay?"
    show sayori 1bq at t22 zorder 2
    show yuri at f21 zorder 3
    y 3bp "E-Eh?!"
    show yuri 3bo at t21 zorder 2
    show sayori at f22 zorder 3
    show sayori at t22 zorder 2
    s 1bj "If we stop being friends, I'll never forgive you!"
    "I could barely crack a smile through the tightness of my chest."
    "But as the thought of getting a lecture from Sayori of all people about this came to me, I chuckled and smiled."
    mc "Of course."
    show sayori 1bt at t22 zorder 2
    "As I looked into Sayori's eyes, I can tell there was still a sense of uneasiness behind them still."
    "But she's definitely grown from the childhood friend I knew her as."
    "As the three of us conversed, the door opened up again."
    show yuri at t31 zorder 2
    show sayori 1bn at t32 zorder 2
    show monika 1bf at t33 zorder 2
    "Monika stood at the doorway, staring on in silence at us."
    "Her expression was filled with melancholy and regret."
    y 3bn "Monika...?"
    show monika at f33 zorder 3
    m 1bg "I... I wanted to come up and apologize to you, for what I did yesterday."
    m "After speaking with [player] downstairs, I wanted to come speak to you directly myself."
    m 1bp "Then I heard the three of you talking as soon as I got close, and I didn't want to interrupt."
    m "But when I heard everything, that even you were hurt by what I did Sayori, harboring those feelings toward this whole situation like this..."
    m 1bg "I'm truly sorry that I made both of you uncomfortable or hurt you out of my own jealousy."
    m "Whether that was directly, or you caught in the crossfire of it all."
    show monika 1bf at t33 zorder 2
    show sayori 1bu at f32 zorder 3
    s "Monika..."
    show sayori at t32 zorder 2
    show monika 1bp at f33 zorder 3
    m "There's no excuse for the spike that I drove in between all of us like this."
    m "Especially between you and Yuri, [player]."
    m "I let my emotions get the better of me, and didn't realize that I was hurting the club, my friends, in the process..."
    show monika 1br at f33 zorder 3
    "She stopped, seeming to hold back tears as she spoke."
    m 1bg "I hope that you can all forgive me for my selfish stupidity."
    "After a short uneasy silence, Sayori stood up, and walked over to Monika, giving her a hug."
    show monika at t33 zorder 2
    show sayori at f32 zorder 3
    s 1bd "It's okay, Monika. I forgive you."
    s "I can't really stay mad at someone for so long, especially when they apologize."
    show sayori at t32 zorder 2
    show yuri at f31 zorder 3
    "As she follows, Yuri stands up as well."
    y 3bv "Monika, I know we've had our differences and clashed at times, but I forgive you as well."
    y 3bs "To see us all divided... I would hate for us to keep it like this forever."
    show yuri at t31 zorder 2
    show monika at f33 zorder 3
    m "Yuri, Sayori..."
    m "Thank you, to the both of you."
    m 1bj "I'll uphold it as much as I can, as both your president and your friend."
    show monika 1ba at t33 zorder 2
    show sayori at f32 zorder 3
    show yuri at t31 zorder 2
    s 1br "So long as we're all together as friends like this, we'll get through it!"
    show sayori at t32 zorder 2
    "Suddenly, Sayori roped us together for one big group hug, all of us chuckling along."
    show sayori at t42 zorder 2
    show yuri 1bc at t41 zorder 2
    show monika at t43 zorder 2
    show natsuki 3bl at t44 zorder 2
    "As we hugged, Natsuki appeared in the room, holding a plate of different foods and desserts from the breakfast table."
    n "Hey you four! The breakfast was going to close soon, but I managed to get us some food if you were-"
    n 1bh "...Uhh, is everything okay in here?"
    show sayori at f42 zorder 3
    s "Come on, Natsuki! You get in here too!"
    show sayori at t42 zorder 2
    show natsuki at f44 zorder 3
    n 1bv "Wait! Sayori! AHH...!"
    "Sayori plunged Natsuki into the group, all three of us surrounding her now in this little tight group." 
    "As she wriggled her way out without losing any of the food, we all laughed together."
    show natsuki at t44 zorder 2 
    show monika at t43 zorder 3
    m 3ba "Well, we still have a full day of activities ahead of ourselves. Let's get to it, shall we?"
    $ y_name = "Nat and Say"
    y "Yeah!"
    $ y_name = "Yuri"
    scene black
    with dissolve_scene_full
    "After it all, we all got ready for the day, based on this new found energy between all of us."
    "It made me happy to see us all like this, especially Yuri."
    "By the looks on her face, she seemed to be happy with everyone as well."
    "There was no better feeling than that to carry on with the rest of our trip."
    stop music fadeout 2.0

#Scene 6
    scene bg bedroom
    with dissolve_scene_full
    play music t12
    "Man, it's finally the last week of school. I feel so relaxed."
    "I can't believe it's already the end of the school year."
    "And it's the end of mandatory schooling for me in general."
    "Sure, I may have only survived this year because of Yuri's assistance, but that's not the point."
    "Now there's only this last week left and I've already done all the big projects."
    "Hopefully that means I can just chill for the rest of the time."
    stop music fadeout 2.0
    scene bg residential_day
    with wipeleft_scene
    play music t2
    "I get outside my house and walk the usual route to school."
    "Just as I went along, I hear Sayori come up behind me."
    show sayori 1a at t11 zorder 2
    s "Hey [player], are you as ready as I am?"
    mc "Ready for what?"
    s 4s "The last week of school!"
    mc "Oh, yeah. I'm pumped."
    s 2c "You don't sound very pumped. Is there anything wrong?"
    mc "What? No. It's just that I don't want the teachers to throw an assignment at us out of nowhere."
    mc "The fact that this is the last week is what's gonna let me survive."
    s 3s "C'mon, it won't be that bad. I mean, the club will still be available after."
    "At least she's right there."
    "That'll be my saving grace."
    "Wait a minute, available after school, does she mean...?"
    show sayori 1b at t11 zorder 2
    mc "Sayori, do you mean the club will be up after the school day or after the school year?"
    s "I meant after the school day."
    "It just occurred to me. With school ending, will this be the last week of the literature club as well?"
    mc "Hey Sayori, as vice president of the literature club, do you have plans after the school year?"
    s "No, we'll just continue what we're doing now next yea-"
    s 4o "Wait a minute."
    s "..."
    s 4m "If this is the year we graduate, then..."
    s "Oh no! This might be the end of the literature club!"
    s "I have to go talk to Monika about this!"
    s "Bye [player], see you later at the club after school!"
    s 4p "And I mean after the school day!"
    show sayori at thide zorder 1
    hide sayori
    mc "Wait, Sayori!"
    "And like that, she's gone."
    "How does she run so fast?"
    "Well, now I'm left with what to wonder will happen today."
    "Hopefully it won't be as bad as I think it will be."
    stop music fadeout 2.0
    scene bg class_day
    with wipeleft_scene
    play music t6
    "Class today is more chill than normal, which is fine by me."
    "Luckily, there's been no headache inducing test or sleep killing assignments."
    "We were just reading student suggested books today."
    $n_name = "Teacher"
    n "Okay class, what did you think of this week's book?"
    "I look around the students with a collective shrug, all except Yuri."
    "She seemed to be forming her thoughts to completely justify the book."
    n "Hello, would anyone like to give their opinion?"
    show yuri 1f at t11 zorder 2
    y "Yes, well, I find the book to completely lose its tone with its climax, or anticlimax I should say."
    y "The author spends the whole story on its corrupt world and the consequences of such. We meet characters that we treasure as the reader that are taken away in this unjust world."
    y 2h "Yet its ending fails to meet the expectation of the atmosphere, feeling forced compared to the skillful hinting throughout the book."
    "Yuri keeps on with her explanation, going into the metaphors, author's purpose, and other literary analysis."
    "The class pays attention to Yuri, wondering how she doesn't get tired of such a large book in their eyes."
    "Little do they know, this is nothing for her."
    "Yuri concludes with her statement and leaves the class awestruck."
    n "Wow Yuri, you really went into this book. I'm impressed."
    n "Now, who would like to suggest a book or passage for the class to read? This would be the last story of the year."
    "I look over to Yuri, who was holding the Portrait of Markov."
    "Now that I think about it, the class hasn't read that book yet."
    "She attempts to present the book, but still couldn't approach the teacher with courage."
    y 3o "..."
    "Do I go and help Yuri?"
    "The class would be pretty bummed to read such a large book, but the story is so well-written."
    "..."
    show yuri 3p at t11 zorder 2
    mc "...I have a suggestion."
    mc "How about we read Portrait of Markov?"
    "I grab the book out of my bag and hold it up for everyone to see."
    n "Hmm, and what is that?"
    mc "Well... Ah, it's a story that follows this teenage girl that has a long lost sister who moves in with her."
    mc "And well... Maybe we can leave the rest of the book a surprise."
    n "Are there any objections to this?"
    show yuri at thide zorder 1
    hide yuri
    "There was no sound made, the only echo was of silence."
    "Maybe the others are actually interested?"
    "{i}Or shocked about the pure size of the book...{/i}"
    "The bell rings and I'm left with Yuri walking to our next class."
    "Before Yuri wanders out of the room, she smiles at me."
    show yuri 1s at t11 zorder 2
    y "Thank you."
    show yuri at thide zorder 1
    hide yuri
    $n_name = "Natsuki"
    "That smile is something I never want to lose."
    "Even if it meant having the class wanting to stab me, it was totally worth it."
    stop music fadeout 2.0
    show bg corridor
    with wipeleft_scene
    play music t5
    "The rest of the school day today had been manageable."
    "I can't remember the last time it was like that."
    "And with the club coming up, I'm looking forward to a good conclusion."
    "As I hear footsteps going up the stairs, I turn around to see the figure."
    show yuri 1a at t11 zorder 2
    y "Hello, [player]."
    mc "Hi Yuri. How has your day been going?"
    y 1b "It's been going well. I find this last week to be calming for everyone here."
    mc "Good to hear. Are you ready for the club today?"
    y 2c "Of course."
    mc "Alright."
    "Yuri and I walk to the clubroom."
    "We're both in such a great mood, I doubt there's anything that can stop it."
    "I grasp on the handle and open the door, but doing so, I feel an ominous pressure that engulfs me."
    "This can't be good."
    show yuri at thide zorder 1
    hide yuri
    scene bg club_day
    with wipeleft_scene
    show sayori 4h at t21 zorder 2
    show monika 1o at t22 zorder 2
    "I enter the club room to see Sayori and Monika discussing about something."
    "They seem rather distressed about it."
    s "What are we gonna do Monika? I can't think of a way to keep this."
    m "Calm down Sayori. We don't want the others to panic over it."
    m 1p "Just give me some time. I'll figure something out."
    show sayori at thide zorder 1
    hide sayori
    show monika at thide zorder 1
    hide monika
    "Monika and Sayori seem to be discussing something important."
    "Best to stay out of it just to make it worse."
    show natsuki 2s at t11 zorder 2
    "I see Natsuki at one end of the club room."
    "She looks like she's stressed out about something too."
    "Maybe she needs to talk about said thing."
    show natsuki 5i at t11 zorder 2
    n "..."
    n 5h "...What are you looking at?"
    "Or maybe not."
    "What's up with everyone today? Did anything serious go wrong before we got here?"
    show natsuki at thide zorder 1
    hide natsuki
    show yuri 2t at t11 zorder 2
    y "Hey [player], is anything bothering you? You seem to be puzzled."
    mc "What? Oh, it's nothing."
    mc "The room just feels more intense than usual."
    y 2u "I can understand. There does seem to be a tension lurking about."
    y "How about we just sit down and read a book?"
    mc "That sounds nice right about now."
    show yuri at thide zorder 1
    hide yuri
    "Yuri and I walk to our spot on the ground and she goes to her backpack to retrieve the book we've been reading recently."
    "We get in our usual reading position and try to relax."
    "However, that eerie feeling lingered on."
    "Any hint to what is happening goes through my mind."
    "First, it was Sayori this morning."
    "She ran to talk with Monika, but she was talking with her here in the afternoon instead."
    "Speaking of, what were they talking about?"
    "Whatever it was, Monika tried hard to not let it spread."
    "And then there was Natsuki who's been having a stronger attitude today."
    show yuri 2e at t11 zorder 2
    y "[player]."
    "I mean, Natsuki has always had her temper, but..."
    y 2f "[player]?"
    "Combined with all the weirdness of today, it just doesn't make sense..."
    y 2n "[player]!"
    mc "What?! What happened?!"
    y 2o "Oh i-it's just that..."
    y 2n "You weren't responding to me."
    mc "Ah! Really? I'm sorry."
    y "It's fine, it's just that you've been rather distracted."
    mc "Is it that apparent?"
    y 2o "Y-yes."
    y "..."
    y 1n "Hey [player], are... Are you worried about anything?"
    mc "Well, I just find that everyone is on edge today."
    mc "To be honest, you're the only one acting normal today."
    mc "Everyone else has been acting strangely, myself included I guess."
    y 3o "Perhaps that's the reason for the intense atmosphere of today."
    mc "Hopefully we're just imagining it, I don't want to deal with anything big this week."
    stop music fadeout 2.0
    show yuri at thide zorder 1
    hide yuri
    show monika 3o at t11 zorder 2
    "As we spoke, Monika walked up to the front of the room."
    m "Okay everyone, I have some news to share."
    m "Please pay attention to what I have to say."
    show sayori 1k at t41 zorder 2
    show natsuki 3s at t42 zorder 2
    show monika 3o at f43 zorder 3
    show yuri 1f at t44 zorder 2
    "Monika seems a bit depressed while giving the news."
    "Looks like I'm getting my answer for the mood today."
    m 1p "It is with a heavy heart that this will be the last week of the Literature Club."
    m "There are no plans to continue the club at school since we are the only members, and all of us are graduating."
    m "Any personal items left in the classroom need to be taken back by the owner before the end of the week."
    m 1r "As for us, I don't have any plans to continue this club during college, as I believe not all of us will be looking for a second education."
    show monika 1o at t43 zorder 2
    show natsuki 42b at t42 zorder 2
    show yuri 1g at t44 zorder 2
    "With that bombshell finally hitting, each of us sunk a bit."
    "We all knew the end would come eventually, but none of us anticipated it sucking this much."
    "I then look to Yuri, who unlike the rest of us, had an all-knowing face on her."
    "Not one that brags about their knowledge, but one that is saddened by it."
    "With all of us down, Monika begins to speak again."
    show monika 4e at f43 zorder 3
    m "So with all of this being said, I have one final request."
    show sayori 2n at t41 zorder 2
    show natsuki 3k at t42 zorder 2
    show yuri 2f at t44 zorder 2
    "All of our ears beckons to Monika as she relays her last assignment."
    play music t6
    m 4k "Instead of being all gloomy, we can throw a bit of a party on the last day!"
    m 1a "I can bring some party supplies to make it feel a bit festive."
    show yuri 2w at t44 zorder 2
    "The others start getting their spirits up. This actually sounds like fun."
    show monika 4e at t43 zorder 2
    show sayori 3c at f41 zorder 3
    s "A party? Monika, isn't this a bit too late?"
    s "I mean, I don't think we'll have enough time to look for a DJ."
    show sayori 3c at t41 zorder 2
    show monika 3b at f43 zorder 3
    m "It doesn't have to be a big party, just a celebration to who we have become today."
    show monika 3b at t43 zorder 2
    show sayori 3a at f41 zorder 3
    s "Oh, okay! Can I be the DJ then?"
    show monika 2k at f43 zorder 3
    show sayori 3a at t41 zorder 2
    m "Sure, Sayori."
    show monika 2k at t43 zorder 2
    show sayori 4r at f41 zorder 3
    s "Yay!"
    show natsuki 5y at f42 zorder 2
    n "Heh, with you already sorting things out, I have a feeling you just assumed I would bring cupcakes."
    n "Am I right about that?"
    show natsuki 5y at t42 zorder 2
    show monika 5a at f43 zorder 3
    m "Well, I was going to ask you to, but since you brought it up like that I guess I can ask someone else-"
    show natsuki 1v at f42 zorder 3
    show monika 5a at t43 zorder 2
    n "Wait, I'm joking! I'll bake something for the party!"
    show natsuki 1v at t42 zorder 2
    show monika 1k at t43 zorder 2
    "Monika starts giggling about Natsuki's reaction."
    "Typical Monika doing her typical teasing."
    show sayori 1a at t41 zorder 2
    show natsuki 1a at t42 zorder 2
    show monika 1a at t43 zorder 2
    mc "A party sounds really fun."
    mc "And if Sayori's DJ we'll be safe to know that the school won't be upset about the music."
    show sayori 4j at f41 zorder 3
    s "Hey, do you think I'll just play little kid songs?"
    s 5d "{i}It would just be a few of them...{/i}"
    show sayori 5d at t41 zorder 2
    show natsuki 1z at t42 zorder 2
    show monika 2k at t43 zorder 2
    "Monika, Natsuki, and I laughed a bit from Sayori's retort."
    "Honestly, I'm starting to feel better about the last day."
    "That is, until I turned to Yuri."
    "She's gone from her all knowing expression to a solemn one."
    "I thought she would be more excited about the party, but it seems now she's the only one upset in the clubroom."
    show sayori 1a at t41 zorder 2
    show natsuki 1a at t42 zorder 2
    show monika 4b at f43 zorder 3
    m "I think it's safe to end the day here."
    m "We'll talk more about the party tomorrow."
    show sayori at thide zorder 1
    hide sayori
    show natsuki at thide zorder 1
    hide natsuki
    show monika at thide zorder 1
    hide monika
    show yuri 2h at t11 zorder 2
    "And with that, everyone started getting their stuff from the clubroom."
    "Natsuki asked Sayori if she could help carry her manga for her."
    "Yuri though was still looked somewhat down." 
    "I took the liberty of taking her tea set out of the closet and carrying it for her."
    "After saying goodbye, I leave the classroom in a good mood, with Yuri beside me."
    show yuri thide zorder 1
    hide yuri
    scene bg road
    with wipeleft_scene
    show yuri 1g at t11 zorder 2
    "On the walk home, there isn't much said between us." 
    "Yuri just keeps her demeanor and moves on."
    "I want to ask what's happening."
    "This isn't like other times where she looks like she's worried she doesn't have the answer and wants me to help her."
    "Quite the opposite actually."
    "She has the look that she has things figured out, but she doesn't look happy about it."
    show yuri at thide zorder 1
    hide yuri
    scene bg yuri_house
    with wipeleft
    show yuri 1g at t11 zorder 2
    "Because I was carrying her supplies, we walked to her house first."
    "After being able to set down the box, I decided to find the courage in me to see what the problem is and ask."
    mc "Hey Yuri, do you want to talk for a bit?"
    y 1f "Oh, is everything okay?"
    mc "You just seem more down than usual."
    mc "Since we left the school you haven't uttered a word."
    mc "Is anything bothering you?"
    "In an ironic sense, the roles have reversed about who's worried about who from the beginning of the club today."
    y 1h "Everything's fine."
    y "Things are going as expected..."
    mc "Expected? What do you mean?"
    y 1h "Just with the club. I suppose it all comes to an end..."
    mc "Yeah, I suppose so."
    y "But umm, I should probably get going inside. There's some things I have to take care of."
    mc "Oh, alright then. Well, this is it then."
    mc "Of course, no worries, Yuri."
    mc "I'll see you at school tomorrow."
    mc "Bye, Yuri."
    y "Bye, [player]."
    show yuri at thide zorder 1
    hide yuri
    "After handing her the box, she heads in and shuts the door."
    "I feel a bit of anxiety creeping on my spine though."
    "Despite saying she's fine, there's still a hint of sadness in her eyes."
    "I could barely get anything from our conversation, so I'm out of the loop."
    "The end of the club was a bit of a sad thing, and it seemed to be hitting her a certain way."
    "It's probably that she's worried about the last day, but I think she'll come around when the party happens."
    "After all, it is a day with her friends."
    "...Hopefully."
    stop music fadeout 2.0
    scene bg black
    with fade
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "The second day of the school week starts, and I find myself more pumped than yesterday."
    "For some reason, I can't get the idea of the party out of my head."
    "I know it isn't gonna be anything too big, but something about it just seems exciting."
    "My thoughts linger on until Sayori runs up to me from behind."
    show sayori 4s at t11 zorder 2
    s "{i}Huff{/i}. Ha. Hey [player]. {i}Huff{/i}."
    mc "Hey Sayori. You came out of your house later than usual."
    s "Any reason why?"
    s "Oh. {i}huff{/i}. Sorry about that."
    s 5a "I was up last night deciding what songs to put on the playlist."
    mc "You're really taking this role seriously."
    mc "You know, no one's really expecting you to be a full-on DJ."
    s 5b "I know, but it just seems so fun."
    mc "Alright. Just remember that you're still taking classes right now."
    mc "Don't push yourself too hard, master DJ."
    s 3r "I'll try to remember that."
    s "It's just that there's so many songs to choose from, it takes time for me to know what fits."
    mc "Ok then. What songs have you put on the playlist anyway?"
    s 1a "The answer is a secret until Friday."
    mc "Is one of the songs the chicken dance?"
    s 5b "Da-a, nooo..."
    s 5d "Well, a bit of the song is the chicken dance."
    s 4h "But can you really blame me for putting that on there? It's so catchy!"
    show sayori 4r at t11 zorder 2
    "Sayori then does the dance moves in front of me."
    "It doesn't matter if we're alone or in public, if she thinks of the chicken dance, she will do the chicken dance."
    show sayori at thide zorder 1
    hide sayori
    show bg school
    with wipeleft_scene
    show sayori 4r at t11 zorder 2
    "By the time we reach the school, she's still dancing."
    "It's pretty funny, but I have to end the fun eventually."
    show sayori 4a at t11 zorder 2
    mc "Ok Chicken Sayori, that's enough for now, you have to save that energy for the party."
    mc "And the rest of the school day for that matter."
    s 4p "Aww, but it was so much fun."
    s 4a "I guess I'll just have to be extra chicken with my moves at the party."
    s 4x "I'll see you later, [player]."
    mc "See ya, Sayori."
    stop music fadeout 2.0
    show sayori at thide zorder 1
    hide sayori
    scene bg class_day
    with wipeleft_scene
    play music t6
    "With that conversation done, I go through the school day."
    "Meaning I get to spend another class period with Yuri."
    "However, today, something struck a chord with me."
    "Yuri's glum attitude from yesterday was still going strong."
    "The weird thing was that today, we were finally reading Portrait of Markov."
    "She should be ecstatic about this."
    "Instead, she's looking down, uninterested in the world around her."
    "I try some antics to get her attention."
    "I did the 'pspsps' thing that always gets a cat's attention, but I receive nothing to my avail."
    "I have the feeling that the rest of the week may not plan out well."
    "The class continued on and still nothing from her."
    "The anxiety I left behind yesterday was returning, my mind wondering what's going on in her head."
    "She didn't give me much to go off of in yesterday's conversation, so I'm drawing a blank."
    scene bg class_day
    with wipeleft_scene
    "The bell for the class rings and I'm left with nothing."
    "I get up to go to my next class as if it were any other day."
    "But I see Yuri still sitting there for a bit with the same still expression on her face before getting up."
    "Something is clearly messing with her, and I can't just let myself wonder while she obviously has something going through her head."
    show yuri 3g at t11 zorder 2
    "I walk up to her, but she still looked rather listless, disconnected from everything around her."
    mc "Hey Yuri, are you feeling well today?"
    show yuri 3n at t11 zorder 2
    "Yuri seemed a bit shocked when I asked that."
    y 3q "Ah, y-yes. Just a bit... Distracted today."
    y 2f "Why do you ask?"
    mc "I guess I'm just worried."
    mc "You've been really distant since yesterday."
    mc "I was wondering if you wanted to talk about it."
    show yuri 2h at t11 zorder 2
    "Yuri then made a slightly frustrated expression."
    "I don't think she was mad at me, but herself rather."
    y "I see."
    y 1t "[player], is it possible we can discuss this at a later time?"
    y "I don't want to be late to my next class."
    mc "Sure. Just ah... Promise me that we can talk about this, okay?"
    mc "It doesn't sit well with me when you get upset like this."
    y 1s "I-I promise."
    show yuri at thide zorder 1
    hide yuri
    "After that, she went on down the hall with great haste."
    "She nearly tripped over her own footsteps with how quick she was going."
    "This wasn't very successful, but she did promise to talk about it, so I suppose that's a step in the right direction."
    "My only hope is that we can talk after the club today."
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft
    play music t5
    "After the school day finishes, I make my way to the clubroom as normal."
    "However, instead of the gloom from yesterday that took over the room, there was something else going on."
    show sayori 4o at t11 zorder 2
    "I see Sayori looking around the rooms with the look of a detective in her eye."
    "Natsuki is watching her closely as well at one of the desks."
    show monika 1d at t31 zorder 2
    show natsuki 1k at t32 zorder 2
    show sayori 4o at t33 zorder 2
    "After setting my stuff down, I go ask Monika as to what is going on."
    mc "Hey Monika, do you have any idea as to why Sayori wants to be Sherlock Holmes right now?"
    show monika 1i at f31 zorder 3
    m "Shhhh."
    show monika 1d at t31 zorder 2
    "Monika puts a finger on my lip to silence me, as me, Monika, and Natsuki watch Sayori walk round the room."
    show sayori 4o at t33 zorder 2
    "She goes around the teacher's desk a few times before moving on to the windows."
    show sayori 4n at t33 zorder 2
    "I'm not sure what's more lost right now, me trying to figure out what's going on, or Sayori's detective skills."
    "At the windows, Sayori does a quick inspection on each frame before moving on to the closet."
    show sayori 4o at t33 zorder 2
    "Sayori then, for some reason, stealthily infiltrates the closet."
    "She snoops around each shelf before she jumps out of the closet and returns to the teacher's desk."
    show monika 1d at t31 zorder 2
    show natsuki 1k at t32 zorder 2
    show sayori 2a at f33 zorder 3
    s "Alright! With my examination done, I will place it here!"
    mc "Place what there?"
    s 2q "The boombox, of course."
    mc "Wait, you're telling me you went through the trouble of being a detective in this whole room, just to find out where to put a boombox?"
    show sayori 1a at t33 zorder 2
    show monika 2j at t31 zorder 2
    show natsuki 4z at t32 zorder 2
    "It's then that Natsuki starts to burst out laughing."
    show natsuki 4z at f32 zorder 3
    n "Oh my God! That's the funniest thing I've seen all day!"
    n "You went here thinking something important happened, to then find out the commotion was for a boombox!"
    show natsuki 4z at t32 zorder 2
    "Natsuki continues to giggle loudly at the desk."
    mc "I-It's not that funny."
    mc "There's no way you would laugh at me like that, right Monika?"
    "My heart is broken as I see Monika snickering to herself, trying her best to hide her humor."
    mc "C'mon Monika, not you too."
    show monika 3l at f31 zorder 3
    m "I'm sorry, [player]. I was meaning to tell you what was happening, but I thought it would be funnier to throw you in a loop."
    m "I'll be sure to tell you anything else that happens."
    show monika 2k at t31 zorder 2
    "You say you're sorry but you're still laughing..."
    show sayori 4r at t33 zorder 2
    "I turn to Sayori who is also laughing, like the traitor she is."
    mc "Were you in on this too Sayori?"
    show sayori 4r at f33 zorder 3
    s "N-no, {i}giggle{/i}, I swear. I'm only {i}giggle{/i} laughing because {i}snort{/i} they're laughing."
    show sayori 4r at t33 zorder 2
    "I'm in a triangle of laughter right now."
    "I know I should be mad right now, but for some reason I can't help but chuckle as well."
    show monika 3k at f31 zorder 3
    m "That's the spirit, [player]."
    m "You have to admit, that was pretty funny."
    show monika 3k at t31 zorder 2
    mc "Yeah, I guess you're right."
    "The laughter eventually dies down, but when it does, I notice Yuri."
    show natsuki 4z at t42 zorder 2
    show monika 2k at t41 zorder 2
    show sayori 4r at t43 zorder 2
    show yuri 4b at t44 zorder 2
    "Was she in the room the whole time?"
    "I walk over to Yuri, seeing that she's not sharing the same cheerful attitude as the club right now."
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    show sayori at thide zorder 1
    hide sayori
    show yuri 1g at t11 zorder 2
    mc "Yuri, did you see what happened just now?"
    y "...I did."
    y "I ah... Just don't have the urge to laugh right now."
    "I'm able to sense the tone in her voice."
    "Her bad mood from this morning is still upon her, changing the relaxing attitude I just had to one of worry."
    mc "Um, Yuri... Do you want to talk about anything?"
    mc "You said earlier you would be open to it."
    y 1f "I did, didn't I...?"
    y 1v "Can we... Talk about it later?"
    y "I don't feel comfortable talking about it right now."
    mc "Sure."
    "Despite the shenanigans today, Yuri still seems to be distraught about something."
    show yuri at thide zorder 1
    hide yuri
    "The day continues on like this, with Sayori planning something out over something very trivial."
    "I don't know why, but each of us smile when she does."
    "Except Yuri, however. Her demeanor stays the same throughout the entire meeting."
    "I know Yuri doesn't partake in anything so silly, but she would at least find it amusing like she has before."
    "The club day eventually ends, each of us saying our goodbyes as we made our exits."
    stop music fadeout 2.0
    scene bg road_sunset
    with wipeleft
    show yuri 1g at t11 zorder 2
    "On the way home, Yuri keeps to herself, shutting off any place for her radiant warmth to glow."
    "It's difficult to see her like this, but I figure now is as good a time as any to ask about why she's so depressed."
    mc "Yuri, we need to talk."
    y 1f "What do we need to talk about?"
    mc "I just... Need to know what's happening with you."
    mc "You look like you've lost all hope in life right now."
    mc "It hurts me to see you like this. Can you please tell me what's happening?"
    show yuri 1g at t11 zorder 2
    "Yuri takes a bit to form her response."
    "It looks like she's willing to open up."
    y 1h "It's going to take a bit of time to explain, do you have anything to do today?"
    mc "No. I want to listen to you."
    show yuri 1g at t11 zorder 2
    "She takes an apprehensive face before she speaks, almost afraid of what to say."
    y "..."
    play music t9
    y 1t "[player], do you remember when I first showed you my cuts?"
    "My spine begins to tingle when I hear that."
    mc "Yeah."
    y 2h "And when I thought about breaking up..."
    mc "..."
    y "I used the excuse that we weren't permanent."
    y "That you'll move on." 
    y "Well, here we are in the future, but something just feels... Wrong."
    y 1h "Everything around us is changing."
    y "When the club was announced to be cancelled, it opened my eyes to the truth."
    y 1h "The club will be gone, but what about the rest of you, the friends I made along the way?"
    y "I already told you I used to eat alone in the cafeteria, that I couldn't make friends in general."
    y "But the club, it felt like there was finally hope for me."
    y 2t "Hope that I could finally be happy with people other than myself."
    y 2v "It's so weird and difficult to explain, because I had always wished to be alone."
    y "But you all showed me how happy I can be, how free I can feel from my burdens."
    y "However, unfortunately, as the end was coming near, my instincts were right."
    y "I was right to believe everything was temporary."
    y "I was a fool to think otherwise, naive to believe that I can change the way destiny flows."
    y 3w "And what's the result?"
    y "I go back to relying on my burdens."
    y 3v "This pain, it's ironically the only relief I have with myself."
    y "And when everyone runs away from me because of my burdens, those burdens will be all I have left to comfort me."
    y "Though it can't amount to the friends I've made along the way..."
    y "Those friends, too, will be gone."
    y "Friends that took so long for me to find, stripped away from me."
    y 4b "..."
    y "I know it will only be harder from here on out for me."
    "We stay silent, standing on the road."
    "I knew Yuri's problems cut deep, but I didn't know it went beyond skin."
    "It goes to her very character."
    "I thought that I was helping her through this, but I haven't even gone through problem one."
    "What am I suppose to do now?"
    "..."
    y 1g "I... I should be going home now."
    y "I need some time alone."
    mc "Oh... Okay."
    y 1h "Goodbye, [player]."
    mc "Bye, Yuri."
    show yuri at thide zorder 1
    hide yuri
    scene bg black
    with wipeleft_scene
    "She walks off into the sunset, the only dark spot on the golden horizon."
    "I start walking back home, as well, taking in and processing the conversation."
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    "What the hell do I do?"
    "Everything was going somewhat well before, but now..."
    "How am I suppose to fix this? I can't exactly stop the end from happening."
    "I was in this room with her the first time she explained this to me, all that time ago."
    "But here I am, still unknowable to how to help her."
    "Maybe there's something from that time that could help me now."
    "When she believed in me, when she went outside of her own head and saw what I was doing for her."
    "After that, she saw that she was worthwhile for me."
    "But now, here at the end, she's afraid of the thought of losing all of us for good."
    "But... If that's the case..."
    "Maybe I just need to show how worthwhile she is to her friends."
    "Maybe if I can show we can live beyond the literature club, that they can love her and understand her throughout life..."
    "Perhaps that can be just what she needs to hear."
    "But for that to happen, for Yuri to truly believe they'll love her through anything, I'll have to tell them everything about Yuri."
    "Which could include her cutting."
    "..."
    "It's going to be rough in more ways than one."
    "But she needs to hear it, from all of us."
    "I'll talk with Sayori when I see her tomorrow, perhaps just have her talk to Yuri first."
    "But if that doesn't work, then we may have to move to more certain measures."
    "This is so strange, so unlike me when I think back."
    "But, for some reason, I know I have to do this."
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "Another day of school, another day that I wish I could sleep in."
    "Or at least, I would say that if today wasn't so important."
    "I have to make sure things go well with Sayori."
    "Not too long after finishing that thought, I see her coming up to me from up the street."
    "Speak of the devil."
    show sayori 1a at t11 zorder 2
    s "Hey [player], how's it going?"
    mc "It's going pretty well Sayori."
    s "You waited for me today instead of being groggy, so I'm guessing you have something in mind."
    mc "Wait, how would you know something like that?"
    s 2x "I've lived next to you for so long, I know how you act, [player]."
    "I have to remind myself that Sayori isn't an airhead all the time, despite how she acts."
    "She can be pretty sharp and creative when she puts her mind to something."
    s "Well, what are you hoping for today?"
    mc "Well, it's about Yuri."
    mc "You've noticed how she's been a bit down for the past few days, right?"
    s 2k "Yeah, she just seems so upset about something."
    s "I can tell she's going through a difficult time, believe me."
    mc "I do, I tried talking to her about it yesterday and it didn't pan out so well."
    s 2c "Did anything serious happen? Like, relationship threatening?"
    mc "No, nothing like that. But it is something threatening however."
    s 3b "What is it?"
    mc "Yuri believes that because the literature club is ending, that she'll be no longer friends with us."
    s 4h "What? But we would never leave her behind!"
    mc "That's what I was thinking too, and that's why I need your help."
    s 1b "I'm listening, [player]."
    mc "I need you to talk to Yuri today. I think I've done all I can on my own, so that's why I need you to help Yuri out as well."
    mc "You two share a class, right?"
    s 2c "Yeah, I share math with her."
    mc "Can you talk with her then?"
    s 2h "Of course, there's no way I would leave a friend thinking they're valueless."
    s "It really feels like the worst."
    mc "Thanks Sayori, I can always rely on you."
    s 2a "No problem."
    show sayori at thide zorder 1
    hide sayori
    scene bg school
    with wipeleft_scene
    show sayori 1a at t11 zorder 2
    "By the time our discussion ends, we're already outside the school."
    mc "I'll be seeing you later, Sayori."
    s "Alright, bye [player]."
    "Hopefully Sayori can handle this on her own."
    "If she can't, I'll have to use plan B."
    stop music fadeout 2.0
    show sayori at thide zorder 1
    hide sayori
    scene bg club_day
    with wiperight
    play music t5
    "Here I am after school, and I'm just hoping everything went okay between Sayori and Yuri."
    "I wasn't able to focus at all in class today with how Yuri is fairing."
    "I'm lucky this week doesn't really count."
    "I hear footsteps by the door, the anticipation of who is walking killing me."
    show sayori 1f at t11 zorder 2
    s "Hey, [player]."
    mc "Hi Sayori, how did it go with Yuri?"
    show sayori 1k at t11 zorder 2
    "With Sayori's face looking down, I didn't expect good news."
    s "I don't think I really got to her."
    s "She seemed really stuck with her thoughts."
    s "I tried mentioning it subtly at first, but she saw through me."
    s "I think she got mad at herself by me asking anything about her raincloud."
    s 1g "Sorry I wasn't able to help."
    mc "It's okay Sayori, you did the best you could."
    "This isn't good at all." 
    "With how things are going, that plan B might have to come into action." 
    "I'm going to have to tell the club about Yuri's cutting so they can really understand what's going on."
    "I know they'll understand, but I'm not sure Yuri will."
    "Natsuki and Monika enter the room, both talking happily about something."
    show natsuki 1a at t31 zorder 2
    show monika 1a at t32 zorder 2
    show sayori 1b at t33 zorder 2
    mc "Hi guys, what's going on?"
    show natsuki 3d at f31 zorder 3
    n "Oh, it's nothing. Monika just said something she really shouldn't have."
    show natsuki 4y at f31 zorder 3
    n "Honestly Monika, I didn't know you were like that."
    show natsuki 4y at t31 zorder 2
    show monika 2l at f32 zorder 3
    m "I'm not, Natsuki. My mind just wanders sometimes, you know."
    show monika 2l at t32 zorder 2
    show natsuki 4d at f31 zorder 3
    n "I don't think just anyone would wonder if-"
    show monika 5b at f32 zorder 3
    show natsuki 4l at t31 zorder 2
    m "Not in front of [player], Natsuki!"
    show monika 5b at t32 zorder 2
    show natsuki 5y at f31 zorder 3
    n "You get to tease me all the time! I say it's my turn to tease you!"
    show monika 5b at f32 zorder 3
    show natsuki 5y at t31 zorder 2
    m "But not with something like that!"
    show monika 5b at t32 zorder 2
    show natsuki 5d at f31 zorder 3
    n "That'll just make it even better."
    mc "What are you two even talking about?"
    n 4d "Well, Monika was just wondering if you and-"
    n 1z "Wha-! Gahahahaha!"
    show natsuki 1z at t31 zorder 2
    show monika 5a at t32 zorder 2
    "Monika then went on a tickle assault toward Natsuki, and a ferocious one at that."
    show natsuki 1v at f31 zorder 3
    n "Mon-haha-ik-ha-aa! {i}giggle{/i} Quit it! Haha!"
    show natsuki 1v at t31 zorder 2
    show monika 5j at f32 zorder 3
    m "It's gonna take alot more than simple begging to stop me."
    show monika 5j at t32 zorder 2
    "Natsuki is trying her best to be angry, but the tickling is preventing her from being so."
    "Monika continues her attack on Natsuki as me and Sayori just stand here."
    mc "Is it me, or is everyone acting a bit out of character right now?"
    show sayori 1x at f33 zorder 3
    s "I guess everyone's just really comfortable with each other at the moment."
    show sayori 1b at t33 zorder 2
    mc "Yeah. A tickle attack is more of your style Sayori."
    s 1n "..."
    show sayori 2q at f33 zorder 3
    s "And it still is."
    show sayori 2q at t33 zorder 2
    mc "Wait, what was that?"
    show sayori 4r at t33 zorder 2
    "Sayori suddenly started making a sinister face and glares at Natsuki."
    show sayori 4r at f33 zorder 3
    s "Here I come!"
    show sayori 4r at t33 zorder 2
    show natsuki 1v at f31 zorder 3
    n "Say-{i}haha{/i}-ori, ha! Not you, {i}giggle{/i} too!"
    show natsuki 1v at t31 zorder 2
    show monika 1a at f32 zorder 3
    m "I guess I can stop now since you've learned your lesson."
    m 3j "But that just leaves you at the mercy of Sayori."
    show natsuki 1v at f31 zorder 3
    show monika 1a at t32 zorder 2
    n "Nooo-{i}haha{/i}-ooo!"
    show natsuki 1v at t31 zorder 2
    "Well, looks like things are going back to normal."
    mc "Monika, what was it that Natsuki was trying to say?"
    show monika 2n at f32 zorder 3
    m "Oh that. I don't think you'll want to know, you may not like what you hear."
    show monika 2n at t32 zorder 2
    mc "You don't say?"
    "I look back at Natsuki who is reclaiming her stance, and gets out her vicious fang."
    show monika 3k at f32 zorder 3
    m "Alright Sayori, you can calm down on the tickling now."
    show monika 3k at t32 zorder 2
    show sayori 1q at f33 zorder 3
    s "Okay, okay."
    show sayori 1q at t33 zorder 2
    show natsuki 5u at t31 zorder 2
    "Natsuki stands up with a sour expression on her face."
    show natsuki 5w at f31 zorder 3
    n "You two are out of your mind, you know that?"
    show natsuki 5w at t31 zorder 2
    mc "C'mon Natsuki, don't tell me you didn't have any fun."
    show natsuki 5s at f31 zorder 2
    n "..."
    n 5q "That's not untrue."
    show natsuki 5s at f31 zorder 2
    "We all have a laugh from that. Well, all except Yuri."
    show natsuki 5s at t41 zorder 2
    show monika 3k at t42 zorder 2
    show sayori 1q at t43 zorder 2
    show yuri 1g at t44 zorder 2
    "She was just sitting at a desk reading a book."
    "A part of me doubts she didn't see the commotion."
    "I just wish I could just get through to her."
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 2
    hide natsuki
    show sayori at thide zorder 2
    hide sayori
    show yuri at thide zorder 2
    hide yuri
    "The day goes on in a relaxed tone."
    "Everyone is just talking to each other, nothing holding us down."
    "But Yuri continued to stay in her book the whole time." 
    "I think I'm understanding more about her burden, though."
    "I remember Monika once telling me that Yuri's books are a band-aid, and I'm seeing that clearly right now."
    show monika 3k at t11 zorder 2
    m "Okay everyone, I think we had our fun for today. I call this meeting to an end."
    "Everyone starts walking out of the clubroom the same as yesterday."
    "Despite Yuri and I not talking much, I still walk home with her."
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 2
    hide natsuki
    show sayori at thide zorder 2
    hide sayori
    show yuri at thide zorder 2
    hide yuri
    stop music fadeout 2.0
    scene bg residential_sunset
    with wipeleft
    show yuri 4b at t11 zorder 2
    play music t12
    "On the way home, I notice the atmosphere isn't as strangling as yesterday."
    "Even the sun's rays aren't blasting at me, rather a soft glow on my skin."
    "I look over to Yuri who is looking off in the distance."
    "I wonder what she's thinking about."
    "..."
    y 4a "[player]?"
    mc "U-um, what is it Yuri?"
    y "Can I ask you something?"
    mc "S-sure, anything at all."
    "She's been silent through the whole day, there's no way I'll know what she's gonna ask."
    y "Earlier in the clubroom today, and even the day before, you all looked so happy."
    y 4b "I just need to know... How?" 
    y "How can you be so joyful when you can't see a future for yourself?"
    stop music fadeout 2.0
    play music t9
    y 3t "Aren't you afraid at all about the future? How it could be like before you met everyone?"
    mc "Well, to be honest Yuri, not really."
    mc "Even before the club, I wasn't really in a bad place, but I don't think it was the same for you."
    y 4b "Unfortunately not..."
    mc "You're always thinking ahead and about every situation you've been in."
    mc "That's great to do honestly, and it's part of what makes me love you."
    mc "Sayori even told me I'd be a neet if I didn't think like that, but..."
    y 3f "But what?"
    mc "That's not an enjoyable way to live life for me, being honest."
    mc "I don't usually think this emotionally because it doesn't suit me."
    mc "But a part of me felt though if I can get through another day just so I could see you and the others, then so be it."
    mc "Even though this might not be the best life advice, I need to be honest with myself."
    mc "Does that help you with anything?"
    y 3i "...It does a little bit."
    y "Thank you for talking with me."
    "We arrive at my house by the time I was done answering her question."
    mc "I guess this is where we say goodbye for today."
    y 3j "I suppose so."
    y "Goodbye, [player]."
    mc "Bye, Yuri."
    show yuri at thide zorder 1
    hide yuri
    "It's another beautiful sunset for today, but this time, Yuri doesn't contrast so much with the horizon."
    "Maybe things are getting better. She was willing to listen today."
    "Have I gotten through to her? If I have someone else go talk to her about this then she might just be able to be happy with herself."
    "..."
    "Probably not."
    "Something like this doesn't feel like it'll be solved in one talk."
    "I feel like she still needs another push before she finally embraces herself and her fears, and I'm afraid that little push will need me to be proactive."
    "I'm sorry Yuri, it's time for plan B."
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "Here we are on a Thursday."
    "With what I have to do, I feel a bit nervous."
    "This can end very poorly by how Yuri receives it, but I just have to hope she's able to pull through with my idea."
    "Sayori comes along as normal."
    "She seems to be happy about something."
    show sayori 1a at t11 zorder 2
    s "Hi [player]!"
    mc "Hi Sayori, has anything piqued your interest today?"
    mc "You seem to have something on your mind."
    s 2a "Yep! It's that tomorrow is the party and my playlist is almost ready."
    mc "That sounds great. But ah, can you actually do me a favor today?"
    s 1b "Another one? Is it about Yuri?"
    mc "Well, kind of."
    mc "I need you and the rest of the girls except Yuri to talk with me after the club ends."
    mc "There's something important I need to discuss."
    s 3c "No problem, [player]."
    s "I'm willing to do anything to see Yuri feel better."
    mc "I feel the same way."
    mc "Thank you, Sayori."
    show sayori at thide zorder 1
    hide sayori
    scene bg school
    with wipeleft_scene
    show sayori 1a at t11 zorder 2
    "We arrive at the school right when the bell rings."
    s "Bye [player], I'll see you at the club."
    mc "Later, Sayori."
    show sayori at thide zorder 1
    hide sayori
    "Hopefully she takes the news I'll have to deliver well."
    "For Yuri's sake."
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t5
    "The club day ends as it has throughout the week."
    "There's laughter to be had and some talk about the party tomorrow."
    "Throughout the whole meeting, however, I had this unnerving feeling."
    "I feel a pang of guilt for what I have to do today."
    "I have no idea how the girls will react once I tell them."
    "I know my reason is justified, but the thought of Yuri feeling betrayed honestly scares me."
    "They have to understand, they have to..."
    show monika 4b at f41 zorder 3
    show natsuki 1a at t42 zorder 2
    show sayori 1a at t43 zorder 2
    show yuri 1g at t44 zorder 2
    m "Okay everyone, that'll be it for today."
    m "Other than that, please be excited for the party tomorrow."
    show monika 4b at t41 zorder 2
    show natsuki 2m at f42 zorder 2
    show sayori 1o at t43 zorder 2
    n "Sayori, are you alright? You're staring past us."
    show natsuki 2m at t42 zorder 2
    show sayori 1o at f43 zorder 3
    s "I have been preparing my whole life for this."
    show natsuki 2g at f42 zorder 3
    show sayori 1o at t43 zorder 2
    n 2d "Sayori, get a hold of yourself!"
    n "It's just a party!"
    show natsuki 2d at t42 zorder 2
    show sayori 5a at f43 zorder 3
    s "Sorry, I'm just so excited!"
    show natsuki 2d at f42 zorder 3
    show sayori 5a at t43 zorder 2
    n "I am too, but no need to be creepy about it."
    show natsuki 2d at t42 zorder 2
    "Looks like the girls are already together."
    "I just have to get Yuri to leave the room now."
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    show sayori at thide zorder 1
    hide sayori
    show yuri 1e at t11 zorder 2
    mc "Hey Yuri, you could head home without me today."
    mc "I told Sayori we have to get some preparations ready for the party tomorrow."
    y 1f "Oh, I didn't think Sayori would make you involved in this as well."
    mc "Actually, this is something I've been meaning to do."
    mc "You know, it makes it feel special."
    y "Wow [player], I didn't expect you to take the initiative for this."
    mc "Yeah, I surprise even myself."
    y 1s "Okay then. I'll see you tomorrow."
    y "Bye, [player]."
    mc "Bye, Yuri."
    show yuri at thide zorder 1
    hide yuri
    show monika 1a at t31 zorder 2
    show natsuki 1a at t32 zorder 2
    show sayori 1a at t33 zorder 2
    "Yuri exits the clubroom, leaving me with the rest of the girls."
    "Deep breaths, [player]. It's all going to be fine."
    "I hope."
    "I went up to the group as they gathered together in the front of the room."
    mc "Sayori, do you remember what I talked about this morning?"
    show sayori 1b at f33 zorder 3
    s "Yeah, you said you had to tell us something."
    show sayori 1b at t33 zorder 2
    show monika 1d at f31 zorder 3
    m "Wait, what's this thing that's so important?"
    m 5b "With Yuri out of the room, I'm guessing you're throwing a special surprise for her tomorrow."
    m "Way to make it about her."
    show monika 5b at t31 zorder 2
    mc "That's not really-"
    show natsuki 4e at f32 zorder 3
    n "Yeah [player], this is supposed to be about all of us."
    show natsuki 4e at t32 zorder 2
    mc "It's just that-"
    show sayori 2c at f33 zorder 3
    s "Wait guys, I think it's actually serious." 
    s "He was pretty upset when he mentioned it."
    show sayori 2c at t33 zorder 2
    mc "You're right, it's-"
    show natsuki 4w at f32 zorder 3
    n "Well, spill it out. What is it that only us three can hear-{nw}"
    stop music fadeout 2.0
    show natsuki 4w at t32 zorder 2
    mc "Yuri cuts herself!"
    show monika 1d at t31 zorder 2
    show natsuki 1p at t32 zorder 2
    show sayori 1g at t33 zorder 2
    $ n_name = "All"
    n "..."
    show monika 1o at t31 zorder 2
    show natsuki 1q at t32 zorder 2
    show sayori 1k at t33 zorder 2
    n "..."
    $ n_name = "Natsuki"
    "The room went dead silent."
    "No one knew how to respond after that, and I couldn't blame them."
    "It was definitely not something you would just here."
    "The silence hung for a while before Sayori was able to break the ice."
    show sayori 1h at f33 zorder 3
    s "[player], what do you mean by she cuts herself?"
    show sayori 1h at t33 zorder 2
    mc "I mean that she cuts herself, and... Kind of has a thing about it."
    mc "She likes to cut her arms to feel the pain... To feel something."
    show sayori 1k at f33 zorder 3
    play music t9
    s "..."
    s "I-I never knew."
    show sayori 1k at t33 zorder 2
    show monika 3p at f31 zorder 3
    m "Excuse my language, but that's one hell of a bomb to drop."
    show monika 1p at t31 zorder 2
    mc "Yeah..."
    mc "..."
    n "..."
    show natsuki 5q at f32 zorder 3
    n "So, have you done anything about it?"
    show natsuki 12b at t32 zorder 2
    mc "I've been trying to help, and I thought I was, but-"
    show natsuki 5h at f32 zorder 3
    n "But what? It sounds like you're doing a pretty lousy job at being a boyfriend."
    show natsuki 5g at t32 zorder 2
    show monika 1i at f31 zorder 3
    m "Natsuki, you don't need to be spiteful towards [player]."
    show natsuki 1h at f32 zorder 3
    show monika 1i at t31 zorder 2
    n "But, Yuri's hurting, and it doesn't look like [player] is doing a darn thing about it."
    show natsuki 1h at t32 zorder 2
    show monika 1i at f31 zorder 3
    m "I'm sure he's done everything he could so far. You know that he loves her."
    m "Otherwise, what was the point of telling us if he didn't care?"
    show natsuki 5u at f32 zorder 3
    show monika 1i at t31 zorder 2
    n "...I suppose you're right."
    n "It just... Sucks, you know? She had this problem the whole time, and none of us knew."
    show natsuki 5u at t32 zorder 2
    mc "None of you could've known, she kept it pretty well hidden."
    mc "..."
    show monika 1f at f31 zorder 3
    m "So, what can we do to help?"
    show monika 1f at t31 zorder 2
    mc "Monika?"
    show monika 1g at f31 zorder 3
    m "I know I've acted like a villain in the past, but I truly do care about her, about all of us."
    m "Just tell us what needs to be done and we'll do it."
    show monika 1e at t31 zorder 2
    show sayori 3d at t33 zorder 2
    show natsuki 2j at t32 zorder 2
    "Sayori and Natsuki smiled and nodded in response, awaiting what I had to say as well."
    "It made me happy to see them take it all so well."
    "And I'm sure Yuri will as well."
    mc "Thanks, Monika. You too, Natsuki, Sayori. I apperciate it a lot."
    mc "I did have something in mind, during the party." 
    mc "Here's what we'll do tomorrow..."
    stop music fadeout 2.0
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    show sayori at thide zorder 1
    hide sayori
    scene bg black
    with fade
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "It's finally Friday."
    "After speaking with the others yesterday about my plan, I felt ready."
    "This is the make it or break it day."
    "I see Sayori catching up to me on the way to school."
    show sayori 1a at t11 zorder 2
    mc "Hey Sayori. Are you ready for today?"
    s "Definitely. I have my whole playlist ready, along with my spirit."
    mc "And you remember what to do during the party today?"
    s 2x "Yeah, take all the cupcakes before Natsuki realizes."
    mc "Sayori, I meant with Yuri."
    s 1d "Oh yeah, I remember what to do then too."
    mc "Good. Also, you need to learn how to share."
    s 1a "I'll give you a portion of them if you don't mention it to Natsuki."
    mc "Deal."
    show sayori at thide zorder 1
    hide sayori
    scene bg school
    with wipeleft
    show sayori 1a at t11 zorder 2
    "We arrive at the school waiting for the bell to ring."
    mc "I'll see you at the club later."
    s "Alright then, bye [player]."
    mc "Later, Sayori."
    show sayori at thide zorder 1
    hide sayori
    "Sayori walks off into the scurry of students passing the halls."
    "There's a lot more students that I thought would show up, but there's only one that I'm thinking about today."
    "I want to see you happy again, Yuri."
    stop music fadeout 2.0
    scene bg club_day
    with wiperight
    play music t5
    show sayori 1a at t11 zorder 2
    "I arrive in the clubroom with Sayori."
    "Natsuki and Monika are already here, preparing for the party."
    "Monika is setting up some props and streamers, while Natsuki is setting up the food area."
    "Sayori immediately dashes for one of the cupcakes while Natsuki has her back turned."
    "I know I saw it coming, but even for Sayori that was fast."
    "She grabs one and puts it behind her back, obscuring it from Natsuki's sight."
    "Sayori then gently whispers to me."
    s 1x "If I take them all at once, then she might notice that they're disappearing."
    mc "R-right, Sayori. I'm sure that'll be the solution."
    show sayori at thide zorder 1
    hide sayori
    "Without hesitance, I go grab a cupcake myself. These things are really something to behold after all."
    "Right when I'm about to grab one though, Natsuki turns around."
    show natsuki 4g at t11 zorder 2
    n "What do you think you're doing, idiot?!"
    mc "Ah... Taking a cupcake?"
    n 3e "Well duh, but you can't have any yet! You have to wait until we're all here."
    n 3h "Wait a minute..."
    n 4f "[player], did you already take one?!"
    mc "N-no!"
    n "I can tell you're lying, your voice gives it away!"
    mc "But I really didn't take one yet!"
    mc "It was Sayo-"
    "I turn around to rat out the real culprit, but I don't see Sayori. Where did she go?"
    n "Don't think you can pull a fast one on me, I know I put one there."
    "I decide there's no point in arguing, she already has her mind set."
    "Might as well keep quiet."
    n 4w "Can't talk after the truth is exposed? Well, I'll be."
    n 4y "I guess I can forgive you this time. I'm happy to know they're worth lying over."
    "I can hear Monika snickering in the background. She probably saw Sayori take the cupcake."
    "The things I must bear with this group to keep them happy."
    show natsuki at thide zorder 1
    hide natsuki
    "I hear footsteps approaching from outside of the door."
    "That must be Yuri."
    show monika 4i at t11 zorder 2
    m "Okay everyone, act natural!"
    show monika at thide zorder 1
    hide monika
    show yuri 4b at t11 zorder 2
    "Yuri enters the room with her eyes looking at the ground."
    "I guess she's been scared to enter the clubroom today."
    "I'll have to make her feel like she's wanted."
    mc "Hey, Yuri. How are you feeling right now?"
    "Great job [player], there's no way you can sound more generic."
    y 1v "I feel fine, I guess."
    y "I've been thinking alot over about what you told me a few days ago."
    mc "Well, if you feel stressed, you can have a cupcake."
    mc "They still taste as great as ever."
    show yuri 4b at t21 zorder 2
    show natsuki 2d at f22 zorder 3
    n "Yeah Yuri, so great that [player] even took one before we were all here."
    show natsuki 2d at t22 zorder 2
    mc "I told you, it wasn't me!"
    show yuri 3u at t21 zorder 2
    "Yuri giggles from me and Natsuki's squabble."
    show yuri 3u at f21 zorder 3
    y "Yeah, I think I'm due for a cupcake actually."
    show yuri 3u at t21 zorder 2
    "She takes one up and bites it, with a familiar smile of satisfaction on her face."
    "No one can deny the joy of Natsuki's cupcakes."
    show yuri 3u at t41 zorder 2
    show natsuki 2d at t42 zorder 2
    show sayori 3o at t43 zorder 2
    show monika 1a at t44 zorder 2
    "Sayori re-enters with a boombox in her hands."
    "I know why she left the room now. What perfect timing..."
    show sayori 3o at f43 zorder 3
    s "Alright Monika, I got this, let me just-"
    show sayori 3o at t43 zorder 2
    "Sayori struggles to carry the boombox. I have to admit, this one does look admirably big."
    mc "Sayori, are you sure you can handle that?"
    show sayori 3o at f43 zorder 3
    s "Yeah, I just gotta-"
    show sayori 3o at t43 zorder 2
    "Sayori, after much struggle, is finally able to place the boombox on the teacher's desk."
    show sayori 3s at f43 zorder 3
    s "{i}Huff{\i} See, {i}huff{\i}, not that heavy."
    show sayori 5a at t43 zorder 2
    show monika 1d at f44 zorder 2
    m "Where did you even find this anyway, Sayori?"
    show sayori 1c at f43 zorder 3
    show monika 1d at t44 zorder 2
    s "There was a classroom where this was just laying around for a year, and no one ever bothered to pick it up."
    s "I figured since this was the last day of school and no one was taking it that I would give it a new home."
    s 2x "That way, nothing bad can happen to it when next year rolls around!"
    show sayori 2x at t43 zorder 2
    mc "Yeah, I just have to make sure it's safe from you first."
    show sayori 2j at f43 zorder 3
    s "Hey, that's not nice. I can take care of it."
    show sayori 2j at t43 zorder 2
    mc "You can have it when you can be responsible for it."
    show sayori 4p at f43 zorder 3
    s "Noooooo!"
    show sayori 4p at t43 zorder 2
    show natsuki 3w at f42 zorder 3
    n "What the heck is wrong with you guys?!" 
    n "You're acting like it's some puppy. It's a boombox!"
    n "Just play something on it already!"
    show sayori 2a at f43 zorder 3
    show natsuki 3g at t42 zorder 2
    s "Sure thing, Natsuki."
    show sayori 2a at t43 zorder 2
    show yuri 4e at t41 zorder 2
    "As Sayori goes on her phone to find her playlist, I notice Yuri is once again giggling to herself."
    "Looks like being with her friends is making her feel just a bit better."
    "It nearly brings a tear to my face, but I'm reminded that this alone probably won't be enough to see her own value."
    "With Yuri as open as she's being right now, I think it's time we finally talk."
    show sayori 1b at t43 zorder 2
    stop music fadeout 2.0
    mc "Sayori, can you pause on finding that playlist right now?"
    mc "I think it's time."
    "Sayori puts down her phone right away, everyone else noticing my cue."
    "Here we go..."
    show yuri 2e at f41 zorder 2
    y "Um, what's going on? Was there something we were suppose to do first?"
    show yuri 2e at t41 zorder 2
    "I walk up and put my hand on top of Yuri's as she put it to her chest."
    mc "Yuri, we just want to say, this whole club has been an amazing ride with you."
    mc "Please don't be scared of what I'm about to ask."
    y "W-what are you talking about, [player]?"
    y 3q "I... I'm starting to get nervous."
    play music t10
    mc "Yuri, I need you to roll up your sleeves."
    show yuri 3p at t41 zorder 2
    "Her face immediately changed to one of shock, which was not unexpected."
    show yuri 3p at f41 zorder 3
    y 3p "W-What?! 
    y "[player], you know I can't do that!" 
    y "Not with everyone around...!"
    show yuri 3p at t41 zorder 2
    show monika 1d at f44 zorder 3
    m "We already know, Yuri. [player] told us yesterday about it."
    show monika 1d at t44 zorder 2
    show yuri 3p at hf41 zorder 3
    y "Wha-what?! Why?! Why did you tell them?!"
    y "It was suppose to be a secret!"
    y 3o "I'm not ready for others to know. I'm not ready to deal with others thinking of me like... Like a freak!"
    show yuri 3o at t41 zorder 2
    mc "Yuri, I had to tell them. What you told me on Tuesday really frightened me."
    mc "It sounded like you already gave up on yourself without giving yourself a chance."
    mc "I knew they would understand, but I needed a way to prove that to you."
    show yuri 3o at f41 zorder 3
    y "But... But not like this! It's all so sudden! I-I need to go, b-but..."
    y "W-Where do I go?"
    y "There's... Nowhere for me to leave."
    show yuri 3v at t41 zorder 2
    "Yuri just stayed sitting down realizing that it's no use running away."
    show yuri 4b at f41 zorder 3
    y "You must have planned this ahead of time, didn't you, [player]?"
    mc "Yeah, I did."
    show yuri 4b at t41 zorder 2
    stop music fadeout 2.0
    "Yuri sat there in silence, contemplating."
    "It really seemed like she didn't know how to react right now."
    "A part of me did feel guilty, because I know how hard this might be for her."
    "But she had to know what we felt about her as her friends, her family."
    "From every single one of us, about every part of her, no matter what."
    y "..."
    y "I guess there's nothing to hide anymore..."
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    "Yuri grabs hold of her sleeve and slowly unravels her arms."
    show monika 1g at t44 zorder 2
    show sayori 1m at t43 zorder 2
    show natsuki 1c at t41 zorder 2
    show yuri 5ac2 at t42 zorder 2
    play music t9
    "..."
    "Sayori is stunned from the damage that's left on her arms."
    "Even I'm a bit terrified, this is the worst I've ever seen them."
    "I see some from before that have healed, but there are others that are new and look... Painful."
    y "..."
    y 5dc2 "You all think I'm a freak now, don't you?"
    show natsuki 1b at f41 zorder 3
    n "What?"
    show natsuki 1g at t41 zorder 2
    y "...You all think I'm a freak, terrified right now at who I am."
    y 5bc2 "I'm sorry that I can't control myself."
    y "I can barely keep myself when I speak. People have a hard time with me."
    y "My interests are weird, so everyone is just disgusted with me."
    y "I look like the most dangerous person you'll ever know."
    y 5cc2 "A freak show that can't keep herself in check."
    y 5dc2 "That's why others avoid me, they want to keep themselves safe from me, they're afraid of me."
    y "I was right to ostracize myself, because after this I won't be able to make friends with anyone again."
    y "I'm a threat to everyone, even myself."
    y "I never thought that it would hurt so much being alone again..."
    y 5ac2 "But after this school year with all of you, I don't want to ever go back."
    y "But... I'll have to keep going."
    y "Things can never stay the same."
    y "Life will always move while I'm still here, stuck in my own traps."
    y 5bc2 "I'll never be happy with all of you, because... Because I'm the wor-"
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    "Out of nowhere, Natsuki goes in for a hug, with Yuri going silent."
    "And slowly, Sayori and Monika make their way, adding their own arms around her."
    show natsuki 12a at f42 zorder 3
    n "Yuri, I really need you to be quiet real quick..."
    n "Do you really think we'll all run away because you're hurt?"
    n 1q "Well, I have news for you."
    n 1h "This club is never separating."
    n "I never had a place where I feel accepted to be me."
    n "And you're part of this club, so don't you dare think we'll leave because of who you are."
    show natsuki 1g at t42 zorder 2
    show monika 1i at f44 zorder 3
    m "Yuri... Your demeanor, your interests, your desires, that's what makes you unique."
    m 1e "There's no way we can have this club without you."
    show monika 1e at t44 zorder 2
    show sayori 1g at f43 zorder 3
    s "Even if it feels like you're in a deep hole that you can never jump out of, your friends are here to grab your hands to help you."
    s 1t "And even if we fall in, we'll fall in together."
    show sayori 1t at t43 zorder 2
    mc "Yuri, remember when I said life moves on?"
    mc "Well, life moves on with friends too."
    mc "And the friends that stay beside you are the ones who accept you for everything that makes you, you."
    mc "It's not just me that loves you Yuri."
    mc "We all love you."
    "I see a tear drop from Yuri's face, then more start to fall."
    "Before we know it, her face was full with tears as she cried in their arms."
    #(many facial changes of Yuri crying)
    show yuri 5dc2 at f41 zorder 3
    y 5cc2 "..."
    y "..."
    y 5ec2 "..."
    y 4nc2 "Thank you, all of you, truly."
    y 4oc2 "You all make me happy to just purely exist."
    y "And there's no better feeling I've felt than what you have all given me."
    show yuri 4sc2 at t41 zorder 2
    "As her crying started to slow, she slowly rolled her sleeves back down, wiping the tears off her face."
    show yuri 2u at f41 zorder 3
    y "I think I'm feeling better now..."
    show yuri 2u at t41 zorder 2
    show sayori 1d at f43 zorder 3
    s "Aww, but I want the hug to last a bit longer."
    s "It feels so nice, especially when Natsuki decides she wants to be in it."
    show sayori 1d at t43 zorder 2
    show natsuki 1v at f42 zorder 3
    n "And that's where I draw the line! Hugs over now, move on!"
    show natsuki 1v at t42 zorder 2
    mc "C'mon Natsuki, I was liking that hug too."
    show natsuki 1d at f42 zorder 3
    n "Well, if you want to keep on hugging, then you come here and hug your girlfriend too!"
    show natsuki 1d at t42 zorder 2
    show monika 5a at f44 zorder 3
    m "I'm sure he'll be happy to."
    m "After all, he does have incentive."
    show yuri 1s at t41 zorder 2
    show monika 5a at t44 zorder 2
    show natsuki 1d at f42 zorder 3
    n "Monika, you said you didn't let your mind wander to those types of thoughts."
    show natsuki 1d at t42 zorder 2
    show monika 5a at f44 zorder 3
    m "I know, I know. It's just funny to see you get so flustered."
    show monika 5a at t44 zorder 2
    show sayori 3o at f43 zorder 3
    s "Wait, what are you two talking about?"
    show sayori 3o at t43 zorder 2
    show monika 2j at f44 zorder 3
    m "Don't worry about it Sayori, let's just keep this party going."
    m 2k "As club president, I order this to be the most exciting meeting ever!"
    show monika 2j at t44 zorder 2
    show natsuki 2k at f42 zorder 3
    n "You mean, you {i}former{/i} club president."
    show natsuki 2k at t42 zorder 2
    show monika 1f at f44 zorder 3
    m "Former?"
    show monika 1f at t44 zorder 2
    show natsuki 2d at f42 zorder 3
    n "Yeah, the school day is over, meaning your reign is finally over."
    show natsuki 2d at t42 zorder 2
    show monika 1l at f44 zorder 3
    m "Hey, this is still a club activity! I still have the power."
    show monika 1a at t44 zorder 2
    show sayori 2n at f43 zorder 3
    s "Wait a minute, if Monika is no longer the president, does that mean I become president?"
    show sayori 2n at t43 zorder 2
    show monika 1l at f44 zorder 3
    m "You know Sayori, sure. You're the club president now."
    show monika 1l at t44 zorder 2
    show sayori 4r at f43 zorder 3
    s "Yaaaaay!"
    s 2x "Well, come on guys, let's get pumped! I have the perfect song right now!"
    show sayori 4r at t43 zorder 2
    "Sayori goes on her phone once more and we're finally able to hear her playlist."
    "Truth be told, it wasn't that bad. There were actually some fire beats in there. "
    "Just as long as you were okay with the chicken dance."
    show sayori at thide zorder 1
    hide sayori
    show monika at thide zorder 1
    hide monika
    show natsuki at thide zorder 1
    hide natsuki
    show yuri at thide zorder 1
    hide yuri
    scene bg club_sunset
    with wipeleft_scene
    "The party goes on for a while until the hue outside changes."
    "After cleaning up, we all get together one more time."
    show yuri 1a at t41 zorder 2
    show natsuki 1a at t42 zorder 2
    show sayori 1a at t43 zorder 2
    show monika 1a at t44 zorder 2
    n "Well, I'll be seeing you all later."
    n 1d "I have some things I need to attend to, but once I come back I'll be more vicious than ever before!"
    show natsuki at thide zorder 1
    hide natsuki
    show yuri 1a at t31 zorder 2
    show sayori 1a at t32 zorder 2
    show monika 1a at t33 zorder 2
    "Natsuki then walks confidently out the door."
    "I wonder how much more powerful she'll get."
    show sayori 1q at f32 zorder 3
    s "Today was really fun. We have to try something like this again."
    s "Maybe at my place! You all know where it is, after all."
    show sayori 1q at t32 zorder 2
    mc "Maybe Sayori, maybe."
    "As she made her way toward the door, she put up both hands, waving at the rest of us."
    show sayori 2r at f32 zorder 3
    s "Byyye!!!"
    show sayori at thide zorder 1
    hide sayori
    show yuri 1a at t21 zorder 2
    show monika 1a at t22 zorder 2
    "Sayori doesn't go hopping out like the door like I expected, but she looks alot happier."
    show monika 5a at f22 zorder 3
    m "This has been one interesting year, hasn't it Yuri?"
    show monika 5a at t22 zorder 2
    show yuri 1c at f21 zorder 3
    y "Of course, what with all of us finding each other through our own journeys, carving us to be better people than we were before."
    show yuri 1c at t21 zorder 2
    show monika 1k at f22 zorder 3
    m "Haha."
    m 1a "Yuri, make sure to never stop being as great as you are."
    m "And [player], make sure you love her like no one else in this reality."
    mc "Sure will."
    show monika 1k at thide zorder 1
    hide monika
    show yuri 1a at t11 zorder 2
    "Monika leaves the room, same as she walks in everyday, but she doesn't feel out of reach."
    "Rather, she feels like she's beside me, like we're equals."
    "With Monika out though, that just leaves Yuri and I alone in the room."
    "I get my things ready to walk out of the room, but then I feel a tug at my shirt."
    y 1f "Um, [player]."
    mc "What is it Yuri?"
    y 1s "Well, I was just wondering if, before we leave this place, that we can sit by the wall one more time."
    "I can't help but giggle to myself."
    "Just what does she have in mind?"
    mc "Sure thing Yuri."
    scene cg yuri_against_wall
    "We both adjust ourselves to the wall, taking a seat."
    "Now that I think about it, this is a rather uncomfortable wall."
    "But seeing Yuri so relaxed and happy, I can't help but do anything for her."
    "Our hands intermingled, we lean against each other instead of the wall."
    "She feels warm."
    "I notice that Yuri is holding Portrait of Markov with her other hand."
    y "[player], truth be told, I find it odd a horror book would be the reason I found the one I love."
    mc "I guess it is weird when you put it like that."
    mc "But to be fair, everything feels extraordinary when I'm with you."
    y "Hehe, you have such a way with words."
    "While Yuri rests her head on my shoulder, I notice I have some chocolate in my bag."
    mc "Hey Yuri, I have another chocolate bar if you wanna finish what we started."
    y "I'm sorry, but I'll have to decline."
    y "I have to end it the way my heart wanted it to."
    scene bg black
    with fade
    "Yuri pushes her face towards mine until our mouths connect."
    y "I love you, [player]."
    y "I love you too, Yuri."
    scene end
    with fade
    "Thank you for playing DDLCtVN Yuri Route!"
    return
