import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    sufficient_sleep_length = catactivities.LENGTH_OF_SATISFYING_NAP + 1
    catactivities.cat_nap(sufficient_sleep_length)
    mock_sleep.assert_called_with(sufficient_sleep_length)


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    insufficient_sleep_length = catactivities.LENGTH_OF_SATISFYING_NAP - 1
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(insufficient_sleep_length)
        assert mock_sleep.called
