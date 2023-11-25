bank = {'Pawel': 100, 'Basia': 100, 'Asia': 100}

def money_transfer(user1, user2, money):
    bank[user1] -= money
    bank[user2] += money
    if user2 == 'Asia':
        bank[user2] -= 1

money_transfer('Asia', 'Pawel', 20)
money_transfer('Basia', 'Pawel', 50)
money_transfer('Pawel', 'Asia', 60)
money_transfer('Basia', 'Asia', 30)

print(f'Pawel has {bank["Pawel"]} PLN')
print(f'Basia has {bank["Basia"]} PLN')
print(f'Asia has {bank["Asia"]} PLN')