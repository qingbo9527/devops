* awk 分隔符

  * 输入分隔符

    ```
    [root@localhost ~]# cat test
    abc#123#idu#ddd
    8ua#456#auv#ppp#7v7
    [root@localhost ~]# awk -F# '{print $1,$2}' test
    abc 123
    8ua 456
    上例中，我们使用了-F 选项，指定了使用#号作为输入分隔符，于是，awk将每一行都通过#号为我们分割了。
    ```

  * 输出分隔符

    ``` 
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

* awk变量

  * 内置变量

    * NR、NF

    ```
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

    ```
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

    ```
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

    ```
    [root@localhost ~]# awk -v ORS="+++" '{print NR, $0}' test
    1 abc 123 idu ddd+++2 8ua 456 auv ppp 7v7+++[root@localhost ~]#
    ```

    ```
    [root@localhost ~]# awk -v RS=" " -v ORS="+++" '{print NR, $0}' test
    1 abc+++2 123+++3 idu+++4 ddd
    8ua+++5 456+++6 auv+++7 ppp+++8 7v7
    +++[root@localhost ~]#
    ```

    * FILENAME 

    ```
    [root@localhost ~]# awk '{print FILENAME, FNR, $0}' test test1
    test 1 abc 123 idu ddd
    test 2 8ua 456 auv ppp 7v7
    test1 1 abc#123#iuy#ddd
    test1 2 8ua#455#auv#ppp#7y7
    ```

    * ARGC、ARGV

  * 自定义变量

    * 方法一：-v varname=value

    ```
    [root@localhost ~]# awk -v myVar='testVar' 'BEGIN{print myVar}'
    testVar
    [root@localhost ~]# abc=666666
    [root@localhost ~]# awk -v myvar=$abc 'BEGIN{print myvar}'
    666666
    ```

    * 方法二：在program中直接定义

    ```
    注意，变量定义与动作之间需要用分号";"隔开
    [root@localhost ~]# awk 'BEGIN{ myvar="ttt" ; print myvar }'
    ttt
    ```

  * printf命令

    * printf "指定的格式" "文本1" "文本2" "文本3"…...

    ```
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

    ```
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

  * s



