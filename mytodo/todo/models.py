from django.db import models

# Create your models here.
class Todo(models.Model):
    # 코드에는 없지만 Django가 기본으로 제공하는 pk인 id 필드도 포함되어있음
    # 이후 id값을 pk로 활용해서 Todo 데이터를 구분할 것
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) # TextField: 긴 텍스트 저장, 최대 길이 제한 없음
    created = models.DateTimeField(auto_now_add=True) # 날짜와 시간 데이터 저장
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self): # 객체가 문자열로 표현될 때 반환할 값을 정의
        return self.title # title 필드를 반환한다 => 예를들어 관리자 페이지에서 Todo 갳페 목록을 볼 때, title로 표시됨
    
# CharField
# 타입: 문자열 (짧은 텍스트)
# 속성:
# max_length: 필수. 문자열의 최대 길이를 지정합니다.
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.

# TextField
# 타입: 문자열 (긴 텍스트)
# 속성:
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.

# IntegerField
# 타입: 정수
# 속성:
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.

# BooleanField
# 타입: 불리언 (True/False)
# 속성:
# default: 필드의 기본값을 지정합니다. 기본값은 False입니다.

# DateTimeField
# 타입: 날짜 및 시간
# 속성:
# auto_now: 객체가 저장될 때마다 현재 날짜와 시간으로 업데이트됩니다.
# auto_now_add: 객체가 처음 생성될 때 현재 날짜와 시간으로 설정됩니다.
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.

# DateField
# 타입: 날짜
# 속성:
# auto_now: 객체가 저장될 때마다 현재 날짜로 업데이트됩니다.
# auto_now_add: 객체가 처음 생성될 때 현재 날짜로 설정됩니다.
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.

# FloatField
# 타입: 부동 소수점 숫자
# 속성:
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.

# EmailField
# 타입: 이메일 주소 (문자열)
# 속성:
# max_length: 문자열의 최대 길이를 지정합니다. 기본값은 254자입니다.
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.

# URLField
# 타입: URL (문자열)
# 속성:
# max_length: 문자열의 최대 길이를 지정합니다. 기본값은 200자입니다.
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.

# ForeignKey
# 타입: 외래 키 (다른 모델과의 관계)
# 속성:
# to: 참조할 다른 모델을 지정합니다.
# on_delete: 참조된 객체가 삭제될 때의 동작을 지정합니다. 예: CASCADE-부모 객체가 삭제되면 자식 객체도 자동으로 삭제, SET_NULL, PROTECT 등.
# related_name: 역참조 시 사용할 이름을 지정합니다.
# blank: True일 경우, 필드가 빈 값이어도 유효합니다.
# null: True일 경우, 데이터베이스에서 이 필드는 NULL 값을 가질 수 있습니다.
# default: 필드의 기본값을 지정합니다.