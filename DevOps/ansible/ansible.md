Ansible

### 一、常用模块

  * fetch模块

      * 从远程主机拉取文件到ansilbe主机

      * 主机清单配置

        ```
        [root@localhost ~]# vim /etc/ansible/hosts
        [testA]
        test173 ansible_host=172.16.179.173
        test174 ansible_host=172.16.179.174
        [testB]
        test167 ansible_host=172.16.179.167
        [test:children]
        testA
        testB
        ```

* - 假如我们想要将testA组中所有主机的/etc/fstab文件拉取到本地，则可以使用如下命令

    ```
    [root@localhost ~]# ansible testA -m fetch -a "src=/etc/fstab dest=/testdir/ansible/"
    ps:如上述命令所示，-m选项用于调用指定的模块，"-m fetch"表示调用fetch模块，

    -a选项用于传递模块所需要使用的参数， -a "src=/etc/fstab dest=/testdir/ansible/"表示我们在使用fetch模块时，为fetch模块传入了两个参数，src与dest，这两个参数是必须有的
    ```

  - 列出absible所支持的模块

    ```
    [root@localhost ~]# ansible-doc -l
    ```

  - 查看模块的详细帮助信息

    ```
    [root@localhost ~]# ansible-doc -s fetch
    ```

  - 调用模块，比如调用ping模块

    ```
    [root@localhost ~]# ansible all -m ping
    ```

  - 调用模块的同时传入模块所需要的参数，以fetch模块为例

    ```
    [root@localhost ~]# ansible 172.16.179.167 -m fetch -a "src=/etc/fstab dest=/testdir/ansible/"
    ```

* copy模块

  * 将ansible主机上的文件拷贝到远程主机中

  * **src参数**    ：用于指定需要copy的文件或目录

    **dest参数**  ：用于指定文件将被拷贝到远程主机的哪个目录中，dest为必须参数

    **content参数**  ：当不使用src指定拷贝的文件时，可以使用content直接指定文件内容，src与content两个参数必有其一，否则会报错。

    **force参数**  :  当远程主机的目标路径中已经存在同名文件，并且与ansible主机中的文件内容不同时，是否强制覆盖，可选值有yes和no，默认值为yes，表示覆盖，如果设置为no，则不会执行覆盖拷贝操作，远程主机中的文件保持不变。

    **backup参数** :  当远程主机的目标路径中已经存在同名文件，并且与ansible主机中的文件内容不同时，是否对远程主机的文件进行备份，可选值有yes和no，当设置为yes时，会先备份远程主机中的文件，然后再将ansible主机中的文件拷贝到远程主机。

    **owner参数** : 指定文件拷贝到远程主机后的属主，但是远程主机上必须有对应的用户，否则会报错。

    **group参数** : 指定文件拷贝到远程主机后的属组，但是远程主机上必须有对应的组，否则会报错。

    **mode参数** : 指定文件拷贝到远程主机后的权限，如果你想将权限设置为"rw-r--r--"，则可以使用mode=0644表示，如果你想要在user对应的权限位上添加执行权限，则可以使用mode=u+x表示。

  * 将ansible主机中/testdir/copytest文件复制到远程主机的/opt目录下，注意，如果copytest文件已经存在于远程主机的/opt目录中，并且远程主机中的copytest与ansible主机中copytest文件内容不同，那么使用如下命令时，远程主机中的copytest文件将被覆盖。

    ```
    ansible test173 -m copy -a "src=/testdir/copytest dest=/opt/"
    ```

  * 在远程主机的/opt目录下生成文件test，test文件中有两行文本，第一行文本为aaa，第二行为bbb，当使用content指定文件内容时，dest参数对应的值必须是一个文件，而不能是一个路径。

    ```
    ansible test70 -m copy -a 'content="aaa\nbbb\n" dest=/opt/test'
    ```

  * 将ansible主机中/testdir/copytest文件复制到远程主机的/opt目录中时，如果远程主机中已经存在/opt/copytest文件，并且文件内容与ansible主机中的copytest文件的内容不一致，则不执行拷贝操作，远程主机中的/opt/copytest文件内容不会被改变。

    ```
    ansible test173 -m copy -a "src=/testdir/copytest dest=/opt/ force=no"
    test173 | SUCCESS => {
        "changed": false,
        "dest": "/opt/",
        "src": "/testdir/copytest"
    }
    ```

  * 将ansible主机中/testdir/copytest文件复制到远程主机的/opt目录中时，如果远程主机中已经存在/opt/copytest文件，并且文件内容与ansible主机中的copytest文件的内容不一致，会执行拷贝操作，但是在执行拷贝操作之前，会将远程主机中的原文件重命名，以作备份，然后再进行拷贝操作。

    ```
    ansible test173 -m copy -a "src=/testdir/copytest dest=/opt/ backup=yes"
    ```

  * 拷贝文件时，指定文件的属主，需要注意，远程主机上必须存在对应的用户。

    ```
    ansible test173 -m copy -a "src=/testdir/copytest dest=/opt/ owner=qingbobo"
    ```

  * 拷贝文件时，指定文件的属组，需要注意，远程主机上必须存在对应的组。

    ```
    ansible test173 -m copy -a "src=/testdir/copytest dest=/opt/ group=qingbobo"
    ```

  * 拷贝文件时，指定文件的权限

    ```
    ansible test173 -m copy -a "src=/testdir/copytest dest=/opt/ mode=0640"
    ```

* file模块

  * file模块可以帮助我们完成一些对文件的基本操作，比如，创建文件或目录、删除文件或目录、修改文件权限等

    此处我们介绍一些file模块的常用参数，然后再给出对应示例。

    **path参数** ：必须参数，用于指定要操作的文件或目录，在之前版本的ansible中，使用dest参数或者name参数指定要操作的文件或目录，为了兼容之前的版本，使用dest或name也可以。

    **state参数** ：此参数非常灵活，此参数对应的值需要根据情况设定，比如，当我们需要在远程主机中创建一个目录的时候，我们需要使用path参数指定对应的目录路径，假设，我想要在远程主机上创建/testdir/a/b目录，那么我则需要设置path=/testdir/a/b，但是，我们无法从"/testdir/a/b"这个路径看出b是一个文件还是一个目录，ansible也同样无法单单从一个字符串就知道你要创建文件还是目录，所以，我们需要通过state参数进行说明，当我们想要创建的/testdir/a/b是一个目录时，需要将state的值设置为directory，"directory"为目录之意，当它与path结合，ansible就能知道我们要操作的目标是一个目录，同理，当我们想要操作的/testdir/a/b是一个文件时，则需要将state的值设置为touch，当我们想要创建软链接文件时，需将state设置为link，想要创建硬链接文件时，需要将state设置为hard，当我们想要删除一个文件时（删除时不用区分目标是文件、目录、还是链接），则需要将state的值设置为absent，"absent"为缺席之意，当我们想让操作的目标"缺席"时，就表示我们想要删除目标。

    **src参数** ：当state设置为link或者hard时，表示我们想要创建一个软链或者硬链，所以，我们必须指明软链或硬链链接的哪个文件，通过src参数即可指定链接源。

    **force参数**  :  当state=link的时候，可配合此参数强制创建链接文件，当force=yes时，表示强制创建链接文件，不过强制创建链接文件分为两种情况，情况一：当你要创建的链接文件指向的源文件并不存在时，使用此参数，可以先强制创建出链接文件。情况二：当你要创建链接文件的目录中已经存在与链接文件同名的文件时，将force设置为yes，回将同名文件覆盖为链接文件，相当于删除同名文件，创建链接文件。情况三：当你要创建链接文件的目录中已经存在与链接文件同名的文件，并且链接文件指向的源文件也不存在，这时会强制替换同名文件为链接文件。

    **owner参数** ：用于指定被操作文件的属主，属主对应的用户必须在远程主机中存在，否则会报错。

    **group参数** ：用于指定被操作文件的属组，属组对应的组必须在远程主机中存在，否则会报错。

    **mode参数**：用于指定被操作文件的权限，比如，如果想要将文件权限设置为"rw-r-x---"，则可以使用mode=650进行设置，或者使用mode=0650，效果也是相同的，如果你想要设置特殊权限，比如为二进制文件设置suid，则可以使用mode=4700，很方便吧。

    **recurse参数**：当要操作的文件为目录，将recurse设置为yes，可以递归的修改目录中文件的属性。

  * 在test173主机上创建一个名为testfile的文件，如果testfile文件已经存在，则会更新文件的时间戳，与touch命令的作用相同

    ```
    ansible test173 -m file -a "path=/testdir/testfile state=touch"
    ```

  * 在test173主机上创建一个名为testdir的目录，如果testdir目录已经存在，则不进行任何操作

    ```
    ansible test173 -m file -a "path=/testdir/testdir state=directory"
    ```

  * 在test173上为testfile文件创建硬链接文件，硬链接名为hardfile，执行下面命令的时候，testfile已经存在

    ```
    ansible test173 -m file -a "path=/testdir/hardfile state=hard src=/testdir/testfile"
    ```

  * ​

  * ​

    ​