import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
# Test 1 
    def test1_add_book(self):
        lover = BookLover("Liz Khan", "Lizkhan@ymmail.com", "Mystery")
        
        lover.add_book("Death on the Nile", 4)
        #assert lover.has_read("Death on the Nile")
        self.assertTrue(lover.has_read('Death on the Nile'))
        
# Test 2 
    def test2_add_book(self):
        lover = BookLover("Liz Khan", "Lizkhan@ymmail.com", "Fantasy")
        
        lover.add_book("Twilight", 6)
        lover.add_book("Twilight", 4)
        assertlover.num_books_read() == 2
        
# test 3 
    def test3_has_read(self):
        lover = BookLover("Liz Khan", "Lizkhan@ymmail.com", "ScienceFi")
        
        lover.add_book("Knight Owl", 5)
        assert lover.has_read("Knight Owl")
    
# Test 4  
    def test4_has_read(self):
        lover = BookLover("Liz Khan", "Lizkhan@ymmail.com", "HistoricalFi")
        
        lover.add_book("Hooly", 4)
        assert not lover.has_read("To Kill a Mockingbird")

# Test 5 
    def test5_num_books_read(self):
        lover = BookLover("Liz Khan", "Lizkhan@ymmail.com", "Romance")
        
        lover.add_book("It Ends With Us", 5)
        lover.add_book("Before We Were Strangers", 4)
        self.assertEqual(lover.num_books_read(), expected)
        #assert lover.num_books_read() == 2
# Test 6 
    def test6_fav_books(self):
        lover = BookLover("Liz Khan", "Lizkhan@ymmail.com", "Thriller")
        
        lover.add_book("Misery", 4)
        lover.add_book("In Cold Blood", 3)
        lover.add_book("The Stand", 5)
        fav_books = lover.fav_books()
        assert all(fav_books['book_rating'] > 3)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)