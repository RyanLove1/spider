'''抓取腾讯视频'''

import requests


def get_tencent_video():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    vids = "e00316w2fzo"
    url = "http://vv.video.qq.com/getinfo?vids={}&platform=101001&charge=0&otype=json".format(vids)
    response = requests.get(url, headers=header)
    json_text = response.text
    print(json_text)
    fvkey = "DBC55730D54589A20194BF805B4A52319A33CB76255B85979D4792C6B49282B2CAEB48A3B0AAB96070420F3E6FE76BAD3884168CCA5A201EB2725CE153C2DFBEF504CEF362D23CC1414C791B431DF5102015673C3A7F4FA969DC6E67EDFB31CE4B676C49F1BEC8A1EDDE32DD9F4A4ED7"
    re_url = "http://183.192.163.154/vlive.qqvideo.tc.qq.com/AJKG8LvxBGpk3mq8q72kPs2DMlmISn5Jtyu8QbM1XkdU/uwMROfz2r5zAoaQXGdGnCWdfiMWgH5k-_llZA2_eVQs5f0Er/"
    video_mp = "e00316w2fzo.m1.mp4"
    video_url = re_url + video_mp + "?vkey=" + fvkey
    res = requests.get(video_url, headers=header)
    with open("斗破.mp4", "ab") as f:
        f.write(res.content)
        f.flush()


if __name__ == "__main__":
    get_tencent_video()
