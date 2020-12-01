```Bash
[root@locahost ~]# gitlab-ctl reconfigure
```

* 4. 初始化Gitlab服务、启动Gitlab服务。

```bash
[root@localhost ~]# gitlab-ctl reconfigure
[root@localhost ~]# gitlab-ctl start | restart | status | stop
ps：每次修改 /etc/gitlab/gitlab.rb 都需要 gitlab-ctl reconfigure
```

* 5. gitlab汉化

  - 汉化包链接：<https://gitlab.com/xhang/gitlab/>

  ```
  [root@localhost ~]# tar xf gitlab-12-3-stable-zh.tar.gz
  [root@localhost ~]# gitlab-ctl stop
  [root@localhost ~]# \cp -r gitlab-12-3-stable-zh/* /opt/gitlab/embedded/service/gitlab-rails/
  [root@localhost ~]# gitlab-ctl start
  ```

* 6. 访问Gitlab服务、以及gitlab邮箱测试。

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

    ```
    1、修改默认存放备份站点目录，然后进行重新加载配置文件
    [root@qingbo ~]# vim /etc/gitlab/gitlab.rb

    gitlab_rails['manage_backup_path'] = true		# 开启备份
    gitlab_rails['backup_path'] = "/data/gitlab/backups"	# 更改备份路径
    gitlab_rails['backup_keep_time'] = 604800		# 备份保留7天

    [root@qingbo ~]# gitlab-ctl reconfigure
    2、手动执行备份命令，会将备份的结果存储于/data/gitlab/backups目录中
    [root@qingbo ~]# gitlab-rake gitlab:backup:create
    [root@qingbo ~]# ls /data/gitlab/backups
    1604485149_2020_11_04_13.4.3_gitlab_backup.tar
    3、添加定时任务，每天凌晨2点15分执行备份
    [root@qingbo ~]# crontab -l
    15 2 * * * gitlab-rake gitlab:backup:create &>/dev/null

    ## 恢复gitlab数据
    1、停止gitlab数据写入服务
    [root@qingbo ~]# gitlab-ctl stop unicorn
    [root@qingbo ~]# gitlab-ctl stop sidekiq
    2、通过gitlab-rake命令进行恢复
    [root@qingbo ~]# gitlab-rake gitlab:backup:restore BACKUP=1604485149_2020_11_04_13.4.3
    ## gitlab升级
    1、停止gitlab服务
    [root@qingbo ~]# gitlab-ctl stop unicorn
    [root@qingbo ~]# gitlab-ctl stop sidekiq
    [root@qingbo ~]# gitlab-ctl stop nginx
    2、备份gitlab
    [root@qingbo ~]# gitlab-rake gitlab:backup:create
    3、下载gitlab 的 RPM 包并进行升级
    ###直接安装高版本
    [root@qingbo ~]# yum install gitlab-ce-13.5.2-ce.0.el7.x86_64
    ###报错
    Error executing action `run` on resource 'ruby_block[directory resource: /var/opt/gitlab/git-data/repositories]'
    ###解决方法
    [root@qingbo ~]# chmod 2777 /var/opt/gitlab/git-data/repositories
    4、启动并查看gitlab版本信息
    [root@qingbo ~]# gitlab-ctl reconfigure
    [root@qingbo ~]# gitlab-ctl restart
    [root@qingbo ~]# head -1 /opt/gitlab/version-manifest.txt
    13.5.2-ce.0.el7
    ```

    ​

* 7. Gitlab - 分支 - tag基本使用

  * 创建tag标签

    ```
    git tag -a "v1.1" -m "new tag"
    ```

    ​