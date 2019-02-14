from django.db import models

class Portfolio(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/') # images라는 파일에 저장
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.title

# image를 데이터베이스에 넣고 싶을때
# pip install pillow
