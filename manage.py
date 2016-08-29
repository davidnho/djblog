#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djblog.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_blog.settings")
>>>>>>> 6f4f41430417306bd4f207e2c9256f5095e3679f

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
