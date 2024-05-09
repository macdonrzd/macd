import streamlit as st

# 각 페이지에서 입력된 정보를 저장할 딕셔너리들을 선언합니다.
school_info = {}
student_teacher_info = {}
curriculum_info = {}
club_info = {}
subject_evaluation_info = {}
achievement_ratio_info = {}
admission_results_info = {}
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
    grade1_students = st.number_input("1학년 학생 수:", step=1, format="%d", value=0)
    grade2_students = st.number_input("2학년 학생 수:", step=1, format="%d", value=0)
    grade3_students = st.number_input("3학년 학생 수:", step=1, format="%d", value=0)

    # 총 학생 수 계산
    total_students = grade1_students + grade2_students + grade3_students

    # 데이터 저장
    student_teacher_info.update({
        "1학년 학생 수": grade1_students,
        "2학년 학생 수": grade2_students,
        "3학년 학생 수": grade3_students,
        "총 교원 수": st.number_input("총 교원 수:", step=1, format="%d", value=0),
        "전교생 수": total_students
    })

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
            curriculum_info[selected_grade_semester].pop()
            st.write("최신 항목이 삭제되었습니다.")
        else:
            st.write("저장된 항목이 없습니다.")


# 페이지 4: 동아리 활동 정보 입력
def page_club_info():
    st.title("동아리 활동 정보 입력")
    club_name = st.text_input("동아리 이름:")
    club_activities = st.text_area("동아리 활동 내용:", height=100)

    # 데이터 저장
    club_info[club_name] = club_activities

    if st.button("저장"):
        st.write("동아리 활동 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        club_info.pop(club_name, None)
        st.write("동아리 활동 정보가 삭제되었습니다.")


# 페이지 5: 교과평가 정보 입력
def page_subject_evaluation():
    st.title("교과평가 정보 입력")
    subject_name = st.text_input("교과목 이름:")
    evaluation_criteria = st.text_area("평가 기준:", height=100)

    # 데이터 저장
    subject_evaluation_info[subject_name] = evaluation_criteria

    if st.button("저장"):
        st.write("교과평가 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        subject_evaluation_info.pop(subject_name, None)
        st.write("교과평가 정보가 삭제되었습니다.")


# 페이지 6: 성취도 비율 정보 입력
def page_achievement_ratio():
    st.title("성취도 비율 정보 입력")
    achievement_subject = st.text_input("성취도 비율 대상 과목:")
    achievement_ratio = st.number_input("성취도 비율(%):", min_value=0.0, max_value=100.0, step=0.1)

    # 데이터 저장
    achievement_ratio_info[achievement_subject] = achievement_ratio

    if st.button("저장"):
        st.write("성취도 비율 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        achievement_ratio_info.pop(achievement_subject, None)
        st.write("성취도 비율 정보가 삭제되었습니다.")


# 페이지 7: 입시 결과 정보 입력
def page_admission_results():
    st.title("입시 결과 정보 입력")
    university_name = st.text_input("입시 대학 이름:")
    number_admitted = st.number_input("입학자 수:", step=1, format="%d", value=0)

    # 데이터 저장
    admission_results_info[university_name] = number_admitted

    if st.button("저장"):
        st.write("입시 결과 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        admission_results_info.pop(university_name, None)
        st.write("입시 결과 정보가 삭제되었습니다.")


# 페이지 8: 과목 별 수업 준비 정보 입력
def page_subject_preparation():
    st.title("과목 별 수업 준비 정보 입력")
    subject_name = st.text_input("과목 이름:")
    preparation_info = st.text_area("수업 준비 내용:", height=100)

    # 데이터 저장
    subject_preparation_info[subject_name] = preparation_info

    if st.button("저장"):
        st.write("수업 준비 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        subject_preparation_info.pop(subject_name, None)
        st.write("수업 준비 정보가 삭제되었습니다.")


# 페이지 렌더링 함수
def render_page(page):
    if page == "학교 정보 입력":
        page_school_info()
    elif page == "학생 수 및 교원 수 입력":
        page_student_teacher_info()
    elif page == "교육과정 편제표 입력":
        page_curriculum()
    elif page == "동아리 활동 정보 입력":
        page_club_info()
    elif page == "교과평가 정보 입력":
        page_subject_evaluation()
    elif page == "성취도 비율 정보 입력":
        page_achievement_ratio()
    elif page == "입시 결과 정보 입력":
        page_admission_results()
    elif page == "과목 별 수업 준비 정보 입력":
        page_subject_preparation()


# 사이드바에 페이지 선택 메뉴 표시
page = st.sidebar.selectbox("페이지 선택", ["학교 정보 입력", "학생 수 및 교원 수 입력",
                                           "교육과정 편제표 입력", "동아리 활동 정보 입력",
                                           "교과평가 정보 입력", "성취도 비율 정보 입력",
                                           "입시 결과 정보 입력", "과목 별 수업 준비 정보 입력"])

# 페이지 렌더링
render_page(page)

