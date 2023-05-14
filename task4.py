revenue = int(input('введите выручку фирмы:'))
costs = int(input('введите издержки фирмы:'))
employee = int(input('введите численность сотрудников:'))


if revenue > costs:

    profit = revenue - costs
    rent = profit / revenue
    profitemp = profit / employee
    print('выручка больше издержек')
    print(f'прибыль: {profit}')
    print(f'рентабельность: {rent}')
    print(f'пприбыль фирмы на одного сотрудника:  {profitemp}')

else:
    print('издержки больше выручки ')


