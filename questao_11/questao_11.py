import imp
from clientes import Cliente
from contas import Conta
from contas import ContaEspecial

maria = Cliente("Maria da Silva", "555-4321")

conta = ContaEspecial([maria], 3432, 50000, 10000)
conta.extrato()
conta.saque(6000)
conta.saque(3000)
conta.saque(1000)
conta.extrato()