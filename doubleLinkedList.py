''' from multiprocessing.sharedctypes import Value
from os import remove '''
import math

class DoubleLinkedList:
    #creamos la clase nodo
    class Node:
        #creamos el metodo inicializador a la clase nodo
        def __init__(self,value):
            self.value=value
            self.next_node=None
            self.previous_node=None
    
    #creamos el metodo inicializador de la clase DoubleLinkedList
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    #metodo para imprimir la lista doblemente enlazada
    def show_double_linked_list(self):
        #la lista almacena los nodos de la lista doblemente enlazada
        array_double_list=[]
        current_node=self.head
        while current_node!=None:
            #unicamente almacenamos en la lista el valor del nodo
            array_double_list.append(current_node.value)
            current_node=current_node.next_node
        print(f"{array_double_list} cantidad de nodos -> {self.length}")
        
    #metodo para añadir nodos al inicio de la lista
    def prepend_node(self,value):
        #al nuevo nodo le asignamos la estructura real de la clase node
        current_node=self.Node(value)
        #validamos si no hay cabeza ni cola
        if self.head==None and self.tail==None:
            #la cabeza toma el valor del current_node
            self.head=current_node
            #la cola toma el valor que tiene la cabeza
            self.tail=self.head
        else:
            #el enlace anterior de la actual cabeza conecta con el nodo actual
            self.head.previous_node=current_node
            current_node.next_node=self.head
            self.head=current_node
        self.length+=1
     
    #agregar al final de la lista       
    def append_node(self,value):
        current_node=self.Node(value)
        if self.head==None and self.tail==None:
            self.head=current_node
            self.tail=self.head
        else:
            self.tail.next_node=current_node
            current_node.previous_node=self.tail
            self.tail=current_node
        self.length+=1
            
    #eliminar el primer nodo de la lista
    def shift_node(self):
        if self.length==0:
            self.head=None
            self.tail=None
        elif self.head!=None:
            #el nodo a eliminar es la cabeza
            remove_node=self.head
            #la nueva cabeza será el nodo siguiente a la anterior cabeza
            self.head=remove_node.next_node
            #el enlace siguiente de la antigua cabeza apunta a none
            remove_node.next_node=None
            #el enlace anterior de la cabeza actual apunta a none
            remove_node.previous_node=None
        self.length-=1
        print(f"El valor del nodo eliminado es: {remove_node.value}")
        
    #eliminar el último nodo de la lista
    def pop_node(self):
        if self.length==0:
            self.head=None
            self.tail=None
        else:
            #el nodo a liminar será la cola
            remove_node=self.tail
            #la nueva cola pasa a ser el nodo previo de la cola antigua
            self.tail=remove_node.previous_node
            #la cola la desvincula de la lista con su nodo 
            self.tail.next_node=None
            remove_node.previous_node=None
        self.length-=1
        print(f"El valor del nodo eliminado es: {remove_node.value}")
        
    #metodo para obtener el valor de un nodo en determinada posición
    def get_node(self,index):
        #tomar la lista desde 1 
        
        if index==1:
            print(f"El valor buscado es: {self.head.value}")
            return self.head
        elif index==self.length:
            print(f"El valor buscado es: {self.tail.value}")
            return self.tail
        elif (index <= 0 or index > self.length):
            print("fuera de rango")
        elif not(index == 1 or index == self.length):
            #búsqueda rápida del nodo
            middle_index=int(self.length/2)
            if index <= middle_index:
                current_node=self.head
                count_node=1
                while count_node != index:
                    #aumentamos en uno el recorrido de los nodos
                    current_node=current_node.next_node
                    #aumentar el contador de nodos
                    count_node+=1
                print(f"El valor buscado es: {current_node.value}")
                return current_node
            else:
                current_node=self.tail
                count_node=self.length
                while count_node != index:
                    #aumentamos en uno el recorrido de los nodos
                    current_node=current_node.previous_node
                    #disminuir el contador de nodos
                    count_node-=1
                print(f"El valor buscado es: {current_node.value}")
                return current_node
            
    #actualizar el valor de un nodo por el valor al cuadrado del nodo anterior
    def update(self,index):
        current_node=self.get_node(index)
        if index < 1:
            print("************************** INVÁLIDO **************************")
        elif self.length==0:
            self.head=None
            self.tail=None
        else:
            if current_node!=None:
                if type(current_node.previous_node.value)==str:
                    print("No se puede actulizar ya que es una letra")
                else:
                    value=current_node.previous_node.value
                    result=math.pow(value,2)
                    current_node.value=result
                    
    #insertar un nuevo nodo en la lista
    def insert(self,index,value):
        if index < 1:
            print("************************** INVÁLIDO **************************")
        elif index==1:
            current_node=self.get_node(index)
            multiple=current_node.next_node.value
            if value % multiple == 0:
                return self.prepend_node(value)
            else:
                print(f"El valor {value} no es múltiplo de {multiple}")
        elif index==self.length:
            print("No es posible ya que el siguiente valor es null")
        else:
            current_node=self.get_node(index)
            multiple=current_node.value
            if value % multiple == 0:
                new_node=self.Node(value)
                anterior_node=self.get_node(index-1)
                new_node.next_node=current_node
                new_node.previous_node=anterior_node
                current_node.previous_node=new_node
                anterior_node.next_node=new_node
                self.length+=1
            else:
                print(f"El valor {value} no es múltiplo de {multiple}")
                
        
    #eliminar un nodo de la lista
    def remove(self,index):
        if index < 1:
            print("************************** INVÁLIDO **************************")
        elif index==1:
            return self.shift_node()
        elif index==self.length:
            return self.pop_node()
        else:
            current_node=self.get_node(index+1)
            anterior_node=self.get_node(index-1)
            anterior_node.next_node=current_node
            current_node.previous_node=anterior_node
            self.length-=1
        
    #invertir la lista
    def reverse(self):
        if self.length == 0:
            self.head=None
            self.tail=None
        else:
            current_node=self.head
            aux1=current_node.next_node
            current_node.next_node=None
            current_node.previous_node=aux1
            while aux1 != None:
                raiz=math.sqrt(current_node.value)
                current_node.value=raiz
                aux1.previous_node=aux1.next_node
                aux1.next_node=current_node
                current_node=aux1
                aux1=aux1.previous_node
            self.head=current_node
            raiz_head=math.sqrt(self.head.value)
            self.head.value=raiz_head
            return self.head
                
            