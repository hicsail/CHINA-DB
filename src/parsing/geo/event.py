"""
EventParser class -- Iterates over 'event' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

from src.parsing.geo import Parser


class EventParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(EventParser, self).__init__(input_dir)