# Тестовое задание
В данном проекте реализованы: Авторизация по номеру телефона - https://mentaque.pythonanywhere.com/enter-by-phone/ (API принимает на вход номер телефона и имитирует смс код в ответе, на серевере создается запись этого пользователся, где ему дается уникальный 6-ти значный invite_code, а также каждый вход дается новый auth_code для аутентификации).
Ввод кода, полученного из ответа предыдущего API - https://mentaque.pythonanywhere.com/confirm-phone/ (API принимает на вход номер телефона и auth_code, если всё правильно, то в ответе вернется профиль пользователя, в базе поле is_authenticated поменяется на true и теперь этот пользователь может указать того, кто его пригласил)
Ввод invite_code и получения профиля - https://mentaque.pythonanywhere.com/user-profile/ (API принимает на вход номер телефона и invite_code, если оставить поле с invite_code пустым, то вернется профиль пользователя, а если указать invite_code другого пользователя, то в бд запишется информация о том, кто его пригласил, а у того пользователя, который пригласил, в профиле будут показываться пользователи, которые ввели его код.
