label Natsuki2:
    $ n_karma = 0
    $ y_name = "Yuri"
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ m_name = "Monika"

#For definitions file: Natsuki asset references
#Mod assets: BGs
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

#Cafe
#image bg cafe = "mod_assets/cafe.png"
#image bg cafe_in = "mod_assets/cafe_in.png"

#Movie Theater
#image bg theater = "mod_assets/theater_out.png"
#image bg theater_in = "mod_assets/theater_in.png"

#Carnival
#image bg carnival = "mod_assets/carnival.png"

#Mod Assets: Music
#bird chirpings
#define audio.t12 = "<loop 0>mod_assets/12.mp3"

#Scene 1:
    scene black
    play music t12
    "It's morning."
    "Pale, impossibly bright sunlight filters into my room between the blinds and directly onto my shut eyes. Even so, it manages to wake me up."
    mc "Ngh..."
    scene bg bedroom
    with dissolve_scene_full
    "I open my eyes, wincing as the light fills my vision. After the intial pain fades, I try to sit up, but fail."
    "Looking to my left, I find Natsuki lying beside me. Her arms wrapped around my midriff and my arm is underneath her."
    "I have long since lost any feeling in the limb, but I barely notice as I watch Natsuki."
    "Her eyes are closed and her mouth is slightly parted as she breathes slowly and evenly."
    "She looks so peaceful. And, well... {w=0.25} cute of course."
    "..."
    "And naked."
    "I don't mean to gawk at her like this. It's just... {w=0.5} she looks so innocent and pure that I can't bring myself to lookk away."
    "I love her so much."
    "Another minute passes and then, Natsuki begins to stir and mumbles something incoherently."
    n "Mmm... [player]?"
    "I hesitate."
    mc "Good morning, Natsuki."
    n "How long have you been awake?"
    mc "A couple of minutes, actually."
    "She sits up and looks at me with a somewhat annoyed expression. Whether because of me or just being woken up isn't clear."
    n "Were you watching me sleep?"
    mc "I, uh... {w=0.25} Y-yes? Sorta?"
    n "That's creepy, [player]."
    "I start to defend myself, but before I can even get a word out, she cuts me off."
    n "I'm teasing. God, you're easy."
    "I frown. It's too early for jokes."
    "Or much of anything else really."
    n "What time is it?"
    mc "5:35 a.m."
    mc "Don't worry, we've got some time before school."
    n "So breakfast then?"
    mc "Sounds good to me. I'm not sure what I have, thought."
    "Natsuki grins at me as if I had just challenged her ability to make something delicious from scraps."
    n "Trust me, you'll love whatever I whip up."
    n "You'd better, anyways, or I won't make breakfast for you ever again."
    mc "Fair enough. But we should probably get dressed first, right?"
    n "Well, duh."

    scene bg kitchen
    with wiperight
    stop music

    "Turns out I had more than I thought. Bread, eggs, cinnamon, butter, flour, and a few other things."
    "Natsuki really outdid herself."
    "I tried to help, of course. But since I'm not really much of a cook, all I really did was end up making a mess. Oh well, at least one of us will clean it up later"
    "Right now, I've got a massive plate with two huge slices of french toast, scrambled eggs, and hash browns on it. And right next to the plate, I have a large glass of fresh orange juice."
    "Natsuki has a nearly identical plate as well, on the other side of the table."
    "I don't think I've eaten this well since... well, ever really."
    show natsuki 4y at t11 zorder 2
    n 4y "Don't just stare at it. Eat it, dork."
    show natsuki 2j
    "Natsuki's words snap me bnack to the present and I meet her eyes. She hasn't eaten any of hers yet either."
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
    

    scene end
    with fade
    "Thank you for playing DDLCtVN Natsuki Route!"
    return