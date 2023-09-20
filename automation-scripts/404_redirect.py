import requests as r
import webbot as w
from time import sleep

urls = [

'/jd-creation-6102757/cardigan.html',
'/earthing-solutions-7402734/spark-arrestor.html',
'/shreeya-fasteners-10955358/t-bolts.html',
'/ue-store-10655474/cctv-camera.html',
'/earthing-solutions-7402734/spark-arrestor.html',
'/toyo-ink-india-pvt-ltd-9977556/printing-ink.html',
'/earthing-solutions-7402734/spark-arrestor.html',
'/d-p-designs-pvt-ltd-1046407/gold-pendants.html',
'/shreeya-fasteners-10955358/t-bolts.html',
'/rane-nsk-steering-systems-pvt-ltd-26831391/seat-belt.html',
'/kheya-collections-5271664/fancy-designer-sarees.html',
'/elmech-motors-controls-3326250/high-speed-motor.html',
'/jaaheshwar-international-6541857/fresh-vegetables.html',
'/tolexmart-com-10863672/insulated-terminal.html',
'/crystrong-photoelectric-technology-co-ltd-8653562/crystallizer.html',
'/batliboi-ltd-10158856/cnc-turning-centre.html',
'/r-k-light-house-7501648/led-lights.html',
'/batliboi-ltd-10158856/cnc-turning-centre.html',
'/p-i-industries-limited-5372831/agricultural-insecticides.html',
'/yan-shan-yong-hui-steel-pipe-co-ltd-3929262/rolled-steel-tubes.html',
'/n-gen-stamp-9824569/stamping.html',
'/kripa-international-india-348352/fiberglass-fabric.html',
'/media-fusion-india-pvt-ltd-5570728/jewelry-books.html',
'/seven-star-35001427/upvc-french-windows.html',
'/senkay-global-tours-event-management-pvt-ltd-13159769/tour-packages-services.html',
'/gondals-press-india-ltd-2256867/calendar-printing-services.html',
'/eveready-industries-india-ltd-23674677/torches.html',
'/cann-office-equipment-pvt-ltd-10210224/digital-photocopier-machine.html',
'/sri-vishnu-industries-1947162/gauze-bandage.html',
'/linear-motion-solutions-10686727/industrial-chains.html',
'/ningbo-gemfan-international-trading-co-ltd-3375260/propellers.html',
'/indigo-design-studio-9813238/sleeveless-jackets.html',
'/kss-greens-9840892/led-bulbs.html',
'/sri-vishnu-industries-1947162/gauze-swab.html',
'/rachna-rotopack-industries-2576834/flexible-packaging-films.html',
'/sunil-fastners-24695815/steel-flat-washer.html',
'/akuma-global-exporters-ltd-5274996/pet-bottles-scrap.html',
'/shree-roshan-metal-industries-17451015/water-jet-cutter.html',
'/aks-exim-india-2209789/coriander-seeds.html',
'/morinda-international-7765376/millet-flakes.html',
'/serial-publication-258617/jewelry-books.html',
'/duyachi-batteries-10703773/tubular-batteries.html',
'/india-gelatine-chemicals-ltd-225222/edible-gelatin.html',
'/kavira-fashions-pvt-ltd-8058258/suiting-fabrics.html',
'/deepthi-hydromech-5545393/circular-saw-machine.html',
'/sai-aditya-foods-retail-pvt-ltd-7653362/birthday-cake.html',
'/gomes-elina-garments-pvt-ltd-9681877/custom-t-shirt.html',
'/socomec-innovative-power-solutions-pvt-ltd-2839579/capacitor-part.html',
'/madura-industrial-textiles-limited-11159972/tire-cord-fabric.html',
'/alfa-chemicals-leather-company-12030000/rump-steak.html',
'/soca-farmers-5527197/cow-milk.html',
'/jmd-flour-edible-oil-mills-pvt-ltd-3855352/mustard-oil.html',
'/p-i-industries-limited-5372831/thiamethoxam.html',
'/toyo-ink-india-pvt-ltd-9977556/printing-ink.html',
'/alcon-wireless-pvt-ltd-8689319/cctv-camera.html',
'/suzhou-huayu-electronics-technology-co-ltd-27207327/jaundice-meter.html',
'/philco-crafts-2238258/disposable-cutlery.html',
'/shanti-trading-company-2768869/ring-washers.html',
'/sharada-oil-industries-3223724/oil-can.html',
'/suzhou-hadiya-transmission-technology-co-ltd-11504653/high-pressure-fans.html',
'/amiya-bedding-store-2556175/single-bed-sheets.html',
'/tech-mech-engineering-services-8375171/roller.html',
'/design-steen-10856269/acrylic-modular-kitchen.html',
'/deepthi-hydromech-5545393/turning-lathes.html',
'/safari-industries-i-pvt-ltd-8124805/duffle-bag.html',
'/sunshine-collections-5746130/ladies-leather-shoes.html',
'/fancy-dress-darzee-9470569/belly-dance-costumes.html',
'/toyo-ink-india-pvt-ltd-9977556/printing-ink.html',
'/j3-vista-printers-publishers-pvt-ltd-8431946/brochures.html',
'/p-i-industries-limited-5372831/thiamethoxam.html',
'/canixa-life-sciences-private-limited-9658153/ointment.html',
'/cixi-tonghui-photovoltaic-technology-co-ltd-3401720/junction-box.html',
'/aplab-limited-2421003/solar-generators.html',
'/jeffrey-garments-3440675/kids-western-wear.html',
'/jal-industries-4036406/industrial-pressure-vessels.html',
'/sunheat-electrical-1873131/high-density-cartridge-heaters.html',
'/chandra-enterprises-19425793/plastic-granules.html',
'/sonal-engineering-company-3919572/air-receiver-tank.html',
'/kasturi-enterprises-9444150/led-bulbs.html',
'/natures-basket-ltd-7397608/chocolate.html',
'/shree-vallabh-trade-9949699/round-bars.html',
'/shree-vallabh-trade-9949699/round-bars.html',
'/alcon-wireless-pvt-ltd-8689319/cctv-camera.html',
'/my-home-furniture-10287346/bedroom-bed.html',
'/sidharth-automat-india-pvt-ltd-1840112/industrial-fabrication-services.html',
'/shanti-doot-co-12382270/ladies-pants.html',
'/lara-machinery-co-9962385/pvc-processing-machine.html',
'/ma-sharda-enterprises-28261739/regular-water-cooler.html',
'/j-j-marble-granite-11019068/kadappa-stone.html',
'/tong-i-hsing-light-industrial-pvt-ltd-8767289/diving-helmet.html',
'/namicom-llc-4637760/bird-eggs.html',
'/shaurya-foods-6871292/high-protein-snacks.html',
'/subam-paper-works-2886655/bags.html',
'/barock-industries-26072627/mould-bases.html',
'/k-b-products-pvt-ltd-6103667/ghee.html',
'/hawa-valves-india-pvt-ltd-1426757/check-valves.html',
'/p-r-packaging-2848598/duplex-cartons.html',
'/guangzhou-sanse-technology-co-ltd-5409015/ddr-memory.html',
'/hangzhou-great-bicycle-co-ltd-5802035/bicycle-tyres.html',

]

for url in urls:
    new_url = f"https://beta-stag.tradeindia.com{url}"
    res1 = r.get(new_url)
    print(url,':', res1.status_code)
    if url:
        brw = w.Browser()
        brw.go_to(new_url)
        del brw

    sleep(1)