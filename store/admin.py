from django.contrib import admin

from store.models import Category, Subcategory, Brand, Product, Review, ProductImage, Order, Promo, Cart, CartProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    readonly_fields = ['updated_at', 'created_at']
    list_filter = ('active',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    readonly_fields = ['updated_at', 'created_at']
    list_filter = ('active',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ('active',)
    readonly_fields = ['updated_at', 'created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategory', 'brand', 'title']
    list_filter = ('active',)
    readonly_fields = ['updated_at', 'created_at']


admin.site.register(ProductImage)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'star', 'buyer']
    readonly_fields = ['updated_at', 'created_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'total_price']
    list_filter = ('status',)
    readonly_fields = ['updated_at', 'created_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer']


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'qty']


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
    list_filter = ('active',)
    sortable_by = 'active'
