TBNAME_PROJECTS = 'projects'
TBNAME_COLORFULNESS = 'colorfulness'
PARAMS_PROJECTS = {
    'projecttitle': 'ProjectTitle',
    'videotitle': 'VideoTitle',
    'videopath': 'VideoPath'
}

PARAMS_COLORFULNESS = {
    'imgcolor': 'imgcolor',
    'meancolor': 'meancolor',
    'stdcolor': 'stdcolor',
    'meanadj': 'meanadj',
    'stdadj': 'stdadj',
    'meanadjabs': 'meanadjabs',
    'stdadjabs': 'stdadjabs'
}


def value_gen(length):
    if length == 1:
        return ('?')
    elif length == 2:
        return ('?', '?')
    elif length == 3:
        return ('?', '?', '?')
    elif length == 4:
        return ('?', '?', '?', '?')
    elif length == 5:
        return ('?', '?', '?', '?', '?')
    elif length == 6:
        return ('?', '?', '?', '?', '?', '?')
    elif length == 7:
        return ('?', '?', '?', '?', '?', '?', '?')
    elif length == 8:
        return ('?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 9:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 10:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 11:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 12:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 13:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 14:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 15:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 16:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 17:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 18:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 19:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 20:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
