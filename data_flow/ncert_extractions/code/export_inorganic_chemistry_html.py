#!/usr/bin/env python3
"""Entry point for rendering an NCERT INORGANIC CHEMISTRY chapter.

    python3 scripts/export_inorganic_chemistry_html.py CHE12L-ch05 \\
        --pdf inputs/ncert/latest/Class_12th/Chemistry/Chapter_5.pdf \\
        --title "Chemistry Class 12 (Latest NCERT) - Unit 5: Coordination Compounds"

The page layout lives in `chemistry_render.py`, which is shared with the organic flow because
Unit 5 and Unit 9 are the same book. This file exists so that the two subjects have two separate,
clearly-named entry points: a change made for organic cannot arrive here by accident, and reading
a command line tells you which subject is being built.

Inorganic adds no render hooks. Its figures are coordination diagrams, which are cropped from the
page like any other artwork, and its three displayed equations are handled by the shared renderer's
own text-first path. Everything subject-specific about this chapter is therefore in the data, not
in code -- which is the honest answer for it, and the reason this file is short.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chemistry_render  # noqa: E402

if __name__ == "__main__":
    sys.exit(chemistry_render.main())
