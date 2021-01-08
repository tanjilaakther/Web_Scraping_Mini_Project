from flask import Flask, render_template, request
import requests
import json

#my_list = ["-compact-ns&", "circuit-breaker-compact-nsxm", "circuit-breaker-compact-nsx"]
my_list = ["-compact-ns&", 
    "-compact-nsxm&", 
    "-compact-nsx&", 
    "circuit-breaker-compact-nsx",
    "/switch-disconnector-fuse%2C-fupact-", 
    "-masterpact-switch-disconnectors&",
    "-compact-nsx-na&",
    "-compact--ins-inv&",
    "-compact-nsxm-na&",
    "-compact-ns-na&",
    "-tesys-island&",
    "-tesys-t&",
    "-tesys-u&",
    "-tesys-gv2",
    "-tesys-gv3",
    "-tesys-gv4",
    "-tesys-gv5",
    "-tesys-gv6",
    "-tesys-control-relays&",
    "-tesys-d&",
    "-tesys-f&",
    "-tesys-k&",
    "-tesys-b&",
    "miniature-circuit-breaker-sn201-",
    "miniature-circuit-breaker-s200mt-",
    "miniature-circuit-breaker-s200-",
    "miniature-circuit-breaker-su200m-"
    ]

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def index_ns():
    user_input_url = request.args.get('enter_url')
    if user_input_url:
        xq = my_function(user_input_url)
        if xq == '-compact-ns&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mccbs_comPact_NS"
            }
        elif xq == '-compact-nsxm&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mccbs_comPact_NSXM"
            }
        elif xq == '-compact-nsx&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mccbs_comPact_NSX"
            }
        elif xq == 'circuit-breaker-compact-nsx':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mccbs_comPact_NSX_dc"
            }
        elif xq == '/switch-disconnector-fuse%2C-fupact-':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_sdf_FuPact"
            }
        elif xq == '-masterpact-switch-disconnectors&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_sdf_masterPact_sd"
            }
        elif xq == '-compact-nsx-na&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_sdf_comPact_NSX_NA"
            }
        elif xq == '-compact--ins-inv&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_sdf_comPact_insinv"
            }
        elif xq == '-compact-nsxm-na&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_sdf_comPact_NSXM_NA"
            }
        elif xq == '-compact-ns-na&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_sdf_comPact_NS_NA"
            }
        elif xq == '-tesys-island&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_dms_TeSys_island"
            }
        elif xq == '-tesys-t&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_dms_Tesys_T"
            }
        elif xq == '-tesys-u&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_dms_Tesys_U"
            }
        elif xq == '-tesys-gv2':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mpcb_TeSys_GV2"
            }
        elif xq == '-tesys-gv3':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mpcb_TeSys_GV3"
            }
        elif xq == '-tesys-gv4':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mpcb_TeSys_GV4"
            }
        elif (xq == '-tesys-gv5') or (xq == '-tesys-gv6'):
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_mpcb_TeSys_GV5_GV6"
            }
        elif xq == '-tesys-control-relays&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_indsC_TeSys_ControlRelays"
            }
        elif xq == '-tesys-d&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_indsC_TeSys_D"
            }
        elif xq == '-tesys-f&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_indsC_TeSys_F"
            }
        elif xq == '-tesys-k&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_indsC_TeSys_K"
            }
        elif xq == '-tesys-b&':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "se_indsC_TeSys_B"
            }
        elif xq == 'miniature-circuit-breaker-sn201-':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "abb_mcb_sn201-range"
            }
        elif xq == 'miniature-circuit-breaker-s200mt-':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "abb_mcb_s200-mt-range"
            }
        elif xq == 'miniature-circuit-breaker-s200-':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "abb_mcb_s200-range"
            }
        elif xq == 'miniature-circuit-breaker-su200m-':
            req_obj = {
                "request": {
                    "url": user_input_url,
                    "callback": "parse",
                    "meta": {
                        "url": user_input_url
                    },
                },
                "spider_name": "abb_mcb_su200-range"
            }
        resp = requests.post(
            url='http://127.0.0.1:9080/crawl.json', data=json.dumps(req_obj)
        ).json()

        items = resp.get('items')
        return render_template('index.html', product_char=items)
    else:
        return render_template('index.html', product_char={})

     
def my_function(txt1):
    x = []
    txt2 = txt1
    for i in my_list:
        x = txt2.rpartition(i)
        if i in x:
            break
        else:
            continue
     
    for item in my_list:
        if item in x:
            p = item 
    return p
     
     
if __name__ == '__main__':
    app.run(debug=True)