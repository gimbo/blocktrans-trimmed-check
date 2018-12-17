[![Build Status](https://travis-ci.org/gimbo/blocktrans-trimmed-check.svg?branch=master)](https://travis-ci.org/gimbo/blocktrans-trimmed-check)
[![Coverage Status](https://coveralls.io/repos/github/gimbo/blocktrans-trimmed-check/badge.svg?branch=master)](https://coveralls.io/github/gimbo/blocktrans-trimmed-check?branch=master)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/5vtv8s91y2f35cs4?svg=true)](https://ci.appveyor.com/project/gimbo/blocktrans-trimmed-check)


# blocktrans-trimmed-check

This is a pre-commit hook, written for the [pre-commit.com
framework](https://pre-commit.com/), which looks for Django template
files containing a multi-line
[`blocktrans`](https://docs.djangoproject.com/en/2.1/topics/i18n/translation/#blocktrans-template-tag)
block but no `trimmed` directive.

## Configuration

Example `.pre-commit-config.yaml` entry:

      - repo: https://github.com/gimbo/blocktrans-trimmed-check.git
        rev: master
        hooks:
          - id: blocktrans-trimmed-check
