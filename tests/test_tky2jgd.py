from unittest import TestCase

from tky2jgd import lat_lon2mesh_code


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
