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