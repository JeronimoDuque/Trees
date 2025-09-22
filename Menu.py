print("bienvenido al menu")
print("1. Arbol binario de busqueda")
print("2. Arbol autobalanceado")
print("3. Arbol B")
print("4. Arbol Trie")
print("5. Arbol N-ario")
print("6. Salir")
opcion = int(input("Seleccione una opcion: "))

match opcion:
    case 1:
    # En Binary_tree.py
        from Binary_tree import Binary_tree
        from Binary_Search_Tree import BinarySearchTree

        bst = BinarySearchTree()
        while True:
            print("que operacion desea realizar con el arbol binario de busqueda?")
            print("1. Insertar un valor")
            print("2. eliminar un valor")
            print("3. Buscar un valor")
            print("4. Salir")
            operacion = int(input("Seleccione una opcion: "))
            if operacion == 1:
                valor = int(input("Ingrese el valor a insertar: "))
                bst.insert(valor)
                print(f"Valor {valor} insertado.")
                bst.visualize()
            elif operacion == 2:
                valor = int(input("Ingrese el valor a eliminar: "))
                bst.delete(valor)
                print(f"Valor {valor} eliminado.")
                bst.visualize()
            elif operacion == 3:
                metodo = int(input("Seleccione el metodo de busqueda:\n1. pre order\n2. in order\n3. post order\n"))
                if metodo == 1:
                    value_to_find = int(input("Ingrese el valor a buscar: "))
                    order , positions = bst.preorder_with_position(value_to_find)
                    print(order)
                    if positions:
                        print(f"Valor {value_to_find} encontrado en las posiciones (preorder): {positions}")
                    else:
                        print(f"Valor {value_to_find} no encontrado en el arbol.")
                elif metodo == 2:
                    value_to_find = int(input("Ingrese el valor a buscar: "))
                    order , positions = bst.inorder_with_position(value_to_find)
                    print(order)
                    if positions:
                        print(f"Valor {value_to_find} encontrado en las posiciones (inorder): {positions}")
                    else:
                        print(f"Valor {value_to_find} no encontrado en el arbol.")
                elif metodo == 3:
                    value_to_find = int(input("Ingrese el valor a buscar: "))
                    order , positions = bst.postorder_with_position(value_to_find)
                    print(order)
                    if positions:
                        print(f"Valor {value_to_find} encontrado en las posiciones (postorder): {positions}")
                    else:
                        print(f"Valor {value_to_find} no encontrado en el arbol.")
                else:
                    print("Opcion no valida, intente de nuevo.")
                bst.visualize()
            elif operacion == 4:
                break
            else:
                print("Opcion no valida, intente de nuevo.")
    case 2:
    # En AVL_tree.py
        from Binary_tree import Binary_tree
        from AVL import AVLTree

        bst = AVLTree()
        while True:
            print("que operacion desea realizar con el arbol binario de busqueda?")
            print("1. Insertar un valor")
            print("2. eliminar un valor")
            print("3. Buscar un valor")
            print("4. Salir")
            operacion = int(input("Seleccione una opcion: "))
            if operacion == 1:
                valor = int(input("Ingrese el valor a insertar: "))
                bst.insert(valor)
                print(f"Valor {valor} insertado.")
                bst.visualize()
            elif operacion == 2:
                valor = int(input("Ingrese el valor a eliminar: "))
                bst.delete(valor)
                print(f"Valor {valor} eliminado.")
                bst.visualize()
            elif operacion == 3:
                metodo = int(input("Seleccione el metodo de busqueda:\n1. pre order\n2. in order\n3. post order\n"))
                if metodo == 1:
                    value_to_find = int(input("Ingrese el valor a buscar: "))
                    order , positions = bst.preorder_with_position(value_to_find)
                    print(order)
                    if positions:
                        print(f"Valor {value_to_find} encontrado en las posiciones (preorder): {positions}")
                    else:
                        print(f"Valor {value_to_find} no encontrado en el arbol.")
                elif metodo == 2:
                    value_to_find = int(input("Ingrese el valor a buscar: "))
                    order , positions = bst.inorder_with_position(value_to_find)
                    print(order)
                    if positions:
                        print(f"Valor {value_to_find} encontrado en las posiciones (inorder): {positions}")
                    else:
                        print(f"Valor {value_to_find} no encontrado en el arbol.")
                elif metodo == 3:
                    value_to_find = int(input("Ingrese el valor a buscar: "))
                    order , positions = bst.postorder_with_position(value_to_find)
                    print(order)
                    if positions:
                        print(f"Valor {value_to_find} encontrado en las posiciones (postorder): {positions}")
                    else:
                        print(f"Valor {value_to_find} no encontrado en el arbol.")
                else:
                    print("Opcion no valida, intente de nuevo.")
                bst.visualize()
            elif operacion == 4:
                break
            else:
                print("Opcion no valida, intente de nuevo.")
    case 3:
    # En B_tree.py
        from B_tree import B_tree

        btree = B_tree(2)
        while True:
            print("que operacion desea realizar con el arbol B?")
            print("1. Insertar un valor")
            print("2. Buscar un valor")
            print("3. Obtener lista en orden de niveles y posicion de un valor")
            print("4. Salir")
            operacion = int(input("Seleccione una opcion: "))
            if operacion == 1:
                valor = int(input("Ingrese el valor a insertar: "))
                btree.insert(valor)
                print(f"Valor {valor} insertado.")
                btree.visualize("mi_btree")
            elif operacion == 2:
                value_to_find = int(input("Ingrese el valor a buscar: "))
                found = btree.search_level_order(value_to_find)
                if found:
                    print(f"Valor {value_to_find} encontrado en el arbol.")
                else:
                    print(f"Valor {value_to_find} no encontrado en el arbol.")
            elif operacion == 3:
                value_to_find = int(input("Ingrese el valor a buscar: "))
                lista, pos = btree.get_level_order_list_and_position(value_to_find)
                print("Lista de claves por niveles:", lista)
                if pos != -1:
                    print(f"Posición de la clave {value_to_find} en la lista: {pos}")
                else:
                    print(f"Clave {value_to_find} no encontrada en el árbol.")
            elif operacion == 4:
                break
            else:
                print("Opcion no valida, intente de nuevo.")
    case 4:
    # En Trie_tree.py
        from Trie_tree import Trie

        trie = Trie()
        while True:
            print("que operacion desea realizar con el arbol Trie?")
            print("1. Insertar una palabra")
            print("2. Buscar una palabra")
            print("3. Salir")
            operacion = int(input("Seleccione una opcion: "))
            if operacion == 1:
                palabra = input("Ingrese la palabra a insertar: ")
                trie.insert(palabra)
                print(f"Palabra '{palabra}' insertada.")
            elif operacion == 2:
                palabra = input("Ingrese la palabra a buscar: ")
                found = trie.search(palabra)
                if found:
                    print(f"Palabra '{palabra}' encontrada en el Trie.")
                else:
                    print(f"Palabra '{palabra}' no encontrada en el Trie.")
            elif operacion == 3:
                break
            else:
                print("Opcion no valida, intente de nuevo.")
            trie.visualize()
    case 5:
    # En N_ary_tree.py
        from N_tree import N_Tree
        n_tree = N_Tree()
        while True:
            print("que operacion desea realizar con el arbol N-ario?")
            print("1. Insertar un nodo")
            print("2. Eliminar un nodo")
            print("3. Buscar un valor")
            print("4. Mostrar lista en orden de niveles")
            print("5. Salir")
            operacion = int(input("Seleccione una opcion: "))
            if operacion == 1:
                parent_value = input("Ingrese el valor del nodo padre (o 'None' para la raiz): ")
                if parent_value.lower() == 'none':
                    parent_value = None
                else:
                    parent_value = int(parent_value)
                value = int(input("Ingrese el valor del nuevo nodo: "))
                success = n_tree.insert(parent_value, value)
                if success:
                    print(f"Nodo con valor {value} insertado bajo el padre {parent_value}.")
                else:
                    print(f"Padre con valor {parent_value} no encontrado.")
            elif operacion == 2:
                value = int(input("Ingrese el valor del nodo a eliminar: "))
                success = n_tree.delete(value)
                if success:
                    print(f"Nodo con valor {value} eliminado.")
                else:
                    print(f"Valor {value} no encontrado.")
            elif operacion == 3:
                value = int(input("Ingrese el valor a buscar: "))
                found = n_tree.search_level_order(value)
                if found:
                    print(f"Valor {value} encontrado en el arbol.")
                else:
                    print(f"Valor {value} no encontrado en el arbol.")
            elif operacion == 4:
                level_order_list = n_tree.get_level_order_list()
                print("Lista de valores en orden de niveles:", level_order_list)
            elif operacion == 5:
                break
            else:
                print("Opcion no valida, intente de nuevo.")
            n_tree.visualize()
    case 6:
        print("Saliendo...")
        exit()
    case _:
        print("Opcion no valida")
        exit()