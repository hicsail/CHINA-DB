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

    def map_to_coords(self):

        ret = []

        for inst in self.institution_table:

            # initialize dict that stores info about this institution & populate below
            i_rec = \
                {
                    "type": "institution",
                    "institution_type": "N/A",
                    "nationality": "N/A",
                    "tradition": "N/A",
                    "denomination": "N/A",
                    "start_year": "N/A",
                    "name": "N/A",
                    "coords":
                        {
                            "lat": "N/A",
                            "lon": "N/A"
                        },
                    "loc":
                        {
                            "location_type": "N/A",
                            "location_name": "N/A"
                        }
                }

            try:
                i_rec["name"] = self.institution_table[inst]["inst_name"]
            except KeyError:
                # no name for this entry, just skip to next one
                continue

            try:
                i_rec["start_year"] = self.institution_table[inst]["start_year"]
            except KeyError:
                pass

            try:
                geo = self.institution_table[inst]["geography"]
            except KeyError:
                continue

            for g in geo:

                i_rec_copy = copy.deepcopy(i_rec)
                geo_rec = self.fetch_geo(i_rec_copy, g)

                if geo_rec is not None:
                    ret.append(geo_rec)

        return ret
