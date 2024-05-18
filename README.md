# TKY2JGD

![PyPI - tky2jgd](https://img.shields.io/pypi/v/tky2jgd)
![pytest status](https://img.shields.io/github/actions/workflow/status/shuuji3/tky2jgd/main.yaml?branch=main)

国土地理院のTKY2JGDをPythonに移植したものです。

オリジナルのTKY2JGDは<http://vldb.gsi.go.jp/sokuchi/tky2jgd/download/down.cgi>からダウンロードできます。

座標変換パラメータファイル`data/TKY2JGD.par`はv2.1.1を使用しています。

## Usage

```
$ python3 tky2jgd.py 36.103774791666666 140.08785504166664
36.10696628160147 140.08457686629436
```

```python
import tky2jgd

tky2jgd.load_parameter("data/TKY2JGD.par")
# Original First-class Triangulation Point at the Japan GSI Tsukuba
lat, lon = 36.100578889, 140.091149167
dB, dL = tky2jgd.bilinear(lat, lon)
lat += dB / 3600
lon += dL / 3600
assert (lat, lon) == (36.10377077065109, 140.08787082896106)
```
        lat, lon = 36.100578889, 140.091149167 # Tsukuba Original First-class Triangulation Point
        dB, dL = bilinear(lat, lon)
        lat += dB / 3600
        lon += dL / 3600
        assert (lat, lon) == (36.10377077065109, 140.08787082896106)
## Credits

- Original application TKY2JGD developed by Japan GSI: http://vldb.gsi.go.jp/sokuchi/tky2jgd/download/down.cgi
- Original Python port: https://github.com/mugwort-rc/TKY2JGD

This repository updates and refactors codes and publishes it as a PyPI package.
