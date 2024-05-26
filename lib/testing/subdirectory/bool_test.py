#!/usr/bin/env python3

import os
import sys

print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

try:
    from bool_functions import return_true
except ImportError as e:
    print("ImportError:", e)
    sys.exit(1)
except Exception as e:
    print("An unexpected error occurred while importing:", e)
    sys.exit(1)

def test_return_true():
    '''In bool_functions, function "return_true" returns True.'''
    try:
        assert return_true() == True
        print("Test passed.")
    except AssertionError:
        print("Test failed: return_true() did not return True.")
    except Exception as e:
        print("An unexpected error occurred during the test:", e)

# Run the test
test_return_true()
