# Утро второго дня
label v2_s1:

    "Вот и наступило утро субботы. Я просыпаюсь от того, что меня будит Яна."
    show y 1-2 at center with moveinbottom
    y "Дань, уже почти десять. Мы за покупками пойдём?"
    D "А, что? А, ага, да, сейчас."
    "Видимо хорошо вчера с Саней посидели."
    "Проделав все утренние процедуры, я надеваю ветровку."
    y "Пошли?"
    D "Ага."
    hide y with moveoutleft
    play sound door
    show y 1-1 at left2 with moveinleft
    "Так как я стараюсь в последнее время всё больше покидать квартиру, я хожу за покупками вместе с Яной."
    "И, вот, мы уже дошли до магазина. Людей сегодня не так много. Похоже все высыпаются после пятницы, хе-хе."
    y 3-6 "Так, я вчера написала список, так что пойдём по нему."
    D "Что-то я не припомню, чтобы раньше ты писала списки."
    y 2-3 "Стараюсь быть более ответственной. Формирую полезные привычки."
    D "Неплохо, неплохо. С чего начнём?"
    y 2-0 "С яблок."
    "Мы неспешно прогуливаемся по магазину."
    D "Ян, а ты сможешь чизкейк сделать?"
    y 1-4 "Ну, я уже делала пару раз чизкейки, так что думаю да."
    D "Если бы ты приготовила на следующей неделе чизкейк, было бы очень приятно."
    y 1-1 "Договорились. Так, теперь нужно вернуться в раздел с молочкой."
    "Ещё какое-то время мы ходим по магазину. Идём на кассу, оплачиваем покупки, и выходим на улицу."
    y 2-1 "В пекарню я итак сегодня пойду, так что эклеры принесу после собеса."
    D "Ой, как удобно."
    y 1-4 "Ага. Кстати, а почему ты хочешь, чтобы я сделала чизкейк на следующей неделе? Я же могу в воскресенье этим заняться."
    D "В воскресенье я буду немного занят. Саня хочет отпраздновать сдачу курсовой."
    y 2-6 "Сдачу? Осенью?"
    D "Ну, пересдачу."
    y 1-2 "Отмечать пересдачу? Весело. Когда домой вернёшься?"
    D "Пока не знаю. Саня меня приведёт, если ты об этом."
    y 1-7 "Да нет, я скорее о том, что не похоже это всё на тебя. Давно ты стал любить вечеринки?"
    D "Может теперь я стану самым общительным человеком во всей Москве."
    y 2-3 "Всё может быть. Только с ночёвкой не оставайся там. А то, если сутра тебя не будет, я инфаркт схвачу."
    D "Ну, я не просто так ношу мобилу с собой. Если что, звони."
    y 1-2 "Угу."
    "Мы возвращаемся домой."

    jump v2_s2

# Сцена после похода в магазин
label v2_s2:

    play sound door
    hide y with moveoutleft
    "Яна идёт разбирать продукты. Она весьма быстро разбирается с этим."
    show y 1-1 at center with moveinleft
    y "Я тогда пойду готовиться к собеседованию."
    D "А ты разве не получила уже оффер?"
    y 2-1 "Получила, конечно, но мало ли..."
    hide y with moveoutright
    "Я остаюсь один на кухне. Идей у меня сейчас не очень много."
    menu:
        "Пойти приободрить Яну" if coldPoints <= 1:
            jump v2_s2_yana
        "Сварить чашку улуна":
            jump v2_s2_oolong
        "Пойти на балкон":
            jump v2_s2_mind
        "Кубик рубика?":
            jump v2_s2_rubik

# Игрок выбирает "Поддержать Яну перед собесом"
label v2_s2_yana:

    play sound door
    show y 1-5 at center with fade
    D "Как настроение?"
    y "Нервничаю немного. В \"Шалфее\" я работала одна, виделась только с начальницей и парой девочек, которые меня сменяли."
    y 2-1 "Теперь придётся знакомиться со всеми работниками. Я ведь буду менеджером."
    y "Надеюсь у меня получится влиться в коллектив."
    D "Ну, учитывая твою общительность, могу с уверенностью сказать, что всё у тебя получится. Не переживай."
    y 1-1 "Ого, приободрил даже."
    "В этот момент мне становится немного неловко, я решаю сменить тему."
    D "Кстати, как звонок прошёл?"
    y 2-1 "Начальнице \"Шалфея\"? Ну она расстроилась, но после того как я объяснила ситуацию, она поняла и пожелала удачи на новом месте."
    D "И никакой волокиты с бумагами?"
    y 2-4 "В современном мире без волокиты с бумагами ничто не работает, забыл? Пришлось вчера поехать решать вопросы в затопленный торговый центр."
    D "Неужели я так долго просидел за шашками с Саней?"
    y 1-1 "Да не особо, просто начальница всё приготовила к моему приезду."
    D "Ой, как приятно."
    y 1-4 "Ага, вот в такие моменты понимаешь, что этой работы тебе будет не хватать."
    $ yanaPoints += 1

    menu:
        "И снова неловкое молчание."
        "Спросить о планах":
            D "Как там твои планы? Уже выбрала страну для переезда?"
            y 2-3 "Не особо. Будет весьма тяжело найти работу за границей с российским дипломом."
            D "Да ладно тебе, я в этом не сильно разбираюсь, но диплом по специальности точно хуже не сделает."
            y 3-3 "Это да. Хочу в Америку или Канаду. Но на это нужно очень много денег."
            D "Ну, английским ты владеешь хорошо, так что одной проблемой меньше."
            y 1-2 "Я бы так не сказала, нужно будет сдать экзамен на знание языка."
            D "Как-то ты пессимистично настроена."
            y "Просто я ещё не решилась, такие серьёзные вопросы за один день не решаются."
            D "Это да. Ладно, не буду тебя отвлекать, удачи на собесе."
            y 1-1 "Спасибо!"

        "Похвалить":
            D "Я понимаю, ты очень переживаешь из-за новой работы. И тебе грустно из-за потери старой."
            D "Но ты хороший человек, и я уверен в том, что у тебя всё получится."
            D "Я знаю тебя со средней школы. И ты всегда находила общий язык с людьми, не переживай."
            "Так, что-то меня не туда понесло уже. Нужно валить, а то ещё лишнего наговорю."
            y 1-6 "Спасибо за поддержку. Правда."
            "Обнимашки? Ну ок."
            D "Давай, удачи на собесе."
            y 1-1 "Агась!"
            $ yanaPoints += 1

        "Пойти в свою комнату":
            D "Ладно, не буду тебя отвлекать, удачи на собесе."
            y 1-7 "Спасибо."

    hide y with fade
    play sound door

    jump v2_s3

# Игрок выбирает "Заварить улуна"
label v2_s2_oolong:

    "Что-то так захотелось улуна. Конечно, его нельзя пить на голодный желудок, но меня это никогда не останавливало."
    "Подходя к столу я понимаю, что проблему с выбором улуна нужно как-то решить."
    "Потому что передо мной встаёт очень сложный выбор. Я бы подбрасывал каждый раз монетку, если бы мог."
    "Может перейти на какой-то один улун? Тогда выбор станет весьма простым."

    menu:
        "Ну, пока у меня дома имеются два сорта улуна, нужно сделать выбор."
        "Большой красный халат":
            "Как я помню, Да Хун Пао - один из самых популярных улунов. Никогда не пробовал его сильно заваривать, но говорят, что тогда его шоколадные нотки сильно раскроются."
        "Молочный улун" if milkOolong != 2:
            "А мне начинает нравиться молочный улун. Раньше я его не так много пил."
            $ milkOolong += 1
        "ХОЧУ МОЛОЧНЫЙ УЛУН!" if milkOolong == 2:
            "Хочу молочный улун, очень хочу. Вот именно молочный улун хочу."
            $ milkOolong += 1

    play sound tea0
    "Я наливаю воду в чайник и включаю его. Надо будет попросить Яну посмотреть есть ли на дне накипь. Давно уже не кипятил в чайнике лимонную кислоту."
    "Так, где же я оставил свою кружку..."

    if milkOolong =< 2:
        "А, вот она. Я достаю кружку, бросаю в неё пару скрученных листьев, кладу руку на чайник."
    else:
        "А, вот она! Я достаю кружку, почти судорожно бросаю в неё пару-тройку скрученных листьев, кладу руку на чайник."
    stop sound fadeout 1

    play sound tea1
    "Осталось залить листья. Отмеряю уровень воды в кружке с помощью мизинца. Улун готов."
    stop sound fadeout 1

    "А ведь некоторые люди так и пьют всю жизнь чай в пакетиках. Засыпают две-три ложки сахара. Бррр, ужас."
    "Какое-то время я просто сижу на кухне и растягиваю улун."

    jump v2_s3

# Игрок идёт на балкон преисполняться в своём познании
label v2_s2_mind:

    "Ну, сидеть на кухне как-то скучно, пойду на балкон."
    play sound door

    menu:
        "Какую тему обдумать сегодня?"
        "О себе":
            "Ещё до случившегося я был не очень общительным. В школе у меня было максимум два друга."
            "В поздней школе я понял, что нужно вести себя более социально, но люди всё равно от меня уходили."
            "Может, быть одному - мой путь?"
            "Как бы разговоры с самим собой не казались странными, мне это помогает. Наверное."
            "Ну, как помогает, без них я бы давно с ума сошёл."
            "Я никогда не понимал людей, которые создают себе воображаемых друзей, и разговаривают с ними."
            "Мне казалось, что тульпа - изобретение от жизиков для жизиков. Но в итоге я сам стал для себя тульпой."
            "Хотя, нет, я же существую. Наверное. Ну в смысле моё тело же существует. И разум тоже."
            "Просто я люблю разговаривать сам с собой. Все так делают, просто не поднимают эту тему в разговоре."
            "Вот если бы у меня была вторая личность, с которой я бы разговаривал, тогда да, можно было бы считать меня шизофреником."
            "А я просто много думаю. Слишком много думаю."
            "Хотя, учитывая всё случившееся, это стоило ожидать. Что мне ещё делать? Идти в вуз для инвалидов? Где-то я уже это слышал."
            "Так или иначе, то, что я всё чаще возвращаюсь в свой уютный уголочек в моей голове немного настораживает."
            "Может заняться медитацией? Надо будет обдумать это."
            $ mindPoints += 1

        "О людях":
            "Никогда не понимал людей. Иногда они ведут себя прямо как персонажи какой-нибудь игры. Торопятся сутра на работу. Потом торопятся вечером домой."
            "Иногда они могут выдать что-то стоящее, но в остальном их беседы между собой весьма скучны."
            "Ну серьёзно, взять пару любых студентов в метро. О чём же они будут говорить?"
            "Об играх или учёбе. Всё. Две темы. То, что происходит с ними в вузе и то, во что они играют."
            "Возьмём двух студенток, тут ещё проще. Разговоры об учёбе и личной жизни."
            "Как будто людей больше ничего не интересует. Ни разу не видел, чтобы хоть кто-нибудь обсуждал в метро суперпозицию или симулякры."
            "Неужели я один такой? Ещё в школьные времена я обсуждал на переменах с одноклассниками космос, квантовую физику, философию."
            "Да, они не всегда могли поддержать разговор, но мне было достаточно того, что они меня слушают. И, да, я понимал, что выгляжу странно, и ожидаю слишком многого от школьников."
            "Может быть я и выгляжу как человек, стоящий по колено в грязи, и мечтающий о звёздах, но это явно интереснее, чем обсуждать преподов."
            "Неужели философов больше не осталось? Неужели бытие и его смысл больше никого не интересуют?"
            "Неужели я остался один на этой планете тупых ...... "
            "Ладно, проехали."
            "Как обычно злюсь только из-за того, что не смог найти человека, похожего на меня."
            "Хоть я и понимаю, что скорее всего никогда такого человека не найду, не нужно лишний раз лишать себя нервных клеток."
            $ coldPoints += 1

    "Ладно, пойду в комнату, а то уже как-то слишком холодно стало."
    play sound door

    jump v2_s3

# Игрок решает пойти собрать кубас
label v2_s2_rubik:

    # Если есть вопросы по этой ветке, рекомендую прочитать описание коммита 3e14a4bf11df0ed2dfd22e3228efabb6b36fc9d0
    "Я иду в свою комнату. Кубик должен лежать где-то на столе. Я плавно скольжу руками по столу..."
    "А, вот же он. Итак, начнём."
    play sound rubik
    "Вообще весьма пугает моё стремление к удержанию старых привычек. Одна мысль о том, что я больше не смогу собирать кубик рубика пугает."
    "Поэтому я попросил Яну нацарапать символы на каждой клетке. Не очень удобно, но я уже приноровился."
    "На каждой клетке нацарапана буква, которая обозначает цвет. Всего их шесть (как и сторон кубика)."
    " \"Б\" - белый, \"К\" - красный, \"С\" - синий, \"З\" - зелёный, \"О\" - оранжевый, \"Ж\" - жёлтый."
    "Вообще я был бы непротив и любых других символов. Сейчас уже мне незачем знать какого цвета грань, достаточно того, что на ней есть символ."
    "Конечно, я уже не могу собирать его за одну-две минуты. Но, есть же люди, которым достаточно один раз посмотреть на кубик, и дальше они соберут его вслепую."
    "Мне до этого далеко. Тем более я очень часто совершаю ошибки, и приходится пересобирать его, но практики каждый день помогают."
    "Месяц назад я вообще тратил около часа на сборку. Сейчас уже меньше пяти минут."
    "Все мои хобби уже стали частичкой меня, и чтобы не произошло, я не хочу их терять."
    "Тем более сборка кубика рубика неплохо разогревает мои пальцы. А руки мне теперь очень нужны."
    "Я и до всего этого понимал, что руки для меня - самая главная часть в теле. Теперь уже точно в этом уверен."
    "Также это очень весело. С каждым движением кубик издаёт очень приятный звук. Я бы не назвал это хрустом, но могу сказать точно, этот звук очень успокаивает."
    "Проходит ещё какое-то время. И, вот, кубик готов."
    stop sound fadeout 1

    jump v2_s3

# Игрок разговаривает с Саней
label v2_s3:

    "Нужно позвонить Сане. Он хотел о чём-то поговорить."
    "Набираю номер Сани зажатием одной кнопки...."
    show mb 0-0 at center with moveinleft
    s "Да-да."
    D "Ты просил тебе позвонить вчера."
    s "Агась. Ты занят сейчас?"
    "Яна уже ушла на собеседование.... Да и делать мне нечего."
    D "Да, свободен. Хочешь взять реванш в шашках?"
    show mb 0-6 at center
    s "Эй! Я вообще-то больше партий вчера выиграл!"
    D "Да? Я после тех трёх поражений подряд перестал считать партии...."
    show mb 0-0 at center
    s "Ха-ха, ну ладно, реванш ты ещё успеешь взять. Я хотел с тобой обсудить завтрашнее."
    D "Так приходи. Яна ушла, я как раз чай заварю."
    s "Ну вообще я хотел чтобы мы у меня посидели."
    D "Не, чувак, извини, но погода на улице слишком тёплая. Тем более я уже нагулялся с Яной сутра."
    s "Ладно, минут через десять приду."
    D "Договорились."
    hide mb with moveoutleft

    "Я кладу телефон на стол, сажусь на кровать. Странные мысли лезут в голову. Может я слишком сильно переживаю о завтрашнем?"
    "Проходит около двадцати минут.... или десяти? Во времени теперь ориентироваться ещё сложнее."
    play sound door
    show sn 1-2 at center with moveinleft
    s "Йо, мог бы и встретить меня."
    D "А, да, что-то задумался."
    s 1-1 "Посвятишь?"
    D "Не, как обычно...."
    s "Так или иначе, по плану мы начинаем в десять..... "
    s 1-5 "Так, подожди, ты же говорил, что заваришь чай."
    D "Эм, ну, не получилось."
    s 1-4 "Господи, чем ты тут занимался?"
    D "Проехали. Так что ты говорил? В десять начинаем?"
    s 1-1 "Ага, до десяти мне нужно будет сходить за покупками, но к назначенному времени всё будет готово."
    D "Ты же не попросишь меня сходить с тобой за алкоголем? Я не против, но смотреться будет странно."
    s "Не, с покупками мне поможет одногруппник, он работает кассиром, и сможет выбить мне скидку."
    D "Это хорошо. Будет какая-нибудь программа?"
    s 2-5 "Ага, тамаду позовём, конкурсы организуем."
    D "Ну я серьёзно."
    s 2-4 "Какая программа, Дань? Это просто обмывание сдачи курсовой. Никаких вписок, тусовок и прочего."
    D "Эх, жаль, а так хотелось..."
    s "Могу турнир по шашкам устроить, но вряд ли у тебя будет на это время."
    D "Это ещё почему?"
    s 1-2 "Потому что из парней будем только ты, я и двое одногруппников."
    D "А всего человек?"
    s 1-1 "Минимум десять."
    D "Никакого баланса, ну ладно. Вряд ли я буду знакомиться с кем-нибудь, но попробовать стоит."
    s 2-1 "Да ладно тебе, я же не школьниц позвал. У нас планируются светские посиделки вообще-то."
    D "Странное название для обмывания пересдачи."
    s "Ладно, не суть, в общем я зайду за тобой в 9:50."
    D "Ого, оставишь гостей ради меня?"
    s 1-5 "Я больше чем уверен, что никто вовремя не придёт. Мы же не в центре москвы живём, помнишь?"
    D "Это да. Ладно, договорились."
    show sn 1-1 at center
    "Следующие два часа мы проводим просто беседуя о насущном. Весьма приятно осознавать, что Саня не переживает о завтрашнем. Хотя на его плечах организация всего этого."
    s "Ну, ладно, мне пора уже."
    D "Давай, удачи с завтрашним."
    hide sn with fade
    play sound door

    "Планов у меня никаких нет. Пойду прилягу наверное."
    menu:
        "Может поспать?"
        "Идея неплохая":
            pass
        "Лучше просто полежу":
                "Откровенно говоря, я всегда имел высокую самооценку. Нет, это не гены или воспитание. Ещё в средней школе я относился с иронией к себе. Поэтому говорил, что я самый умный и красивый."
                "И в итоге на подсознательном уровне (наверное) стал стремиться, сам того не понимая. Я продолжал говорить, что являюсь самым умным человеком во всей Москве, это обычно вызывало смех, но меня всё устраивало."
                "А потом я стал действительно чего-то добиваться. И ведь добился. Вот только теперь это уже не важно."
                "Сейчас уже нет смысла учиться новой профессии, попытки рисовать ничем не увенчались, книги я могу только слушать."
                "Хотя я стал больше слушать художественные произведения. Раньше их терпеть не мог, не видел смысла, ведь можно с тем же успехом просто посмотреть сериал."
                "Иронично. Теперь аудиокниги - мой единственный выбор. Хотя, я и не против. В художественной литературе есть одна очень приятная особенность. Ты используешь своё воображение для визуализации."
                "Герои и локации выглядят так, как ты хочешь (с поправкой на описание от автора). Жалко только, что я не могу придумать голоса для персонажей так как текст за меня читает группа озвучки."
                "Вообще, мне очень печально от того, что нынешние люди вообще не воспринимают книги как формат. Безусловно, легче посмотреть фильм или сериал, но неужели люди даже не пытаются?"
                "Это ведь непередаваемое ощущение. Фактически ты используешь самый мощный визуализатор - своё воображение."
                $ coldPoints += 1
                "Ладно, теперь у меня уже реально болит голова, нужно поспать."

    scene time_skip couple_hours
    with fade
    ""
    hide window
    scene bg void
    with fade

    jump v2_s4

label v2_s4:

    play sound door
    show y 1-1 at center with fade
    y "Я вернулась."
    D "Как прошло?"
    y 1-4 "Ну, как тебе сказать. Персонал весьма дружный, владелица сразу взяла под крыло."
    y "Со следующей понедельника выхожу, буду пять дней работать с текущим менеджером, потом сама."
    D "И эти пять дней тебе не оплатят, да?"
    y 2-3 "Конечно. А ты предложил бы хозяйке платить двум менеджерам сразу?"
    D "Ну ладно, ладно. Ты эклеры принесла?"
    y 1-1 "Ага, теперь у меня есть скидочная карточка сотрудника, двадцать пять процентов на всё."
    D "Да я сам бы пошёл туда работать ради такого."
    y 1-7 "Так ты можешь."
    D "В каком месте?!"
    y "Ну, владелица уже давно нас запомнила."
    "Ещё бы она не запомнила."
    y "И сказала, что может устроить тебя консультантом по чаю."
    D "Это как?"
    y 2-0 "Ну ты будешь стоять около чайного угла и подсказывать покупателям какой чай им лучше всего подойдёт."
    D "Надо будет обдумать это. Времени у меня много, может смогу хоть начать самостоятельно оплачивать квартиру."
    y "Как надумаешь, скажи. Я буду рядом всегда, если что, помогу."
    D "Пойду с тобой в понедельник, поговорю с хозяйкой."
    y 3-0 "Ого, быстро ты."
    D "Я не устраиваться иду, просто интересно как она себе это представляет."
    y 3-6 "Но ты же согласишься на вакансию, да?"
    D "Говорить о чае и зарабатывать деньги весь день? Звучит заманчиво."
    y 1-1 "Я рада, напишу ей сейчас об этом."
    D "Агась, и ещё кое-что."
    y 2-0 "Да-да?"
    D "Завтра Саня зайдёт за мной в 9:50."
    y 2-1 "Как-то рановато ты начинаете."
    if coldPoints > 2:
        D "Все вопросы к Сане. Ладно, пойду полежу."
        y 1-2 "Ага."
        "Самое время послушать какой-нибудь детективчик."
    else:
        D "Все вопросы к Сане. Так вот, не думаю, что вернусь под час ночи, так что не переживай."
        D "Кстати, чем завтра займёшься?"
        "Не то, чтобы мне было очень интересно, просто делать нечего."
        y 3-6 "Ну, я скачала пару книг по менеджменту, так что скорее всего ..."
        D "Будешь весь день читать книги? Не похоже на тебя."
        y 2-0 "Надо расти, не всю же жизнь мыло продавать."
        D "Это да."
        "Тем для разговора у меня больше нет."
        D "Ладно, удачи тебе в познании менеджмента, а я пойду послушаю какой-нибудь детективчик."
        y 1-1 "У-у-у, расскажешь потом?"
        if coldPoints == 0:
            D "Да, конечно."
        else:
            D "Может быть."

    hide y with fade
    play sound door
    jump v2_s5

label v2_s5:

    "Я иду к себе в комнату, и меня посещает интересная мысль."
    menu:
        "Под аудиокнигу может хорошо зайти улун."
        "Не буду портить книгу улуном":
            "Улун будет лишь отвлекать от сюжета, тем более я слишком много его пью в последнее время."

        "Прекрасная идея":
            "Буду выглядеть как дешёвый циник, вместо книги - аудиокнига, вместо бокала вина - кружка чая. Но меня всё устраивает."
            menu:
                "Что же я заварю?"
                "Молочный":
                    "Конечно же мой любимый молочный улун!"
                    if milkOolong == 3:
                        "Я прямо подсел на него. Теперь буду брать только его."
                    else:
                        "Он не будет слишком сильно отвлекать меня, так что это единственный верный выбор."

                "Большой Красный":
                    "Думаю, под книгу Да Хун Пао подойдёт лучше. Он более суровый, что ли. Даже цвет у него более темный."
                    "Хотя последнее, что меня интересует теперь - это цвет."
            play sound door
            # Добавить звук заваривания чая
            "Я снова иду на кухню, и уже на автоматизме через десять минут у меня в руках появляется кружка любимого улуна."
            "Чай готов, иду в комнату."

    "У меня на плеере было около трёх детективов, но один я начал, и он мне не зашёл. Ещё один сложный выбор."

    menu:
        "Судить о аудиокниге по названию нельзя вроде как, но мне ничего не остаётся."
        "Детский лагерь":
            jump v2_s5_camp
        "Страх и ненависть в Липецке":
            jump v2_s5_fear

label v2_s5_camp:

    "История о загадочной пропаже людей в пионер-лагере."
    "Главный герой - милицейский старой закалки. После недели поисков он находит в лесу останки жертв."
    "Остались только кости. По ним в следствии экспертизы становится известно, что в этой куче не хватает одного пионера."
    menu:
        "Ужас какой. Может остановится? Я вроде просил Яну скачать мне детективы, а не ужастики..."
        "Да, не хочу знать, что там произошло":
            "Как можно писать детективы про убийства детей? Это вообще законно?"
            jump v2_s5_mind
        "Нет, я всё-таки дослушаю":
            pass

    "Итак, одного пионера не хватает в этой груде костей. Значит он - убийца."
    "Но почему он это сделал? Все вещи пионеров остались на месте. Он забрал только их тела, и оставил кости в лесу."
    "В один из вечеров главный герой решает разделится с напарником и обыскать лес. После часового похода, он слышит какие-то странные движения в кустах."
    "Резко, заметив главного героя, что-то выпрыгивает из кустов. Милиционер успевает сделать два выстрела из табельного прямо в голову ..."
    "Пропавшего пионера. В кустах он находит тело своего напарника с обглоданной рукой."
    "На этом книга заканчивается. Нет ни логического конца, ни ответа, ничего."
    "Может он просто сошёл с ума и съел всех людей в лагере? Может в этом лесу жил злой дух или что-то подобное?"
    "{i} Опять этот лес и ваш беспредел{i}."
    "Классика. Ну, я не против открытых концовок, но в не в детективах. Хотя первый раз вижу такое, может быть я слишком предвзят."
    "У пионера точно крыша поехала и он неделю питался телами своих товарищей. Хотя он не смог бы столько съесть за такой малый срок ..."
    "Ладно, этот сюжет нужно обдумать."

    jump v2_s6

label v2_s5_fear:

    "История о загадочном убийстве молодой пары в заурядном клубе Липецка."
    "Главный герой - современный детектив, приезжает вечером на вызов. На танцполе лежит мужчина с сильными порезами в области пресса."
    "Настолько сильными, что остальная часть тела с ногами лежит в другом углу клуба."
    menu:
        "Ужас какой-то. Может остановится? Я вроде просил Яну скачать мне детективы, а не ужастики..."
        "Да, не хочу знать, что там произошло":
            "Его, блин, пополам порезали, нет, спасибо, я пасс."
            jump v2_s5_mind
        "Нет, я всё-таки дослушаю":
            pass
    "Девушка рядом с травмами черепа, ей явно проломили голову молотком. Кто мог это сделать? Зачем?"
    "У обоих жертв остались их вещи, это не было вымогательство или ограбление. Также пара не была замечена в криминальных сделках."
    "Через неделю поисков убийцы, главный герой выходит на криминального авторитета с позывным Хантер."
    "У героя нет ордера. Он просит напарника зайти в дом через подвал, а сам пытается залезть через окно. Он тихо падает на ковёр, оставаясь незамеченным."
    "Вдруг он слышит выстрелы и крики. Пролетая лестницу с табельным в руках он спускается в подвал. Хантер замечает это. Они с главным героем целятся друг в друга из пистолетов, и ... "
    "Напарник, лежащий на с тремя пулевыми ранениями делает последний в его жизни выстрел прямо в голову убийце."
    "После вызова скорой, к главному герою приезжает отдел внутренних расследований. Его отстраняют от должности и сажают в тюрьму."
    "Напарника спасти не удаётся."
    "На этом книга заканчивается. Нет ни логического конца, ни ответа, ничего."
    "Что жертвы делали в клубе? Может они не простые гражданские? Почему Хантер так зверски убил их? Столько вопросов."
    "{i}Не раскидать по саду. Не растерять повсюду.{/i}"
    "Ладно, этот сюжет нужно обдумать."

    jump v2_s6

label v2_s5_mind:

    "Да, видимо это не мой жанр. Скорее всего я вернусь к нему, но попрошу Яну скачать что попроще."
    "Так тщательно описывать убийства, да автору нужно не детективы писать, а хорроры."
    "Энивей, слушать такое я не собираюсь, итак сам с собой разговариваю как будто у меня интервью берут."
    "А после таких подробностей вообще с ума сойду. Так что не, возвращаюсь пока на классическую литературу."
    $ mindPoints += 1

    jump v2_s6


label v2_s6:

    "Птицы перестали петь. Скорее всего уже наступил вечер. Яна что-то делает на кухне, пойду поинтересуюсь."
    play sound door
    show y 1-1 at center with fade
    D "Надеюсь ты не эклеры мои ешь."
    if event0:
        y "Нет, что ты. Я же не хочу, чтобы около моего имени было два пунктика карандашом."
        D "После пунктика карандашом вообще-то идёт пунктик ручкой."
        $ event0 = False
    
    y 1-4 "Нет, не переживай. Эклеры я теперь без тебя есть не буду."
    y "Просто вечер очень тихий для субботы, вот и решила посидеть на кухне с книгой."
    D "Прямо растёшь в моих глазах."
    y "Саморазвитие."
    if mindPoints >= 2:
        D "Когда-то и я этим занимался."
        "Опять в нытьё ухожу, надо менять тему."
    if coldPoints >= 2:
        "Идти после таких детективов спасть - не лучшая идея."
        "Делать всё равно нечего."
    D "Что уже прочитала?"
    "Ещё банальнее вопрос придумать невозможно."
    y 2-1 "Немного не очень полезной информации. Первые две главы в книга обычно самые скучные. Предисловие, кто такой автор и прочее."
    D "Классика. Я обычно начинал читать книгу со второй главы."
    y 3-1 "А так разве можно? Вдруг там что-то очень важное."
    if mindPoints >= 2:
        D "Раньше я был готов пойти на такой риск, уж очень мне не нравилось читать про то, какая это книга прекрасная."
        D "Зато сейчас я не могу прочитать конкретную главу, так что приходится слушать всё целиком. Вот тебе преступление и наказание."
        y 2-4 "Ой, ну не говори так."
        "И опять нытьё. Боже."
    else:
        D "Ну, я готов поставить на обратное. Никто не будет писать в начале книги самое важное."
        y 3-0 "В этом есть смысл. Обычно самое важное или интересное в середине или конце."
        D "Ага. Ты могла сэкономить время. Ну, ладно, зато на своих ошибках учиться легче."
        y "Да уж."
    "Диалог зашёл в тупик."
    D "Энивей, пойду спать уже."
    y 2-3 "Ага, давай. Спокойной ночи."
    if coldPoints >= 3:
        D "Да."
    elif mindPoints >= 3:
        D "..."
    elif yanaPoints >= 2:
        D "Споки."
    else:
        D "Тебе тоже."

    hide y with fade
    play sound door

    jump v3_s1
