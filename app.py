from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import sqlite3
import os
from datetime import datetime
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('lesson_plans.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lesson_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_num INTEGER,
            subject TEXT,
            chapter_num INTEGER,
            chapter_title TEXT,
            month TEXT,
            year INTEGER,
            unit TEXT,
            learning_outcomes TEXT,
            teaching_points TEXT,
            teaching_aids TEXT,
            teaching_methodology TEXT,
            activity_planned TEXT,
            learning_skill_practice TEXT,
            life_skill_learnt TEXT,
            assignment_planned TEXT,
            assessment_planned TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert sample data (Class 5 Rimjhim Chapter 8)
    cursor.execute('''
        INSERT OR REPLACE INTO lesson_plans 
        (class_num, subject, chapter_num, chapter_title, month, year, unit,
         learning_outcomes, teaching_points, teaching_aids, teaching_methodology,
         activity_planned, learning_skill_practice, life_skill_learnt,
         assignment_planned, assessment_planned)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        5, 'Hindi (रिमझिम)', 8, 'वे दिन भी क्या दिन थे (विज्ञान कथा)', 'October', 2025, 'पाठ 8',
        '''1. छात्र विज्ञान कथा की विधा को समझ सकेंगे और उसकी विशेषताओं को पहचान सकेंगे
2. भविष्य की तकनीक और आविष्कारों के बारे में कल्पना कर सकेंगे
3. पाठ के माध्यम से भाषा की सुंदरता और शब्द भंडार में वृद्धि कर सकेंगे
4. कहानी के पात्रों के भावों और विचारों को समझ सकेंगे
5. वैज्ञानिक दृष्टिकोण विकसित कर तर्कसंगत चिंतन कर सकेंगे''',
        '''1. विज्ञान कथा का परिचय और इसकी विशेषताएं
2. कहानी के मुख्य पात्रों का चरित्र-चित्रण
3. भविष्य की तकनीक और वैज्ञानिक आविष्कारों की चर्चा
4. पाठ में आए नए शब्दों का अर्थ और प्रयोग
5. कहानी की मुख्य घटनाओं का क्रमवार विवरण
6. पात्रों के संवादों का भावपूर्ण वाचन
7. वैज्ञानिक सोच और कल्पनाशीलता का विकास
8. भाषा की शुद्धता और उच्चारण पर ध्यान
9. कहानी के माध्यम से मिलने वाले संदेश की व्याख्या
10. आधुनिक तकनीक और भविष्य की संभावनाओं पर चर्चा''',
        '''1. रिमझिम पाठ्य पुस्तक, श्यामपट्ट और चार्ट पेपर
2. विज्ञान और तकनीक से संबंधित चित्र और मॉडल
3. प्रोजेक्टर/स्मार्ट बोर्ड (यदि उपलब्ध हो)''',
        '''1. व्याख्यान विधि और प्रश्नोत्तर विधि का प्रयोग
2. समूहिक चर्चा और सहयोगी शिक्षण पद्धति''',
        'छात्रों को समूहों में बांटकर भविष्य के आविष्कारों पर चर्चा कराना और उन्हें अपनी कल्पना के आधार पर एक छोटी विज्ञान कथा लिखने के लिए प्रेरित करना',
        '''1. पठन कौशल - पाठ का शुद्ध उच्चारण और भावपूर्ण वाचन
2. लेखन कौशल - नए शब्दों का शुद्ध लेखन और वाक्य प्रयोग''',
        'वैज्ञानिक दृष्टिकोण और तर्कसंगत चिंतन का विकास, भविष्य की चुनौतियों के लिए तैयार होना',
        'पाठ के कठिन शब्दों के अर्थ लिखकर वाक्य प्रयोग करना तथा अपनी कल्पना के आधार पर 10 पंक्तियों में एक छोटी विज्ञान कथा लिखना',
        '''1. मौखिक प्रश्नों के द्वारा पाठ की समझ का आकलन
2. शब्द भंडार और भाषा प्रयोग की जांच
3. रचनात्मक लेखन और कल्पनाशीलता का मूल्यांकन
4. सामूहिक गतिविधि में भागीदारी और सहयोग का आकलन
5. गृहकार्य की जांच और व्यक्तिगत प्रगति का मूल्यांकन'''
    ))
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_print')
def test_print():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Print Test</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            @media print { .no-print { display: none !important; } }
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="no-print text-center mb-4">
                <button id="printBtn1" class="btn btn-success me-2">
                    <i class="fas fa-print"></i> Test Print
                </button>
                <button onclick="window.print()" class="btn btn-primary me-2">
                    <i class="fas fa-print"></i> Direct Print
                </button>
            </div>
            <h2>Print Test Content</h2>
            <p>This is test content for print functionality.</p>
        </div>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                document.getElementById('printBtn1').addEventListener('click', function() {
                    console.log('Print button clicked');
                    window.print();
                });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/get_chapters/<int:class_num>')
def get_chapters(class_num):
    conn = sqlite3.connect('lesson_plans.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT DISTINCT chapter_num, chapter_title 
        FROM lesson_plans 
        WHERE class_num = ? 
        ORDER BY chapter_num
    ''', (class_num,))
    
    chapters = cursor.fetchall()
    conn.close()
    
    return jsonify([{'chapter_num': ch[0], 'chapter_title': ch[1]} for ch in chapters])

@app.route('/lesson_plan/<int:class_num>/<int:chapter_num>')
def view_lesson_plan(class_num, chapter_num):
    conn = sqlite3.connect('lesson_plans.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM lesson_plans 
        WHERE class_num = ? AND chapter_num = ?
    ''', (class_num, chapter_num))
    
    lesson_plan = cursor.fetchone()
    conn.close()
    
    if not lesson_plan:
        return "Lesson plan not found!", 404
    
    # Convert tuple to dictionary for easy template access
    columns = ['id', 'class_num', 'subject', 'chapter_num', 'chapter_title', 
               'month', 'year', 'unit', 'learning_outcomes', 'teaching_points',
               'teaching_aids', 'teaching_methodology', 'activity_planned',
               'learning_skill_practice', 'life_skill_learnt', 'assignment_planned',
               'assessment_planned', 'created_at']
    
    lesson_data = dict(zip(columns, lesson_plan))
    
    return render_template('lesson_plan.html', lesson=lesson_data)

@app.route('/print/<int:class_num>/<int:chapter_num>')
def print_lesson_plan(class_num, chapter_num):
    conn = sqlite3.connect('lesson_plans.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM lesson_plans 
        WHERE class_num = ? AND chapter_num = ?
    ''', (class_num, chapter_num))
    
    lesson_plan = cursor.fetchone()
    conn.close()
    
    if not lesson_plan:
        return "Lesson plan not found!", 404
    
    # Convert tuple to dictionary for easy template access
    columns = ['id', 'class_num', 'subject', 'chapter_num', 'chapter_title', 
               'month', 'year', 'unit', 'learning_outcomes', 'teaching_points',
               'teaching_aids', 'teaching_methodology', 'activity_planned',
               'learning_skill_practice', 'life_skill_learnt', 'assignment_planned',
               'assessment_planned', 'created_at']
    
    lesson_data = dict(zip(columns, lesson_plan))
    
    # Return a print-optimized version
    return render_template('print_lesson_plan.html', lesson=lesson_data)

@app.route('/download/<int:class_num>/<int:chapter_num>')
def download_lesson_plan(class_num, chapter_num):
    conn = sqlite3.connect('lesson_plans.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM lesson_plans 
        WHERE class_num = ? AND chapter_num = ?
    ''', (class_num, chapter_num))
    
    lesson_plan = cursor.fetchone()
    conn.close()
    
    if not lesson_plan:
        return "Lesson plan not found!", 404
    
    # Create Word document
    doc = Document()
    
    # Title
    title = doc.add_heading('LESSON PLAN', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Basic Information
    basic_info_para = doc.add_paragraph()
    basic_info_para.add_run(f'Class: {lesson_plan[1]}    ')
    basic_info_para.add_run(f'Month: {lesson_plan[5]}    ')
    basic_info_para.add_run(f'Year: {lesson_plan[6]}\n')
    basic_info_para.add_run(f'Subject: {lesson_plan[2]}    ')
    basic_info_para.add_run(f'Unit: {lesson_plan[7]}\n')
    basic_info_para.add_run(f'Topic: {lesson_plan[4]}')
    
    doc.add_paragraph()
    
    # Add all sections
    sections = [
        ('Learning Outcomes (शिक्षण उद्देश्य)', lesson_plan[8]),
        ('Teaching Points (शिक्षण बिंदु)', lesson_plan[9]),
        ('Teaching Aids (शिक्षण सहायक सामग्री)', lesson_plan[10]),
        ('Teaching Methodology (शिक्षण विधि)', lesson_plan[11]),
        ('Activity Planned (नियोजित गतिविधि)', lesson_plan[12]),
        ('Learning Skill Practice (अधिगम कौशल अभ्यास)', lesson_plan[13]),
        ('Life Skill Learnt (जीवन कौशल)', lesson_plan[14]),
        ('Assignment Planned (गृहकार्य)', lesson_plan[15]),
        ('Assessment Planned (मूल्यांकन योजना)', lesson_plan[16])
    ]
    
    for section_title, content in sections:
        doc.add_heading(section_title, level=2)
        
        # Split content into lines and add as bullet points
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                p = doc.add_paragraph()
                p.style = 'List Bullet'
                p.add_run(line.strip())
    
    # Footer
    doc.add_paragraph()
    footer_para = doc.add_paragraph()
    footer_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer_para.add_run('तैयारकर्ता: [शिक्षक का नाम]\n')
    footer_para.add_run(f'दिनांक: {datetime.now().strftime("%d %B, %Y")}')
    
    # Save to memory
    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    
    filename = f'lesson_plan_class{class_num}_chapter{chapter_num}.docx'
    
    return send_file(
        doc_io,
        as_attachment=True,
        download_name=filename,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)