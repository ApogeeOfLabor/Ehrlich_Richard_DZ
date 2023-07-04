class StopZeroDevision(Exception):
    ...
    
    
def main(num: int):
    try:
        return 2/num
    except:
        raise StopZeroDevision


if __name__ == '__main__':
    try:
        print(main(int(input(f'num = '))))
    except:
        print('Борода, досвидули!')
        