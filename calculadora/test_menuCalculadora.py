from .menucalculadora import suma

def prueba_enteros():
    assert suma(100,1) == 101
    assert suma(2,2)==4
    assert suma(9,9)==18

def prueba_ceros():
    assert suma(0.25,0.75)==1.0
    assert suma(1.5,0.5)==2.0
    assert suma(-7,-9)==-18
