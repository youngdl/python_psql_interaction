import psycopg2
from config import config
import decimal
import datetime
import traceback


def main_loop(cur, conn):
    while True:
        command = input('Please enter a command: ')
        if command == 'q':  # Quit
            break
        elif command == 'co':  # Create owner
            owner = input('Please enter name of new owner: ')
            cur.execute('insert into person (name) values (%s)', (owner,))
            conn.commit()
        elif command == 'lo':  # List owners.
            cur.execute('select * from person')
            print(cur.fetchall())

        # create device category
        elif command == 'cdc':
            device_category = input('Please enter name of a new device category: ')
            cur.execute('insert into device_category (category) values (%s)', (device_category, ))
            conn.commit()
        # create device
        elif command == 'cd':
            device = input('Please enter a name of a new device: ')
            category_id = input('Please enter a category_id: ')
            cur.execute('insert into device (name, device_category_id) values (%s, %s)', (device, category_id))
            conn.commit()
        # create inventory
        elif command == 'ci':
            owner_id = input('Please enter a owner_id: ')
            device_id = input('Please enter a device_id: ')
            purchase_date = datetime.datetime.strptime(input('Please enter a purchase date in yyyy-mm-dd: '), '%Y-%m-%d').date()
            price = decimal.Decimal(input('Please enter purchase price: '))
            cur.execute(
                'insert into inventory (person_id, device_id, is_active, purchase_date, price) values (%s, %s, %s, %s, %s)',
                (owner_id, device_id, True, purchase_date, price))
            conn.commit()

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        print('Connecting to Postgresql database...')
        cur = conn.cursor()
        print('Postgresql version:')
        cur.execute('select version()')
        db_version = cur.fetchone()
        print(db_version)
        main_loop(cur, conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('-' * 80)
        traceback.print_exc()
        print('-' * 80)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection has been closed')


if __name__ == '__main__':
    connect()
