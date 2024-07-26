import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# firebase database 인증 및 앱 초기화
cred = credentials.Certificate("YOUR_SERVICE_ACCOUNT_KEY.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'YOUR_REALTIME_DATABSE_URL'
})

# 기본 위치 지정
ref = db.reference()
child_1_ref = ref.child('child_1')
# 키, 배열
child_1_ref.update({'0': ['one','two','three']})
# child_1
print(child_1_ref.get())
# [['one', 'two', 'three']]

# 키, 값
child_2_ref = ref.child('child_2')
child_2_ref.update({'0' : 'one'})
child_2_ref.update({'1' : 'two'})
child_2_ref.update({'2' : 'three'})
# child_2
print(child_2_ref.get())
# ['one', 'two', 'three']