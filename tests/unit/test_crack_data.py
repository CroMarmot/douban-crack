import re

from douban_crack.crack_data.crack_data import crack_data, crack_data_v0_0_2

from . import mock_html


def test_crack_data():
    html = mock_html("book")
    data: str = re.search('window.__DATA__ = "([^"]+)"', html).group(1)  # 加密的数据
    result = crack_data(data)
    assert len(result) == 1
    assert len(result[0]) == 57


def test_crack_data_v0_0_2():
    html = mock_html("book")
    data: str = re.search('window.__DATA__ = "([^"]+)"', html).group(1)  # 加密的数据
    result = crack_data_v0_0_2(data)
    import json

    assert len(result["payload"]["items"]) == 16
    print(json.dumps(result["payload"]["items"][1], ensure_ascii=False, indent=2))
    assert result["payload"]["items"][1] == {
        "id": 6854525,
        "url": "https://book.douban.com/subject/6854525/",
        "rating": {"rating_info": "", "value": 7.8, "star_count": 4, "count": 8816},
        "more_url": "onclick=\"moreurl(this,{i:'0',query:'%E9%BB%91%E5%A4%A9%E9%B9%85',subject_id:'6854525',from:'book_subject_search',cat_id:'1001'})\"",
        "abstract": "纳西姆•尼古拉斯•塔勒布 (Nassim Nicholas Taleb) / 万丹 / 刘宁 / 中信出版社 / 2011-10-1 / 49.00元",
        "abstract_2": "",
        "title": "黑天鹅 : 如何应对不可预知的未来",
        "extra_actions": [
            {
                "color": "#973F31",
                "text": "豆瓣阅读电子版",
                "url": "https://read.douban.com/ebook/2010442/?dcs=search-buylink&dcm=douban&dct=6854525",
            }
        ],
        "topics": [],
        "label_actions": [],
        "tpl_name": "search_subject",
        "interest": None,
        "cover_url": "https://img2.doubanio.com/view/subject/m/public/s28991761.jpg",
        "labels": [],
    }
