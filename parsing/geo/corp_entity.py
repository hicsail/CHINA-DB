"""
CorpEntity class -- Iterates over 'corporate_entity' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

from parsing.geo import Parser


class CorpEntityParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(CorpEntityParser, self).__init__(input_dir)

        self.corporate_entity_table = self.load_record("corporate_entity")

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

    def type_dict(self):

        ret = {}

        for rec in self.corporate_entity_type_table.keys():

            this_record = self.corporate_entity_type_table[rec]

            try:
                corp_type = this_record["type_en"]
            except KeyError:
                continue

            ret[rec] = corp_type

        return ret

    def map_to_coords(self):

        ret = []

        corp_to_nationality = self.nationality_dict()
        corp_to_type = self.type_dict()

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
                    "corp_entity_type": [],
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

            try:
                corp_type_rec = c["corporate_entity_type"]
                for t in corp_type_rec:
                    c_rec["corp_entity_type"].append(corp_to_type[t])
            except KeyError:
                pass

        return ret







