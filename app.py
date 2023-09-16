import streamlit as st


######## 텍스트 출력 ########

st.write('1+1 =', 2)
# st.write('Below is a DataFrame: ', df, 'Above is a DataFrame')
"Hello **world**"  # Magic 라이브러리도 지원됨


## Title
st.title("Streamlit Tutorial")
## Header/Subheader
st.header("This is header")
st.subheader("This is subheader")

## Text
st.text("Hello Streamlit! 이 글은 튜토리얼")  # 텍스트 형태

# Markdown 형식을 지원
st.markdown("# This is a Markdown Title")
st.markdown("## This is a Markdown Header")
st.markdown(" - item 1\n"
            "   - item 1.1\n"
            "   - item 1.2")
            
st.markdown(" 1. item 1\n"
            "   1. item 1.1\n"
            "   2. item 1.2")
            
            
# Latex : 수식 표현
st.latex(r"Y = \alpha + \beta X_i")
## Latex-inline
st.markdown(r"회귀분석은 잔차식은 다음과 같다")

# 메세지, 예외처리
st.success("Successful")
st.info("Information!")
st.warning("This is a warning!")
st.error("This is an error!")
st.exception("Name(Error)")



#### 데이터프레임과 테이블 출력

## Load data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#GitHub에서 아이리스 데이터 다운로드
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris_df = pd.read_csv(url)

## Return table/dataframe
# table
st.table(iris_df.head())

# dataframe
st.dataframe(iris_df)
st.write(iris_df)

st.markdown("* * *")


########## 위젯 ############
# -> 반환값이 존재

# Checkbox
if st.checkbox("Show/Hide"):
    st.write("체크박스가 선택되었습니다.")

# Radio Button
status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")
    
# Select Box
occupation = st.selectbox("직군을 선택하세요.", [
    "Backend Developer",
    "Frontend Developer",
    "Engineer",
    "Scientist"
    ])
    
st.write(" 직군은", occupation, " 입니다.")

# Dropdown (MultiSelect)
location = st.multiselect("선호하는 유튜브 채널을 선택하세요.",
                            (
                                "운동",
                                "IT기기",
                                "브이로그"
                            )
)
st.write(len(location), "가지를 선택했습니다.")

# Slider
level = st.slider("레벨을 선택하세요.", 1, 5)

# Button  *Submit 기능 X
if st.button("About"):
    st.text("Streamlit을 이용한 튜토리얼입니다.")
    
# 텍스트 입력 (Input)
first_name = st.text_input("Enter your First name", "Type Here ...")
if st.button("Submit", key="first_name"):
    result = first_name.title()
    st.success(result)

# TextArea
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key="message"):
    result = message.title()
    st.success(result)

# 날짜와 시간 입력
import datetime

today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())


# 코드의 json 출력
import numpy as np  # one-line code
import pandas as pd  # code snippet

## Display Raw Code — one line
st.subheader("Display one-line code")
st.code("import numpy as np")
# Display Raw Code — snippet
st.subheader("Display code snippet")

with st.echo():
# 여기서부터 아래의 코드를 출력합니다. 
    import pandas as pd
    df = pd.DataFrame()
    
## Display JSON
st.subheader("Display JSON")
st.json({"name" : "민수", "gender": "male", "Age": 29})

# Sidebar
st.sidebar.header("사이드바 메뉴")
st.sidebar.selectbox("메뉴를 선택하세요.",
["데이터", "EDA", "코드"])


## 차트 그리기
st.subheader("Matplotlib으로 차트 그리기")

#GitHub에서 아이리스 데이터 다운로드
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris_df = pd.read_csv(url)

## Plotting
st.subheader("Matplotlib으로 차트 그리기")
fig, ax = plt.subplots()
ax = iris_df[iris_df['species']=='virginica']['petal_length'].hist() 
st.pyplot(fig)


# 레이아웃
st.title("Registeration form")

first, last = st.columns(2)
first.text_input("First Name")
last.text_input("Last Name")

email, mob = st.columns([3,1])
email.text_input("Email ID")
mob.text_input("Mob Number")

user, pw, pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password", type="password")
pw2.text_input("Retype your password", type="password")

ch, bl, sub = st.columns(3)
ch.checkbox("I Agree")
sub.button("Submit")


# 캐싱
import time

@st.cache_data  # 데이터 로딩 등 긴 실행 시간이 필요한 함수 위에 붙이기 -> 데이터 캐시 사용 (함수명 및 파라미터명이 동일해야 함)
def fetch_and_clean_data(url):
    # URL에서 데이터를 페치!
    data = pd.read_csv(url)
    
    return data
    

DATA_URL_1 = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
DATA_URL_2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/raw/titanic.csv"

#시작 시간 기록
start_time = time.time()
d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

#종료 시간 기록
end_time = time.time()
#실행 시간 계산
execution_time = end_time - start_time
#실행 시간 출력
st.write(f"총 실행 시간: {execution_time:.6f} 초")

st.write(d1.head())


#시작 시간 기록
start_time = time.time()
d2 = fetch_and_clean_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the data in d1 is the same as in d2.

#종료 시간 기록
end_time = time.time()
#실행 시간 계산
execution_time = end_time - start_time
#실행 시간 출력
st.write(f"총 실행 시간: {execution_time:.6f} 초")

st.write(d2.head())


#시작 시간 기록
start_time = time.time()
d3 = fetch_and_clean_data(DATA_URL_2)
# This is a different URL, so the function executes.

#종료 시간 기록
end_time = time.time()
#실행 시간 계산
execution_time = end_time - start_time
#실행 시간 출력
st.write(f"총 실행 시간: {execution_time:.6f} 초")


st.write(d3.head())


# 세션
st.title("Counter Example")

if 'count' not in st.session_state:
    st.session_state.count = 0
    
increment = st.button("Increment")
if increment:
    st.session_state.count += 1

decrement = st.button("Decrement")
if decrement:
    st.session_state.count -= 1
    
st.write("Count = ", st.session_state.count)


# 파일 업로드
uploaded_files = st.file_uploader("Choose a CSV file",
accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    
    
# 데이터 프로파일링
import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Linux':
    rc('font', family='Gothic') 
    
# 스트림릿 앱 생성
st.title("데이터 프로파일링 실습")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("데이터 파일 업로드", type=["csv", "xlsx"])
if uploaded_file is not None:
# 업로드한 파일을 DataFrame 으로 변환
    df = pd.read_csv(uploaded_file) # 엑셀 파일일 경우 pd.read_excel 사용
    
    # 데이터 프로파일링 
    st.header("데이터 미리보기") 
    st.write(df.head())
    
    st.header("기본 정보") 
    st.write("행 수:", df.shape[0]) 
    st.write("열 수:", df.shape[1])
    
    st.header("누락된 값") 
    missing_data = df.isnull().sum() 
    st.write(missing_data)
    
    st.header("중복된 행 수") 
    duplicated_rows = df.duplicated().sum() 
    st.write(duplicated_rows)
    
    st.header("수치형 데이터 기술 통계량") 
    numerical_stats = df.describe()
    
    st.write(numerical_stats)
    
    st.header("이상치 탐지 (상자 그림)") 
    plt.figure(figsize=(10, 6)) 
    plt.boxplot(df.select_dtypes(include=['number']).values) 
    plt.xticks(range(1, len(df.columns) + 1), df.columns, rotation=45)
        
    plt.title("Outlier detection (box plot)")
    st.pyplot(plt)
    
    st.header("데이터 분포 시각화")
    column_to_plot = st.selectbox("열 선택", df.columns)
    plt.figure(figsize=(10, 6)) 
    plt.hist(df[column_to_plot], bins=20, edgecolor='k') 
    plt.xlabel(column_to_plot)
    plt.ylabel("빈도")
    plt.title(f"{column_to_plot} Data Distribution") 
    st.pyplot(plt)
    

# IRIS 데이터 시각화
## Case 1.
import pandas as pd
import seaborn as sns


st.set_option('deprecation.showPyplotGlobalUse', False)

# 아이리스 데이터셋 불러오기 
@st.cache_data
def load_data():
    
    #GitHub에서 아이리스 데이터 다운로드
    url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
    iris_df = pd.read_csv(url)
    return iris_df

iris_data = load_data()

#스트림릿 앱 제목 설정
st.title('아이리스 데이터 시각화')

# 데이터프레임 출력 
st.subheader('아이리스 데이터셋') 
st.write(iris_data)

# 품종별 특성 분포 시각화 
st.subheader('품종별 특성 분포')
for feature in iris_data.columns[:-1]:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='species', y=feature, data=iris_data)
    plt.title(f'{feature} Distribution')
    plt.xlabel('species')
    plt.ylabel(feature)
    st.pyplot()
    
# 특성 간 상관 관계 시각화 
st.subheader('특성 간 상관 관계')
correlation_matrix = iris_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot()

# 품종별 특성 산점도 시각화 
st.subheader('품종별 특성 산점도')
sns.pairplot(iris_data, hue='species', diag_kind='kde')
st.pyplot()

## Case 2.

# 아이리스 데이터셋 불러오기
@st.cache_data
def load_data():
    #GitHub에서 아이리스 데이터 다운로드
    url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
    iris_df = pd.read_csv(url)
    return iris_df
    
iris_data = load_data()

#스트림릿 앱 제목 설정 
st.title('아이리스 데이터 시각화')

# 데이터프레임 출력 
st.subheader('아이리스 데이터셋') 
st.write(iris_data)

# 품종별 특성 분포 시각화 
st.subheader('품종별 특성 분포')
for feature in iris_data.columns[:-1]:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='species', y=feature, data=iris_data)
    plt.title(f'{feature} Distribution')
    plt.xlabel('species')
    plt.ylabel(feature)
    st.pyplot(plt)
    
# 특성 간 상관 관계 시각화 
st.subheader('특성 간 상관 관계')
correlation_matrix = iris_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot(plt)

# 품종별 특성 산점도 시각화
st.subheader('품종별 특성 산점도') 
sns.pairplot(iris_data, hue='species', diag_kind='kde') 
sns.pairplot(iris_data, hue='species', diag_kind='kde') 
st.pyplot(plt)



## 세션 값 테스트 코드
# Sessions Don’t Store Values Forever
# Storing Value
# Associate Session State With Input Widgets # Sharing Value Between Reruns
# Delete Values From Session State
#rerun 세션 값 유지 테스트 코드
import streamlit as st

input_var = st.text_input("enter a name")

st.write(f"Hello, {input_var}!")

if ("name" not in st.session_state) and (input_var != ""):
    st.session_state["name"] = input_var
    
st.write("first name you have entered: ")
if "name" in st.session_state:
    st.write(st.session_state["name"])
    
st.write(st.session_state)

# input widget 세션 값 변경 테스트 코드 import streamlit as st
input_select = st.selectbox("select a food", options= ("sushi", "steak","burger"), key="food")
st.write(st.session_state)
