[TOC]

### shell命令

#### 两种组合命令方法

* 目前有两个目录，这两个目录分别为/test1和/test2，目录中分别存在如下文件

  ```
  [root@localhost ~]# ls tes1 tes2
  tes1:
  t1  t2  t3

  tes2:
  t1
  ```

* 两种方法示例如下

  ```
  [root@localhost ~]# (ls tes1; ls tes2) | wc -l
  4
  [root@localhost ~]# { ls tes1; ls tes2; } | wc -l;
  4
  ps：大括号内的所有命令都用空格隔开了，而且大括号内的每个命令都必须以分号";"结尾，即使是大括号内的最后一个命令，也需要以分号结尾，而且需要用空格与大括号隔开。
  ```


* [] 与[[]] 的区别

  * 场景一：判断变量是否为空

    * test命令判断一个字符串是否为空，test命令为我们提供了"-z选项"与"-n选项"，使用这两个选项可以判断字符串是否为空。

      "-z选项"可以判断指定的字符串是否为空，为空则返回真，非空则返回假，-z可以理解为zero

      "-n选项"可以判断指定的字符串是否为空，非空则返回真，为空则返回假，-n可以理解为nozero

    * 示例如下

      ```
      [root@localhost ~]# test -n $b
      [root@localhost ~]# echo $?
      0
      上例中，变量b的值为空，按照正常的逻辑来说，使用test -n 命令判断变量b的值是否为空时，应该返回假，因为test命令的-n选项表示指定的字符串非空时，返回真，为空时，返回假，但是上例中，'test -n $b' 这条命令的返回值却为真（应该为假），这是明显不正确的，所以，为了防止上述情况的发生，在使用test命令的-n选项判断变量的值是否为空时，需要在变量的外侧加上"双引号"，示例如下
      [root@localhost ~]# test -n "$b"
      [root@localhost ~]# echo $?
      1
      ```

    * 在Linux中，"[ ]"与"test命令"是等效的，比如，我们也可以使用"-n"或者"-z"结合"[ ]"去判断变量是否为空

      ``````
      [root@localhost ~]# a=abc
      [root@localhost ~]# echo $a
      abc
      [root@localhost ~]# echo $b

      [root@localhost ~]# [ -n "$a" ]
      [root@localhost ~]# echo $?
      0
      [root@localhost ~]# [ -n "$b" ]
      [root@localhost ~]# echo $?
      1
      ``````

    * 根据上例中的结果可以看出，当"[ ]"中使用"-n"或者"-z"这些选项判断变量是否为空时，必须在变量的外侧加上双引号，才更加保险，与"test命令"的使用方法相同。不过，使用"[[ ]]"时则不用考虑这样的问题，示例如下

      ```

      ```

  * 创建多个目录

    ```
    [root@localhost conf.d]# mkdir -p /qingbo_code/centos/centos{1..10}
    [root@localhost conf.d]# ls /qingbo_code/centos/
    centos1  centos10  centos2  centos3  centos4  centos5  centos6  centos7  centos8  centos9
    ```

  截取变量

  * 掐头去尾截取之掐头

    ```
    [root@www init.d]# webside=www.qingbo.com
    [root@www init.d]# echo ${webside}
    www.qingbo.com
    [root@www init.d]# echo ${webside#*.}
    qingbo.com
    ## 使用"#*."即可删除字符串中从左向右数第一个 "." 以及其左侧的全部字符，这就是所谓"掐头去尾"中的掐头，准确的说，应该是掐去头部，截取尾部，将"."换成其它字符也同样适用，示例：
    [root@www ~]# teststr=bbAccAddAeeA
    [root@www ~]# echo ${teststr}
    bbAccAddAeeA
    [root@www ~]# echo ${teststr#*A}
    ccAddAeeA
    "##*."表示删除字符串中从左向右最后一个遇到的 "." ，以及其左侧的字符
    [root@www ~]# echo ${webside}
    www.qingbo.com
    [root@www ~]# echo ${webside##*.}
    com
    其它字符也适用
    [root@www ~]# testpath="/usr/local/nginx/conf.d"
    [root@www ~]# echo ${testpath##*/}
    conf.d
    ```

  * 掐头去尾截取之去尾

    ```
    [root@www ~]# testpath="/usr/local/nginx/conf.d"
    [root@www ~]# echo ${testpath%/*}
    /usr/local/nginx
    "%/*"表示删除字符串中从右向左第一个遇到的 "/" ，以及其右侧的字符
    将"/"换成其它字符，示例如下：
    [root@www ~]# website="www.qingbo.com.cn"
    [root@www ~]# echo ${website%.*}
    www.qingbo.com
    [root@www yum.repos.d]# website="https://www.qingbo.com/index.html"
    [root@www yum.repos.d]# echo ${website}
    https://www.qingbo.com/index.html
    [root@www yum.repos.d]# echo ${#website}
    33
    [root@www yum.repos.d]# echo ${website%/*}
    https://www.qingbo.com
    [root@www yum.repos.d]# echo ${website%%/*}
    https:
    上例中，"%%/*"表示删除字符串中从右向左最后一个遇到的 "/" ，以及其右侧的字符。
    换句话说，从右向左最后一个遇到的 "/" 以及其右侧的字符都被当做"尾部"去掉了。
    ```

#### 日期时间

* date

  * 获取到2020年12月31日的unix时间戳

    ```
    # date -d 2020-12-31 +%s
    1609344000
    ```

  * 将unix时间戳改为正常日期格式

    ```
    # date --date='@1609344000'
    2020年 12月 31日 星期四 00:00:00 CST
    ```

#### 替换变量中的字符串

* 替换字符串

  * 把字符串"www.qingbo.com"中的"www"替换成"linux"

    ```
    [root@www yum.repos.d]# echo ${websit}
    www.qingbo.com
    [root@www yum.repos.d]# echo ${websit/www/linux}
    linux.qingbo.com
    ```

  * 多处替换

    ```
    [root@www yum.repos.d]# teststr="www.abc.www.def"
    [root@www yum.repos.d]# echo ${teststr//www/linux}
    linux.abc.linux.def
    ```

  * 针对行首字符串替换

    ```
    [root@www yum.repos.d]# teststr="www.abc.www"
    [root@www yum.repos.d]# echo ${teststr}
    www.abc.www
    [root@www yum.repos.d]# echo ${teststr/#www/linux}
    linux.abc.www
    ```

  * 针对行尾字符串替换

    ```
    [root@www yum.repos.d]# echo ${teststr/%www/linux}
    www.abc.linux
    ```

#### 删除变量中的字符串

* 将替换字符串语法中的替换部分省略即是删除

  ```
  [root@www yum.repos.d]# echo ${teststr/%www/linux}
  www.abc.linux
  [root@www yum.repos.d]# echo ${teststr/.}
  wwwabc.www
  ```

  * 刚才的示例中，我们只删除了字符串中的第一个"."  ，如果我们想要删除字符串中的所有的"." ，则可以使用如下语法

    ```
    [root@www yum.repos.d]# echo ${teststr//.}
    wwwabcwww
    ```

  * 删除行首的某个字符串或者删除行尾的某个字符串的方法如下

    ```
    [root@www yum.repos.d]# test="www.abc.def.www"
    [root@www yum.repos.d]# echo ${test/#www}
    .abc.def.www
    [root@www yum.repos.d]# echo ${test/%www}
    www.abc.def.
    ```

* 特殊情况

  * 如果，我们要删除字符串"/usr/local/chroot/usr/local"中第一个遇到的"/usr"，该怎么办呢？

    ```
    # teststr="/usr/local/chroot/usr/local/nginx"
    # echo ${teststr//usr}
    //local/chroot//local/nginx
    # 上例按正常情况会把所有的"/usr"都删除掉，这时需要用转义符
    对"/"进行转义
    # echo ${teststr/\/usr}
    /local/chroot/usr/local/nginx
    ```

  * 下例表示删除字符串中行尾的"H"

    ```
    # teststr="H.H.H.H.H.H"
    # echo ${teststr/%H}
    H.H.H.H.H.
    ```

  * 下例表示删除字符串行尾的"%"

    ```
    # teststr="abc%def%linux%"
    # echo ${teststr/%%}
    abc%def%linux
    ## 由于删除字符串中行尾的字符时需要使用语法"/%"，所以如果想要删除字符串中第一个遇到的"%"时，则不能使用"/%"，需要对"%"进行转义
    # echo ${teststr/\%}
    abcdef%linux%
    ```

* 字符串大小写转换

  * 准备一个变量，变量值为字母a到z，只不过a到k为小写，L到Z为大写，如下所示：

    ```
    [root@www ~]# testvar1=$( echo {a..k};echo {L..Z} )
    [root@www ~]# echo ${testvar1}
    a b c d e f g h i j k L M N O P Q R S T U V W X Y Z
    ```

  * 将变量testvar1中的所有小写英文字母都转换成大写：

    ```
    [root@www ~]# echo ${testvar1^^}
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    ```

  * 将变量testvar1中的所有大写英文字母都转换成小写:

    ```
    [root@www ~]# echo ${testvar1,,}
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    ```

    ​