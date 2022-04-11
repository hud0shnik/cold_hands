﻿# Персонажи
define D = Character('Даня', color="#72f1e7")
define y = Character('Яна', color="#f18b72")
define nv = Character(None, kind=nvl)

# Музыка и звуки
define audio.initialize = "sound/initialize.mp3"
define audio.rain = "music/rain.mp3"
define audio.tea0 = "sound/tea0.mp3"
define audio.tea1 = "sound/tea1.mp3"
define audio.keys = "sound/keys.mp3"
define audio.door = "sound/door.mp3"

# Переменные 
define milkOolong = False
define yanaPoints = 0
define guitarPoints = 0
define coldPoints = 0
define crazyPoints = 0

# Начало
label start:

    scene bg void
    stop music fadeout 4.0

    "Осень - моё любимое время года. Жалко, что не могу как раньше наслаждаться видом оранжевого леса из окна, но, как я люблю говорить: \"У всего есть плюсы и минусы\"."
    "В последнее время я начал больше времени проводить с самим собой наедине. От этого грустных мыслей не убавилось."

    menu:
        "Раньше от плохого настроения мне помогала гитара, может стоит попробовать?"

        "От одного рифа хуже не станет":    
            play sound initialize
            $ guitarPoints = 1
            "Кое-как нащупываю первый лад, и ..."
            stop sound fadeout 0.5
            "Нет, тут даже гитара не поможет."

        "Не сегодня, не сегодня":
            "Я медленно откладываю гитару на диван."
            pass
    
    "В моменты, когда человеку скучно и грустно многие делают весьма страшные вещи. Надо пройтись."
    "Сегодня Яна работает, пойти на улицу не с кем, поэтому пройтись я могу лишь на кухню, хех."
    
    "Моя любовь к чаю никуда не делась, так что сейчас самое время пропустить чашечку. Хотя странно наверное называть \"чашечкой\" кружку 0.5"
    
    menu:
        "Какой же улун я выберу сегодня?"
        "Да Хун Пао":
            "Большой Красный Халат. Достаточно кинуть пару листов в кружку и получишь легкую шоколадную нотку. Не могу представить свою жизнь без него."
        "Цзинь Сюань":
            $ milkOolong = True
            "Молочный улун. Достаточно кинуть пару листов в кружку и получишь лёгкое молочное послевкусие. Может стоило купить пару килограмм вместо одного пакета?"
    
    play sound tea0
    "Я наливаю воду в чайник и включаю его. За прошедшие 4 месяца я неплохо научился ориентироваться в квартире."
    "И резко полюбил порядок. Потому что искать полчаса кружку - не круто. Можно сказать, что я построил свою систему координат или что-то подобное."
    
    if milkOolong:
        "Я достаю кружку, бросаю в неё пару скрученных листьев. Даже сейчас я начинаю слышать лёгкий молочный запах. Кладу руку на чайник - так легче мерить температуру."
    else:
        "Я достаю кружку, бросаю в неё пару продольно скрученных листьев, кладу руку на чайник - так легче мерить температуру."
    stop sound fadeout 1
    
    play sound tea1
    "Осталось залить листья. Отмеряю уровень воды в кружке с помощью мизинца. Улун готов."
    stop sound fadeout 1
    
    "Теперь нужно аккуратно вернуться в свою комнату. Хотя если пролью немного по пути, ничего страшного не произойдет. Я перестал портить чай сахаром ещё в средней школе."
    "Медленно ставлю кружку на табуретку рядом с кроватью. Так как я не перемешал улун, ему нужно дать время завариться. Ложусь на мягкую, но скрипучую кровать."
    "А ведь и правда, раньше я проводил намного меньше времени наедине с самим собой. Не знаю хорошо это или плохо."
    
    play sound keys
    "Звук ключей. Похоже в этот раз мне не придется коротать остаток дня в беседах с самим собой."
    stop sound fadeout 1 
    
    play sound door
    "По осторожному звуку открытия двери я понимаю, что это Яна. Но сейчас ведь только обед."
    stop sound fadeout 1 

    y "Уже проснулся?"
    D "Сегодня решил встать пораньше. Ты разве не должна сейчас работать?"
    y "Из-за ливня торговый центр немного затопило, и меня отправили домой."
    D  "А в такой ситуации разве не должны наоборот выдавать сотрудникам вёдра и швабры?"
    y "Дань, я же не уборщицей или охранником работаю. Хозяйка сказала, что на сегодня \"Шалфей\" закрывается."
    y "Эх, а так хотелось по полчаса объяснять, что бомбочки для ванной могут стоить больше ста рублей."
    D  "Я уж думал, что ты тоже полюбила дождь. Ну, раз у тебя сегодня выходной, сгоняешь за эклерами?"
    y "Конечно сгоняю! В такую прекрасную погоду так и хочется пройтись до пекарни!"
    D  "Ну ладно-ладно, в холодильнике вроде осталась ещё парочка."

    "Ливень похоже и вправду сильный. Эх, сейчас бы погулять..."
    menu:
        "Может попросить Яну со мной выйти?"
        "Не уверен, что это сработает, но попробовать стоит":
            D "Не хочешь пройтись?"
            y "Дань, ну не в такую погоду же. Там даже зонтик не поможет. Если просвежиться хочешь, иди на балконе постой."
            play sound door
            "Результат довольно предсказуем. Я открываю дверь балкона, и..."
            play music rain
            "Да, ливень действительно хороший."
            "Раньше я очень любил стоять на балконе, и смотреть на прохожих. Мог так часами проводить время."
            "Балкон был для меня как большой террариум. Сутра люди торопились на работу, а вечером бежали домой. Но те времена прошли. Теперь балкон для меня - просто источник белого шума."
            "Ну, по крайней мере, лучше, чем ничего. Звуки дождя расслабляют. Хотя я и так не очень-то обеспокоенный или нервный."
            "Теперь моя жизнь вообще лишена каких-либо стрессоров. На работу не надо, из вуза я отчислился, в армию по понятным причинам меня не заберут. Остаётся только жить жизнь."
            "Грустно, конечно, быть обузой для родителей. Обычно после 18ти люди съезжают от родни. Но в моём случае наоборот. Они оставили мне квартиру на моё девятнадцатилетие."
            "Теперь из-за меня они вынуждены присылать каждый месяц деньги Яне на моё содержание. Я всё ещё не привык к такому, и похоже не привыкну."
            "Хотя Яна довольна. Она снимает у меня комнату в обмен за уход. Я и непротив, тем более она убирается по выходным и иногда готовит."
            "С первого взгляда может показаться, что это не жизнь, а мечта: собственная квартира, в соседней комнате живет девушка, не нужно работать. Но как я люблю говорить: "
            "\"У всего есть плюсы и минусы\""
            $ coldPoints = 1
            stop music
            play sound door
        "Нет, тут у меня нету шансов":
            pass

    "Слышу звуки кипящей воды в кастрюле. Ладно, что-то есть захотелось. Пойду на кухню."

    play sound door
    y "Ну как там на улице?"
    D "Прекрасно, жалко кое-кто не захотел пойти погулять."
    y "Да ладно тебе, меня чуть не утопило по дороге. Есть будешь?"
    D "Ммм, пельмени, оригинально."
    y "Ну извини, из продуктов я могла только бутерброды сделать, и то без хлеба."
    "Я сажусь за стол. Пытаюсь найти руками тарелку и вилку, но Яна меня опережает и направляет мои руки прямо к ним. Не самая удобная еда, я бы предпочёл бутерброды или суп."
    D "Завтра у нас что?"
    y "Суббота. Если ты собрался за покупками пойти, то давай сутра сразу? У меня завтра кое-какие дела."
    D "Утром так утром."
    "Пельмени то и дело пытаются выскользнуть, но я ловко натыкаю их вилкой. Начинаю привыкать к такой форме потребления пищи." 
    D "А что за дела? Не посвятишь?"
    y "Опять собес. Хоть начальница в Шалфее и добрая, но зарплата меня всё ещё не устраивает. Да и ехать долго."
    D "Дай угадаю, хочешь устроиться в аптеку? А, хотя нет, там платят ещё меньше, тогда ставлю на магазин для хобби."
    y "Мимо, у меня собес в пекарню."
    D "Я тебя расстрою, но там платят явно меньше."
    y "Продавцам да, а вот менеджерам..."
    D "А с каких пор ты стала дипломированным менеджером?"
    y "А ты знаешь кто владелец этой пекарни?"
    D "Понятия не имею."
    y "Ну тогда не буду сильно грузить тебя подробностями. Просто встретила её в зале, и мы так разговорились, что она пригласила меня на собес."
    y "Ну как собес, она уже сказала, что это будет скорее знакомство с остальным персоналом и обсуждение графика и тому подобного."
    D "Интересный метод вербовки сотрудников. Ну и как думаешь, справишься? Должность не самая лёгкая."
    y "Ну с \"Менеджером\" я немного перегнула. Тайтл немного другой. В обязанности выходит контроль поставок и общение с посетителями, ну и по мелочи ещё."
    D "А что по зарплате?"
    y "Чуть больше прежней, но ехать никуда не надо, а это существенно экономит деньги."
    y "Интересно узнать твоё мнение по этому поводу."
    "Зная Яну, могу сказать, что менеджер из неё такой же, как из меня кинокритик. Хотя недавно она проходила какие-то курсы. Вообще я не против того, чтобы она работала практически в моём доме." 
    
    menu:
        "Но чувствую я, что это плохая идея. А что если она не подойдёт? Она должна будет снова искать работу, а для Яны это неплохой такой стресс. Что же ей ответить?"
        "Поддержать":
            jump v1_agree
        "Усомниться":
            jump v1_doubt
        "Всё равно, пусть сама думает":
            jump v1_neutral

label v1_agree:
    D "Ну, думаю у тебя получится. Особенно если ты будешь ходить с хозяйкой пекарни в зал."
    $ yanaPoints = 1
    y "Спасибо. Я буду максимально стараться. Ну и наши походы в зал не будут причиной моих повышений! Наверное."
    y "А вообще весьма неожиданно слышать от тебя одобрение. Разве тебе не всё равно?"
    D "Может я решил пересмотреть отношение к людям. А может мне просто дождь поднял настроение. "
    y "Ну как знаешь. Так или иначе, спасибо! Не то, чтобы мне сейчас нужна была поддержка, но всё равно приятно слышать такое."
    y "Особенно от тебя."
    "Последнее наверное было лишним, но я пропускаю это мимо ушей."
    jump v1_c2

label v1_doubt:
    D "Весьма рискованно метить в менеджеры, когда ты только год отработала продавцом косметики. Не переживаешь по этому поводу?"
    $ yanaPoints -= 1
    y "Понимаю, переход будет не самым лёгким, но у меня будет испытательный срок, во время которого меня всему научат. Наверное."
    y "Ну и надеюсь, что хозяйка пекарни не будет сильно меня загонять... Хотя вряд ли там много работы."
    y "А вообще весьма неожиданно слышать от тебя сомнения по этому поводу. Разве тебе не всё равно?"
    D "Может я решил разобраться в вопросе и точно описать тебе ситуацию."
    y "Спасибо, пожалуй воздержусь от твоего экспертного мнения."
    D "Как хочешь."
    "Не стоило наверное так говорить. Но что сделано, то сделано. Тем более мне и вправду всё равно где она будет работать."
    jump v1_c2

label v1_neutral:
    D "Ну если ты взвесила все за и против, могу только пожелать удачи. Я в таких вопросах не сильно компетентен, да и не очень интересно."
    $ coldPoints += 1
    y "Типичный твой ответ. Я почти дословно предсказала эту реплику."
    D "Стабильность - залог успеха. Да и вообще, просить совета у человека, который ни часа не проработал - такое себе."
    y "Да ладно, я уже привыкла. Зато никаких сор у нас нет."
    D "Ну ты уже могла понять, что я не очень люблю конфликты. Тем более я не против, чтобы ты работала через дорогу. Весьма удобно."
    "Как всегда ответил в своём стиле, но мне и вправду всё равно где она будет работать."
    jump v1_c2

label v1_c2:
    D "Спасибо за еду. Пойду прилягу."
    if yanaPoints == 1:
        y "Ну вот, а я ещё поговорить хотела. Точно ещё не останешься?"
        # Добавить сцену с разговором #---------------------------------------------------
    elif yanaPoints == 0:
        y "Давай. А я пока пойду эклеры доем. "
    else:
        y "Ага."
    "Я медленно иду в свою комнату."

    return