class TestsUI:
    def test_ui_fixture(self, ui_fixture):
        assert ui_fixture == "ui_fixture"

    def test_api_ui_fixture(self, common_api_ui_fixture):
        assert common_api_ui_fixture == 1

    def test_api_ui_fixture_get_str(self, common_api_ui_fixture_get_str):
        assert common_api_ui_fixture_get_str == "str"