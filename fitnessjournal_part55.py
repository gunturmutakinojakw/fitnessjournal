# === Stage 55: Add a setting to disable colorized output ===
# Project: FitnessJournal
def colorize(text, color):
    if color is None:
        return text
    if not sys.stdout.isatty():
        return text
    codes = {
        'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
        'magenta': 35, 'cyan': 36, 'white': 37, 'gray': 90,
    }
    code = codes.get(color)
    if code is None:
        return text
    return '\033[{}m{}\033[0m'.format(code, text)


SETTING_DISABLE_COLOR = False


def set_disable_color(enabled):
    global SETTING_DISABLE_COLOR
    SETTING_DISABLE_COLOR = enabled


def print_reported(value, color='green'):
    if SETTING_DISABLE_COLOR:
        print(value)
    else:
        print(colorize(value, color))


def print_header(title, color='cyan'):
    if SETTING_DISABLE_COLOR:
        print(title)
    else:
        print(colorize(title.upper(), color))
