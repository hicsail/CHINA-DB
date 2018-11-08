import os

from parsing.download import PullData
from parsing.geo.person import PersonParser

dir_path = os.path.dirname(os.path.realpath(__file__))
a = PullData("{}/download/config/".format(dir_path))
a.pull_all_data()

a = PersonParser()

# write to /tmp/geo.js
a.write_records()