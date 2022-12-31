# def:함수를 만듣때,즉 정의핟떄 (definition)
#형식: def 함수이름():

def open_acc(): #함수만듣기
    print('새로운 통장읃 만듣었습니다.')

open_acc() # 함수 호출(만든 함수는 호춛해야 사용가능)

#입금
def deposit(balance,money):
    print('입금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance+money))
    return balance + money #필연적인 존재

#출금
def withdraw(balance,money):
    if balance >= money:
        print('출금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance-money))
        return balance-money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {0}원입니다.'.format(balance))
        return balance

#저녁에 출금을 할 경우 수수료를 내야 함
def withdraw_night(balance,money):
    commission=100 #야간 수수료
    return commission,balance-money-commission

balance=0
balance=deposit(balance,2000)
balance=withdraw(balance,500)
commission,balance = withdraw_night(balance,500)

print('출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(commission,balance))
