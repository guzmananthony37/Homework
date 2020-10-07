# Anthony Guzman      7.25       CIS2348
def exact_change(user_total):
    if user_total > 0:
        dollars = int(user_total / 100)
        user_total = user_total % 100

        quarters = int(user_total / 25)
        user_total = user_total % 25

        dimes = int(user_total / 10)
        user_total = user_total % 10

        nickels = int(user_total / 5)
        user_total = user_total % 5

        pennies = user_total
        return dollars, quarters, dimes, nickels, pennies
    else:
        return 0, 0, 0, 0, 0


if __name__ == '__main__':
    input_val = int(input())

    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(
        input_val)

    if input_val <= 0:
        print('no change')

    if num_dollars == 1:
        print('%d dollar' % (num_dollars))
    elif num_dollars > 0:
        print('%d dollars' % (num_dollars))

    if num_quarters == 1:
        print('%d quarter' % (num_quarters))
    elif num_quarters > 0:
        print('%d quarters' % (num_quarters))

    if num_dimes == 1:
        print('%d dime' % (num_dimes))
    elif num_dimes > 0:
        print('%d dimes' % (num_dimes))

    if num_nickels == 1:
        print('%d nickel' % (num_nickels))
    elif num_nickels > 0:
        print('%d nickels' % (num_nickels))

    if num_pennies == 1:
        print('%d penny' % (num_pennies))
    elif num_pennies > 0:
        print('%d pennies' % (num_pennies))