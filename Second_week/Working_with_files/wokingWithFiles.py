#!/usr/bin/env python3
"""Paths can be different across different operating systems. We need to make
sure we can provide alternatives for the platforms we want to support"""

import os

if os.path.exists("novel.txt"):
    os.remove("novel.txt")
if os.path.exists("first_draft.txt"):
    os.rename("first_draft.txt", "finished_masterpiece.txt")
