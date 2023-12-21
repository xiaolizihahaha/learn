# Leetcode

- **链表**

  ```python
  #链表定义
  class ListNode:
    def __init__(self,x):
      self.val = x
      self.next = None
  
  #链表的创建
  if __name__ == '__main__':
    num1 = 520
    
    head = ListNode(0)
    pre = head
    
    for n in str(num1):
      pre.next = ListNode(int(n))
      pre = pre.next
      
    pre.next = None
    l1 = head.next
    #此时链表l1为：5->2->0->None
    
    
    for n in str(num1)[::-1]:
      pre.next = ListNode(int(n))
      pre = pre.next
      
    pre.next = None
    l2 = head.next 
    #此时链表l2为：0->2->5->None
    
    
    return l1, l2
  
  
  
  ```

  

- 1
- 