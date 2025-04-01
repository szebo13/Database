import psycopg2 # import postgress databazi
from psycopg2 import extensions # pro status ready
# Parametry p?ipojen�
db_params = {
    'dbname': 'jakubszebesta', #
    'user': 'koyeb-adm', #
    'password': 'XQc0HOTwa1Kl', #
    'host': 'ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app', #
    'port': 5432,
    'sslmode': 'require'
}

# s try-except
try:
    # 1. P?ipojen� k datab�zi
    conn = psycopg2.connect(**db_params)
    print(":white_check_mark: P?ipojen� k datab�zi bylo �sp?�n�.")
    # 2. Ov??en� p?ipojen�
    if conn.closed == 0:
        print(":white_check_mark: P?ipojen� je aktivn�.")
    else:
        print(":x: P?ipojen� je uzav?en�.")
    if conn.status == extensions.STATUS_READY:
        print(":white_check_mark: P?ipojen� je p?ipraven� k pou�it�.")
    else:
        print(":warning: P?ipojen� nen� ve stavu 'READY'.")
except psycopg2.Error as e:
    print(f":x: Chyba p?i p?ipojen� k DB: {e}")
finally:
    # 3. Uzav?en� spojen�
    conn.close()
    print(":white_check_mark: Spojen� bylo uzav?eno.")