import copy

from parsing.geo import Parser


class PersonParser(Parser):
    """
    Iterates over 'person' table and produces a separate GeoJson formatted
    JSON object for each organization/institution with geographical coordinates
    that they were involved with, along with other relevant information.
    """

    def __init__(self, input_dir='/tmp/table_data/'):

        super(PersonParser, self).__init__(input_dir)

        self.parse_type = "PERSON"

        self.person_table = self.load_record("person")

    def nationality_dict(self):
        """
        Map Nationality ID's to strings.
        """

        ret = {}

        for rec in self.nationality_table.keys():

            this_record = self.nationality_table[rec]

            try:
                people = this_record["person"]
            except KeyError:
                # missing person field, skip to next entry
                continue

            for p in people:
                ret[p] = this_record["country_en"]

        return ret

    def tradition_mapping(self, inst_rec):

        ret = \
            {
                "religious_family": "N/A",
                "corp_name": "N/A"
            }

        try:
            org_org_id = inst_rec["organization_organization"][0]
            rel_record = self.org_org_table[org_org_id]
            corp_rel = rel_record["corp_id_2"]
            this_corp = self.corporate_entity_table[corp_rel]

            ret["corp_name"] = this_corp["corp_name_en"]
            ret["religious_family"] = self._religious_family_mapping(this_corp["religious_family"][0])
        except KeyError:
            pass

        return ret

    def add_geo_inst(self, inst_id, rec):
        """
        Fetch geographical coordinates for this record via the Institution that
        it corresponds to.
        """

        ret = []

        current_institution = self.institution_table[inst_id]
        rec["institution_name"] = current_institution["inst_id"].lower()
        rec["tradition"] = self.tradition_mapping(current_institution)

        geo = current_institution["geography"]

        for g in geo:

            rec_copy = copy.deepcopy(rec)
            geo_rec = self.fetch_geo(g)

            rec_copy["coords"]["lat"] = geo_rec["coords"]["lat"]
            rec_copy["coords"]["lon"] = geo_rec["coords"]["lon"]
            rec_copy["loc"]["location_type"] = geo_rec["loc"]["location_type"]
            rec_copy["loc"]["location_name"] = geo_rec["loc"]["location_name"]

            if geo_rec is not None:
                ret.append(rec_copy)

        return ret

    def add_geo_corp(self, corp_id, rec):
        """
        Fetch geographical coordinates for this record via the Corporate
        Entity that it corresponds to.
        """

        ret = []

        current_corp = self.corporate_entity_table[corp_id]

        try:
            org_org_ids = current_corp["organization_organization 2"]
            corp_name = current_corp["corp_name_en"]
            religious_family = self._religious_family_mapping(current_corp["religious_family"][0])
        except KeyError:
            return []

        for ooid in org_org_ids:

            try:
                inst_id = self.org_org_table[ooid]["inst_id_1"][0]
                inst_name = self.institution_table[inst_id]["name"]
                geo = self.institution_table[inst_id]["geography"]

                rec["institution_name"] = inst_name
                rec["tradition"]["corp_name"] = corp_name
                rec["tradition"]["religious_family"] = religious_family

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
        """
        For each Person record, build a record of each institutions/organization that
        they participated in, where they were located, and what time they did it.
        """

        ret = []

        person_to_nationality = self.nationality_dict()

        for p in self.person_table:

            # initialize dict that stores info about this person & populate below
            p_ret = \
                {
                    "coords":
                        {
                            "lat": "N/A",
                            "lon": "N/A"
                        },
                    "time":
                        {
                            "start_year": "N/A",
                            "birth_year": "N/A",
                            "death_year": "N/A"
                        },
                    "loc":
                        {
                            "location_type": "N/A",
                            "location_name": "N/A"
                        },
                    "titles":
                        {
                            "family_name_en": "N/A",
                            "given_name_en": "N/A",
                            "family_name_py": "N/A",
                            "given_name_py": "N/A"
                        },
                    "tradition":
                        {
                            "religious_family": "N/A",
                            "corp_name": "N/A"
                        },
                    "type": "person",
                    "nationality": "N/A",
                    "gender": "N/A",
                    "institution_name": "N/A"
                }

            for e in p_ret["titles"]:
                try:
                    p_ret["titles"][e] = self.person_table[p][e].lower()
                except KeyError:
                    continue

            try:
                p_ret["time"]["birth_year"] = self.person_table[p]["birth_year"]
            except KeyError:
                pass

            try:
                p_ret["time"]["death_year"] = self.person_table[p]["death_year"]
            except KeyError:
                pass

            try:
                p_ret["gender"] = self.person_table[p]["gender"][0].lower()
            except KeyError:
                pass

            try:
                p_ret["nationality"] = person_to_nationality[p].lower()
            except KeyError:
                pass

            try:
                orgs = self.person_table[p]["person_organization"]
            except KeyError:
                # no orgs == can't map to coords, skip to next entry
                continue

            for org in orgs:

                # org can correspond to an institution or a corporate entity
                current_org = self.person_org_table[org]

                try:
                    p_ret["time"]["start_year"] = self.person_org_table[org]["start_year"]
                except KeyError:
                    pass

                try:
                    inst_id = current_org["inst_id"][0]
                    recs = self.add_geo_inst(inst_id, p_ret)
                    if len(recs) > 0:
                        ret.extend(recs)
                except KeyError:
                    pass

                try:
                    corp_id = current_org["corp_id"][0]
                    recs = self.add_geo_corp(corp_id, p_ret)
                    if len(recs) > 0:
                        ret.extend(recs)
                except KeyError:
                    pass

        return ret
