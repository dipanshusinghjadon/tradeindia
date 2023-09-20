import requests as r
from time import sleep
from selenium import webdriver
URL = "https://housekeeping.tradeindia.com"
BINARY_EXECUTABLE_PATH = './chromedriver'

browser = webdriver.Chrome(executable_path=BINARY_EXECUTABLE_PATH)

urls = [

'https://dev2fe.tradeindia.com/',
'https://dev2fe.tradeindia.com/seller/',
'https://dev2fe.tradeindia.com/seller/agriculture/',
'https://dev2fe.tradeindia.com/seller/agriculture/rice/',
'https://dev2fe.tradeindia.com/services/',
'https://dev2fe.tradeindia.com/services/advertising/',
'https://dev2fe.tradeindia.com/services/advertising/brochure-advertising-services/',
'https://dev2fe.tradeindia.com/manufacturers/',
'https://dev2fe.tradeindia.com/manufacturers/sella-basmati-rice.html',
'https://dev2fe.tradeindia.com/business-services/',
'https://dev2fe.tradeindia.com/business-services/digital-brochure-advertising.html',
'https://dev2fe.tradeindia.com/delhi/sella-basmati-rice-city-228067.html',
'https://dev2fe.tradeindia.com/delhi/sella-basmati-rice-in-rohini.html',
'https://dev2fe.tradeindia.com/products/',
'https://dev2fe.tradeindia.com/products/long-grain-basmati-rice-c6453433.html',
'https://dev2fe.tradeindia.com/products/agriculture-black-mulching-film-7093444.html',
'https://dev2fe.tradeindia.com/gananathan-traders-27479462/',
'https://dev2fe.tradeindia.com/canwin-imports-exports-34250712/',
'https://dev2fe.tradeindia.com/rajesh-eneterprise-18708017/',
'https://dev2fe.tradeindia.com/country-suppliers/',
'https://dev2fe.tradeindia.com/jp/',
'https://dev2fe.tradeindia.com/jp/hospital-medical-supplies/',
'https://dev2fe.tradeindia.com/jp/hospital-medical-supplies/medical-equipment/',
'https://dev2fe.tradeindia.com/jp/vessel-sealing-system.html',
'https://dev2fe.tradeindia.com/industry-hubs/',
'https://dev2fe.tradeindia.com/industry-hubs/andhra-pradesh.html',
'https://dev2fe.tradeindia.com/industry-hubs/andhra-pradesh/guntur.html',
'https://dev2fe.tradeindia.com/my-tradeindia/',
'https://dev2fe.tradeindia.com/login/login.html',
'https://dev2fe.tradeindia.com/join_now/verification.html',
'https://dev2fe.tradeindia.com/tradekhata/',
'https://dev2fe.tradeindia.com/about-us/',
'https://dev2fe.tradeindia.com/TradeLeads/',
'https://dev2fe.tradeindia.com/Buyer/',
'https://dev2fe.tradeindia.com/sitemap.html',
'https://dev2fe.tradeindia.com/search.html?search_return_url=%2F&search_form_id=18&keyword=human+hair',
'https://dev2fe.tradeindia.com/tradeshows/',
'https://dev2fe.tradeindia.com/tradeshows/all-categories.html',
'https://dev2fe.tradeindia.com/tradeshows/agriculture/',
'https://dev2fe.tradeindia.com/tradeshows/agriculture/city/mumbai/207486/',
'https://dev2fe.tradeindia.com/tradeshows/agriculture/year-2022/november/',
'https://dev2fe.tradeindia.com/tradeshows/all-cities.html',
'https://dev2fe.tradeindia.com/tradeshows/city/mumbai/207486/',
'https://dev2fe.tradeindia.com/tradeshows/city/mumbai/207486/year-2022/november/',
'https://dev2fe.tradeindia.com/tradeshows/all-countries.html',
'https://dev2fe.tradeindia.com/tradeshows/country/india/',
'https://dev2fe.tradeindia.com/tradeshows/country/india/city/mumbai/207486/',
'https://dev2fe.tradeindia.com/tradeshows/country/india/year-2022/november',
'https://dev2fe.tradeindia.com/tradeshows/112131/auto-expo-components-2023.html',
'https://dev2fe.tradeindia.com/tradeshows/virtual-events/',
'https://dev2fe.tradeindia.com/tradeshows/year-2022/november/',
'https://dev2fe.tradeindia.com/tradeshows/organisers-listing.html',
'https://dev2fe.tradeindia.com/tradeshows/organizer-11377129/media-day-marketing.html',
'https://dev2fe.tradeindia.com/tradeshows/venue-listing.html',
'https://dev2fe.tradeindia.com/tradeshows/venue/biec-bengaluru/6444/',
'https://dev2fe.tradeindia.com/tradeshows/tradeindia-participated-trade-shows.html',
'https://dev2fe.tradeindia.com/tradeshows/fairs/indiawood_2020.html',
'https://dev2fe.tradeindia.com/tradeshows/tradeindia-will-participate-trade-shows.html',
'https://dev2fe.tradeindia.com/tradeshows/109190/pacprocess-food-pex-mumbai-2022.html',
'https://dev2fe.tradeindia.com/tradeshows/advertise.html',
'https://dev2fe.tradeindia.com/tradeshows/trade_show_form.html',
'https://dev2fe.tradeindia.com/blog/',
'https://dev2fe.tradeindia.com/design2017/sourcing/sourcing_requirements.html',
'https://dev2fe.tradeindia.com/TradeLeads/buy/Packaging-Paper/Adhesive-Tapes/',
'https://dev2fe.tradeindia.com/communities/6/3129/Payment-Modes-Finance-Issues/Cash-Against-Delivery-CAD-the-pros-cons.html',
'https://dev2fe.tradeindia.com/survey/109/index.html',
'https://dev2fe.tradeindia.com/ti_forms/rfq/rfq_action.html',
'https://dev2fe.tradeindia.com/tradeindia-news.html',
'https://careers.tradeindia.com/',
'https://dev2fe.tradeindia.com/about-us/contact-us/',
'https://dev2fe.tradeindia.com/about-us/partner-with-us.html',
'https://pay.tradeindia.com/',
'https://dev2fe.tradeindia.com/return-cancellation-policy.html',
'https://dev2fe.tradeindia.com/shipping-and-delivery-policy.html',
'https://dev2fe.tradeindia.com/about-us/product-and-services/product-and-services.html',
'https://dev2fe.domainjerry.com/',
'https://dev2fe.tradeindia.com/newsletters/newsletter_archives.html',
'https://dev2fe.tradeindia.com/about-us/order/credit-report.html',
'https://dev2fe.tradeindia.com/rewards.html',
'https://dev2fe.tradeindia.com/ti-pay/',
'https://dev2fe.tradeindia.com/download-getbizonline.html',
'https://dev2fe.tradeindia.com/ti_logistics/',
'https://dev2fe.tradeindia.com/vcard/',
'https://dev2fe.tradeindia.com/join_now/subscribe_to_trade_alerts.html?type=Sell',
'https://dev2fe.tradeindia.com/join_now/upload_product.html',
'https://dev2fe.tradeindia.com/about-us/terms/terms_01.html',
'https://dev2fe.tradeindia.com/ti-lending/',

]

for url in urls:
    # new_url = f"https://beta-stag.tradeindia.com{url}"
    print(url,':', end="\t")
    try:
        res1 = r.get(url)
        browser.get(url)
    except Exception as e:
        print(e)
    
    print(res1.status_code)
    
    # if url:
    #     #brw = w.Browser()
    #     #brw.go_to(url)
    #     #del brw

    sleep(1)
