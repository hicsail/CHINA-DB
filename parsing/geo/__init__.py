import json
import os
import pystache


class Parser:

    def __init__(self, input_dir='/tmp/table_data/'):

        self.input_dir = input_dir
        self.template_dir = "{}/templates/".format(os.path.dirname(os.path.realpath(__file__)))
        self.parse_type = "BASE"

        self.person_org_table = self.load_record("person_organization")
        self.org_org_table = self.load_record("organization_organization")
        self.corporate_entity_type_table = self.load_record("corporate_entity_type")
        self.institution_table = self.load_record("institution")
        self.corporate_entity_table = self.load_record("corporate_entity")
        self.geo_table = self.load_record("geography")
        self.township_table = self.load_record("township")
        self.county_table = self.load_record("county")
        self.prefecture_table = self.load_record("prefecture")
        self.province_table = self.load_record("province")
        self.nationality_table = self.load_record("nationality")
        self.religious_family_table = self.load_record("religious_family")

        self.records = None

    def load_record(self, rec_type):
        """
        Load a table from file
        """

        with open("{0}/{1}.json".format(self.input_dir, rec_type), 'r') as f:

            ret = json.loads(f.read())

        return ret

    def map_to_coords(self):
        """
        Overridden in subclasses
        """

        return {}

    def _religious_family_mapping(self, fam_id):

        return self.religious_family_table[fam_id]["name_en"].lower()

    def _corp_type_mapping(self, type_id):

        return self.corporate_entity_type_table[type_id]["type_en"].lower()

    def grab_province_from_township(self, t_rec):

        try:
            county_rec = t_rec["county_id"][0]
            c_rec = self.county_table[county_rec]
            pref_rec = c_rec["prefecture_id"][0]
            p_rec = self.prefecture_table[pref_rec]
            prov_rec = p_rec["province_id"][0]
            province_record = self.province_table[prov_rec]
            try:
                name_en = province_record["name_en"]
            except KeyError:
                name_en = "N/A"
            try:
                name_py = province_record["name_py"]
            except KeyError:
                name_py = "N/A"
            try:
                name_zh = province_record["name_zh"]
            except KeyError:
                name_zh = "N/A"
            return {"name_en": name_en.lower(), "name_py": name_py.lower(), "name_zh": name_zh}
        except KeyError:
            return {"name_en": "N/A", "name_py": "N/A", "name_zh": "N/A"}

    def grab_province_from_county(self, c_rec):

        try:
            pref_rec = c_rec["prefecture_id"][0]
            p_rec = self.prefecture_table[pref_rec]
            prov_rec = p_rec["province_id"][0]
            province_record = self.province_table[prov_rec]
            try:
                name_en = province_record["name_en"]
            except KeyError:
                name_en = "N/A"
            try:
                name_py = province_record["name_py"]
            except KeyError:
                name_py = "N/A"
            try:
                name_zh = province_record["name_zh"]
            except KeyError:
                name_zh = "N/A"
            return {"name_en": name_en.lower(), "name_py": name_py.lower(), "name_zh": name_zh}
        except KeyError:
            return {"name_en": "N/A", "name_py": "N/A", "name_zh": "N/A"}

    def grab_province_from_prefecture(self, p_rec):

        try:
            prov_rec = p_rec["province_id"][0]
            province_record = self.province_table[prov_rec]
            try:
                name_en = province_record["name_en"]
            except KeyError:
                name_en = "N/A"
            try:
                name_py = province_record["name_py"]
            except KeyError:
                name_py = "N/A"
            try:
                name_zh = province_record["name_zh"]
            except KeyError:
                name_zh = "N/A"
            return {"name_en": name_en.lower(), "name_py": name_py.lower(), "name_zh": name_zh}
        except KeyError:
            return {"name_en": "N/A", "name_py": "N/A", "name_zh": "N/A"}

    def fetch_geo(self, g):
        """
        Map location of a record to a township / county / prefecture / province
        in decreasing order of granularity.
        """

        rec = \
            {
                "coords":
                    {
                        "lat": "N/A",
                        "lon": "N/A"
                    },
                "loc":
                    {
                        "location_type": "N/A",
                        "location_name": "N/A",
                        "location_name_zh": "N/A",
                        "province_name": {}
                    }
            }

        try:
            g_rec = self.geo_table[g]["township_id"][0]
            t_rec = self.township_table[g_rec]

            rec["coords"]["lat"] = t_rec["latitude"]
            rec["coords"]["lon"] = t_rec["longitude"]
            rec["loc"]["location_type"] = "township"
            rec["loc"]["location_name"] = t_rec["name_en"].lower()
            rec["loc"]["location_name_zh"] = t_rec["name_zh"]
            rec["loc"]["province_name"] = self.grab_province_from_township(t_rec)

            return rec

        except KeyError:
            pass

        try:
            g_rec = self.geo_table[g]["county_id"][0]
            c_rec = self.county_table[g_rec]

            rec["coords"]["lat"] = c_rec["latitude"]
            rec["coords"]["lon"] = c_rec["longitude"]
            rec["loc"]["location_type"] = "county"
            rec["loc"]["location_name"] = c_rec["name_en"].lower()
            rec["loc"]["location_name_zh"] = c_rec["name_zh"]
            rec["loc"]["province_name"] = self.grab_province_from_county(c_rec)

            return rec

        except KeyError:
            pass

        try:
            g_rec = self.geo_table[g]["prefecture_id"][0]
            p_rec = self.prefecture_table[g_rec]

            rec["coords"]["lat"] = p_rec["latitude"]
            rec["coords"]["lon"] = p_rec["longitude"]
            rec["loc"]["location_type"] = "prefecture"
            rec["loc"]["location_name"] = p_rec["name_en"].lower()
            rec["loc"]["location_name_zh"] = p_rec["name_zh"]
            rec["loc"]["province_name"] = self.grab_province_from_prefecture(p_rec)

            return rec

        except KeyError:
            pass

        try:
            g_rec = self.geo_table[g]["province_id"][0]
            p_rec = self.province_table[g_rec]

            rec["coords"]["lat"] = p_rec["latitude"]
            rec["coords"]["lon"] = p_rec["longitude"]
            rec["loc"]["location_type"] = "province"
            rec["loc"]["location_name"] = p_rec["name_en"].lower()
            rec["loc"]["location_name_zh"] = p_rec["name_zh"]
            try:
                name_en = p_rec["name_en"]
            except KeyError:
                name_en = "N/A"
            try:
                name_py = p_rec["name_py"]
            except KeyError:
                name_py = "N/A"
            try:
                name_zh = p_rec["name_zh"]
            except KeyError:
                name_zh = "N/A"
            rec["loc"]["province_name"] = \
                {
                    "name_en": name_en.lower(),
                    "name_py": name_py.lower(),
                    "name_zh": name_zh
                }

            return rec

        except KeyError:
            pass

        return None

    def build_records(self):
        """
        Maps each record to its set of filter data, then consolidates
        that list into a GeoJson formatted list of points with all
        matching objects for each point stored in a list on that point.
        """

        records = self.map_to_coords()

        ret = {}
        all_coords = set()
        id_num = 0

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
                        "id": str(id_num),
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
                id_num += 1

        self.records = list(ret.values())

        return self

    def write_records(self, out_path=None):
        """
        Write GeoJson formatted records to file
        """

        if self.records is None:
            self.build_records()

        if out_path is None:
            out_path = "/tmp/geo_{}.js".format(self.parse_type)

        template = open("{}/geo.tmpl".format(self.template_dir)).read()

        data = \
            {
                "DATA": json.dumps(self.records, indent=4, sort_keys=False)
            }

        with open(out_path, 'w', encoding='utf8') as f:
            f.write(pystache.render(template, data))
