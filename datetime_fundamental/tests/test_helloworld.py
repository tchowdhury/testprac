from newproject.newproject import print_hi, listThing

def test_helloworld():
    assert print_hi("Yummy") == "Hi, Yummy"

def test_listThing():
    x = listThing()
    assert len(x['thingTypes']) == 1