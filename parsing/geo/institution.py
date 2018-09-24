"""
InstitutionParser class -- Iterates over 'institution' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

from src.parsing.geo import Parser


class InstitutionParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(InstitutionParser, self).__init__(input_dir)

    def build_records(self):

        for inst in self.institution_table:

            inst_name = self.institution_table[inst]["inst_name"]
            start_year = self.institution_table[inst]["start_year"]

            geo = self.institution_table[inst]["geography"]


