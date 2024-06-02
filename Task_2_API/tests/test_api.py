import requests

from Task_2_API.lib.apiwrapper import get_form, post_form, BASE_URL


class TestClass:
    def test_get_form_http_status(self):
        assert get_form().status_code == 200

    def test_post_form_http_status(self):
        data = [["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]]
        assert post_form(data).status_code == 200

    def test_leetcode_case_2(self):
        data = [["X"]]
        assert post_form(data).text.rstrip() == '[["X"]]'

    def test_all_O(self):
        data = [["O", "O"],
                ["O", "O"]]
        assert post_form(data).text.rstrip() == '[["O","O"],["O","O"]]'

    def test_O_in_center(self):
        data = [["X", "X", "X"],
                ["X", "O", "X"],
                ["X", "X", "X"]]
        assert post_form(data).text.rstrip() == '[["X","X","X"],["X","X","X"],["X","X","X"]]'

    def test_borders_are_O(self):
        data = [["O", "X", "O"],
                ["X", "O", "X"],
                ["O", "X", "O"]]
        assert post_form(data).text.rstrip() == '[["O","X","O"],["X","X","X"],["O","X","O"]]'

    def test_large_board(self):
        data = [["X"] * 200 for _ in range(200)]
        data[0][0] = "O"
        data[199][199] = "O"
        expected = [['"X"'] * 200 for _ in range(200)]
        expected[0][0] = '"O"'
        expected[199][199] = '"O"'
        expected_str = "["
        for row in expected:
            expected_str += "[" + ",".join(row) + "],"
        expected_str = expected_str.rstrip(",") + "]"

        assert post_form(data).text.rstrip() == expected_str

    def test_empty_board(self):
        data = [[]]
        assert post_form(data).status_code == 400

    def test_invalid_size(self):
        data = [["X"] * 201 for _ in range(201)]
        assert post_form(data).status_code == 400

    def test_invalid_characters(self):
        data = [["X", "Z"],
                ["SXL", "123"]]
        assert post_form(data).status_code == 400

    def test_not_all_rows_same_length(self):
        data = [["X", "O", "X"],
                ["O", "X"]]
        assert post_form(data).status_code == 400

    def test_invalid_type(self):
        data = "1"
        assert post_form(data).status_code == 400

    def test_non_existent_endpoint(self):
        response = requests.post(f'{BASE_URL}daklsdjklasdakjask')
        assert response.status_code == 404

    def test_withot_form_data(self):
        response = requests.post(BASE_URL)
        assert response.status_code == 405

    def test_is_solution_get_form_content_type(self):
        assert get_form().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_is_solution_post_form_content_type(self):
        assert post_form("test").headers['Content-Type'] == 'text/html; charset=utf-8'