import requests as r
import webbot as w
from time import sleep

urls = [

'/mumbai/oilseed-extraction-plant-in-andheri-east.html',
'/delhi/sheep-casings-in-ajmeri-gate.html',
'/chennai/fresh-eggs-in-alandur.html',
'/mumbai/fresh-eggs-in-byculla.html',
'/mumbai/fresh-eggs-in-dadar-west.html',
'/pune/fresh-eggs-in-wadgaon-sheri.html',
'/delhi/fresh-eggs-in-bawana.html',
'/delhi/fresh-eggs-in-chandni-chowk.html',
'/delhi/fresh-eggs-in-gandhi-nagar.html',
'/delhi/fresh-eggs-in-shalimar-bagh.html',
'/ghaziabad/poultry-feed-in-raj-nagar-rdc.html',
'/indore/poultry-feed-in-rnt-marg.html',
'/indore/poultry-feed-in-ushaganj.html',
'/mumbai/poultry-feed-in-chandivali.html',
'/delhi/poultry-feed-in-chandni-chowk.html',
'/delhi/poultry-feed-in-chawri-bazar.html',
'/delhi/poultry-feed-in-laxmi-nagar.html',
'/delhi/poultry-feed-in-rohini.html',
'/delhi/poultry-feed-in-vasundhara-enclave.html',
'/delhi/educational-models-india-in-madhu-vihar.html',
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
'/products/special-slitting-saw-c1427.html',
'/products/ladies-cotton-crepe-printed-blouse-377.html',
'/products/censer-386.html',
'/products/saree-guard-for-two-wheelers-553.html',
'/products/incense-cones-610.html',
'/products/parimal-incense-sticks-632.html',
'/products/industrial-painted-cable-trays-642.html',
'/products/air-dust-bellow-for-2-wheeler-667.html',
'/products/cctv-cables-689.html',
'/products/centrifugal-fans-690.html',
'/products/pitless-type-weighbridge-700.html',
'/products/sculpture-706.html',
'/products/stone-rainbow-717.html',
'/products/amplifiers-721.html',
'/products/magnetic-proximity-switches-for-security-alarm-systems-731.html',
'/products/cutlery-753.html',
'/products/full-shirt-with-overcoat-755.html',
'/products/welding-helmet-1174.html',
'/products/building-insulation-materials-1202.html',
'/products/core-holding-chucks-1239.html',
'/products/numerical-control-machined-components-1248.html'

]

for url in urls:
    new_url = f"https://beta-stag.tradeindia.com{url}"
    if url:
        brw = w.Browser()
        brw.go_to(new_url)
        del brw

    sleep(1)