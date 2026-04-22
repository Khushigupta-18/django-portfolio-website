# Portfolio Website Specification

## 1. Project Overview

**Project Name:** Django Portfolio Website
**Type:** Personal Portfolio Web Application
**Core Functionality:** A modern, responsive portfolio website with custom admin dashboard for managing projects, skills, and contact messages.
**Target Users:** Potential employers, clients, and collaborators viewing a developer's portfolio.

---

## 2. Tech Stack

- **Backend:** Django 5.2 (latest stable)
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript (minimal)
- **UI Framework:** Custom CSS with modern design principles (no Bootstrap/Tailwind - custom styling)
- **Icons:** Font Awesome 6
- **Fonts:** Google Fonts (Outfit, Inter)

---

## 3. UI/UX Specification

### 3.1 Color Palette

| Role | Color | Hex Code |
|------|-------|----------|
| Primary Background | Deep Charcoal | `#0a0a0a` |
| Secondary Background | Dark Gray | `#141414` |
| Card Background | Soft Black | `#1a1a1a` |
| Primary Accent | Electric Cyan | `#00d4ff` |
| Secondary Accent | Soft Violet | `#7c3aed` |
| Text Primary | Off White | `#f5f5f5` |
| Text Secondary | Muted Gray | `#a0a0a0` |
| Success | Emerald | `#10b981` |
| Error | Rose | `#ef4444` |
| Border | Subtle Gray | `#2a2a2a` |

### 3.2 Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Headings | Outfit | 700 | 3rem - 4rem |
| Subheadings | Outfit | 600 | 1.5rem - 2rem |
| Body | Inter | 400 | 1rem |
| Small Text | Inter | 400 | 0.875rem |

### 3.3 Layout Structure

#### Public Pages
- **Max Width:** 1200px centered
- **Responsive Breakpoints:**
  - Mobile: < 768px
  - Tablet: 768px - 1024px
  - Desktop: > 1024px

#### Admin Dashboard
- **Sidebar Width:** 260px (collapsed: 70px)
- **Main Content:** Fluid with 24px padding

### 3.4 Visual Effects

- **Glassmorphism:** backdrop-filter: blur(10px) on cards
- **Gradients:** Subtle cyan-to-violet gradients on hover
- **Animations:**
  - Fade-in on scroll (IntersectionObserver)
  - Smooth hover transitions (0.3s ease)
  - Button scale on hover (1.02)
  - Progress bar animations on load

---

## 4. Page Structure

### 4.1 Public Homepage

#### Hero Section
- Full viewport height (100vh)
- Animated gradient background with floating shapes
- Large heading: "Hi, I'm [Your Name]"
- Tagline: "Django Developer | Problem Solver | Creative Coder"
- Two CTA buttons: "View Projects" (primary), "Contact Me" (outline)
- Animated scroll indicator at bottom

#### About Section
- Two-column layout (image + text)
- Profile image with gradient border
- Bio text
- Skills displayed as progress bars with percentage

#### Projects Section
- Grid layout (3 columns desktop, 2 tablet, 1 mobile)
- Project cards with:
  - Image thumbnail
  - Title
  - Description (2 lines max)
  - Tech stack tags
  - GitHub & Live Demo links

#### Services Section
- Grid layout (3 columns)
- Service cards with icon, title, description
- Hover: lift effect + glow

#### Contact Section
- Two-column: Form + Info
- Form fields: Name, Email, Subject, Message
- Submit button with loading state
- Success/error messages

#### Footer
- Social links (GitHub, LinkedIn, Twitter, Email)
- Copyright text
- Back to top button

### 4.2 Custom Admin Dashboard

#### Login Page
- Centered card with glassmorphism effect
- Username/Password fields
- Remember me checkbox
- Error messages

#### Dashboard Home
- Sidebar navigation (collapsible)
- Stats cards:
  - Total Projects (with icon)
  - Total Messages (with icon)
  - Total Skills (with icon)
- Recent messages preview

#### Projects Management
- Table view with all projects
- Columns: Image, Title, Tech Stack, Actions
- Add/Edit/Delete buttons
- Modal or inline editing

#### Skills Management
- Card grid view
- Add/Edit/Delete functionality
- Progress percentage slider

#### Messages Management
- List view of all contact messages
- Read/Delete actions
- Timestamp display

---

## 5. Data Models

### 5.1 Project Model
```python
class Project(models.Model):
    title = CharField(max_length=200)
    description = TextField()
    image = ImageField(upload_to='projects/')
    tech_stack = CharField(max_length=500)  # Comma-separated
    github_link = URLField(blank=True)
    live_link = URLField(blank=True)
    created_at = DateTimeField(auto_now_add=True)
    order = PositiveIntegerField(default=0)
```

### 5.2 Skill Model
```python
class Skill(models.Model):
    name = CharField(max_length=100)
    percentage = PositiveIntegerField(default=0)  # 0-100
    category = CharField(max_length=50)  # frontend, backend, tools
    order = PositiveIntegerField(default=0)
```

### 5.3 ContactMessage Model
```python
class ContactMessage(models.Model):
    name = CharField(max_length=200)
    email = EmailField()
    subject = CharField(max_length=300)
    message = TextField()
    created_at = DateTimeField(auto_now_add=True)
    is_read = BooleanField(default=False)
```

### 5.4 Service Model
```python
class Service(models.Model):
    title = CharField(max_length=200)
    description = TextField()
    icon = CharField(max_length=50)  # Font Awesome icon class
    order = PositiveIntegerField(default=0)
```

---

## 6. URL Structure

### Public URLs
- `/` - Homepage
- `/contact/` - Contact form submission (POST)

### Admin URLs
- `/admin/` - Custom admin login
- `/admin/dashboard/` - Admin dashboard home
- `/admin/projects/` - Manage projects
- `/admin/projects/add/` - Add project
- `/admin/projects/edit/<id>/` - Edit project
- `/admin/projects/delete/<id>/` - Delete project
- `/admin/skills/` - Manage skills
- `/admin/messages/` - View messages
- `/admin/messages/delete/<id>/` - Delete message
- `/admin/logout/` - Logout

---

## 7. Security Requirements

- CSRF protection on all forms
- Login required for admin pages
- Password hashing (Django's PBKDF2)
- X-Frame-Options middleware enabled
- Secure password validation
- Input sanitization

---

## 8. Acceptance Criteria

### Visual Checkpoints
- [ ] Homepage loads with animated hero section
- [ ] All sections visible and properly styled
- [ ] Responsive on mobile, tablet, desktop
- [ ] Admin login page has glassmorphism effect
- [ ] Dashboard shows stats and navigation
- [ ] All CRUD operations work correctly

### Functional Checkpoints
- [ ] Contact form submits and saves to database
- [ ] Admin can add/edit/delete projects
- [ ] Admin can add/edit/delete skills
- [ ] Admin can view/delete messages
- [ ] Static files load correctly
- [ ] Images upload and display properly

---

## 9. Project Structure

```
portfoliowebsite/
├── manage.py
├── db.sqlite3
├── portfoliowebsite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
├── portfolio/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── contact/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── dashboard/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── decorators.py
├── templates/
│   ├── base.html
│   ├── core/
│   │   ├── home.html
│   │   └── includes/
│   │       ├── hero.html
│   │       ├── about.html
│   │       ├── projects.html
│   │       ├── services.html
│   │       ├── contact.html
│   │       └── footer.html
│   └── dashboard/
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       ├── projects.html
│       ├── skills.html
│       └── messages.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

---

## 10. Instructions to Run

1. **Install dependencies:**
   ```bash
   pip install django pillow
   ```

2. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Run development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access URLs:**
   - Homepage: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
