import unittest
from pathlib import Path
from data import generar_ventas
from streamlit.testing.v1 import AppTest

class DashboardTests(unittest.TestCase):
    def test_datos(self):
        df = generar_ventas()
        self.assertEqual(len(df), 1200)
        self.assertTrue(df.pedido.is_unique)
        self.assertTrue((df.venta > 0).all())
        self.assertTrue(df.equals(generar_ventas()))

    def test_aplicacion_y_filtros(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py")).run(timeout=30)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.metric), 4)
        app.sidebar.multiselect[0].set_value(["Tecnología"]).run()
        self.assertEqual(len(app.exception), 0)
        esperado = generar_ventas().query("categoria == 'Tecnología'")
        self.assertEqual(app.metric[1].value, f"{len(esperado):,}".replace(",", "."))
        app.sidebar.multiselect[0].set_value([]).run()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.warning), 1)

if __name__ == "__main__":
    unittest.main()
