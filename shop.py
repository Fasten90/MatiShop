import csv


config = []


def load_offline_config():
    global config
    config.clear()
    with open('items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['item'], row['barcode'], row['cost'])
            config.append({'item': row['item'], 'barcode':row['barcode'], 'cost':row['cost']})


def check_if_item_is_available(code):
    for item in config:
        if item['barcode'] == code:
            return True
    return False


def get_item_info(code):
    for item in config:
        if item['barcode'] == code:
            return item
    return None


def add_item(code, itemname, value):
    print(f'Add code: {code}')
    global config
    config.append({'item': itemname, 'barcode':code, 'cost':value})
    save_config()


def save_config():
    with open('items.csv', 'w', newline='') as csvfile:
        fields=['item', 'barcode', 'cost']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(config)


if __name__ == '__main__':
    load_offline_config()
    code = '1234'
    if check_if_item_is_available(code):
        print(get_item_info(code))
    else:
        add_item(code, "Test", 12)

    code = '4567'
    if check_if_item_is_available(code):
        print(get_item_info(code))
    else:
        add_item(code, "Test", 12)

