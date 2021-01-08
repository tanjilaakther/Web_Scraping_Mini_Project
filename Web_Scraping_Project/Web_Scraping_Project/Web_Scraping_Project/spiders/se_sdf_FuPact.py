import scrapy
from scrapy_splash import SplashRequest


class SeSdfFupactSpider(scrapy.Spider):
    name = 'se_sdf_FuPact'
    #allowed_domains = ['www.se.com']
    #start_urls = ['http://www.se.com/']

    script = '''
        function main(splash, args)
            headers = {
                ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                ['cookie'] = 'PESV2_Cart_en_US=0; PESV2_Cart_B2C_en_US=0; DYN_USER_ID=1721743395; DYN_USER_CONFIRM=96923667c4ff7ad4baf5a3af7b22fbad; AWSELB=A9D3D3CF18851E073A4EDC85449131241AFDCA2F6CE38017D8293A5F9014C3649B16D88FBE085CE0A083E1EBECAF0ACF7663572C71D8C6D6522F59EB62D739072263E9C48189963BF6D4D78B08E93DC68C564277B7; tCdebugLib=1; TCPID=120831957258615485129; _ga=GA1.3.673050826.1597856245; liveagent_oref=https://www.sahkonumerot.fi/3606062; liveagent_ptid=70eba87d-55d8-4d9e-84d8-e5ef8278441f; TC_PRIVACY=0@004@1%2C2%2C3%2C4@@1597856263815@; TC_PRIVACY_CENTER=1%2C2%2C3%2C4; _fbp=fb.1.1597856264498.1642687967; kampyle_userid=aef0-3db0-ea72-5c20-9160-a3b8-3f07-9a44; mdigital_alternative_uuid=cc83-67db-2f87-2e9b-a85c-b319-285d-1da8; cd_user_id=17407a83d552a2-02310d425f3cc4-3323767-144000-17407a83d56279; country_selected=true; optimizelyEndUserId=oeu1597856695329r0.21556259016639245; _gcl_au=1.1.573328939.1597856699; liveagent_vc=3; _ga=GA1.2.673050826.1597856245; SECOUNTRYCODE=wwen; ABCD_banner_test=c; se_user_type=anonymous; LAST_INVITATION_VIEW=1601277086978; DECLINED_DATE=1601277288319; _cs_c=0; kampyleUserSession=1601374910333; kampyleUserSessionsCount=10; kampyleUserPercentile=67.84571899233498; PESV2SESSID=0GANkWSmkTP3zjpowSGF2q44.prd_PESstore11-1; AKA_A2=A; ak_bmsc=AF369C5B347DF7B9FCF51276CDC06CCF50EFED2EF5530000B086755FC6F5555F~pliSJKQPHV/uRud9FHygI82YovWwp7Rnc2nDm1IRNJMs1AO6hR5u1+dnOmqACw2cEp0Lv/Jvv8EVPx3MjWhjj9JP7LWpdqMbEKY7ydN1eq9CDxU9VR2b+wa37V3vwcW6p0rhzpWeXmqOfUw3gFwFynqvRhe8aHj4T5BUi2bV1gNHFf16RKyOUnlM1YH6um4V3po3ylNTL2d4pwjWbG6DJ5ZQ1JtJexqX6PQsAFEn+0IXI=; _gid=GA1.3.1409707920.1601537707; _mkto_trk=id:178-GYD-668&token:_mch-se.com-1597856264328-55581; _gat_statTracker=1; RT="z=1&dm=se.com&si=ydxqw3wyyvp&ss=kf6sxkbi&sl=0&tt=0"; _cs_id=a27f7a7b-54c1-a6fb-c1b0-7172fbe48546.1597856264.36.1601538662.1601537696.1.1632020264610.Lax.0; _cs_s=21.1; bm_sv=1113E3C04425DA667CC53F02F9F13698~SnJv7NegtmOHfEFy+kzSgeK4cwD8FEs/acVqsj2Ud6W7BThd6qhFCof7qceX0VLxVpHuEsmbFcv5zMgjot158N0sgsFw6gCLFVJ1lR0SeUQYnut9vGWYOkjYuLu0w1LK93TqrSdy5JsDiJ52w/Y1/c/YzgAKWfE7qy4uj65lwl4=; kampyleSessionPageCounter=22; kampylePageLoadedTimestamp=1601538668651'
            }
            splash:set_custom_headers(headers)
            splash.private_mode_enabled = false
            --splash.images_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(1))
            splash:set_viewport_full()
            assert(splash:wait(1))
            return(splash.html())
        end
    
    '''

    def modify_realtime_request(self, request):
        user_url_input = request.meta["url"]
        return SplashRequest(user_url_input, self.parse,
                             args={
                                 'lua_source': self.script
                             },
                             endpoint='execute'
                             )

    def parse(self, response):
        # print(response.body)

        characteristics = response.xpath(
            "//div[@class='drawer']/ul/li/section/table[3]/tbody")


        for n in characteristics:
            product_name = response.xpath("normalize-space(//h2[@class='pdp-product-info__description']/text())").get()
            product_height = n.xpath("normalize-space(.//tr[9]/td/div/text())").get()
            product_width = n.xpath("normalize-space(.//tr[8]/td/div/text())").get()
            product_depth = n.xpath("normalize-space(.//tr[10]/td/div/text())").get()
            product_weight = n.xpath("normalize-space(.//tr[11]/td/div/text())").get()
            yield {
                'productName': product_name,
                'productHeight': product_height,
                'productWidth': product_width,
                'productDepth': product_depth,
                'productWeight': product_weight
            }
