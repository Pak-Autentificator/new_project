from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField('Название', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    product_information_60 = models.CharField('Информация о товаре(Кратко)', max_length=60)
    product_information = models.TextField('Информация о товаре')

    #--------Характеристики клавиатуры---------#

    keyboard_type = models.CharField('Тип клавиатуры', max_length=50)
    connection = models.CharField('Подключение', max_length=50)
    backlit_keys = models.CharField('Подсветка клавиш', max_length=50)
    form = models.CharField('Форма', max_length=50)
    peculiarities = models.TextField('Особенности')
    manufacturer_country = models.CharField('Страна-производитель', max_length=50)
    layout = models.CharField('Раскладка', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    interface = models.CharField('Интерфейс', max_length=50)
    weight = models.FloatField('Вес')
    frame = models.CharField('Корпус', max_length=50)
    additional_functions = models.TextField('Дополнительные функции')
    sensing_distance = models.CharField('Дистанция срабатывания', max_length=50)
    pressure_force = models.CharField('Сила нажатия', max_length=50)
    production_technology = models.CharField('Технология производства', max_length=50)
    number_of_keyboard_buttons = models.IntegerField('Количество кнопок клавиатуры')
    key_features = models.CharField('Особенности клавиш', max_length=100)
    equipment = models.TextField('Комплектация')
    dimensions = models.CharField('Размеры', max_length=50)
    keystroke_resource = models.CharField('Ресурс нажатия клавиш', max_length=50)
    color_of_cyrillic_letters = models.CharField('Цвет букв кириллицы', max_length=50)
    os_compatibility = models.CharField('Совместимость с ОС', max_length=100)
    cable_length = models.DecimalField('Длина кабеля, м', max_digits=5, decimal_places=2)
    brand_registration_country = models.CharField('Страна регистрации бренда', max_length=50)
    guarantee = models.CharField('Гарантия', max_length=50)



    # Поле для изображения (например, фотографии товара)
    imageURL_title = models.URLField('Титульное Изображение (URL)')
    imageURL_1 = models.URLField('Изображение 1(URL)')
    imageURL_2 = models.URLField('Изображение 2(URL)')
    imageURL_3 = models.URLField('Изображение 3(URL)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост с товаром'
        verbose_name_plural = 'Посты с товаром'



class Order(models.Model):
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return self.name  # Вернуть имя пользователя или другое поле в качестве строкового представления


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'




