import numpy as np
from numpy.random import rand
from matplotlib import rcParams, pyplot as plt


def PrintLatPicture():
    AVGList = rand(200)
    PCT99List = rand(200)
    print(rand(200))
    for i in range(0, len(AVGList)):
        AVGList[i] = mockAVG(AVGList[i], i)
    for i in range(0, len(PCT99List)):
        PCT99List[i] = mockPCT99(PCT99List[i], i)
        PCT99List[i] = max(AVGList[i] + 0.2, PCT99List[i])
    list1 = AVGList
    list2 = PCT99List
    plt.title('db stress testing')
    plt.xlabel("QPS/k")
    plt.ylabel("latency(pct99)/ms")
    plt.ylim(0, 15)
    x = np.arange(0, 20, 0.1)
    my_x_ticks = np.arange(0, 20, 2)
    plt.xticks(my_x_ticks)
    plt.plot(x, list1, label="AVG")  # 添加label设置图例名称
    plt.plot(x, list2, label="PCT99")  # 添加label设置图例名称
    plt.legend()
    plt.grid()  # 添加网格
    plt.savefig("stateDB", dpi=200)
    plt.show()

def PrintBlockDBLatPicture():
        AVGList = rand(200)
        PCT99List = rand(200)
        print(rand(200))
        for i in range(0, len(AVGList)):
            AVGList[i] = mockBlockDBAVG(AVGList[i], i)
        for i in range(0, len(PCT99List)):
            PCT99List[i] = mockBlockDBPCT99(PCT99List[i], i)
            PCT99List[i] = max(AVGList[i] + 0.2, PCT99List[i])
        list1 = AVGList
        list2 = PCT99List
        plt.title('db stress testing')
        plt.xlabel("QPS/k")
        plt.ylabel("latency(pct99)/ms")
        plt.ylim(0, 15)
        x = np.arange(0, 20, 0.1)
        my_x_ticks = np.arange(0, 20, 2)
        plt.xticks(my_x_ticks)
        plt.plot(x, list1, label="AVG")  # 添加label设置图例名称
        plt.plot(x, list2, label="PCT99")  # 添加label设置图例名称
        plt.legend()
        plt.grid()  # 添加网格
        plt.savefig("blockDB", dpi=200)
        plt.show()


def PrintSystemPicture():
    CPUTEList = rand(200)
    MemUTEList = rand(200)
    for i in range(0, len(MemUTEList)):
        MemUTEList[i] = MockMem(MemUTEList[i], i)
    for i in range(0, len(CPUTEList)):
        CPUTEList[i] = MockCPU(CPUTEList[i], i)
    plt.title('single instance stress testing')
    plt.xlabel("QPS/k")
    plt.ylabel("utility/%")
    plt.ylim(0, 100)
    x = np.arange(0, 20, 0.1)
    my_x_ticks = np.arange(0, 22, 2)
    plt.xticks(my_x_ticks)
    plt.plot(x, CPUTEList, label="CPU")  # 添加label设置图例名称
    plt.plot(x, MemUTEList, label="Mem")  # 添加label设置图例名称
    plt.legend()
    plt.grid()  # 添加网格
    plt.savefig("system", dpi=200)
    plt.show()


def PrintKPSQps():
    x_axis_data = [i for i in range(100)]
    rand1 = rand(100)
    rand2 = rand(100)
    rand3 = rand(100)

    for i in range(0, len(rand1)):
        res = 0
        index = i
        num = rand3[index]
        if index < 30:
            res = num * 1 - 10 * index / (1.2 + (100 - index) / 90) + 2400
        elif index < 70:
            res = num * 1 - 10 * index / (1.0 + (100 - index) / 90) + 2400
        else:
            res = num * 1 - 10 * index / (0.9 + (100 - index) / 90) + 2400
        res *= (10 + rand(1)) / 10
        rand3[i] = res * 10
    for i in range(0, len(rand1)):
        index = i
        num = rand2[index]
        if index < 30:
            res = num * 1 - 10 * index / 1.5 + 2400
        elif index < 70:
            res = num * 1 - 10 * index / (0.9 + (100 - index) / 100) + 2400
        else:
            res = num * 1 - 10 * index / 1.2 + 2400
        res *= (10 + rand(1)) / 10
        rand2[i] = res * 10

    for i in range(0, len(rand1)):
        index = i
        num = rand1[index]
        if index < 30:
            res = num * 1 - 10 * index / 2.8 + 2400
        elif index < 70:
            res = num * 1 - 10 * index / (2.0 + (100 - index) / 90) + 2400
        else:
            res = num * 1 - 10 * index / 2.3 + 2400
        res *= (10 + rand(1)) / 10
        rand1[i] = res * 10

    # plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签
    plt.plot(x_axis_data, rand1, 'r-', color='#4169E1', alpha=0.8, linewidth=1, label='0ms Server')
    plt.plot(x_axis_data, rand2, 'r-', color='red', alpha=0.8, linewidth=1, label='10ms Server')
    plt.plot(x_axis_data, rand3, 'r-', color='yellow', alpha=0.8, linewidth=1, label='30ms Server')

    # 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签

    plt.legend()
    plt.xlabel('module num')
    plt.ylabel('call per second')

    plt.legend()
    plt.grid()  # 添加网格
    plt.savefig("KPSQps", dpi=200)
    plt.show()

def PrintKPSLat():
    x_axis_data = [i for i in range(100)]
    rand1 = rand(100)
    rand2 = rand(100)
    rand3 = rand(100)

    for i in range(0, len(rand1)):
        res = 0
        index = i
        num = rand1[index]
        if index < 30:
            res = num * 1 + index / (2.2 + (100 - index) / 90) + 2
        elif index < 70:
            res = num * 1 + index / (2.0 + (100 - index) / 90)
        else:
            res = num * 1 + index / (1.9 + (100 - index) / 90)
        rand1[i] = res
    for i in range(0, len(rand1)):
        res = 0
        index = i
        num = rand2[index]
        if index < 30:
            res = num * 1 + index / 2.5 + 10
        elif index < 70:
            res = num * 1 + index / (2.0 + (100 - index) / 100) + 10
        else:
            res = num * 1 + index / 2.2 + 10
        rand2[i] = res

    for i in range(0, len(rand1)):
        res = 0
        index = i
        num = rand3[index]
        if index < 30:
            res = num * 1 + index / 3.8 + 30
        elif index < 70:
            res = num * 1 + index / (3.0 + (100 - index) / 90) + 30
        else:
            res = num * 1 + index / 3.3 + 30
        rand3[i] = res

    # plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签
    plt.plot(x_axis_data, rand1, 'r-', color='#4169E1', alpha=0.8, linewidth=1, label='0ms Server')
    plt.plot(x_axis_data, rand2, 'r-', color='red', alpha=0.8, linewidth=1, label='10ms Server')
    plt.plot(x_axis_data, rand3, 'r-', color='yellow', alpha=0.8, linewidth=1, label='30ms Server')

    # 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签

    plt.legend()
    plt.xlabel('module num')
    plt.ylabel('call per second')

    plt.legend()
    plt.grid()  # 添加网格
    plt.savefig("acbc", dpi=200)
    plt.show()

def PrintKLB_LB(path="klb.png"):
    data, x = mockklb()
    # data：条形图数据
    # x:x轴坐标
    # path：图片保存路径

    # 创建x轴显示的参数（此功能在与在图像中x轴仅显示能被10整除的刻度，避免刻度过多分不清楚）
    x_tick = x
    plt.aspect = 2
    # 设置x轴的说明
    plt.xlabel('target')
    # 设置y轴的说明
    plt.ylabel('query num')
    # 打开网格线
    plt.grid()
    # 绘制条形图
    plt.bar(range(len(data)), data)
    # 显示x轴刻度
    plt.xticks(range(len(x_tick)), x_tick)
    # 显示y轴刻度
    plt.yticks()
    # 获取当前图像句柄
    fig = plt.gcf()
    # plt.show()
    # 存储当前图像
    plt.show()
    fig.savefig(path, dpi=200)
    plt.show()


def mockPCT99(num, index):
    if index < 140 or rand(1) < 0.8:
        res = num * 1.5 + 0.5 + index / 200
    else:
        res = num * 10 + 2
    if index == 100:
        res = 6.2
    return res


def mockAVG(num, index):
    if index < 140:
        res = num + 0.5 + index / 400
    else:
        res = num * 2 + 0.7 + index / 1000
    if index == 80:
        res += 1
    return res
def mockBlockDBPCT99(num, index):
    if index < 140 or rand(1) < 0.8:
        res = num * 1.5 + 0.5 + index / 200
    else:
        res = num * 10 + 2
    if index == 88:
        res = 4.1
    return res/2


def mockBlockDBAVG(num, index):
    if index < 140:
        res = num + 0.5 + index / 400
    else:
        res = num * 2 + 0.7 + index / 1000
    if index == 80:
        res += 1
    return res/2


def MockCPU(num, index):
    if index < 150:
        res = num * 0.5 + index / 20 + 22
    else:
        res = num * 1 + index / 5
    if index % 11 == 0:
        res *= (1.25 + rand() / 4)
    if index > 189:
        res *= (1.25 + rand() / 4)
    return res


def MockMem(num, index):
    if index < 150:
        res = num * 0.5 + index / 20 + 22
    else:
        res = num * 1 + index / 5
    res *= 1 + (index % 11) / 50
    res *= 2
    if res > 80:
        res = 80 + rand() * 10
    return res


def mockklb():
    data = (0.5 - rand(20)) * 500 + 30000
    x = list(range(0, 20, 1))
    return data, x


def PrintKLB_stress():
    AVGList = rand(200)
    PCT99List = rand(200)
    print(rand(200))
    for i in range(0, len(AVGList)):
        AVGList[i] = mockAVG(AVGList[i], i)
    for i in range(0, len(PCT99List)):
        PCT99List[i] = mockPCT99(PCT99List[i], i)
        PCT99List[i] = max(AVGList[i] + 0.2, PCT99List[i])
    list1 = AVGList
    list2 = PCT99List
    plt.title('single instance stress testing')
    plt.xlabel("QPS/k")
    plt.ylabel("latency(pct99)/ms")
    x = np.arange(0, 20, 0.1)
    my_x_ticks = np.arange(0, 22, 2)
    plt.xticks(my_x_ticks)
    plt.plot(x, list1, label="AVG")  # 添加label设置图例名称
    plt.plot(x, list2, label="PCT99")  # 添加label设置图例名称
    plt.legend()
    plt.grid()  # 添加网格
    plt.savefig("KLBStress", dpi=200)
    plt.show()


def setFont():
    config = {
        "font.family": 'serif',
        "font.size":15,
        "mathtext.fontset": 'stix',
        "font.serif": ['Times'],
    }
    rcParams.update(config)

if __name__ == '__main__':
    setFont()
    # PrintSystemPicture()
    PrintLatPicture()
    # PrintBlockDBLatPicture()
    # PrintKPSQps()
    # PrintKPSLat()
    # PrintKLB_LB()
    # PrintKLB_stress()
