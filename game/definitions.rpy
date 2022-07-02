define persistent.demo = False
define persistent.steam = False
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

define b_w = "mod_assets/b_w.png"

# Music
#Mod Music
#bird chirpings
define audio.t12 = "<loop 0>mod_assets/12.mp3"
#wind
define audio.t13 = "<loop 0>mod_assets/13.mp3"
#sunset sounds
define audio.t14 = "<loop 0>mod_assets/14.mp3"
define audio.doorbell = "mod_assets/doorbell.mp3"
#heartbeat
define audio.t15 = "<loop 0>mod_assets/15.mp3"
#rain
define audio.t16 = "<loop 0>mod_assets/16.mp3"

define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)
define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

define audio.t5_monika = "<loop 4.444>bgm/5_monika.ogg"
define audio.t5_sayori = "<loop 4.444>bgm/5_sayori.ogg"
define audio.t5_natsuki = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.t5_yuri = "<loop 4.444>bgm/5_yuri.ogg"
define audio.tbc = "mod_assets/tbc.ogg"
define audio.monikasong = "mod_assets/monikasong.ogg"

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg livingroom = "mod_assets/livingroom.png"
image bg livingroom_evening = "mod_assets/livingroom2.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"
image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

define pickedCorrectYuriGame = False

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0


image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 7a = "mod_assets/sEnd.png"

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "old2/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

image natsuki 6ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsleep2.png")
image natsuki 6bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsleep.png")

image natsuki blaa = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/a.png")
image natsuki blab = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/b.png")
image natsuki blac = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/c.png")
image natsuki blad = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/d.png")
image natsuki blae = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/e.png")
image natsuki blaf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/f.png")
image natsuki blag = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/g.png")
image natsuki blah = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/h.png")
image natsuki blai = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/i.png")
image natsuki blaj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/j.png")
image natsuki blak = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/k.png")
image natsuki blal = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/l.png")
image natsuki blam = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/m.png")
image natsuki blan = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/n.png")
image natsuki blao = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/o.png")
image natsuki blap = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/p.png")
image natsuki blaq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/q.png")
image natsuki blar = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/r.png")
image natsuki blas = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/s.png")
image natsuki blat = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/t.png")
image natsuki blau = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/u.png")
image natsuki blav = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/v.png")
image natsuki blaw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/w.png")
image natsuki blax = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/x.png")
image natsuki blay = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/y.png")
image natsuki blaz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/z.png")

image natsuki bla2a = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2bta.png")
image natsuki bla2b = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2btb.png")
image natsuki bla2c = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2btc.png")
image natsuki bla2d = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2btd.png")
image natsuki bla2e = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2bte.png")
image natsuki bla2f = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2btf.png")
image natsuki bla2g = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2btg.png")
image natsuki bla2h = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2bth.png")
image natsuki bla2i = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/2bti.png")

image natsuki bla1 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "mod_assets/natsleep.png")
image natsuki bla2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "mod_assets/natsleep2.png")

image natsuki 7a = "mod_assets/nEnd.png"

image natsuki 8a = "mod_assets/natsuki/buffsuki.png"


# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y1.png")
image yuri 1by2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y2.png")
image yuri 1by3 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y3.png")
image yuri 1by4 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y4.png")
image yuri 1by5 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y5.png")
image yuri 1by6 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y6.png")
image yuri 1by7 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "yuri/y7.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y1.png")
image yuri 2by2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y2.png")
image yuri 2by3 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y3.png")
image yuri 2by4 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y4.png")
image yuri 2by5 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y5.png")
image yuri 2by6 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y6.png")
image yuri 2by7 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y7.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y1.png")
image yuri 3by2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y2.png")
image yuri 3by3 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y3.png")
image yuri 3by4 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y4.png")
image yuri 3by5 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y5.png")
image yuri 3by6 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y6.png")
image yuri 3by7 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "yuri/y7.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image yuri 7a = "mod_assets/yEnd.png"


image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/a.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/a.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/a.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/a.png")


image monika 1ba = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/a.png")
image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/b.png")
image monika 1bc = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/c.png")
image monika 1bd = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/d.png")
image monika 1be = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/e.png")
image monika 1bf = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/f.png")
image monika 1bg = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/g.png")
image monika 1bh = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/h.png")
image monika 1bi = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/i.png")
image monika 1bj = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/j.png")
image monika 1bk = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/k.png")
image monika 1bl = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/l.png")
image monika 1bm = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/m.png")
image monika 1bn = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/n.png")
image monika 1bo = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/o.png")
image monika 1bp = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/p.png")
image monika 1bq = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/q.png")
image monika 1br = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/r.png")

image monika 2ba = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/a.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/b.png")
image monika 2bc = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/c.png")
image monika 2bd = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/d.png")
image monika 2be = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/e.png")
image monika 2bf = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/f.png")
image monika 2bg = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/g.png")
image monika 2bh = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/h.png")
image monika 2bi = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/i.png")
image monika 2bj = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/j.png")
image monika 2bk = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/k.png")
image monika 2bl = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/l.png")
image monika 2bm = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/m.png")
image monika 2bn = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/n.png")
image monika 2bo = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/o.png")
image monika 2bp = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/p.png")
image monika 2bq = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/q.png")
image monika 2br = im.Composite((960, 960), (0, 0), "mod_assets/1bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/r.png")

image monika 3ba = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/a.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/b.png")
image monika 3bc = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/c.png")
image monika 3bd = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/d.png")
image monika 3be = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/e.png")
image monika 3bf = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/f.png")
image monika 3bg = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/g.png")
image monika 3bh = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/h.png")
image monika 3bi = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/i.png")
image monika 3bj = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/j.png")
image monika 3bk = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/k.png")
image monika 3bl = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/l.png")
image monika 3bm = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/m.png")
image monika 3bn = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/n.png")
image monika 3bo = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/o.png")
image monika 3bp = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/p.png")
image monika 3bq = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/q.png")
image monika 3br = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/1br.png", (0, 0), "monika/r.png")

image monika 4ba = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/a.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/b.png")
image monika 4bc = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/c.png")
image monika 4bd = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/d.png")
image monika 4be = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/e.png")
image monika 4bf = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/f.png")
image monika 4bg = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/g.png")
image monika 4bh = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/h.png")
image monika 4bi = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/i.png")
image monika 4bj = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/j.png")
image monika 4bk = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/k.png")
image monika 4bl = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/l.png")
image monika 4bm = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/m.png")
image monika 4bn = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/n.png")
image monika 4bo = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/o.png")
image monika 4bp = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/p.png")
image monika 4bq = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/q.png")
image monika 4br = im.Composite((960, 960), (0, 0), "mod_assets/2bl.png", (0, 0), "mod_assets/2br.png", (0, 0), "monika/r.png")

image monika 8a = "mod_assets/mEnd.png"


image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

image tbc = "mod_assets/tbc.png"


# Character variables
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

define tbc = DynamicCharacter('tbc', image='tbc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"


# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.

default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.

default poemsread = 0


# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0


# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None

# 2.0 

#Variable
define pickedCorrectYuriGame = False
define sayori_confronted = False

#Sound

# bird chirpings
define audio.t12 = "<loop 0>mod_assets/12.mp3"
#wind
define audio.t13 = "<loop 0>mod_assets/13.mp3"
#sunset sounds
define audio.t14 = "<loop 0>mod_assets/14.mp3"
define audio.doorbell = "mod_assets/doorbell.mp3"
#heartbeat
define audio.t15 = "<loop 0>mod_assets/15.mp3"
define audio.tbc = "mod_assets/tbc.ogg"
define audio.monikasong = "mod_assets/monikasong.ogg"

#Art

#Cafe
image bg cafe = "mod_assets/cafe.png"
image bg cafe_in = "mod_assets/cafe_in.png"

#Theater
image bg theater = "mod_assets/theater_out.png"
image bg theater_in = "mod_assets/theater_in.png"

#Player House
image bg bedroom_dirty = "mod_assets/bedroom_dirty.png"
image bg livingroom_sunset = "mod_assets/livingroom_sunset.png"

#School
image bg school = "mod_assets/school.png"
image bg school courtyard = "mod_assets/courtyard.png" # Wretched Team - Kimagure After

#Road
image bg road = "mod_assets/road.png"
image bg road_sunset = "mod_assets/road_sunset.png"
image bg road_night = "mod_assets/road_night.png"

#Bookstore
image bg central_hub = "mod_assets/central_hub.png"
image bg bookstore = "mod_assets/bookstore.png"
image bg bookstore_sunset = "mod_assets/bookstore_sunset.png"
image bg reading_room = "mod_assets/reading_room.png"

#Restaurant
image bg restaurant_front = "mod_assets/restaurant_front.png"
image bg restaurant = "mod_assets/restaurant.png"

#Yuri's House
image bg yuri_house = "mod_assets/yuri_house.png"
image bg yuri_house_night = "mod_assets/yuri_house_night.png"
image bg yuri_bedroom = "mod_assets/yuri_bedroom.png"
image bg yuri_bedroom_night = "mod_assets/yuri_bedroom_night.png"
image bg yuri_bathroom = "mod_assets/yuri_bathroom.png"

#Hotel
image bg bus = "mod_assets/bus.png"
image bg hotel_outside = "mod_assets/hotel_outside.png"
image bg hotel_room = "mod_assets/hotel_room.png"
image bg hotel_lobby = "mod_assets/hotel_lobby.png"

#Subway
image bg subway_afternoon = "mod_assets/subway_afternoon.png"
image bg subway_night_lights = "mod_assets/subway_night_lights.png"

#Station
image bg station_day = "mod_assets/station_day.png"
image bg station_night = "mod_assets/station_night.png"

#Graveyard
image bg cemetery = "mod_assets/cemetery.png"

#Christmas tree
image bg christmas_tree = "mod_assets/christmastree.png"

image bg ending_e = "mod_assets/natsuki/endings/e.png"
image bg ending_f = "mod_assets/natsuki/endings/f.png"
image bg ending_g = "mod_assets/natsuki/endings/g.png"
image bg ending_h = "mod_assets/natsuki/endings/h.png"

image yuri_note = "mod_assets/yuri_ch1_note.png"
transform noteposition :
    xalign 0.5
    yalign 0.25
image bg black = "mod_assets/black.png"
image bg corner = "mod_assets/corner.png"
image bg bowling_alley = "mod_assets/bowling_alley.png"

image bg sayori_bedroom_daydream = "mod_assets/sayori_bedroom_daydream.png"
image bg park = "mod_assets/park.png"
    #Sayo
        #CG
image sayori_bed = "mod_assets/sayori/cg/bed sayori.png"
image sayori_bed_one_eye = "mod_assets/sayori/cg/sayori bed one eye.png"

        #Pyjama
image sayori pja = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/a.png")
image sayori pjb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/b.png")
image sayori pjc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/c.png")
image sayori pjd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/d.png")
image sayori pje = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/e.png")
image sayori pjf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/f.png")
image sayori pjg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/g.png")
image sayori pjh = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/h.png")
image sayori pji = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/i.png")
image sayori pjj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/j.png")
image sayori pjk = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/k.png")
image sayori pjl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/l.png")
image sayori pjm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/m.png")
image sayori pjn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/n.png")
image sayori pjo = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/o.png")
image sayori pjp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/p.png")
image sayori pjq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/q.png")
image sayori pjr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/r.png")
image sayori pjs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/s.png")
image sayori pjt = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/t.png")
image sayori pju = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/u.png")
image sayori pjv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/v.png")
image sayori pjw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/w.png")
image sayori pjx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/x.png")
image sayori pjy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "sayori/y.png")

        #Jacket
image sayori jaca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/a.png")
image sayori jacb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/b.png")
image sayori jacc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/c.png")
image sayori jacd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/d.png")
image sayori jace = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/e.png")
image sayori jacf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/f.png")
image sayori jacg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/g.png")
image sayori jach = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/h.png")
image sayori jaci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/i.png")
image sayori jacj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/j.png")
image sayori jack = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/k.png")
image sayori jacl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/l.png")
image sayori jacm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/m.png")
image sayori jacn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/n.png")
image sayori jaco = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/o.png")
image sayori jacp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/p.png")
image sayori jacq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/q.png")
image sayori jacr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/r.png")
image sayori jacs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/s.png")
image sayori jact = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/t.png")
image sayori jacu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/u.png")
image sayori jacv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/v.png")
image sayori jacw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/w.png")
image sayori jacx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/x.png")
image sayori jacy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "sayori/y.png")

        #Blanket
image sayori blaa = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/a.png")
image sayori blab = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/b.png")
image sayori blac = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/c.png")
image sayori blad = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/d.png")
image sayori blae = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/e.png")
image sayori blaf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/f.png")
image sayori blag = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/g.png")
image sayori blah = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/h.png")
image sayori blai = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/i.png")
image sayori blaj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/j.png")
image sayori blak = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/k.png")
image sayori blal = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/l.png")
image sayori blam = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/m.png")
image sayori blan = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/n.png")
image sayori blao = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/o.png")
image sayori blap = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/p.png")
image sayori blaq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/q.png")
image sayori blar = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/r.png")
image sayori blas = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/s.png")
image sayori blat = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/t.png")
image sayori blau = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/u.png")
image sayori blav = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/v.png")
image sayori blaw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/w.png")
image sayori blax = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/x.png")
image sayori blay = im.Composite((960, 960), (0, 0), "mod_assets/sayori/blanket/sayoriblanket.png", (0, 0), "sayori/y.png")


    #Natsuki
        #Blanket
image natsuki blaa = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/a.png")
image natsuki blab = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/b.png")
image natsuki blac = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/c.png")
image natsuki blad = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/d.png")
image natsuki blae = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/e.png")
image natsuki blaf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/f.png")
image natsuki blag = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/g.png")
image natsuki blah = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/h.png")
image natsuki blai = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/i.png")
image natsuki blaj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/j.png")
image natsuki blak = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/k.png")
image natsuki blal = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/l.png")
image natsuki blam = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/m.png")
image natsuki blan = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/n.png")
image natsuki blao = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/o.png")
image natsuki blap = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/p.png")
image natsuki blaq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/q.png")
image natsuki blar = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/r.png")
image natsuki blas = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/s.png")
image natsuki blat = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/t.png")
image natsuki blau = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/u.png")
image natsuki blav = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/v.png")
image natsuki blaw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/w.png")
image natsuki blax = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/x.png")
image natsuki blay = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/y.png")
image natsuki blaz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "natsuki/z.png")

image natsuki bla1 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "mod_assets/natsleep.png")
image natsuki bla2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/blanket/natsukiblanket.png", (0, 0), "mod_assets/natsleep2.png")


    #Yuri
        #Cut

# Fresh cut
# Casual
image yuri 3bac2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/a.png")
image yuri 3bbc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/b.png")
image yuri 3bcc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/c.png")
image yuri 3bdc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/d.png")
image yuri 3bec2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/e.png")
image yuri 3bfc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/f.png")
image yuri 3bgc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/g.png")
image yuri 3bhc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/h.png")
image yuri 3bic2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/i.png")
image yuri 3bjc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/j.png")
image yuri 3bkc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/k.png")
image yuri 3blc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/l.png")
image yuri 3bmc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/m.png")
image yuri 3bnc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/n.png")
image yuri 3boc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/o.png")
image yuri 3bpc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/p.png")
image yuri 3bqc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/q.png")
image yuri 3brc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/r.png")
image yuri 3bsc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/s.png")
image yuri 3btc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/t.png")
image yuri 3buc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/u.png")
image yuri 3bvc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/v.png")
image yuri 3bwc2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/w.png")
image yuri 3by1c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y1.png")
image yuri 3by2c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y2.png")
image yuri 3by3c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y3.png")
image yuri 3by4c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y4.png")
image yuri 3by5c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y5.png")
image yuri 3by6c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y6.png")
image yuri 3by7c2 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y7.png")

image yuri 4bac2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/a.png")
image yuri 4bbc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/b.png")
image yuri 4bcc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/c.png")
image yuri 4bdc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/d.png")
image yuri 4bec2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/e.png")
image yuri 4bfc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/f.png")
image yuri 4bgc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/g.png")
image yuri 4bhc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/h.png")
image yuri 4bic2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/i.png")
image yuri 4bjc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/j.png")
image yuri 4bkc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/k.png")
image yuri 4blc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/l.png")
image yuri 4bmc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/m.png")
image yuri 4bnc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/n.png")
image yuri 4boc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/o.png")
image yuri 4bpc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/p.png")
image yuri 4bqc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/q.png")
image yuri 4brc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/r.png")
image yuri 4bsc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/s.png")
image yuri 4btc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/t.png")
image yuri 4buc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/u.png")
image yuri 4bvc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/v.png")
image yuri 4bwc2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/w.png")
image yuri 4by1c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y1.png")
image yuri 4by2c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y2.png")
image yuri 4by3c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y3.png")
image yuri 4by4c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y4.png")
image yuri 4by5c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y5.png")
image yuri 4by6c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y6.png")
image yuri 4by7c2 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcut.png", (0, 0), "yuri/y7.png")

image yuri 5bac2 = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "mod_assets/yuri/cut/3cutb.png")
image yuri 5bbc2 = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "mod_assets/yuri/cut/3cutb.png")
image yuri 5bcc2 = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "mod_assets/yuri/cut/3cutb.png")
image yuri 5bdc2 = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "mod_assets/yuri/cut/3cutb.png")
image yuri 5bec2 = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "mod_assets/yuri/cut/3cutb.png")

# School
image yuri 3ac2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/a.png")
image yuri 3bc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/b.png")
image yuri 3cc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/c.png")
image yuri 3dc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/d.png")
image yuri 3ec2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/e.png")
image yuri 3fc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/f.png")
image yuri 3gc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/g.png")
image yuri 3hc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/h.png")
image yuri 3ic2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/i.png")
image yuri 3jc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/j.png")
image yuri 3kc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/k.png")
image yuri 3lc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/l.png")
image yuri 3mc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/m.png")
image yuri 3nc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/n.png")
image yuri 3oc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/o.png")
image yuri 3pc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/p.png")
image yuri 3qc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/q.png")
image yuri 3rc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/r.png")
image yuri 3sc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/s.png")
image yuri 3tc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/t.png")
image yuri 3uc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/u.png")
image yuri 3vc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/v.png")
image yuri 3wc2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/w.png")
image yuri 3y1c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y1.png")
image yuri 3y2c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y2.png")
image yuri 3y3c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y3.png")
image yuri 3y4c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y4.png")
image yuri 3y5c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y5.png")
image yuri 3y6c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y6.png")
image yuri 3y7c2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y7.png")

image yuri 4ac2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/a.png")
image yuri 4bc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/b.png")
image yuri 4cc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/c.png")
image yuri 4dc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/d.png")
image yuri 4ec2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/e.png")
image yuri 4fc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/f.png")
image yuri 4gc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/g.png")
image yuri 4hc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/h.png")
image yuri 4ic2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/i.png")
image yuri 4jc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/j.png")
image yuri 4kc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/k.png")
image yuri 4lc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/l.png")
image yuri 4mc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/m.png")
image yuri 4nc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/n.png")
image yuri 4oc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/o.png")
image yuri 4pc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/p.png")
image yuri 4qc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/q.png")
image yuri 4rc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/r.png")
image yuri 4sc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/s.png")
image yuri 4tc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/t.png")
image yuri 4uc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/u.png")
image yuri 4vc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/v.png")
image yuri 4wc2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/w.png")
image yuri 4y1c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y1.png")
image yuri 4y2c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y2.png")
image yuri 4y3c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y3.png")
image yuri 4y4c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y4.png")
image yuri 4y5c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y5.png")
image yuri 4y6c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y6.png")
image yuri 4y7c2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/yuri/cut/cut.png", (0, 0), "yuri/y7.png")

image yuri 5ac2 = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "mod_assets/yuri/cut/3cut.png")
image yuri 5bc2 = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "mod_assets/yuri/cut/3cut.png")
image yuri 5cc2 = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "mod_assets/yuri/cut/3cut.png")
image yuri 5dc2 = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "mod_assets/yuri/cut/3cut.png")
image yuri 5ec2 = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "mod_assets/yuri/cut/3cut.png")

# Healed cut
image yuri 3bac1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/a.png")
image yuri 3bbc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/b.png")
image yuri 3bcc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/c.png")
image yuri 3bdc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/d.png")
image yuri 3bec1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/e.png")
image yuri 3bfc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/f.png")
image yuri 3bgc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/g.png")
image yuri 3bhc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/h.png")
image yuri 3bic1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/i.png")
image yuri 3bjc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/j.png")
image yuri 3bkc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/k.png")
image yuri 3blc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/l.png")
image yuri 3bmc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/m.png")
image yuri 3bnc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/n.png")
image yuri 3boc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/o.png")
image yuri 3bpc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/p.png")
image yuri 3bqc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/q.png")
image yuri 3brc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/r.png")
image yuri 3bsc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/s.png")
image yuri 3btc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/t.png")
image yuri 3buc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/u.png")
image yuri 3bvc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/v.png")
image yuri 3bwc1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/w.png")
image yuri 3by1c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y1.png")
image yuri 3by2c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y2.png")
image yuri 3by3c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y3.png")
image yuri 3by4c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y4.png")
image yuri 3by5c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y5.png")
image yuri 3by6c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y6.png")
image yuri 3by7c1 = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y7.png")

image yuri 4bac1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/a.png")
image yuri 4bbc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/b.png")
image yuri 4bcc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/c.png")
image yuri 4bdc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/d.png")
image yuri 4bec1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/e.png")
image yuri 4bfc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/f.png")
image yuri 4bgc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/g.png")
image yuri 4bhc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/h.png")
image yuri 4bic1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/i.png")
image yuri 4bjc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/j.png")
image yuri 4bkc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/k.png")
image yuri 4blc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/l.png")
image yuri 4bmc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/m.png")
image yuri 4bnc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/n.png")
image yuri 4boc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/o.png")
image yuri 4bpc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/p.png")
image yuri 4bqc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/q.png")
image yuri 4brc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/r.png")
image yuri 4bsc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/s.png")
image yuri 4btc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/t.png")
image yuri 4buc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/u.png")
image yuri 4bvc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/v.png")
image yuri 4bwc1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/w.png")
image yuri 4by1c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y1.png")
image yuri 4by2c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y2.png")
image yuri 4by3c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y3.png")
image yuri 4by4c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y4.png")
image yuri 4by5c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y5.png")
image yuri 4by6c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y6.png")
image yuri 4by7c1 = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/yuri/cut/bcuth.png", (0, 0), "yuri/y7.png")

        #Blanket
image yuri blaa = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blab = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blac = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blad = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blae = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blaf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blag = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blah = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blai = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blaj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blak = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blal = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blam = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blan = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blao = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blap = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blaq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blar = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blas = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blat = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blau = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blav = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")
image yuri blaw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/blanket/yuriblanket.png")

        #CG
image cg yuri_in_bed = "mod_assets/yuri/cg/yuri_in_bed.png"
image cg yuri_on_chest = "mod_assets/yuri/cg/yuri_on_chest.png"
image cg yuri_against_wall = "mod_assets/yuri/cg/yuri_against_wall.png"


    #Monika
        #Blanket
image monika blaa = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/a.png")
image monika blab = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/b.png")
image monika blac = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/c.png")
image monika blad = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/d.png")
image monika blae = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/e.png")
image monika blaf = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/f.png")
image monika blag = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/g.png")
image monika blah = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/h.png")
image monika blai = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/i.png")
image monika blaj = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/j.png")
image monika blak = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/k.png")
image monika blal = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/l.png")
image monika blam = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/m.png")
image monika blan = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/n.png")
image monika blao = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/o.png")
image monika blap = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/p.png")
image monika blaq = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/q.png")
image monika blar = im.Composite((960, 960), (0, 0), "mod_assets/monika/blanket/monikablanket.png", (0, 0), "monika/r.png")


# 2.0 Art PLACEHOLDER, HAVE TO BE REPLACE BEFORE RELEASE. WE DON'T HAVE THE RIGHTS ON THOSE ONE

# Sayo 
# Winking
image sayori 1wink = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 2wink = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 3wink = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 4wink = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")

image sayori 1bwink = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 2bwink = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 3bwink = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 4bwink = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")

image sayori 1fwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 2fwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 3fwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 4fwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")

image sayori pjwink = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pj/pj.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori jacwink = im.Composite((960, 960), (0, 0), "mod_assets/sayori/jacket/jac.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")

image sayori 1uwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 2uwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 3uwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")
image sayori 4uwink = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "mod_assets/placeholder/sayori/wink.png")

# Casual special pose
image sayori 5ba = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/5ba.png")
image sayori 5bb = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/5bb.png")
image sayori 5bc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/5bc.png")
image sayori 5bd = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/5bd.png")

# Formal
image sayori 1fa = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/a.png")
image sayori 1fb = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/b.png")
image sayori 1fc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/c.png")
image sayori 1fd = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/d.png")
image sayori 1fe = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/e.png")
image sayori 1ff = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/f.png")
image sayori 1fg = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/g.png")
image sayori 1fh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/h.png")
image sayori 1fi = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/i.png")
image sayori 1fj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/j.png")
image sayori 1fk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/k.png")
image sayori 1fl = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/l.png")
image sayori 1fm = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/m.png")
image sayori 1fn = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/n.png")
image sayori 1fo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/o.png")
image sayori 1fp = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/p.png")
image sayori 1fq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/q.png")
image sayori 1fr = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/r.png")
image sayori 1fs = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/s.png")
image sayori 1ft = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/t.png")
image sayori 1fu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/u.png")
image sayori 1fv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/v.png")
image sayori 1fw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/w.png")
image sayori 1fx = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/x.png")
image sayori 1fy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/y.png")

image sayori 2fa = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/a.png")
image sayori 2fb = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/b.png")
image sayori 2fc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/c.png")
image sayori 2fd = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/d.png")
image sayori 2fe = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/e.png")
image sayori 2ff = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/f.png")
image sayori 2fg = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/g.png")
image sayori 2fh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/h.png")
image sayori 2fi = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/i.png")
image sayori 2fj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/j.png")
image sayori 2fk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/k.png")
image sayori 2fl = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/l.png")
image sayori 2fm = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/m.png")
image sayori 2fn = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/n.png")
image sayori 2fo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/o.png")
image sayori 2fp = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/p.png")
image sayori 2fq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/q.png")
image sayori 2fr = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/r.png")
image sayori 2fs = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/s.png")
image sayori 2ft = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/t.png")
image sayori 2fu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/u.png")
image sayori 2fv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/v.png")
image sayori 2fw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/w.png")
image sayori 2fx = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/x.png")
image sayori 2fy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/1l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/y.png")

image sayori 3fa = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/a.png")
image sayori 3fb = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/b.png")
image sayori 3fc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/c.png")
image sayori 3fd = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/d.png")
image sayori 3fe = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/e.png")
image sayori 3ff = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/f.png")
image sayori 3fg = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/g.png")
image sayori 3fh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/h.png")
image sayori 3fi = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/i.png")
image sayori 3fj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/j.png")
image sayori 3fk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/k.png")
image sayori 3fl = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/l.png")
image sayori 3fm = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/m.png")
image sayori 3fn = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/n.png")
image sayori 3fo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/o.png")
image sayori 3fp = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/p.png")
image sayori 3fq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/q.png")
image sayori 3fr = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/r.png")
image sayori 3fs = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/s.png")
image sayori 3ft = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/t.png")
image sayori 3fu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/u.png")
image sayori 3fv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/v.png")
image sayori 3fw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/w.png")
image sayori 3fx = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/x.png")
image sayori 3fy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/1r.png", (0, 0), "sayori/y.png")

image sayori 4fa = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/a.png")
image sayori 4fb = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/b.png")
image sayori 4fc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/c.png")
image sayori 4fd = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/d.png")
image sayori 4fe = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/e.png")
image sayori 4ff = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/f.png")
image sayori 4fg = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/g.png")
image sayori 4fh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/h.png")
image sayori 4fi = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/i.png")
image sayori 4fj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/j.png")
image sayori 4fk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/k.png")
image sayori 4fl = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/l.png")
image sayori 4fm = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/m.png")
image sayori 4fn = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/n.png")
image sayori 4fo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/o.png")
image sayori 4fp = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/p.png")
image sayori 4fq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/q.png")
image sayori 4fr = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/r.png")
image sayori 4fs = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/s.png")
image sayori 4ft = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/t.png")
image sayori 4fu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/u.png")
image sayori 4fv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/v.png")
image sayori 4fw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/w.png")
image sayori 4fx = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2r.png", (0, 0), "sayori/x.png")
image sayori 4fy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/formal/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2br.png", (0, 0), "sayori/y.png")

# Underwear
image sayori 1ua = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/a.png")
image sayori 1ub = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/b.png")
image sayori 1uc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/c.png")
image sayori 1ud = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/d.png")
image sayori 1ue = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/e.png")
image sayori 1uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/f.png")
image sayori 1ug = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/g.png")
image sayori 1uh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/h.png")
image sayori 1ui = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/i.png")
image sayori 1uj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/j.png")
image sayori 1uk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/k.png")
image sayori 1ul = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/l.png")
image sayori 1um = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/m.png")
image sayori 1un = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/n.png")
image sayori 1uo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/o.png")
image sayori 1up = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/p.png")
image sayori 1uq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/q.png")
image sayori 1ur = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/r.png")
image sayori 1us = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/s.png")
image sayori 1ut = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/t.png")
image sayori 1uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/u.png")
image sayori 1uv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/v.png")
image sayori 1uw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/w.png")
image sayori 1ux = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/x.png")
image sayori 1uy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/y.png")

image sayori 2ua = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/a.png")
image sayori 2ub = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/b.png")
image sayori 2uc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/c.png")
image sayori 2ud = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/d.png")
image sayori 2ue = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/e.png")
image sayori 2uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/f.png")
image sayori 2ug = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/g.png")
image sayori 2uh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/h.png")
image sayori 2ui = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/i.png")
image sayori 2uj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/j.png")
image sayori 2uk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/k.png")
image sayori 2ul = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/l.png")
image sayori 2um = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/m.png")
image sayori 2un = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/n.png")
image sayori 2uo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/o.png")
image sayori 2up = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/p.png")
image sayori 2uq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/q.png")
image sayori 2ur = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/r.png")
image sayori 2us = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/s.png")
image sayori 2ut = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/t.png")
image sayori 2uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/u.png")
image sayori 2uv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/v.png")
image sayori 2uw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/w.png")
image sayori 2ux = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/x.png")
image sayori 2uy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/1l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/y.png")

image sayori 3ua = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/a.png")
image sayori 3ub = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/b.png")
image sayori 3uc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/c.png")
image sayori 3ud = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/d.png")
image sayori 3ue = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/e.png")
image sayori 3uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/f.png")
image sayori 3ug = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/g.png")
image sayori 3uh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/h.png")
image sayori 3ui = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/i.png")
image sayori 3uj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/j.png")
image sayori 3uk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/k.png")
image sayori 3ul = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/l.png")
image sayori 3um = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/m.png")
image sayori 3un = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/n.png")
image sayori 3uo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/o.png")
image sayori 3up = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/p.png")
image sayori 3uq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/q.png")
image sayori 3ur = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/r.png")
image sayori 3us = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/s.png")
image sayori 3ut = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/t.png")
image sayori 3uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/u.png")
image sayori 3uv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/v.png")
image sayori 3uw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/w.png")
image sayori 3ux = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/x.png")
image sayori 3uy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/1r.png", (0, 0), "sayori/y.png")

image sayori 4ua = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/a.png")
image sayori 4ub = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/b.png")
image sayori 4uc = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/c.png")
image sayori 4ud = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/d.png")
image sayori 4ue = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/e.png")
image sayori 4uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/f.png")
image sayori 4ug = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/g.png")
image sayori 4uh = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/h.png")
image sayori 4ui = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/i.png")
image sayori 4uj = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/j.png")
image sayori 4uk = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/k.png")
image sayori 4ul = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/l.png")
image sayori 4um = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/m.png")
image sayori 4un = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/n.png")
image sayori 4uo = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/o.png")
image sayori 4up = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/p.png")
image sayori 4uq = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/q.png")
image sayori 4ur = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/r.png")
image sayori 4us = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/s.png")
image sayori 4ut = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/t.png")
image sayori 4uu = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/u.png")
image sayori 4uv = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/v.png")
image sayori 4uw = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/w.png")
image sayori 4ux = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/undies/2r.png", (0, 0), "sayori/x.png")
image sayori 4uy = im.Composite((960, 960), (0, 0), "mod_assets/placeholder/sayori/undies/2l.png", (0, 0), "mod_assets/placeholder/sayori/formal/2br.png", (0, 0), "sayori/y.png")


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc