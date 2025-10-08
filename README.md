# Lesson Plan Management System

A simple web-based lesson plan management system that allows teachers to view and download lesson plans based on class and chapter selection.

## 🌐 **GitHub Repository**
**Repository URL**: https://github.com/brajeshmishra26/lessonplan.git

## 🚀 **Quick Start**
```bash
git clone https://github.com/brajeshmishra26/lessonplan.git
cd lessonplan
pip install -r requirements.txt
python app.py
```

## Features

- **Class & Chapter Selection**: Easy dropdown selection interface
- **View Lesson Plans**: Display lesson plans in a formatted HTML view
- **Download DOCX**: Generate and download professional Word documents
- **Database Storage**: SQLite database for storing lesson plan data
- **Responsive Design**: Mobile-friendly interface
- **Print Functionality**: Print lesson plans directly from browser

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Document Generation**: python-docx

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Navigate to the project directory:**
   ```cmd
   cd "d:\lesson plan\lesson_plan_website"
   ```

2. **Install required packages:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```cmd
   python app.py
   ```

4. **Access the website:**
   Open your browser and go to: `http://localhost:5000`

## Usage

### Main Interface
1. Select a class from the dropdown (1st to 8th)
2. Choose a chapter from the available options
3. Click "View Lesson Plan" to see it in browser
4. Click "Download DOCX" to get a Word document

### Available Features
- **View**: Opens lesson plan in new tab with formatted display
- **Download**: Generates and downloads DOCX file
- **Print**: Print lesson plan directly from view page
- **Responsive**: Works on desktop, tablet, and mobile devices

## Database Structure

The SQLite database contains a `lesson_plans` table with the following fields:
- `id`: Primary key
- `class_num`: Class number (1-8)
- `subject`: Subject name
- `chapter_num`: Chapter number
- `chapter_title`: Chapter title
- `month`, `year`: Time period
- `unit`: Unit information
- `learning_outcomes`: Learning objectives
- `teaching_points`: Teaching points
- `teaching_aids`: Teaching materials
- `teaching_methodology`: Teaching methods
- `activity_planned`: Planned activities
- `learning_skill_practice`: Skill practices
- `life_skill_learnt`: Life skills
- `assignment_planned`: Assignments
- `assessment_planned`: Assessment methods

## Sample Data

The system comes pre-loaded with:
- **Class 5th**: Hindi (रिमझिम) - Chapter 8: "वे दिन भी क्या दिन थे (विज्ञान कथा)"

## Adding New Lesson Plans

You can add new lesson plans by:
1. Modifying the `init_db()` function in `app.py`
2. Adding INSERT statements with your lesson plan data
3. Restarting the application

## File Structure

```
lesson_plan_website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── lesson_plans.db       # SQLite database (created automatically)
├── templates/            # HTML templates
│   ├── index.html        # Main selection page
│   └── lesson_plan.html  # Lesson plan display page
├── static/               # Static files
│   └── css/
│       └── style.css     # Custom CSS styles
└── downloads/            # Downloaded files directory
```

## Customization

### Adding More Lesson Plans
Edit the `init_db()` function in `app.py` to add more lesson plans to the database.

### Styling
Modify `static/css/style.css` to change the appearance of the website.

### Templates
Edit HTML templates in the `templates/` directory to modify the layout.

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Database not created**: Ensure you have write permissions in the directory.

3. **Import errors**: Make sure all requirements are installed:
   ```cmd
   pip install -r requirements.txt
   ```

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License

This project is free to use for educational purposes.

## Support

For issues or questions, please check the code comments or create an issue in the project repository.