import numpy as np
import trimesh
import os

fileloc = 'C:/Users/Acer/PythonProjects/Internship_project-main/CAD_models'

# All files in above directory are checked for min. thickness
for root, dirs, files in os.walk(fileloc, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        # filename = fd.askopenfilename()
        mesh = trimesh.load_mesh(os.path.join(root, name))

        
        # mesh = trimesh.load_mesh('C:/Users/Acer/PythonProjects/Internship_project-main/CAD_models/Rect1.stl')

        ray_origin = mesh.triangles_center
        vector = mesh.face_normals
        ray_direction = np.array(vector)

        #gives out thickness between various mesh triangles as a numpy array.
        thickness= trimesh.proximity.thickness(mesh, ray_origin, exterior=False, normals=None, method='ray')

        #gives the index of minimum thikness.
        index_small = thickness.min()
        list=[]
        min_ray=[]
        min_dir=[]

        for i in range(len(thickness)):
            if thickness[i] < 1.5:
                list.append(i)

        for j in list:
            min_ray.append(ray_origin[j])
            min_dir.append(ray_direction[j])

        min_ray = np.array(min_ray)
        min_dir = np.array(min_dir)

        print(thickness)

        #draws a line where the minimum thickness is encountered
        ray_visualize = trimesh.load_path(np.hstack((min_ray,
                                                     min_ray + min_dir*2.0)).reshape(-1, 2, 3))

        # i=27
        # ray_visualize = trimesh.load_path(np.hstack((ray_origin[i],
        #                                              ray_origin[i] + ray_direction[i])).reshape(-1, 2, 3))

        mesh.visual.face_colors = [255,255,255,255]
        mesh.visual.face_colors[[21,22,27,28]] = [255, 0, 0, 255]
        scene = trimesh.Scene([mesh,ray_visualize])
        scene.show()