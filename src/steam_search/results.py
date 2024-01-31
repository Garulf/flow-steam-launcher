from typing import Generator, Iterable

from pyflowlauncher import Result
from pyflowlauncher.api import open_uri

from steam_client.commands import run_game_id, store, uninstall
from steam_client.game import App


def app_result(app: App) -> Result:
    uri = run_game_id(app.appid)
    return Result(
        Title=str(app.name),
        SubTitle=uri,
        IcoPath=str(app.icon),
        JsonRPCAction=open_uri(uri),
        ContextData=[str(app.appid)]
    )


def app_results(apps: Iterable[App]) -> Generator[Result, None, None]:
    for app in apps:
        yield app_result(app)


def context_results(appid: str) -> Generator[Result, None, None]:
    yield Result(
        Title="Open Store Page",
        SubTitle="Open the Steam store page for this app",
        IcoPath="icon.png",
        JsonRPCAction=open_uri(store(appid))
    )
    yield Result(
        Title="Uninstall",
        SubTitle="Uninstall this app",
        IcoPath="icon.png",
        JsonRPCAction=open_uri(uninstall(appid))
    )