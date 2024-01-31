from pyflowlauncher import Plugin

from .methods import query, context_menu


def main():
    plugin = Plugin()
    plugin.add_methods(
        [
            query,
            context_menu
        ]
    )
    plugin.run()
