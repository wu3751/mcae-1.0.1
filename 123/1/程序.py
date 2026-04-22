from PIL import Image, ImageDraw, ImageFont

datapack_name = "mcae"
text = "walk through fire with you"
font_path = "msyh.ttc"
font_size = 40

particle_type = "minecraft:end_rod"
base_color = (0.2, 0.5, 1)

param1 = 1
param2 = 0
param3 = 0.3
param4 = 0
param5 = 0
param6 = 0
param7 = 0
param8 = 1
param9 = 0
#speed_expr = "vy=0.1"
calc_interval = 1.0
group = "null"

width = int(font_size * len(text) * 1.5)
height = int(font_size * 1.5)
img = Image.new("L", (width, height), 0)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
draw.text((0, 0), text, 255, font=font)

points = []
for y in range(img.height):
    for x in range(img.width):
        if img.getpixel((x, y)) > 128:
            scaled_x = x * 0.08
            scaled_y = (img.height - 1 - y) * 0.08
            points.append((scaled_x, scaled_y))

output_file = "000000.mcfunction"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"# 粒子文字：{text}\n")
    f.write(f"# 粒子类型：{particle_type}\n")
    f.write(f"# 粒子数量：{len(points)} 个像素点\n")
    f.write(f"# 制作工具：Python 制作者：kali无 使用模组：ColorBlock\n")
    f.write(f"# 详细教程：https://mc.ecylt.top/#tutorial\n")
    f.write(f"# 商务合作：2672365813\n\n")
    f.write(f"# 【版权声明】\n")
    f.write(f"# 本作品（含资源包、代码、素材等）版权归 kali无 所有\n")
    f.write(f"# 未经授权，禁止任何形式的商用、转载、二次修改及分发\n")
    f.write(f"# 侵权行为将依法追责\n\n")

    for px, py in points:
        pos_x = f"~{px -23:.2f}"
        pos_y = f"~{py:.2f}"
        pos_z = "~-30"

        cmd = (f"particleex normal {particle_type} {pos_x} {pos_y} {pos_z} "
               f"{base_color[0]:.1f} {base_color[1]:.1f} {base_color[2]:.1f} "
               f"{param1} {param2} {param3} {param4} {param5} {param6} {param7} {param8} {param9} "
               #f"\"{speed_expr}\" {calc_interval:.1f} {group}\n")
               f"{group}\n")
        f.write(cmd)

print(f"已生成 {output_file} 文件，包含 {len(points)} 个粒子点")