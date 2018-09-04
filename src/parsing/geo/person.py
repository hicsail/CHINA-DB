"""
PersonParser class -- Iterates over 'person' table and produces a separate GeoJson formatted
JSON object for each organization/institution with geographical coordinates that they were
involved with, along with other relevant information.
"""

import json
import os
import pystache
import ast


class PersonParser:

    def __init__(self, input_dir='/tmp/table_data/'):

        self.input_dir = input_dir
        self.template_dir = "{}/templates/".format(os.path.dirname(os.path.realpath(__file__)))

        self.person_table = self.load_record("person")
        self.person_org_table = self.load_record("person_organization")
        self.institution_table = self.load_record("institution")
        self.geo_table = self.load_record("geography")
        self.township_table = self.load_record("township")
        self.county_table = self.load_record("county")
        self.prefecture_table = self.load_record("prefecture")
        self.province_table = self.load_record("province")

    def load_record(self, rec_type):

        with open("{0}/{1}.json".format(self.input_dir, rec_type), 'r') as f:

            ret = json.loads(f.read())

        return ret

    def build_json_person(self, pid, inst_name, start_year, lat, lon, name, loc_type):

        template = open("{}/person.tmpl".format(self.template_dir)).read()

        data = \
            {
                "LAT": lat,
                "LON": lon,
                "PID": pid,
                "INST_NAME": inst_name,
                "START_YEAR": start_year,
                "LOC_TYPE": loc_type,
                "LOC_NAME": name
            }

        return ast.literal_eval(pystache.render(template, data))

    def build_record(self, pid, inst_id, start_year):

        ret = []

        current_institution = self.institution_table[inst_id]
        inst_name = current_institution["inst_id"]
        geo = current_institution["geography"]

        for g in geo:

            try:

                g_rec = self.geo_table[g]["township_id"][0]

                t_rec = self.township_table[g_rec]

                lat = t_rec["latitutde"]
                lon = t_rec["longitude"]
                name = t_rec["township_id"]

                rec = self.build_json_person(pid, inst_name, start_year, lat, lon, name, "Township")
                ret.append(rec)

                continue

            except KeyError:

                pass

            try:

                g_rec = self.geo_table[g]["county_id"][0]

                c_rec = self.county_table[g_rec]

                lat = c_rec["latitude"]
                lon = c_rec["longitude"]
                name = c_rec["county_id"]

                rec = self.build_json_person(pid, inst_name, start_year, lat, lon, name, "County")
                ret.append(rec)

                continue

            except KeyError:

                pass

            try:

                g_rec = self.geo_table[g]["perfecture_id"][0]

                p_rec = self.prefecture_table[g_rec]

                lat = p_rec["latitude"]
                lon = p_rec["longitude"]
                name = p_rec["prefecture_id"]

                rec = self.build_json_person(pid, inst_name, start_year, lat, lon, name, "Prefecture")
                ret.append(rec)

                continue

            except KeyError:

                pass

            try:

                g_rec = self.geo_table[g]["province_id"][0]

                p_rec = self.province_table[g_rec]

                lat = p_rec["latitude"]
                lon = p_rec["longitude"]
                name = p_rec["province_id"]

                rec = self.build_json_person(pid, inst_name, start_year, lat, lon, name, "Province")
                ret.append(rec)

                continue

            except KeyError:

                pass

        return ret

    def map_person_to_coords(self):

        ret = []

        for p in self.person_table:

            try:

                pid = self.person_table[p]["person_id"]
                orgs = self.person_table[p]["person_organization"]

            except KeyError:

                continue

            for org in orgs:

                current_org = self.person_org_table[org]

                try:

                    inst_id = current_org["inst_id"][0]
                    start_year = current_org["start_year"]

                    rec = self.build_record(pid, inst_id, start_year)
                    ret.extend(rec)

                except KeyError:

                    pass

        return ret













