from name_function import get_formatted_name


def test_first_last_name():
    full_name = get_formatted_name("fabricio", "jacob")
    assert full_name == "Fabricio Jacob"


def test_first_last_middle_name():
    full_name = get_formatted_name("fabricio", "lucas", "felicio")
    assert full_name == "Fabricio Felicio Lucas"
