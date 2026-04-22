from PIL import Image, ImageDraw, ImageFont

# Minecraft Particle Text Generator
datapack_name = "mcae"
text = "Minecraft"
font_path = "arial.ttf"
font_size = 40

# Create image
img = Image.new("L", (font_size * len(text) * 2, font_size * 2), 0)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
draw.text((0, 0), text, 255, font=font)

# Get pixel points
points = []
for y in range(img.height):
    for x in range(img.width):
        if img.getpixel((x, y)) > 128:
            points.append((x * 0.1, (img.height - 1 - y) * 0.1))

# Base position
base_x, base_y, base_z = 0, 4, 0

# Generate mcfunction file
with open("my_particles.mcfunction", "w") as f:
    f.write("# Particle Text\n")
    f.write(f"# Points: {len(points)}\n\n")
    for px, py in points:
        f.write(f"particle end_rod {base_x+px:.2f} {base_y+py:.2f} {base_z} 0 5 0 0.1 0\n")

print("File generated successfully")
