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

    def nationality_dict(self):

        ret = {}

        for rec in self.nationality_table.keys():

            this_record = self.nationality_table[rec]

            try:
                corp_entities = this_record["corporate_entity"]
            except KeyError:
                # missing person field, skip to next entry
                continue

            for c in corp_entities:
                ret[c] = this_record["country_en"]

        return ret

    def map_to_coords(self):

        ret = []

        corp_to_nationality = self.nationality_dict()

        for c in self.corporate_entity_table:

            # initialize dict that stores info about this institution & populate below
            c_rec = \
                {
                    "coords":
                        {
                            "lat": "N/A",
                            "lon": "N/A"
                        },
                    "time":
                        {
                            "start_year": "N/A"
                        },
                    "loc":
                        {
                            "location_type": "N/A",
                            "location_name": "N/A"
                        },
                    "type": "corporate entity",
                    "corp_entity_type": "N/A",
                    "nationality": "N/A",
                    "tradition": "N/A",
                    "denomination": "N/A",
                    "name": "N/A",
                }

            try:
                c_rec["time"]["start_year"] = self.corporate_entity_table[c]["china_start_year"]
            except KeyError:
                continue

            try:
                c_rec["nationality"] = corp_to_nationality[c].lower()
            except KeyError:
                pass







