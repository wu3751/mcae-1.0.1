#利用python在MC中打印粒子图像
#长宽建议：300 * 300
from PIL import Image
im:Image.Image = Image.open("in/666.png")
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
#print(valid_width, valid_height)

for i in range(len(points)):
    points[i] = (
        points[i][0] - min_x - valid_width // 2,
        points[i][1] - min_y - valid_height // 2,
    )


def convert_to_mc_command(x, y):
    speed_scale = 0.01  # 运动速度
# 展开
    # 水平
    #command = 'particle minecraft:end_rod 0 5.5 0 {0} 0 {1} {2} 0 force'.format(x, y, speed_scale)
    # 竖立
    command = 'particle minecraft:end_rod 0 18 0 {0} {1} 0 {2} 0 force'.format(x,y,speed_scale)
    # 倾斜
    #command = 'particle minecraft:end_rod 0 4.5 0 {0} {1} {2} {3} 0 force'.format(x, y, y, speed_scale)
# 收拢
    # 水平
    #command = 'particle minecraft:end_rod ~{0} ~ ~{1} {3} 0 {4} {2} 0 force'.format(x / 3, y / 3, speed_scale, -x * 2.5, -y * 2.5)
    # 竖立
    #command = 'particle minecraft:end_rod {0} {1} 39 {3} {4} 0 {2} 0 force'.format(x / 3 +9, y / 3 + 5 +30, speed_scale, -x * 2.5, -y * 2.5)
    # 倾斜
    #command = 'particle minecraft:end_rod ~{0} ~{1} ~{2} {3} {4} {5} {6} 0 force'.format(x / 2, y / 2 + 5, y / 2, -x * 4.1, -y * 4.1, -y * 4.1, speed_scale)

    #自定义

    #command = 'particle minecraft:end_rod 62 38 33 {0} 0 {1} {2} 0 force'.format(x * 10, y * 10, speed_scale)  #展开 水平
    #command = 'particle minecraft:end_rod 66 18 25 0 {1} {0} {2} 0 force'.format(x * 1, y * 1, speed_scale)  # 竖立 展开
    #command = 'particle minecraft:end_rod 0 18 0 {0} 0 {1} {2} 0 force'.format(x *15, y *15, speed_scale)  #展开 水平 max
    #command = 'particle minecraft:end_rod {0} 107 {1} 0 75 0 {2} 0 force'.format(x /15 +1588, y /15 +2135, speed_scale)  #上升
    #command = 'particle minecraft:end_rod {0} 10 {1} 0 5 0 0.4 0 force'.format(x / 10 + 68, y / 10 + 27)  # 静止
    #command = 'particle minecraft:end_rod 8 30 35 {0} {1} 0 {2} 0 force'.format(x * 5, y * 5, speed_scale)
    return command
# 输出§
with open('test_1_last2.mcfunction', 'w') as f:
    print('{0} partlces'.format(len(points)))
    for point in points:
        mcc_command = convert_to_mc_command(point[0], point[1])
        f.write(mcc_command + '\n')
