from unittest import TestCase

from tky2jgd import lat_lon2mesh_code, tonari_mesh_code, MeshCode, load_parameter, bilinear


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

        edge_case_1 = {
            'lat_lng': [36.0833333333333, 139.0833333333333],
            'mesh_code': '5439-10-06',
        }
        mesh_code = lat_lon2mesh_code(*edge_case_1['lat_lng'])
        assert mesh_code.mesh_code_str == edge_case_1['mesh_code']

        edge_case_2 = {
            'lat_lng': [36.0833333333333, 138.45],
            'mesh_code': '5438-13-06',
        }
        mesh_code = lat_lon2mesh_code(*edge_case_2['lat_lng'])
        assert mesh_code.mesh_code_str == edge_case_2['mesh_code']

    def test_tonari_mesh_code(self):
        # You can use this website to find the adjacent mesh codes:
        # 地域メッシュ - MULTISOUP - https://maps.multisoup.co.jp/exsample/mesh/mesh_search.html
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

    def test_bilinear(self):
        load_parameter('tky2jgd/data/TKY2JGD.par')
        # Original First-class Triangulation Point at the Japan GSI Tsukuba
        lat, lon = 36.100578889, 140.091149167
        dB, dL = bilinear(lat, lon)
        lat += dB / 3600
        lon += dL / 3600
        assert (lat, lon) == (36.10377077065109, 140.08787082896106)


class TestMeshCode(TestCase):
    def setUp(self) -> None:
        self.mesh_codes = [
            MeshCode(1234, 56, 78),
            MeshCode(1, 2, 3),
            MeshCode(1234, 56, 78),
        ]

    def test_mesh_code123(self):
        assert self.mesh_codes[0].mesh_code123 == 12345678
        assert self.mesh_codes[1].mesh_code123 == 10203
        assert self.mesh_codes[2].mesh_code123 == 12345678

    def test_mesh_code_str(self):
        assert self.mesh_codes[0].mesh_code_str == '1234-56-78'
        assert self.mesh_codes[1].mesh_code_str == '0001-02-03'
        assert self.mesh_codes[2].mesh_code_str == '1234-56-78'
