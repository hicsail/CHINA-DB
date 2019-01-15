import os
from subprocess import call

from parsing.download import PullData
from parsing.geo.merger import MergeParser

dir_path = os.path.dirname(os.path.realpath(__file__))
a = PullData("{}/download/config/".format(dir_path))
a.pull_all_data()

b = MergeParser()
b.write_records()

base_dir_path = "/".join(dir_path.split("/")[:-1])

cmd = "mv /tmp/geo_all.js {}/src/assets/geo.js".format(base_dir_path)

call(cmd, shell=True)