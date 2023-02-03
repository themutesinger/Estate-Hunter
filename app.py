import json

import scrapper


def main():
    data = scrapper.get_data()
    with open('datas.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print('Данные сохранены')
    print(f'Количество обьявлений: {len(data)}')


if __name__ == '__main__':
    main()
