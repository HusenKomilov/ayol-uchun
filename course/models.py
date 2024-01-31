from django.db import models


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="author/",
                              default="https://w7.pngwing.com/pngs/336/946/png-transparent-avatar-user-medicine-surgery-patient-avatar-face-heroes-head.png")
    description = models.TextField(blank=True, null=True)


class Category(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category/", blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title


class Complaint(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CourseAll(BaseModel):
    TAG_CHOICES = (
        (1, "Bestseller"),
        (2, "Tafsiya etiladi"),
    )
    title = models.CharField(max_length=300)
    short_content = models.CharField(max_length=350, blank=True, null=True)
    description = models.TextField()

    price = models.IntegerField()
    stock_price = models.IntegerField(null=True, blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course/')
    is_taken = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_recommendation = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CourseModule(BaseModel):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(CourseAll, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CourseVideo(BaseModel):
    title = models.CharField(max_length=300)
    course_time = models.CharField(max_length=200)
    short_description = models.CharField(max_length=350)
    description = models.TextField()

    language = models.CharField(max_length=100)
    watched = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    short_url = models.URLField()

    course = models.ForeignKey(CourseAll, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, blank=True, null=True)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, blank=True, null=True)

    video = models.FileField(f'course_video/{CourseAll.title}/')
    file = models.FileField(f'course_file/{CourseAll.title}/', blank=True, null=True)
    image = models.ImageField(f'course_image/{CourseAll.title}/', blank=True, null=True)

    is_public = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.title
