from Aula53.dao.base_dao import BaseDao
from Aula53.model.produto_model import ProdutoModel

#--- Criação da classe para realizar as operações na tabela produto
#--- Criado classe utilizando herança da classe BaseDao, que possui as configurações de acesso a base
class ProdutoDao(BaseDao):
    #--- Declaração do método de listagem de todos os dados da tabela utilizando a sessao com o banco de dados criada na classe 'Mâe'
    def list_all(self):
        return self.sessao.query(ProdutoModel).all()
