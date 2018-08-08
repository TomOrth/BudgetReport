import unittest
from unittest.mock import patch
from app.expense.models import Expense
class TestBudgetModel(unittest.TestCase):

    def setUp(self):
        self.expense = Expense(user_id=1, description='test', amount=120, budget_id=1)

    def test_expense_properties(self):
        self.assertEqual(self.expense.user_id, 1)
        self.assertEqual(self.expense.description, 'test')
        self.assertEqual(self.expense.amount, 120)
        self.assertEqual(self.expense.budget_id, 1)

    
    @patch('app.Expense')
    def test_query_all(self, mock_expense):
        mock_expense.query.all.return_value = [self.expense]

        expenses = mock_expense.query.all()
        first_expense = expenses[0]
        self.assertTrue(len(expenses), 1)
        self.assertEqual(first_expense.user_id, 1)
        self.assertEqual(first_expense.description, 'test')
        self.assertEqual(first_expense.amount, 120)
        self.assertEqual(first_expense.budget_id, 1)

    @patch('app.Expense')
    def test_filter_by(self, mock_expense):
        mock_expense.query.filter_by.return_value = [self.expense]

        expense_list = mock_expense.query.filter_by(name='test')

        first_expense = expense_list[0]
        self.assertTrue(len(expense_list), 1)
        self.assertEqual(first_expense.user_id, 1)
        self.assertEqual(first_expense.description, 'test')
        self.assertEqual(first_expense.amount, 120)
        self.assertEqual(first_expense.budget_id, 1)
        
        
if __name__ == '__main__':
    unittest.main()