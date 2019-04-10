import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Board
from .forms import BoardForm

plus = False
# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')

    context = {'boards' : boards}
    print(request.user.id)
    
    return render(request, 'boards/index.html', context)

@login_required
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('boards:index')
    if request.method == 'POST':
        '''
        # 앞으로는 request.POST를 사용하지 않을것.
        # 검증이 안되기 때문
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Boad(title=title, content=content)
        board.save()
        '''
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            # title = board_form.cleaned_data.get('title')
            # content = board_form.cleaned_data.get('content')
            # board = Board(title=title, content=content)
            # board.save()
            # return redirect('boards:detail' board.pk)
            
            
            # board_form.user = request.user
            # board.save()
            
            board = board_form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect(board)
    else:
        board_form = BoardForm()
    context = {'board_form' : board_form}
    return render(request, 'boards/form.html', context)
    
def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    board.hit += 1
    board.save()
    context = {'board' : board}
    return render(request, 'boards/detail.html', context)
    

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    # board = Board.objects.get(pk=board_pk)
    
    if request.method == 'POST':
        if request.user.is_superuser:
            board.delete()
            messages.success(request, '삭제되었습니다.')
            return redirect('boards:index')
        if board.user == request.user:
            board.delete()
            messages.success(request, '삭제되었습니다.')
            return redirect('boards:index')
            
    # messages.add_message(request, messages.SUCCESS, '유효하지 않은 접근입니다.')
    # messages.success(request, '유효하지 않은 접근입니다.')
    messages.warning(request, '유효하지 않은 접근입니다.')

    return redirect(board)
    
    
    
    # if request.method == 'POST':
    #     board.delete()
    #     return redirect('boards:index')
    # else:
    #     return redirect(board)
        
def update(request, board_pk):
    # 1. board_pk에 해당하는 오브젝트를 가져온다.
    #   - 없으면, 404 에러
    #   - 있으면, board = Board.objects.get(pk=board_pk)와 동일
    board = get_object_or_404(Board, pk=board_pk)
    
    # 2. POST 요청이면 (사용자가 form을 통해 데이터를 보내 준 것.)
    if request.method == 'POST':
        # 사용자 입력 값(request.POST)을 BoardForm에 전달해주고,
        board_form = BoardForm(request.POST, instance=board)
        # 그 값을 검증한다.(유효성 체크)
        if board_form.is_valid():
            # board.title = board_form.cleaned_data.get('title')
            # board.content = board_form.cleaned_data.get('content')
            # board.save()
            board = board_form.save()
            return redirect(board)
    # 2-2. GET 요청이면, (수정하기 버튼을 눌렀을 때)
    else:
        # BoardForm을 초기화(사용자 입력값을 넣어준 상태)
        board_form = BoardForm(instance=board)
        # board_form = BoardForm(initial={'title' : board.title, 'content' : board.content})
    # context에 담겨있는 board_form은 두 가지 상황이 있다.
    # 1 - POST 요청에서 검증에 실패하였을 때, 오류 메세지가 포함된 상태
    # 2 - GET 요청에서 초기화 된 상태
    context = {'board_form' : board_form}
    return render(request, 'boards/form.html', context)
    
    

