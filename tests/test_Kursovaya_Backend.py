from Kursovaya_Backend import edit_data


def test_edit_data(dates):
    assert edit_data(dates[0]) == "08.12.2019"
