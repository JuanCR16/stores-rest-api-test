from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'test123')

        self.assertEqual(user.username, 'test',
                         'The name of the user after creation does not equal the constructor argument.')
        self.assertEqual(user.password, 'test123',
                         'The password of the user after creation does not equal the constructor argument.')
