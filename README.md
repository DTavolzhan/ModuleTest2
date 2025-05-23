# ModuleTest2

Варіант 1 (Галерея):
1. Необхідно додати в аплікації gallery модель для категорії зображень.
- назва моделі: Category
- атрибути: name (CharField)
2. Необхідно додати в аплікації gallery модель для зображення.
- назва моделі: Image
- атрибути: title (CharField), image (ImageField), categories (ManyToManyField), created_date (DateField), age_limit (PositiveIntegerField)
3. Написати unit-тести, які протестують роботу із створеними моделями.   
