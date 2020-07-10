from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.sites.draftkings.showdown.importer import DraftKingsShowdownGolfModeCSVImporter



POSITIONS = [
    LineupPosition('G', ('G',)),
    LineupPosition('G', ('G',)),
    LineupPosition('G', ('G',)),
    LineupPosition('G', ('G',)),
    LineupPosition('G', ('G',)),
    LineupPosition('G', ('G',)),
]

class DraftKingsShowdownGolfModeSettings(BaseSettings):
    site = Site.DRAFTKINGS_SHOWDOWN_GOLF
    budget = 50000
    max_from_one_team = 6
    csv_importer = DraftKingsShowdownGolfModeCSVImporter
    positions = [
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
    ]


@SitesRegistry.register_settings
class DraftKingsShowdownGolfSettings(DraftKingsShowdownGolfModeSettings):
    sport = Sport.GOLF
    positions = POSITIONS[:]
