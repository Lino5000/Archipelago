from ..bases import SVTestBase
from ...mods.mod_data import ModNames
from ...options import Mods, BuildingProgression


class TestGreenhouseSprinklersVanilla(SVTestBase):
    options = {
        BuildingProgression.internal_name: BuildingProgression.option_vanilla,
        Mods.internal_name: ModNames.greenhouse_sprinklers
    }

    def test_no_greenhouse_sprinklers(self):
        with self.subTest(check="no items"):
            item_names = {item.name for item in self.multiworld.get_items()}
            self.assertNotIn("Progressive Hidden Sprinklers", item_names)

        with self.subTest(check="no locations"):
            location_names = {location.name for location in self.multiworld.get_locations()}
            self.assertNotIn("Greenhouse Sprinkler Upgrade Blueprint", location_names)
            self.assertNotIn("Greenhouse Sprinkler Upgrade 2 Blueprint", location_names)
            self.assertNotIn("Greenhouse Sprinkler Upgrade 3 Blueprint", location_names)


class TestGreenhouseSprinklersProgressive(SVTestBase):
    options = {
        BuildingProgression.internal_name: BuildingProgression.option_progressive,
        Mods.internal_name: ModNames.greenhouse_sprinklers
    }

    def test_greenhouse_sprinklers(self):
        with self.subTest(check="has items"):
            item_names = [item.name for item in self.multiworld.get_items()]
            self.assertEqual(item_names.count("Progressive Hidden Sprinklers"), 3)

        with self.subTest(check="has locations"):
            location_names = {location.name for location in self.multiworld.get_locations()}
            self.assertIn("Greenhouse Sprinkler Upgrade Blueprint", location_names)
            self.assertIn("Greenhouse Sprinkler Upgrade 2 Blueprint", location_names)
            self.assertIn("Greenhouse Sprinkler Upgrade 3 Blueprint", location_names)

