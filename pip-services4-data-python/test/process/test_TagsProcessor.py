# -*- coding: utf-8 -*-
from pip_services4_data.process import TagsProcessor


class TestTagsProcessor:

    def test_normalize_tags(self):
        tag = TagsProcessor.normalize_tag('  A_b#c ')
        assert 'A b c' == tag

        tags = TagsProcessor.normalize_tags(['  A_b#c ', 'd__E f'])
        assert len(tags) == 2
        assert 'A b c' == tags[0]
        assert 'd E f' == tags[1]

        tags = TagsProcessor.normalize_tag_list('  A_b#c ,d__E f;;')
        assert len(tags) == 3
        assert 'A b c' == tags[0]
        assert 'd E f' == tags[1]

    def test_compress_tags(self):
        tag = TagsProcessor.compress_tag('  A_b#c ')
        assert 'abc' == tag

        tags = TagsProcessor.compress_tags(['  A_b#c ', 'd__E f'])
        assert len(tags) == 2
        assert 'abc' == tags[0]
        assert 'def' == tags[1]

        tags = TagsProcessor.compress_tag_list('  A_b#c ,d__E f;;')
        assert len(tags) == 3
        assert 'abc' == tags[0]
        assert 'def' == tags[1]

    def test_extract_hash_tags(self):
        tags = TagsProcessor.extract_hash_tags('  #Tag_1  #TAG2#tag3 ')
        assert len(tags) == 3
        assert 'tag1' == tags[0]
        assert 'tag2' == tags[1]
        assert 'tag3' == tags[2]

    def test_extract_hash_tags_from_value(self):
        tags = TagsProcessor.extract_hash_tags_from_value(
            {
                'tags': ['Tag 1', 'tag_2', 'TAG3'],
                'name': 'Text with tag1 #Tag1',
                'description': 'Text with #tag_2,#tag3-#tag4 and #TAG__5'
            },
            'name', 'description'
        )
        assert list({'tag1', 'tag2', 'tag3', 'tag4', 'tag5'} - set(tags)) == []

    def test_extract_hash_tags_from_object(self):
        tags = TagsProcessor.extract_hash_tags_from_value(
            {
                'tags': ['Tag 1', 'tag_2', 'TAG3'],
                'name': {
                    'short': 'Just a name',
                    'full': 'Text with tag1 #Tag1'
                },
                'description': {
                    'en': 'Text with #tag_2,#tag4 and #TAG__5',
                    'ru': 'Текст с #tag_2,#tag3 и #TAG__5'
                }
            },
            'name', 'description'
        )
        assert list({'tag1', 'tag2', 'tag3', 'tag4', 'tag5'} - set(tags)) == []
