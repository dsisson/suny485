import json
import pytest
import requests
from requests.exceptions import MissingSchema

from suny485.projects.hw14.api import app

"""
testable things for projects.hw14.api.py::get_password_strength()
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
"""


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiThroughCode(object):

    @pytest.mark.parametrize(
        'good_strength',
        [
            '_@4-%@o_rds',
            '$$$$$$$ord'
        ]
    )
    def test_api_good_password(self, client, good_strength):
        # disambiguate
        password = good_strength  # flake8 will say this is bad; ignore that!
        expected_strength = 'good'

        response = client.get(f"/get_strength?password={password}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_strength',
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
    def test_api_bad_password(self, client, bad_strength):
        # disambiguate
        password = bad_strength  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        response = client.get(f"/get_strength?password={password}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'errors',
        [
            '_@4-#%o_rds',
            'pass#word',
            'pa&&word',
        ]
    )
    def test_query_string_truncation(self, client, errors):
        # a `#` in the query string will be truncated
        # disambiguate
        password = errors  # flake8 will say this is bad; ignore that!

        response = client.get(f"/get_strength?password={password}")
        data = json.loads(response.data.decode())

        assert response.status_code == 200
        print(f"data: {data}")
        # the char `#` is not allowed in this url; anything after the `#`
        # is stripped from the request
        assert data.get('password') != password
        assert '#' not in data.get('password')

    @pytest.mark.parametrize(
        'div_by_zero',
        [
            '#password',
            ''
        ]
    )
    def test_api_error(self, client, div_by_zero):
        # disambiguate
        password = div_by_zero  # flake8 will say this is bad; ignore that!

        with pytest.raises(ZeroDivisionError):
            client.get(f"/get_strength?password={password}")


class TestApiThroughHttp(object):

    base = 'http://127.0.0.1:5000/get_strength?'

    @pytest.mark.parametrize(
        'good_strength',
        [
            '_@4-%@o_rds',
            '$$$$$$$ord',
        ], ids=[
            '_@4-%@o_rds',
            '$$$$$$$ord',
        ]
    )
    def test_api_good_password(self, good_strength):
        # disambiguate
        password = good_strength  # flake8 will say this is bad; ignore that!
        expected_strength = 'good'

        res = requests.get(f"{self.base}password={password}")
        assert res.status_code == 200

        data = res.json()
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    @pytest.mark.parametrize(
        'bad_strength',
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
    def test_api_bad_password(self, bad_strength):
        # disambiguate
        password = bad_strength  # flake8 will say this is bad; ignore that!
        expected_strength = 'bad'

        res = requests.get(f"{self.base}password={password}")
        data = res.json()

        assert res.status_code == 200
        print(f"data: {data}")
        assert data == {'password': password, 'strength': expected_strength}

    def test_api_bad_key(self):
        key = 'Password'
        query = f"{key}=password1"

        res = requests.get(f"{self.base}{query}")
        assert res.status_code == 500

    @pytest.mark.parametrize(
        'schema_errors',
        [
            'pass#word',
            'pa??word',
            'pa&&word',
        ]
    )
    def test_url_schema_error(self, client, schema_errors):
        # disambiguate
        password = schema_errors  # flake8 will say this is bad; ignore that!

        with pytest.raises(MissingSchema):
            requests.get(f"/get_strength?password={password}")
