import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_set_genre_to_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Чапаев и Пустота')

        # устанавливаем добавленной книге жанр
        collector.set_book_genre('Чапаев и Пустота', 'Фантастика')

        # проверяем, что установился нужный жанр
        assert collector.books_genre['Чапаев и Пустота'] == 'Фантастика'

    def test_get_book_genre_from_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаём словарь с двумя книгами
        collector.books_genre = {'Чапаев и Пустота': '', 'Бойцовский клуб': ''}

        # устанавливаем добавленной книге жанр
        collector.set_book_genre('Чапаев и Пустота', 'Фантастика')

        # проверяем, что метод get_book_genre возвращает нужный жанр
        assert collector.get_book_genre('Чапаев и Пустота') == 'Фантастика'

    def test_get_books_with_specific_genre_get_detectives(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаём словарь с четырьмя книгами
        collector.books_genre = {
            'Чапаев и Пустота': 'Фантастика',
            'Бойцовский клуб': 'Детективы',
            'Шерлок Холмс': 'Детективы',
            'Незнайка на Луне': 'Комедии'
        }

        # проверяем, что метод get_book_genre возвращает список из двух книг
        assert collector.get_books_with_specific_genre('Детективы') == ['Бойцовский клуб', 'Шерлок Холмс']

    def test_get_books_genre_2_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаём словарь с двумя книгами
        collector.books_genre = {
            'Чапаев и Пустота': 'Фантастика',
            'Бойцовский клуб': 'Детективы'
        }

        # проверяем, что метод get_books_genre возвращает словарь из двух книг
        assert collector.get_books_genre() == {'Чапаев и Пустота': 'Фантастика', 'Бойцовский клуб': 'Детективы'}

    def test_get_books_for_children_2_names(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаём словарь с четырьмя книгами
        collector.books_genre = {
            'Чапаев и Пустота': 'Фантастика',
            'Бойцовский клуб': 'Детективы',
            'Оно': 'Ужасы',
            'Незнайка на Луне': 'Комедии'
        }

        # проверяем, что get_books_for_children возвращает список из двух книг
        assert collector.get_books_for_children() == ['Чапаев и Пустота', 'Незнайка на Луне']

    def test_add_book_in_favorites_1_adding(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаём словарь с одной книгой
        collector.books_genre = {
            'Чапаев и Пустота': 'Фантастика'
        }

        # добавляем книгу в избранное
        collector.add_book_in_favorites('Чапаев и Пустота')

        # проверяем наличие добавленной книги в избранном
        assert collector.favorites == ['Чапаев и Пустота']

    def test_delete_book_from_favorites_1_removing(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # заполняем список favorites
        collector.favorites = ['12 правил', 'Шахматы', 'Бойцовский клуб', 'Чапаев и Пустота']

        # удаляем 1 книгу с помощью метода delete_book_from_favorites
        collector.delete_book_from_favorites('Бойцовский клуб')

        # проверяем, что осталось 3 книги в избранном
        assert collector.favorites == ['12 правил', 'Шахматы', 'Чапаев и Пустота']

    def test_get_list_of_favorites_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # заполняем список favorites
        collector.favorites = ['12 правил', 'Шахматы', 'Бойцовский клуб', 'Чапаев и Пустота']

        # проверяем, что возвращает метод get_list_of_favorites_books
        assert collector.get_list_of_favorites_books() == ['12 правил', 'Шахматы', 'Бойцовский клуб', 'Чапаев и Пустота']

    @pytest.mark.parametrize('book', ['12 правил', 'Шахматы', 'Бойцовский клуб', 'Чапаев и Пустота'])
    def test_add_new_book_add_different_books(self, book):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(book)

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert collector.get_book_genre(book) == ''







