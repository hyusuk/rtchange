import pytest


class TestSDNML(object):
    @pytest.fixture
    def sdnml(self):
        from rtchange.coding import SDNML
        return SDNML(discounting_param=0.1, order=3)

    def test_length(self, sdnml):
        l = list(sdnml.length([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))
        # First order+1 elements should be 0
        assert l[0:4] == [0, 0, 0, 0]
        assert l[0:5] != [0, 0, 0, 0, 0]
