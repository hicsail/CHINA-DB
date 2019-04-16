import copy

from parsing.geo import Parser


class InstitutionParser(Parser):
    """
    Iterates over 'institution' table and produces a separate GeoJson
    formatted JSON object for each with geographical coordinates, along
    with other relevant information.
    """

    def __init__(self, input_dir='/tmp/table_data/'):

        super(InstitutionParser, self).__init__(input_dir)

        self.parse_type = "INST"

        self.institution_type_table = self.load_record("institution_type")

    def type_dict(self):
        """
        Map Institution Type ID's to strings.
        """

        ret = {}

        for rec in self.institution_type_table.keys():

            this_record = self.institution_type_table[rec]

            try:
                institutions = this_record["institution"]
            except KeyError:
                # no institutions for this type, skip to next entry
                continue

            for i in institutions:
                ret[i] = this_record["type_en"]

        return ret

    def nationality_dict(self):
        """
        Map Nationality ID's to strings.
        """

        ret = {}

        for rec in self.nationality_table.keys():

            this_record = self.nationality_table[rec]

            try:
                institutions = this_record["institution"]
            except KeyError:
                # missing person field, skip to next entry
                continue

            for i in institutions:
                ret[i] = this_record["country_en"]

        return ret

    def corp_relation_mapping(self, ooid):
        """
        Map an Institution to the Corporate Entity that it's related to,
        and that Corporate Entity's religious family.
        """

        ret = \
            {
                "religious_family": "N/A",
                "association": "N/A"
            }

        rel_record = self.org_org_table[ooid]

        try:
            corp_id = rel_record["corp_id_2"][0]
        except KeyError:
            return ret

        this_corp = self.corporate_entity_table[corp_id]

        try:
            ret["religious_family"] = self._religious_family_mapping(this_corp["religious_family"][0])
        except KeyError:
            pass

        try:
            ret["association"] = this_corp["corp_name_en"]
        except KeyError:
            pass

        return ret

    def add_geo(self, rec, geo):
        """
        Fetch geographical coordinates for this record.
        """

        ret = []

        for g in geo:

            rec_copy = copy.deepcopy(rec)
            geo_rec = self.fetch_geo(g)

            if geo_rec is not None:

                rec_copy["coords"]["lat"] = geo_rec["coords"]["lat"]
                rec_copy["coords"]["lon"] = geo_rec["coords"]["lon"]
                rec_copy["loc"]["location_type"] = geo_rec["loc"]["location_type"]
                rec_copy["loc"]["location_name"] = geo_rec["loc"]["location_name"]
                rec_copy["loc"]["location_name_zh"] = geo_rec["loc"]["location_name_zh"]
                rec_copy["loc"]["province_name"] = geo_rec["loc"]["province_name"]
                ret.append(rec_copy)

        return ret

    def map_to_coords(self):
        """
        For each Institution record, build a record of it's type, nationality,
        religious family, association, and where and when it existed.
        """

        ret = []

        institution_to_type = self.type_dict()
        institution_to_nationality = self.nationality_dict()

        for i in self.institution_table:

            # initialize dict that stores info about this institution & populate below
            i_rec = \
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
                            "location_name": "N/A",
                            "province_name": {}
                        },
                    "type": "institution",
                    "institution_type": "N/A",
                    "nationality": "N/A",
                    "corp_relations":
                        {
                            "religious_family": "N/A",
                            "association": "N/A"
                        },
                    "name": "N/A",
                    "name_zh": "N/A"
                }

            try:
                i_rec["name"] = self.institution_table[i]["inst_name"].lower()
            except KeyError:
                # no name for this entry, skip to next one
                continue

            try:
                i_rec["name_zh"] = self.institution_table[i]["inst_name_zh"]
            except KeyError:
                pass

            try:
                i_rec["institution_type"] = institution_to_type[i].lower()
            except KeyError:
                pass

            try:
                i_rec["time"]["start_year"] = self.institution_table[i]["start_year"]
            except KeyError:
                pass

            try:
                i_rec["nationality"] = institution_to_nationality[i].lower()
            except KeyError:
                pass

            try:
                org_org_id = self.institution_table[i]["organization_organization"][0]
                i_rec["corp_relations"] = self.corp_relation_mapping(org_org_id)
            except KeyError:
                pass

            try:
                geo = self.institution_table[i]["geography"]
                recs = self.add_geo(i_rec, geo)
                if len(recs) > 0:
                    ret.extend(recs)
            except KeyError:
                continue

        return ret
