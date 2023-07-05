from twttr import shorten

def test_shorten():
    assert shorten("avyaan") == "vyn"
    assert shorten("monologue") == "mnlg"
    assert shorten("MyNameIsAvyaanVerma") == "MyNmsvynVrm"
    assert shorten("My..Name..Is/Avyaan_Verma") == "My..Nm..s/vyn_Vrm"
    assert shorten("12345") == "12345"



