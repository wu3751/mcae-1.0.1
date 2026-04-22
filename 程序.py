#利用python在MC中打印粒子图像
#长宽建议：300 * 300
from PIL import Image
im:Image.Image = Image.open("Minecraft_OCEAN.png")
im_gray = im.convert('L')
im.close()

points = []
threshold = 128
for y in range(im_gray.height):
    for x in range(im_gray.width):
        if im_gray.getpixel((x, y)) < threshold:
            points.append((x, (im_gray.height - y - 1)))
min_x = 1000000
min_y = 1000000
max_x = -1000000
max_y = -1000000
for point in points:
    min_x = min(point[0], min_x)
    min_y = min(point[1], min_y)
    max_x = max(point[0], max_x)
    max_y = max(point[1], max_y)

valid_width = max_x - min_x
valid_height = max_y - min_y
# print(valid_width, valid_height)

for i in range(len(points)):
    points[i] = (
        points[i][0] - min_x - valid_width // 2,
        points[i][1] - min_y - valid_height // 2,
    )
def convert_to_mc_command(x, y):
    speed_scale = 0.01  # 运动速度

# 向外展开___
    # 水平
    #command = 'particle minecraft:end_rod 28 5 24 {0} 0 {1} {2} 0 force'.format(x, y, speed_scale)
    # 竖立
    #command = 'particle minecraft:end_rod 0 20 5 {0} {1} 0 {2} 0 force'.format(x,y,speed_scale)
    # 倾斜
    # command = 'particle minecraft:end_rod 0 30 0 {0} {1} {2} {3} 0 force'.format(x, y*-1, y, speed_scale + 0.02)

    # 向内收拢____?
    #command = 'particle minecraft:end_rod ~{0} ~{1} ~ {3} {4} 0 {2} 0 force'.format(x / 3, y / 3 + 1.7, speed_scale, -x * 2.5, -y * 2.5)

    #向内收拢——间距
    command = 'particle minecraft:end_rod ~{0} ~{1} ~ {2} {3} 0 {4} 0 force'.format(x / 1, y / 1 + 2.5, -x * 8.5, -y * 8.5, speed_scale)
    # 上升
    #command = 'particle minecraft:end_rod ~{0} ~{1} ~1 0 15 0 0.1 0 force'.format(x/10, y/10 - 5)
    # 平移
    # command = 'particle minecraft:end_rod {0} {1} 0 0 0 3 0.5 0 force'.format(x/10, y/10 + 20)

    # 自定义动画
    # command = 'particle minecraft:end_rod {0} {1} 0 0 0 0 0 0 force'.format(x/7,y/7 + 15)
    #command = 'particle minecraft:end_rod 0 22 0 {0} 0 {1} {2} 0 force'.format(x, y, speed_scale + 0.1)
    #command = 'particle minecraft:end_rod ~{0} ~{1} ~ 0 0 0 0.1 0 force'.format(x / 10, y / 10)
    return command

# 输出§
with open('./mc.mcfunction', 'w') as f:
    print('{0} partlces'.format(len(points)))
    for point in points:
        mcc_command = convert_to_mc_command(point[0], point[1])
        f.write(mcc_command + '\n')
