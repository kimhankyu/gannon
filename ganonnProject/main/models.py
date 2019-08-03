from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=200)
    flatform = models.CharField(max_length=200)
    gameStory = models.TextField(max_length=1000)#수정




# 게임스토리
# 평점
# 제작사
# 출시년도
# 장르
# 사진
# 동영상링크