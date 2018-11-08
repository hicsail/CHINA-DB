"""
OrgParser class -- Iterates over 'organization' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

from parsing.geo import Parser


class CorpEntityParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(CorpEntityParser, self).__init__(input_dir)

        self.corporate_entity_table = self.load_record("corporate_entity")
        self.corporate_entity_type_table = self.load_record("corporate_entity_type")

    def map_to_coords(self):

        ret = []

        return ''

    def build_records(self):

        records = self.map_to_coords()
