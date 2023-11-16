import unittest

# 테스트 코드
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 2, 3) # 같은지 판별
        self.assertTrue(10 == 10) # True인지 판별
        self.assertFalse(1 == 10) # False인지 판별
        self.assertGreater(5, 1) # 앞에 것이 뒤에 것보다 큰지(5 > 1)
        self.assertLess(2, 5) # 앞에 것이 뒤에 것보다 작은지(2 > 5)
        self.assertIn(1, [1, 3, 5, 6]) # 앞에 것이 뒤에 것에 포함되는지(1 => [1, 3, 5, 6])
        self.assertIsInstance('a', str) # 앞에 것이 뒤에 것의 인스턴스인지(a => str)

if __name__ == '__main__':
    unittest.main()