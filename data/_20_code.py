import bpy
import numpy as np
import math
import mathutils
import sys


# get the word to reverse from the command line args!
try:
    myword = " ".join(sys.argv).split("--")[1].strip()
except:
    myword = "okay"

# clean up any existing objects
for o in bpy.context.scene.objects:
    o.select_set(True)
    bpy.ops.object.delete(use_global=True)
    

# create my different colors as materials
mat_1 = bpy.data.materials.new("mat1")
mat_2 = bpy.data.materials.new("mat2")
mat_3 = bpy.data.materials.new("mat3")

# Set all the values we need and create the objects
myradius = len(myword)
mydepth = 0.15 * len(myword)

# place a "stage"
bpy.ops.mesh.primitive_plane_add(size=12*myradius, enter_editmode=False, location=(0, 0, 0))
activeObject = bpy.context.active_object # Set active object to variable
activeObject.data.materials.append(mat_1) # add the material to the object
bpy.context.object.active_material.diffuse_color = (56/255, 230/255, 30/255, 1) # and set the color

bpy.ops.mesh.primitive_cylinder_add(radius=myradius, depth=mydepth, enter_editmode=False, location=(0, 0, mydepth/2))
activeObject = bpy.context.active_object # Set active object to variable
activeObject.data.materials.append(mat_2) # add the material to the object
bpy.context.object.active_material.diffuse_color = (218/255, 231/255, 245/255, 1) # and set the color


# place all characters on the stage
for i in range(len(myword)):
    current_char = myword[i]
    current_xoffset = len(myword) - 1 - i
    mynewxpos = i - current_xoffset
    mynewzpos = 1.01 * mydepth

    bpy.ops.object.text_add(enter_editmode=False, location=(mynewxpos, 0, mynewzpos))
    bpy.context.object.data.extrude = 0.1
    bpy.ops.transform.rotate(value=math.pi/2, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    
    activeObject = bpy.context.active_object #Set active object to variable
    activeObject.data.materials.append(mat_3) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (12/255, 79/255, 148/255, 1) # and set the color 

    # to change the content of the current text field (we need to 
    # treat each text field separately)    
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    
    # Set new char and the style of the current text field   
    bpy.ops.font.text_insert(text=current_char)
    bpy.ops.font.select_all()
    bpy.ops.font.case_set(case='UPPER')
    bpy.ops.font.style_set(style='BOLD')
    bpy.ops.object.editmode_toggle()
    

    
    
# create a light source    
bpy.ops.object.light_add(type='SUN', radius=8*myradius, location=(4.95938, 4.81107, 9.06277))
bpy.context.object.data.energy = 9
    
# set the starting position of the camera, with reference
# to the values of the cylinder (see above)
camera_x = 0
camera_y = 3.4 * -myradius 
camera_z = 4.2 * mydepth

# set the starting rotation of the camera
camera_rotate_x = 1.39626
camera_rotate_y = 0
camera_rotate_z = 0

bpy.ops.object.camera_add(enter_editmode=False, location=(camera_x, camera_y, camera_z), rotation=(camera_rotate_x, camera_rotate_y, camera_rotate_z))
bpy.context.scene.camera = bpy.context.object

# make sure the camera will always look at the cylinder
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Cylinder"]
bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'

# Set up camera rotation
frame_num = 120

camera = bpy.context.scene.camera 
cameraOrigin = np.array(camera.location)
theta = math.pi/frame_num   # rotate halfway around (1 pi radian), over 250 frames

def rotateCamera(scene):    
    newTheta = theta * scene.frame_current
    rotationMatrix = np.array([[math.cos(newTheta), -math.sin(newTheta),0],
                               [math.sin(newTheta), math.cos(newTheta), 0],
                               [0, 0, 1]])
    camera.location = np.dot(cameraOrigin, rotationMatrix)

    # also rotate all the text objects!    
    mychars = [o for o in bpy.context.scene.objects if o.type == "FONT"]     
    for obj in mychars:
        obj.select_set(True)
        # rotate at the z-axis
        obj.rotation_euler=(math.pi/2, 0, 0)
        obj.keyframe_insert(data_path='rotation_euler', frame=0)      
        obj.rotation_euler=(math.pi/2, 0, -math.pi)  # set the coordinate to math.pi
                                                     # for counter-clockwise rotation!
        obj.keyframe_insert(data_path='rotation_euler', frame=frame_num)
        obj.select_set(False)
    
def setRotation():
    # clear old handlers
    bpy.app.handlers.frame_change_pre.clear()
    # register a new handler
    bpy.app.handlers.frame_change_pre.append(rotateCamera)
    
setRotation()


# set the render resolution and then render each frame to a file
bpy.context.scene.render.resolution_x /= 2.2
bpy.context.scene.render.resolution_y /= 2.2

outpath = "./data/images/frame_{:03d}.png"
for current_frame_num in range(frame_num + 1):
    bpy.context.scene.frame_set(current_frame_num)
    bpy.context.scene.render.filepath = outpath.format(current_frame_num)
    bpy.ops.render.render(write_still=True)    
