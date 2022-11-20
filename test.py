from funix.decorator import funix_export


def triple(x: int):  # this function should NOT be hosted
    return x * 3


@funix_export()
def triple_plus(x: int):  # this function should be hosted at redstone.textea.io/USER_NAME/PROJECT_NAME/FUNCTION_NAME
    return triple(x) + 1


@funix_export()
def file_read() -> str:
    """Simply read a file in this repo and return the first line as a string
    """
    with open('README.md', 'r') as fp:
        head = fp.readline()

    return head
