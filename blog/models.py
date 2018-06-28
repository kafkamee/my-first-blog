from django.db import models
from django.utils import timezone

class Post(models.Model):
	#models.ForeignKey : 다른 모델에 대한 링크를 의미함
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	#model.CharField : 글자 수가 제한된 텍스트를 정의할 때 사용(글 제목과 같이 짧은 문자열 정보를 저장할 때)
	title = models.CharField(max_length=200)
	
	#models.TextField : 글자수에 제한이 없는 긴 텍스트를 위한 속성(블로그 컨텐츠)
	text = models.TextField()
	
	#models.DateTimeField : 날짜와 시간을 의미함
	created_date = models.DateTimeField(
		default=timezone.now)
	
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

