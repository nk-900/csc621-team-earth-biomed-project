import SimpleITK as sitk

image = sitk.Image([128, 128, 64], sitk.sitkInt16)

print("Dimension: ", image.GetDimension())
print("Size: ", image.GetSize())    
print("Spacing: ", image.GetSpacing()) 

# SimpleITK to NumPy
# Note that while SimpleITK uses (x,y,z) indexing, NumPy uses (z,y,x) indexing.

array = sitk.GetArrayFromImage(image)
print("Array shape: ", array.shape)  # (64, 128, 128)