import streamlit as st

# 각 페이지에서 입력된 정보를 저장할 딕셔너리들을 선언합니다.
school_info = {}
student_teacher_info = {}
curriculum_info = {}
club_info = {}
subject_evaluation_info = {}
achievement_ratio_info = {}
admission_results_info = []
subject_preparation_info = {}


# 페이지 1: 학교 정보 입력
def page_school_info():
    st.title("학교 정보 입력")
    administration_district = st.text_input("행정구:")
    school_name = st.text_input("학교 이름:")
    graduated_students = st.number_input("졸업생 수:", step=1, format="%d", value=0)
    four_year_college = st.number_input("4년제 진학(명):", step=1, format="%d", value=0)
    vocational_college = st.number_input("전문대 진학(명):", step=1, format="%d", value=0)

    # 재수 인원 및 예비 재수 비율 계산
    retest_students_estimate = max(graduated_students - (four_year_college + vocational_college), 0)
    prep_resit_ratio_value = retest_students_estimate / graduated_students if graduated_students != 0 else 0

    # 계산 결과 출력
    st.write(f"예상 재수 인원: {retest_students_estimate} 명")
    st.write(f"예비 재수 비율: {prep_resit_ratio_value:.2%}")

    # 데이터 저장
    school_info.update({
        "행정구": administration_district,
        "학교 이름": school_name,
        "졸업생 수": graduated_students,
        "4년제 진학(명)": four_year_college,
        "전문대 진학(명)": vocational_college,
        "예상 재수 인원": retest_students_estimate,
        "예비 재수 비율": prep_resit_ratio_value
    })

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("학교 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        school_info.clear()
        st.write("학교 정보가 삭제되었습니다.")


# 페이지 2: 학생 수 및 교원 수 입력
def page_student_teacher_info():
    st.title("학생 수 및 교원 수 입력")
    grade1_students = st.number_input("1학년 학생 수:", step=1, format="%d", value=0, key="grade1_students")
    grade2_students = st.number_input("2학년 학생 수:", step=1, format="%d", value=0, key="grade2_students")
    grade3_students = st.number_input("3학년 학생 수:", step=1, format="%d", value=0, key="grade3_students")

    # 총 학생 수 및 전교생 수 계산
    total_students = grade1_students + grade2_students + grade3_students
    total_teachers = st.number_input("총 교원 수:", step=1, format="%d", value=0)

    # 전교생 수 및 교사 1인당 학생 수 계산
    total_students_text = f"전교생 수: {total_students} 명"
    if total_teachers > 0:
        students_per_teacher = total_students / total_teachers
        total_students_text += f", 교사 1인당 학생 수: {students_per_teacher:.2f} 명"

    # 데이터 저장
    student_teacher_info.update({
        "1학년 학생 수": grade1_students,
        "2학년 학생 수": grade2_students,
        "3학년 학생 수": grade3_students,
        "총 교원 수": total_teachers,
        "전교생 수": total_students
    })

    # 결과 출력
    st.write(total_students_text)

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("학생 수 및 교원 수가 저장되었습니다.")
    if st.button("저장 삭제"):
        student_teacher_info.clear()
        st.write("학생 수 및 교원 수가 삭제되었습니다.")


# 페이지 3: 교육과정 편제표 입력
def page_curriculum():
    st.title("교육과정 편제표 입력")
    selected_grade_semester = st.selectbox("학년 및 학기 선택", ["1학년 1학기", "1학년 2학기",
                                                           "2학년 1학기", "2학년 2학기",
                                                           "3학년 1학기", "3학년 2학기"])

    # 과목 및 세부 과목 선택
    subjects = {
        "국어": ["공통국어", "문학", "독서", "화법과 작문", "언어와 매체"],
        "수학": ["공통수학", "수학1", "수학2", "심화수학", "경제수학", "기하", "미적분", "확률과 통계"],
        "영어": ["공통영어", "영어1", "영어2", "영어독해", "영어작문", "영어회화", "영어듣기"],
        "사회탐구": ["통합사회", "한국사", "사회문화", "정치와 법", "경제", "세계지리", "한국지리",
                  "생활과 윤리", "윤리와 사상", "세계사", "동아시아사"],
        "과학탐구": ["물리1", "물리2", "생명과학1", "생명과학2", "지구과학1", "지구과학2", "화학1", "화학2", "통합과학"]
    }

    selected_subject = st.selectbox("과목 선택", list(subjects.keys()))
    selected_sub_subject = st.selectbox(f"{selected_subject} 선택", subjects[selected_subject])

    # 시수 입력란 추가
    lesson_hours = st.number_input("시수 입력:", min_value=0, step=1)

    # 데이터 저장
    curriculum_info.setdefault(selected_grade_semester, []).append({
        "과목": selected_subject,
        "세부 과목": selected_sub_subject,
        "시수": lesson_hours
    })

    if st.button("저장"):
        st.write("교육과정 편제표가 저장되었습니다.")
    if st.button("저장 삭제"):
        if selected_grade_semester in curriculum_info:
            del curriculum_info[selected_grade_semester]
            st.write("교육과정 편제표가 삭제되었습니다.")


# 페이지 4: 동아리 정보 입력
def page_club_info():
    st.title("동아리 정보 입력")
    club_name = st.text_input("동아리 이름:")
    club_type = st.radio("동아리 유형", ["정규", "자율"])
    club_activity = st.text_area("동아리 활동 내용:", height=100)

    # 데이터 저장
    club_info[club_name] = {
        "동아리 이름": club_name,
        "동아리 유형": club_type,
        "동아리 활동 내용": club_activity
    }

    if st.button("저장"):
        st.write("동아리 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        if club_name in club_info:
            del club_info[club_name]
            st.write("동아리 정보가 삭제되었습니다.")

# 페이지 5: 과목 평가 방법 입력
def page_subject_evaluation():
    st.title("과목 평가 방법 입력")
    selected_grade_semester = st.selectbox("학년 및 학기 선택", ["1학년 1학기", "1학년 2학기",
                                                           "2학년 1학기", "2학년 2학기",
                                                           "3학년 1학기", "3학년 2학기"])

    selected_subject = st.selectbox("과목 선택", ["국어", "수학", "영어", "사회탐구", "과학탐구"])

    evaluation_type = st.radio("평가 유형", ["지필평가", "수행평가"])
    if evaluation_type == "지필평가":
        evaluation_method = st.text_input("지필 유형 입력:")
    else:
        evaluation_method = st.text_input("수행 유형 입력:")  # 직접 입력란으로 변경

    weight = st.number_input("반영 비율:", min_value=0.0, step=0.1)  # 수정된 부분
    evaluation_count = st.number_input("평가 횟수:", min_value=0, step=1, value=0)
    basic_score = st.number_input("기본 점수:", min_value=0, step=1, value=0)
    evaluation_timing = st.text_input("평가 시기:")

    # 데이터 저장
    subject_evaluation_info.setdefault(selected_grade_semester, []).append({
        "과목": selected_subject,
        "평가 유형": evaluation_type,
        "평가 방법": evaluation_method,
        "반영 비율": weight,
        "평가 횟수": evaluation_count,
        "기본 점수": basic_score,
        "평가 시기": evaluation_timing
    })

    if st.button("저장"):
        st.write("과목 평가 방법이 저장되었습니다.")
    if st.button("저장 삭제"):
        if selected_grade_semester in subject_evaluation_info:
            del subject_evaluation_info[selected_grade_semester]
            st.write("과목 평가 방법이 삭제되었습니다.")


# 페이지 6: 학업 성취도별 분포 비율 입력
def page_achievement_ratio():
    st.title("학업 성취도별 분포 비율 입력")
    selected_grade_semester = st.selectbox("학년 및 학기 선택", ["1학년 1학기", "1학년 2학기",
                                                           "2학년 1학기", "2학년 2학기",
                                                           "3학년 1학기", "3학년 2학기"])

    subjects = {
        "국어": ["공통국어", "문학", "독서", "화법과 작문", "언어와 매체"],
        "수학": ["공통수학", "수학1", "수학2", "심화수학", "경제수학", "기하", "미적분", "확률과 통계"],
        "영어": ["공통영어", "영어1", "영어2", "영어독해", "영어작문", "영어회화", "영어듣기"],
        "사회탐구": ["통합사회", "한국사", "사회문화", "정치와 법", "경제", "세계지리", "한국지리",
                  "생활과 윤리", "윤리와 사상", "세계사", "동아시아사"],
        "과학탐구": ["물리1", "물리2", "생명과학1", "생명과학2", "지구과학1", "지구과학2", "화학1", "화학2", "통합과학"]
    }

    # 평균값 및 표준편차 입력
    selected_subject = st.selectbox("과목 선택", list(subjects.keys()))
    selected_sub_subject = st.selectbox(f"{selected_subject} 선택", subjects[selected_subject])
    mean = st.number_input(f"{selected_sub_subject} 평균값 입력", min_value=0.0, step=0.1)
    std_deviation = st.number_input(f"{selected_sub_subject} 표준편차 입력", min_value=0.0, step=0.1)

    st.subheader("성취도 비율 입력")
    with st.form(key=f"{selected_subject}_{selected_sub_subject}"):
        col1, col2, col3, col4, col5 = st.columns(5)
        ratio_A = col1.number_input("A 비율", min_value=0.0, step=0.1)
        ratio_B = col2.number_input("B 비율", min_value=0.0, step=0.1)
        ratio_C = col3.number_input("C 비율", min_value=0.0, step=0.1)
        ratio_D = col4.number_input("D 비율", min_value=0.0, step=0.1)
        ratio_E = col5.number_input("E 비율", min_value=0.0, step=0.1)
        submit_button = st.form_submit_button(label='저장')

    # 데이터 저장
    if submit_button:
        achievement_ratio_info.setdefault(selected_grade_semester, []).append({
            "과목": selected_subject,
            "세부 과목": selected_sub_subject,
            "성취도 비율": {
                "평균값": mean,
                "표준편차": std_deviation,
                "A 비율": ratio_A,
                "B 비율": ratio_B,
                "C 비율": ratio_C,
                "D 비율": ratio_D,
                "E 비율": ratio_E
            }
        })

        st.write("학업 성취도별 분포 비율이 저장되었습니다.")
    if st.button("저장 삭제"):
        if selected_grade_semester in achievement_ratio_info:
            del achievement_ratio_info[selected_grade_semester]
            st.write("학업 성취도별 분포 비율이 삭제되었습니다.")


# 페이지 7: 대입 입결 정보 입력
def page_admission_results():
    st.title("대입 입결 정보 입력")
    university_name = st.text_input("대학 이름:")
    department_name = st.text_input("학과 이름:")
    academic_score = st.number_input("내신 성적(전교과):", min_value=0.0, step=0.1)
    admission_type = st.text_input("전형 이름:")
    admission_result = st.selectbox("합격 여부", ["합격", "불합격", "추가 합격"])

    # 데이터 저장
    admission_results_info.append({
        "대학 이름": university_name,
        "학과 이름": department_name,
        "내신 성적(전교과)": academic_score,
        "전형 이름": admission_type,
        "합격 여부": admission_result
    })

    if st.button("저장"):
        st.write("대입 입결 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        admission_results_info.clear()
        st.write("대입 입결 정보가 삭제되었습니다.")


# 페이지 8: 과목별 준비 사항 및 특징 입력
def page_subject_preparation():
    st.title("과목별 준비 사항 및 특징 입력")
    subjects = {
        "국어": ["공통국어", "문학", "독서", "화법과 작문", "언어와 매체"],
        "수학": ["공통수학", "수학1", "수학2", "심화수학", "경제수학", "기하", "미적분", "확률과 통계"],
        "영어": ["공통영어", "영어1", "영어2", "영어독해", "영어작문", "영어회화", "영어듣기"],
        "사회탐구": ["통합사회", "한국사", "사회문화", "정치와 법", "경제", "세계지리", "한국지리",
                  "생활과 윤리", "윤리와 사상", "세계사", "동아시아사"],
        "과학탐구": ["물리1", "물리2", "생명과학1", "생명과학2", "지구과학1", "지구과학2", "화학1", "화학2", "통합과학"]
    }

    selected_subject = st.selectbox("과목 선택", list(subjects.keys()))
    selected_sub_subject = st.selectbox(f"{selected_subject} 선택", subjects[selected_subject])

    st.subheader("준비 사항 및 특징 입력")
    preparation_and_features = st.text_area("준비 사항 및 특징:", height=200)

    # 데이터 저장
    curriculum_info.setdefault(selected_subject, {})[selected_sub_subject] = preparation_and_features

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("과목별 준비 사항 및 특징이 저장되었습니다.")
    if st.button("저장 삭제"):
        if selected_subject in curriculum_info and selected_sub_subject in curriculum_info[selected_subject]:
            del curriculum_info[selected_subject][selected_sub_subject]
            st.write("과목별 준비 사항 및 특징이 삭제되었습니다.")


# 페이지 9: 입력된 정보 표로 정리 및 자동 저장
def page_summary():
    st.title("입력된 정보 요약")

    # 학교 정보 요약
    st.header("학교 정보")
    st.table([school_info])

    # 학생 수 및 교원 수 요약
    st.header("학생 수 및 교원 수")
    st.table([student_teacher_info])

    # 교육과정 편제표 요약
    st.header("교육과정 편제표")
    for key, value in curriculum_info.items():
        st.subheader(key)
        st.table(value)

    # 동아리 정보 요약
    st.header("동아리 정보")
    for club in club_info.values():
        st.table([club])

    # 과목 평가 정보 요약
    st.header("과목 평가 정보")
    for key, value in subject_evaluation_info.items():
        st.subheader(key)
        st.table(value)

    # 학업 성취도별 분포 비율 요약
    st.header("학업 성취도별 분포 비율")
    for key, value in achievement_ratio_info.items():
        st.subheader(key)
        for sub_key, sub_value in value.items():
            st.subheader(sub_key)
            st.table([sub_value])

    # 입시 결과 요약
    st.header("입시 결과")
    st.table([{"입시 결과": "\n".join(admission_results_info)}])

    # 과목별 대비 준비율 요약
    st.header("과목별 대비 준비율")
    for key, value in subject_preparation_info.items():
        st.subheader(key)
        st.table([value])


# Streamlit 애플리케이션 설정
def main():
    st.sidebar.title("메뉴")
    page = st.sidebar.radio("이동", ["학교 정보 입력", "학생 수 및 교원 수 입력", "교육과정 편제표 입력",
                                     "동아리 정보 입력", "과목 평가 정보 입력", "학업 성취도별 분포 비율 입력",
                                     "입시 결과 입력", "과목별 대비 준비율 입력", "입력된 정보 요약"])

    if page == "학교 정보 입력":
        page_school_info()
    elif page == "학생 수 및 교원 수 입력":
        page_student_teacher_info()
    elif page == "교육과정 편제표 입력":
        page_curriculum()
    elif page == "동아리 정보 입력":
        page_club_info()
    elif page == "과목 평가 정보 입력":
        page_subject_evaluation_info()
    elif page == "학업 성취도별 분포 비율 입력":
        page_achievement_ratio()
    elif page == "입시 결과 입력":
        page_admission_results()
    elif page == "과목별 대비 준비율 입력":
        page_subject_preparation()
    elif page == "입력된 정보 요약":
        page_summary()


if __name__ == "__main__":
    main()
