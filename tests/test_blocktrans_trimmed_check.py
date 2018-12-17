import pytest

from blocktrans_trimmed_check import blocktrans_trimmed_check
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('test_subject', 'expected_return_value'), (
        ('no_blocktrans', 0),
        ('single_line_blocktrans_trimmed', 0),
        ('single_line_blocktrans_not_trimmed', 0),
        ('multi_line_blocktrans_trimmed', 0),
        ('multi_line_blocktrans_not_trimmed', 1),
        ('mixed_with_no_non_trimmed_block', 0),
        ('mixed_with_one_non_trimmed_block', 1),
    ),
)
def test_blocktrans_trimmed(capsys, test_subject, expected_return_value):
    filename = test_subject + '.html'
    return_value = blocktrans_trimmed_check.main([get_resource_path(filename)])
    assert return_value == expected_return_value
    if expected_return_value == 1:
        stdout, _ = capsys.readouterr()
        assert filename in stdout
