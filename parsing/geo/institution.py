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

    def map_to_coords(self):

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
                    "tradition": "N/A",
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
                i_rec["name"] = self.institution_table[i]["inst_name"]
            except KeyError:
                # no name for this entry, skip to next one
                continue

            try:
                geo = self.institution_table[i]["geography"]
            except KeyError:
                continue

            for g in geo:

                i_rec_copy = copy.deepcopy(i_rec)
                geo_rec = self.fetch_geo(i_rec_copy, g)

                if geo_rec is not None:
                    ret.append(geo_rec)

        return ret
