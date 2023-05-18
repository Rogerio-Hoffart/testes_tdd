import pytest
from bytebank import Funcionario
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"  #Given - entrada
        esperado = 23

        funcionario_teste = Funcionario("teste", entrada, 1111)
        resultado = funcionario_teste.idade()   #when - ação

        assert resultado == esperado    #Then - desfecho

    def test_quando_sobrenome_recebe_Lucas_carvalho_de_retornar_apenas_carvalho(self):
        entrada = 'Lucas Carvalho'  #Given - entrada
        esperado = 'Carvalho'

        funcionario_teste = Funcionario(entrada, 10/11/1998, 1211)
        resultado = funcionario_teste.sobrenome()   #When - ação

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000    #Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '12/07/1993', entrada_salario)
        funcionario_teste.decrescimo_salario()  #When
        resultado = funcionario_teste.salario

        assert resultado == esperado    #then
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  #Given
        esperado = 100

        funcionario_teste = Funcionario('Jose', '12/07/1993', entrada)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000  # Given

            funcionario_teste = Funcionario('Jose', '12/07/1993', entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado  # then

