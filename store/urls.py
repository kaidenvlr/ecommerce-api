from django.urls import path

from store.views import category

urlpatterns = [
    # Category
    path('add-category', category.add_category, name='add-category'),
    path('get-category', category.get_one_category, name='get-category'),
    path('get-categories', category.get_all_categories, name='get-categories'),
    path('update-category', category.update_category, name='update-category'),
    path('delete-category', category.delete_category, name='delete-category'),


]
