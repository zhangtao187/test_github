import psutil
print('--------------内存----------------')
mem=psutil.virtual_memory();
print('获取内存完整信息：', mem)
print('获取内存总数：', mem.total/(1024*1024*1024),'G')
print('获取内存空闲总数：', mem.free/(1024*1024*1024),'G')
print('获取swap分区的内存信息：', psutil.swap_memory())
print('-----------磁盘信息----------------')
print('获取磁盘完整信息:', psutil.disk_partitions())
print('获取分区的使用情况:', psutil.disk_usage('/'))
print('获取硬盘总的IO个数、读写信息：', psutil.disk_io_counters())
print('获取单个分区IO个数:', psutil.disk_io_counters(perdisk=True))
print('--------------网络信息--------------')
print('获取网络总的IO信息:', psutil.net_io_counters())
print('输出每个网络接口的IO信息', psutil.net_io_counters(pernic=True))
print('----------------其它信息-------------')
print('获取当前登陆系统的用户信息:', psutil.users())
print('获取开机时间:', psutil.boot_time())
print("------------------进程信息--------------")
plist=psutil.pids()
print('进程名     进程bin路径   进程工作目录绝对路径 进程状态  进程内存利用率  进程内存rss vms信息 进程开启的线程数')
for p in plist:
    ps=psutil.Process(p);
    if ps.name() == 'java':
       print(ps.name()+' '+ps.exe()+' '+ps.cwd()+' '+ps.status()+' '+str(ps.memory_percent())+' '+str(ps.memory_info())+' '+str(ps.num_threads()))