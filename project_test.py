import numpy as np
import trimesh

mesh = trimesh.load_mesh('Rect1.stl')

ray_origin = mesh.triangles_center
vector = mesh.face_normals
ray_direction = np.array(vector)

#gives out thickness between various mesh triangles as a numpy array.
thickness= trimesh.proximity.thickness(mesh, ray_origin, exterior=False, normals=None, method='ray')

#gives the index of minimum thikness.
index_small = thickness.argmin()
print(thickness)

#draws a line where the minimum thickness is encountered
ray_visualize = trimesh.load_path(np.hstack((ray_origin[index_small],
                                             ray_origin[index_small] + ray_direction[index_small]*2.0)).reshape(-1, 2, 3))
mesh.visual.face_colors = [255,255,255,255]
scene = trimesh.Scene([mesh,ray_visualize])
scene.show()



