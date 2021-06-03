# django rest framework packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, AllBookSerializer
from .models import Books, BorrowBook

# user creation class
class CreateUser(APIView):
    
    def post(self, request):
        user_serialize = UserSerializer(data=request.data)
        if user_serialize.is_valid():
            user_serialize.save()
            return Response(user_serialize.data, status=status.HTTP_201_CREATED)
        return Response(user_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
# get all details of Books
class AllBooks(APIView):
    
    def get(self, request):
        print(request.user)
        books = Books.objects.all()
        book_serialize = AllBookSerializer(books, many = True)
        return Response(book_serialize.data, status=status.HTTP_302_FOUND)

# get details of specific Book
class Detail(APIView):
    
    def get(self, request,id):
        if Books.objects.filter(id=id).exists():
            book = Books.objects.get(id=id)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book_serialize = AllBookSerializer(book)
        return Response(book_serialize.data, status=status.HTTP_302_FOUND)

# class for borrow details
class Borrow(APIView):
    
    # get all books borrowed by user
    def get(self, request):
        user = request.user
        borrow = BorrowBook.objects.filter(user=user)
        books = {}
        for book in borrow:
            books[book.id] = book.book.book_name
        return Response(books, status=status.HTTP_200_OK)
    
    # creating new borrow
    def post(self, request):
        user = request.user
        book_id = request.data['book_id']
        if Books.objects.filter(id=book_id).exists():
            book = Books.objects.get(id=book_id)
            if book.book_count >= 1:  # check existence
                borrow = BorrowBook.objects.create(user = user, book = book)
                book.book_count -= 1
                book.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
            
        
        