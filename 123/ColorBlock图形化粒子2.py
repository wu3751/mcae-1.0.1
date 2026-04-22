from PIL import Image, ImageDraw, ImageFont

# 数据包名称（请根据实际情况修改）
datapack_name = "mcae"
# 文字内容
text = "kali无"
# 字体路径（可替换为本地支持中文的字体文件路径）
font_path = "msyh.ttc"  # 微软雅黑，或系统其他中文字体（如 simhei.ttf 黑体）
font_size = 40  # 字体大小，可调整

# ================== 镜像选项 ==================
# 取消注释其中一行来选择需要的镜像效果：

# 1. 无镜像（原始图像）
# img_flipped = img

# 2. 水平翻转（左右镜像）
#img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

# 3. 垂直翻转（上下镜像）
# img_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)

# 4. 旋转90度
# img_flipped = img.transpose(Image.ROTATE_90)

# 5. 旋转180度
# img_flipped = img.transpose(Image.ROTATE_180)

# 6. 旋转270度
# img_flipped = img.transpose(Image.ROTATE_270)

# 7. 转置（对角线翻转）
# img_flipped = img.transpose(Image.TRANSPOSE)

# 8. 横向转置（另一对角线翻转）
# img_flipped = img.transpose(Image.TRANSVERSE)

# ================== 可自定义配置 ==================
particle_type = "minecraft:end_rod"  # 粒子类型
base_color = (0.8, 0.2, 0.8)  # 基础颜色（RGB，范围 0.0-1.0）
# 其他参数（根据您提供的示例）
param1 = 1   # 颜色后的第一个参数
param2 = 0   # x方向偏移
param3 = 0.1 # y方向偏移
param4 = 0   # z方向偏移
param5 = 0   # 第五个参数
param6 = 0   # 第六个参数
param7 = 0   # 第七个参数
param8 = 1   # 第八个参数
param9 = 0   # 第九个参数
speed_expr = "x,y,cr,cb=t,sin(t),sin(t/7)/5+0.2,sin(t/5)/3-0.6"  # 函数表达式
calc_interval = 1.0  # 计算间隔
group = "null"  # 粒子组名称
# ==================================================

# 创建图像并渲染文字
width = int(font_size * len(text) * 1.5)
height = int(font_size * 1.5)
img = Image.new("L", (width, height), 0)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
draw.text((0, 0), text, 255, font=font)

# 镜像处理（在上面选择需要的镜像效果）
img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
# 提取文字像素点坐标（使用处理后的图像）
points = []
for y in range(img_flipped.height):
    for x in range(img_flipped.width):
        if img_flipped.getpixel((x, y)) > 128:
            # 坐标缩放+Y轴反向，将X坐标映射到Z轴
            scaled_z = -8 + x * 0.08  # X坐标改为Z坐标
            scaled_y = (img_flipped.height - 1 - y) * 0.08
            points.append((scaled_z, scaled_y))

# 生成 particleex 格式的 mcfunction 文件
output_file = "6666.mcfunction"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"# 粒子文字 - 使用 particleex 指令（水平翻转）\n")
    f.write(f"# 粒子类型: {particle_type}\n")
    f.write(f"# 粒子数量: {len(points)} 个粒子点\n\n")

    for pz, py in points:
        # 按照目标格式生成指令，Z坐标作为主要坐标
        pos_x = "~10"  # X坐标固定
        pos_y = f"~{py:.2f}"  # Y坐标
        pos_z = f"~{pz:.2f}"  # Z坐标（原来的X坐标）

        # 生成完整指令（严格按照您提供的格式）
        cmd = (f"particleex normal {particle_type} {pos_x} {pos_y} {pos_z} "
               f"{base_color[0]:.1f} {base_color[1]:.1f} {base_color[2]:.1f} "
               f"{param1} {param2} {param3} {param4} {param5} {param6} {param7} {param8} {param9} "
               f"\"{speed_expr}\" {calc_interval:.1f} {group}\n")
        f.write(cmd)

# 输出提示信息
print(f"✅ 已生成 {output_file} 文件，包含 {len(points)} 个粒子点（水平翻转）")
print(f"📁 使用方法：")
print(f"  1. 将文件放入数据包的 functions 文件夹（路径：{datapack_name}/data/{datapack_name}/functions/）")
print(f"  2. 在游戏中执行指令：/function {datapack_name}:6666")
print(f"🎨 可修改脚本中的参数调整效果")