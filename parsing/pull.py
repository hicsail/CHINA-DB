import os

from parsing.download import PullData

dir_path = os.path.dirname(os.path.realpath(__file__))
a = PullData("{}/download/config/".format(dir_path))
a.pull_all_data()
