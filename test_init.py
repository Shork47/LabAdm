from lab1Adm import createBD
from lab1Adm import fillBD
from lab1Adm import showClientsBD
from lab1Adm import showOrdersBD

def test_createBD_true():
    assert createBD() == True

def test_fillBD_true():
    assert fillBD() == True

def test_countClients():
    assert showClientsBD() >= 10

def test_countOrders():
    assert showOrdersBD() >= 10

# pytestс --junitxml=result.xml