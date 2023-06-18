import pandas as pd
import pygsheets

# authorization API key
gc = pygsheets.authorize(service_file='sheets_api.json')

df = pd.DataFrame()
df['customer_name'] = []
df['drink_name'] = []
df['quantity'] = []


# Log all transactions, e.g. who ordered what and how many. Can be used for debugging
def create_transactions(customer_name, drink_name, quantity):
    sh = gc.open('Sheets api test')
    wks = sh[1]  # table name: transactions

    existing_data = wks.get_all_records()
    print(existing_data)

    new_row = {
        'customer_name': customer_name,
        'drink_name': drink_name,
        'quantity': quantity
    }

    existing_data.append(new_row)
    wks.set_dataframe(pd.DataFrame(existing_data), start='A1')


def add_to_customer(customer_name, drink_name, quantity):
    sh = gc.open('Sheets api test')
    wks = sh[0]  # table name: main

    existing_data = wks.get_all_records()
    print(existing_data)

    for row in existing_data:
        if row['customer_name'] == customer_name:
            print(row['quantity'])
            if pd.isna(row['quantity']):
                row['quantity'] = 0
            row['quantity'] += quantity
            break

    wks.set_dataframe(pd.DataFrame(existing_data), start='A1')
