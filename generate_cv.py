from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 24)
        # Title
        self.cell(0, 10, 'Jossef Choha', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'IT Developer & Problem Solver', 0, 1, 'L')
        self.set_line_width(0.5)
        self.line(10, 30, 200, 30)
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln()

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 8, title, 0, 1, 'L')
    
    def section_content(self, content):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, content)
        self.ln(2)

    def job_entry(self, role, company, duration, description):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 6, f"{role} | {company}", 0, 1)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 6, duration, 0, 1)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, description)
        self.ln(4)

pdf = PDF()
pdf.add_page()

# Contact Info
pdf.set_font('Arial', '', 10)
pdf.cell(0, 6, 'Email: jchoha2000@gmail.com | Location: Dushanbe, Tajikistan', 0, 1, 'L')
pdf.ln(5)

# Professional Summary
pdf.chapter_title('Professional Summary')
pdf.chapter_body("I am a dedicated and innovative IT professional, with a bachelor's degree in Information Technology and a strong interest in business applications, particularly in the Forex trading market. Through hands-on internships, freelance projects, and self-directed learning, I blend technical skills with business acumen to develop efficient digital solutions for business environments. After graduating in 2022, I focused on gaining practical experience through a short internship and subsequent freelance work on small-scale IT projects, such as basic web development and data automation tasks for local clients, while actively seeking full-time opportunities to build a stronger professional foundation.")

# Education
pdf.chapter_title('Education')
pdf.section_title('Bachelor of Information Technology')
pdf.section_content("Technological University of Tajikistan, Dushanbe | 2018-2022\nFinal Year Project: \"Development of a Basic Forex Trading Simulation Tool for Educational Purposes\"")
pdf.section_title('High School Diploma (Mathematics and Physics)')
pdf.section_content("Lyceum of TNU, Dushanbe | 2016-2018")

# Experience
pdf.chapter_title('Work Experience')
pdf.job_entry('Freelance IT Developer', 'Self-Employed', '2023-Present', 
              "Handled small freelance projects for local businesses, including basic website maintenance, script automation for data processing, and simple Forex-related tool prototypes. Gained hands-on experience in client communication and project delivery, focusing on cost-effective solutions that incorporated business analytics to improve efficiency.")

pdf.job_entry('IT Intern', 'Business Consulting Firm, Dushanbe', '2022-2023 (6 months)', 
              "Assisted in developing and maintaining IT systems for business operations, including database management and software integration to support financial analysis. Applied basic programming skills to automate reporting tasks, incorporating business strategies learned from online courses to optimize processes and reduce manual efforts by 10%.")

# Projects
pdf.chapter_title('Side Projects')
pdf.section_title('Forex Trading Tracker App | 2023')
pdf.section_content("Developed a simple web-based application using basic HTML, CSS, and JavaScript to simulate Forex market tracking, combining IT principles with business analytics for user-friendly trade monitoring.")

pdf.section_title('Basic Website Portfolio | 2022')
pdf.section_content("Created a personal portfolio website showcasing simple IT projects, utilizing free tools like WordPress to demonstrate web development basics.")

pdf.section_title('Simple Data Analysis Script | 2021')
pdf.section_content("Built a Python script for basic data processing and visualization, applying it to sample datasets to practice automation in everyday tasks.")

pdf.section_title('Community IT Volunteer Project | 2020-2021')
pdf.section_content("Led a small team to set up basic computer systems and provide IT training in a local community, applying foundational skills to secure resources and improve digital access.")

# Skills
pdf.chapter_title('Skills')
pdf.section_content("Python, HTML/CSS/JavaScript, WordPress, Data Automation, Business Analytics, Problem Solving")

# Certifications
pdf.chapter_title('Certifications')
pdf.section_content("- Google IT Support Professional Certificate | Coursera, 2022\n- Introduction to Business Analytics | Coursera, 2023\n- Financial Markets (with focus on Forex) | Coursera, 2024")

pdf.output('cv/Jo_Choha_2000.pdf', 'F')
print("CV Generated Successfully")

