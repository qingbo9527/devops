```Bash
[root@locahost ~]# gitlab-ctl reconfigure
```

* 4.初始化Gitlab服务、启动Gitlab服务。

```bash
[root@localhost ~]# gitlab-ctl reconfigure
[root@localhost ~]# gitlab-ctl start | restart | status | stop
ps：每次修改 /etc/gitlab/gitlab.rb 都需要 gitlab-ctl reconfigure
```

* 5.gitlab汉化

  - 汉化包链接：<https://gitlab.com/xhang/gitlab/>

  ```
  [root@localhost ~]# tar xf gitlab-12-3-stable-zh.tar.gz
  [root@localhost ~]# gitlab-ctl stop
  [root@localhost ~]# \cp -r gitlab-12-3-stable-zh/* /opt/gitlab/embedded/service/gitlab-rails/
  [root@localhost ~]# gitlab-ctl start
  ```

* 6.访问Gitlab服务、以及gitlab邮箱测试。

  - 配置域名

    ```
    # vim /etc/hostname
    gitlab.qingbo.com
    # vim /etc/hosts
    172.16.179.172 gitlab.qingbo.com
    ```

  - 配置邮箱

  - gitlab基本使用

  - gitlab中 用户组 用户 项目

  - Gitlab 基本运维 备份 恢复 升级

