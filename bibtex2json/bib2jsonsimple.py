#!/usr/bin/env python
import json
import re

from .bibutils import extractEntries

def parse(lines):
    entries = extractEntries(lines)
    return lines