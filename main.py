# Получить из строки config такой список VLANов:#
# ['1', '3', '10', '20', '30', '100']
# Записать итоговый список в переменную result.
# (именно эта переменная будет проверяться в тесте)
# Полученный список result вывести на стандартный поток
# вывода (stdout) с помощью print. Тут очень важный
# момент, что надо получить именно список (тип данных),
# а не, например, строку, которая похожа на показанный список.#
# Ограничение: Все задания надо выполнять используя только пройденные темы.#
# config = "switchport trunk allowed vlan 1,3,10,20,30,100"

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config = config.split()[-1].split(',')
print(config)