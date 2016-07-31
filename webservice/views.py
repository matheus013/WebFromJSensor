from django.shortcuts import render, get_object_or_404
from models import Node
from models import Application
from models import Operation
from models import StateApp


# Create your views here.

def test_views(request):
    return render(request, 'index.html', {})


def node_detail(request, pk):
    node = get_object_or_404(Node, pk=pk)
    return render(request, 'node_detail.html', {'node': node})


def app_detail(request, pk):
    app = get_object_or_404(Application, pk=pk)
    return render(request, 'app_detail.html', {'app': app})


def size(request, pk):
    app = get_object_or_404(Application, pk=pk)
    return render(request, 'size.html', {'app': app})


def op_detail(request, pk):
    op = get_object_or_404(Operation, pk=pk)
    return render(request, 'op_detail.html', {'op': op})


def state_detail(request, pk):
    state = get_object_or_404(StateApp, pk=pk)
    return render(request, 'state_detail.html', {'state': state})


def finish_application(request, pk):
    app = get_object_or_404(Application, pk=pk)
    app.running = False
    app.save()
    return render(request, 'app_detail.html', {'app': app})
