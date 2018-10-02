"""
OrgParser class -- Iterates over 'organization' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

from parsing.geo import Parser


class OrgParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(OrgParser, self).__init__(input_dir)