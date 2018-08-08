import unittest
from unittest.mock import patch
from app.budget.models import Budget
class TestBudgetModel(unittest.TestCase):

    def setUp(self):
        self.budget = Budget(user_id=1, name='test', amount=120, intial_amount=120)

    def test_budget_properties(self):
        self.assertEqual(self.budget.user_id, 1)
        self.assertEqual(self.budget.name, 'test')
        self.assertEqual(self.budget.amount, 120)
        self.assertEqual(self.budget.intial_amount, 120)

    
    @patch('app.Budget')
    def test_query_all(self, mock_budget):
        mock_budget.query.all.return_value = [self.budget]

        budgets = mock_budget.query.all()
        first_budget = budgets[0]
        self.assertTrue(len(budgets), 1)
        self.assertEqual(first_budget.user_id, 1)
        self.assertEqual(first_budget.name, 'test')
        self.assertEqual(first_budget.amount, 120)
        self.assertEqual(first_budget.intial_amount, 120)

    @patch('app.Budget')
    def test_filter_by(self, mock_budget):
        mock_budget.query.filter_by.return_value = [self.budget]

        budget_list = mock_budget.query.filter_by(name='test')

        first_budget = budget_list[0]
        self.assertTrue(len(budget_list), 1)
        self.assertEqual(first_budget.user_id, 1)
        self.assertEqual(first_budget.name, 'test')
        self.assertEqual(first_budget.amount, 120)
        self.assertEqual(first_budget.intial_amount, 120)
        
        
if __name__ == '__main__':
    unittest.main()