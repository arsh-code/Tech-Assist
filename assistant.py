import os

while True:
    print("How can I help you ? ", end='')
    p = input().lower()

    if ("run" in p) or ("open" in p) or ("start" in p):

        if ("google" in p) or ("chrome" in p) or ("browser" in p):
            os.system("start chrome")

        elif ("shell" in p):
            os.system("start powershell")

        elif ("cmd" in p) or ("command" in p) or ("prompt" in p) or ("terminal" in p):
            os.system("start cmd")

        elif ("python" in p):
            os.system("start python")

        elif ("media" in p) or ("wmplayer" in p) or ("player" in p):
            os.system("start wmplayer")

        elif ("note" in p) or ("pad" in p) or ("text" in p):
            os.system("start notepad")

        elif ("word" in p) or ("doc" in p):
            os.system("start winword")

        elif (("power" in p) and ("point" in p)) or ("ppt" in p) or ("slide" in p):
            os.system("start powerpnt")

        elif ("excel" in p) or ("sheet" in p) or ("spread" in p):
            os.system("start excel")

        elif ("outlook" in p) or ("mail" in p):
            os.system("start outlook")

        elif ("task" in p) or ("manager" in p):
            os.system("start taskmgr")

        elif ("vlc" in p):
            os.system("start vlc")

        elif ("fire" in p) and ("fox" in p):
            os.system("start firefox")

        elif ("control" in p) or ("panel" in p):
            os.system("start /MAX control")

        elif ("code" in p) or ("editor" in p) or (("visual" in p) and ("studio" in p)):
            os.system("start code")

        elif ("opera" in p):
            os.system("start opera")

        elif ("reader" in p) or ("acrobat" in p) or ("pdf" in p):
            os.system("start acroRd32")

        elif ("snip" in p) or (("screen" in p) and ("capture" in p) or ("shot" in p) or ("print" in p)):
            os.system("start snippingTool")

        elif ("sticky" in p) or ("remind" in p):
            os.system("start StikyNot")

        elif ("clean" in p):
            os.system("start cleanmgr")

        elif ("perfmon" in p) or ("mmc" in p) or (("perf" in p) and ("monitor" in p)):
            os.system("start perfmon")

        elif ("record" in p):
            os.system("start SoundRecorder")

        else:
            print("I cant do that. Please try something else")

    elif("terminate" in p) or ("stop" in p) or ("end" in p) or ("close" in p) or ("exit" in p) or ("quit" in p):
        break

    else:
        print("I cant do that. Please try something else")
