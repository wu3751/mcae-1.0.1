from PIL import Image, ImageDraw, ImageFont

# 数据包名称（请根据实际情况修改）
datapack_name = "mcae"

# 文字内容
text = "纷飞的回忆"  # 日文示例
# 字体路径（可替换为本地支持中文的字体文件路径）
font_path = "msyh.ttc"  # 微软雅黑，或使用系统其他中文字体
font_size = 40  # 增大字体

# 创建更高分辨率的图像
img = Image.new("L", (font_size * len(text) * 2, font_size * 2), 0)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
draw.text((0, 10), text, 255, font=font)

# 获取所有黑色像素点坐标
points = []
for y in range(img.height):
    for x in range(img.width):
        if img.getpixel((x, y)) > 128:
            # y坐标反向，修正上下颠倒
            points.append((x * 0.1, (img.height - 1 - y) * 0.1))

# 粒子生成基准位置（可根据实际需要调整）
base_x_offset, base_y_offset, base_z_offset = -10, 0, -30

# 生成单个 mcfunction 文件
with open("1004.mcfunction", "w", encoding="utf-8") as f:
    f.write("# 末地烛粒子文字 - 我的世界\n")
    f.write(f"# 生成时间: {len(points)} 个粒子点\n\n")

    for px, py in points:
        # 生成末地烛粒子，使用相对坐标偏移
        final_x = base_x_offset + px
        final_y = base_y_offset + py
        final_z = base_z_offset
        f.write(f"particle end_rod ~{final_x:.2f} ~{final_y:.2f} ~{final_z:.2f} 0 -10 0 0.1 0 force\n")

print(f"已生成 mc.mcfunction 文件，包含 {len(points)} 个粒子点")
print(f"将文件放入数据包 functions 文件夹")
print(f"在游戏中执行 /function {datapack_name}:my_particles 即可显示粒子文字")