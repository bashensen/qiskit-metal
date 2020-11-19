# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

#pylint: disable-msg=unnecessary-pass
#pylint: disable-msg=too-many-public-methods
"""
Qiskit Metal unit tests components functionality.

Created on Wed Apr 22 09:58:35 2020
@author: Jeremy D. Drysdale
"""

import unittest

from qiskit_metal.components.base import qubit
from qiskit_metal.components.basic import circle_caterpillar
from qiskit_metal.components.basic import circle_raster
from qiskit_metal.components.basic import rectangle
from qiskit_metal.components.basic import rectangle_hollow
from qiskit_metal.components.basic import n_gon
from qiskit_metal.components.basic import n_square_spiral
from qiskit_metal.components.connectors.cpw_hanger_t import CPWHangerT
from qiskit_metal.components.connectors import open_to_ground
from qiskit_metal.components.connectors import short_to_ground
from qiskit_metal.components.interconnects.anchored_path import RouteAnchors
from qiskit_metal.components.interconnects import straight_path
from qiskit_metal.components.interconnects import meandered
from qiskit_metal.components.interconnects.mixed_path import RouteMixed
from qiskit_metal.components.interconnects.pathfinder import RoutePathfinder
from qiskit_metal import designs
from qiskit_metal.components.passives.launchpad_wb import LaunchpadWirebond
from qiskit_metal.components.passives.launchpad_wb_coupled import LaunchpadWirebondCoupled
from qiskit_metal.components.passives.cap_three_fingers import CapThreeFingers
from qiskit_metal.components.qubits import transmon_concentric
from qiskit_metal.components.qubits import transmon_cross
from qiskit_metal.components.qubits import transmon_pocket
from qiskit_metal.components.qubits import transmon_pocket_cl
from qiskit_metal.components import _template
from qiskit_metal.tests.assertions import AssertionsMixin

#pylint: disable-msg=line-too-long
from qiskit_metal.components.interconnects.resonator_rectangle_spiral import ResonatorRectangleSpiral


class TestComponentOptions(unittest.TestCase, AssertionsMixin):
    """
    Unit test class
    """

    def setUp(self):
        """
        Setup unit test
        """
        pass

    def tearDown(self):
        """
        Tie any loose ends
        """
        pass

    def test_component_circle_caterpiller_options(self):
        """
        Test that default options of circle_caterpiller in circle_caterpillar.py were not
        accidentally changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _circle_caterpillar = circle_caterpillar.CircleCaterpillar(
            _design, 'my_name')
        _options = _circle_caterpillar.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 11)
        self.assertEqual(_options['segments'], '5')
        self.assertEqual(_options['distance'], '1.2')
        self.assertEqual(_options['radius'], '300um')
        self.assertEqual(_options['pos_x'], '0um')
        self.assertEqual(_options['pos_y'], '0um')
        self.assertEqual(_options['resolution'], '16')
        self.assertEqual(_options['cap_style'], 'round')
        self.assertEqual(_options['subtract'], 'False')
        self.assertEqual(_options['helper'], 'False')
        self.assertEqual(_options['chip'], 'main')
        self.assertEqual(_options['layer'], '1')

    def test_component_circle_raster_options(self):
        """
        Test that default options of circle_raster in circle_raster.py were not accidentally changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _circle_raster = circle_raster.CircleRaster(_design, 'my_name')
        _options = _circle_raster.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 9)
        self.assertEqual(_options['radius'], '300um')
        self.assertEqual(_options['pos_x'], '0um')
        self.assertEqual(_options['pos_y'], '0um')
        self.assertEqual(_options['resolution'], '16')
        self.assertEqual(_options['cap_style'], 'round')
        self.assertEqual(_options['subtract'], 'False')
        self.assertEqual(_options['helper'], 'False')
        self.assertEqual(_options['chip'], 'main')
        self.assertEqual(_options['layer'], '1')

    def test_component_rectangle_options(self):
        """
        Test that default options of rectangle in rectangle.py were not accidentally changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _rectangle = rectangle.Rectangle(_design, 'my_name')
        _options = _rectangle.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 9)
        self.assertEqual(_options['width'], '500um')
        self.assertEqual(_options['height'], '300um')
        self.assertEqual(_options['pos_x'], '0um')
        self.assertEqual(_options['pos_y'], '0um')
        self.assertEqual(_options['rotation'], '0')
        self.assertEqual(_options['subtract'], 'False')
        self.assertEqual(_options['helper'], 'False')
        self.assertEqual(_options['chip'], 'main')
        self.assertEqual(_options['layer'], '1')

    def test_component_rectangle_hollow_options(self):
        """
        Test that default options of rectangle_hollow in rectangle_hollow.py were not accidentally
        changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _rectangle_hollow = rectangle_hollow.RectangleHollow(_design, 'my_name')
        _options = _rectangle_hollow.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 10)
        self.assertEqual(_options['width'], '500um')
        self.assertEqual(_options['height'], '300um')
        self.assertEqual(_options['pos_x'], '0um')
        self.assertEqual(_options['pos_y'], '0um')
        self.assertEqual(_options['rotation'], '0')
        self.assertEqual(_options['subtract'], 'False')
        self.assertEqual(_options['helper'], 'False')
        self.assertEqual(_options['chip'], 'main')
        self.assertEqual(_options['layer'], '1')

        self.assertEqual(len(_options['inner']), 5)
        self.assertEqual(_options['inner']['width'], '250um')
        self.assertEqual(_options['inner']['height'], '100um')
        self.assertEqual(_options['inner']['offset_x'], '40um')
        self.assertEqual(_options['inner']['offset_y'], '-20um')
        self.assertEqual(_options['inner']['rotation'], '15')

    def test_component_n_gon_options(self):
        """
        Test that default options of NGon in n_gon.py were not accidentally changed
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        my_n_gon = n_gon.NGon(design, 'my_name')
        options = my_n_gon.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(options), 9)
        self.assertEqual(options['n'], '3')
        self.assertEqual(options['radius'], '30um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['subtract'], 'False')
        self.assertEqual(options['helper'], 'False')
        self.assertEqual(options['chip'], 'main')
        self.assertEqual(options['layer'], '1')

    def test_component_n_square_spiral_options(self):
        """
        Test that default options of NSquareSpiral in n_square_spiral.py were not accidentally
        changed
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        my_n_square_spiral = n_square_spiral.NSquareSpiral(design, 'my_name')
        options = my_n_square_spiral.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(options), 11)
        self.assertEqual(options['n'], '3')
        self.assertEqual(options['width'], '1um')
        self.assertEqual(options['radius'], '40um')
        self.assertEqual(options['gap'], '4um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['subtract'], 'False')
        self.assertEqual(options['helper'], 'False')
        self.assertEqual(options['chip'], 'main')
        self.assertEqual(options['layer'], '1')

    def test_component_basequbit_options(self):
        """
        Test that default options of BaseQubit in qubit.py were not accidentally changed.
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        my_base_qubit = qubit.BaseQubit(design, 'my_name', make=False)
        options = my_base_qubit.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 4)
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['connection_pads'], {})
        self.assertEqual(options['_default_connection_pads'], {})

    def test_component_open_to_ground_options(self):
        """
        Test that default options of OpenToGround in open_to_ground.py were not accidentally
        changed.
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        my_open_to_ground = open_to_ground.OpenToGround(design, 'my_name')
        options = my_open_to_ground.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 8)
        self.assertEqual(options['width'], '10um')
        self.assertEqual(options['gap'], '6um')
        self.assertEqual(options['termination_gap'], '6um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['chip'], 'main')
        self.assertEqual(options['layer'], '1')

    def test_component_short_to_ground_options(self):
        """
        Test that default options of ShortToGround in short_to_ground.py where not accidentally
        changed.
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        my_short_to_ground = short_to_ground.ShortToGround(design, 'my_name')
        options = my_short_to_ground.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 6)
        self.assertEqual(options['width'], '10um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['chip'], 'main')
        self.assertEqual(options['layer'], '1')

    def test_component_straight_path_options(self):
        """
        Test that default options of RouteStraight in straight_path.py were not
        accidentally changed.
        """
        # Setup expected test results
        my_straight_path = straight_path.RouteStraight
        options = my_straight_path.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 7)
        self.assertEqual(options['fillet'], '0')
        self.assertEqual(options['total_length'], '7mm')
        self.assertEqual(options['layer'], '1')
        self.assertEqual(options['trace_width'], 'cpw_width')
        self.assertEqual(options['chip'], 'main')

        self.assertEqual(len(options['pin_inputs']), 2)
        self.assertEqual(len(options['pin_inputs']['start_pin']), 2)
        self.assertEqual(len(options['pin_inputs']['end_pin']), 2)
        self.assertEqual(options['pin_inputs']['start_pin']['component'], '')
        self.assertEqual(options['pin_inputs']['start_pin']['pin'], '')
        self.assertEqual(options['pin_inputs']['end_pin']['component'], '')
        self.assertEqual(options['pin_inputs']['end_pin']['pin'], '')

        self.assertEqual(len(options['lead']), 4)
        self.assertEqual(options['lead']['start_straight'], '0mm')
        self.assertEqual(options['lead']['end_straight'], '0mm')
        self.assertEqual(options['lead']['start_jogged_extension'], '')
        self.assertEqual(options['lead']['end_jogged_extension'], '')

    def test_component_route_meander_options(self):
        """
        Test that default options of RouteMeander in meandered.py were not
        accidentally changed.
        """
        # Setup expected test results
        my_route_meander = meandered.RouteMeander
        options = my_route_meander.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 3)
        self.assertEqual(options['snap'], 'true')
        self.assertEqual(options['prevent_short_edges'], 'true')

        self.assertEqual(len(options['meander']), 2)
        self.assertEqual(options['meander']['spacing'], '200um')
        self.assertEqual(options['meander']['asymmetry'], '0um')

    def test_component_route_mixed_options(self):
        """
        Test that default options of RouteMixed in mixed_path.py were not accidentally changed.
        """
        # Setup expected test results
        my_route_mixed = RouteMixed
        options = my_route_mixed.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 1)
        self.assertEqual(options['between_anchors'], {})

    def test_component_my_qcomponent_options(self):
        """
        Test that default options in MyQComponent in _template.py were not accidentally changed.
        """
        # Setup expected test results
        my_qcomponent_local = _template.MyQComponent
        options = my_qcomponent_local.default_options

        # Test all elements of the results data against expected ata
        self.assertEqual(len(options), 6)
        self.assertEqual(options['width'], '500um')
        self.assertEqual(options['height'], '300um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['layer'], '1')

    def test_component_transmon_concentric_options(self):
        """Test that default options of transmon_concentric in transmon_concentric.py were not
        accidentally changed
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        my_transmon_concentric = transmon_concentric.TransmonConcentric(
            design, 'my_name')
        options = my_transmon_concentric.default_options

        self.assertEqual(len(options), 19)
        self.assertEqual(options['width'], '1000um')
        self.assertEqual(options['height'], '1000um')
        self.assertEqual(options['layer'], '1')
        self.assertEqual(options['rad_o'], '170um')
        self.assertEqual(options['rad_i'], '115um')
        self.assertEqual(options['gap'], '35um')
        self.assertEqual(options['jj_w'], '10um')
        self.assertEqual(options['res_s'], '100um')
        self.assertEqual(options['res_ext'], '100um')
        self.assertEqual(options['fbl_rad'], '100um')
        self.assertEqual(options['fbl_sp'], '100um')
        self.assertEqual(options['fbl_gap'], '80um')
        self.assertEqual(options['fbl_ext'], '300um')
        self.assertEqual(options['pocket_w'], '1500um')
        self.assertEqual(options['pocket_h'], '1000um')
        self.assertEqual(options['position_x'], '2.0mm')
        self.assertEqual(options['position_y'], '2.0mm')
        self.assertEqual(options['rotation'], '0.0')
        self.assertEqual(options['cpw_width'], '10.0um')

    def test_component_transmon_cross_options(self):
        """
        Test that default options of transmon_cross in transmon_cross.py were not accidentally
        changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _transmon_cross = transmon_cross.TransmonCross(_design, 'my_name')
        _options = _transmon_cross.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 7)
        self.assertEqual(_options['pos_x'], '0um')
        self.assertEqual(_options['pos_y'], '0um')
        self.assertEqual(_options['cross_width'], '20um')
        self.assertEqual(_options['cross_length'], '200um')
        self.assertEqual(_options['cross_gap'], '20um')
        self.assertEqual(_options['orientation'], '0')

        self.assertEqual(len(_options['_default_connection_pads']), 6)
        self.assertEqual(_options['_default_connection_pads']['connector_type'],
                         '0')
        self.assertEqual(_options['_default_connection_pads']['claw_length'],
                         '30um')
        self.assertEqual(_options['_default_connection_pads']['ground_spacing'],
                         '5um')
        self.assertEqual(_options['_default_connection_pads']['claw_width'],
                         '10um')
        self.assertEqual(_options['_default_connection_pads']['claw_gap'],
                         '6um')
        self.assertEqual(
            _options['_default_connection_pads']['connector_location'], '0')

    def test_component_transmon_pocket_options(self):
        """
        Test that default options of transmon_pocket in transmon_pocket.py were not accidentally
        changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _transmon_pocket = transmon_pocket.TransmonPocket(_design, 'my_name')
        _options = _transmon_pocket.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 10)
        self.assertEqual(_options['pos_x'], '0um')
        self.assertEqual(_options['pos_y'], '0um')
        self.assertEqual(_options['pad_gap'], '30um')
        self.assertEqual(_options['inductor_width'], '20um')
        self.assertEqual(_options['pad_width'], '455um')
        self.assertEqual(_options['pad_height'], '90um')
        self.assertEqual(_options['pocket_width'], '650um')
        self.assertEqual(_options['pocket_height'], '650um')
        self.assertEqual(_options['orientation'], '0')

        self.assertEqual(len(_options['_default_connection_pads']), 12)
        self.assertEqual(_options['_default_connection_pads']['pad_gap'],
                         '15um')
        self.assertEqual(_options['_default_connection_pads']['pad_width'],
                         '125um')
        self.assertEqual(_options['_default_connection_pads']['pad_height'],
                         '30um')
        self.assertEqual(_options['_default_connection_pads']['pad_cpw_shift'],
                         '5um')
        self.assertEqual(_options['_default_connection_pads']['pad_cpw_extent'],
                         '25um')
        self.assertEqual(_options['_default_connection_pads']['cpw_width'],
                         'cpw_width')
        self.assertEqual(_options['_default_connection_pads']['cpw_gap'],
                         'cpw_gap')
        self.assertEqual(_options['_default_connection_pads']['cpw_extend'],
                         '100um')
        self.assertEqual(_options['_default_connection_pads']['pocket_extent'],
                         '5um')
        self.assertEqual(_options['_default_connection_pads']['pocket_rise'],
                         '65um')
        self.assertEqual(_options['_default_connection_pads']['loc_W'], '+1')
        self.assertEqual(_options['_default_connection_pads']['loc_H'], '+1')

    def test_component_transmon_pocket_cl_options(self):
        """
        Test that default options of transmon_pocket_cl in transmon_pocket_cl.py were not
        accidentally changed
        """
        # Setup expected test results
        _design = designs.DesignPlanar()
        _transmon_pocket_cl = transmon_pocket_cl.TransmonPocketCL(
            _design, 'my_name')
        _options = _transmon_pocket_cl.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(_options), 7)
        self.assertEqual(_options['make_CL'], True)
        self.assertEqual(_options['cl_gap'], '6um')
        self.assertEqual(_options['cl_width'], '10um')
        self.assertEqual(_options['cl_length'], '20um')
        self.assertEqual(_options['cl_ground_gap'], '6um')
        self.assertEqual(_options['cl_pocket_edge'], '0')
        self.assertEqual(_options['cl_off_center'], '100um')

    def test_component_cpw_hanger_t_options(self):
        """
        Test that default options of CPWHangerT in cpw_hanger_t.py were not accidentally changed.
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        hanger_t = CPWHangerT(design, 'my_name')
        options = hanger_t.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(options), 14)
        self.assertEqual(options['prime_width'], '10um')
        self.assertEqual(options['prime_gap'], '6um')
        self.assertEqual(options['second_width'], '10um')
        self.assertEqual(options['second_gap'], '6um')
        self.assertEqual(options['coupling_space'], '3um')
        self.assertEqual(options['coupling_length'], '100um')
        self.assertEqual(options['fillet'], '25um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['mirror'], False)
        self.assertEqual(options['open_termination'], True)
        self.assertEqual(options['chip'], 'main')
        self.assertEqual(options['layer'], '1')

    def test_component_resonator_rectangle_spiral_options(self):
        """
        Test that default options of ResonatorRectangleSpiral in resonator_rectangle_spiral.py
        were not accidentally changed
        """
        # Setup expected test results
        design = designs.DesignPlanar()
        resonator_rectangle_spiral = ResonatorRectangleSpiral(design, 'my_name')
        options = resonator_rectangle_spiral.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(options), 11)
        self.assertEqual(options['n'], '3')
        self.assertEqual(options['length'], '2000um')
        self.assertEqual(options['line_width'], '1um')
        self.assertEqual(options['height'], '40um')
        self.assertEqual(options['gap'], '4um')
        self.assertEqual(options['coupler_distance'], '10um')
        self.assertEqual(options['pos_x'], '0um')
        self.assertEqual(options['pos_y'], '0um')
        self.assertEqual(options['rotation'], '0')
        self.assertEqual(options['chip'], 'main')
        self.assertEqual(options['layer'], '1')

    def test_component_route_anchors_options(self):
        """
        Test that default options of RouteAnchors in anchored_path.py were not accientally
        changed.
        """
        # Setup expected test results
        route_anchors = RouteAnchors
        options = route_anchors.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(options), 2)
        self.assertEqual(options['anchors'], {})
        self.assertEqual(len(options['advanced']), 1)
        self.assertEqual(options['advanced']['avoid_collision'], 'false')

    def test_component_route_pathfinder_options(self):
        """
        Test that default options of RoutePathfinder in pathfinder.py were not accidentally
        changed.
        """
        # Setup expected test results
        route_pathfinder = RoutePathfinder
        options = route_pathfinder.default_options

        # Test all elements of the result data against expected data
        self.assertEqual(len(options), 2)
        self.assertEqual(options['step_size'], '0.25mm')
        self.assertEqual(len(options['advanced']), 1)
        self.assertEqual(options['advanced']['avoid_collision'], 'true')

    def test_component_launch_v1_options(self):
        """
        Test that default options of LaunchpadWirebond in launchpad_wb.py were not accidentally changed.
        """
        design = designs.DesignPlanar()
        launch_v1 = LaunchpadWirebond(design, 'my_name')
        options = launch_v1.default_options

        self.assertEqual(len(options), 7)
        self.assertEqual(options['layer'], '1')
        self.assertEqual(options['cpw_width'], '10um')
        self.assertEqual(options['cpw_gap'], '6um')
        self.assertEqual(options['leadin_length'], '65um')
        self.assertEqual(options['pos_x'], '100um')
        self.assertEqual(options['pos_y'], '100um')
        self.assertEqual(options['orientation'], '0')

    def test_component_launch_v2_options(self):
        """
        Test that default options of LaunchpadWirebondCoupled in launchpad_wb_coupled.py were not accidentally changed.
        """
        design = designs.DesignPlanar()
        launch_v2 = LaunchpadWirebondCoupled(design, 'my_name')
        options = launch_v2.default_options

        self.assertEqual(len(options), 7)
        self.assertEqual(options['layer'], '1')
        self.assertEqual(options['cpw_width'], '10um')
        self.assertEqual(options['cpw_gap'], '6um')
        self.assertEqual(options['leadin_length'], '65um')
        self.assertEqual(options['pos_x'], '100um')
        self.assertEqual(options['pos_y'], '100um')
        self.assertEqual(options['orientation'], '0')

    def test_component_cap_three_fingers(self):
        """
        Test that default options of CapThreeFingers were not accidentally changed.
        """
        design = designs.DesignPlanar()
        cap_three_fingers = CapThreeFingers(design, 'my_name')
        options = cap_three_fingers.default_options

        self.assertEqual(len(options), 8)
        self.assertEqual(options['layer'], '1')
        self.assertEqual(options['trace_width'], '10um')
        self.assertEqual(options['finger_length'], '65um')
        self.assertEqual(options['pocket_buffer_width_x'], '10um')
        self.assertEqual(options['pocket_buffer_width_y'], '30um')
        self.assertEqual(options['pos_x'], '100um')
        self.assertEqual(options['pos_y'], '100um')
        self.assertEqual(options['orientation'], '0')


if __name__ == '__main__':
    unittest.main(verbosity=2)