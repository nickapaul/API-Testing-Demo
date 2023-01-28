import unittest
import json
import Helpers.mlb_api.mlb_api_helpers as mlb_help



class ApiTestDemo(unittest.TestCase):

  def test_GIVEN_mlb_player_id_THEN_player_info_is_returned_and_Confirmed(self):  
    expected_last_name= 'Cespedes'
    player_raw = mlb_help.get_player_info('493316')
  
    player = json.loads(player_raw.content)
    player_last_name = player['player_info']['queryResults']['row']['name_last']
    self.assertEqual(expected_last_name, player_last_name)