import os
import json
import pystache

from parsing.geo.corp_entity import CorpEntityParser
from parsing.geo.institution import InstitutionParser
from parsing.geo.person import PersonParser


class MergeParser:
    """
    Spawn each parser type and merge all records into a single GeoJson file.
    """

    def __init__(self, input_dir='/tmp/table_data/'):

        self.input_dir = input_dir
        self.template_dir = "{}/templates/".format(os.path.dirname(os.path.realpath(__file__)))

        self.corp_parser = CorpEntityParser()
        self.inst_parser = InstitutionParser()
        self.person_parser = PersonParser()

        self.records = None

    def create_all(self):
        """
        Generate all records
        """

        self.corp_parser.build_records()
        self.inst_parser.build_records()
        self.person_parser.build_records()

        return self

    def merge_all(self):
        """
        Merge all records into a single list of point records
        """

        if self.records is None:
            self.create_all()

        all_records = self.corp_parser.records + self.inst_parser.records + self.person_parser.records

        ret = {}
        all_coords = set()
        id_num = 0

        for r in all_records:

            coords = "{0} {1}".format(r["coords"]["lon"], r["coords"]["lat"])

            if coords in all_coords:
                # merge this record with an existing Point

                del r["coords"]

                if r["type"] == "person":
                    ret[coords]["properties"]["persons"].append(r)
                elif r["type"] == "corporate_entity":
                    ret[coords]["properties"]["corporate_entities"].append(r)
                elif r["type"] == "institution":
                    ret[coords]["properties"]["institutions"].append(r)
                elif r["type"] == "event":
                    ret[coords]["properties"]["events"].append(r)
                else:
                    print("Encountered unknown type: {}".format(r["type"]))
                    continue

            else:

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
                                "persons": [],
                                "institutions": [],
                                "corporate_entities": [],
                                "events": []
                            }
                    }

                if r["type"] == "person":
                    new_dict["properties"]["persons"].append(r)
                elif r["type"] == "corporate_entity":
                    new_dict["properties"]["corporate_entities"].append(r)
                elif r["type"] == "institution":
                    new_dict["properties"]["institutions"].append(r)
                elif r["type"] == "event":
                    new_dict["properties"]["events"].append(r)
                else:
                    print("Encountered unknown type: {}".format(r["type"]))
                    continue

                ret[coords] = new_dict
                id_num += 1

        self.records = list(ret.values())

        return self

    def write_records(self, out_path=None):
        """
        Write GeoJson formatted records to file
        """

        if self.records is None:
            self.merge_all()

        if out_path is None:
            out_path = "/tmp/geo_all.js"

        template = open("{}/geo.tmpl".format(self.template_dir)).read()

        data = \
            {
                "DATA": json.dumps(self.records, indent=4, sort_keys=False)
            }

        with open(out_path, 'w', encoding='utf8') as f:
            f.write(pystache.render(template, data))
