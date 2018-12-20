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
                # TODO: there's a type_zh field too, could add later
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

    def religious_family_mapping(self, org_org_id_list):
        """
        Map an Insitution to a list of Corporate Entities that it
        is related to, and then return a dict of the Corporate Entity
        types whose values are lists of their corresponding Corporate
        Entities.
        """

        ret = {}

        for oid in org_org_id_list:

            rel_record = self.org_org_table[oid]

            try:
                corp_rel = rel_record["corp_id_2"]
                corp_family = rel_record["religious_family"]
            except KeyError:
                continue

            if corp_family not in ret.keys():
                ret[corp_family] = [corp_rel]
            else:
                ret[corp_family].append(corp_rel)

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
                ret.append(rec_copy)

        return ret

    def map_to_coords(self):
        """
        For each Institution record, build a record of it's type, nationality,
        religious family, denomination, name, and where and when it existed.
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
                            "location_name": "N/A"
                        },
                    "type": "institution",
                    "institution_type": "N/A",
                    "nationality": "N/A",
                    "religious_family": {},
                    "denomination": "N/A",
                    "name": "N/A",
                }

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
                org_org_id = self.institution_table["organization_organization"]
                i_rec["religious_family"] = self.religious_family_mapping(org_org_id)
            except KeyError:
                pass

            try:
                i_rec["name"] = self.institution_table[i]["inst_name"]
            except KeyError:
                # no name for this entry, skip to next one
                continue

            try:
                geo = self.institution_table[i]["geography"]
                recs = self.add_geo(i_rec, geo)
                if len(recs) > 0:
                    ret.extend(recs)
            except KeyError:
                continue

        return ret
