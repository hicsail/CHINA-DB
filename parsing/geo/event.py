"""
EventParser class -- Iterates over 'event' table and produces a separate GeoJson formatted
JSON object for each with geographical coordinates, along with other relevant information.
"""

from parsing.geo import Parser


class EventParser(Parser):

    def __init__(self, input_dir='/tmp/table_data/'):

        super(EventParser, self).__init__(input_dir)

        self.parse_type = "EVENT"

        self.event_table = self.load_record("event")
        self.event_type_table = self.load_record("event_type")

    def type_dict(self):

        ret = {}

        for rec in self.event_type_table.keys():

            this_record = self.event_type_table[rec]

            try:
                events = this_record["event"]
            except KeyError:
                # no events for this type, skip to next entry
                continue

            for e in events:
                ret[e] = this_record["type_en"]

        return ret

    def map_to_coords(self):
        """
        For each Event record, build a record of it type, and where & when it occurred.
        """

        ret = []

        event_to_type = self.type_dict()

        for e in self.event_table:

            # initialize dict that stores info about this event & populate below
            e_ret = \
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
                            "province_name": "N/A"
                        },
                    "type": "event",
                    "event_type": "N/A",
                    "name": "N/A"
                }

            try:
                e_ret["time"]["start_year"] = self.event_table[e]["start_year"]
            except KeyError:
                pass

            try:
                e_ret["event_type"] = event_to_type[e].lower()
            except KeyError:
                pass

            try:
                e_ret["name"] = self.event_table[e]["event_name_en"]
            except KeyError:
                pass

        # TODO: geo records once event_id is added to geography table

        return ret
