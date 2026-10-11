import sys
import SimpleITK as sitk
import vtk
import numpy as np
import matplotlib
import pandas as pd

print("Python: ", sys.version)
print("Python executable: ", sys.executable)
print("SimpleITK: ", sitk.Version())
print("VTK:", vtk.vtkVersion.GetVTKVersion())
print("NumPy: ", np.__version__)
print("Matplotlib: ", matplotlib.__version__)
print("Pandas: ", pd.__version__)

print("\nEnvironment setup successful.")

# Expected output:
# Python:  3.14.0 (bla bla bla) [bla bla bla]
# Python executable:  C:..\csc621-team-earth-biomed-project\CovidCTAnalysis\.venv\Scripts\python.exe
# SimpleITK:  SimpleITK Version: 2.5.6 (ITK 5.4)
# Compiled: something something date/time
#
# VTK: 9.7.1
# NumPy:  2.5.4
# Matplotlib:  3.11.2
# Pandas:  3.0.6
#
# Environment setup successful.
# Press any key to continue . . .
