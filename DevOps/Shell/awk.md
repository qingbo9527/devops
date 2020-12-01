[TOC]

#### 一、awk 分隔符

* 输入分隔符

  ```bash
  [root@localhost ~]# cat test
  abc#123#idu#ddd
  8ua#456#auv#ppp#7v7
  [root@localhost ~]# awk -F# '{print $1,$2}' test
  abc 123
  8ua 456
  上例中，我们使用了-F 选项，指定了使用#号作为输入分隔符，于是，awk将每一行都通过#号为我们分割了。
  ```

* 输出分隔符

  ``` bash
  1. 输出分割符的意思就是：当我们要对处理完的文本进行输出的时候，以什么文本或符号作为分隔符。
  [root@localhost ~]# cat test
  abc#123#idu#ddd
  8ua#456#auv#ppp#7v7
  [root@localhost ~]# awk -F# '{print $1,$2}' test
  abc 123
  8ua 456
  2. 上例中，abc 123之间的空格就是awk默认的输出分隔符
  3. 我们可以使用awk的内置变量OFS来设定awk的输出分隔符，当然，使用变量的时候要配合使用-v选项，示例如下:
  [root@localhost ~]# cat test
  abc 123 idu ddd
  8ua 456 auv ppp 7v7
  [root@localhost ~]# awk -v OFS='+++' '{print $1,$2}' test
  abc+++123
  8ua+++456
  4. 同时指定输入分隔符和输出分割符了，示例如下
  [root@localhost ~]# cat test1
  abc#123#iuy#ddd
  8ua#455#auv#ppp#7y7
  [root@localhost ~]# awk -v FS='#' -v OFS='----' '{print $1,$2}' test1
  abc----123
  8ua----455
  5. 如果，在输出的时候，我们想要让两列合并在一起显示，不使用输出分隔符分开显示，该怎么做呢？如下所示
  [root@localhost ~]# awk '{print $1,$2}' test
  abc 123
  8ua 456
  [root@localhost ~]# awk '{print $1 $2}' test
  abc123
  8ua456
  ps：上面示例在语法上的区别就是，一个有"逗号"，一个没有"逗号"。
  ```

#### 二、awk变量

* 内置变量

  * NR、NF

  ```bash
  内置变量NR表示每一行的行号，内置变量NF表示每一行中一共有几列，示例
  [root@localhost ~]# cat test
  abc 123 idu ddd
  8ua 456 auv ppp 7v7
  [root@localhost ~]# awk '{print NR,NF}' test
  1 4
  2 5
  [root@localhost ~]# awk '{print NR,$0}' test
  1 abc 123 idu ddd
  2 8ua 456 auv ppp 7v7
  ```

  * FNR

  ```bash
  [root@localhost ~]# awk '{print NR,$0}' test test1
  1 abc 123 idu ddd
  2 8ua 456 auv ppp 7v7
  3 abc#123#iuy#ddd
  4 8ua#455#auv#ppp#7y7
  [root@localhost ~]# awk '{print FNR,$0}' test test1
  1 abc 123 idu ddd
  2 8ua 456 auv ppp 7v7
  1 abc#123#iuy#ddd
  2 8ua#455#auv#ppp#7y7
  ## FNR的作用就是当awk处理多个文件时，分别对每个文件的行数进行计数
  ```

  * RS 输入行分隔符

  ```bash
  [root@localhost ~]# awk '{print NR,$0}' test
  1 abc 123 idu ddd
  2 8ua 456 auv ppp 7v7
  [root@localhost ~]# awk -v RS=" " '{print NR,$0}' test
  1 abc
  2 123
  3 idu
  4 ddd
  8ua
  5 456
  6 auv
  7 ppp
  8 7v7
  ```

  * ORS 输出行分隔符

  ```bash
  [root@localhost ~]# awk -v ORS="+++" '{print NR, $0}' test
  1 abc 123 idu ddd+++2 8ua 456 auv ppp 7v7+++[root@localhost ~]#
  ```

  ```bash
  [root@localhost ~]# awk -v RS=" " -v ORS="+++" '{print NR, $0}' test
  1 abc+++2 123+++3 idu+++4 ddd
  8ua+++5 456+++6 auv+++7 ppp+++8 7v7
  +++[root@localhost ~]#
  ```

  * FILENAME 

  ```bash
  [root@localhost ~]# awk '{print FILENAME, FNR, $0}' test test1
  test 1 abc 123 idu ddd
  test 2 8ua 456 auv ppp 7v7
  test1 1 abc#123#iuy#ddd
  test1 2 8ua#455#auv#ppp#7y7
  ```

  * ARGC、ARGV

* 自定义变量

  * 方法一：-v varname=value

  ```bash
  [root@localhost ~]# awk -v myVar='testVar' 'BEGIN{print myVar}'
  testVar
  [root@localhost ~]# abc=666666
  [root@localhost ~]# awk -v myvar=$abc 'BEGIN{print myvar}'
  666666
  ```

  * 方法二：在program中直接定义

  ```bash
  注意，变量定义与动作之间需要用分号";"隔开
  [root@localhost ~]# awk 'BEGIN{ myvar="ttt" ; print myvar }'
  ttt
  ```

#### 三、printf命令

* printf "指定的格式" "文本1" "文本2" "文本3"…...

```bash
[root@localhost ~]# printf "%s\n" abc def ghi jkl mno
abc
def
ghi
jkl
mno
[root@localhost ~]# printf "灵宠名称 体温\n"; printf "%-10s %-12d \n" 烈火兽 180 冰晶兽 -70
灵宠名称 体温
烈火兽  180
冰晶兽  -70在awk中使用printf动作时，需要注意以下3点
```

* 在awk中使用printf动作时，需要注意以下3点

  * 使用printf动作输出的文本不会换行，如果需要换行，可以在对应的"格式替换符"后加入"\n"进行转义
  * 使用printf动作时，"指定的格式" 与 "被格式化的文本" 之间，需要用"逗号"隔开
  * 使用printf动作时，"格式"中的"格式替换符"必须与 "被格式化的文本" 一一对应

  ```bash
  [root@localhost ~]# cat test
  abc 123 idu ddd
  8ua 456 auv ppp 7v7
  [root@localhost ~]# awk '{printf "第一列：%s 第二列：%s\n" , $1,$2}' test
  第一列：abc 第二列：123
  第一列：8ua 第二列：456
  ## 利用awk的内置变量FS，指定输入字段分隔符，然后再利用printf动作，进行格式化，示例如下:
  [root@localhost ~]# cat test1
  abc#123#iuy#ddd
  8ua#455#auv#ppp#7y7
  [root@localhost ~]# awk -v FS="#" '{printf "第一列：%s\t 第二列：%s\n" , $1,$2}' test1
  第一列：abc	 第二列：123
  第一列：8ua	 第二列：455
  [root@localhost etc]# awk -v FS=":" 'BEGIN{printf "%-10s\t %s\n" , "用户名称","用户ID"} {printf "%-10s\t %s\n" , $1,$3}' /etc/passwd
  用户名称      	 用户ID
  root      	 0
  bin       	 1
  daemon    	 2
  adm       	 3
  lp        	 4
  sync      	 5
  shutdown  	 6
  halt      	 7
  mail      	 8
  ```

#### 四、awk模式（Pattern）之一

* 当awk进行逐行处理的时候，会把pattern（模式）作为条件，			  			 判断将要被处理的行是否满足条件，是否能跟"模式"进行匹配，如果匹配，则处理，如果不匹配，则不进行处理。

  * 示例：

    ```bash
    root@www ~]# cat test
    abc 123 idu ddd
    8ua 456 auv ppp 7v7
    123 666
    [root@www ~]# awk 'NF==5 {print $0}' test
    8ua 456 auv ppp 7v7
    [root@www ~]# awk 'NF>2 {print $0}' test
    abc 123 idu ddd
    8ua 456 auv ppp 7v7
    [root@www ~]# awk 'NF<=4 {print $0}' test
    abc 123 idu ddd
    123 666
    [root@www ~]# awk '$1==123 {print $0}' test
    123 666
    ```

  * 空模式、关系表达式模式、BEGIN模式、END模式

    ```bash
    [root@www ~]# awk 'BEGIN{print "aaa","bbb"} {print $1,$2} END{print "ccc","ddd"}' test
    aaa bbb
    abc 123
    8ua 456
    123 666
    ccc ddd
    ```

  * 正则模式

  * 行范围模式

    ```Bash
    [root@qingbo ~]# cat -n test4
         1	Allen Phillips
         2	Green Lee
         3	William Aiden James Lee
         4	Angel Jack
         5	Tyler Kevin
         6	Lucas Thomas
         7	Kevin
    ## 找出从Lee第一次出现的行，到Kevin第一次出现的行之间的所有行
    [root@qingbo ~]# awk '/Lee/,/Kevin/{print $0}' test4
    Green Lee
    William Aiden James Lee
    Angel Jack
    Tyler Kevin
    awk '/正则1/,/正则2/{动作}' /some/file
    ## 打印出从第3行到第6行之间的所有行
    [root@qingbo ~]# awk 'NR>=3 && NR<=6 {print $0}' test4
    William Aiden James Lee
    Angel Jack
    Tyler Kevin
    Lucas Thomas
    ## 如下文本中找出，网卡1的IP地址在192.168.0.0/16网段内的主机:
    [root@qingbo ~]# cat test5
    主机名  网卡1的IP				网卡2的IP
    主机A   192.168.1.123		   192.168.1.124
    主机B   192.168.2.222		   172.16.100.2
    主机C   10.1.0.1		       172.16.100.3
    主机D   10.1.2.1		       192.168.1.60
    主机E   10.1.5.1		       172.16.100.5
    主机F   192.168.1.234		   172.16.100.6
    主机G   10.1.7.1		       172.16.100.7
    [root@qingbo ~]# awk --posix '$2~/192\.168\.[0-9]{1,3}\.[0-9]{1,3}/{print $1,$2}' test5
    主机A 192.168.1.123
    主机B 192.168.2.222
    主机F 192.168.1.234
    ```

#### 五、awk 动作

* 动作总结

  ```bash
  判断出/etc/passwd文件中的哪些用户属于系统用户，哪些用户属于普通用户
  # awk -F ":" '{ if($3<1000) { print $1 "系统用户" } else{ print $1 "普通用户" } }' /etc/passwd

  ```

  * 循环控制语句

    ```bash
    #for循环语法格式1
    for(初始化; 布尔表达式; 更新) {
    //代码语句
    }
     
    #for循环语法格式2
    for(变量 in 数组) {
    //代码语句
    }
     
    #while循环语法
    while( 布尔表达式 ) {
    //代码语句
    }
     
    #do...while循环语法
    do {
    //代码语句
    }while(条件)
    [root@www ~]# awk 'BEGIN{i=1; do{print "test";i++}while(i<1)}'
    test
    [root@www ~]# awk 'BEGIN{ do{print "test";i++}while(i<5)}'
    test
    test
    test
    test
    test
    [root@www ~]# awk 'BEGIN{ for(i=0;i<6;i++){print i}}'
    0
    1
    2
    3
    4
    5
    [root@www ~]# awk 'BEGIN{ for(i=0;i<6;i++){ if(i==3){continue} ;print i}}'
    0
    1
    2
    4
    5
    [root@www ~]# awk 'BEGIN{ for(i=0;i<6;i++){ if(i==3){break} ;print i}}'
    0
    1
    2
    ```

    ​









