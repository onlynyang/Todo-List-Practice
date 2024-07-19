from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request): # request: 사용자의 요청정보를 담는 객체
    todos = Todo.objects.filter(complete = False) # complete가 Fasle인 모든 Todo 객체를 쿼리(데베에서 데이터를 가져옴)
    return render(request, 'todo/todo_list.html', {'todos': todos}) # {}: 템플릿에 전달할 변수 이름 / 'todos': 템플릿에서 사용할 변수 이름 / todos: 그 변수가 가리키는 데이터
    # request: 사용자의 요청 정보를 담고있음

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk) # 객체의 id(기본키)가 pk와 일치하는지 객체를 검색 / pk는 url에서 추출한 값
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_post(request):
    if request.method == "POST": # 요청 메소드 확인
        form = TodoForm(request.POST) # POST로 TodoForm 인스턴스 생성
        if form.is_valid(): # 유효성 검사
            todo = form.save(commit=False) # commit=False : 데베에 저장 않고 객체만 생성 -> 추가 데이터 처리 또는 유효성 검사(특정 조건을 만족하지 않으면 저장하지 않고 에러메시지 띄우는 등)
            todo.save() # 이후 데베에 저장
            return redirect('todo_list')
    else:
        form = TodoForm() # POST요청이 아니면 빈 TodoForm 인스턴스를 생성해서 폼을 초기화 = 폼을 처음 로드할 때 
    return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo) # 제출된 데이터로 폼 초기화
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo) # 기존 데이터를 폼에 미리 채워줌
    return render(request, 'todo/todo_post.html', {'form': form})

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones':dones})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')


# request : 요청을 담는 객체 생성
# request.method: HTTP 요청의 메서드(GET, POST 등)
# request.GET: HTTP GET 요청으로 전송된 데이터를 담고 있는 딕셔너리
# request.POST: HTTP POST 요청으로 전송된 데이터를 담고 있는 딕셔너리
# request.FILES: HTTP POST 요청으로 전송된 파일 데이터를 담고 있는 딕셔너리
# request.session: 사용자 세션 정보를 담고 있는 세션 객체
# request.path: 요청한 URL의 경로 부분