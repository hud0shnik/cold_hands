label v1_s1:
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
            jump v1_s1_agree
        "Усомниться":
            jump v1_s1_doubt
        "Всё равно, пусть сама думает":
            jump v1_s1_neutral

label v1_s1_agree:

    D "Ну, думаю у тебя получится. Особенно если ты будешь ходить с хозяйкой пекарни в зал."
    y "Спасибо. Я буду максимально стараться. Ну и наши походы в зал не будут причиной моих повышений! Наверное."
    y "А вообще весьма неожиданно слышать от тебя одобрение. Разве тебе не всё равно?"
    D "Может я решил пересмотреть отношение к людям. А может мне просто дождь поднял настроение. "
    y "Ну как знаешь. Так или иначе, спасибо! Не то, чтобы мне сейчас нужна была поддержка, но всё равно приятно слышать такое."
    y "Особенно от тебя."
    "Последнее наверное было лишним, но я пропускаю это мимо ушей."
    $ yanaPoints += 2

    jump v1_s2

label v1_s1_doubt:

    D "Весьма рискованно метить в менеджеры, когда ты только год отработала продавцом косметики. Не переживаешь по этому поводу?"
    y "Понимаю, переход будет не самым лёгким, но у меня будет испытательный срок, во время которого меня всему научат. Наверное."
    y "Ну и надеюсь, что хозяйка пекарни не будет сильно меня загонять... Хотя вряд ли там много работы."
    y "А вообще весьма неожиданно слышать от тебя сомнения по этому поводу. Разве тебе не всё равно?"
    D "Может я решил разобраться в вопросе и точно описать тебе ситуацию."
    y "Спасибо, пожалуй воздержусь от твоего экспертного мнения."
    D "Как хочешь."
    "Не стоило наверное так говорить. Но что сделано, то сделано. Тем более мне и вправду всё равно где она будет работать."
    $ yanaPoints -= 1
   
    jump v1_s2

label v1_s1_neutral:

    D "Ну если ты взвесила все за и против, могу только пожелать удачи. Я в таких вопросах не сильно компетентен, да и не очень интересно."
    y "Типичный твой ответ. Я почти дословно предсказала эту реплику."
    D "Стабильность - залог успеха. Да и вообще, просить совета у человека, который ни часа не проработал - такое себе."
    y "Да ладно, я уже привыкла. Зато никаких сор у нас нет."
    D "Ну ты уже могла понять, что я не очень люблю конфликты. Тем более я не против, чтобы ты работала через дорогу. Весьма удобно."
    "Как всегда ответил в своём стиле, но мне и вправду всё равно где она будет работать."
    $ coldPoints += 1
    
    jump v1_s2

label v1_s2:

    D "Спасибо за еду. Пойду прилягу."
    if yanaPoints == 2:
        y "Ну вот, а я ещё поговорить хотела. Точно ещё не останешься?"
        D "Если ты хочешь что-то ещё обсудить, валяй."
        y "Просто интересно твоё мнение. Я уверенна в том, что меня примут в пекарню, но не знаю как сказать своей начальнице. Молча уйти я не могу."
        D "Ну я бы точно просто ушёл. Устраивать прощальный день - такая себе идея. Но мы не обо мне говорим, так что тут нужно подумать."
        y "Просто начальница такая милая, вот, даже отпустила меня сегодня с работы."
        D "Ну у тебя на работе остались вещи личные какие-нибудь?"
        y "Нет, из-за потопа я забрала все вещи оттуда. Там конечно осталась какая-то мелочёвка, но её даже забирать не хочется."
        D "Тогда всё очень просто. Позвони начальнице, объясни ситуацию. Можешь сказать, что тебе нужно ухаживать за слепым другом, я думаю она всё поймёт."
        y "А я даже не думала о том, чтобы позвонить. Неплохая неделя."
        D "Как раз обсудишь с ней бумажную волокиту и прочие прелести взрослой жизни."
        y "А ведь и правда. Спасибо. Пойду приготовлюсь к звонку."
        "Приготовиться к звонку? Это как? Морально что ли? Ладно, не буду мешать Яне с \"подготовкой\"."
        $ yanaPoints += 1

    elif yanaPoints == 1:
        y "Давай. А я пока пойду эклеры доем."
    else:
        y "Ага."

    "Я медленно иду в свою комнату."
    play sound door
    "И снова я один. Хотя за всё это время я уже привык. Раньше я гораздо меньше оставался наедине с самим собой, и упрекал себя за это."
    "Мне казалось, что чем человек больше времени проводит в раздумьях, чем больше он слушает свои мысли, тем крепче становиться его рассудок."
    "Ну теперь я точно стал проводить больше времени в раздумьях. Только вот хорошо ли это?"
    "Меня отталкивали люди, слушающие аудиокниги во время сна только ради только ради того, чтобы в голову не лезли плохие мысли."
    "\"Плохие мысли\""
    "Разве у человека может возникнуть что-то подобное? А если такое и возникает, разве человек не должен наоборот попытаться найти причину?"
    "А то как-то странно получается. Наверное если человека преследуют странные мысли последнее, что надо сделать - не обращать на них внимание."
    "Ну это уже сугубо моя точка зрения."
    "Точка зрения........."
    "Так, ладно, нужно позвонить Саньку, а то я уже сам тут сходить с ума начинаю."
    "Беру телефон. Теперь я предпочитаю ретро мобильники. С смартфонами перестал дружить по понятным причинам."
    "Не знаю как называется эта опция, но она оказалась очень удобной. Достаточно зажать одну из цифр для звонка Сане."
    
    "..." 
    s "Йо, как жизнь, старик?"
    D "Да как обычно, потихоньку. Ты сам как? Могу к тебе домой завалиться?"
    "Конечно один я никуда \"завалиться\" не могу. Не дойду просто. Но Саня уже давно заходит за мной, даже если потом мы идём к нему."
    s "Прямо сейчас нет, но через два часа я буду свободен. Короче зайду за тобой часика через два примерно."
    D "Забились. Ладно, до встречи."
    s "Ага, давай."
    "..." 

    "Ну вот теперь день точно обещает быть интересным."
    menu:
        "Как же мне скоротать время до Сани?"
        "Гитарка":
            jump v1_s3_guitar
        "Поспать":
            jump v1_s3_sleep
        "Чай?":
            jump v1_s3_tea
        "Покопаться в себе" if mindPoints == 1:
            jump v1_s3_mind

label v1_s3_guitar:
    "Я беру гитару со стойки. И начнём мы с ...."
    
    play sound "sound/prelude.mp3"
    "\"Prelude\" - это один из первых риффов, который я выучил. Конечно, я его немного доработал. От оригинала остались только аккорды."
    stop sound

    play sound "sound/vrat'.mp3"
    "Теперь рифф из песни \"Врать\". Единственный риф с флажолетами, который я могу теперь себе позволить."
    stop sound

    play sound "sound/smelost'.mp3"
    "В риффе из песни \"Смелость\" меня привлекла игра с тониками. Если бы я писал музыку, то точно бы использовал подобные приёмы."
    stop sound

    play sound "sound/ponpon.mp3"
    "Ну и закончу я риффом из игры. Так давно не играл в игры. И наверное больше не буду. С другой стороны у меня больше свободного времени стало."
    stop sound

    "Хотя, как пел один чел: \"Так много времени на жизнь, оно растянуто в проклятии\". Ну ладно. На сегодня пока хватит."
    "Вообще надо бы попеть когда-нибудь. Давно не пел. Правда теперь читать текст песни я не смогу. Только по памяти. Зато душевнее будет, наверное."

    "Оставшееся время я провожу за упражнениями. Запоминаю ноты на слух. И местоположение ладов. Только я начинаю тренировать флажолеты..."
    $ guitarPoints += 1

    s "Йо, это какой-то сложный мат-рок рифф? Пять восьмых?"
    D "Нет, это просто упражнение, которое я сам придумал."
    s "Слава богу. А то я уже подумал, что ты за мат-рок сел"
    D "Не вижу в этом ничего плохого"
    s "..."
    "Повисает неловкая пауза. Ну тут я уже сам подставился. Хотя меня немного улыбнуло с обстановки."
    s "Эээ, а ты шашки взял?"
    D "Мы вчера с Яной играли, так что спроси у неё."
    s "Окей, пойду спрошу."
    "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
    if yanaPoints < 0:
        s "Какая-то Яна сегодня задумчивая. У неё что-то случилось?"
        D "Ага, повышение случилось."
        s "Рад за неё."
    jump v1_s4

label v1_s3_sleep:
    "Вроде бы из-за недостатка клетчатки после еды люди хотят спать. Ну, я не могу ничего поделать."
    "Вот оно, моё любимое место в квартире - кровать. Не самая дорогая, я бы даже сказал дешевая. Но что-то в ней есть. Что-то манящее. "
    "Закрываю глаза и ..."
    "Серьёзно? Я теперь и во сне чай пью? Похоже это реально \"единственная радость души моей\". Но смысла такого сна я всё равно не понимаю. Во сне человек не может ничего ощущать."
    "Какое-то время я продолжаю просто пить чай во сне, пока не чувствую сильный запах дезодоранта. Он как будто вытягивает меня из сна и возвращает в реальный мир."
    s "Сон после обеда? Чтоб я так жил."
    D "Поверь мне, ты совсем не хочешь так жить."
    s "Ой, да ладно тебе. Куда ты шашки дел?"
    D "Мы вчера с Яной играли, так что спроси у неё. Сыщик из меня такой себе."
    s "Окей, пойду спрошу."
    "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
    if yanaPoints < 0:
        s "Какая-то Яна сегодня задумчивая. У неё что-то случилось?"
        D "Ага, повышение случилось."
        s "Рад за неё."
    jump v1_s4

label v1_s3_tea:
    "Ну, улун, который я заварил час назад, уже остыл. Весьма печально. Я не из тех людей, которые греют чай в микроволновке, так что пойду ещё кружку заварю."
    "На кухне уже никого нет, Яна ушла в свою комнату. Я подхожу к столу и понимаю, что ..."
    "Единственный минус у моей любви к чаю - постоянно нужно совершать такой сложный выбор."

    menu:
        "Итак, что же я выберу на этот раз?"
        "Да Хун Пао":
            "Большой Красный Халат. Неплохой выбор как к солёному, так и к сладкому. Но чаще всего я пью его просто так."
            $ milkOolong-=1
        "Цзинь Сюань":
            if milkOolong+=1:
                "Снова молочный улун. Уж очень он мне заходит в последнее время. Частичная обжарка листа даёт этому улуну весьма узнаваемые нотки."
            else:
                "Молочный улун. Как же он приятно пахнет. Частичная обжарка листа даёт этому улуну весьма узнаваемые нотки."
            $ milkOolong+=1
    
    play sound tea0
    "Я наливаю воду в чайник и включаю его. Как же хорошо иметь пластмассовый чайник. Можно держать руку на нём для контроля температуры."
    "Вообще с чайником мне повезло. Его подарила мамина подруга, которая торгует кухонной утварью. Чайник оказался очень дорогим."
    "Он служит мне уже 5 лет, но, думаю, что он меня ещё переживёт. Прекрасный чайник, просто прекрасный."
    
    "Я ополаскиваю кружку в раковине, бросаю в неё пару листьев. Как обычно кладу руку на чайник."
    stop sound fadeout 1
    
    play sound tea1
    "Заливаю листья. Отмерять уровень воды с помощью мизинца весьма удобно. Вообще, мизинец - очень полезный палец. Я часто меряю им температуру у еды."
    stop sound fadeout 1

    "Итак. Улун готов."
    "Я сажусь за стол. Осталось только дождаться пока улун заварится и остынет. Но на это уходит не так уж много времени, я кипячу воду примерно до восьмидесяти градусов."
    "Ну, думаю улун готов. Вкус прекрасен, как обычно. Из-за того, что я завариваю весьма малое количество листьев, на выходе получается очень слабый улун."
    "Если привести аналогию, то чай, который заваривают обычно люди (черный, крепкий, с сахаром, лимоном и т.д.) я бы сравнил с картиной, написанной жирным слоем гуаши."
    "Я же предпочитаю картины, написанные акварелью бедным студентом (минимум краски, максимум воды)."
    "Оставшееся время я провожу растягивая улун. Я понял, что немного потерял счет времени когда Саня зашёл на кухню."
    s "Чаёвничаем во всю?"
    D "Типа того."
    s "Всё ещё не переносишь кофе? Как вообще можно целыми днями пить чай?"
    D "Ну знаешь, не очень хочется подсаживаться на кофеин. Да, в чае он есть, но не столько, сколько в кофе."
    s "Ой, давай сегодня без лекций об алкалоидах. Ты шашечки взял?"
    D "Нет, мы вчера с Яной играли, так что возьми у неё."
    s "Окей, пойду спрошу."
    "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
    if yanaPoints < 0:
        s "Какая-то Яна сегодня задумчивая. У неё что-то случилось?"
        D "Ага, повышение случилось."
        s "Рад за неё."
    jump v1_s4

label v1_s3_mind:
    "Два часа разговоров с самим собой, что может пойти не так? Хотя я бы не сказал, что из-за такого человек может с ума сойти."
    "Но вот два часа загонов могут сильно повлиять на человека. Ну, сегодня у меня в планах ничего подобного нету."
    "И всё же я не понимаю. Как люди могут в здравом уме пить кофе? Он же мало того, что горький, так ещё и кофеина там больше, чем воды."
    "Некоторые, несомненно, добавляют в кофе сахар. Но это лучше ситуацию не делает. И вообще сахар очень вредный."
    "Просто, если человек пьёт минимум по две кружки кофе в день, это сколько же он потребляет сахара и кофеина в год? Ужас полный."
    "Тем более кофе очень дорогой. Да, хороший чай стоит около десяти тысяч за килограмм, но для меня это нормально. Ведь ста грамм чая мне хватает на месяц (хотя я не считал точно)."
    "А кофе со сгущёнкой? Это же вообще смерть!"
    "В общем, не понимаю кофе. И людей, которые его пьют."
    menu:
        "Что-то так захотелось в шашки партию сыграть. Может пойти поиграть с Яной?"
        "Отличная идея":
            "Я иду в комнату Яны"
            play sound door
            y "Дай угадаю, закончились чистые ложки?"
            D "Не, недавно я переосмыслил всё, и понял, что ложки теперь мне не нужны."
            y "Это почему?"
            D "Ну....... Мне просто лень их мыть, да и погружать в улун что-то металлическое - такая себе идея. Не уверен, что это влияет на вкус, но всё же."
            y "Да ладно, тебе просто лень их мыть."
            D "Ладно, ты меня раскусила."
            y "Окей, раз это не ложки, то наверное ты пришёл ругать меня за эклеры, да?"
            D "Что? Так, подожди..... Ты что, съела все эклеры?"
            y "Ну они просто так лежали грустно в холодильнике. Вот я и решила...."
            D "Беспредел. Там ведь две штуки оставалось. Один тебе, один мне. Ну лан, проехали."
            "Не ожидал такого предательства. Это же эклеры с заварным кремом! Не со сгущёнкой! С заварным кремом!"
            "Уже поворачиваюсь чтобы уйти, но потом вспоминаю про шашки. Нужно забрать их из рук этой коварной девушки!!!"
            D "За мной скоро Саня зайдёт, дай шашки. Пожалуйста."
            y "Минуту. Так, куда я могла их деть?"
            "Проходит около тридцати минут, и Яна находит шашки"
            y "На, держи. Не хочешь партейку сыграть?"
            D "Нет, спасибо. Мне нужно переосмыслить некоторые моменты жизни. Например доверие."
            y "Ой, да ладно тебе. Схожу я за эклерами завтра."
            D "Я то не обижаюсь. Но пунктик карандашиком поставил."
            y "Ладно, за чаем тоже схожу."
            D "Вот это уже другой разговор. Дело закрыто. Подсудимый оправдан."
            "У меня получилось сказать это весьма серьёзным и грозным голосом. От чего Яна начинает заливаться смехом."
            $ yanaPoints += 1
            play sound door
            "Я выхожу с шашками и победным настроением."
            "Остаток времени я провожу обдумывая самые странные аспекты жизни. Как обычно. На самом деле в жизни столько странных вещей. Иногда это даже пугает."
            s "Ого, как необычно. Даня лежит на кровати и думает. Давно такого не было."
            D "Вот этот твой пассивно-агрессивный сарказм...... Как бы так сказать..."
            s "Да понял я, понял. Ты шашки взял?"
            D "Ага, выдвигаемся?"
            s "Пошли."
            jump v1_s4
            
        "Не, играть буду с Саней попозже":
            "Как бы я не любил настольные игры, но весь день играть в шашки - такое себе. Поэтому лучше полежу на кровати."
            "Вчера вечером мы с Яной неплохо поиграли. Я не тот человек, который считает очки, количество побед и т.д. Но не могу не заметить, что Яна стала играть намного лучше."
            "Она даже выдала три победы подряд. Наверное первый раз за всё время."
            "Сначала я думал, что она мне поддаётся, но затем это ощущение быстро развеялось. Может это со мной что-то не так? Я вроде не сильно стараюсь. Да и проигрывать не боюсь."
            "Тем более, когда слышу как она радуется каждой победе. Иногда я даже поддавался. Просто чтобы сделать кого-то счастливее."
            "Остаток времени я провожу обдумывая самые странные аспекты жизни. Как обычно. На самом деле в жизни столько странных вещей. Иногда это даже пугает."
            s "Ого, как необычно. Даня лежит на кровати и думает. Давно такого не было."
            D "Вот этот твой пассивно-агрессивный сарказм...... Как бы так сказать..."
            s "Да понял я, понял. Ты шашки взял?"
            D "Нет, мы вчера с Яной играли, так что возьми у неё."
            s "Окей, пойду спрошу."
            "Саня идёт в соседнюю комнату, спустя пару минут возвращается с шашками."
            if yanaPoints < 0:
                s "Какая-то Яна сегодня задумчивая. У неё что-то случилось?"
                D "Ага, повышение случилось."
                s "Рад за неё."
            jump v1_s4

label v1_s4:
    "Я не очень быстро, да и не очень аккуратно одеваюсь, и через всего лишь тридцать минут мы выходим на улицу."
    play sound traffic
    "Свежий воздух, наконец-то. Я весьма опечален тем, что дождь прошёл, но зато можно не торопиться."
    s "Как пойдём? Подлиннее или покороче?"
    menu:
        "Погода хорошая, можно и подольше погулять":
            D "Давай через парк, сегодня очень свежо."
            s "Как скажешь. Ну как там у тебя с адаптацией?"
            D "Да так, потихоньку. Раньше я и мечтать не мог о таком большом количестве времени. Можно многое обдумать."
            s "Представляю. Уже чувствуешь, как начинаешь лучше слышать?"
            D "Ага, потихоньку превращаюсь в инопланетянина. Скоро третья рука вырастет."
            "Саню это рассмешило. Даже слишком."
            D "Ну, а если серьёзно, то могу сказать, что твой дезодорант я учуял с порога."
            s "Даже не знаю хорошо это или плохо. Ну, раз уж об этом разговор, как тебе?"
            D "Ну не знаю. Слишком сильный запах, наверное. А ты пробовал тот, которым я пользуюсь?"
            s "Думаешь, я знаю каким ты дезиком пользуешься?"
            D "Да ты у меня дома практически каждые выходные проводишь, мог бы и заметить в ванной."
            s "Ну ладно, ладно, а каким ты пользуешься?"
            D "Понятия не имею. Я просто говорю Яне взять тот, который до этого был."
            s "Ладно, когда буду у тебя дома, посмотрю."
            "Тема для разговора себя изжила."
            D "А что ты эти два часа делал? Что-то очень важное?"
            s "Это ты с чего взял?"
            D "Ну, раз сразу не пошёл за мной, значит дело очень важное."
            s "Ха-ха-ха, ну, весьма логично. Я бегал курсовую печатать. Препод наконец-то дал зелёный свет."
            D "Как оценил?"
            s "Незаслуженный \"хор\""
            D "Неплохо..."
            s "\"Неплохо\"?!?! Да я целый месяц убил на него. Знаешь за что препод снизил оценку на балл?"
            D "Валяй."
            s "За то, что в источниках я указал фамилию, отчество и имя автора."
            D "Вот тут не понял."
            s "А надо было указать фамилию, имя и отчество."
            D "Ну это всё меняет. Тебе ещё повезло, что он на пересдачу не отправил. Такая серьёзная ошибка. Как ты мог?!?!"
            s "Вот всё тебе в шутку надо превратить."
            D "Ну ладно, ладно. Может ему твой дезик не понравился просто."
            s "Очень смешно."
        "Не, лучше сразу к Сане пойти":
            D "Давай по короткому, хочу быстрее шашки разложить."
            s "Понял, принял."
            s "Я тут недавно курсовую наконец-то доделал, хочешь расскажу про что она?"
            s "Валяй."
        "Весь оставшийся путь я слушаю краткое описание курсовой работы Сани. Действительно, работа была проделана титаническая. Не ожидал от него такого."
    jump v1_s5

label v1_s5:
    play sound door
    "Итак, мы заходим в квартиру.иЯ снимаю ветровку и отдаю её Сане. Так как здесь я не могу свободно ориентироваться, приходится ходить вдоль стен."
    "Саня ведёт меня в свою комнату"
    s "Так, ты садись пока, а я пойду сделаю нам что-нибудь."
    D "Это \"что-нибудь\" будет вискарём с колой?"
    s "А как жеш. Тебе как обычно, по минимуму?"
    D "Ага, шот на стакан. Только в этот раз давай безо льда."
    s "Будет сделано, разложи шашки пока."
    "Я достаю коробку модифицированных шашек и начинаю раскладывать фигуры. Это смесь двух наборов, так что белые и чёрные фигуры можно легко различить даже не видя их."
    "Также на поле есть наклейки на черных клетках, что делает их больше. Это не сильно помогает, так как во время партий, я обычно держу ситуацию на поле у себя в голове."
    "Конечно, мне далеко до шахматистов, которые могут играть партии просто называя ходу друг другу, но с шашками я уже справляюсь и без зрения."
    "С кухни доносится звон стаканов и льда. Через минуту Саня возвращается. Бакалы осторожно ставятся на стол."
    s "Уже всё подготовил? "
    D "Ага, ты уже морально готов к поражению?"
    s "Ха-ха, это мы ещё увидим."
    "Партия длится не слишком долго, исход меня совсем не удивил."
    D "Ты прямо любишь подставляться."
    s "Это я не разогрелся ещё. Давай следующую."
    "В этой партии я совершил ошибку."
    s "Ну вот, я же говорил! Сейчас две подряд сделаю."
    "В середине партии Саня начинает весьма интересный разговор."
    s "Слушай, я в воскресенье собираюсь тут маленькое мероприятие устроить. Отпраздновать сдачу курсовой так сказать."
    D "Учитывая то, что сейчас сентябрь, я бы назвал это \"пересдачей\" курсовой."
    s "Ну вот надо тебе на больное давить? Я ещё от оценки не отошёл."
    D "Ладно, ладно, что намечается?"
    s "В общем я планирую позвать человек пятнадцать, все скидываются, но так как я тебе должен, можешь не скидываться."
    D "Интересно как ты уместишь такое большое количество людей в одной трёшке. Ну ладно, я в воскресенье не занят, так что, думаю, смогу."
    s "Ого, я думал, что придётся тебя уговаривать. Решил перестать сидеть целыми днями дома?"
    D "Просто попробую найти человека, который сможет меня выиграть в шашки."
    s "Ну, пара человек на примете есть, если ты об этом. Есть даже одна девушка шахматистка. Кстати вот ты и подставился."
    "На секунду я отвлёкся мыслью об шахматистке, чем Саня и воспользовался. Разве девушка, которая хорошо играет в шахматы, будет ходить по квартирам друзей? Интересно."
    s "Два - один, Дань, ты сегодня не в духе?"
    D "Ничего, ничего, сейчас отыграюсь!"
    "Следующие две партии я пытаюсь выровнять счёт. Что у меня успешно получается. Но мысли об воскресенье не дают мне покоя. Нужно ли было соглашаться? Как люди примут пою слепоту?"
    "Знакомиться я не любил всегда. Может стоит поменять своё отношение к этому? Завтра об этом подумаю."
    D "Ты мог две шашки съесть вот тут."
    s "Да? А это манёвр такой. Чтобы сбить оппонента с толку."
    D "Ха-ха-ха, ну ладно, ответ принимае..."
    "Не успеваю я договорить, как Саня берёт три мои шашки. Действительно сбил с толку."
    D "Ого, неплохо, неплохо. Я тебя недооценил, ну ничего, сейчас отыграюсь."
    "Следующие два-три часа мы проводим за партиями в шашки. Было очень весело."
    D "Ладно, я пойду наверное, проводишь?"
    s "Конечно! Только шашки соберу."
    "Саня собирает шашки, отдаёт их мне вместе с ветровкой, и мы вместе идём до моей квартиры."
    s "Неплохо сегодня отыграли, есть на завтра планы?"
    D "Утром у меня шоппинг с Яной, а потом я свободен."
    s "Созвонимся тогда завтра."
    D "Ага."
    play sound door
    D "Ян, ты дома?"
    "Конечно, я слышу, как она перебирает какие-то бумаги в своей комнате, но ради приличия всё равно надо было спросить. Яна подходит ко мне, снимает с меня ветровку."
    y "Ну как сегодня? Саша смог взять реванш?"
    D "После десятой партии я перестал считать победы. Ну, могу сказать, что он стал лучше играть."
    D "В отличие от некоторых."
    y "Ой, да ну тебя. В крестики-нолики я тебя постоянно обыгрываю."
    "Хотел бы я сказать, что это из-за того, что Яна всегда первая ходит, но в некоторых партиях, даже когда я первый ходил, она побеждала."
    D "Ну тут не могу не согласиться. Ладно, пойду спать."
    y "Давай. Спокойной ночи."
    D "Спокойной."
    "Ежедневная рутина по чистке зубов, принятию душа и переодевания пролетает незаметно, и вот я уже лежу на кровати."
    # Дань, раздели этот файл на три (init start vol1)
    return
    