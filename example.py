from CodeVideoRenderer import CodeVideo

# Complete code content to record
code_to_render = '''from PIL import Image, ImageDraw, ImageFont # PIL library

# Comment section (don't worry if you don't understand, I'll explain slowly)
# Created by kaliwu, using Python script to create graphical particle text
# Principle: enumerate every pixel point
# Datapack name (please modify according to actual situation)

datapack_name = "mcae"
# Text content
text = "Minecraft"
# Font path (can be replaced with local Chinese font file path)
font_path = "msyh.ttc"  # Microsoft YaHei, or use other Chinese fonts in the system
font_size = 40  # Increase font size

# Create higher resolution image
img = Image.new("L", (font_size * len(text) * 2, font_size * 2), 0)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
draw.text((0, 0), text, 255, font=font)

# Get all black pixel coordinates
points = []
for y in range(img.height):
    for x in range(img.width):
        if img.getpixel((x, y)) > 128:
            # Reverse Y coordinate, fix upside down
            points.append((x * 0.1, (img.height - 1 - y) * 0.1))

# Particle generation base position (can be adjusted as needed)
base_x, base_y, base_z = 0, 4, 0

# Generate single mcfunction file
with open("my_particles.mcfunction", "w", encoding="utf-8") as f:
    f.write("# End Rod Particle Text - Minecraft\\n")
    f.write(f"# Generation time: {len(points)} particle points\\n\\n")

    for px, py in points:
        # Generate end rod particles, fixed position
        f.write(f"particle end_rod {base_x + px:.2f} {base_y + py:.2f} {base_z} 0 5 0 0.1 0\\n")

print(f"Generated my_particles.mcfunction file, containing {len(points)} particle points")
print(f"Put the file in datapack functions folder")
print(f"Execute in game: /function {datapack_name}:my_particles to display particle text")
'''

# Create code recording video
video = CodeVideo(
    video_name="minecraft_particle_text_generator",
    code_string=code_to_render,
    language="python",
    line_spacing=0.8
    # Removed theme parameter as it's not supported
)

# Start recording
video.render()