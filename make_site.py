import staticjinja


index_content = {
    'user': 'Вася Пупкин',
    'current_city': 'Новосибирск',
    'cities': [
        "Кемерово",
        "Красноярск",
        "Новосибирск",
        "Омск",
        "Томск"
    ],
    "manufacturers_count": 25,
    "companies_count": 105,
    "comments_count": 5,
    "request": "60шт. ПК от 72-15 до ПК 21-15 можно без сахара. Каргат, с доставкой до порога.",
    "author_name": "Алексей",
    "message_time": "Вчера, в 21:30",
    "number_of_views": 12,
    'our_telephone': '+7 999 888 77 66',
}

catalog_main = {
    'user': 'Вася Пупкин',
    'current_city': 'Новосибирск',
    'cities': [
            "Кемерово",
            "Красноярск",
            "Новосибирск",
            "Омск",
            "Томск"
        ],
    'our_telephone': '+7 999 888 77 66',
    'companies': [
        {'name': "ООО Строй-сервис монтаж", 'place': "Новосибирск", 'product': "ЖБИ", "address": "Под часами", "telephone": "000-00-00"},
        {"name": "ООО ЖБИ-3", "place": "Кемерово", "product": "ЖБИ", "address": "Под часами", "telephone": "11-11-11"},
    ],
    'products': [
        'ЖБИ',
        "Кирпич, газобетон, брус",
        "Что-то ещё",
        "Что-то ещё",
    ]
}

company_services = {
    'user': 'Вася Пупкин',
    'current_city': 'Новосибирск',
    'our_telephone': '+7 999 888 77 66',
    'cities': [
                "Кемерово",
                "Красноярск",
                "Новосибирск",
                "Омск",
                "Томск"
            ],
}


catalog_end_page = {
    'user': 'Вася Пупкин',
    'current_city': 'Новосибирск',
    'our_telephone': '+7 999 888 77 66',
    'cities': [
                "Кемерово",
                "Красноярск",
                "Новосибирск",
                "Омск",
                "Томск"
    ],
    'company_name': "Строй-Сервис-Монтаж",
    "place": "Новосибирск",
    "production": "ЖБИ, Бетон",
    "address": "Под часами на том же месте",
    "telephone": "Там же",
    'activities': [
             "Плиты",
             "Поерекрытия",
             "Доставляем бесплатно",
    ],
}

if __name__=="__main__":
    site = staticjinja.make_site(outpath='./docs', contexts=[('index.html', index_content),
                                                             ('catalog_main.html', catalog_main),
                                                             ('catalog_end_page.html', catalog_end_page),
                                                             ('catalog_list.html', catalog_main),
                                                             ('zajavki.html', index_content),
                                                             ('profile.html', index_content)])
    site.render()
