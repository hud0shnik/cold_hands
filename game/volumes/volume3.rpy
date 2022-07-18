# Утро третьего дня
label v3_s1:
    "Удивительно, но проснулся я сам."
    "И сколько сейчас времени? Саня должен был зайти за мной в 9:50."
    "Неужели я так рано проснулся?"
    "Для начала нужно спросить Яну."
    play sound door
    D "{size=-10}Ян, ты здесь?{/size}"
    "..."
    "Ну да, она спит."
    "Яна встаёт в девять часов каждый день, так что по ней можно неплохо ориентироваться во времени сутра."
    if event1 == True:
        "Ох, хорошо, что я не стал дослушивать тот детектив, а то вообще не уснул бы."
        $ event1 = False
    else:
        "Может я так рано встал из-за того, что перед сном слушал тот странный детектив?"
    "Так или иначе, пойду чай заварю."
    play sound door
        
    play sound tea0
    "Я наливаю воду в чайник и включаю его. Наверное можно уже считать его членом семьи."
    "Осталось только начать с ним здороваться. Блин, забыл спросить Яну про накипь."
    "Я прямо уверен, что на дне уже образовался сантиметр накипи. Ладно, завтра точно займусь этим."

    menu:
        "Какой выбрать сегодня?"
        "{b}Молочный улун{/b}" if milkOolong > 2:
            "Ну, большой красный халат подождёт. Надо будет его Сане отдать, похоже я выбрал свой любимый улун."
            "Положу наверное сегодня побольше листьев."
            $ milkOolong += 1
            "Я достаю кружку, бросаю в неё горсть молочного улуна, кладу руку на чайник."
        "Дзинь Сюань" if milkOolong <= 2 :
            "Вообще, у молочного улуна очень много противников. Вроде это самый популярный ароматизированный чай."
            "Его не томят в молоке, не поливают им кусты. Просто на одной из стадий к чаю добавляется ароматизатор."
            "Из-за этого многие его не любят. В моём случае всё намного интереснее."
            "Я покупаю молочный улун в чайном магазине в соседнем районе. Продавец там очень много хвалил этот чай."
            "Натуральные ароматизаторы, никакой химии."
            "В целом, я верю ему."
            "Достаю кружку, бросаю в неё пару листьев улуна, кладу руку на чайник."
            $ milkOolong += 1
        "Да Хун Пао":
            "Классика в мире улунов. Жалко только, что стоит дорого. Хотя, учитывая то, сколько листьев я кладу на пол литра воды ..."
            "Весьма недорого."
            "Я достаю кружку, бросаю в неё пару продольно скрученных листьев, кладу руку на чайник."

    play sound tea1
    "Осталось залить листья и подождать."
    "Может размешать их ложкой? Так они заварятся быстрее."
    "Не, не хватало ещё привкуса стали. Времени у меня много, подожду."
    stop sound fadeout 1
    "Да, надо прекращать пить чай на голодный желудок."
    "Кстати, в холодильнике должны были остаться эклеры."
    "Я достаю пару штук из холодильника. Вот и завтрак намутил."
    "Вообще, не мне стоит переживать о здоровье. Люди рано или поздно умирают. От всех бед не спастись."
    "В этом плане я и до произошедшего был гедонистом. От жизни нужно получать удовольствие, иначе я не вижу в ней смысла."
    "Ну, да, самопожертвование жизнь ради идеи и прочее тоже стоит рассматривать, но это не мой путь."
    "Может быть я слишком пессимистично настроен?"
    if coldPoints >= 3:
        "А может это с другими людьми что-то не так?"
    elif mindPoints >= 3:
        "Наверное так и есть."
    else:
        "С другой стороны, я вроде всегда таким был."
    "Следующие полчаса я провожу в размышлениях на эту тему."

    jump v3_s2


label v3_s2:
    show y 1-1 at center with moveinleft
    y "Без меня эклеры ешь, да?"
    y 1-2 "Я думала ты не злопамятный."
    D "Просто завтракаю. Тебе половину оставил."
    y "Завтракают обычно кашей, яичницей или йогуртом хотя бы."
    D "Не переживай, об этом я уже подумал."
    y 1-7 "И что надумал?"
    D "Я - гедонист."
    y 2-3 "Даже спрашивать не буду."
    D "Да ладно, ты же в меде училась, у вас там должна была быть философия."
    y 3-1 "Ага, на втором курсе."
    D "А, ну да."
    D "Энивей, не подскажешь время?"
    y 1-1 "Конечно. Без пятнадцати десять."
    D "Вот знаешь, никогда не любил такие приколы со временем."
    y 2-6 "А что тебя не устраивает?"
    D "Ну, 9:45 звучит понятнее, не нужно считать ничего."
    y "Ой, ну не знаю, сколько себя знаю, всегда говорила без пятнадцати десять."
    D "Окей, тогда как ты назовёшь 9:50?"
    y 3-3 "Без десяти десять."
    D "Ничего не смущает?"
    y "Да не, нормально вроде."
    D "Ну как может быть без десяти десять, если это ноль."
    y 1-4 "Ха-ха-ха, ну так-то да, но не в нашем случае."
    D "..."
    "Что-то меня не туда унесло."
    D "Ладно, скоро за мной Саня придёт, надо собираться."
    y 2-0 "Ой, надо тебе угля дать."
    D "Ну я же не буду там водку хлестать."
    y "Так я может и не тебе, вдруг кому понадобится."
    D "Как скажешь. Если найдёшь, положи на зеркало."
    hide y with moveinleft
    play sound door

    "И, вот, я снова в своей комнате."
    "Кое-как переодеваюсь."
    "Слышу, что Саня уже пришёл. Они с Яной о чем-то разговаривают в зале."

    play sound door

    show sn 1-1 at left2 # Намутить эффектов
    show y 1-1 at right2
    D "Уже всё закупил?"
    s 1-5 "И тебе доброе утро."
    y 1-4 "Так, ладно, у меня очень важные дела, я пойду."
    D "Ага, удачи в познании."
    hide y with moveoutright
    s "До меня что-то не дошло."
    D "По дороге расскажу."
    show sn 2-5 at center with moveinleft
    s "Окей. Так, вижу ты уже готов, шашки брать будешь?"
    D "Да ладно тебе, мы же в клуб настольных игр идём."
    s 2-3 "Неожиданно, ну ладно."
    D "Хотя в ДнД я бы поиграл."
    s 1-1 "Ой, а это хорошая идея. Но не сегодня."
    D "Ну, это понятно."
    "Мы идём к выходу."
    s 1-5 "Это что, две пачки активированного угля?"
    D "Ага, Яна дала на всякий."
    s 1-1 "Блин, она думает, что мы там по полной бухать будем?"
    D "Не думаю. Просто подстраховаться не помешает."
    s 1-5 "Безусловно."
    
    jump v3_s3

label v3_s3:
    "По дороге я рассказываю Сане о повышении Яны."
    "В этот раз мы пришли намного быстрее. По понятным причинам."
    s "Пока никого нет. Я пообещал встретить всех на остановке."
    D "Так уж и быть, отпущу тебя."
    s "Ты тут один точно справишься?"
    D "Ну, планирую просто сидеть и залипать."
    s "Звучит как план."
    play sound door
    "Не очень приятная ситуация. Саня ушёл, в его квартире я не разбираюсь, да и нервничаю немного."
    "Больше всего не люблю такие моменты."
    "Ещё когда я ходил в университет, я торопился первым пойти отвечать на экзамене."
    "Потому что я шарил за предметы и мог ответить? Нет."
    "Потому что я хотел как можно быстрее узнать результат. Чего бы мне это не стоило."
    "Я бы не назвал себя человеком, который любит накручивать себя."
    "Просто не вижу ничего хорошего в ожидании. Может быть я просто очень нетерпеливый."
    "С другой стороны пока что я могу отрепетировать то, что буду говорить, какие темы поднимать в разговоре."
    "Как я представлюсь и прочее."
    "..."
    "Не, так заморачиваться я не буду. Я же не на собеседовании, просто сижу в квартире кореша."
    "Скоро придут его друзья, мы будем разговаривать. Ничего сложного."
    "Да, похоже я всё таки из тех, кто накручивает себя."
    "Энивей, надо сменить тему."
    "Вот, кстати, всегда интересно было, другие люди тоже проговаривают свои мысли в голове?"
    "Просто скорость передачи сигналов нейронами намного выше скорости проговаривания мыслей."
    "Причём если перестать это делать, то будешь думать быстрее. Наверное."
    "Мне кажется это неуместным в моём случае: времени у меня много, а клиповое мышление - зло."
    "Не хочу становиться человеком, который не может нормально сконцентрироваться на чём-то одном."
    "Хотя вряд ли мне это светит. Сейчас мне физически не на что отвлекаться."
    "И из-за этого я скорее всего сойду с ума."
    if mindPoints < 2:
        "Мне точно нужно больше проводить времени за разговорами с другими."
        
    play sound keys
    "Проходит ещё какое-то время. Из мыслей меня вырывают звуки ключей."
    stop sound fadeout 1

    play sound door
    s "А вот и мы!"
    s "Так, раковина вот там, вещи можете оставить здесь."
    s "Как помоете руки, присоединяйтесь к Дане, он уже за столом."
    "Я ещё не способен определять количество людей по звукам, но вроде пока я слышу минимум пятерых."
    "Не то, чтобы меня это пугало, в школьные годы я был очень общительным."
    "Просто теперь всё немного по-другому."
    "Люди постепенно садятся за стол."
    D "Сразу со всеми поздороваюсь. Всем привет, я Даня. Скорее всего, Саня уже всё обо мне вам рассказал."
    nm "А то! Столько историй рассказывал."
    nf "Ага, приятно познакомиться, Дань."
    s "Собственно, то, из-за чего мы собрались."
    s "Сегодня мы собрались чтобы отпраздновать то, что теперь я свободен."
    s "Курсовая закрыта, теперь у меня вообще нет долгов. Свободный человек."
    "Следующие десять-двадцать минут все за столом обсуждают курсовую Сани."
    "Всё оказалось намного проще. Приятно."
    D "Сань, оформи мне два куска пепперони, будь добор."
    s "Конечно! Одну минуту."
    s "Кстати, может тебе вискаря с колой ещё?"
    D "Ой, было бы вообще прекрасно."
    "Через какое-то время передо мной появляются два куска пиццы и хайболл."
    "Вообще, мне больше нравится гавайская пицца, но таких же гурманов сегодня среди нас нет, так что Саня просто заказал 5-6 коробок пепперони."
    "В целом, я не против."
    "Следующие полчаса пролетают за историями из детства. Классика."
    "Энивей, самая сложная часть закончилась. Все разбились по 2-3 человека и разбрелись по квартире, так что можно выловить Саню и выяснить пару вопросиков."
    jump v3_s4

label v3_s4:
    s "Дань, давай сюда, хочу тебя кое с кем познакомить."
    "Он меня опередил."
    s "Даня не очень общительный в большой компании, но наедине он может часами трещать."
    s "Ещё мы с ним играем в шашки практически шесть дней в неделе."
    nf "Ого, я думала сейчас уже никто не играет в шашки."
    if mindPoints >= 2:
        "..."
    else:
        D "Да ладно тебе, не самая сложная игра, тем более шашки, в отличие ДнД, есть практически у каждого."
        "Ой, а я даже не спросил имени."
        s "Даже представиться времени не дал."
    s "Это Аня, она учится на нейробиолога и раньше играла в шахматы."
    s "Прямо серьёзно играла."
    s "Прямо с турнирами, кубками и поездками в Китай."
    a "Ой, да ладно тебе, до поездок так и не дошло."
    D "Ого..."
    s "Так, ладно, мне нужно срочно переговорить с одним человечком, так что я вас оставлю."
    D "Окей."
    "Саня нас покинул."
    D "Нейробиолог, да? Наверное вообще свободного времени нет."
    a "Я бы так не сказала, пока ничего серьёзного нам не преподают."
    a "Так что свободного времени у меня хватает."
    D "И как же ты его убиваешь?"
    a "У меня есть несколько хобби."
    a "Чаще всего я читаю книги. Нет, не про нейробиологию или психологию."
    D "Художку?"
    a "Ага, романы, приключения, иногда детективы."
    D "На тему последних у нас ещё будет разговор."
    a "Ой, ты тоже любитель литературы?"
    D "Агась, в наше время это не очень распространённая черта, но времени у меня много."
    D "Так что периодически обращаюсь к аудиокнигам."
    D "Энивей, кроме книг, чем ты ещё занимаешься в свободное время?"
    "В принципе этого уже достаточно, чтобы я мог начать беседу на минимум два часа. Но интерес берёт верх надо мной."
    a "Уже около месяца я учусь писать маслом. Я учусь этому сама. Только вот цены на масло явно против этого."
    "Не уверен, что она это заметила, но я немного улыбнулся. Очень комичная ситуация. Художник против капитализма."
    "Об визуальном искусстве я поддержать диалог не могу, хотя раньше частенько ходил в Третьяковку. Так что лучше промолчу."
    a "На день рождения мне подарили цифровое пианино, но я его ещё даже не распаковала."
    D "Недавно отмечала?"
    a "Два месяца назад."
    "Оу."
    a "Наверное я просто боюсь снова проходить через путь ошибок"
    D "В формировании новых привычек?"
    a "Похоже на то."
    a "Так, теперь твоя очередь."
    D "Ну, у меня всё очень просто. Днями пью улуны под аудиокниги, да и просто так. Почти каждый день играю на гитаре."
    D "Но только то, что раньше умел, учить что-то новое слишком сложно."
    D "Собираю кубик-рубика иногда. Моя подруга подписала стороны, так что это не очень сложно."
    D "Про то, что мы с Саней часто играем в шашки он уже рассказал наверное."
    D "Я очень люблю настолки, вот только шансы поиграть выпадают крайне редко."
    a "Ого, много у тебя свободного времени."
    D "Ну, из универа я отчислился, а идти в институт для инвалидов не сильно хочу."
    D "Целыми днями дома сижу, вот и занимаю себя чем могу."
    D "Хочу устроиться в пекарню консультантом по чаям, на следующей неделе собеседование."
    a "А как ты будешь добираться до работы?"
    D "Моя подруга устроилась туда менеджером, так что с этим проблем не будет."
    a "Звучит очень интересно. Хотела бы я работать в пекарне."
    D "Вместо нейробиолога?"
    a "Нет конечно. На время учёбы. Запах выпечки, никакой офисной рутины."
    D "А почему тогда не устроишься?"
    a "Из меня плохой продавец, да и консультант не особо хороший."
    a "Честно говоря я не очень социальный человек."
    D "Ты же сейчас говоришь со мной, а мы знакомы меньше часа."
    a "Я скорее про общение с большим количеством человек."
    D "Тогда ты не будешь против, если мы переместимся на балкон, да?"
    "Стоять и разговаривать у всех на виду... Не, не моё."
    a "Почему бы и нет."
    jump v3_s5

label v3_s5:

    play sound door
    play music rain
    "Аня провела меня на балкон."
    D "Осенний дождь, прекрасно."
    a "Мне тоже нравится."
    a "Только если я не на улице в это время, конечно."
    D "Да ладно тебе, ты никогда не попадала под теплый дождь?"
    a "Скажем так, я бы выбрала сидеть дома и пить что-то горячее, чем мокнуть под дождём."
    D "С этим сложно поспорить."
    a "Дань, у тебя много друзей?"
    "Немного неожиданный вопрос."
    D "Ну, после того, что случилось у меня остались только Саня и Яна."
    D "Мы знакомы со средней школы, она снимает у меня комнату за уход, готовку и прочее."
    D "Так что мой ответ - 2."
    a "Обгоняешь меня на одного."
    D "Неужели из друзей у тебя только подруга, которая пригласила тебя?"
    a "Ага, я же говорила. Не очень социальный человек."
    D "Но ведь сейчас ты познакомилась с новым человеком."
    a "Во-первых это Саша нас познакомил."
    a "Во-вторых я выпила уже две бутылки сидра."
    D "Неплохой способ против замкнутости."
    a "А то."
    a "Вообще не понимаю как люди знакомятся в кафе, барах или торговых центрах."
    D "Тут я с тобой согласен. Какая-то секретная социальная техника."
    a "То есть они выбирают с кем познакомится только по внешности, но ведь это нечестно."
    D "И неправильно, но в таком мире мы живём."
    a "Ага, в неправильном и несправедливом."
    D "Капиталистическое общество потребления, ничего удивительного."
    a "Ой, так ты разбираешься в философии?"
    D "Нет, не разбираюсь, просто читал пару книг."
    "Следующий час мы обсуждаем пост-модерн и современное общество."
    play sound door
    s "Ой, я вам помешал, да?"
    s "Мы собираемся поехать в бар, вы с нами?"
    D "Я точно минус, Сань, сам понимаешь."
    a "Мне уже пора домой, извини."
    s "Понял принял."
    play sound door
    D "Да и мне пора уже наверное."
    D "Спасибо за беседу, всегда приятно пообщаться на такие широкие темы."
    a "Мне тоже."
    D "Могу я взять у тебя номер?"
    a "Ой, конечно, давай телефон."
    "Достаю свой прекрасный ретро-мобильник."
    D "Держи, настоящий олдскул."
    "Аня клацает по кнопкам телефона."
    a "Всё, если что, звони."
    D "Ага."
    stop music fadeout 1
    play sound door
    "Мы выходим из балкона."
    s "Так, все в сборе?"
    nm "Конечно в сборе!"
    s "Тогда я пойдёмте."
    play sound door
    "Мы всей компанией идём сначала до моего дома. Дождь уже почти закончился."
    s "Так, я пойду провожу Даню, а вы пока ждите тут."
    D "Всем пока."
    nm "Пока."
    nf "Давай."
    a "Пока, Дань."
    "Мы с Саней поднимаемся в лифте вдвоём."
    s "Как тебе Аня?"
    if mindPoints >=3:
        D "Нормально. Только без вискаря я бы к ней даже не подошёл."
        s "Зато сколько болтали. Я тебя вообще-то ещё с остальными хотел познакомить."
    else:
        D "Приятная девушка с интересными взглядами на жизнь."
    D "даже номер её взял."
    s "Быстро ты. Молодца!"
    D "Пока не забыл, забей её на быстрый набор."
    s "А, да, точно, секунду."
    "..."
    s "Всё, поставил её на четвёрочку."
    D "Спасибо."
    s "Да не за что."
    play sound door
    y "Уже пришли?"
    D "Ага."
    y "Саш, с поздравляю с победой!"
    s "Хех, спасибо."
    s "Ладно, я пойду."
    D "Пока, Сань."
    y "Удачи."
    s "Пока."
    jump v3_s6

label v3_s6:

    return