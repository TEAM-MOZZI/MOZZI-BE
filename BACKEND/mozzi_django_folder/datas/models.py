from django.db import models
from mongoengine import Document, DictField

class MongoFood(Document):
    food_recipe = DictField()  # 예시로 최대 길이를 1000으로 지정하였습니다.

# Create your models here.

class Foods(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=30)
    food_recipe = models.CharField(max_length=255)
    food_views = models.IntegerField()
    food_pic = models.CharField(max_length=200)
    food_salty_rate = models.FloatField()
    food_sweet_rate = models.FloatField()
    food_bitter_rate = models.FloatField()
    food_sour_rate = models.FloatField()
    food_umami_rate = models.FloatField()
    food_spicy_rate = models.FloatField()
    food_category = models.CharField(max_length=5)
    food_today_views = models.IntegerField()
    food_category_count = models.IntegerField()




class Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_pic = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Category 모델의 외래 키

    def __str__(self):
        return self.ingredient_name
    

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_code = models.CharField(max_length=20)
#     user_nickname = models.CharField(max_length=20)
#     user_register_date = models.DateTimeField()
#     user_isvegan = models.BooleanField()
    
#     class Meta:
#         db_table = 'user'  # MySQL 데이터베이스의 테이블 이름을 'user'로 지정

#     def __str__(self):
#         return self.user_code  # 객체를 출력할 때 사용할 문자열 반환
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_isvegan = models.IntegerField(blank=True, null=True)
    user_register_date = models.DateTimeField(blank=True, null=True)
    user_code = models.CharField(max_length=255, blank=True, null=True)
    user_nickname = models.CharField(max_length=255, blank=True, null=True)
    worldcup = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
    
class FoodIngredient(models.Model):
    food_ingredient_id = models.AutoField(primary_key=True)
    food_id = models.ForeignKey(Foods, on_delete=models.CASCADE, db_column='food_id')
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='ingredient_id')
    ingredient_ratio = models.FloatField()
    ingredient_count = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'food_ingredient'

# class FoodsFoods(models.Model):
#     food_id = models.BigIntegerField(blank=True, null=True)
#     other_food_id = models.BigIntegerField(blank=True, null=True)
#     relations = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'foods_foods'
class RefriIngredients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField(blank=True, null=True)
    stored_pos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refri_ingredients'
        unique_together = (('user', 'ingredient'),)



class UserFood(models.Model):
    user_food_id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Foods, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    user_food_preference = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_food'

class UserIngredients(models.Model):
    user_ingredients_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, blank=True, null=True)
    is_like = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ingredients'
