import psycopg2 # import postgress databazi
from psycopg2 import extensions # pro status ready
# Parametry p?ipojení
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
    # 1. P?ipojení k databázi
    conn = psycopg2.connect(**db_params)
    print(":white_check_mark: P?ipojení k databázi bylo úsp?šné.")
    # 2. Ov??ení p?ipojení
    if conn.closed == 0:
        print(":white_check_mark: P?ipojení je aktivní.")
    else:
        print(":x: P?ipojení je uzav?ené.")
    if conn.status == extensions.STATUS_READY:
        print(":white_check_mark: P?ipojení je p?ipravené k použití.")
    else:
        print(":warning: P?ipojení není ve stavu 'READY'.")
except psycopg2.Error as e:
    print(f":x: Chyba p?i p?ipojení k DB: {e}")
finally:
    # 3. Uzav?ení spojení
    conn.close()
    print(":white_check_mark: Spojení bylo uzav?eno.")