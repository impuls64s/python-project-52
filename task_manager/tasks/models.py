from django.db import models
from task_manager.statuses.models import Statuses
from task_manager.users.models import Users
from task_manager.labels.models import Labels


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    description = models.TextField(max_length=500, blank=True)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        related_name='author'
    )
    executor = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        related_name='executor'
    )
    label = models.ManyToManyField(
        Labels,
        related_name='label',
        through='TaskRelationLabel'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskRelationLabel(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)
