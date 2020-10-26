### shell命令

* 两种组合命令方法

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

  * ​