import json
import pytest

from suny485.projects.hw15.api import app

"""
testable things for API GET endpoint
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

testable things for API GET endpoint

"""


@pytest.fixture
def client_get_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiGetThroughCode(object):

    @pytest.mark.parametrize(
        'good_strength_get',
        [
            '_@4-%@o_rds',
            '$$$$$$$ord'
        ]
    )
    def test_api_good_password(self, client_get_endpoint, good_strength_get):
        # disambiguate
        password = good_strength_get  # flake8 will say this is bad; ignore that!
        expected_strength = 'good'

        response = client_get_endpoint.get(f"/get_strength?password={password}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_strength_get',
        [
            '_@4-%o_rds',
            '$password',
            'x' * 100,
            'x' * 1000,
            'x' * 10000,
        ], ids=[
            '_@4-%o_rds',
            '$password',
            '100chars',
            '1000chars',
            '10000chars',
        ]
    )
    def test_api_bad_password(self, client_get_endpoint, bad_strength_get):
        # disambiguate
        password = bad_strength_get  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        response = client_get_endpoint.get(f"/get_strength?password={password}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'errors_get',
        [
            '_@4-#%o_rds',
            'pass#word',
            'pa&&word',
        ]
    )
    def test_query_string_truncation(self, client_get_endpoint, errors_get):
        # a `#` in the query string will be truncated
        # disambiguate
        password = errors_get  # flake8 will say this is bad; ignore that!

        response = client_get_endpoint.get(f"/get_strength?password={password}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        # the char `#` is not allowed in this url; anything after the `#`
        # is stripped from the request
        assert data.get('password') != password
        assert '#' not in data.get('password')

    @pytest.mark.parametrize(
        'errors_get',
        [
            '_@4-#%o_rds',
            'pass#word',
            'pa&&word',
        ]
    )
    def test_query_string_no_truncation_as_params(self, client_get_endpoint, errors_get):
        # a `#` in the query string will be truncated
        # disambiguate
        password = errors_get  # flake8 will say this is bad; ignore that!
        # assemble params
        params = {'password': password}

        response = client_get_endpoint.get('/get_strength', query_string=params)
        # print(f"url --> {response.url}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        # the char `#` is not allowed in this url; anything after the `#`
        # is stripped from the request
        assert data.get('password') == password

    @pytest.mark.parametrize(
        'div_by_zero_get',
        [
            '#password',
            ''
        ]
    )
    def test_api_error(self, client_get_endpoint, div_by_zero_get):
        # disambiguate
        password = div_by_zero_get  # flake8 will say this is bad; ignore that!

        with pytest.raises(ZeroDivisionError):
            client_get_endpoint.get(f"/get_strength?password={password}")


class TestApiPostThroughCode(object):

    @pytest.mark.parametrize(
        'good_strength_post',
        [
            '_@4-%@o_rds',
            '$$$$$$$ord',
            '_@4-#%o_rds',  # was get error
        ]
    )
    def test_api_good_password(self, client_post_endpoint, good_strength_post):
        # disambiguate
        password = good_strength_post  # flake8 will say this is bad; ignore that!
        expected_strength = 'good'

        # assemble the payload
        data = {'password': password}

        response = client_post_endpoint.post('/get_strength', json=data)
        assert response.status_code == 200
        res_data = json.loads(response.data.decode())

        print(f"res_data: {res_data}")
        assert res_data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_strength_post',
        [
            '_@4-%o_rds',
            '$password',
            'pass#word',  # was get error
            'pa&&word',   # was get error
            'x' * 100,
            'x' * 1000,
            'x' * 10000,
        ], ids=[
            '_@4-%o_rds',
            '$password',
            'pass#word',
            'pa&&word',
            '100chars',
            '1000chars',
            '10000chars',
        ]
    )
    def test_api_bad_password(self, client_post_endpoint, bad_strength_post):
        # disambiguate
        password = bad_strength_post  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        # assemble the payload
        data = {'password': password}

        response = client_post_endpoint.post('/get_strength', json=data)
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'div_by_zero_post',
        [
            '',
        ]
    )
    def test_api_divbyzeror_error(self, client_post_endpoint, div_by_zero_post):
        # disambiguate
        password = div_by_zero_post  # flake8 will say this is bad; ignore that!

        # assemble the payload
        data = {'password': password}

        with pytest.raises(ZeroDivisionError):
            client_post_endpoint.post('/get_strength', json=data)

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
    def test_api_type_error(self, client_post_endpoint, type_error_post):
        # disambiguate
        password = type_error_post  # flake8 will say this is bad; ignore that!

        # assemble the payload
        data = {'password': password}

        with pytest.raises(TypeError):
            client_post_endpoint.post('/get_strength', json=data)
