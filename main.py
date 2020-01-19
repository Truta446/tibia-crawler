import argparse
from importlib import import_module

def main():
    module = _importModule()
    parsed = _getFlag()
    return module.Character(parsed.name)

def _importModule():
    return import_module("tibia")

def _getFlag():
    parser = argparse.ArgumentParser(description="Chamado Crawler")
    subparser = parser.add_subparsers()
    crawler = subparser.add_parser("crawler")
    crawler.add_argument("--name", help="Nome do personagem do tibia")
    return parser.parse_args()

if __name__ == "__main__":
    main()