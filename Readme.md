### Что нужно для просмтра
Нужно создать администратора, чтобы можно было сверять данные вывода
### Примечания к коду
Мой код не идеален, есть много нюансов, и я хотел бы поговорить об этом
Главная суть кода, при входе на главную страницу, мы начинаем ждать, потому что 
у нас генерируются данные (50000 пользователей и тд.) это можно посмотреть в папке 
generators.
#####
У меня генерация самих данных происходит за 7 - 9 секунд.
Рендеринг страницы идет очень долго, около 40 секунд с учетом того,
что будем выводить всех полей. Мне это не нравится, я бы сделал либо АПИ и фронт
на JS с запросами на нажатие подразделений, либо сделать пагинацию.
По итогу я просто сделал вывод имени пользователей и ссылку на админку.
#####
Как я уже писал есть нюансы, их можно было бы обдумать и реализовать, но для тестового
задания я считаю это нормальный результат. Кончено если это рассматривать в качестве 
прода, то тут плохо реализованно.
###Мои контакты
telegram: `@RedPowDan` : <https://t.me/RedPowDan>
mail: 11051969dahul@mail.ru
