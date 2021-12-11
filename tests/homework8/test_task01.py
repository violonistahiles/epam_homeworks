import pytest

from homework8.task01 import KeyValueStorage


def test_attributes_set_correctly(tmpdir):
    """
    Testing KeyValueStorage key value pairs set properly
    """
    test_text = 'name=kek\nlast_name=top\n'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)
    correct_dict = {'name': 'kek', 'last_name': 'top'}

    storage = KeyValueStorage(tmp_path)

    for key in storage.keys():
        assert storage[key] == correct_dict[key]
        assert eval(f'storage.{key}') == correct_dict[key]


def test_int_key_raise_valueerror(tmpdir):
    """
    Testing integer key in key value pair will raise error
    """
    test_text = 'name=kek\n1=top\n'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    with pytest.raises(ValueError):
        _ = KeyValueStorage(tmp_path)


def test_attribute_clash_save_initial_attribute(tmpdir):
    """
    Testing integer key in key value pair will raise error
    """
    test_text = 'name=kek\nname=top\n'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    storage = KeyValueStorage(tmp_path)

    assert storage.name == 'kek'
