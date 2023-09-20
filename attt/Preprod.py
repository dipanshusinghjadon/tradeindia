import requests as r
import webbot as w
from time import sleep

urls = [

'https://preprod.tradeindia.com/',
'https://preprod.tradeindia.com/seller/',
'https://preprod.tradeindia.com/seller/agriculture/',
'https://preprod.tradeindia.com/seller/agriculture/rice/',
'https://preprod.tradeindia.com/services/',
'https://preprod.tradeindia.com/services/advertising/',
'https://preprod.tradeindia.com/services/advertising/brochure-advertising-services/',
'https://preprod.tradeindia.com/manufacturers/',
'https://preprod.tradeindia.com/manufacturers/sella-basmati-rice.html',
'https://preprod.tradeindia.com/business-services/',
'https://preprod.tradeindia.com/business-services/digital-brochure-advertising.html',
'https://preprod.tradeindia.com/delhi/sella-basmati-rice-city-228067.html',
'https://preprod.tradeindia.com/delhi/sella-basmati-rice-in-rohini.html',
'https://preprod.tradeindia.com/products/',
'https://preprod.tradeindia.com/products/long-grain-basmati-rice-c6453433.html',
'https://preprod.tradeindia.com/products/agriculture-black-mulching-film-7093444.html',
'https://preprod.tradeindia.com/gananathan-traders-27479462/',
'https://preprod.tradeindia.com/canwin-imports-exports-34250712/',
'https://preprod.tradeindia.com/rajesh-eneterprise-18708017/',
'https://preprod.tradeindia.com/country-suppliers/',
'https://preprod.tradeindia.com/jp/',
'https://preprod.tradeindia.com/jp/hospital-medical-supplies/',
'https://preprod.tradeindia.com/jp/hospital-medical-supplies/medical-equipment/',
'https://preprod.tradeindia.com/jp/vessel-sealing-system.html',
'https://preprod.tradeindia.com/industry-hubs/',
'https://preprod.tradeindia.com/industry-hubs/andhra-pradesh.html',
'https://preprod.tradeindia.com/industry-hubs/andhra-pradesh/guntur.html',
'https://preprod.tradeindia.com/my-tradeindia/',
'https://preprod.tradeindia.com/login/login.html',
'https://preprod.tradeindia.com/join_now/verification.html',
'https://preprod.tradeindia.com/tradekhata/',
'https://preprod.tradeindia.com/about-us/',
'https://preprod.tradeindia.com/TradeLeads/',
'https://preprod.tradeindia.com/Buyer/',
'https://preprod.tradeindia.com/sitemap.html',
'https://preprod.tradeindia.com/search.html?search_return_url=%2F&search_form_id=18&keyword=human+hair',
'https://preprod.tradeindia.com/tradeshows/',
'https://preprod.tradeindia.com/tradeshows/all-categories.html',
'https://preprod.tradeindia.com/tradeshows/agriculture/',
'https://preprod.tradeindia.com/tradeshows/agriculture/city/mumbai/207486/',
'https://preprod.tradeindia.com/tradeshows/agriculture/year-2022/november/',
'https://preprod.tradeindia.com/tradeshows/all-cities.html',
'https://preprod.tradeindia.com/tradeshows/city/mumbai/207486/',
'https://preprod.tradeindia.com/tradeshows/city/mumbai/207486/year-2022/november/',
'https://preprod.tradeindia.com/tradeshows/all-countries.html',
'https://preprod.tradeindia.com/tradeshows/country/india/',
'https://preprod.tradeindia.com/tradeshows/country/india/city/mumbai/207486/',
'https://preprod.tradeindia.com/tradeshows/country/india/year-2022/november',
'https://preprod.tradeindia.com/tradeshows/112131/auto-expo-components-2023.html',
'https://preprod.tradeindia.com/tradeshows/virtual-events/',
'https://preprod.tradeindia.com/tradeshows/year-2022/november/',
'https://preprod.tradeindia.com/tradeshows/organisers-listing.html',
'https://preprod.tradeindia.com/tradeshows/organizer-11377129/media-day-marketing.html',
'https://preprod.tradeindia.com/tradeshows/venue-listing.html',
'https://preprod.tradeindia.com/tradeshows/venue/biec-bengaluru/6444/',
'https://preprod.tradeindia.com/tradeshows/tradeindia-participated-trade-shows.html',
'https://preprod.tradeindia.com/tradeshows/fairs/indiawood_2020.html',
'https://preprod.tradeindia.com/tradeshows/tradeindia-will-participate-trade-shows.html',
'https://preprod.tradeindia.com/tradeshows/109190/pacprocess-food-pex-mumbai-2022.html',
'https://preprod.tradeindia.com/tradeshows/advertise.html',
'https://preprod.tradeindia.com/tradeshows/trade_show_form.html',
'https://preprod.tradeindia.com/blog/',
'https://preprod.tradeindia.com/design2017/sourcing/sourcing_requirements.html',
'https://preprod.tradeindia.com/TradeLeads/buy/Packaging-Paper/Adhesive-Tapes/',
'https://preprod.tradeindia.com/communities/6/3129/Payment-Modes-Finance-Issues/Cash-Against-Delivery-CAD-the-pros-cons.html',
'https://preprod.tradeindia.com/survey/109/index.html',
'https://preprod.tradeindia.com/ti_forms/rfq/rfq_action.html',
'https://preprod.tradeindia.com/tradeindia-news.html',
'https://careers.tradeindia.com/',
'https://preprod.tradeindia.com/about-us/contact-us/',
'https://preprod.tradeindia.com/about-us/partner-with-us.html',
'https://pay.tradeindia.com/',
'https://preprod.tradeindia.com/return-cancellation-policy.html',
'https://preprod.tradeindia.com/shipping-and-delivery-policy.html',
'https://preprod.tradeindia.com/about-us/product-and-services/product-and-services.html',
'https://preprod.domainjerry.com/',
'https://preprod.tradeindia.com/newsletters/newsletter_archives.html',
'https://preprod.tradeindia.com/about-us/order/credit-report.html',
'https://preprod.tradeindia.com/rewards.html',
'https://preprod.tradeindia.com/ti-pay/',
'https://preprod.tradeindia.com/download-getbizonline.html',
'https://preprod.tradeindia.com/ti_logistics/',
'https://preprod.tradeindia.com/vcard/',
'https://preprod.tradeindia.com/join_now/subscribe_to_trade_alerts.html?type=Sell',
'https://preprod.tradeindia.com/join_now/upload_product.html',
'https://preprod.tradeindia.com/about-us/terms/terms_01.html',
'https://preprod.tradeindia.com/ti-lending/',

]

print("URL,STATUS_CODE")

for url in urls:
    # new_url = f"https://preprod.tradeindia.com{url}"
    if url:
        try:
            resp = r.get(url)
        except:
            print(f"{url},Failed")
        else:
            print(f"{url},{resp.status_code}")
        # brw = w.Browser()
        # brw.go_to(url)
        # del brw

    sleep(1)