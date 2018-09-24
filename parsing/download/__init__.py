import json
import os

from airtable import Airtable


class PullData:

    def __init__(self, config_path):

        self.config_path = config_path
        self.api_key = self.load_api_key()
        self.base_key = self.load_base_key()
        self.tables = self.load_tables()

    def load_api_key(self):

        with open("{}/auth.json".format(self.config_path), 'r') as f:

            params = json.loads(f.read())

            return params["API_KEY"]

    def load_base_key(self):

        with open("{}/auth.json".format(self.config_path), 'r') as f:

            params = json.loads(f.read())

            return params["BASE_KEY"]

    def load_tables(self):

        with open("{}/tables.json".format(self.config_path), 'r') as f:

            params = json.loads(f.read())

            return params["TABLES"]

    def pull_all_data(self, output_dir=None):

        if output_dir is None:
            output_dir = "/tmp/table_data"

        os.makedirs(output_dir, exist_ok=True)

        for table in self.tables:

            table_dict = dict()

            data = Airtable(self.base_key, table, api_key=self.api_key).get_all()

            for d in data:
                table_dict[d["id"]] = d["fields"]

            with open("{0}/{1}.json".format(output_dir, table), 'w') as out:

                json.dump(table_dict, out, indent=4, sort_keys=True)





