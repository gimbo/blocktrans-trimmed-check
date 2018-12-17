from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

import argparse
import io


def main(argv=None):
    args = parse_args(argv)
    results = {
        check_file(filename) for filename in args.filenames
    }
    return 0 if results == {False} else 1


def check_file(path):
    result = has_dirty_blocktrans(path)
    if result:
        print(path)
    return result


def has_dirty_blocktrans(path):
    """
    Quick and dirty check for a multi-line blocktrans lacking a trimmed
    directive.

    A more solid approach would involve the Django HTML template parser, e.g.
    see https://stackoverflow.com/a/24583004/392743
    """
    with io.open(path, encoding='utf-8') as infile:
        for line in infile:
            if '{% blocktrans' in line and '{% endblocktrans' not in line:
                if 'trimmed' not in line:
                    return True
    return False


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    return parser.parse_args(argv)


if __name__ == '__main__':
    exit(main())
