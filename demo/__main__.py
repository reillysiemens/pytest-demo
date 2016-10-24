from demo.utils import InvalidHovercraftContents, Hovercraft, uppercase


def main():
    print(uppercase('Hello, World!'))

    try:
        hovercraft = Hovercraft()
        hovercraft.contents = 'dogs'
    except InvalidHovercraftContents as err:
        print(err)

    try:
        hovercraft = Hovercraft()
        hovercraft.contents = 'eels'
    except InvalidHovercraftContents as err:
        print(err)
