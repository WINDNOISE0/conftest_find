class TestsAPILoad:

    """Из tests_load"""
    def test_api_ui_fixture(self, common_api_ui_fixture):
        assert common_api_ui_fixture == 1

    """Из tests_api"""
    def test_api_fixture(self, common_api_fixture):
        assert common_api_fixture == 4

    """Переопределена"""
    def test_api_ui_fixture_get_str(self, common_api_ui_fixture_get_str):
        assert common_api_ui_fixture_get_str == "string"
