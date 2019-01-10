import os

from parsing.geo.corp_entity import CorpEntityParser
from parsing.geo.institution import InstitutionParser
from parsing.geo.person import PersonParser


class MergeParser:
    """
    Spawn each parser type and merge all records into a single GeoJson file.
    """

    def __init__(self, input_dir='/tmp/table_data/'):

        self.input_dir = input_dir
        self.template_dir = "{}/templates/".format(os.path.dirname(os.path.realpath(__file__)))

        self.corp_parser = CorpEntityParser()
        self.inst_parser = InstitutionParser()
        self.person_parser = PersonParser()

    def merge_all(self):

        self.corp_parser.build_records()
        self.inst_parser.build_records()
        self.person_parser.build_records()

        all_records = self.corp_parser.records + self.inst_parser.records + self.person_parser.records

        ret = {}
        all_coords = set()
        id_num = 0

        for r in all_records:

            coords = "{0} {1}".format(r["coords"]["lon"], r["coords"]["lat"])

            if coords in all_coords:
                # merge this record with an existing Point

                '''
                del r["coords"]

                ret[coords]["properties"]["objects"].append(r)
                '''
            else:

                all_coords.add(coords)

                new_coords = [r["coords"]["lon"], r["coords"]["lat"]]
                del r["coords"]
