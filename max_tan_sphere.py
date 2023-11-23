import trimesh
import time

r2time1 = time.time()
# Load a 3D mesh from a file
mesh = trimesh.load_mesh('E:\\Suyogya Shakya\\Solid2.STL')

# Define a list of points where you want to find tangent spheres
points = mesh.triangles_center
vertices = mesh.vertices
# print(points)
# points = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

# Find the maximum tangent spheres inscribed within the mesh
# r2time1 = time.time()
result = trimesh.proximity.max_tangent_sphere(mesh, points, inwards=True)
# r2time2 = time.time()
#print(vertices)
# Print the result

# Finding mesh thickness

# result2 = trimesh.proximity.thickness(mesh, points, exterior=False, normals=None, method='max_sphere')


# r3time1 = time.time()
# result3 = trimesh.proximity.thickness(mesh, points, exterior=False, normals=None, method='ray')
# r3time2 = time.time()

r2time2 = time.time()
print(2*result[1])

# Display mesh thickness
#print(result2)
print(f"result execution time: {r2time2-r2time1}")
#print(result3)
#print(f"result3 execution time: {r3time2-r3time1}")