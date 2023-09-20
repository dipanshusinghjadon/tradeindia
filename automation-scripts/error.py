import requests as r
urls = [
'/products/skin-graft-blade-c117.html',
'/products/standard-stitch-cutter-c120.html',
'/products/disposable-scalpel-blade-c121.html',
'/products/disposable-blade-remover-c123.html',
'/products/scalpel-blades-c125.html',
'/products/metallic-flexible-pump-connectors-c779.html',
'/products/hose-production-equipments-c780.html',
'/products/wire-braiding-machine-c781.html',
'/products/bobbin-winding-machine-c782.html',
'/products/exhaust-flex-pipe-c783.html',
'/products/metal-expansion-joints-c787.html',
'/products/metal-hose-assemblies-c880.html',
'/products/corrugated-flexible-hose-c881.html',
'/products/industrial-chasers-c1417.html',
'/products/circular-saw-blades-c1422.html',
'/products/circular-saw-blade-c1423.html',
'/products/circular-saw-paper-knives-c1424.html',
'/products/circular-saw-c1425.html',
'/products/t-c-t-circular-saw-blades-c1426.html',
'/products/special-slitting-saw-c1427.html'

]


for url in urls:
    new_url = f"https://beta-stag.tradeindia.com{url}"
    url1 = f"https://orig-www.tradeindia.com{url}"
    res1 = r.get(new_url)
    res2 = r.get(url1)
    print(url, ':', res1.status_code, ':',res2.status_code)