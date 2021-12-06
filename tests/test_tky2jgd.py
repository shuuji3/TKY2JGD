from unittest import TestCase

from tky2jgd import lat_lon2mesh_code, tonari_mesh_code, MeshCode


class Test(TestCase):
    def test_lat_lon2mesh_code(self):
        tokyo_tower = {
            'lat_lng': [35.65867376197596, 139.74544620945704],
            'mesh_code': '5339-35-99'
        }
        mesh_code = lat_lon2mesh_code(*tokyo_tower['lat_lng'])
        assert mesh_code.mesh_code_str == tokyo_tower['mesh_code']

        south_east_of_tokyo_tower = {
            'lat_lng': [35.65820117583567, 139.75010145376297],
            'mesh_code': '5339-36-80',
        }
        mesh_code = lat_lon2mesh_code(*south_east_of_tokyo_tower['lat_lng'])
        assert mesh_code.mesh_code_str == south_east_of_tokyo_tower['mesh_code']

    def test_tonari_mesh_code(self):
        tokyo_tower_mesh = MeshCode(5339, 35, 99)
        expected_mash = {
            'east': MeshCode(5339, 36, 90),
            'north': MeshCode(5339, 45, 9),
            'north_east': MeshCode(5339, 46, 0),
        }

        west, north, north_west = tonari_mesh_code(tokyo_tower_mesh)
        assert west.mesh_code_str == expected_mash['east'].mesh_code_str
        assert north.mesh_code_str == expected_mash['north'].mesh_code_str
        assert north_west.mesh_code_str == expected_mash['north_east'].mesh_code_str
