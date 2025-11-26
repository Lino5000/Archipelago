from worlds.stardew_valley.data.game_item import Requirement
from ..game_content import ContentPack
from ..mod_registry import register_mod_content_pack
from ...data.building import Building
from ...data.shop import ShopSource
from ...data.requirement import RegionRequirement, SpecificFriendRequirement, BuildingRequirement
from ...mods.mod_data import ModNames
from ...strings.artisan_good_names import ArtisanGood
from ...strings.building_names import ModBuilding
from ...strings.craftable_names import Sprinkler
from ...strings.region_names import Region
from ...strings.villager_names import NPC

# Gold, sprinkler type, sprinkler count, battery count, wizard heart count
SingleCost = tuple[int, str, int, int, int]
UPGRADE_COSTS_MEDIUM: tuple[SingleCost, ...] = (
    (20_000, Sprinkler.quality, 5, 1, 2),
    (30_000, Sprinkler.iridium, 5, 5, 5),
    (50_000, Sprinkler.iridium, 20, 10, 10),
)

def generate_buildings(costs: tuple[SingleCost, ...]) -> tuple[Building, ...]:
    out: list[Building] = []
    for i, (gold, sprinkler_type, sprinklers, batteries, hearts) in enumerate(costs):
        has_prev_building: Requirement
        if i == 0:
            # First upgrade needs the Greenhouse to have been repaired
            has_prev_building = RegionRequirement(Region.greenhouse)
        else:
            # Further upgrades need the previous upgrade to have been built
            has_prev_building = BuildingRequirement(ModBuilding.greenhouse_sprinklers[i-1])

        building = Building(
            ModBuilding.greenhouse_sprinklers[i],
            sources=(
                ShopSource(
                    shop_region=Region.carpenter,
                    price=gold,
                    items_price=((sprinklers, sprinkler_type), (batteries, ArtisanGood.battery_pack)),
                    other_requirements=(
                        SpecificFriendRequirement(NPC.wizard, hearts),
                        has_prev_building,
                    ),
                ),
            ),
        )
        out.append(building)
    return tuple(out)


register_mod_content_pack(ContentPack(
    ModNames.greenhouse_sprinklers,
    farm_buildings=generate_buildings(UPGRADE_COSTS_MEDIUM),
))
