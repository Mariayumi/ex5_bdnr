from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    ## CREATE ##
    # usuário #
    def usuario(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarUsu)

    @staticmethod
    def _criarUsu(db):
        query = ("CREATE (object: usuario {nome: $nomeUsu, email: $emailUsu, cpf: $cpfUsu, estado: $estadoUsu, cidade: $cidadeUsu, rua: $ruaUsu, numero: $numeroUsu})")

        nomeUsu = input("Nome: ")
        emailUsu = input("Email: ")
        cpfUsu = input("CPF: ")
        print("\n---- Endereço ----")
        estadoUsu = input("Estado: ")
        cidadeUsu = input("Cidade: ")
        ruaUsu = input("Rua: ")
        numeroUsu = input("Número: ")

        result = db.run(query, nomeUsu=nomeUsu, emailUsu=emailUsu, cpfUsu=cpfUsu, estadoUsu=estadoUsu, cidadeUsu=cidadeUsu, ruaUsu=ruaUsu, numeroUsu=numeroUsu)

        print("Usuário criado com sucesso!")
        return [{"object": row["object"]["nome"]["email"]["cpf"]["estado"]["cidade"]["rua"]["numero"]} for row in result]

    # vendedor #
    def vendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarVend)

    @staticmethod
    def _criarVend(db):
        query = ("CREATE (object: vendedor {nome: $nomeVend, email: $emailVend, cnpj: $cnpjVend, estado: $estadoVend, cidade: $cidadeVend, rua: $ruaVend, numero: $numeroVend})")

        nomeVend = input("Nome: ")
        emailVend = input("Email: ")
        cnpjVend = input("CNPJ: ")
        print("\n---- Endereço ----")
        estadoVend = input("Estado: ")
        cidadeVend = input("Cidade: ")
        ruaVend = input("Rua: ")
        numeroVend = input("Número: ")

        result = db.run(query, nomeVend=nomeVend, emailVend=emailVend, cnpjVend=cnpjVend, estadoVend=estadoVend, cidadeVend=cidadeVend, ruaVend=ruaVend, numeroVend=numeroVend)

        print("Vendedor criado com sucesso!")
        return [{"object": row["object"]["nome"]["email"]["cnpj"]["estado"]["cidade"]["rua"]["numero"]} for row in result]

    # produto #
    def produto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarProd)

    @staticmethod
    def _criarProd(db):
        query = ("CREATE (object: produto {nome: $nomeProd, quantidade: $quantProd, status: $statusProd, preço: $precoProd, vendedor: $cnpjVend})")

        nomeProd = input("Nome: ")
        quantProd = input("Quantidade: ")
        statusProd = input("Status: ")
        precoProd = input("Preço: ")
        print("\n---- Vendedor ----")
        cnpjVend = input("CNPJ do vendedor: ")

        result = db.run(query, nomeProd=nomeProd, quantProd=quantProd, statusProd=statusProd, precoProd=precoProd, cnpjVend=cnpjVend)

        print("Produto criado com sucesso!")
        return [{"object": row["object"]["nome"]["quantidade"]["status"]["preco"]["vendedor"]} for row in result]

    # compra #
    def compra(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarCompra)

    @staticmethod
    def _criarCompra(db):
        query = ("CREATE (object: compra {id: $idComp, status: $statusComp, formaPagamento: $formaPagamentoComp, precoTotal: $precoTotal, produto: $nomeProd, quantidade: $quantComp, vendedor: $cnpjVend, usuario: $cpfUsu})")

        idComp = input("ID da compra: ")
        statusComp = input("Status da compra: ")
        formaPagamentoComp = input("Forma de pagamento: ")
        precoTotal = input("Preço total: ")
        print("\n---- Produto ----")
        nomeProd = input("Nome do produto: ")
        quantComp = input("Quantidade: ")
        print("\n---- Vendedor ----")
        cnpjVend = input("CNPJ do vendedor: ")
        print("\n---- Usuário ----")
        cpfUsu = input("CPF do usuário: ")

        result = db.run(query, idComp=idComp, statusComp=statusComp, formaPagamentoComp=formaPagamentoComp, precoTotal=precoTotal, nomeProd=nomeProd, quantComp=quantComp, cnpjVend=cnpjVend, cpfUsu=cpfUsu)

        print("Compra criada com sucesso!")
        return [{"object": row["object"]["id"]["status"]["formaPagamento"]["precoTotal"]["produto"]["quantidade"]["vendedor"]["usuario"]} for row in result]
    

    ## READ ALL ##
    # usuário #
    def readUsuarios(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readUsuarios)

    @staticmethod
    def _readUsuarios(db):
        query = "MATCH (u:usuario) RETURN u"
        result = db.run(query)
        return [print([row]) for row in result]

    # vendedor #
    def readVendedores(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readVendedores)

    @staticmethod
    def _readVendedores(db):
        query = "MATCH (v:vendedor) RETURN v"
        result = db.run(query)
        return [print([row]) for row in result]

    # produto #
    def readProdutos(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readProdutos)

    @staticmethod
    def _readProdutos(db):
        query = "MATCH (p:produto) RETURN p"
        result = db.run(query)
        return [print([row]) for row in result]

    # compra #
    def readCompras(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readCompras)

    @staticmethod
    def _readCompras(db):
        query = "MATCH (c:compra) RETURN c"
        result = db.run(query)
        return [print([row]) for row in result]

    
    ## READ ONE ##
    # usuário #
    def readUsuario(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readUsuario)
    
    @staticmethod
    def _readUsuario(db):
        cpfUsu = input("Insira o CPF do usuário que deseja encontrar: ")
        query = "MATCH (u:usuario) WHERE u.cpf = $cpfUsu RETURN u"
        result = db.run(query, cpfUsu=cpfUsu)
        return [print([row]) for row in result]

    # vendedor #
    def readVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readVendedor)
    
    @staticmethod
    def _readVendedor(db):
        cnpjVend = input("Insira o CNPJ do vendedor que deseja encontrar: ")
        query = "MATCH (v:vendedor) WHERE v.cnpj = $cnpjVend RETURN v"
        result = db.run(query, cnpjVend=cnpjVend)
        return [print([row]) for row in result]

    # produto #
    def readProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readProduto)
    
    @staticmethod
    def _readProduto(db):
        nomeProd = input("Insira o nome do produto que deseja encontrar: ")
        query = "MATCH (p:produto) WHERE p.nome = $nomeProd RETURN p"
        result = db.run(query, nomeProd=nomeProd)
        return [print([row]) for row in result]

    # compra #
    def readCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readCompra)
    
    @staticmethod
    def _readCompra(db):
        idCompra = input("Insira o ID da compra que deseja encontrar: ")
        query = "MATCH (c:compra) WHERE c.id = $idCompra RETURN c"
        result = db.run(query, idCompra=idCompra)
        return [print([row]) for row in result]


    ## UPDATE ##
    # usuário #
    def updateUsuario(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateUsuario)

    @staticmethod
    def _updateUsuario(db):
        cpfUsu = input("Insira o CPF do usuário que deseja atualizar: ")

        print('''
                1 - Nome
                2 - Email
                3 - CPF
                4 - Estado
                5 - Cidade
                6 - Rua
                7 - Número
            ''')
        
        option = input("Insira o número da opção que deseja atualizar: ")

        while int(option) < 1 or int(option) > 7:
            print("Opção inválida")
            option = input("Insira outra opção: ")

        if option == "1": option = "nome"
        elif option == "2": option = "email"
        elif option == "3": option = "cpf"
        elif option == "4": option = "estado"
        elif option == "5": option = "cidade"
        elif option == "6": option = "rua"
        elif option == "7": option = "numero"

        new= input("Insira o novo valor: ")

        query = ("MATCH (u:usuario) WHERE u.cpf = $cpfUsu SET u." + option + " = $new")

        print("Usuário atualizado com sucesso!")

        db.run(query, cpfUsu = cpfUsu, option=option, new=new)

    # vendedor #
    def updateVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateVendedor)

    @staticmethod
    def _updateVendedor(db):
        cnpjVend = input("Insira o CNPJ do vendedor que deseja atualizar: ")

        print('''
                1 - Nome
                2 - Email
                3 - CNPJ
                4 - Estado
                5 - Cidade
                6 - Rua
                7 - Número
            ''')
        
        option = input("Insira o número da opção que deseja atualizar: ")

        while int(option) < 1 or int(option) > 7:
            print("Opção inválida")
            option = input("Insira outra opção: ")

        if option == "1": option = "nome"
        elif option == "2": option = "email"
        elif option == "3": option = "cnpj"
        elif option == "4": option = "estado"
        elif option == "5": option = "cidade"
        elif option == "6": option = "rua"
        elif option == "7": option = "numero"

        new= input("Insira o novo valor: ")

        query = ("MATCH (v:vendedor) WHERE v.cnpj = $cnpjVend SET v." + option + " = $new")

        print("Vendedor atualizado com sucesso!")

        db.run(query, cnpjVend=cnpjVend, option=option, new=new)

    # produto #
    def updateProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateProduto)

    @staticmethod
    def _updateProduto(db):
        nomeProd = input("Insira o nome do produto que deseja atualizar: ")

        print('''
                1 - Nome
                2 - Quantidade
                3 - Status
                4 - Preço
                5 - CNPJ do Vendedor
            ''')
        
        option = input("Insira o número da opção que deseja atualizar: ")

        while int(option) < 1 or int(option) > 7:
            print("Opção inválida")
            option = input("Insira outra opção: ")

        if option == "1": option = "nome"
        elif option == "2": option = "quantidade"
        elif option == "3": option = "status"
        elif option == "4": option = "preço"
        elif option == "5": option = "cnpjVend"

        new= input("Insira o novo valor: ")

        query = ("MATCH (p:produto) WHERE p.nome = $nomeProd SET p." + option + " = $new")

        print("Produto atualizado com sucesso!")

        db.run(query, nomeProd=nomeProd, option=option, new=new)

    # compra #
    def updateCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateCompra)

    @staticmethod
    def _updateCompra(db):
        idCompra = input("Insira o ID da compra que deseja atualizar: ")

        new= input("Insira o novo valor: ")

        query = ("MATCH (c:compra) WHERE c.id = $idCompra SET c.status = $new")

        print("Compra atualizada com sucesso!")

        db.run(query, idCompra=idCompra, new=new)

    
    ## DELETE ##
    # usuário #
    def deleteUsuario(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteUsuario)

    @staticmethod
    def _deleteUsuario(db):
        cpfUsu = input("Insira o CPF do usuário a ser deletado: ")
        query = "MATCH (u:usuario) WHERE u.cpf = $cpfUsu DETACH DELETE u"
        print("Usuário deletado com sucesso")
        db.run(query, cpfUsu=cpfUsu)

    # vendedor #
    def deleteVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteVendedor)

    @staticmethod
    def _deleteVendedor(db):
        cnpjVend = input("Insira o CNPJ do vendedor a ser deletado: ")
        query = "MATCH (v:vendedor) WHERE v.cnpj = $cnpjVend DETACH DELETE v"
        print("Vendedor deletado com sucesso")
        db.run(query, cnpjVend=cnpjVend)

    # produto #
    def deleteProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteProduto)

    @staticmethod
    def _deleteProduto(db):
        nomeProd = input("Insira o nome do produto a ser deletado: ")
        query = "MATCH (p:produto) WHERE p.nome = $nomeProd DETACH DELETE p"
        print("Produto deletado com sucesso")
        db.run(query, nomeProd=nomeProd)

    # compra #
    def deleteCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deleteCompra)

    @staticmethod
    def _deleteCompra(db):
        idCompra = input("Insira o ID da compra a ser deletado: ")
        query = "MATCH (c:compra) WHERE c.id = $idCompra DETACH DELETE c"
        print("Compra deletada com sucesso")
        db.run(query, idCompra=idCompra)


if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://516f9ca3.databases.neo4j.io"
    user = "neo4j"
    password = "WVsvVDO0m2ol_GSLUalfSJAYgJYYih4d2F9XY39uiDY"
    app = App(uri, user, password)

    ## CREATE ##
    #app.usuario()
    #app.vendedor()
    #app.produto()
    #app.compra()

    ## READ ALL ##
    #app.readUsuarios()
    #app.readVendedores()
    #app.readProdutos()
    #app.readCompras()

    ## READ ONE ##
    #app.readUsuario()
    #app.readVendedor()
    #app.readProduto()
    #app.readCompra()

    ## UPDATE ##
    #app.updateUsuario()
    #app.updateVendedor()
    #app.updateProduto()
    #app.updateCompra()

    ## DELETE ##
    #app.deleteUsuario()
    #app.deleteVendedor()
    #app.deleteProduto()
    #app.deleteCompra()

    app.close()