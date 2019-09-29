import unittest
from datetime import datetime, timezone
from nasty.search.tweet import Tweet
from nasty.init import init_nasty

tweet_json = {
    # Tweet accessed via Search API on 2019-09-27
    '1142944425502543875': {
        'created_at': 'Sun Jun 23 23:56:00 +0000 2019',
        'id': 1142944425502543875,
        'id_str': '1142944425502543875',
        'full_text': 'It is obvious that Mr. Trump is a terrible judge of cha'
                     'racter. His nominees for various high level cabinet pos'
                     'itions have been unqualified, unforthcoming, or engaged'
                     ' in behavior unbecoming of a public servant. His standa'
                     'rds should not be our standards. https://t.co/CHuQqFs5E'
                     'X',
        'truncated': False,
        'display_text_range': [0, 276],
        'entities': {
            'hashtags': [],
            'symbols': [],
            'user_mentions': [],
            'urls': [{'url': 'https://t.co/CHuQqFs5EX',
                      'expanded_url': 'https://www.washingtonpost.com/opinion'
                                      's/global-opinions/the-white-house-is-a'
                                      'llowing-personal-scandals-to-become-na'
                                      'tional-embarrassments/2019/06/20/122f4'
                                      'e84-938b-11e9-b570-6416efdc0803_story.'
                                      'html?utm_term=.790cde3fee18',
                      'display_url': 'washingtonpost.com/opinions/globa…',
                      'indices': [253, 276]}]},
        'source': '<a href="https://sproutsocial.com" rel="nofollow">Sprout S'
                  'ocial</a>',
        'in_reply_to_status_id': None,
        'in_reply_to_status_id_str': None,
        'in_reply_to_user_id': None,
        'in_reply_to_user_id_str': None,
        'in_reply_to_screen_name': None,
        'geo': None,
        'coordinates': None,
        'place': None,
        'contributors': None,
        'is_quote_status': False,
        'retweet_count': 1109,
        'favorite_count': 3709,
        'reply_count': 241,
        'conversation_id': 1142944425502543875,
        'conversation_id_str': '1142944425502543875',
        'favorited': False,
        'retweeted': False,
        'possibly_sensitive': False,
        'possibly_sensitive_editable': True,
        'lang': 'en',
        'supplemental_language': None,
        'user': {
            'id': 949934436,
            'id_str': '949934436',
            'name': 'Tom Steyer',
            'screen_name': 'TomSteyer',
            'location': 'San Francisco, CA',
            'description': 'Husband & father. Former investor. Signed The Giv'
                           'ing Pledge to donate the majority of my net worth'
                           ' in my lifetime. He/him. 2020 Democrat for presid'
                           'ent.',
            'url': 'https://t.co/n1r4Xd6IXH',
            'entities': {
                'url': {
                    'urls': [{
                        'url': 'https://t.co/n1r4Xd6IXH',
                        'expanded_url': 'https://go.tomsteyer.com/ts2020',
                        'display_url': 'go.tomsteyer.com/ts2020',
                        'indices': [0, 23]}]},
                'description': {
                    'urls': []}},
            'protected': False,
            'followers_count': 245080,
            'fast_followers_count': 0,
            'normal_followers_count': 245080,
            'friends_count': 1086,
            'listed_count': 2764,
            'created_at': 'Thu Nov 15 15:28:50 +0000 2012',
            'favourites_count': 3535,
            'utc_offset': None,
            'time_zone': None,
            'geo_enabled': False,
            'verified': True,
            'statuses_count': 8513,
            'media_count': 812,
            'lang': None,
            'contributors_enabled': False,
            'is_translator': False,
            'is_translation_enabled': False,
            'profile_background_color': '666666',
            'profile_background_image_url':
                'http://abs.twimg.com/images/themes/theme2/bg.gif',
            'profile_background_image_url_https':
                'https://abs.twimg.com/images/themes/theme2/bg.gif',
            'profile_background_tile': False,
            'profile_image_url':
                'http://pbs.twimg.com/profile_images/1148571376355119104/EqZu'
                'tNij_normal.png',
            'profile_image_url_https':
                'https://pbs.twimg.com/profile_images/1148571376355119104/EqZ'
                'utNij_normal.png',
            'profile_banner_url':
                'https://pbs.twimg.com/profile_banners/949934436/1562688733',
            'profile_image_extensions_media_color': {
                'palette': [
                    {'rgb': {'red': 23, 'green': 44, 'blue': 73},
                     'percentage': 50.97},
                    {'rgb': {'red': 202, 'green': 158, 'blue': 142},
                     'percentage': 29.1},
                    {'rgb': {'red': 112, 'green': 77, 'blue': 69},
                     'percentage': 11.04},
                    {'rgb': {'red': 213, 'green': 224, 'blue': 232},
                     'percentage': 7.46},
                    {'rgb': {'red': 18, 'green': 39, 'blue': 69},
                     'percentage': 0.3}]},
            'profile_image_extensions_alt_text': None,
            'profile_image_extensions_media_availability': None,
            'profile_image_extensions': {
                'mediaStats': {'r': {'missing': None},
                               'ttl': -1}},
            'profile_banner_extensions_media_color':
                {'palette': [
                    {'rgb': {'red': 179, 'green': 154, 'blue': 132},
                     'percentage': 28.83},
                    {'rgb': {'red': 71, 'green': 48, 'blue': 42},
                     'percentage': 28.18},
                    {'rgb': {'red': 174, 'green': 186, 'blue': 222},
                     'percentage': 17.33},
                    {'rgb': {'red': 115, 'green': 112, 'blue': 117},
                     'percentage': 11.66},
                    {'rgb': {'red': 155, 'green': 92, 'blue': 87},
                     'percentage': 1.96}]},
            'profile_banner_extensions_alt_text': None,
            'profile_banner_extensions_media_availability': None,
            'profile_banner_extensions': {
                'mediaStats': {'r': {'missing': None},
                               'ttl': -1}},
            'profile_link_color': '2802A3',
            'profile_sidebar_border_color': '000000',
            'profile_sidebar_fill_color': 'FFEBD6',
            'profile_text_color': '605CBA',
            'profile_use_background_image': True,
            'has_extended_profile': False,
            'default_profile': False,
            'default_profile_image': False,
            'pinned_tweet_ids': [1175916938305949696],
            'pinned_tweet_ids_str': ['1175916938305949696'],
            'has_custom_timelines': True,
            'can_dm': None,
            'can_media_tag': None,
            'following': None,
            'follow_request_sent': None,
            'notifications': None,
            'muting': None,
            'blocking': None,
            'blocked_by': None,
            'want_retweets': None,
            'advertiser_account_type': 'promotable_user',
            'advertiser_account_service_levels':
                ['dso', 'media_studio', 'smb', 'dso', 'mms', 'smb', 'dso'],
            'profile_interstitial_type': '',
            'business_profile_state': 'none',
            'translator_type': 'none',
            'followed_by': None,
            'require_some_consent': False}}
}


class TestTweet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_nasty()

    def test_1142944425502543875(self):
        tweet = Tweet(tweet_json['1142944425502543875'])
        self.assertEqual(datetime(year=2019, month=6, day=23,
                                  hour=23, minute=56, second=0,
                                  tzinfo=timezone.utc),
                         tweet.created_at)
        self.assertEqual('1142944425502543875', tweet.id)
        self.assertEqual('It is obvious that Mr. Trump is a terrible judge of'
                         ' character. His nominees for various high level cab'
                         'inet positions have been unqualified, unforthcoming'
                         ', or engaged in behavior unbecoming of a public ser'
                         'vant. His standards should not be our standards. ht'
                         'tps://t.co/CHuQqFs5EX', tweet.text)
        self.assertEqual(
            'https://twitter.com/TomSteyer/status/1142944425502543875',
            tweet.url)

        self.assertEqual('949934436', tweet.user.id)
        self.assertEqual('Tom Steyer', tweet.user.name)
        self.assertEqual('TomSteyer', tweet.user.screen_name)
        self.assertEqual('https://twitter.com/TomSteyer', tweet.user.url)

        self.assertEqual(tweet, Tweet.from_json(tweet.to_json()))


if __name__ == '__main__':
    unittest.main()
