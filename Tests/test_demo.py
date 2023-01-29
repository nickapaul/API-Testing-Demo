import unittest
import json
import Helpers.pet_store_helpers as pet_help

class ApiTestDemo(unittest.TestCase):

  def test_GIVEN_pet_is_created_THEN_pet_can_be_returned(self):  
    expected_dog_name= 'Brady'
    pet_id = pet_help.create_pet_and_return_pet_id()

    pet = pet_help.get_pet_via_pet_id(pet_id)

    self.assertEqual(expected_dog_name, pet['name'])



  
   