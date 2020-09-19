# Brought to you by st4rchild with the help of Hanz Petrov @ http://remotescripts.blogspot.com
# Avoid using tabs for indentation, use spaces.

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = -1 #offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 1 #Channel assignment for all mapped buttons/pads; valid range is 0 to 15 ; 0=1, 1=2 etc.
SHIFTBANKCHANNEL = 3 #Channel assignment for all mapped side buttons; default is ch.4 (3) from MF Utility
MESSAGETYPE = 1 #Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
        #When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.

# General
PLAY = -1 #Global play
STOP = -1 #Global stop
REC = -1 #Global record
TAPTEMPO = -1 #Tap tempo
NUDGEUP = -1 #Tempo Nudge Up
NUDGEDOWN = -1 #Tempo Nudge Down
UNDO = 15 #Undo
REDO = -1 #Redo
LOOP = -1 #Loop on/off
PUNCHIN = -1 #Punch in
PUNCHOUT = -1 #Punch out
OVERDUB = -1 #Overdub on/off
METRONOME = -1 #Metronome on/off
RECQUANT = -1 #Record quantization on/off
DETAILVIEW = -1 #Detail view switch
CLIPTRACKVIEW = 21 #Clip/Track view switch

# Device Control
DEVICELOCK = -1 #Device Lock (lock "blue hand")
DEVICEONOFF = 18 #Device on/off
DEVICENAVLEFT = 14 #Device nav left
DEVICENAVRIGHT = 17 #Device nav right
DEVICEBANKNAVLEFT = 26 #Device bank nav left for standard btns
DEVICEBANKNAVRIGHT = 27 #Device bank nav right
# DEVICEBANKNAVLEFT = 14 #Device bank nav left for side btns/shift bank
# DEVICEBANKNAVRIGHT = 17 #Device bank nav right
DEVICEBANK = (-1, #Bank 1 #All 8 banks must be assigned to positive values in order for bank selection to work
              -1, #Bank 2
              -1, #Bank 3
              -1, #Bank 4 - Shared with MasterVol value
              -1, #Bank 5
              -1, #Bank 6
              -1, #Bank 7
              -1, #Bank 8
              )

# Arrangement View Controls
SEEKFWD = -1 #Seek forward
SEEKRWD = -1 #Seek rewind

# Session Navigation (aka "red box")
SESSIONLEFT = 8 #Session left
SESSIONRIGHT = 11 #Session right
SESSIONUP = -1 #Session up
SESSIONDOWN = -1 #Session down
ZOOMUP = -1 #Session Zoom up
ZOOMDOWN = -1 #Session Zoom down
ZOOMLEFT = -1 #Session Zoom left
ZOOMRIGHT = -1 #Session Zoom right

# Track Navigation
TRACKLEFT = -1 #Track left
TRACKRIGHT = -1 #Track right

# Scene Navigation
SCENEUP = -1 #Scene down
SCENEDN = -1 #Scene up

# Scene Launch
SELSCENELAUNCH = -1 #Selected scene launch
SCENELAUNCH = (-1, #Scene 1 Launch
               -1, #Scene 2
               -1, #Scene 3
               -1, #Scene 4
               )

# Clip Launch / Stop
SELCLIPLAUNCH = -1 #Selected clip launch
STOPALLCLIPS = -1 #Stop all clips

# 4x4 Matrix note assignments
# Track no.:     1   2   3   4 
CLIPNOTEMAP = ((-1, -1, -1, -1), #Row 1
               (-1, -1, -1, -1), #Row 2
               (-1, -1, -1, -1), #Row 3
               (-1, -1, -1, -1), #Row 4
               )

# Track Control
MASTERSEL = -1 #Master track select
TRACKSTOP = (4, #Track 1 Clip Stop
             5, #Track 2
             6, #Track 3
             7, #Track 4
             )
TRACKSEL = (28, #Track 1 Select
            29, #Track 2
            30, #Track 3
            31, #Track 4
            )
TRACKMUTE = (12, #Track 1 On/Off
             13, #Track 2
             14, #Track 3
             15, #Track 4
             )
TRACKSOLO = (8, #Track 1 Solo
             9, #Track 2
             10, #Track 3
             11, #Track 4
             )
TRACKREC = (-1, #Track 1 Record
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            )


# Pad Translations for Drum Rack

PADCHANNEL = 0 # MIDI channel for Drum Rack notes
DRUM_PADS = (-1, -1, -1, -1, # MIDI note numbers for 4 x 4 Drum Rack
             -1, -1, -1, -1, # Mapping will be disabled if any notes are set to -1
             -1, -1, -1, -1, # Notes will be "swallowed" if already mapped elsewhere
             -1, -1, -1, -1,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored

SLIDERCHANNEL = 0 #Channel assignment for all mapped CCs; valid range is 0 to 15
ENCODERSHIFTCHANNEL = 4 #Channel assignment for 'shift encoder knob' CCs; default is ch.5 (4) from MF Utility
TEMPO_TOP = 207.0 # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 80.0 # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1 #Tempo control CC assignment; control range is set above
MASTERVOLUME = 3 #Master track volume
CUELEVEL = -1 #Cue level control
CROSSFADER = -1 #Crossfader control

TRACKVOL = (12, #Track 1 Volume
            13, #Track 2
            14, #Track 3
            15, #Track 4
            )
TRACKPAN = (-1, #Track 1 Pan
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            )
TRACKSENDA = (0, #Track 1 Send A
              1, #Track 2
              2, #Track 3
              3, #Track 4
              )
TRACKSENDB = (4, #Track 1 Send B
              5, #Track 2
              6, #Track 3
              7, #Track 4
              )
TRACKSENDC = (8, #Track 1 Send C
              9, #Track 2
              10, #Track 3
              11, #Track 4
              )
PARAMCONTROL = (16, #Param 1 #All 8 params must be assigned to positive values in order for param control to work
                17, #Param 2
                18, #Param 3
                19, #Param 4
                20, #Param 5
                21, #Param 6
                22, #Param 7
                23, #Param 8
                24, #Param 9
                25, #Param 10
                26, #Param 11
                27, #Param 12
                28, #Param 9
                29, #Param 10
                30, #Param 11
                31, #Param 12
                )
