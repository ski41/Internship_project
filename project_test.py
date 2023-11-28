import numpy as np
import trimesh

#mesh = trimesh.load_mesh('cup.stl')
#mesh = trimesh.load_mesh('Rect_1_5_8.stl')
file_name = 'CAD_models/cup.stl'
mesh = trimesh.load_mesh(file_name)

ray_origin = mesh.triangles_center
vector = mesh.face_normals
ray_direction = np.array(vector)

#gives out thickness between various mesh triangles as a numpy array.
thickness= trimesh.proximity.thickness(mesh, ray_origin, exterior=False, normals=None, method='ray')

#gives the index of minimum thikness.
#index_small = thickness.min()
list=[]
tri_ind=[]
min_ray=[]
min_dir=[]

for i in range(len(thickness)):
    if thickness[i] < 1.5:
        list.append(i)
        tri_ind.append(i)

for j in list:
    min_ray.append(ray_origin[j])
    min_dir.append(ray_direction[j])

min_ray = np.array(min_ray)
min_dir = np.array(min_dir)


#draws a line where the minimum thickness is encountered
if(thickness.min() < 1.5):
    
    ray_visualize = trimesh.load_path(np.hstack((min_ray,
                                                min_ray + min_dir*0.5)).reshape(-1, 2, 3))

    mesh.unmerge_vertices()
    mesh.visual.face_colors = [255,255,255,255]
    mesh.visual.face_colors[tri_ind] = [255, 0, 0, 255]
    scene = trimesh.Scene([mesh,ray_visualize])
    scene.show()

    print("Thickness less than 1.5 for file :", file_name)
else:
    print("Ok for printing :", file_name)






