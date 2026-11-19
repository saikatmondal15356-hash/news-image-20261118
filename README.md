# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/saikatmondal15356-hash/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/saikatmondal15356-hash/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world's news of Wednesday 18 November 2026: a
newspaper front page with a UTC timeline of the day, led by Iran saying
it fired at a US base in Kuwait, Xi greeting Trump in Shenzhen, and
Voyager 1 reaching one light-day from Earth — 52 stories in all across
7 regions, 16 drawn panels with labelled scenes and three-line decks
that carry the facts, plus a pinned world map, and a date check that
Wednesday's news from Tuesday's (the Gaza warning, the Qeshm strike, the
Alaska Senate call, Nvidia's results, the Knesset vote, the Prague rail
crash, COP31's first draft) and from what had not happened yet
(Thursday's Trump–Xi–Putin summit, Anthropic's first trade, GTA VI's US
release, Cyclone Akvan's landfall). Also on the page: Amnesty's report on
RSF drone strikes in El Obeid, Category 5 Cyclone Xavier in the Cook
Islands, a magnitude 6.0 quake in Papua New Guinea, Australia's sanctions
on settler leader Daniella Weiss, and Iran's claim of downing a US MQ-9
drone over the Strait of Hormuz.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) decodes `entry.png.b64`
— the 1024×1024 PNG front page, drawn during the build — and writes it
to `$MAKEFUN_OUTPUT_DIR/entry.png`. It also checks the decoded bytes are
a PNG under the 1 MiB limit and exactly 1024×1024. No network, no clock,
no randomness: two runs write the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ddm5nwx4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
