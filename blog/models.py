from django.db import models
                                                                                          
                                                                                          
class Post(models.Model):                                                                      
    content = models.CharField(max_length=256)                                                 
    created_at = models.DateTimeField('Datetime created')                                      
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.content
                                                                                          
                                                                                          
class Comment(models.Model):                                                                   
    post = models.ForeignKey(Post)                                                             
    message = models.TextField()                                                               
    created_at = models.DateTimeField('Datetime created')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.message

class Travel(models.Model):
	name=models.CharField(max_length=256) 
	place=models.CharField(max_length=256) 
	cost=models.CharField(max_length=100)

	Datetime=models.DateTimeField('Datetime available')
	description=models.TextField()
	def __unicode__(self):  # Python 3: def __str__(self):
    	    return self.name