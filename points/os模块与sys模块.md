#sys模块
##sys模块主要是用于提供对python解释器相关的操作

函数

- sys.argv #命令行参数List，第一个元素是程序本身路径
- sys.path #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
- sys.modules.keys() #返回所有已经导入的模块列表
- sys.modules #返回系统导入的模块字段，key是模块名，value是模块
- sys.exc_info() #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
- sys.exit(n) #退出程序，正常退出时exit(0)
- sys.hexversion #获取Python解释程序的版本值，16进制格式如：0x020403F0
- sys.version #获取Python解释程序的版本信息
- sys.platform #返回操作系统平台名称
- sys.maxint # 最大的Int值
- sys.stdout #标准输出
- sys.stdout.write('aaa') #标准输出内容
- sys.stdout.writelines() #无换行输出
- sys.stdin #标准输入
- sys.stdin.read() #输入一行
- sys.stderr #错误输出
- sys.exc_clear() #用来清除当前线程所出现的当前的或最近的错误信息
- sys.exec_prefix #返回平台独立的python文件安装的位置
- sys.byteorder #本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
- sys.copyright #记录python版权相关的东西
- sys.api_version #解释器的C的API版本
- sys.version_info #'final'表示最终,也有'candidate'表示候选，表示版本级别，是否有后继的发行
- sys.getdefaultencoding() #返回当前你所用的默认的字符编码格式
- sys.getfilesystemencoding() #返回将Unicode文件名转换成系统文件名的编码的名字
- sys.builtin_module_names #Python解释器导入的内建模块列表
- sys.executable #Python解释程序路径
- sys.getwindowsversion() #获取Windows的版本
- sys.stdin.readline() #从标准输入读一行，sys.stdout.write(a) 屏幕输出a
- sys.setdefaultencoding(name) #用来设置当前默认的字符编码(详细使用参考文档)
- sys.displayhook(value) #如果value非空，这个函数会把他输出到sys.stdout(详细使用参考文档)

#os模块
##OS模块是Python标准库中的一个用于访问操作系统功能的模块，使用OS模块中提供的接口，可以实现跨平台访问

用于提供系统级别的操作

- os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
- os.chdir(dirname) 改变当前脚本工作目录；相当于shell下cd
- os.curdir 返回当前目录: ('.')
- os.pardir 获取当前目录的父目录字符串名：('..')
- os.makedirs('dir1/dir2') 可生成多层递归目录
- os.removedirs('dirname1') 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
- os.mkdir('dirname') 生成单级目录；相当于shell中mkdir dirname
- os.rmdir('dirname') 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
- os.listdir('dirname') 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
- os.remove() 删除一个文件
- os.rename(oldname,new) 重命名文件/目录
- os.stat('path/filename') 获取文件/目录信息
- os.sep 操作系统特定的路径分隔符，win下为\,Linux下为/
- os.linesep 当前平台使用的行终止符，win下为\t\n,Linux下为\n
- os.pathsep 用于分割文件路径的字符串
- os.name 字符串指示当前使用平台。win->'nt'; Linux->'posix'
- os.system(bash command) 运行shell命令，直接显示
- os.environ 获取系统环境变量
- os.path.abspath(path) 返回path规范化的绝对路径
- os.path.split(path) 将path分割成目录和文件名二元组返回
- os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
- os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
- os.path.exists(path) 如果path存在，返回True；如果path不存在，返回False
- os.path.lexists  #路径存在则返回True,路径损坏也返回True
- os.path.isabs(path) 如果path是绝对路径，返回True
- os.path.isfile(path) 如果path是一个存在的文件，返回True。否则返回False
- os.path.isdir(path) 如果path是一个存在的目录，则返回True。否则返回False
- os.path.join(path1[, path2[, ...]]) 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
- os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间
- os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间
- os.path.commonprefix(list) #返回list(多个路径)中，所有path共有的最长的路径。
- os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
- os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”
- os.access('pathfile',os.W_OK) 检验文件权限模式，输出True，False
- os.chmod('pathfile',os.W_OK) 改变文件权限模式