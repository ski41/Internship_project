import numpy as np
import trimesh
import os

# import tkinter as tk
# from tkinter import filedialog as fd
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
# def select_file():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)

#     showinfo(
#         title='Selected File',
#         message=filename
#     )


# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )

# open_button.pack(expand=True)


# # run the application
# root.mainloop()

fileloc = 'C:/Users/Acer/PythonProjects/Internship_project-main/CAD_models'

for root, dirs, files in os.walk(fileloc, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        # filename = fd.askopenfilename()
        mesh = trimesh.load_mesh(os.path.join(root, name))

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
        mesh.visual.face_colors = [128,255,255,255]
        scene = trimesh.Scene([mesh,ray_visualize])
        scene.show()



