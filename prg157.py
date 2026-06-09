class Candidate:
    def __init__(self, cid, name, skills):
        self.cid = cid
        self.name = name
        self.skills = set(skills)
    def display_candidate(self):
        print("\nCandidate Details")
        print("ID :", self.cid)
        print("Name :", self.name)
        print("Skills :", self.skills)
class JobOpening(Candidate):
    def __init__(self, cid, name, skills, job_title, required_skills):
        super().__init__(cid, name, skills)
        self.job_title = job_title
        self.required_skills = set(required_skills)
    def apply_job(self):
        print(f"\n{self.name} applied for {self.job_title}")
class Interview(JobOpening):
    def __init__(self, cid, name, skills, job_title,
                 required_skills, tech_score, hr_score):
        super().__init__(cid, name, skills, job_title, required_skills)
        self.tech_score = tech_score
        self.hr_score = hr_score
    def calculate_score(self):
        return (self.tech_score + self.hr_score) / 2
class RecruitmentManager(Interview):
    def __init__(self, cid, name, skills, job_title,
                 required_skills, tech_score, hr_score):
        super().__init__(cid, name, skills, job_title,
                         required_skills, tech_score, hr_score)
    def shortlist(self):
        avg_score = self.calculate_score()
        if self.required_skills.issubset(self.skills) and avg_score >= 70:
            print("\nCandidate Shortlisted")
        else:
            print("\nCandidate Rejected")
    def final_report(self):
        print("\n----- Final Selection Report -----")
        self.display_candidate()
        print("Job Title :", self.job_title )
        print("Technical Score :", self.tech_score)
        print("HR Score :", self.hr_score)
        print("Average Score :", self.calculate_score())
c1 = RecruitmentManager(101,"Rahul",{"Python", "SQL", "Java"},"Software Developer",{"Python", "SQL"},85,75)
c1.apply_job()
c1.shortlist()
c1.final_report()