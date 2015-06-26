import unittest

from worldengine.drawing_functions import *
from worldengine.world import *
from tests.draw_test import TestBase, PixelCollector


class TestDrawingFunctions(TestBase):

    def setUp(self):
        super(TestDrawingFunctions, self).setUp()
        self.w = World.open_protobuf("%s/seed_28070.world" % self.tests_data_dir)

    def test_draw_ancient_map_factor1(self):
        w_large = World.from_pickle_file("%s/seed_48956.world" % self.tests_data_dir)
        target = PixelCollector(w_large.width, w_large.height)
        draw_ancientmap(w_large, target, resize_factor=1)
        self._assert_img_equal("ancientmap_48956", target)

    def test_draw_ancient_map_factor3(self):
        target = PixelCollector(self.w.width * 3, self.w.height * 3)
        draw_ancientmap(self.w, target, resize_factor=3)
        self._assert_img_equal("ancientmap_28070_factor3", target)

    def test_gradient(self):
        self._assert_are_colors_equal((10, 20, 40),
                                      gradient(0.0, 0.0, 1.0, (10, 20, 40), (0, 128, 240)))
        self._assert_are_colors_equal((0, 128, 240),
                                      gradient(1.0, 0.0, 1.0, (10, 20, 40), (0, 128, 240)))
        self._assert_are_colors_equal((5, 74, 140),
                                      gradient(0.5, 0.0, 1.0, (10, 20, 40), (0, 128, 240)))

    def test_draw_rivers_on_image(self):
        target = PixelCollector(self.w.width * 2, self.w.height * 2)
        draw_rivers_on_image(self.w, target, factor=2)
        self._assert_img_equal("rivers_28070_factor2", target)

if __name__ == '__main__':
    unittest.main()
