from django.db import models

# Create your models here.

class Provider(models.Model):
	name = models.CharField(max_length = 255, verbose_name = '名称')
	baseurl = models.CharField(max_length = 255, verbose_name = '基础URL')

	def __str__(self):
		return self.name

class API(models.Model):
	provider = models.ForeignKey(Provider, verbose_name = '提供者')
	name = models.CharField(max_length = 255, verbose_name = '名称')
	slug = models.CharField(max_length = 255, verbose_name = 'URL')
	type = models.CharField(max_length = 255, verbose_name = '类型')
	args = models.TextField(verbose_name = '参数')
	retu = models.CharField(max_length = 255, verbose_name = '返回定义')
	authority = models.CharField(max_length = 255, verbose_name = '认证')

	def __str__(self):
		return '{}.{}'.format(self.provider.name, self.name)

class Logic(models.Model):
	name = models.CharField(max_length = 255, verbose_name = '名称')
	describe = models.CharField(max_length = 255, verbose_name = '描述')
	Q = models.TextField(verbose_name = 'IF')
	A = models.TextField(verbose_name = 'THEN')
	T = models.IntegerField(verbose_name = '周期')
	TimeStamp = models.DateTimeField(auto_now_add = True, verbose_name = '时间戳')

	def __str__(self):
		return '{}[{}]'.format(self.name, self.describe)
