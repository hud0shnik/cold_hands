# Начало
label start:

    scene bg void
    stop music fadeout 4.0

    "Осень - моё любимое время года. Жалко, что не могу как раньше наслаждаться видом оранжевого леса из окна, но у всего есть плюсы и минусы."
    "В последнее время я начал больше времени проводить с самим собой наедине. От этого грустных мыслей не убавилось."

    menu:
        "Раньше от плохого настроения мне помогала гитара, может стоит попробовать?"

        "От одного рифа хуже не станет":
            play sound initialize
            "Кое-как нащупываю первый лад, и ..."
            stop sound fadeout 0.5
            "Нет, тут даже гитара не поможет."

        "Не сегодня, не сегодня":
            "Да, музыка для позеров."
            pass

    "В моменты, когда человеку скучно и грустно многие делают весьма страшные вещи. Надо пройтись."
    "Сегодня Яна работает, пойти на улицу не с кем, поэтому пройтись я могу лишь на кухню, хех."
    play sound door
    with fade
    "Чай. Самое время пропустить чашечку. Хотя странно наверное называть \"чашечкой\" кружку 0.5"

    menu:
        "Какой же улун я выберу сегодня?"
        "Да Хун Пао":
            "Большой Красный Халат. Достаточно кинуть пару листов в кружку и получишь яркий вкус жаренного улуна. Не могу представить свою жизнь без него."
        "Цзинь Сюань":
            $ milkOolong += 1
            "Молочный улун. Достаточно кинуть пару листов в кружку и получишь сильное молочное послевкусие. Может стоило купить пару килограмм вместо одного пакета?"

    play sound tea0
    "Я наливаю воду в чайник и включаю его. За прошедшие 4 месяца я неплохо научился ориентироваться в квартире."
    "И резко полюбил порядок. Потому что искать полчаса кружку - не круто. Можно сказать, что я построил свою систему координат или что-то подобное."

    if milkOolong == 1:
        "Я достаю кружку, бросаю в неё пару скрученных листьев. Даже сейчас я начинаю слышать лёгкий молочный запах. Кладу руку на чайник - так легче мерить температуру."
    else:
        "Я достаю кружку, бросаю в неё пару продольно скрученных листьев, кладу руку на чайник - так легче мерить температуру."
    stop sound fadeout 1

    play sound tea1
    "Осталось залить листья. Отмеряю уровень воды в кружке с помощью мизинца. Улун готов."
    stop sound fadeout 1

    play sound door
    with fade

    "Теперь нужно аккуратно вернуться в свою комнату. Хотя, если пролью немного по пути, ничего страшного не произойдет. Я перестал портить чай сахаром ещё в средней школе."
    "Медленно ставлю кружку на табуретку рядом с кроватью. Так как я не перемешал улун, ему нужно дать время завариться. Ложусь на кровать."
    "А ведь и правда, раньше я проводил намного меньше времени наедине с самим собой. Не знаю хорошо это или плохо."
    jump v1_s1

# Яна пришла с работы
label v1_s1:

    play sound keys
    "Звук ключей. Похоже в этот раз мне не придется коротать остаток дня в беседах с самим собой."
    stop sound fadeout 1

    play sound door
    "По осторожному звуку открытия двери я понимаю, что это Яна. В это время она обычно на работе, интересно что случилось."

    show y 1-1 at center with moveinleft

    y "Уже проснулся?"
    D "Сегодня решил встать пораньше. Ты разве не должна сейчас продавать мыло?"
    y 2-4 "Из-за ливня торговый центр немного затопило, и меня отправили домой."
    D "А в такой ситуации разве не должны наоборот выдавать сотрудникам вёдра и швабры?"
    y 2-6 "Дань, я же не уборщицей или охранником работаю. Начальница сказала, что на сегодня \"Шалфей\" закрывается."
    y "Эх, а так хотелось по полчаса объяснять, что бомбочки для ванной могут стоить больше ста рублей."
    D "О-о-очень интересно. Энивей, раз у тебя сегодня выходной, сгоняешь за эклерами?"
    y 1-5 "Конечно сгоняю! В ливень так и хочется пройтись до пекарни!"
    D "Ну ладно-ладно, в холодильнике вроде ещё осталась парочка."
    "Ливень похоже и вправду сильный. Эх, сейчас бы погулять..."

    menu:
        "Может попросить Яну со мной выйти?"
        "Не уверен, что это сработает, но попробовать стоит":

            D "Не хочешь пройтись?"
            y 2-4 "Дань, ну не в такую погоду же. Там даже зонтик не поможет. Если просвежиться хочешь, иди на балконе почилль."
            hide y with dissolve
            play sound door
            with fade
            "Результат довольно предсказуем. Я открываю дверь балкона, и..."
            play music rain
            "Да, ливень действительно хороший."
            "Раньше я очень любил стоять на балконе, смотреть на прохожих. Мог так часами проводить время."
            "Балкон был для меня как большой террариум. Сутра люди торопились на работу, а вечером бежали домой. Но те времена прошли. Теперь балкон для меня - просто источник белого шума."
            "Ну, по крайней мере, лучше, чем ничего. Звуки дождя расслабляют. Хотя я и так не очень-то обеспокоенный или нервный."
            "Теперь моя жизнь вообще лишена какого-либо стресса. На работу не надо, из вуза я отчислился, в армию по понятным причинам меня не заберут. Остаётся только жить жизнь."
            "Грустно, конечно, быть обузой для родителей. Обычно после 18-ти люди съезжают от родни. Но в моём случае наоборот. Они оставили мне квартиру на моё девятнадцатилетие."
            "Теперь из-за меня они вынуждены присылать каждый месяц деньги Яне на моё содержание. Я всё ещё не привык к такому, и похоже не привыкну."
            "Хотя Яна довольна. Она снимает у меня комнату в обмен за уход. Я и непротив, тем более она убирается по выходным и неплохо готовит."
            "С первого взгляда может показаться, что это не жизнь, а мечта: собственная квартира, в соседней комнате живет девушка, не нужно работать."
            "Но у всего есть плюсы и минусы"
            $ coldPoints += 1
            stop music
            play sound door
            "Из кухни доносятся звуки кипящей воды. Ладно, что-то есть захотелось. Пойду на кухню."
            show y 1-4 at center with fade
            y "Ну как там на улице?"
            D "Прекрасно, жалко кое-кто не захотел пойти погулять."
            y 1-7 "Да ладно тебе, меня чуть не утопило по дороге. Есть будешь?"

        "Нет, тут у меня мало шансов":
            hide y with dissolve
            "Какое-то время я просто стою осознавая, что очень хотел бы пойти погулять. Пока не начинаю ощущать запах еды."
            play sound door
            show y 1-4 at center with fade
            D "Что-то варишь?"
            y 2-0 "Агась, сможешь угадать?"


    D "Ммм, пельмени, оригинально."
    y 1-5 "Ну извини, из продуктов я могла только бутерброды сделать, и то без хлеба."
    "Я сажусь за стол. Пытаюсь найти руками тарелку и вилку, но Яна меня опережает и направляет мои руки прямо к ним. Не самая удобная еда, я бы предпочёл бутерброды или суп."
    D "Завтра у нас что?"
    y 1-1 "Суббота. Если ты собрался за покупками пойти, то давай сутра сразу? У меня завтра кое-какие дела."
    D "Утром так утром."
    "Пельмени то и дело пытаются выскользнуть, но я ловко натыкаю их вилкой. Начинаю привыкать к такой форме потребления пищи."
    D "А что за дела? Не посвятишь?"
    y 2-3 "Опять собес. Хоть начальница в \"Шалфее\" и добрая, но зарплата меня всё ещё не устраивает. Да и ехать долго."
    D "Дай угадаю, хочешь устроиться в аптеку? А, хотя нет, там платят ещё меньше, тогда ставлю на магазин для хобби."
    y 2-6 "Мимо, у меня собес в пекарню."
    D "Я тебя расстрою, но там платят явно меньше."
    y 1-1 "Продавцам да, а вот менеджерам..."
    D "А с каких пор ты стала дипломированным менеджером?"
    y 1-7 "А ты знаешь кто владелец этой пекарни?"
    D "Понятия не имею."
    y "Ну тогда не буду сильно грузить тебя подробностями. Просто встретила её в зале, и мы так разговорились, что она пригласила меня на собес."
    y 2-0 "Ну как собес, она уже сказала, что это будет скорее знакомство с остальным персоналом и обсуждение графика и тому подобного."
    D "Интересный метод вербовки сотрудников. Ну и как думаешь, справишься? Должность не самая лёгкая."
    y 1-4 "Ну с \"Менеджером\" я немного перегнула. Тайтл немного другой. В обязанности выходит контроль поставок и общение с посетителями, ну и по мелочи ещё."
    D "Ясно, разнорабочей взять хотят. А что по зарплате?"
    y "На десять процентов больше прежней, да и ехать никуда не надо, а это существенно экономит деньги."
    y 1-6 "Интересно узнать твоё мнение по этому поводу."
    "Зная Яну, могу сказать, что менеджер из неё такой же, как из меня кинокритик. Хотя недавно она проходила какие-то курсы. Вообще я не против того, чтобы она работала практически в моём же доме."

    menu:
        "Но чувствую я, что это плохая идея. А что если она не подойдёт? Она должна будет снова искать работу, а для Яны это сильный стресс. Что же ей ответить?"
        "Поддержать":
            jump v1_s1_agree
        "Усомниться":
            jump v1_s1_doubt
        "Всё равно, пусть сама думает":
            jump v1_s1_neutral

# Игрок поддержал решение Яны
label v1_s1_agree:

    D "Ну, думаю у тебя получится. Особенно если ты будешь ходить с хозяйкой пекарни в зал."
    y 2-5 "Спасибо. Я буду максимально стараться. Ну и наши походы в зал не будут причиной моих повышений! Наверное."
    y 3-1 "А вообще весьма неожиданно слышать от тебя одобрение. Разве тебе не всё равно?"
    D "Может я решил пересмотреть отношение к людям. А может просто рад, что ты будешь таскать эклеры с работы. "
    y 3-3 "Ну это я устроить смогу. Так или иначе, спасибо! Не то, чтобы мне сейчас нужна была поддержка, но всё равно приятно слышать такое."
    y 2-3 "Особенно от тебя."
    "Последнее наверное было лишним, но я пропускаю это мимо ушей."
    "..."
    "Нет, не пропускаю. Наверное надо больше интересоваться её жизнью."
    $ yanaPoints += 1
    jump v1_s2

# Игрок усомнился в решении Яны
label v1_s1_doubt:

    D "Весьма рискованно метить в менеджеры, особенно когда ты только год отработала продавцом косметики. Не переживаешь по этому поводу?"
    y 3-1 "Понимаю, переход будет не самым лёгким, но у меня будет испытательный срок, во время которого меня всему научат. Наверное."
    y 2-1 "Ну и надеюсь, что хозяйка пекарни не будет сильно меня загонять... Хотя вряд ли там много работы."
    y 2-6 "А вообще весьма неожиданно слышать от тебя сомнения по этому поводу. Разве тебе не всё равно?"
    D "Может я решил разобраться в вопросе и точно описать тебе ситуацию."
    y 1-7 "Спасибо, пожалуй воздержусь от твоего экспертного мнения."
    D "Как хочешь."
    "Не стоило наверное так говорить. Но что сделано, то сделано. Тем более мне и вправду всё равно где она будет работать."
    $ mindPoints += 1
    jump v1_s2

# Игроку всё равно на решение Яны
label v1_s1_neutral:

    D "Ну если ты взвесила все за и против, могу только пожелать удачи. Я в таких вопросах не сильно компетентен, да и не очень интересно."
    y 1-7 "Типичный твой ответ. Я почти дословно предсказала эту реплику."
    D "Стабильность - залог успеха. Да и вообще, просить совета у человека, который ни часа не проработал - такое себе."
    y 2-5 "Да ладно, я уже привыкла. Зато никаких сор у нас нет."
    D "Ага. Тем более я не против, чтобы ты работала через дорогу. Весьма удобно."
    "Как всегда ответил в своём стиле, но мне и правда всё равно где она будет работать."
    $ coldPoints += 1
    jump v1_s2

# Сцена со звонком Сане
label v1_s2:

    D "Спасибо за еду. Пойду прилягу."
    if yanaPoints == 1:
        y 2-4 "Ну вот, а я ещё поговорить хотела. Точно ещё не останешься?"
        D "Если ты хочешь ещё что-то обсудить, валяй."
        y 3-1 "Просто интересно твоё мнение. Я уверенна в том, что меня примут в пекарню, но не знаю как сказать об этом нынешней начальнице. Молча уйти я не могу."
        D "Ну я бы точно просто ушёл. Устраивать прощальный день - такая себе идея. Но мы не обо мне говорим, так что тут нужно подумать."
        y 1-5 "Просто начальница такая милая, вот, даже отпустила меня сегодня с работы."
        D "У тебя на работе остались вещи какие-нибудь?"
        y 3-1 "Нет, из-за потопа я забрала почти все вещи оттуда. Там конечно осталась какая-то мелочёвка, но её даже забирать не хочется."
        D "Тогда всё очень просто. Позвони начальнице, объясни ситуацию. Можешь сказать, что тебе нужно ухаживать за слепым другом, я думаю она всё поймёт."
        y 1-4 "А я даже не думала о том, чтобы позвонить. Неплохая неделя."
        D "Как раз обсудишь с ней бумажную волокиту и прочие прелести взрослой жизни."
        y "А ведь и правда. Спасибо. Пойду приготовлюсь к звонку."
        "Приготовиться к звонку? Это как? Морально что ли? Ладно, не буду мешать Яне с \"подготовкой\"."
    elif coldPoints == 0:
        y "Давай. А я пока пойду эклеры доем."
        "Эклеры? Не, я не думаю, что она оба съест. У неё же есть совесть."
    else:
        y "Ага."


    hide y with fade
    "Я медленно иду в свою комнату."
    play sound door
    "И снова я один. Хотя за всё это время я уже привык. Раньше я гораздо меньше оставался наедине с самим собой, и упрекал себя за это."
    "Мне казалось, что чем человек больше времени проводит в раздумьях, чем больше он слушает свои мысли, тем крепче становиться его рассудок."
    "Ну теперь я точно стал проводить больше времени в раздумьях. Только вот хорошо ли это?"
    "Меня отталкивали люди, слушающие аудиокниги во время сна только ради только ради того, чтобы в голову не лезли плохие мысли."
    "\"Плохие мысли\""
    "Разве у человека может возникнуть что-то подобное? А если такое и возникает, разве человек не должен наоборот попытаться найти причину?"
    "А то как-то странно получается. Наверное если человека преследуют странные мысли, последнее, что надо делать - это не обращать на них внимание."
    "Ну это уже сугубо моя точка зрения."
    "Точка зрения........."
    "Так, ладно, нужно позвонить Саньку, а то я уже сам сходить с ума начинаю."
    show mb 0-0 at center with moveinleft
    "Беру телефон. Теперь я предпочитаю ретро-мобильники. Со смартфонами перестал дружить по понятным причинам."
    "Не знаю как называется эта опция, но она оказалась очень удобной. Достаточно зажать одну из кнопок для звонка Сане."

    "..."
    s "Йо, как жизнь, старик?"
    D "Да как обычно, потихоньку. Ты сам как? Могу к тебе домой завалиться?"
    "Конечно один я никуда \"завалиться\" не могу. Не дойду просто. Но Саня уже давно заходит за мной, даже если потом мы идём к нему."
    s "Прямо сейчас нет, но через какое-то время я буду свободен. Короче зайду за тобой часика через два примерно."
    D "Забились. Ладно, до встречи."
    s "Ага, давай."
    "..."
    hide mb with fade

    "Ну вот теперь день точно обещает быть интересным."
    menu:
        "Как же мне скоротать время до Сани?"
        "Чай, очень хочу чай":
            jump v1_s3_tea
        "Поиграть на гитаре":
            jump v1_s3_guitar
        "Покопаться в себе":
            jump v1_s3_mind
        "Поспать":
            jump v1_s3_sleep

# Игрок коротает время за гитарой
label v1_s3_guitar:

    "Я беру гитару со стойки. И начнём мы с ...."

    play sound "sound/prelude.mp3"
    "\"Prelude\" - это один из первых риффов, который я выучил. Конечно, я его немного доработал. От оригинала остались только аккорды."
    stop sound

    play sound "sound/vrat'.mp3"
    "Теперь рифф из песни \"Врать\". Один из немногих рифов с флажолетами, который я могу теперь себе позволить."
    stop sound

    play sound "sound/smelost'.mp3"
    "В риффе из песни \"Смелость\" меня привлекла игра с тониками. Если бы я писал музыку, то точно использовал бы подобные приёмы."
    stop sound

    play sound "sound/ponpon.mp3"
    "Ну и закончу я риффом из видео-игры. Так давно не играл в видео-игры. И наверное больше не буду. С другой стороны у меня появилось много свободного времени."
    stop sound

    "Хотя, как пел один чел: \"Так много времени на жизнь, оно растянуто в проклятии\". Ну ладно. На сегодня хватит."
    "Надо бы попеть когда-нибудь. Давно не пел. Только вот теперь читать текст песни я не смогу. Только по памяти. Зато душевнее будет, наверное."

    "Оставшееся время я провожу за упражнениями. Запоминаю ноты на слух. И местоположение ладов. Только я начинаю тренировать флажолеты..."

    show sn 1-4 at center with moveinbottom
    s "Йо, это какой-то сложный мат-рок рифф? Пять восьмых?"
    D "Нет, это просто упражнение, которое я сам придумал."
    s 2-4 "Слава богу. А то я уже подумал, что ты за мат-рок сел."
    D "Не вижу в этом ничего плохого."
    s 1-5 "..."
    "Повисает неловкая пауза. Ну тут я уже сам подставился. Хотя меня немного улыбнуло с обстановки."
    s 2-1 "Эээ, а ты шашки взял?"
    D "Мы вчера с Яной играли, так что спроси у неё."
    s 2-5 "Окей, пойду спрошу."
    hide sn with fade
    "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
    show sn 2-1 at center with moveinbottom

    jump v1_s4

# Игрок коротает время за сном
label v1_s3_sleep:

    "Вроде бы из-за недостатка клетчатки после еды люди хотят спать. Ну, я не могу ничего поделать с естественными нуждами."
    "Вот оно, любимое место в квартире - кровать. Не самая дорогая, я бы даже сказал дешевая. Но что-то в ней есть. Что-то манящее."
    "Закрываю глаза и ..."
    "Серьёзно? Я теперь и во сне чай пью? Похоже это реально \"единственная радость души моей\". Но смысла такого сна я всё равно не понимаю. Во сне человек не может ничего ощущать."
    "Какое-то время я продолжаю просто пить чай во сне, пока не чувствую сильный запах дезодоранта. Он как будто вытягивает меня из сна и возвращает в реальный мир."
    show sn 1-5 at center with moveinbottom
    s "Сон после обеда? Чтоб я так жил."
    D "Поверь мне, ты совсем не хочешь так жить."
    s 2-1 "Ой, да ладно тебе. Куда шашки дел?"
    D "Мы вчера с Яной играли, так что спроси у неё. Сыщик из меня такой себе."
    s 2-5 "Окей, пойду спрошу."
    hide sn with fade
    "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
    show sn 2-1 at center with moveinbottom

    jump v1_s4

# Игрок идёт пить улун
label v1_s3_tea:

    "Ну, улун, который я заварил час назад, уже остыл. Весьма печально. Я не из тех людей, которые греют чай в микроволновке, так что пойду ещё кружку заварю."
    "На кухне уже никого нет, Яна ушла в свою комнату. Я подхожу к столу и понимаю, что ..."
    "Единственный минус моей любви к чаю - постоянно нужно совершать такой сложный выбор."

    menu:
        "Итак, что же я выберу на этот раз?"
        "Да Хун Пао":
            "Большой Красный Халат. Неплохой выбор как к солёному, так и к сладкому. Но чаще всего я пью его просто так. Нет смысла портить что-то настолько самодостаточное."
        "Цзинь Сюань":
            if milkOolong > 0:
                "Снова молочный улун. Уж очень он мне заходит в последнее время. Частичная обжарка листа даёт этому улуну весьма приятные нотки."
            else:
                "Молочный улун. Как же он приятно пахнет. Частичная обжарка листа даёт ему весьма узнаваемые нотки."
            $ milkOolong += 1

    play sound tea0
    "Я наливаю воду в чайник и включаю его. Как же хорошо иметь пластмассовый чайник. Можно держать руку на нём для контроля температуры."
    "Вообще с чайником мне повезло. Его подарила мамина подруга, которая торгует кухонной утварью. Чайник оказался очень дорогим."
    "Служит мне уже 5 лет, но, думаю, что он меня ещё переживёт. Прекрасный чайник, просто прекрасный."

    "Ополаскиваю кружку в раковине, бросаю в неё пару листьев. Кладу руку на чайник."
    stop sound fadeout 1

    play sound tea1
    "Заливаю листья. Отмерять уровень воды с помощью мизинца весьма удобно. Вообще, мизинец - очень полезный палец. Я часто меряю им температуру."
    stop sound fadeout 1

    "Итак. Улун готов."
    "Я сажусь за стол. Осталось только дождаться пока улун заварится и остынет. Но на это уходит не так уж много времени, я кипячу воду примерно до восьмидесяти градусов."
    "Ну, думаю улун готов. Вкус прекрасен, как обычно. Из-за того, что я завариваю весьма малое количество листьев, на выходе получается очень слабый улун."
    "Если привести аналогию, то чай, который заваривают обычно люди (черный, крепкий, с сахаром, лимоном и т.д.) я бы сравнил с картиной, написанной жирным слоем гуаши."
    "Я же предпочитаю картины, написанные акварелью бедным студентом (минимум краски, максимум воды)."
    show sn 2-5 at center with moveinbottom
    "Оставшееся время я провожу растягивая улун. Я понял, что немного потерял счет времени когда Саня зашёл на кухню."
    s "Чаёвничаем во всю?"
    D "Типа того."
    s 2-2 "Всё ещё не переносишь кофе? Как вообще можно целыми днями пить чай?"
    D "Ну знаешь, не очень хочется подсаживаться на кофеин. Да, в чае он есть, но не столько, далеко не столько."
    s 3-1 "Ой, давай сегодня без лекций об алкалоидах. Ты шашечки взял?"
    D "Мы вчера с Яной играли, так что возьми у неё."
    s "Окей, пойду спрошу."
    hide sn with fade
    "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
    show sn 2-1 at center with moveinbottom

    jump v1_s4

# Игрок разговаривает сам с собой
label v1_s3_mind:

    "Два часа разговоров с самим собой, что может пойти не так? Хотя я бы не сказал, что из-за такого человек может с ума сойти."
    "Но вот два часа загонов могут сильно повлиять на человека. Ну, сегодня у меня в планах ничего подобного нету."
    "И всё же я не понимаю. Как люди могут в здравом уме пить кофе? Он же мало того, что горький, так ещё и кофеина там ужасно огромное количество."
    "Некоторые, несомненно, добавляют в кофе сахар. Но это лучше ситуацию не делает. И вообще сахар очень вредный, а кофеин - зло."
    "Просто, если человек пьёт минимум по две кружки кофе в день, это сколько же он потребляет сахара и кофеина в год? Ужас."
    "Тем более кофе очень дорогой. Да, хороший чай стоит около десяти тысяч за килограмм, но для меня это нормально. Ведь ста грамм чая мне хватает на месяц (хотя я не считал точно)."
    "А кофе со сгущёнкой? Это же вообще смерть!"
    "В общем, не понимаю кофе. И людей, которые его пьют."

    menu:
        "Что-то так захотелось в шашки партейку сыграть. Может пойти пойти с Яной разложить?"
        "Отличная идея":
            "Я иду в комнату Яны"
            play sound door
            show y 1-1 at center with fade
            y "Дай угадаю, закончились чистые ложки?"
            D "Не, недавно я переосмыслил всё, и понял, что ложки мне не нужны."
            y 1-4 "Это почему?"
            D "Ну....... Мне просто лень их мыть, да и погружать в улун что-то металлическое - такая себе идея. Не уверен, что это влияет на вкус, но всё же."
            y 2-0 "Да ладно, тебе просто лень их мыть."
            D "Ладно, ты меня раскусила."
            y 3-4 "Окей, раз это не ложки, то ты наверное пришёл ругать меня за эклеры, да?"
            D "Что? Так, подожди..... Ты съела все эклеры?!"
            y 2-6 "Ну они просто так лежали грустно в холодильнике, вот я и решила...."
            D "Беспредел. Там ведь две штуки оставалось. Один тебе, один мне. Ну лан, проехали."
            "Не ожидал такого предательства. Это же эклеры с заварным кремом! Не со сгущёнкой! С заварным кремом!"
            "Уже поворачиваюсь чтобы уйти, но потом вспоминаю про шашки. Нужно забрать их из рук этой коварной девушки!!!"
            D "За мной скоро Саня зайдёт, дай шашки. Пожалуйста."
            y 3-6 "Минуту. Так, куда я могла их деть?"
            hide y with moveoutright
            "Проходит около тридцати минут. И всё же Яна находит шашки."
            show y 2-5 at center with moveinright
            y "На, держи. Не хочешь партейку сыграть?"
            D "Нет, спасибо. Мне нужно переосмыслить некоторые моменты жизни. Например доверие."
            y 1-7 "Ой, да ладно тебе. Схожу я за эклерами завтра."
            D "Я не обижаюсь. Но пунктик карандашиком поставил."
            $ event0 = True
            y 2-3 "Ладно, за чаем тоже схожу."
            D "Вот это уже другой разговор. Дело закрыто. Подсудимый оправдан."
            "У меня получилось сказать это весьма серьёзным и грозным голосом. От чего Яна начинает смеяться."
            $ yanaPoints += 1
            hide y with fade
            play sound door
            "Я выхожу с шашками и победным настроением."
            "Остаток времени я провожу обдумывая проблемы доверия в современном обществе. В жизни столько странных вещей. Иногда это даже пугает."
            show sn 2-4 at center with moveinbottom
            s "Ого, как необычно. Даня лежит на кровати и думает. Давно такого не было."
            D "Вот этот твой пассивно-агрессивный сарказм...... Как бы так сказать..."
            s 1-1 "Да понял я, понял. Ты шашки взял?"
            D "Ага, выдвигаемся?"
            s 2-1 "Пошли."
            jump v1_s4

        "Не, играть буду с Саней попозже":
            $ mindPoints += 1
            "Как бы я не любил настольные игры, но весь день играть в шашки - такое себе. Поэтому лучше полежу на кровати."
            "Вчера вечером мы с Яной неплохо поиграли. Я не тот человек, который считает очки, количество побед и т.д. Но не могу не заметить, что Яна стала играть намного лучше."
            "Она даже выдала три победы подряд. Наверное первый раз за всё время. Но хвалить её не буду, расслабится ещё."
            "Сначала я думал, что она мне поддаётся, но затем это ощущение быстро развеялось. Может это со мной что-то не так? Я вроде не сильно стараюсь. Да и проигрывать не боюсь."
            "Тем более, когда слышу как она радуется каждой победе. Иногда я даже поддавался. Просто чтобы сделать кого-то счастливее."
            "Остаток времени я провожу обдумывая самые странные аспекты жизни. Как обычно. На самом деле в жизни столько странных вещей. Иногда это даже пугает."
            show sn 2-4 at center with moveinbottom
            s "Ого, как необычно. Даня лежит на кровати и думает. Давно такого не было."
            D "Вот этот твой пассивно-агрессивный сарказм...... Как бы так сказать..."
            s 1-1 "Да понял я, понял. Ты шашки взял?"
            D "Нет, мы вчера с Яной играли, так что возьми у неё."
            s "Окей, пойду спрошу."
            hide sn with dissolve
            "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
            show sn 2-1 at center with moveinbottom
            jump v1_s4

# Поход к Сане домой
label v1_s4:

    if yanaPoints == 0:
        s 2-2 "Какая-то Яна сегодня задумчивая. У неё что-то случилось?"
        D "Ага, повышение случилось."
        s 2-4 "Рад за неё."

    hide sn with fade

    "Я не очень быстро, да и не очень аккуратно одеваюсь, и через всего лишь тридцать минут мы выходим на улицу."
    play sound door
    play music traffic
    show sn 2-1 at left2 with moveinleft
    "Свежий воздух, наконец-то. Я весьма опечален тем, что дождь прошёл, но зато можно не торопиться."
    s "Как пойдём? Подлиннее или покороче?"

    menu:
        "Погода хорошая, можно и подольше погулять":
            D "Давай через парк, сегодня очень приятная погода."
            s 2-2 "Как скажешь. Ну как там у тебя с адаптацией?"
            D "Да так, потихоньку. Раньше я и мечтать не мог о таком большом количестве времени. Можно многое обдумать."
            s 1-2 "Представляю. Уже чувствуешь, как начинаешь лучше слышать?"
            D "Ага, потихоньку превращаюсь в инопланетянина. Скоро третья рука вырастет."
            D "Ну, а если серьёзно, то могу сказать, что твой дезодорант я учуял с порога."
            s 1-5 "Даже не знаю хорошо это или плохо."
            D "А что ты эти два часа делал? Что-то очень важное?"
            s 1-1 "Это ты с чего взял?"
            D "Ну, раз сразу не пошёл за мной, значит дело очень важное."
            s 2-4 "Ха-ха-ха, ну, весьма логично. Я бегал курсовую печатать. Препод наконец-то дал зелёный свет."
            D "Как оценил?"
            s 1-3 "Незаслуженный \"хор\"."
            D "Неплохо..."
            s 1-5 "\"Неплохо\"?!?! Я целый месяц убил на него. Знаешь за что препод снизил оценку на балл?"
            D "Валяй."
            s "За то, что в источниках я указал фамилию, отчество и имя автора."
            D "Вот тут не понял."
            s 1-6 "А надо было указать фамилию, имя и отчество."
            D "Ну это всё меняет. Тебе ещё повезло, что он на пересдачу не отправил. Такая серьёзная ошибка. Как ты мог?!?!"
            s 3-3 "Вот всё тебе в шутку надо превратить."
            D "Ну ладно, ладно. Может ему твой дезик не понравился просто."
            s 1-1 "Очень смешно."

        "Не, лучше сразу к Сане пойти":
            D "Давай по короткому, хочу быстрее шашки разложить."
            s 1-1 "Понял, принял."
            s "Я тут недавно курсовую наконец-то доделал, хочешь расскажу про что она?"
            s "Валяй."

    "Весь оставшийся путь я слушаю краткое описание курсовой работы Сани. Действительно, работа была проделана титаническая. Не ожидал от него такого."

    jump v1_s5

# Игрок чиллит у Сани дома
label v1_s5:
    hide sn
    play sound door
    show sn 1-1 at center with moveinright
    "Итак, мы заходим в квартиру. Я снимаю ветровку и отдаю её Сане. Так как здесь я не могу свободно ориентироваться, приходится ходить вдоль стен."
    "Саня ведёт меня в свою комнату"
    s 3-5 "Так, ты садись пока, а я пойду сделаю нам что-нибудь."
    D "Это \"что-нибудь\" будет вискарём с колой?"
    s 3-4 "А как же, тебе как обычно, по минимуму?"
    D "Ага, шот на стакан. Только в этот раз давай безо льда."
    s 2-5 "Будет сделано, разложи шашки пока."
    hide sn
    "Я достаю коробку модифицированных шашек и начинаю раскладывать фигуры. Это смесь двух наборов, так что белые и чёрные фигуры можно легко различить даже не видя их."
    "Также на поле есть наклейки на черных клетках, что делает их больше. Это не сильно помогает, так как во время партий, я обычно держу ситуацию на поле у себя в голове."
    "Конечно, мне далеко до шахматистов, которые могут играть партии просто называя ходу друг другу, но с шашками я уже справляюсь и без зрения."
    "С кухни доносится звон стаканов и льда. Через минуту Саня возвращается. Бакалы осторожно падают на стол."
    show sn 2-1 at center with moveinleft
    s "Разложил? "
    D "Ага, ты морально готов к поражению?"
    s 2-4 "Ха-ха, это мы ещё увидим."
    "Партия длится не слишком долго, исход меня совсем не удивил."
    D "Ты прямо любишь подставляться."
    s 1-3 "Это я не разогрелся ещё. Давай следующую."
    "В этой партии я совершил ошибку."
    s 2-4 "Ну вот, я же говорил! Сейчас две подряд сделаю."
    "В середине партии Саня начинает весьма интересный разговор."
    s 3-1 "Слушай, я в воскресенье собираюсь тут маленькое мероприятие устроить. Отпраздновать сдачу курсовой так сказать."
    D "Учитывая то, что сейчас сентябрь, я бы назвал это \"пересдачей\" курсовой."
    s 1-5 "Ну вот надо тебе на больное давить? Я ещё от оценки не отошёл."
    D "Ладно, ладно. Что намечается?"
    s 1-2 "Я планирую позвать человек пятнадцать, все скидываются, но так как я тебе должен, можешь не скидываться."
    D "Интересно как ты уместишь такое большое количество людей в одной трёшке. Ну ладно, я в воскресенье не занят, так что, думаю, смогу."
    s 1-1 "Ого, я думал, что придётся тебя уговаривать. Решил перестать сидеть целыми днями дома?"
    D "Просто попробую найти человека, который сможет выиграть меня в шашки."
    s 1-4 "Ну, пара человек на примете есть, если ты об этом. Есть даже одна шахматистка, подруга подруги. Кстати, вот ты и подставился."
    "На секунду я отвлёкся мыслью об шахматистке, чем Саня и воспользовался. Разве девушка, которая хорошо играет в шахматы, будет ходить по квартирам друзей? Интересно."
    s 2-4 "Два - один, Дань, ты сегодня не в духе?"
    D "Ничего, ничего, сейчас отыграюсь!"
    "Следующие две партии я пытаюсь выровнять счёт. Но мысли о предстоящем мероприятии не дают мне покоя. Нужно ли было соглашаться? Как люди примут меня?"
    "Знакомиться я всегда не любил. Может стоит поменять своё отношение к этому? Завтра об этом подумаю."
    D "Ты мог две шашки съесть вот тут."
    s 2-1 "Да? А это манёвр такой. Чтобы сбить оппонента с толку."
    D "Ха-ха-ха, ну ладно, ответ принимае..."
    "Не успеваю я договорить, как Саня берёт три шашки. Действительно сбил с толку."
    D "Ого, неплохо, неплохо. Я тебя недооценил, сейчас отыграюсь."
    "Следующие два-три часа мы проводим за партиями в шашки. Было очень весело."
    D "Ладно, я пойду наверное, проводишь?"
    s 2-4 "Конечно! Только шашки соберу."
    hide sn with moveoutleft
    show sn 2-4 at center with moveinleft
    "Саня собирает шашки, отдаёт их мне вместе с ветровкой. Мы идём вместе до моей квартиры обсуждая сегодняшние партии."
    s "Неплохо сегодня отыграли, есть на завтра планы?"
    D "Утром у меня шоппинг с Яной, а потом я свободен."
    s 1-1 "Созвонимся тогда завтра."
    D "Ага."
    hide sn with fade
    play sound door
    D "Ян, ты дома?"
    "Конечно я слышу как она перебирает какие-то бумаги в своей комнате, но ради приличия всё равно надо было спросить. Яна подходит ко мне, снимает с меня ветровку."
    show y 1-1 at center with moveinleft
    y "Ну как сегодня? Саша смог взять реванш?"
    D "После десятой партии я перестал считать победы. Ну, могу сказать, что он стал лучше играть."
    D "В отличие от некоторых."
    y 1-7 "Ой, да ну тебя. В крестики-нолики я тебя постоянно обыгрываю."
    "Хотел бы я сказать, что это из-за того, что Яна всегда первая ходит, но в некоторых партиях, даже когда я ходил первым, она побеждала."
    D "Ну, тут не могу не согласиться. Ладно, пойду спать."
    y 1-1 "Давай. Спокойной ночи."
    D "Спокойной."
    hide y
    "Ежедневная рутина по чистке зубов и принятию душа пролетает незаметно. И вот я уже лежу на кровати."
    jump v2_s1
