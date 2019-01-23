"""
CorpEntity class -- Iterates over 'corporate_entity' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

import copy

from parsing.geo import Parser


class CorpEntityParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(CorpEntityParser, self).__init__(input_dir)

        self.parse_type = "CORP_ENTITY"

        self.org_org_rel_type_table = self.load_record("organization_organization_rel_type")

    def nationality_dict(self):
        """
        Map Nationality ID's to strings.
        """

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
        """
        Map Corporate Entity type ID's to strings.
        """

        ret = {}

        for rec in self.corporate_entity_type_table.keys():

            this_record = self.corporate_entity_type_table[rec]

            try:
                corp_type = this_record["type_en"]
            except KeyError:
                continue

            ret[rec] = corp_type

        return ret

    def fetch_rel_type(self, rel_type_id):
        """
        Get relation type between two organizations.
        """

        try:
            rel_type_rec = self.org_org_rel_type_table[rel_type_id]
            return rel_type_rec["org_org_rel_type_en"]
        except KeyError:
            return ''

    def corp_relation_mapping(self, corp_rec):

        ret = \
            {
                "religious_family": "N/A",
                "association": "N/A"
            }

        try:
            ret["religious_family"] = self._religious_family_mapping(corp_rec["religious_family"][0])
        except KeyError:
            pass

        try:
            ret["association"] = self._corp_type_mapping(corp_rec["corporate_entity_type"][0])
        except KeyError:
            pass

        return ret

    def add_geo(self, org_org_ids, rec):
        """
        Since Corporate Entities have no geographical data, grab
        all institutions connected to this Corporate Entity and
        create a unique GeoJson record for each Institution.
        """

        ret = []

        for ooid in org_org_ids:

            try:
                inst_id = self.org_org_table[ooid]["inst_id_1"][0]
                rec["child_inst_name"] = self.institution_table[inst_id]["inst_name"].lower()
                geo = self.institution_table[inst_id]["geography"]

                for g in geo:

                    rec_copy = copy.deepcopy(rec)
                    geo_rec = self.fetch_geo(g)

                    if geo_rec is not None:

                        rec_copy["coords"]["lat"] = geo_rec["coords"]["lat"]
                        rec_copy["coords"]["lon"] = geo_rec["coords"]["lon"]
                        rec_copy["loc"]["location_type"] = geo_rec["loc"]["location_type"]
                        rec_copy["loc"]["location_name"] = geo_rec["loc"]["location_name"]
                        ret.append(rec_copy)
            except KeyError:
                continue

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
                    "type": "corporate_entity",
                    "nationality": "N/A",
                    "corp_relations":
                        {
                            "religious_family": "N/A",
                            "association": "N/A"
                        },
                    "name": "N/A",
                    "child_inst_name": "N/A"
                }

            try:
                c_rec["time"]["start_year"] = self.corporate_entity_table[c]["china_start_year"]
            except KeyError:
                continue

            try:
                c_rec["nationality"] = corp_to_nationality[c].lower()
            except KeyError:
                pass

            c_rec["corp_relations"] = self.corp_relation_mapping(self.corporate_entity_table[c])

            try:
                org_org_ids = self.corporate_entity_table[c]["organization_organization 2"]
                recs = self.add_geo(org_org_ids, c_rec)
                if len(recs) > 0:
                    ret.extend(recs)
            except KeyError:
                continue

        return ret
