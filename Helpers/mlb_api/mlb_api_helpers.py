import Helpers.common.request_helpers as req_help

def get_player_info(player_id):
    url = f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{player_id}'"
    payload={}
    headers = {
        'Cookie': 'cf_use_ob=0'
    }
    return req_help.send_request("Get", url, payload, headers)
    