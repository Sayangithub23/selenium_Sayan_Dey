import os
import unittest

os.makedirs("reports", exist_ok=True)
suite = unittest.TestLoader().discover("tests", pattern="test_*unittest.py")
result = unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():
    raise SystemExit(1)
