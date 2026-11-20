"""Geometry invariants used when adapting packaging; no design files are changed."""
import importlib.util
import math
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'layout_geometry', Path(__file__).resolve().parents[1] / 'scripts' / 'layout_geometry.py')
geometry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geometry)


class GeometryTests(unittest.TestCase):
    def test_changed_aspect_preserves_contain_and_cover_proportions(self):
        result = geometry.fit(158.338, 54.529, 182, 51)
        self.assertFalse(result['aspect_ratio_matches'])
        size = result['contain']['artwork_mm']
        self.assertAlmostEqual(size['height'], 51)
        self.assertAlmostEqual(size['width'] / size['height'], 158.338 / 54.529)
        self.assertGreater(result['contain']['total_extra_space_mm']['horizontal'], 33)
        cover = result['cover']['artwork_mm']
        self.assertAlmostEqual(cover['width'], 182)
        self.assertGreater(cover['height'], 51)

    def test_units_can_differ_and_same_ratio_needs_no_extra_space(self):
        result = geometry.fit(2, 1, 100, 50, source_unit='in')
        self.assertTrue(result['aspect_ratio_matches'])
        self.assertAlmostEqual(result['source_mm']['width'], 50.8)
        self.assertAlmostEqual(result['contain']['total_extra_space_mm']['horizontal'], 0)
        self.assertAlmostEqual(result['contain']['total_extra_space_mm']['vertical'], 0)

    def test_pixel_measurements_need_explicit_dpi(self):
        with self.assertRaises(ValueError):
            geometry.fit(2400, 1200, 150, 80, source_unit='px')
        result = geometry.fit(2400, 1200, 150, 80, source_unit='px', source_dpi=300)
        self.assertAlmostEqual(result['source_mm']['width'], 203.2)
        self.assertAlmostEqual(result['contain']['artwork_mm']['height'], 75)

    def test_portrait_target_does_not_silently_rotate(self):
        result = geometry.fit(200, 100, 50, 100)
        self.assertAlmostEqual(result['contain']['artwork_mm']['width'], 50)
        self.assertAlmostEqual(result['contain']['artwork_mm']['height'], 25)
        self.assertAlmostEqual(result['contain']['total_extra_space_mm']['vertical'], 75)

    def test_cylinder_gap_and_overlap_have_opposite_effects(self):
        overlap = geometry.cylinder(5.7, 'cm', overlap=.3, height=5.1)
        gap = geometry.cylinder(57, gap=3)
        self.assertAlmostEqual(overlap['label_length_mm'], math.pi * 57 + 3)
        self.assertAlmostEqual(gap['label_length_mm'], math.pi * 57 - 3)
        self.assertAlmostEqual(overlap['label_height_mm'], 51)
        self.assertIsNone(geometry.cylinder(57)['label_height_mm'])

    def test_invalid_dimensions_and_conflicting_seams_are_rejected(self):
        for invalid in (0, -1, float('nan'), float('inf')):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                geometry.fit(invalid, 20, 30, 40)
        with self.assertRaises(ValueError):
            geometry.cylinder(57, overlap=3, gap=1)
        with self.assertRaises(ValueError):
            geometry.cylinder(57, gap=200)
        with self.assertRaises(ValueError):
            geometry.fit(200, 100, 100, 50, source_unit='px', source_dpi=0)


if __name__ == '__main__':
    unittest.main()
