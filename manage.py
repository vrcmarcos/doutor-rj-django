#!/usr/bin/env python
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "doctor_rj"))
sys.path.insert(1, os.path.join(PROJECT_ROOT, "doctor_rj/core"))
sys.path.insert(2, os.path.join(PROJECT_ROOT, "doctor_rj/doctor_rj"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
