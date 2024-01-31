from typing import Tuple
from pyflowlauncher import ResultResponse, send_results
from pyflowlauncher.utils import score_results

from steam_client.steam import Steam
from steam_client.utils import get_steam_from_registry

from steam_search.results import app_results, context_results


def query(query: str) -> ResultResponse:
    steam = Steam(get_steam_from_registry())
    apps = steam.library.games()
    for user in steam.users:
        apps += user.shortcuts()
    results = app_results(apps)
    return send_results(
        score_results(query, results, match_on_empty_query=True)
    )


def context_menu(context_data: Tuple[str]) -> ResultResponse:
    return send_results(context_results(context_data[0]))