# Персонажи
define D = Character('Даня', color="#72f1e7", what_prefix="\"", what_suffix="\"")
define s = Character('Саша', color="#f1d372", image='sn', what_prefix="\"", what_suffix="\"")
define y = Character('Яна', color="#f18b72", image='y', what_prefix="\"", what_suffix="\"")
define a = Character('Аня', color="#e772f1", image='a', what_prefix="\"", what_suffix="\"")
define nv = Character(None, kind=nvl)

# Музыка и звуки
define audio.traffic = "music/traffic_sounds.mp3"
define audio.initialize = "sound/initialize.mp3"
define audio.rubik = "sound/rubik.mp3"
define audio.rain = "music/rain.mp3"
define audio.tea0 = "sound/tea0.mp3"
define audio.tea1 = "sound/tea1.mp3"
define audio.keys = "sound/keys.mp3"
define audio.door = "sound/door.mp3"

# Переменные
define milkOolong = 0
define yanaPoints = 0
define coldPoints = 0
define mindPoints = 0
define event0 = False
define event1 = False

init:
    $ left2 = Position(xalign=-1.1, yalign=1.1)
    $ right2 = Position(xalign=1.5, yalign=1.1)