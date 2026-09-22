from rest_framework.test import APITestCase

from .models import Produto


class ProdutoAula26Tests(APITestCase):

    def setUp(self):
        Produto.objects.create(
            nome="Notebook Pro",
            preco="3500.00",
            marca="Dell",
            estoque=15,
            descricao="Notebook de alta performance com tela OLED.",
        )
        Produto.objects.create(
            nome="Mouse Sem Fio",
            preco="80.00",
            marca="Logitech",
            estoque=25,
            descricao=None,
        )

    # ---------- Marca ----------

    def test_criar_produto_com_marca_valida(self):
        payload = {
            "nome": "Monitor Ultra",
            "preco": "1200.00",
            "marca": "Dell",
            "estoque": 5,
        }
        response = self.client.post("/api/produtos/", payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["marca"], "Dell")

    def test_criar_com_marca_curta_retorna_400(self):
        payload = {
            "nome": "Monitor",
            "preco": "1000.00",
            "marca": "D",
            "estoque": 5,
        }
        response = self.client.post("/api/produtos/", payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("marca", response.data)

    def test_filtrar_por_marca_existente(self):
        response = self.client.get("/api/produtos/?marca=dell")
        self.assertEqual(response.status_code, 200)
        nomes = [p["nome"] for p in response.data["results"]]
        self.assertIn("Notebook Pro", nomes)
        self.assertNotIn("Mouse Sem Fio", nomes)

    def test_ordenar_por_marca(self):
        response = self.client.get("/api/produtos/?ordering=marca")
        self.assertEqual(response.status_code, 200)
        marcas = [p["marca"] for p in response.data["results"]]
        self.assertEqual(marcas, sorted(marcas, key=str.lower))

    def test_buscar_por_marca(self):
        response = self.client.get("/api/produtos/?search=dell")
        self.assertEqual(response.status_code, 200)
        nomes = [p["nome"] for p in response.data["results"]]
        self.assertIn("Notebook Pro", nomes)

    # ---------- Estoque ----------

    def test_criar_com_estoque_zero_e_valido(self):
        payload = {
            "nome": "Teclado Mecânico",
            "preco": "250.00",
            "marca": "Keychron",
            "estoque": 0,
        }
        response = self.client.post("/api/produtos/", payload)
        self.assertEqual(response.status_code, 201)

    def test_criar_com_estoque_negativo_retorna_400(self):
        payload = {
            "nome": "Fone",
            "preco": "150.00",
            "marca": "Sony",
            "estoque": -5,
        }
        response = self.client.post("/api/produtos/", payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("estoque", response.data)

    def test_filtrar_por_faixa_de_estoque(self):
        response = self.client.get(
            "/api/produtos/?estoque_minimo=10&estoque_maximo=20"
        )
        self.assertEqual(response.status_code, 200)
        nomes = [p["nome"] for p in response.data["results"]]
        self.assertIn("Notebook Pro", nomes)
        self.assertNotIn("Mouse Sem Fio", nomes)

    def test_estoque_nao_participa_da_busca(self):
        response = self.client.get("/api/produtos/?search=15")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"], [])

    # ---------- Descrição ----------

    def test_criar_sem_descricao_e_valido(self):
        payload = {
            "nome": "Cabo HDMI",
            "preco": "35.00",
            "marca": "Ugreen",
            "estoque": 50,
        }
        response = self.client.post("/api/produtos/", payload)
        self.assertEqual(response.status_code, 201)

    def test_descricao_acima_do_limite_retorna_400(self):
        payload = {
            "nome": "Produto X",
            "preco": "10.00",
            "marca": "Marca Y",
            "estoque": 1,
            "descricao": "a" * 501,
        }
        response = self.client.post("/api/produtos/", payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("descricao", response.data)

    def test_buscar_termo_presente_na_descricao(self):
        response = self.client.get("/api/produtos/?search=oled")
        self.assertEqual(response.status_code, 200)
        nomes = [p["nome"] for p in response.data["results"]]
        self.assertIn("Notebook Pro", nomes)

    def test_ordenar_por_descricao_sem_erro_com_nulos(self):
        response = self.client.get("/api/produtos/?ordering=descricao")
        self.assertEqual(response.status_code, 200)
