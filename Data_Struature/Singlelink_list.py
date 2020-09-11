# coding:utf-8
# @time:2020-09-11
# 定义一个节点类
# 节点对象，包括数据元素elem 和 next
class Node(object):
  def __init__(self,elem):
      self.elem = elem
      self.next = None
# 定义链表类
class Singlelink_list(object):
    # 表头指向None
    def __init__(self,node = None):
        self.__head = None
    # 判断链表是否为空
    def is_empty(self):
        return self.__head == None
    def lenght(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.__head
        while cur != None:
            print(self.elem,end=" ")
            cur = cur.next
        print(' ')
    # 添加头节点
    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
    # 添加尾节点
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur != None:
                cur = cur.next
            cur.next = node
    # 插入节点
    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.lenght()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos -1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node
    # 删除节点           
    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    # 插入节点
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
            return False

if __name__ == "__main__":
    ll = Singlelink_list()
    print(ll.is_empty())
    print(ll.lenght())
    ll.append(1)
    print(ll.is_empty())
    print(ll.lenght())

