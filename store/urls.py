from django.urls import path

from store import views

urlpatterns = [
    # Category
    path('add-category', views.category.add_category, name='add-category'),
    path('get-category', views.category.get_one_category, name='get-category'),
    path('get-categories', views.category.get_all_categories, name='get-categories'),
    path('update-category', views.category.update_category, name='update-category'),
    path('delete-category', views.category.delete_category, name='delete-category'),

    # Subcategory
    path('add-subcategory', views.subcategory.add_subcategory, name='add-subcategory'),
    path('get-subcategory', views.subcategory.get_one_subcategory, name='get-subcategory'),
    path('get-subcategories', views.subcategory.get_all_subcategories, name='get-subcategories'),
    path('update-subcategory', views.subcategory.update_subcategory, name='update-subcategory'),
    path('delete-subcategory', views.subcategory.delete_subcategory, name='delete-subcategory'),

    # Brand
    path('add-brand', views.brand.add_brand, name='add-brand'),
    path('get-brand', views.brand.get_one_brand, name='get-brand'),
    path('get-brands', views.brand.get_all_brands, name='get-brands'),
    path('update-brand', views.brand.update_brand, name='update-brand'),
    path('delete-brand', views.brand.delete_brand, name='delete-brand'),
]
