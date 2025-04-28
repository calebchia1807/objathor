import os
import subprocess

# Paths - update to your file path before use!!!
asset_folder     = '/home/navsim/Desktop/objathor/objathor/assets' 
output_folder    = '/home/navsim/.objathor-assets/2023_09_23/assets'
blender_path     = '/usr/local/bin/blender'
main_script_path = '/home/navsim/Desktop/objathor/objathor/main.py'

# Gather all .glb files
glb_files = [f for f in os.listdir(asset_folder) if f.endswith('.glb')]

# Count and display
num_files = len(glb_files)
print(f"Found {num_files} GLB file(s) for conversion.\n")

# Process each .glb file
for idx, filename in enumerate(glb_files, start=1):
    uid = os.path.splitext(filename)[0]  # filename without extension
    glb_path = os.path.join(asset_folder, filename)

    # Construct the command
    command = [
        'python', main_script_path,
        '--uid', uid,
        '--glb', glb_path,
        '--output', output_folder,
        '--extension', '.pkl.gz',
        '--blender_installation_path', blender_path
    ]

    print(f"[{idx}/{num_files}] Converting: {uid}")
    
    try:
        subprocess.run(command, check=True)
        print(f"[{idx}/{num_files}] Successfully converted: {uid}\n")
    except subprocess.CalledProcessError as e:
        print(f"[{idx}/{num_files}] Failed to convert: {uid}")
        print(f"Error: {e}\n")

print("All asset conversions completed.")
