
sha = "hai how are you doing buddy"

def strconvertion():
    le = len(sha)
    reh = sha[4:8][::-1]
    rer = sha[8:12][::-1]
    rey = sha[12:16][::-1]
    red = sha[16:22][::-1]
    Mandatory = ['hai',' buddy']
    new_string = Mandatory[0] + reh + rer + rey + red
    print(new_string+Mandatory[1])
strconvertion()
