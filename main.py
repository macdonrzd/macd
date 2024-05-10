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
    administration_district = st.text_input("행정구:", key="school_admin_district")
    school_name = st.text_input("학교 이름:", key="school_name")
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
        "과학탐구": ["물리1", "물리2", "생명과학1", "생명과학2", "지구과학1", "지구과학2", "화학1", "화학2", "통합과학"],
        "기술가정": ["가정과학", "음식과 조리", "의류와 재료", "주거와 생활", "가정경제", "가정과 소비자", "디자인과 제품개발"],
        "예체능": ["음악", "미술", "체육", "무용", "연극", "실과", "기술"],
        "전공": ["자유선택", "선택과목1", "선택과목2", "심화과목1", "심화과목2"]
    }

    selected_subjects = st.multiselect("과목 선택", list(subjects.keys()))

    # 선택된 과목의 세부 과목 선택
    selected_sub_subjects = []
    for subject in selected_subjects:
        sub_subjects = st.multiselect(f"{subject}의 세부 과목 선택", subjects[subject])
        selected_sub_subjects.extend(sub_subjects)

    # 데이터 저장
    curriculum_info[selected_grade_semester] = selected_sub_subjects

    # 결과 출력
    st.write(f"선택된 과목: {selected_subjects}")
    st.write(f"선택된 세부 과목: {selected_sub_subjects}")

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("교육과정 편제표가 저장되었습니다.")
    if st.button("저장 삭제"):
        curriculum_info.clear()
        st.write("교육과정 편제표가 삭제되었습니다.")


# 페이지 4: 동아리 정보 입력
def page_club_info():
    st.title("동아리 정보 입력")
    club_name = st.text_input("동아리 이름:", key="club_name")
    num_members = st.number_input("동아리 회원 수:", step=1, format="%d", value=0, key="num_members")
    club_fee = st.number_input("동아리 회비:", step=1, format="%d", value=0, key="club_fee")

    # 데이터 저장
    club_info.update({
        "동아리 이름": club_name,
        "동아리 회원 수": num_members,
        "동아리 회비": club_fee
    })

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("동아리 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        club_info.clear()
        st.write("동아리 정보가 삭제되었습니다.")


# 페이지 5: 과목 평가 정보 입력
def page_subject_evaluation_info():
    st.title("과목 평가 정보 입력")
    subject_name = st.text_input("과목 이름:", key="subject_name")
    evaluation_criteria = st.text_area("평가 기준:", key="evaluation_criteria")
    evaluation_score = st.number_input("평가 점수:", step=0.01, format="%f", value=0.0, key="evaluation_score")

    # 데이터 저장
    subject_evaluation_info.update({
        "과목 이름": subject_name,
        "평가 기준": evaluation_criteria,
        "평가 점수": evaluation_score
    })

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("과목 평가 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        subject_evaluation_info.clear()
        st.write("과목 평가 정보가 삭제되었습니다.")


# 페이지 6: 성취도 비율 정보 입력
def page_achievement_ratio_info():
    st.title("성취도 비율 정보 입력")
    subject_name = st.text_input("과목 이름:", key="subject_name_achieve")
    achievement_ratio = st.slider("성취도 비율(%)", min_value=0, max_value=100, value=0, key="achievement_ratio")

    # 데이터 저장
    achievement_ratio_info.update({
        "과목 이름": subject_name,
        "성취도 비율": achievement_ratio
    })

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("성취도 비율 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        achievement_ratio_info.clear()
        st.write("성취도 비율 정보가 삭제되었습니다.")


# 페이지 7: 대학 입학 결과 정보 입력
def page_transcript_university_info():
    st.title("대학 입학 결과 정보 입력")
    university_name = st.text_input("대학 이름:", key="university_name")
    admission_major = st.text_input("전형 항목:", key="admission_major")
    admission_number = st.number_input("입학 인원:", step=1, format="%d", value=0, key="admission_number")

    # 데이터 저장
    transcript_university_info.append({
        "대학 이름": university_name,
        "전형 항목": admission_major,
        "입학 인원": admission_number
    })

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("대학 입학 결과 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        transcript_university_info.clear()
        st.write("대학 입학 결과 정보가 삭제되었습니다.")


# 페이지 8: 입학 결과 정보 입력
def page_admission_results_info():
    st.title("입학 결과 정보 입력")
    student_name = st.text_input("학생 이름:", key="student_name")
    admitted_university = st.text_input("입학 대학:", key="admitted_university")
    admitted_major = st.text_input("입학 학과:", key="admitted_major")

    # 데이터 저장
    admission_results_info.append({
        "학생 이름": student_name,
        "입학 대학": admitted_university,
        "입학 학과": admitted_major
    })

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("입학 결과 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        admission_results_info.clear()
        st.write("입학 결과 정보가 삭제되었습니다.")


def main():
    st.sidebar.title("메뉴")
    app_mode = st.sidebar.selectbox("메뉴를 선택하세요.",
                                    ["학교 정보 입력", "학생 수 및 교원 수 입력",
                                     "교육과정 편제표 입력", "동아리 정보 입력",
                                     "과목 평가 정보 입력", "성취도 비율 정보 입력",
                                     "대학 입학 결과 정보 입력", "입학 결과 정보 입력"])

    if app_mode == "학교 정보 입력":
        page_school_info()
    elif app_mode == "학생 수 및 교원 수 입력":
        page_student_teacher_info()
    elif app_mode == "교육과정 편제표 입력":
        page_curriculum()
    elif app_mode == "동아리 정보 입력":
        page_club_info()
    elif app_mode == "과목 평가 정보 입력":
        page_subject_evaluation_info()
    elif app_mode == "성취도 비율 정보 입력":
        page_achievement_ratio_info()
    elif app_mode == "대학 입학 결과 정보 입력":
        page_transcript_university_info()
    elif app_mode == "입학 결과 정보 입력":
        page_admission_results_info()


if __name__ == "__main__":
    main()
