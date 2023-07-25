# -*- coding: utf-8 -*-
from pip_services4_data.data import MultiString


class TestMultiString:

    def test_crud(self):
        multi_string = MultiString()
        multi_string.append({'fr': 'Bonjour tout le monde!'})
        multi_string.append({'ru': 'Привет мир!'})
        multi_string.append({'en': 'do you speak english'})

        assert multi_string == {'fr': 'Bonjour tout le monde!',
                                'ru': 'Привет мир!',
                                'en': 'do you speak english'}

        assert multi_string.get_languages() == ['fr', 'ru', 'en']
        assert multi_string.get('en') == 'do you speak english'
        multi_string.remove('en')
        assert multi_string.get_languages() == ['fr', 'ru']

    def test_multistring_from(self):
        from_tuples = MultiString.from_tuples('en', 'do you speak english',
                                              'fr', 'parle français',
                                              'de', 'sprichst du deutsch'
                                              )
        assert len(from_tuples) == 3
        assert from_tuples == {'en': 'do you speak english',
                               'fr': 'parle français',
                               'de': 'sprichst du deutsch'}
        from_value = MultiString.from_value({'en': 'do you speak english'})
        assert from_value == {'en': 'do you speak english'}
