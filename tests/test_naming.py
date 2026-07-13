import unittest
from tools.validate_naming import valid_asset_id
class NamingTests(unittest.TestCase):
    def test_valid(self): self.assertTrue(valid_asset_id('bh_villa_wall_window_01'))
    def test_rejects_hyphen(self): self.assertFalse(valid_asset_id('bh-villa-wall'))
    def test_rejects_uppercase(self): self.assertFalse(valid_asset_id('BH_VILLA'))
if __name__=='__main__': unittest.main()
