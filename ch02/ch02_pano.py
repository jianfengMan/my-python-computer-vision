import os
import urllib.request as request
import urllib.parse as urlparse
import json

URL = 'http://www.panoramio.com/map/get_panoramas.php?' \
      'order=popularity&set=public&size=medium&' \
      'from=20&to={n}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}'

# python2中有urllib、urllib2、urlparse，但在python3中这些全部都被整合到了urllib中。
# urllib和urllib2中的内容整合进了urllib.request模块中，
# urlparse整合进了urllib.parse中。python3中urllib中还包括response、error和robotparse这些子模块。

# Santa cruz lighthouse: x=-122.026618 y=36.951614
# White house: x=-77.038564 y=38.897662

x = -122.026618
y = 36.951614
d = 0.001
url = URL.format(
    n=40, minx=x - d, miny=y - d, maxx=x + d, maxy=y + d)

j = json.loads(request.urlopen(url).read())
imurls = [im['photo_file_url'] for im in j['photos']]

for url in imurls:
    image = request.URLopener()
    base = os.path.basename(urlparse.urlparse(url).path)
    image.retrieve(url, os.path.join('out', base))
    print('downloading', url)
