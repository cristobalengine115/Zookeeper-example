import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):


#Pruebas por instructores
    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)
#Pruebas de Tarea
    def test_createEphemeral(self):
        tree = Ztree()
        tree.create('/Ephemeral','Ephemeral_content',True,False,2,'/')
        nodo = tree.tree.get_node('/Ephemeral').data
        self.assertTrue(nodo.ephemeral)
    
    def test_createOnService(self):
        tree = Ztree()
        tree.create('/OnService','onService_content',False,True,7,'/')
        nodo = tree.tree.get_node('/OnService').data
        self.assertTrue(nodo.OnService)
    
    def test_deleteNode(self):
        tree = Ztree()
        tree.create('/OnService2','onService_content2',False,True,5,'/')
        tree.delete('/onService_content2',5)
        self.assertFalse(tree.exist('/onService_content2'))
    
    def test_searchNode(self):
        tree = Ztree()
        tree.create('/node','node_data',True,False,5,'/')
        self.assertTrue(tree.exist('/node'))

    def test_changeData(self):
        tree = Ztree()
        tree.create('/nodeChanging','change_content',False,True,5,'/')
        tree.setData('/nodeChanging','change_new_content')
        self.assertEqual(tree.getData('/nodeChanging'),'change_new_content')


if __name__ == '__main__':
    unittest.main()

