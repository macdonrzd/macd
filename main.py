import streamlit as st

# 전역 변수로 모든 페이지에서 공유할 정보를 선언합니다.
school_info = {}
student_teacher_info = {}
curriculum_info = {}
club_info = {}
subject_evaluation_info = {}
achievement_ratio_info = {}
admission_results_info = []
subject_preparation_info = {}
saved_info = False  # 정보가 저장되었는지 여부를 표시하기 위한 변수

# 페이지 1: 학교 정보 입력
def page_school_info():
    global school_info, saved_info

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
    school_info = {
        "행정구": administration_district,
        "학교 이름": school_name,
        "졸업생 수": graduated_students,
        "4년제 진학(명)": four_year_college,
        "전문대 진학(명)": vocational_college,
        "예상 재수 인원": retest_students_estimate,
        "예비 재수 비율": prep_resit_ratio_value
    }

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("학교 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        school_info.clear()
        saved_info = False
        st.write("학교 정보가 삭제되었습니다.")


# 페이지 2: 학생 수 및 교원 수 입력
def page_student_teacher_info():
    global student_teacher_info, saved_info

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
    student_teacher_info = {
        "1학년 학생 수": grade1_students,
        "2학년 학생 수": grade2_students,
        "3학년 학생 수": grade3_students,
        "총 교원 수": total_teachers,
        "전교생 수": total_students
    }

    # 결과 출력
    st.write(total_students_text)

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("학생 수 및 교원 수가 저장되었습니다.")
    if st.button("저장 삭제"):
        student_teacher_info.clear()
        saved_info = False
        st.write("학생 수 및 교원 수가 삭제되었습니다.")


# 페이지 3: 교육과정 편제표 입력
def page_curriculum():
    global curriculum_info, saved_info

    st.title("교육과정 편제표 입력")
    selected_grade_semester = st.selectbox("학년 및 학기 선택", ["1학년 1학기", "1학년 2학기",
                                                           "2학년 1학기", "2학년 2학기",
                                                           "3학년 1학기", "3학년 2학기"])

    # 과목 및 세부 과목 선택
    subjects = {
        "국어": ["공통국어", "문학", "독서", "화법과 작문", "언어와 매체"],
        "수학": ["공통수학", "수학1", "수학2", "심화수학", "경제수학", "기하", "미적분", "확률과 통계"],
        "영어": ["공통영어", "문법", "독해", "듣기와 말하기", "쓰기"],
        "사회": ["사회문화", "경제", "사회탐구", "세계사", "한국사", "동아시아사"],
        "과학": ["물리학", "화학", "생명과학", "지구과학"],
        "기술가정": ["가정과 생활", "생활과 윤리", "가정과 과학", "가정경제", "생활예술", "식생활과 건강", "의복과 패션", "주거와 인테리어"],
        "체육": ["체육"]
    }
    selected_subject = st.selectbox("과목 선택", list(subjects.keys()))
    selected_subtopic = st.multiselect("세부 과목 선택", subjects[selected_subject])

    # 데이터 저장
    if selected_grade_semester not in curriculum_info:
        curriculum_info[selected_grade_semester] = {}
    curriculum_info[selected_grade_semester][selected_subject] = selected_subtopic

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("교육과정 편제표가 저장되었습니다.")
    if st.button("저장 삭제"):
        curriculum_info[selected_grade_semester].pop(selected_subject, None)
        saved_info = False
        st.write("교육과정 편제표가 삭제되었습니다.")


# 페이지 4: 동아리 정보 입력
def page_club_info():
    global club_info, saved_info

    st.title("동아리 정보 입력")
    club_name = st.text_input("동아리 이름:")
    club_description = st.text_area("동아리 소개:")

    # 데이터 저장
    club_info[club_name] = club_description

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("동아리 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        club_info.pop(club_name, None)
        saved_info = False
        st.write("동아리 정보가 삭제되었습니다.")


# 페이지 5: 교과평가 정보 입력
def page_subject_evaluation_info():
    global subject_evaluation_info, saved_info

    st.title("교과평가 정보 입력")
    subject = st.text_input("과목:")
    evaluation_criteria = st.text_area("평가 기준 및 방법:")

    # 데이터 저장
    subject_evaluation_info[subject] = evaluation_criteria

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("교과평가 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        subject_evaluation_info.pop(subject, None)
        saved_info = False
        st.write("교과평가 정보가 삭제되었습니다.")


# 페이지 6: 성취도 평가 비율 입력
def page_achievement_ratio_info():
    global achievement_ratio_info, saved_info

    st.title("성취도 평가 비율 입력")
    evaluation_type = st.text_input("평가 유형(중간고사, 기말고사 등):")
    ratio = st.number_input("성취도 비율(%):", step=1, format="%d", value=0)

    # 데이터 저장
    achievement_ratio_info[evaluation_type] = ratio

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("성취도 평가 비율이 저장되었습니다.")
    if st.button("저장 삭제"):
        achievement_ratio_info.pop(evaluation_type, None)
        saved_info = False
        st.write("성취도 평가 비율이 삭제되었습니다.")


# 페이지 7: 입시 결과 입력
def page_admission_results_info():
    global admission_results_info, saved_info

    st.title("입시 결과 입력")
    university_name = st.text_input("대학 이름:")
    admission_rate = st.number_input("합격률(%):", step=0.01, format="%f", value=0.0)

    # 데이터 저장
    admission_results_info.append({"대학 이름": university_name, "합격률": admission_rate})

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("입시 결과가 저장되었습니다.")
    if st.button("저장 삭제"):
        admission_results_info.pop()
        saved_info = False
        st.write("입시 결과가 삭제되었습니다.")


# 페이지 8: 과목 별 시험 대비 정보 입력
def page_subject_preparation_info():
    global subject_preparation_info, saved_info

    st.title("과목 별 시험 대비 정보 입력")
    subject_name = st.text_input("과목:")
    preparation_tips = st.text_area("시험 대비 팁 및 방법:")

    # 데이터 저장
    subject_preparation_info[subject_name] = preparation_tips

    # 저장 및 삭제 버튼
    if st.button("저장"):
        saved_info = True
        st.write("과목 별 시험 대비 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        subject_preparation_info.pop(subject_name, None)
        saved_info = False
        st.write("과목 별 시험 대비 정보가 삭제되었습니다.")


# 페이지 렌더링 함수
def render_page():
    page = st.sidebar.radio("페이지 선택", ["학교 정보", "학생 및 교원 정보", "교육과정", "동아리 정보",
                                          "교과평가 정보", "성취도 평가 비율", "입시 결과", "과목 별 시험 대비 정보"])

    if page == "학교 정보":
        page_school_info()
    elif page == "학생 및 교원 정보":
        page_student_teacher_info()
    elif page == "교육과정":
        page_curriculum()
    elif page == "동아리 정보":
        page_club_info()
    elif page == "교과평가 정보":
        page_subject_evaluation_info()
    elif page == "성취도 평가 비율":
        page_achievement_ratio_info()
    elif page == "입시 결과":
        page_admission_results_info()
    elif page == "과목 별 시험 대비 정보":
        page_subject_preparation_info()


# 메인 함수
def main():
    global saved_info

    st.title("학교 관리 시스템")
    saved_info = False

    render_page()

    # 페이지 변경 시 저장 안 된 데이터가 있다면 알림
    if not saved_info:
        st.warning("저장되지 않은 정보가 있습니다.")


if __name__ == "__main__":
    main()
