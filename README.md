# Сделать ендпоинт POST /workers/

Который принимает обьект сотрудник
1. fullname
2. age
3. bio
4. signup_at (не принимается а заполняется текщим временем)

# GET /workers/{worker_id}/
0. id (автоприсвоенный)
1. fullname
2. age
3. bio
4. signup_at
5. last_login (последний логин, по умолчанию None)

# POST /login/
1. fullname
2. last_login (текущая дата, не принимае5тся а заполняется)

Данные можно хранить в json.