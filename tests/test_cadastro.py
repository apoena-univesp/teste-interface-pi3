import time
from pom.cadastro_page_elements import Cadastro
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def test_comparativo_fazenda(set_up):
    page = set_up
    page.get_by_placeholder(Cadastro.nome).click()
    page.get_by_placeholder(Cadastro.nome).fill("fazenda1")
    page.get_by_placeholder(Cadastro.data_aplicacao).fill("2022-11-23")
    page.get_by_placeholder(Cadastro.equipamento).click()
    page.get_by_placeholder(Cadastro.equipamento).fill("equipamento1")
    page.get_by_placeholder(Cadastro.ponta_pulverizacao).click()
    page.get_by_placeholder(Cadastro.ponta_pulverizacao).fill("ponta1")
    page.get_by_role("button", name=Cadastro.botao_cadastrar).click()
    time.sleep(1)
    fazenda = page.locator(Cadastro.comparativo)
    expect(fazenda).to_contain_text("fazenda1")


def test_experimento_fazenda(set_up):
    page = set_up
    page.wait_for_url("http://127.0.0.1:5000/comparativos")
    page.locator(Cadastro.taxa_fazenda).click()
    page.locator(Cadastro.taxa_fazenda).fill("2.34")
    page.locator(Cadastro.velocidade_fazenda).click()
    page.locator(Cadastro.velocidade_fazenda).fill("3.43")
    page.locator(Cadastro.pressao_fazenda).click()
    page.locator(Cadastro.pressao_fazenda).fill("92.6")
    page.locator(Cadastro.temperatura_fazenda).click()
    page.locator(Cadastro.temperatura_fazenda).fill("37.8")
    page.locator(Cadastro.umidade_fazenda).click()
    page.locator(Cadastro.umidade_fazenda).fill("70")
    page.locator(Cadastro.vento_fazenda).click()
    page.locator(Cadastro.vento_fazenda).fill("37.9")
    page.locator(Cadastro.produto_fazenda).click()
    page.locator(Cadastro.produto_fazenda).fill("teste")
    page.locator(Cadastro.dosagem_fazenda).click()
    page.locator(Cadastro.dosagem_fazenda).fill("700")
    page.get_by_role("button", name=Cadastro.botao_experimento_fazenda).click()
    experimento_fazenda = page.locator(Cadastro.cadastro_experimento_fazenda)
    expect(experimento_fazenda).to_contain_text("fazenda1")


def test_comparativo_empresa(set_up):
    page = set_up
    page.wait_for_url("http://127.0.0.1:5000/experimentos_fazenda")
    page.get_by_placeholder(Cadastro.nome).click()
    page.get_by_placeholder(Cadastro.nome).fill("empresa1")
    page.get_by_placeholder(Cadastro.data_aplicacao).fill("2022-11-11")
    page.get_by_placeholder(Cadastro.equipamento).click()
    page.get_by_placeholder(Cadastro.equipamento).fill("equipamento empresa")
    page.get_by_placeholder(Cadastro.ponta_pulverizacao).click()
    page.get_by_placeholder(Cadastro.ponta_pulverizacao).fill("ponta teste")
    page.get_by_role("button", name=Cadastro.botao_cadastrar).click()
    empresa = page.locator(Cadastro.comparativo)
    expect(empresa).to_contain_text("empresa1")

def test_experimento_empresa(set_up):
    page = set_up
    page.wait_for_url("http://127.0.0.1:5000/comparativos")
    page.locator(Cadastro.taxa_empresa).click()
    page.locator(Cadastro.taxa_empresa).fill("6.74")
    page.locator(Cadastro.velocidade_empresa).click()
    page.locator(Cadastro.velocidade_empresa).fill("20")
    page.locator(Cadastro.pressao_empresa).click()
    page.locator(Cadastro.pressao_empresa).fill("60")
    page.locator(Cadastro.temperatura_empresa).click()
    page.locator(Cadastro.temperatura_empresa).fill("33.6")
    page.locator(Cadastro.umidade_empresa).click()
    page.locator(Cadastro.umidade_empresa).fill("75.4")
    page.locator(Cadastro.vento_empresa).click()
    page.locator(Cadastro.vento_empresa).fill("50")
    page.locator(Cadastro.produto_empresa).click()
    page.locator(Cadastro.produto_empresa).fill("teste empresa")
    page.locator(Cadastro.dosagem_empresa).click()
    page.locator(Cadastro.dosagem_empresa).fill("45.9")
    time.sleep(1)
    page.get_by_role("button", name=Cadastro.botao_experimento_empresa).click()
    time.sleep(1)
    experimento_empresa = page.locator(Cadastro.cadastro_experimento_empresa)
    expect(experimento_empresa).to_contain_text("empresa1")

    page.wait_for_url("http://127.0.0.1:5000/experimentos_empresa")
