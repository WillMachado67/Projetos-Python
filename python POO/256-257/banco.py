from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account_number):
        self._agency = agency
        self._account_number = account_number
        self._balance = 0

    def __str__(self):
        raise NotImplementedError('inplemente o metodo "__str__"')

    @abstractmethod
    def withdraw(self, valor):
        raise NotImplementedError('Methodo withdraw nao foi impletado.')

    def deposit(self, valor):
        self._balance += valor
        return f'Você depositou R${valor}'.replace('.', ',')


class CheckingAccount(Account):
    def __init__(self, agency, account_number, limit):
        super().__init__(agency, account_number)
        self._limit = limit

    def __str__(self):
        return f'Agencia: {self._agency} Nºconta: {self._account_number}\n'\
            f'Saldo: R${self._balance:.2f} Limite: '\
            f'R$-{self._limit}'.replace('.', ',')

    def withdraw(self, valor, name, agency, account):
        if banco.authentication(name, agency, account):
            if self._balance + self._limit >= valor:
                self._balance -= valor
                return f'Você sacou R${valor:.2f}'.replace('.', ',')
            else:
                return 'Saldo insuficiente.'
        else:
            return 'Não foi possível autenticar a conta'


class SavingsAccount(Account):
    def __str__(self):
        return f'Agencia: {self._agency} Nºconta: {self._account_number}\n'\
            f'Saldo: R${self._balance:.2f}'.replace('.', ',')

    def withdraw(self, valor, name, agency, account):
        if banco.authentication(name, agency, account):
            if self._balance >= valor:
                self._balance -= valor
                return f'Você sacou {valor:.2f}'
            else:
                return 'Saldo insuficiente.'
        else:
            return 'Não foi possível autenticar a conta'


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


class Client(Person):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self._account = account

    def __str__(self):
        return f'{self.name} {self.age}\n{self._account}'


class Bank:
    _agency = 1234

    def __init__(self):
        self._clients = []
        self._accounts = []

    def create_checking_account(self, name, age, account):
        limit = 500
        _account = account
        new_account = CheckingAccount(self._agency, _account, limit)
        self._accounts.append(_account)
        self._clients.append(Client(name, age, new_account))

    def create_savings_account(self, name, age, account):
        _account = account
        new_account = SavingsAccount(self._agency, _account)
        self._accounts.append(_account)
        self._clients.append(Client(name, age, new_account))

    def authentication(self, name, agency, account):
        client = next((c for c in self._clients if c.name == name), None)
        if client and agency == self._agency and account in self._accounts:
            return True
        else:
            return False


if __name__ == '__main__':
    banco = Bank()
    banco.create_checking_account('Willian', 29, 678950)
    print(banco._clients[-1])
    print()
    print(banco._clients[0]._account.withdraw(200, "Willian", 1234, 678950))
    print(banco._clients[0])
    print(banco._clients[0]._account.deposit(1500.58))
    print(banco._clients[0])
    print(banco._clients[0]._account.withdraw(521.67, "Willian", 1234, 678950))
    print(banco._clients[0])
    print()
    banco.create_savings_account('Suelen', 25, 123456)
    print(banco._clients[-1])
