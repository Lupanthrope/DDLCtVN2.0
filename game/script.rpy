label start:
    scene black
    $ quick_menu = True

    # $ chapter = 0
    # call ch0_main from _call_ch0_main

    "DDLCtVN is a mod that begins by playing through nearly the entirity of the first act."
    "Would you like to skip directly to the new content?"
    
    menu:
        "No, let me play though act one.":
            call ch0_main from _call_ch0_main
        "Yes, skip me to where I choose my route.":
            call newcontent from _call_newcontent
            jump day4
        "Skip me to the new content for 2.0.":
            menu:
                "Please, select a character."
                "Sayori":
                    call sayoriroute2 from _call_Sayori2
                "Natsuki":
                    call Natsuki2 from _call_Natsuki2
                "Yuri":
                    call Yuri2 from _call_Yuri2      
                "Monika":
                    call Monika2 from _call_Monika2
            return

    call poem from _call_poem_1


    $ chapter = 1
    call ch1_main from _call_ch1_main
    call poemresponse_start from _call_poemresponse_start
    call ch1_end from _call_ch1_end


    call poem from _call_poem_2


    $ chapter = 2
    call ch2_main from _call_ch2_main
    call poemresponse_start from _call_poemresponse_start_1
    call ch2_end from _call_ch2_end


    call poem from _call_poem_3


    $ chapter = 3
    call ch3_edited from _call_ch3_edited
    call poemresponse_start from _call_poemresponse_start_2
    call ch3_end from _call_ch3_end


    label day4:
    $ chapter = 4
    call ch4_main from _call_ch4_main

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
