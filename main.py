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
    preparation = st.text_area("과목별 준비 사항 및 특징")

    # 데이터 저장
    if selected_grade_semester not in curriculum_info:
        curriculum_info[selected_grade_semester] = {}
    curriculum_info[selected_grade_semester].update({selected_sub_subject: preparation})

    # 결과 출력
    st.write(f"{selected_grade_semester}의 {selected_subject} - {selected_sub_subject} 정보가 저장되었습니다.")

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("교육과정 편제표 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        if selected_grade_semester in curriculum_info and selected_sub_subject in curriculum_info[selected_grade_semester]:
            del curriculum_info[selected_grade_semester][selected_sub_subject]
            st.write("교육과정 편제표 정보가 삭제되었습니다.")


# 페이지 4: 동아리 정보 입력
def page_club_info():
    st.title("동아리 정보 입력")
    club_name = st.text_input("동아리 이름:")
    club_description = st.text_area("동아리 소개 및 활동 내용")

    # 데이터 저장
    club_info.update({club_name: club_description})

    # 결과 출력
    st.write(f"{club_name} 동아리 정보가 저장되었습니다.")

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("동아리 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        if club_name in club_info:
            del club_info[club_name]
            st.write("동아리 정보가 삭제되었습니다.")


# 페이지 5: 과목 평가 방법 입력
def page_subject_evaluation():
    st.title("과목 평가 방법 입력")
    subject_name = st.text_input("과목 이름:")
    evaluation_method = st.text_area("과목 평가 방법")

    # 데이터 저장
    subject_evaluation_info.update({subject_name: evaluation_method})

    # 결과 출력
    st.write(f"{subject_name} 과목 평가 방법이 저장되었습니다.")

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("과목 평가 방법이 저장되었습니다.")
    if st.button("저장 삭제"):
        if subject_name in subject_evaluation_info:
            del subject_evaluation_info[subject_name]
            st.write("과목 평가 방법이 삭제되었습니다.")


# 페이지 6: 학업 성취도별 분포 비율 입력
def page_achievement_ratio():
    st.title("학업 성취도별 분포 비율 입력")
    achievement_ratio_info.clear()  # 이전에 입력된 정보를 초기화합니다.
    for i in range(1, 6):
        achievement_level = st.number_input(f"{i}학년 성취도 레벨:", min_value=0, step=0.01)
        ratio = st.number_input(f"{i}학년 학생 비율:", min_value=0, step=0.01, max_value=100)
        achievement_ratio_info[f"{i}학년 성취도"] = {"비율": ratio, "성취도 레벨": achievement_level}

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("학업 성취도별 분포 비율이 저장되었습니다.")
    if st.button("저장 삭제"):
        achievement_ratio_info.clear()
        st.write("학업 성취도별 분포 비율이 삭제되었습니다.")


# 페이지 7: 대입 입결 정보 입력
def page_admission_results_info():
    st.title("대입 입결 정보 입력")
    university_name = st.text_input("대학 이름:")
    admission_ratio = st.number_input("합격 비율(%):", min_value=0, step=0.01, max_value=100)
    average_score = st.number_input("평균 입시 성적:", step=0.01)
    entrance_exam_contents = st.text_area("입시시험 내용 및 대비 방법")

    # 데이터 저장
    admission_results_info.append({
        "대학 이름": university_name,
        "합격 비율": admission_ratio,
        "평균 입시 성적": average_score,
        "입시시험 내용": entrance_exam_contents
    })

    # 결과 출력
    st.write(f"{university_name} 대학 정보가 저장되었습니다.")

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("대입 입결 정보가 저장되었습니다.")
    if st.button("저장 삭제"):
        if admission_results_info:
            admission_results_info.pop()
            st.write("대입 입결 정보가 삭제되었습니다.")


# 페이지 8: 과목별 준비 사항 및 특징 입력
def page_subject_preparation():
    st.title("과목별 준비 사항 및 특징 입력")
    st.write("학년 및 학기를 선택하고 해당 과목에 대한 준비 사항 및 특징을 입력하세요.")
    if curriculum_info:
        for grade_semester, subjects in curriculum_info.items():
            st.subheader(f"{grade_semester} 과목별 준비 사항 및 특징 입력")
            for subject, _ in subjects.items():
                preparation = st.text_area(f"{subject} - 준비 사항 및 특징")
                if preparation:
                    curriculum_info[grade_semester][subject] = preparation

    # 저장 및 삭제 버튼
    if st.button("저장"):
        st.write("과목별 준비 사항 및 특징이 저장되었습니다.")
    if st.button("저장 삭제"):
        for grade_semester, subjects in curriculum_info.items():
            for subject, _ in subjects.items():
                curriculum_info[grade_semester][subject] = ""
        st.write("과목별 준비 사항 및 특징이 삭제되었습니다.")


# 페이지 9: 입력된 정보 요약 및 저장 기능
def page_summary_and_save():
    st.title("입력된 정보 요약 및 저장")

    st.subheader("1. 학교 정보")
    if school_info:
        st.write(school_info)
    else:
        st.write("학교 정보가 입력되지 않았습니다.")

    st.subheader("2. 학생 수 및 교원 수")
    if student_teacher_info:
        st.write(student_teacher_info)
    else:
        st.write("학생 수 및 교원 수가 입력되지 않았습니다.")

    st.subheader("3. 교육과정 편제표")
    if curriculum_info:
        st.write(curriculum_info)
    else:
        st.write("교육과정 편제표가 입력되지 않았습니다.")

    st.subheader("4. 동아리 정보")
    if club_info:
        st.write(club_info)
    else:
        st.write("동아리 정보가 입력되지 않았습니다.")

    st.subheader("5. 과목별 성적평가")
    if subject_evaluation_info:
        st.write(subject_evaluation_info)
    else:
        st.write("과목별 성적평가가 입력되지 않았습니다.")

    st.subheader("6. 학업 성취도별 분포 비율")
    if achievement_ratio_info:
        st.write(achievement_ratio_info)
    else:
        st.write("학업 성취도별 분포 비율이 입력되지 않았습니다.")

    st.subheader("7. 대입 입결 정보")
    if admission_results_info:
        st.write(admission_results_info)
    else:
        st.write("대입 입결 정보가 입력되지 않았습니다.")

    st.subheader("8. 과목별 준비 사항 및 특징")
    if curriculum_info:
        for subject, details in curriculum_info.items():
            for sub_subject, preparation in details.items():
                st.write(f"{subject} - {sub_subject}: {preparation}")
    else:
        st.write("과목별 준비 사항 및 특징이 입력되지 않았습니다.")

    # 모든 입력 내용을 저장하는 버튼
    if st.button("전체 정보 저장"):
        with open("saved_information.txt", "w") as file:
            file.write("1. 학교 정보\n")
            file.write(str(school_info) + "\n\n")
            file.write("2. 학생 수 및 교원 수\n")
            file.write(str(student_teacher_info) + "\n\n")
            file.write("3. 교육과정 편제표\n")
            file.write(str(curriculum_info) + "\n\n")
            file.write("4. 동아리 정보\n")
            file.write(str(club_info) + "\n\n")
            file.write("5. 과목별 성적평가\n")
            file.write(str(subject_evaluation_info) + "\n\n")
            file.write("6. 학업 성취도별 분포 비율\n")
            file.write(str(achievement_ratio_info) + "\n\n")
            file.write("7. 대입 입결 정보\n")
            file.write(str(admission_results_info) + "\n\n")
            file.write("8. 과목별 준비 사항 및 특징\n")
            for subject, details in curriculum_info.items():
                for sub_subject, preparation in details.items():
                    file.write(f"{subject} - {sub_subject}: {preparation}\n")
        st.write("모든 정보가 saved_information.txt 파일에 저장되었습니다.")

    # 저장된 정보 출력 버튼
    if st.button("저장된 정보 출력"):
        try:
            with open("saved_information.txt", "r") as file:
                saved_info = file.read()
                st.write(saved_info)
        except FileNotFoundError:
            st.write("저장된 정보가 없습니다.")


# 페이지 선택
page_options = {
    "학교 정보 입력": page_school_info,
    "학생 수 및 교원 수 입력": page_student_teacher_info,
    "교육과정 편제표 입력": page_curriculum,
    "동아리 정보 입력": page_club_info,
    "과목 평가 방법 입력": page_subject_evaluation,
    "학업 성취도별 분포 비율 입력": page_achievement_ratio,
    "대입 입결 정보 입력": page_admission_results_info,
    "과목별 준비 사항 및 특징 입력": page_subject_preparation,
    "입력된 정보 요약 및 저장": page_summary_and_save
}

selected_page = st.sidebar.selectbox("페이지 선택", list(page_options.keys()))

# 선택된 페이지 실행
page_options[selected_page]()




