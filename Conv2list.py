k_w=3
k_h=3
map_w=5
map_h=5
new_map_w=int(((map_w-k_w)/1+1))
new_map_h=int(((map_h-k_h)/1+1))
map = []
map2 = []
map_new = []
for i in range(81):#相当于C++申请堆内存
    map_new.append(i)

for i in range(5):
    line = []
    for j in range(5):
        line.append(i*5+j)

    map2.append(line)

print(map2)
#cv2.imshow("pic",map2)
for i in range(25):#产生一个map
    map.append(i+5)


for k in range(new_map_w):
        for l in range(new_map_h):
            for m in range(k_w):
                for n in range(k_h):
                    #map_new.append(map[k * map_w + l + m *map_w + n])

                    map_new[k * map_w + l + m *map_w + n] = map[k * map_w + l + m *map_w + n]



print(map_new)
