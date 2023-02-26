from ya_api import YaUploader

TOKEN = ''

def test_1():
    yandex = YaUploader(TOKEN)
    res = yandex.create_folder()
    assert res == 201, f'Для того, чтобы создалась папка, ответ должен быть 201, текущий ответ - {res}'
    res_2 = yandex.check_folder()
    assert res_2 == 200, f'Папки не существует'

