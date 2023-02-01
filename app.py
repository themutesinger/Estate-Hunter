from scrapper.lalafo import scrape_lalafo
import json


def main():
    lalafo_data = scrape_lalafo()

    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(lalafo_data, file, indent=2, ensure_ascii=False)
        print('Данные сохранены')
    print(f'Количество обьявлений: {len(lalafo_data)}')


if __name__ == '__main__':
    main()
