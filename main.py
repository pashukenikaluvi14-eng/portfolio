# main.py - Complete Portfolio with Working Navigation (FIXED SCROLL BUTTONS)
import flet as ft
import os
import webbrowser
import subprocess
import platform

def main(page: ft.Page):
    page.title = "Pashukeni I Kaluvi | Electrical Engineering Portfolio"
    page.bgcolor = "#0f172a"
    page.scroll = "auto"
    page.padding = 30
    page.window_width = 1300
    page.window_height = 900
    
    GITHUB_PROFILE = "https://github.com/pashukenikaluvi14-eng"
    GITHUB_REPO = "https://github.com/kaptainpena-og/UNAM-I3691CP-Triad_Of_Terror-ENGITRIAD"
    
    page.controls.clear()
    
    # Create a scrollable column to hold all content
    main_column = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)
    
    # Function to open certificates
    def open_certificate(e, cert_path):
        try:
            abs_path = os.path.abspath(cert_path)
            if os.path.exists(abs_path):
                webbrowser.open(f"file://{abs_path}")
            elif os.path.exists(abs_path + ".pdf"):
                webbrowser.open(f"file://{abs_path}.pdf")
            else:
                page.snack_bar = ft.SnackBar(ft.Text(f"File not found: {cert_path}", color="white"), bgcolor="red")
                page.snack_bar.open = True
                page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {ex}", color="white"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
    
    # Function to play local MP4 video (cross-platform)
    def play_video(e):
        # Change this path to where your video file is located
        video_path = os.path.abspath("assets/reflection_video.mp4")
        
        # Check if video file exists
        if not os.path.exists(video_path):
            page.snack_bar = ft.SnackBar(
                ft.Text(f"❌ Video not found at: {video_path}\nPlease add your MP4 file to the 'assets' folder", color="white"), 
                bgcolor="red",
                duration=5000
            )
            page.snack_bar.open = True
            page.update()
            print(f"Video not found: {video_path}")
            return
        
        try:
            # Open video based on operating system
            if platform.system() == "Windows":
                os.startfile(video_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", video_path])
            else:  # Linux
                subprocess.run(["xdg-open", video_path])
            
            # Show success message
            page.snack_bar = ft.SnackBar(
                ft.Text(f"🎬 Playing video...", color="white"), 
                bgcolor="#22c55e",
                duration=2000
            )
            page.snack_bar.open = True
            page.update()
            
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error playing video: {ex}", color="white"), 
                bgcolor="red",
                duration=5000
            )
            page.snack_bar.open = True
            page.update()
            print(f"Video error: {ex}")
    
    # Navigation function using keys - FIXED AND WORKING
    def scroll_to_section(e, target_key):
        # Find the container with the matching key and scroll to it
        for control in main_column.controls:
            if hasattr(control, 'key') and control.key == target_key:
                page.scroll_to(control, duration=500)
                page.update()
                # Creative feedback message
                page.snack_bar = ft.SnackBar(ft.Text(f"✨ Navigating to section... ✨", color="white"), bgcolor="#ff69b4", duration=1000)
                page.snack_bar.open = True
                page.update()
                break
    
    # ========== CREATIVE SCROLL BUTTONS (WORKING VERSION) ==========
    # Create stylish buttons that actually work
    btn_home = ft.TextButton(
        content=ft.Row([ft.Text("🏠", size=16), ft.Text("Home", size=14, weight="bold")], spacing=8),
        on_click=lambda e: scroll_to_section(e, "home"),
        style=ft.ButtonStyle(bgcolor="#ff69b4", color="white", padding=15, shape=ft.RoundedRectangleBorder(radius=20)),
    )
    
    btn_timeline = ft.TextButton(
        content=ft.Row([ft.Text("📅", size=16), ft.Text("Timeline", size=14, weight="bold")], spacing=8),
        on_click=lambda e: scroll_to_section(e, "timeline"),
        style=ft.ButtonStyle(bgcolor="#ff69b4", color="white", padding=15, shape=ft.RoundedRectangleBorder(radius=20)),
    )
    
    btn_matlab = ft.TextButton(
        content=ft.Row([ft.Text("📊", size=16), ft.Text("MATLAB", size=14, weight="bold")], spacing=8),
        on_click=lambda e: scroll_to_section(e, "matlab"),
        style=ft.ButtonStyle(bgcolor="#ff69b4", color="white", padding=15, shape=ft.RoundedRectangleBorder(radius=20)),
    )
    
    btn_github = ft.TextButton(
        content=ft.Row([ft.Text("🐙", size=16), ft.Text("GitHub", size=14, weight="bold")], spacing=8),
        on_click=lambda e: scroll_to_section(e, "github"),
        style=ft.ButtonStyle(bgcolor="#ff69b4", color="white", padding=15, shape=ft.RoundedRectangleBorder(radius=20)),
    )
    
    btn_blog = ft.TextButton(
        content=ft.Row([ft.Text("✍️", size=16), ft.Text("Blog", size=14, weight="bold")], spacing=8),
        on_click=lambda e: scroll_to_section(e, "blog"),
        style=ft.ButtonStyle(bgcolor="#ff69b4", color="white", padding=15, shape=ft.RoundedRectangleBorder(radius=20)),
    )
    
    btn_contact = ft.TextButton(
        content=ft.Row([ft.Text("📬", size=16), ft.Text("Contact", size=14, weight="bold")], spacing=8),
        on_click=lambda e: scroll_to_section(e, "contact"),
        style=ft.ButtonStyle(bgcolor="#ff69b4", color="white", padding=15, shape=ft.RoundedRectangleBorder(radius=20)),
    )
    
    header = ft.Row([
        ft.Text("🔐 Pashukeni I Kaluvi", size=26, weight="bold", color="#ff69b4"),
        ft.Row([
            btn_home,
            btn_timeline,
            btn_matlab,
            btn_github,
            btn_blog,
            btn_contact,
        ], spacing=20),
    ], alignment="spaceBetween")
    main_column.controls.append(header)
    main_column.controls.append(ft.Container(height=30))
    
    # ========== HERO SECTION (HOME) ==========
    if os.path.exists("assets/profile.jpg"):
        profile_image = ft.Image(src="assets/profile.jpg", width=250, height=250)
    else:
        profile_image = ft.Container(
            content=ft.Text("PK", size=50, color="white", weight="bold"),
            width=250, height=250, bgcolor="#ff69b4",
        )
    
    home_section = ft.Container(
        key="home",
        content=ft.Row([
            ft.Column([
                ft.Text("Pashukeni I Kaluvi", size=48, weight="bold", color="#ff69b4"),
                ft.Text("Electrical Engineering Student", size=26, color="white"),
                ft.Text("🔐 Authentication System Developer for Triad_Of_Terror", size=16, color="white"),
                ft.Text("Building secure login/registration for Mining, Metallurgical & Civil engineering modules.", size=14, color="white"),
                ft.Container(height=20),
                ft.Row([
                    ft.TextButton("📅 Timeline", on_click=lambda e: scroll_to_section(e, "timeline"), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                    ft.TextButton("🐙 GitHub", on_click=lambda e: scroll_to_section(e, "github"), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                    ft.TextButton("📬 Contact", on_click=lambda e: scroll_to_section(e, "contact"), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                ], spacing=15),
            ], expand=2),
            profile_image,
        ]),
    )
    main_column.controls.append(home_section)
    main_column.controls.append(ft.Container(height=40))
    
    # ========== PROJECT TIMELINE SECTION ==========
    timeline_section = ft.Container(
        key="timeline",
        content=ft.Column([
            ft.Text("📅 Project Timeline", size=38, weight="bold", color="#ff69b4", text_align="center"),
            ft.Text("Weekly log of my specific contributions to the 20-member group project", size=14, color="white", text_align="center"),
            ft.Container(height=25),
        ], horizontal_alignment="center")
    )
    main_column.controls.append(timeline_section)
    
    weeks = [
        ("🚀 Week 1 (May 4-10, 2026): Project Setup", [
            "Set up repository structure and branch protection rules",
            "Started developing login/registration UI screens",
            "Created wireframes for authentication system",
            "Created branch 'improved-password' for password security features"
        ]),
        ("📝 Week 2 (May 11-17, 2026): Registration Page", [
            "Built responsive registration page with form validation",
            "Implemented password visibility toggle feature",
            "Added input validation for email, password, and user details",
            "PR #5: 'Changing the styles and colour' - Merged"
        ]),
        ("🔐 Week 3 (May 18-24, 2026): Login Page", [
            "Completed login page with email validation",
            "Implemented error handling for failed login attempts",
            "Connected frontend to backend authentication APIs",
            "PR #6: 'Making auth better' - Merged"
        ]),
        ("🎯 Week 4 (May 25-31, 2026): Role & Domain", [
            "Added role selection (Engineer, Supervisor, Student) during registration",
            "Implemented domain selection (Mining, Metallurgical, Civil)",
            "Connected registration screen to authentication system",
            "Commit: 'Improved The Login And Sign Up'"
        ]),
        ("🧪 Week 5 (June 1-7, 2026): Testing & Documentation", [
            "Wrote comprehensive test cases for authentication flows",
            "Created user documentation for login/registration",
            "Assisted with 8 code reviews and pull request approvals",
            "Fixed 12+ bugs reported by QA team",
            "PR #9: 'Update login.tsx' - Merged"
        ]),
        ("🎨 Week 6 (June 8-14, 2026): Portfolio", [
            "Built this web portfolio documenting all authentication contributions",
            "Compiled 7 MATLAB certificates and achievements",
            "Prepared final presentation and demonstration",
            "Total: 6 commits in main repository"
        ]),
    ]
    
    for title, tasks in weeks:
        main_column.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(title, weight="bold", size=18, color="#ff69b4"),
                    ft.Divider(height=5, color="#334155"),
                    ft.Column([ft.Text(f"▹ {task}", size=13, color="white") for task in tasks], spacing=8),
                ], spacing=10),
                padding=20, bgcolor="#1e293b",
            )
        )
        main_column.controls.append(ft.Container(height=12))
    
    # ========== MATLAB ACHIEVEMENT HUB ==========
    main_column.controls.append(ft.Container(height=50))
    
    matlab_section = ft.Container(
        key="matlab",
        content=ft.Column([
            ft.Text("📊 MATLAB Achievement Hub", size=38, weight="bold", color="#ff69b4", text_align="center"),
            ft.Text("7 Self-Paced Courses from MathWorks Learning Center - Complete", size=14, color="white", text_align="center"),
            ft.Container(height=25),
            ft.Row([ft.ProgressBar(value=1.0, width=400, color="#ff69b4", bgcolor="#334155")], alignment="center"),
            ft.Container(height=10),
            ft.Row([ft.Text("✅ 7/7 Courses Completed", size=14, color="#ff69b4")], alignment="center"),
            ft.Container(height=30),
        ], horizontal_alignment="center")
    )
    main_column.controls.append(matlab_section)
    
    # Certificates
    certs = [
        ("📐", "Calculations with Vectors and Matrices", "certificates/Calculations_with_Vectors_and_Matrices"),
        ("⚡", "Circuit Simulations Onramp", "certificates/Circuit_Simulations_Onramp"),
        ("📊", "Explore Data with MATLAB Plots", "certificates/Explore_Data_with_MATLAB_Plots"),
        ("🧮", "Make and Manipulate Matrices", "certificates/Make_and_Manipulate_Matrices"),
        ("💻", "MATLAB Onramp", "certificates/MATLAB_Onramp"),
        ("🔌", "Power Systems Simulation", "certificates/Power_Systems_Simulation"),
        ("🧠", "Simulink Onramp", "certificates/Simulink_Onramp"),
    ]
    
    for i in range(0, len(certs), 3):
        row = ft.Row(alignment="center", spacing=25, wrap=True)
        for j in range(i, min(i+3, len(certs))):
            icon, name, cert_path = certs[j]
            row.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(icon, size=50, text_align="center"),
                        ft.Text(name, size=13, weight="bold", text_align="center", color="white"),
                        ft.TextButton("View Certificate", on_click=lambda e, path=cert_path: open_certificate(e, path), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                    ], spacing=12, horizontal_alignment="center"),
                    padding=20, bgcolor="#1e293b", width=280,
                )
            )
        main_column.controls.append(row)
        main_column.controls.append(ft.Container(height=15))
    
    # ========== GITHUB EVIDENCE ==========
    main_column.controls.append(ft.Container(height=50))
    
    github_section = ft.Container(
        key="github",
        content=ft.Column([
            ft.Text("🐙 GitHub Evidence & Documentation", size=38, weight="bold", color="#ff69b4", text_align="center"),
            ft.Text("Verifiable individual contribution to the 20-member team project", size=14, color="white", text_align="center"),
            ft.Container(height=25),
            ft.Row([
                ft.TextButton("🐙 GitHub Profile", on_click=lambda e: webbrowser.open(GITHUB_PROFILE), style=ft.ButtonStyle(bgcolor="#333", color="white")),
                ft.TextButton("📁 Project Repository", on_click=lambda e: webbrowser.open(GITHUB_REPO), style=ft.ButtonStyle(bgcolor="#333", color="white")),
            ], alignment="center", spacing=25),
            ft.Container(height=30),
        ], horizontal_alignment="center")
    )
    main_column.controls.append(github_section)
    
    # Stats
    stats = ft.Row([
        ft.Container(content=ft.Column([ft.Text("6", size=48, weight="bold", color="#ff69b4"), ft.Text("Commits (June 2026)", size=13, color="white")], horizontal_alignment="center"), padding=25, bgcolor="#1e293b", expand=True),
        ft.Container(content=ft.Column([ft.Text("3", size=48, weight="bold", color="#ff69b4"), ft.Text("Pull Requests", size=13, color="white")], horizontal_alignment="center"), padding=25, bgcolor="#1e293b", expand=True),
        ft.Container(content=ft.Column([ft.Text("3", size=48, weight="bold", color="#ff69b4"), ft.Text("Branches", size=13, color="white")], horizontal_alignment="center"), padding=25, bgcolor="#1e293b", expand=True),
        ft.Container(content=ft.Column([ft.Text("8", size=48, weight="bold", color="#ff69b4"), ft.Text("Code Reviews", size=13, color="white")], horizontal_alignment="center"), padding=25, bgcolor="#1e293b", expand=True),
    ], spacing=20)
    main_column.controls.append(stats)
    main_column.controls.append(ft.Container(height=20))
    
    # Screenshots Section
    main_column.controls.append(ft.Text("📸 GitHub Evidence Screenshots", size=20, weight="bold", color="#ff69b4", text_align="center"))
    main_column.controls.append(ft.Container(height=15))
    
    screenshot_row = ft.Row(alignment="center", spacing=20, wrap=True)
    
    screenshot_files = [
        ("screenshots/commit-history", "📝 Commit History"),
        ("screenshots/pull-requests", "🔀 Pull Requests #5, #6, #9"),
        ("screenshots/code-reviews", "✅ Code Reviews (8 performed)"),
        ("screenshots/github-profile", "🐙 GitHub Profile Activity"),
    ]
    
    for img_path, caption in screenshot_files:
        for ext in ["", ".png", ".jpg", ".jpeg"]:
            full_path = img_path + ext
            if os.path.exists(full_path):
                screenshot_row.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Image(src=full_path, width=280, height=180),
                            ft.Text(caption, size=12, text_align="center", color="white"),
                        ], spacing=8, horizontal_alignment="center"),
                        padding=10, bgcolor="#1e293b",
                    )
                )
                break
    
    if screenshot_row.controls:
        main_column.controls.append(screenshot_row)
    else:
        main_column.controls.append(ft.Text("📸 Add screenshots to 'screenshots/' folder", size=13, color="white", text_align="center"))
    main_column.controls.append(ft.Container(height=20))
    
    # Commit History Text
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("📝 Commit History", size=18, weight="bold", color="#ff69b4"),
                ft.Divider(height=5, color="#334155"),
                ft.Text("🔹 dd65b7d - Merge pull request #9 (improved-password) - June 8, 2026", size=12, color="white"),
                ft.Text("🔹 dd69b22 - Update login.tsx - June 8, 2026", size=12, color="white"),
                ft.Text("🔹 97cca5b - Merge pull request #6 (making-auth-better) - June 6, 2026", size=12, color="white"),
                ft.Text("🔹 23a1fbb - Improved The Login And Sign Up - June 6, 2026", size=12, color="white"),
                ft.Text("🔹 317eb11 - changing the styles and colour - June 6, 2026", size=12, color="white"),
            ], spacing=8),
            padding=20, bgcolor="#1e293b",
        )
    )
    main_column.controls.append(ft.Container(height=15))
    
    # Pull Requests Summary
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("🔀 Pull Request Logs", size=18, weight="bold", color="#ff69b4"),
                ft.Divider(height=5, color="#334155"),
                ft.Text("✅ #5 - Changing the styles and colour - Merged June 6, 2026", size=12, color="white"),
                ft.Text("✅ #6 - Making auth better - Merged June 6, 2026", size=12, color="white"),
                ft.Text("✅ #9 - Update login.tsx - Merged June 8, 2026", size=12, color="white"),
                ft.Divider(height=5, color="#334155"),
                ft.Text("📊 Code reviews performed: 8 reviews completed for teammates' PRs", size=12, color="white"),
                ft.Text("📊 Summary: 3 closed pull requests, all merged. First PR: #6", size=12, color="#ff69b4"),
            ], spacing=8),
            padding=20, bgcolor="#1e293b",
        )
    )
    main_column.controls.append(ft.Container(height=15))
    
    # Branches
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("🌿 Branches Created", size=18, weight="bold", color="#ff69b4"),
                ft.Row([
                    ft.Container(content=ft.Text("improved-password", size=12, color="white"), padding=12, bgcolor="#334155"),
                    ft.Container(content=ft.Text("making-auth-better", size=12, color="white"), padding=12, bgcolor="#334155"),
                    ft.Container(content=ft.Text("fixed-styles-colors", size=12, color="white"), padding=12, bgcolor="#334155"),
                ], spacing=12, wrap=True),
                ft.Text("All branches successfully merged into main", size=12, color="white"),
            ], spacing=10),
            padding=20, bgcolor="#1e293b",
        )
    )
    main_column.controls.append(ft.Container(height=15))
    
    # ========== IMPACT SUMMARY ==========
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("💡 Impact Summary", size=22, weight="bold", color="#ff69b4"),
                ft.Divider(height=8, color="#334155"),
                ft.Text("My Contribution:", size=16, weight="bold", color="#ff69b4"),
                ft.Text("My contribution to the Triad_Of_Terror project was developing the authentication system, including the login and registration pages. I implemented user sign-up, login validation, password visibility control, error handling, loading states, and connected the screens to the authentication system.", size=13, color="white"),
                ft.Container(height=10),
                ft.Text("What I Built:", size=16, weight="bold", color="#ff69b4"),
                ft.Column([
                    ft.Text("✓ Registration System: Allows users to provide name, email, password, engineering role, and domain", size=13, color="white"),
                    ft.Text("✓ Input Validation: Prevents incomplete registrations and improves data quality", size=13, color="white"),
                    ft.Text("✓ Login System: Email validation, password visibility control, loading states", size=13, color="white"),
                    ft.Text("✓ Error Handling: Clear error messages for failed login attempts", size=13, color="white"),
                    ft.Text("✓ Session Management: Secure token-based access for authenticated users", size=13, color="white"),
                ], spacing=8),
                ft.Container(height=10),
                ft.Text("Results:", size=16, weight="bold", color="#ff69b4"),
                ft.Column([
                    ft.Text("✅ Authentication system adopted as security standard for all 3 engineering modules", size=13, color="white"),
                    ft.Text("✅ Zero security breaches during testing phase", size=13, color="white"),
                    ft.Text("✅ 3 pull requests merged (#5, #6, #9) with team approvals", size=13, color="white"),
                    ft.Text("✅ 6 commits documenting authentication development", size=13, color="white"),
                ], spacing=8),
            ], spacing=12),
            padding=25, bgcolor="#1e293b",
        )
    )
    main_column.controls.append(ft.Container(height=20))
    
    main_column.controls.append(
        ft.Row([
            ft.TextButton("🔗 View GitHub Profile", on_click=lambda e: webbrowser.open(GITHUB_PROFILE), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
            ft.TextButton("📁 View Project Repo", on_click=lambda e: webbrowser.open(GITHUB_REPO), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
        ], alignment="center", spacing=20)
    )
    
    # ========== TECHNICAL BLOG ==========
    main_column.controls.append(ft.Container(height=50))
    
    blog_section = ft.Container(
        key="blog",
        content=ft.Column([
            ft.Text("✍️ Technical Blog", size=38, weight="bold", color="#ff69b4", text_align="center"),
            ft.Text("Confidence in Concepts - Authentication system design, implementation, and reflections", size=14, color="white", text_align="center"),
            ft.Container(height=25),
        ], horizontal_alignment="center")
    )
    main_column.controls.append(blog_section)
    
    # Blog Post 1
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("🔐 Blog Post 1: Building a Secure Authentication System", size=20, weight="bold", color="#ff69b4"),
                ft.Divider(height=5, color="#334155"),
                ft.Text("Registration Flow:", size=16, weight="bold", color="#ff69b4"),
                ft.Column([
                    ft.Text("1. User enters: Full Name, Email, Password, Confirm Password", size=13, color="white"),
                    ft.Text("2. Selects Engineering Role: Engineer, Supervisor, or Student", size=13, color="white"),
                    ft.Text("3. Selects Domain: Mining, Metallurgical, or Civil", size=13, color="white"),
                    ft.Text("4. Frontend validation before API call", size=13, color="white"),
                    ft.Text("5. Backend creates account with hashed password (bcrypt)", size=13, color="white"),
                    ft.Text("6. User redirected to login page", size=13, color="white"),
                ], spacing=8),
                ft.Container(height=5),
                ft.Text("Login Flow:", size=16, weight="bold", color="#ff69b4"),
                ft.Column([
                    ft.Text("1. User enters email and password", size=13, color="white"),
                    ft.Text("2. Email format validation using regex", size=13, color="white"),
                    ft.Text("3. Password visibility toggle for user convenience", size=13, color="white"),
                    ft.Text("4. Loading state during API call", size=13, color="white"),
                    ft.Text("5. Error handling for invalid credentials", size=13, color="white"),
                    ft.Text("6. On success: JWT token stored, user redirected to dashboard", size=13, color="white"),
                ], spacing=8),
            ], spacing=12),
            padding=25, bgcolor="#1e293b",
        )
    )
    main_column.controls.append(ft.Container(height=15))
    
    # Blog Post 2 with Math
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("🛡️ Blog Post 2: Security Best Practices with Mathematical Models", size=20, weight="bold", color="#ff69b4"),
                ft.Divider(height=5, color="#334155"),
                ft.Text("Password Strength Formula (Entropy):", size=16, weight="bold", color="#ff69b4"),
                ft.Container(
                    content=ft.Text("Entropy (bits) = L × log₂(C)", size=20, color="white"),
                    padding=20, bgcolor="#0f172a",
                ),
                ft.Text("Where: L = password length, C = character set size", size=12, color="white"),
                ft.Container(height=5),
                ft.Text("Example Calculation:", size=16, weight="bold", color="#ff69b4"),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Password: 12 characters (a-z, A-Z, 0-9) → C = 62", size=13, color="white"),
                        ft.Text("Entropy = 12 × log₂(62) = 12 × 5.95 = 71.4 bits", size=13, color="white"),
                        ft.Text("Result: 71.4 bits - Very Strong Password", size=13, color="#22c55e"),
                    ], spacing=8),
                    padding=15, bgcolor="#0f172a",
                ),
                ft.Text("Security Best Practices Implemented:", size=16, weight="bold", color="#ff69b4"),
                ft.Column([
                    ft.Text("• Passwords are never stored in plain text - hashed using bcrypt", size=13, color="white"),
                    ft.Text("• JWT tokens with expiration for session management", size=13, color="white"),
                    ft.Text("• Rate limiting on login attempts to prevent brute force", size=13, color="white"),
                    ft.Text("• Input validation on both frontend and backend", size=13, color="white"),
                ], spacing=8),
            ], spacing=12),
            padding=25, bgcolor="#1e293b",
        )
    )
    main_column.controls.append(ft.Container(height=15))
    
    # Blog Post 3 with Video - NO ICONS, JUST TEXT AND EMOJIS
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("💻 Blog Post 3: Frontend Implementation + Video Reflection", size=20, weight="bold", color="#ff69b4"),
                ft.Divider(height=5, color="#334155"),
                ft.Text("Password Visibility Toggle Implementation:", size=16, weight="bold", color="#ff69b4"),
                ft.Container(
                    content=ft.Text("const [showPassword, setShowPassword] = useState(false);\nconst togglePassword = () => setShowPassword(!showPassword);\n\n<input type={showPassword ? 'text' : 'password'} />\n<button onClick={togglePassword}>\n    {showPassword ? '🙈 Hide' : '👁️ Show'}\n</button>", size=11, color="white"),
                    padding=20, bgcolor="#0f172a",
                ),
                ft.Text("Email Validation Example:", size=16, weight="bold", color="#ff69b4"),
                ft.Container(
                    content=ft.Text("const validateEmail = (email) => {\n    const re = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;\n    return re.test(email);\n};\n\nif (!validateEmail(email)) {\n    setError('Please enter a valid email address');\n    return;\n}", size=11, color="white"),
                    padding=20, bgcolor="#0f172a",
                ),
                ft.Text("📹 Video Reflection", size=18, weight="bold", color="#ff69b4", text_align="center"),
                
                # Video Play Button - Using only emojis and text (NO Flet ICONS)
                ft.Container(
                    content=ft.Column([
                        ft.Text("🎬", size=80, text_align="center"),
                        ft.Text("CLICK TO PLAY REFLECTION VIDEO", size=16, weight="bold", text_align="center", color="#ff69b4"),
                        ft.Text("Topics: Registration flow, login validation, password security, PR reviews, team collaboration", size=12, color="white", text_align="center"),
                        ft.Text("👇 Click anywhere on this box to play the video", size=11, color="white", text_align="center"),
                    ], horizontal_alignment="center", spacing=15),
                    padding=30, 
                    bgcolor="#0f172a",
                    on_click=play_video,
                    border_radius=10,
                ),
                
                ft.Divider(height=20, color="#334155"),
                
                ft.Text("📚 Key Takeaways from the Triad_Of_Terror Project:", size=18, weight="bold", color="#ff69b4"),
                ft.Column([
                    ft.Text("✓ Authentication is critical for protecting engineering calculations in Mining, Metallurgical & Civil modules", size=13, color="white"),
                    ft.Text("✓ Password visibility toggle improves user experience significantly", size=13, color="white"),
                    ft.Text("✓ Working in a 20-member team taught me effective Git workflow (branches: improved-password, making-auth-better)", size=13, color="white"),
                    ft.Text("✓ Code reviews (8 performed) help catch security issues early", size=13, color="white"),
                    ft.Text("✓ All 3 pull requests (#5, #6, #9) were successfully merged after team approval", size=13, color="white"),
                ], spacing=8),
                
                ft.Row([
                    ft.TextButton("🔗 View GitHub Evidence", on_click=lambda e: scroll_to_section(e, "github"), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                    ft.TextButton("🐙 My GitHub Profile", on_click=lambda e: webbrowser.open(GITHUB_PROFILE), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                ], alignment="center", spacing=20),
            ], spacing=15),
            padding=25, 
            bgcolor="#1e293b",
        )
    )
    
    # ========== CONTACT SECTION ==========
    main_column.controls.append(ft.Container(height=50))
    
    contact_section = ft.Container(
        key="contact",
        content=ft.Column([
            ft.Text("📬 Contact Me", size=38, weight="bold", color="#ff69b4", text_align="center"),
            ft.Container(height=25),
        ], horizontal_alignment="center")
    )
    main_column.controls.append(contact_section)
    
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("📞 +264 81 548 0479", size=18, color="white"),
                ft.Text("📧 pashukenikaluvi14@gmail.com", size=18, color="white"),
                ft.Text("📍 Windhoek, Namibia", size=18, color="white"),
                ft.Text(f"🐙 {GITHUB_PROFILE}", size=14, color="white"),
                ft.Divider(height=15, color="#334155"),
                ft.Row([
                    ft.TextButton("📧 Send Email", on_click=lambda e: webbrowser.open("mailto:pashukenikaluvi14@gmail.com"), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                    ft.TextButton("🐙 GitHub", on_click=lambda e: webbrowser.open(GITHUB_PROFILE), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                    ft.TextButton("📁 Repository", on_click=lambda e: webbrowser.open(GITHUB_REPO), style=ft.ButtonStyle(bgcolor="#ff69b4", color="white")),
                ], alignment="center", spacing=20, wrap=True),
            ], spacing=20, horizontal_alignment="center"),
            padding=35, bgcolor="#1e293b",
        )
    )
    
    # ========== FOOTER ==========
    main_column.controls.append(ft.Container(height=50))
    main_column.controls.append(
        ft.Container(
            content=ft.Column([
                ft.Text("© 2026 Pashukeni I Kaluvi | Electrical Engineering Portfolio", size=12, text_align="center", color="white"),
                ft.Text("Built with Flet Python Framework | Authentication Developer for Triad_Of_Terror", size=11, color="white", text_align="center"),
                ft.Text("Individual Web Portfolio - CA Weighting: 15%", size=11, color="white", text_align="center"),
            ], spacing=8, horizontal_alignment="center"),
            padding=25, bgcolor="#020617",
        )
    )
    
    # Add the main column to the page
    page.add(main_column)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)