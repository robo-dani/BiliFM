"""download bilibili video series, 视频列表"""

import typer
from .util import request

headers: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com",
}


class Series:
    series_url: str = "https://api.bilibili.com/x/series/archives"

    def __init__(self, uid: str, series_id: str, page_size=30) -> None:
        self.uid = uid
        self.series_id = series_id
        self.page_size = page_size
        self.videos = []
        self.total = 0

    def get_videos(self):
        params = {
            "mid": self.uid,
            "series_id": self.series_id,
            "pn": 1,
            "ps": self.page_size,
            "current_id": self.uid,
        }

        def send_request():
            res =       request(
                method="get", url=self.series_url, params=params, headers=headers
            ).json()
            if res.get("code", -404) != 0:
                typer.echo(res)
                return None
            return res
        res = send_request()
        if res is None:
            return False

        self.total = res['data']["page"]["total"]
        while True:
            bvids = [ar["bvid"] for ar in res["data"]["archives"]]
            self.videos.extend(bvids)

            if len(self.videos) >= self.total or len(bvids) < self.page_size:
                #  len(bvids) < self.page_size indicate we've acquired the last part of series
                break

            params["pn"] += 1
            res = send_request()

            if res is None:
                typer.echo("encounter error, skip audios from {} to {}".format(
                    (params["pn"] -1) * self.page_size,
                    params["pn"] * self.page_size,
                ))

        return True
