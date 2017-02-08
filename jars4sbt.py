# encoding: utf-8
import os,sys
import subprocess
import time

"""
起因：利用sbt开发scala项目时，有一些包下载速度很慢甚至无法下载
解决方法：在国外VPS把项目sbt console好，然后将项目需要的包，传到本地即可(scp/axel)
脚本放在~/.ivy2/目录下
python3 jars4sbt.py %Y-%m-%d-%H-%M
如python3 jars4sbt.py 2017-02-08-12-00
即为选取2017-02-08 12:00之后的更新文件并压缩
"""
cache_new = "cache_" + sys.argv[1]
if os.path.exists(cache_new):
    subprocess.call(["rm", "-rf",cache_new])
subprocess.call(["cp","-r","cache",cache_new])
update_time = time.mktime(time.strptime(sys.argv[1],'%Y-%m-%d-%H-%M'))
for root,dirs,files in os.walk("cache"):
    if os.path.exists(root):
        for d in dirs:
            if os.path.getctime(os.path.join(root,d)) < update_time:
                subprocess.call(["rm", "-rf",os.path.join(root.replace("cache",cache_new),d)])
        for f in files:
            if os.path.getctime(os.path.join(root, f)) < update_time:
                subprocess.call(["rm", "-rf", os.path.join(root.replace("cache",cache_new), f)])
subprocess.call(["tar", "czvf",cache_new + ".tar.gz", cache_new])
