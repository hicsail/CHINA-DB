"""
PersonParser class -- Iterates over 'person' table and produces a separate GeoJson formatted
JSON object for each organization/institution with geographical coordinates that they were
involved with, along with other relevant information.
"""


class PersonParser:

    def __init__(self, input_dir='/tmp/table_data/'):

        self.input_dir = input_dir

