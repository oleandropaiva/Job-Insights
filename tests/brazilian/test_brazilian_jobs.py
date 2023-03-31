from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    translate_dict_key = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert "title" in translate_dict_key[0]
    assert "salary" in translate_dict_key[0]
    assert "type" in translate_dict_key[0]
