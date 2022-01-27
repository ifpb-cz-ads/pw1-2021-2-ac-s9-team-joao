import imp
from clientes import Cliente
from contas import Conta
from contas import ContaEspecial

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria], 2, 500)
conta1.resumo()
conta2.resumo()
print(conta1.saque(1000))
print(conta2.saque(100))
conta1.resumo()
conta2.resumo()

conta3 = ContaEspecial([maria], 3432, 50000, 10000)
conta3.resumo()
print(conta3.saque(100000))
print(conta3.saque(500))
conta3.resumo()