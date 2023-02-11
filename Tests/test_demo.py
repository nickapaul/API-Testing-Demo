import unittest
import Helpers.pet_store_helpers as pet_help

class ApiTestDemo(unittest.TestCase):
  def test_GIVEN_pet_is_created_WHEN_id_is_used_to_fetch_obj_THEN_pet_is_returned(self):  
    # Arrange
    expected_dog_name= 'Brady'
    pet_id = pet_help.create_pet_and_return_pet_id(expected_dog_name)

    # Act
    pet = pet_help.get_pet_via_pet_id(pet_id)

    # Assert
    self.assertEqual(expected_dog_name, "hello")