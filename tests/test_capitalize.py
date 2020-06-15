from ianlibdemo import capital_mod


def test_capitalize_file(tmp_path):
    in_file = tmp_path / "in_file.txt"
    in_content = "this is the lowercase input sentence"
    in_file.write_text(in_content)
    out_file = tmp_path / "out_file.txt"
    out_content = "This is the Lowercase Input Sentence\n"
    # Output shouldn't exist before we call the function
    assert not out_file.exists()
    capital_mod.capitalize(in_file, out_file)
    assert out_file.exists()
    assert out_file.read_text() == out_content
