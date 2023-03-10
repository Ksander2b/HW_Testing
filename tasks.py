geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def getting_new_list():
    new_geo_logs = []
    for logs in geo_logs:
        for places in logs.values():
            if 'Россия' in places:
                new_geo_logs.append(logs)
    return new_geo_logs


ids = {
  'user1': [213, 213, 213, 15, 213],
  'user2': [54, 54, 119, 119, 119],
  'user3': [213, 98, 98, 35]
}

def unique_values():
    ids_new = []
    for values in ids.values():
        for elements in values:
            ids_new.append(elements)
    task_result = set(ids_new)
    task_results_final = list(task_result)
    return task_results_final


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_most_pop_comp():
    max_values = max(stats.values())
    for keys, values in stats.items():
        if values == max_values:
            return keys