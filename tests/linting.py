#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import restructuredtext_lint
import sys

for file in glob.glob('content/*.rst'):
    errors = restructuredtext_lint.lint_file(file)
    if len(errors) > 0:
      print 'Err in %s: L%s - %s' % (errors[0].source , errors[0].line, errors[0].message)
      sys.exit(1)

sys.exit(0)
