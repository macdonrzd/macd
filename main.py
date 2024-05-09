import streamlit as st

# 각 페이지에서 입력된 정보를 저장할 딕셔너리들을 선언합니다.
school_info = {}
student_teacher_info = {}
curriculum_info = {}
club_info = {}
subject_evaluation_info = {}
achievement_ratio_info = {}
transcript_university_info = []
admission_results_info = []


# 페이지 1: 학교 정보 입력
def page_school_info():
    st.title("학교 정보 입력")
    administration_district = st.text_input("행정구:")
    school_name = st.text_input("학교 이름:")
    graduated_students = st.number_input("졸업생 수:", step=1, format="%d", value=0, key="graduated_students")
    four_year_college = st.number_input("4년제 진학(명):", step=1, format="%d", value=0, key="four_year_college")
    vocational_college = st.number_input("전문대 진학(명):", step=1, format="%d", value=0, key="vocational_college")

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
    total_teachers = st.number_input("총 교원 수:", step=1, format="%d", value=0, key="total_teachers")

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
        "과학탐구": ["물리1", "물리2", "화학1", "화학2", "생물1", "생물2", "지구과학1", "지구과학2", "과학탐구실험"],
        "기술가정": ["가정과 생활", "식생활과 영양", "복장과 의복", "생활과 예술", "소비자와 시장"],
        "음악": ["음악이론", "음악연주", "작곡과 편곡", "음악감상", "세계음악"],
        "미술": ["미술의 이해", "그림의 이해", "조소와 설치", "디자인과 공예", "생활공예"],
        "체육": ["운동과 건강", "체조와 발레", "무용", "기초운동", "스포츠과학"]
    }

    selected_subjects = st.multiselect("과목 선택", list(subjects.keys()))

    # 선택된 과목의 세부 과목 선택
    selected_sub_subjects = {}
    for subject in selected_subjects:
        selected_sub_subjects[subject] = st.multiselect(f"{subject} 세부 과목 선택", subjects[subject])

    # 데이터 저장
    curriculum_info[selected_grade_semester] = selected_sub_subjects

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("교육과정 편제표가 저장되었습니다.")
    if st.button("저장 삭제"):
        curriculum_info.clear()
        st.write("교육과정 편제표가 삭제되었습니다.")


# 페이지 4: 동아리 정보 입력
def page_club_info():
    st.title("동아리 정보 입력")
    selected_clubs = st.multiselect("동아리 선택", ["예체능", "학술", "인문사회", "지도부"])
    club_info["동아리 목록"] = selected_clubs

    # 선택된 동아리별 활동 내용 입력
    club_activities = {}
    for club in selected_clubs:
        activity = st.text_area(f"{club} 활동 내용:")
        club_activities[club] = activity

    # 데이터 저장
    club_info["동아리 활동 내용"] = club_activities

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("동아리 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        club_info.clear()
        st.write("동아리 정보가 삭제되었습니다.")


# 페이지 5: 교과평가 및 성취도 정보 입력
def page_subject_evaluation():
    st.title("교과평가 및 성취도 정보 입력")
    subject_name = st.text_input("교과목 이름:")
    grade1_eval_score = st.slider("1학년 평가 점수:", min_value=0, max_value=100, value=0)
    grade2_eval_score = st.slider("2학년 평가 점수:", min_value=0, max_value=100, value=0)
    grade3_eval_score = st.slider("3학년 평가 점수:", min_value=0, max_value=100, value=0)

    # 데이터 저장
    subject_evaluation_info[subject_name] = {
        "1학년 평가 점수": grade1_eval_score,
        "2학년 평가 점수": grade2_eval_score,
        "3학년 평가 점수": grade3_eval_score
    }

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("교과평가 및 성취도 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        subject_evaluation_info.clear()
        st.write("교과평가 및 성취도 정보가 삭제되었습니다.")


# 페이지 6: 학업성취도 및 입시결과 정보 입력
def page_achievement_admission():
    st.title("학업성취도 및 입시결과 정보 입력")
    transcript_university = st.text_area("대학 성적/성적표 정보:")
    admission_results = st.text_area("입시 결과 정보:")

    # 데이터 저장
    transcript_university_info.append(transcript_university)
    admission_results_info.append(admission_results)

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("학업성취도 및 입시결과 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        transcript_university_info.clear()
        admission_results_info.clear()
        st.write("학업성취도 및 입시결과 정보가 삭제되었습니다.")


def main():
    st.sidebar.title("메뉴")
    selected_page = st.sidebar.selectbox("페이지 선택", ["학교 정보 입력", "학생 수 및 교원 수 입력",
                                                         "교육과정 편제표 입력", "동아리 정보 입력",
                                                         "교과평가 및 성취도 정보 입력",
                                                         "학업성취도 및 입시결과 정보 입력"])

    if selected_page == "학교 정보 입력":
        page_school_info()
    elif selected_page == "학생 수 및 교원 수 입력":
        page_student_teacher_info()
    elif selected_page == "교육과정 편제표 입력":
        page_curriculum()
    elif selected_page == "동아리 정보 입력":
        page_club_info()
    elif selected_page == "교과평가 및 성취도 정보 입력":
        page_subject_evaluation()
    elif selected_page == "학업성취도 및 입시결과 정보 입력":
        page_achievement_admission()


if __name__ == "__main__":
    main()

