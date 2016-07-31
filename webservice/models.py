from __future__ import unicode_literals

from django.db import models
import json


# Create your models here.

class KeyAcess(models.Model):
    key = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.key


class Application(models.Model):
    nodes = models.TextField()
    title = models.CharField(max_length=200)
    running = models.BooleanField()
    size = models.IntegerField()
    states = models.TextField(

    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def length(self):
        return self.size

    def toJson(self):
        return json.dumps({'title': self.title, 'nodes': self.nodes, 'running': self.running, 'size': self.size,
                           'states': self.states})


class Node(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    # connections = models.TextField()
    # messages = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)

    def toJson(self):
        return json.dumps(
            {'id': self.id, 'x': self.x, 'y': self.y})
        # {'id': self.id, 'x': self.x, 'y': self.y, 'connections': self.connections, 'messages': self.messages})


class StateApp(models.Model):
    app = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    author = models.TextField()
    operations = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)

    def toJson(self):
        return json.dumps({'app': self.app, 'start': str(self.start), 'end': str(self.end), 'author': self.author,
                           'operations': self.operations})


class Operation(models.Model):
    message = models.TextField()
    successors = models.TextField()
    current = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.message)

    def toJson(self):
        return json.dumps({'message': self.message, 'successors': self.successors, 'current': self.current})
