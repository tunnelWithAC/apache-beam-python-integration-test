# from __future__ import absolute_import

import logging

from porter import pipeline

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  pipeline.run()

