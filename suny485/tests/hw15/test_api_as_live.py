import pytest
import requests

"""
testable things for API GET endpoint live testing
+ input
    + key
        + string
            + must be 'password'
            + else returns 500
    + value
        + string
            + any string
            + length of string
+ logic
    + computes strength for good key/value pair
    + http truncates url at `#`
    + http truncates url at `&`
    + empty value string throws DivByZero
+ output
    + json payload
        + key/value
            + "password"
                original string
            + "strength"
                either "good" or "bad"

testable things for API POST endpoint live testing
+ input
    + key
        + string
            + must be 'password'
            + else returns 400 with payload
                {'error': "Missing key 'password' in the JSON payload"}
    + value
        + string
            + any string
            + length of string
            + empty string returns 500
        + any other type returns 500
+ output
    + json payload
        + key/value
            + "password"
                original string
            + "strength"
                either "good" or "bad"

"""


@pytest.mark.live_api
class TestApiGetThroughHttp(object):

    base = 'http://127.0.0.1:5000/get_strength'

    @pytest.mark.parametrize(
        'good_strength_get',
        [
            '_@4-%@o_rds',
            '$$$$$$$ord',
        ], ids=[
            '_@4-%@o_rds',
            '$$$$$$$ord',
        ]
    )
    def test_api_good_password(self, good_strength_get):
        # disambiguate
        password = good_strength_get  # flake8 will say this is bad; ignore that!
        expected_strength = 'good'

        # assemble the query params for requests; requests will create full url,
        # which will look like "http://127.0.0.1:5000/get_strength?password=<password>"
        params = {'password': password}

        # make the live request, check that the server accepted it
        res = requests.get(self.base, params=params)
        assert res.status_code == 200

        # get the response payload and examine it
        data = res.json()
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_strength_get',
        [
            '_@4-%o_rds',
            '$password',
            # 'x' * 100,
            # 'x' * 1000,
            # 'x' * 10000,
        ], ids=[
            '_@4-%o_rds',
            '$password',
            # '100chars',
            # '1000chars',
            # '10000chars',
        ]
    )
    def test_api_bad_password(self, bad_strength_get):
        # disambiguate
        password = bad_strength_get  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        # assemble the query params for requests; requests will create full url,
        # which will look like "http://127.0.0.1:5000/get_strength?password=<password>"
        params = {'password': password}

        # make the live request, check that the server accepted it
        res = requests.get(self.base, params=params)
        assert res.status_code == 200

        # get the response payload and examine it
        data = res.json()
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_key_get',
        [
            'Password',
            '$password',
            'password '
        ])
    def test_api_bad_key(self, bad_key_get):
        """ Keys that trigger a server 500 """
        password = 'foo'

        # assemble the query params for requests; requests will create full url,
        # which will look like "http://127.0.0.1:5000/get_strength?password=<password>"
        params = {bad_key_get: password}

        # make the live request, check that the server accepted it
        res = requests.get(self.base, params=params)
        assert res.status_code == 500

    @pytest.mark.parametrize(
        'not_schema_errors_get',
        [
            'pass#word',
            'pa??word',
            'pa&&word',
        ]
    )
    def test_url_not_schema_error(self, not_schema_errors_get):
        """ If unescaped in query string, these would cause string truncation """
        # disambiguate
        password = not_schema_errors_get  # flake8 will say this is bad; ignore that!

        # assemble the query params for requests; requests will create full url,
        # which will look like "http://127.0.0.1:5000/get_strength?password=<password>"
        params = {'password': password}

        # make the live request, check that the server accepted it
        res = requests.get(self.base, params=params)
        assert res.status_code == 200

    @pytest.mark.parametrize(
        'div_by_zero_get',
        [
            '',
        ]
    )
    def test_api_divbyzeror_error(self, div_by_zero_get):
        # disambiguate
        password = div_by_zero_get  # flake8 will say this is bad; ignore that!

        # assemble the payload
        params = {'password': password}

        res = requests.get(f"{self.base}", params=params)
        assert res.status_code == 500


@pytest.mark.live_api
class TestApiPostThroughHttp(object):

    base = 'http://127.0.0.1:5000/get_strength?'

    @pytest.mark.parametrize(
        'good_strength_post',
        [
            '_@4-%@o_rds',
            '$$$$$$$ord',
        ], ids=[
            '_@4-%@o_rds',
            '$$$$$$$ord',
        ]
    )
    def test_api_good_password(self, good_strength_post):
        # disambiguate
        password = good_strength_post  # flake8 will say this is bad; ignore that!
        expected_strength = 'good'

        # assemble the payload
        data = {'password': password}

        res = requests.post(f"{self.base}", json=data)
        assert res.status_code == 200

        data = res.json()
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_strength_post',
        [
            '_@4-%o_rds',
            '$password',
            # 'x' * 100,
            # 'x' * 1000,
            # 'x' * 10000,
        ], ids=[
            '_@4-%o_rds',
            '$password',
            # '100chars',
            # '1000chars',
            # '10000chars',
        ]
    )
    def test_api_bad_password(self, bad_strength_post):
        # disambiguate
        password = bad_strength_post  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        # assemble the payload
        data = {'password': password}

        res = requests.post(f"{self.base}", json=data)
        assert res.status_code == 200

        # get the response payload and examine it
        data = res.json()
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_key_post',
        [
            'Password',
            '$password',
            'password '
        ])
    def test_api_bad_key(self, bad_key_post):
        """ Keys that trigger a server 400 """
        key = bad_key_post
        password = 'foo'

        # assemble the payload
        data = {key: password}

        res = requests.post(f"{self.base}", json=data)
        assert res.status_code == 400

        # get the response payload and examine it
        data = res.json()
        print(f"data: {data}")
        assert data == {'error': "Missing key 'password' in the JSON payload"}

    @pytest.mark.parametrize(
        'type_error_post',
        [
            1,
            [1, 2],
            (1, 2),
            {1: 2}
        ], ids=[
            'int',
            'list',
            'tuple',
            'dict'
        ]
    )
    def test_api_type_error(self, type_error_post):
        # disambiguate
        password = type_error_post  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        # assemble the payload
        data = {'password': password}

        res = requests.post(f"{self.base}", json=data)
        assert res.status_code == 500

        # the server should show that this raises a TypeError

    @pytest.mark.parametrize(
        'div_by_zero_post',
        [
            '',
        ]
    )
    def test_api_divbyzeror_error(self, div_by_zero_post):
        # disambiguate
        password = div_by_zero_post  # flake8 will say this is bad; ignore that!

        # assemble the payload
        data = {'password': password}

        res = requests.post(f"{self.base}", json=data)
        assert res.status_code == 500
