"""
EventParser class -- Iterates over 'event' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""


class EventParser:

    def __init__(self, input_dir='/tmp/table_data/'):

        self.input_dir = input_dir