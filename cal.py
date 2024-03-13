import datetime

def line():
    print('--------------------')
    
def instruction():
    print('This app calculate the split bill.')
    print("Default for P1, '-' for P2 side, '+' for back to P1")
    print("'s' for stop")
    print("'#' for comments")

def main():
    line()
    instruction()
    print()
    plus = True
    date = datetime.date.today()
    with open(f'bill-{date}.txt', 'w') as bill:
        sum = 0
        cur = '# start'
        while (cur != 's'):
            if (cur == '-'):
                cur = '# switch to P2'
                print('\nP2')
                plus = False
            elif (cur == '+'):
                cur = '# switch to P1'
                print('\nP1')
                plus = True
                
            if (cur[0] == '#'):
                bill.write(f'{cur}\n')
            else:
                cur = float(cur)
                if plus:
                    sum += cur
                    bill.write(f'+{cur}\n')
                else:
                    sum -= cur
                    bill.write(f'-{cur}\n')
            cur = input()
        sum = sum/2
        print()
        print(sum)
        bill.write(f'\nSplit total: {sum}')

    line()

if __name__ == '__main__':
    main()