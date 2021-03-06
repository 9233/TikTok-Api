from TikTokApi import TikTokApi
import os

api = TikTokApi.get_instance(custom_verifyFp=os.environ.get("verifyFp", None))


def test_trending():
    assert abs(len(api.trending(5)) - 5) <= 2
    assert abs(len(api.trending(10)) - 10) <= 2
    assert abs(len(api.trending(20)) - 20) <= 2
