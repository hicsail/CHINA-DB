"""
PersonParser class -- Iterates over 'person' table and produces a separate GeoJson formatted
JSON object for each organization/institution with geographical coordinates that they were
involved with, along with other relevant information.
"""

import json
import copy

from parsing.geo import Parser


class PersonParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(PersonParser, self).__init__(input_dir)

        self.person_table = self.load_record("person")
        self.nationality_table = self.load_record("nationality")

    def load_record(self, rec_type):
        """
        Load a table from file.
        """

        with open("{0}/{1}.json".format(self.input_dir, rec_type), 'r') as f:

            ret = json.loads(f.read())

        return ret

    def nationality_dict(self):

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

    def fetch_geo(self, rec, g):

        try:
            g_rec = self.geo_table[g]["township_id"][0]
            t_rec = self.township_table[g_rec]

            rec["coords"]["lat"] = t_rec["latitutde"]
            rec["coords"]["lon"] = t_rec["longitude"]
            rec["loc"]["location_type"] = "township"
            rec["loc"]["location_name"] = t_rec["township_id"]

            return rec

        except KeyError:
            pass

        try:
            g_rec = self.geo_table[g]["county_id"][0]
            c_rec = self.county_table[g_rec]

            rec["coords"]["lat"] = c_rec["latitude"]
            rec["coords"]["lon"] = c_rec["longitude"]
            rec["loc"]["location_type"] = "county"
            rec["loc"]["location_name"] = c_rec["county_id"]

            return rec

        except KeyError:
            pass

        try:
            g_rec = self.geo_table[g]["perfecture_id"][0]
            p_rec = self.prefecture_table[g_rec]

            rec["coords"]["lat"] = p_rec["latitude"]
            rec["coords"]["lon"] = p_rec["longitude"]
            rec["loc"]["location_type"] = "prefecture"
            rec["loc"]["location_name"] = p_rec["prefecture_id"]

            return rec

        except KeyError:
            pass

        try:
            g_rec = self.geo_table[g]["province_id"][0]
            p_rec = self.province_table[g_rec]

            rec["coords"]["lat"] = p_rec["latitude"]
            rec["coords"]["lon"] = p_rec["longitude"]
            rec["loc"]["location_type"] = "province"
            rec["loc"]["location_name"] = p_rec["province_id"]

            return rec

        except KeyError:
            pass

        return None

    def add_geo(self, inst_id, rec):

        ret = []

        current_institution = self.institution_table[inst_id]
        rec["institution_name"] = current_institution["inst_id"]
        geo = current_institution["geography"]

        for g in geo:

            rec_copy = copy.deepcopy(rec)
            geo_rec = self.fetch_geo(rec_copy, g)

            if geo_rec is not None:
                ret.append(geo_rec)

        return ret

    def map_to_coords(self):
        """
        For each Person record, build a record of each institutions/organization that
        they participated in, where they were located, and what time they did it.

        TODO: nationality, start year, birth year, death year, gender
        """

        ret = []

        person_to_nationality = self.nationality_dict()

        for p in self.person_table:

            # initialize dict that stores info about this person & populate below
            p_ret = {
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
                "type": "person",
                "nationality": "N/A",
                "gender": "N/A",
                "institution_name": "N/A"
            }

            for e in p_ret["titles"]:
                try:
                    p_ret["titles"][e] = self.person_table[p][e]
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
                p_ret["gender"] = self.person_table[p]["gender"][0]
            except KeyError:
                pass

            try:
                p_ret["nationality"] = person_to_nationality[p]
            except KeyError:
                pass

            try:
                orgs = self.person_table[p]["person_organization"]
            except KeyError:
                # no orgs == can't map to coords, skip to next entry
                continue

            for org in orgs:

                current_org = self.person_org_table[org]
                try:
                    p_ret["time"]["start_year"] = self.person_org_table[org]["start_year"]
                except KeyError:
                    pass

                try:
                    inst_id = current_org["inst_id"][0]

                    recs = self.add_geo(inst_id, p_ret)
                    ret.extend(recs)

                except KeyError:
                    pass

        return ret

    def build_records(self):
        """
        Maps each Person record to its set of institutions / coordinates / time data,
        then consolidates that list into a GeoJson formatted list of points with all
        matching objects for each point stored in a list on that point.
        """

        records = self.map_to_coords()

        ret = {}
        all_coords = set()

        for r in records:

            coords = "{0} {1}".format(r["coords"]["lon"], r["coords"]["lat"])

            if coords in all_coords:
                # merge this record with an existing Point

                del r["coords"]

                ret[coords]["properties"]["objects"].append(r)

            else:
                # create a new Point

                all_coords.add(coords)

                new_coords = [r["coords"]["lon"], r["coords"]["lat"]]
                del r["coords"]

                new_dict = \
                    {
                        "type": "Feature",
                        "geometry":
                        {
                            "type": "Point",
                            "coordinates": new_coords
                        },
                        "properties":
                        {
                            "objects":
                            [
                                r
                            ]
                        }
                    }

                ret[coords] = new_dict

        self.records = list(ret.values())

        return self













