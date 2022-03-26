from doubleLinkedList import DoubleLinkedList

inst_dll=DoubleLinkedList()

inst_dll.prepend_node(20)
inst_dll.prepend_node(14)
inst_dll.prepend_node(5)

#C,B,A
inst_dll.show_double_linked_list()
inst_dll.append_node(2)
#C,B,A,D
''' inst_dll.show_double_linked_list()
inst_dll.shift_node()
#B,A,D
inst_dll.show_double_linked_list()
inst_dll.pop_node() 
#B,A
inst_dll.show_double_linked_list()'''
inst_dll.get_node(0)

#inst_dll.append_node(3)
inst_dll.show_double_linked_list()
inst_dll.update(5)
inst_dll.show_double_linked_list()

inst_dll.insert(3,40)
inst_dll.show_double_linked_list()

inst_dll.remove(5)
inst_dll.show_double_linked_list()

inst_dll.reverse()
inst_dll.show_double_linked_list()
