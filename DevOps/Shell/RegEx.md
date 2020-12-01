[TOC]

### RegEx

#### 一、连续次数的匹配

* 从regex.txt文本中找出哪些行包含两个连续的字母a

  ```
  [root@localhost testdir]# cat -n regex.txt
       1	a a
       2	aa
       3	a aa
       4	bb
       5	bbb
       6	c cc ccc
       7	dddd d dd ddd
       8	ab abc abcc
       9	ef eef eeef
  ```

  * 直接使用grep命令，在文本中搜索"aa"即可，因为"aa"就是两个连续的a字母

    ```
    [root@localhost testdir]# grep --color -n "aa" regex.txt
    2:aa
    3:a aa
    ```

  * 利用grep命令和正则表达式，即可找出哪些行包含2个连续的字母a ，示例如下

    ```
    [root@localhost testdir]# grep --color -n "a{2}" regex.txt
    2:aa
    3:a aa
    ## "\{2\}"就表示"连续出现2次"，所以，"a\{2\}"就表示a连续出现两次
    ```

  * 不过需要注意，如果字符连续出现的次数大于指定的次数，也是可以被匹配到的，示例如下：

    ```
    [root@localhost testdir]# grep --color -n "b\{2\}" regex.txt
    ```

    4:$\color{red}{bb}$

    5:$\color{red}{bb}$b

  * 如果你不想出现上述情况，只是想要精准的匹配连续出现2次且只出现了2次的字母b，示例如下

    ```
    [root@localhost testdir]# grep -n --color "\<b\{2\}\>" regex.txt
    ```

    4:$\color{red}{bb}$

  * 正则表达式中，"\<"表示锚定词首，"\>"表示锚定词尾

    ```bash
    [root@localhost testdir]# cat REG
    abchello world
    abc helloabc abc
    abc abchelloabc abc
    ```

  * 上个文件中，"abchello"中包含"hello",但是"hello"位于"abchello"这个单词的词尾，同理"helloabc"z中也包含"hello",dan但是位于这个单词的词首，正则中、""\<表示

  * 正则表达式中，"\<"表示锚定词首，"\>"表示锚定词尾，现在我们就来实验一下。

    ```bash
    [root@localhost testdir]# grep --color "\<hello" REG
    abc helloabc abc
    [root@localhost testdir]# grep --color "hello\>" REG
    abchello world
    ```

    * abc  $\color{red}{hello}$abc  abc
    * abc$\color{red}{hello}$  world

  * 同理，我们也可以将"\<"与"\>"结合在一起使用，示例如下

    ```bash
    [root@localhost testdir]# cat -n REG
    	1 abchello world
    	2 abc helloabc abc
    	3 abc abchelloabc abc
    	4 abchello helloabc hello ahelloa
    [root@localhost testdir]# grep --colo "\<hello\>" REG
    abchello helloabc hello ahelloa
    abchello helloabc \color{red}{hello} ahellos
    上例中，"\<hello\>"表示当hello既是词首又是词尾时则会被匹配到，换句话说，就是当hello作为一个独立的单词时，则会被匹配到，如上图所示，REG文本中第4行被匹配到了，因为只有第4行中才包含了一个独立的hello单词。
    ```

    * abchello helloabc $\color{red}{hello}$ ahellos

  * 正则表达式中，除了"\<"与"\>"能够表示锚定词首与锚定词尾以外，我们还可以使用"\b"去代替"\<"和"\>"，"\b"既能锚定词首，也能锚定词尾，示例如下:

  * ![](/Users/dev/Documents/RegEx/屏幕快照 2020-10-30 下午3.17.15.png)

  * "\b"是用来锚定词首、锚定词尾的，换句话说，"\b"是用来匹配"单词边界"的，而"\B"则正好相反。"\B"是用来匹配"非单词边界"的，示例如下:

    ![](/Users/dev/Documents/RegEx/屏幕快照 2020-10-30 下午3.49.48.png)

  * 上例中的"\Bhello"表示，只要hello不是词首，就会被匹配到，如上图所示

  * 而"hello\B"则正好相反，表示只要hello不是词尾，就会匹配到，如下图所示

    ![](/Users/dev/Documents/RegEx/屏幕快照 2020-10-30 下午3.55.32.png)

  * "\{x,y\}"表示之前的字符至少连续出现x次，最多连续出现y次，都能被匹配到，换句话说，只要之前的字符连续出现的次数在x与y之间，即可被匹配到，示例如下:

    ```
    [root@localhost testdir]# grep -n --color "d\{2,4\}" regex.txt
    7:dddd d dd ddd
    ```

    7:$\color{red}{dddd}$  d  $\color{red}{dd}$  $\color{red}{ddd}$

  * 小结

    * ^：表示锚定行首，此字符后面的任意内容必须出现在行首，才能匹配。

      $：表示锚定行尾，此字符前面的任意内容必须出现在行尾，才能匹配。

      ^$：表示匹配空行，这里所描述的空行表示"回车"，而"空格"或"tab"等都不能算作此处所描述的空行。

      ^abc$：表示abc独占一行时，会被匹配到。

      \<或者\b ：匹配单词边界，表示锚定词首，其后面的字符必须作为单词首部出现。

      \>或者\b ：匹配单词边界，表示锚定词尾，其前面的字符必须作为单词尾部出现。

      \B：匹配非单词边界，与\b正好相反。

#### 二、常用符号

* [[:alpha:]] 表示"任意字母"（不区分大小写）

  * 从文本中找出a字母后面跟随3个字符的字符串，但是，我们对后面跟随的3个字符有要求，并不能是任意3个字符，而必须是三个字母，示例如下：

    ```
    [root@localhost testdir]# cat reg1
    a
    a6d
    a89&
    a7idai8
    abcd
    aBdc
    aBCD
    a123
    a1a3
    a&@%
    [root@localhost testdir]# grep --color "a[[:alpha:]]\{3\}" reg1
    abcd
    aBdc
    aBCD
    ```

* [[:lower:]]表示任意小写字母

  * 只有当a后面的3个字符均为小写字母时，才会被匹配到，示例如下：

    ```
    [root@localhost testdir]# cat reg1
    a
    a6d
    a89&
    a7idai8
    abcd
    aBdc
    aBCD
    a123
    a1a3
    a&@%
    [root@localhost testdir]# grep --color "a[[:lower:]]\{3\}" reg1
    abcd
    ```

* [[:upper:]]表示任意大写字母

  * 示例如下

    ```
    [root@localhost testdir]# cat reg1
    a
    a6d
    a89&
    a7idai8
    abcd
    aBdc
    aBCD
    a123
    a1a3
    a&@%
    [root@localhost testdir]# grep --color "a[[:upper:]]\{3\}" reg1
    aBCD
    ```

    ​