"""推荐相关 API"""

from .utils.network import NO_PROCESSOR, api_request


@api_request("music.recommend.RecommendFeed", "get_recommend_feed")
async def get_home_feed():
    """获取主页推荐"""
    return {
        "direction": 0,
        "page": 1,
        "s_num": 0,
    }, NO_PROCESSOR


@api_request("music.radioProxy.MbTrackRadioSvr", "get_radio_track")
async def get_guess_recommend():
    """获取猜你喜欢"""
    return {
        "id": 99,
        "num": 5,
        "from": 0,
        "scene": 0,
        "song_ids": [],
        "ext": {"bluetooth": ""},
        "should_count_down": 1,
    }, NO_PROCESSOR
