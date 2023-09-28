import unittest
import pandas as pd

class TestOrderAnalysis(unittest.TestCase):

    def test_monthly_revenue(self):
        # Test the calculation of monthly revenue
        df = pd.DataFrame({
            'order_date': ['2023-01-15', '2023-01-20', '2023-02-10'],
            'product_price': [50.0, 30.0, 40.0]
        })
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['order_month'] = df['order_date'].dt.strftime('%Y-%m')
        monthly_revenue = df.groupby('order_month')['product_price'].sum()
        self.assertEqual(list(monthly_revenue), [80.0, 40.0])

    def test_product_revenue(self):
        # Test the calculation of product revenue
        df = pd.DataFrame({
            'product_name': ['Product A', 'Product B', 'Product A'],
            'product_price': [50.0, 30.0, 40.0]
        })
        product_revenue = df.groupby('product_name')['product_price'].sum()
        self.assertEqual(list(product_revenue), [90.0, 30.0])

    # Add similar tests for customer_revenue and top_10_customers

if __name__ == '__main__':
    unittest.main()
