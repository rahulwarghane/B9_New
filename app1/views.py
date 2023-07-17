from django.shortcuts import render , HttpResponse, redirect
from .models import Book
import datetime

# Create your views here.

def welcome_page(request):
    # return HttpResponse("welcome to the Library application ")
    return render(request , "welcome.html")

def show_books(request):
    books = Book.objects.filter(is_published = True)
    return render(request , "showbooks.html" , {"All_books": books , "today": datetime.datetime.now()})

def show_single_book(request, bid):
    try:
         book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    return render(request ,"bookdetail.html",{"book": book_obj})

def add_single_book(request):
    if request.method == "POST":
        # print("In POST request")
        final_dict = request.POST
        Book_name = final_dict.get("nm")
        Book_price = final_dict.get("price")
        Book_Qty = final_dict.get("qty")
        Book_is_pub = final_dict.get("is_pub")
        if Book_is_pub == "YES":
            is_published = True
        else:
           is_published = False 
        Book.objects.create(name = Book_name , price = Book_price , qty = Book_Qty ,is_published = is_published)  
        return redirect("show_books")
    
    elif request.method == "GET":
        return render(request , "addbook.html")
    


def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method =='GET':
        return render(request , "bookedit.html", {"single_book":book_obj})
    elif request.method =='POST':
        print("In post method")
        final_dict = request.POST
        Book_name = final_dict.get("nm")
        Book_price = final_dict.get("price")
        Book_Qty = final_dict.get("qty")
        Book_is_pub = final_dict.get("is_pub")
        if Book_is_pub == "YES":
            is_published = True
        else:
           is_published = False 

        book_obj.name = Book_name
        book_obj.price = Book_price
        book_obj.qty = Book_Qty
        book_obj.is_published = is_published
        book_obj.save()    
        return redirect("show_books")   

def delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()                         # hard delete
    return redirect("show_books")   



def soft_delete_single_book(request , bid):  # soft delete
    book_obj = Book.objects.get(id=bid)
    book_obj.is_published = False
    book_obj.save()
    return redirect("show_books") 
