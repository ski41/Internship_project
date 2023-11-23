import numpy as np
import trimesh
import time

start_time = time.time()
mesh = trimesh.load_mesh('E:\\Suyogya Shakya\\Solid2.STL')

def calculate_thickness(mesh):
    ray_origin = mesh.triangles_center
    vector = mesh.face_normals
    ray_direction = np.array(-vector)
    # nor = np.linalg.norm(ray_direction)
    # normal = ray_direction / nor
    displacement = 0.001 * ray_direction
    new_coordinates = np.array(ray_origin) + displacement

    # Perform ray casting

    locations = mesh.ray.intersects_id(ray_origins=new_coordinates,
                                        ray_directions=
        ray_direction,
        multiple_hits=False,
        return_locations=True)
    # Calculate distances
    if len(locations[2]) == 0:
        return
    index = np.array(locations[0])
    vector2 = mesh.face_normals[index[0]]
    minimum_thickness = np.linalg.norm(
        locations[2] - ray_origin, axis=1)

    if round(minimum_thickness[0], 4) < 0.05:
        return

    return minimum_thickness[0]           
    
    

def calculate_thickness2(mesh):
    ray_origin = mesh.triangles_center
    vector = mesh.face_normals
    #ray_direction = np.array([-vector[0], -vector[1], -vector[2]])
    ray_direction = np.array(-vector)

    displacement = 0.001 * ray_direction
    new_coordinates = np.array(ray_origin) + displacement


    # Perform ray casting
    locations, _, _ = mesh.ray.intersects_location(ray_origins=new_coordinates,
                                                    ray_directions=
                                                        ray_direction,
                                                    multiple_hits=True)
    
    # Calculate distances
    distances = np.linalg.norm(locations - ray_origin, axis=1)

    # Get minimum thickness
    min_distance = np.min(distances)
    if np.isclose(min_distance, 0, atol=0.01):
        minimum_thickness = np.max(distances)
    else:
        minimum_thickness = min_distance

    return minimum_thickness

end_time = time.time()

t = 2*calculate_thickness(mesh)
print(t)
print(f"execution time:{end_time-start_time}")