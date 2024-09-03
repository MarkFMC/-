
import threading
import random
import time


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

  
    def deposit(self):
        for i in range(100):
            balance_up = random.randint(50, 500)
            self.balance += balance_up
            print(f"Пополнение: {balance_up}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            balance_down = random.randint(50, 500)
            print(f"Запрос на {balance_down}")
            if self.balance >= balance_down:
                self.balance -= balance_down
                print(f'Снятие: {balance_down}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

