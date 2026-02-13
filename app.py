'''import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="AivancityX Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------------
# 2. Load CSS Styles
# ---------------------------------------------------------
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    # Fallback if CSS is missing
    st.markdown("""
        <style>
        [data-testid="stMetric"] {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.title("🎓 AivancityX")
    st.markdown("### Menu")

    # Navigation Selection
    selected_page = st.radio(
        "Navigate to:",
        ["Dashboard", "Students", "Progress", "Settings"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.info("Logged in as: **Admin**")

# ---------------------------------------------------------
# 4. Main Page Logic
# ---------------------------------------------------------

if selected_page == "Dashboard":

    # --- Header ---
    st.title("Dashboard Overview")
    st.markdown("Welcome back, Administrator. Here is the latest EdTech performance overview.")
    st.markdown("---")

    # --- KPI Metrics Row ---
    # Using columns to create the card layout
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(label="Total Students", value="1,240", delta="12%")
    with kpi2:
        st.metric(label="Active Students", value="850", delta="-2%")
    with kpi3:
        st.metric(label="Completion Rate", value="68%", delta="5.4%")
    with kpi4:
        st.metric(label="Certifications", value="412", delta="18 Issued")

    st.markdown("###") # Spacer

    # --- Charts Section ---
    chart_col1, chart_col2 = st.columns([2, 1])

    with chart_col1:
        st.subheader("Student Progress by Module")
        # Mock Data for Bar Chart
        bar_data = pd.DataFrame({
            "Module": ["Intro to AI", "Python Basics", "Data Analysis", "Machine Learning", "Deep Learning"],
            "Avg Progress": [95, 88, 72, 60, 45]
        })

        # Professional Blue Color: #4F46E5
        fig_bar = px.bar(
            bar_data,
            x="Module",
            y="Avg Progress",
            color_discrete_sequence=["#4F46E5"]
        )
        fig_bar.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="",
            yaxis_title="Completion %"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with chart_col2:
        st.subheader("Enrollment Status")
        # Mock Data for Pie Chart
        pie_data = pd.DataFrame({
            "Status": ["Completed", "In-Progress", "Pending"],
            "Count": [300, 850, 90]
        })

        # EdTech Palette: Blue, Purple, Light Blue
        fig_pie = px.pie(
            pie_data,
            values="Count",
            names="Status",
            color_discrete_sequence=["#4F46E5", "#818CF8", "#C7D2FE"],
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")

    # --- Student Table Section ---
    st.subheader("Recent Student Registrations")

    student_data = pd.DataFrame({
        "Name": ["Alice Johnson", "Bob Smith", "Charlie Davis", "Dana Lee", "Erikson G."],
        "Program": ["Data Science", "AI Engineering", "Data Science", "Business AI", "AI Engineering"],
        "Progress": [85, 42, 12, 100, 65],
        "Status": ["Active", "Active", "Pending", "Completed", "Active"]
    })

    # Display dataframe with custom column formatting
    st.dataframe(
        student_data,
        use_container_width=True,
        column_config={
            "Progress": st.column_config.ProgressColumn(
                "Progress %",
                format="%d%%",
                min_value=0,
                max_value=100,
            ),
            "Status": st.column_config.TextColumn(
                "Status",
                help="Current enrollment status"
            )
        },
        hide_index=True
    )

# ---------------------------------------------------------
# Placeholder Pages for Navigation
# ---------------------------------------------------------
elif selected_page == "Students":
    st.title("Student Management Directory")
    st.write("Full student list functionality goes here...")

elif selected_page == "Progress":
    st.title("Detailed Progress Analytics")
    st.write("Advanced charts and reports go here...")

elif selected_page == "Settings":
    st.title("Platform Settings")
    st.write("Configuration options go here...")'''

import pandas as pd
import plotly.express as px
import streamlit as st

# ONLY CALL THIS ONCE AT THE VERY TOP
st.set_page_config(
    page_title="AivancityX | Admin Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- THEME & VISIBILITY GUARD ---
# This CSS ensures high contrast even if the system is in Dark Mode
st.markdown("""
    <style>
    /* Force Light Mode Aesthetics */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Global Visibility for Text */
    h1, h2, h3, h4, p, span, label, .stMarkdown {
        color: #1E293B !important;
        font-weight: 500 !important;
    }
    
    /* Ensure Sidebars and Buttons are clear */
    [data-testid="stSidebar"] { background-color: #F8FAFC !important; }
    [data-testid="stSidebar"] * { color: #1E293B !important; }
    
    /* Card visibility fix */
    [data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIN LOGIC ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    # Centered Login UI
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.title("🎓 Admin Login")
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", type="primary", use_container_width=True):
            if user == "admin" and password == "aivancity2026":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials")
    st.stop()
# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="AivancityX | Admin Portal",
    page_icon="🎓",
    layout="wide"
)

# 2. LOAD CUSTOM CSS
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Assets folder or style.css missing! Please create assets/style.css")

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.title("🎓 AivancityX")
    st.markdown("MAIN MENU")
    page = st.radio("Select Page", ["Dashboard", "Students", "Progress", "Settings"], label_visibility="collapsed")
    st.markdown("---")
    st.button("Log Out", use_container_width=True)

# ---------------------------------------------------------
# PAGE 1: DASHBOARD
# ---------------------------------------------------------
if page == "Dashboard":
    # --- 1. HEADER WITH ACTION ---
    h1, h2 = st.columns([3, 1])
    with h1:
        st.title("Dashboard Overview")
        st.caption("Real-time insights into AivancityX student performance and engagement.")
    with h2:
        st.markdown("###")
        st.button("🔄 Refresh Data", use_container_width=True)

    # --- 2. ADVANCED KPI CARDS (With Trend Indicators) ---
    # We use HTML/Markdown to add the colored trend arrows from your reference
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Total Students", "1,240", "↑ 12%", delta_color="normal")
    with m2:
        st.metric("Active Now", "850", "⚡ +5%", delta_color="normal")
    with m3:
        st.metric("Avg. Completion", "68%", "↑ 2.4%", delta_color="normal")
    with m4:
        st.metric("At Risk", "42", "↓ 5%", delta_color="inverse") # Red if up, Green if down

    st.markdown("---")

    # --- 3. ANALYTICS ROW ---
    col_main, col_side = st.columns([2, 1])

    with col_main:
        st.subheader("Student Progress Tracking")
        # Advanced Multi-color Bar Chart
        prog_data = pd.DataFrame({
            "Module": ["Mod 1", "Mod 2", "Mod 3", "Mod 4", "Mod 5"],
            "Completed": [950, 820, 600, 450, 120],
            "Ongoing": [200, 300, 450, 500, 300]
        })
        fig_prog = px.bar(prog_data, x="Module", y=["Completed", "Ongoing"],
                          barmode="group",
                          color_discrete_sequence=["#4F46E5", "#C7D2FE"])
        fig_prog.update_layout(plot_bgcolor="rgba(0,0,0,0)", height=350, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig_prog, use_container_width=True)

    with col_side:
        st.subheader("Global Engagement")
        # Donut chart with specific center text
        status_df = pd.DataFrame({"Status": ["Engaged", "Passive", "Inactive"], "Values": [70, 20, 10]})
        fig_donut = px.pie(status_df, values="Values", names="Status", hole=0.7,
                           color_discrete_sequence=["#6366F1", "#A5B4FC", "#E2E8F0"])
        fig_donut.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=350)
        st.plotly_chart(fig_donut, use_container_width=True)

    # --- 4. ACTIONABLE INSIGHTS & RECENT ACTIVITY ---
    st.markdown("---")
    c_left, c_right = st.columns(2)

    with c_left:
        st.subheader("⚠️ Urgent Alerts")
        st.error("**Drop-off Warning:** Module 3 completion has decreased by 15% this week.")
        st.warning("**Review Required:** 12 students in 'AI Ethics' have not logged in for 5 days.")

    with c_right:
        st.subheader("🕒 Recent Activity")
        activity_data = pd.DataFrame([
            {"Event": "New Enrollment", "User": "Sarah Jenkins", "Time": "2 mins ago"},
            {"Event": "Certification Issued", "User": "Marc Dubois", "Time": "15 mins ago"},
            {"Event": "Exam Passed", "User": "Chen Wei", "Time": "1 hour ago"}
        ])
        st.table(activity_data)

    # --- 5. DETAILED OVERVIEW TABLE ---
    st.markdown("### Detailed Student Overview")
    df_students = pd.DataFrame([
        {"Student": "John Doe", "Program": "Data Science", "Progress": 85, "Status": "Active"},
        {"Student": "Alice Smith", "Program": "AI Ethics", "Progress": 100, "Status": "Completed"},
        {"Student": "Robert Johnson", "Program": "MLOps", "Progress": 42, "Status": "At Risk"},
    ])

    st.dataframe(df_students, use_container_width=True, hide_index=True,
                 column_config={"Progress": st.column_config.ProgressColumn(format="%d%%")})

# ---------------------------------------------------------
# PAGE 2: STUDENTS (ADVANCED EDITION)
# ---------------------------------------------------------
elif page == "Students":
    st.title("Student Management")
    st.caption("Manage enrollments, edit data live, and manually add student records.")

    # --- 1. DATA PERSISTENCE (Session State) ---
    if "master_data" not in st.session_state:
        st.session_state.master_data = pd.DataFrame([
            {"Name": "John Doe", "Email": "john.d@aivancity.com", "Program": "Data Science MSc",
             "Cohort": "Fall 2023", "Date": "Oct 12, 2023", "Progress": 85, "Status": "Active"},
            {"Name": "Alice Smith", "Email": "alice.s@aivancity.com", "Program": "AI Ethics",
             "Cohort": "Spring 2023", "Date": "Feb 15, 2023", "Progress": 100, "Status": "Completed"},
            {"Name": "Robert Johnson", "Email": "rob.j@aivancity.com", "Program": "Machine Learning",
             "Cohort": "Fall 2023", "Date": "Nov 05, 2023", "Progress": 45, "Status": "At Risk"},
            {"Name": "Emma Lee", "Email": "emma.lee@aivancity.com", "Program": "Data Science MSc",
             "Cohort": "Fall 2023", "Date": "Oct 15, 2023", "Progress": 92, "Status": "Active"},
        ])

    # --- 2. HEADER ACTION BAR ---
    f1, f2, f3, f4 = st.columns([3, 1.5, 1, 1])

    with f1:
        search_query = st.text_input(
            "Search",
            placeholder="🔍 Search name or email...",
            label_visibility="collapsed"
        )

    with f2:
        program_filter = st.selectbox(
            "Program",
            ["All"] + list(st.session_state.master_data["Program"].unique()),
            label_visibility="collapsed"
        )

    with f3:
        with st.popover("➕ Add New Student", use_container_width=True):
            st.markdown("### New Student Profile")
            with st.form("manual_entry", clear_on_submit=True):
                n_name = st.text_input("Full Name")
                n_email = st.text_input("Email")
                n_prog = st.selectbox(
                    "Program",
                    ["Data Science MSc", "AI Ethics", "Machine Learning"]
                )
                n_cohort = st.selectbox(
                    "Cohort",
                    ["Fall 2023", "Spring 2024"]
                )

                if st.form_submit_button("Enroll Student", type="primary", use_container_width=True):
                    if n_name and n_email:
                        new_row = pd.DataFrame([{
                            "Name": n_name,
                            "Email": n_email,
                            "Program": n_prog,
                            "Cohort": n_cohort,
                            "Date": pd.Timestamp.now().strftime("%b %d, %Y"),
                            "Progress": 0,
                            "Status": "Active"
                        }])
                        st.session_state.master_data = pd.concat(
                            [st.session_state.master_data, new_row],
                            ignore_index=True
                        )
                        st.toast(f"✅ {n_name} added successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill Name and Email.")

    with f4:
        csv = st.session_state.master_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Export",
            data=csv,
            file_name="students.csv",
            use_container_width=True
        )

    st.markdown("---")

    # --- 3. FILTER LOGIC ---
    filtered_df = st.session_state.master_data.copy()

    if search_query:
        filtered_df = filtered_df[
            filtered_df["Name"].str.contains(search_query, case=False, na=False) |
            filtered_df["Email"].str.contains(search_query, case=False, na=False)
            ]

    if program_filter != "All":
        filtered_df = filtered_df[
            filtered_df["Program"] == program_filter
            ]

    # --- 4. LIVE DATA EDITOR ---
    edited_df = st.data_editor(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        num_rows="dynamic",
        column_config={
            "Progress": st.column_config.ProgressColumn(
                format="%d%%", min_value=0, max_value=100
            ),
            "Status": st.column_config.SelectboxColumn(
                options=["Active", "Completed", "At Risk"]
            ),
            "Email": st.column_config.LinkColumn("Email"),
            "Date": st.column_config.TextColumn(disabled=True),
        }
    )

    # --- 5. SAVE CHANGES BACK TO SESSION STATE ---
    st.session_state.master_data.update(edited_df)

    st.caption(f"Total students in database: {len(st.session_state.master_data)}")


# ---------------------------------------------------------
# PAGE 3: PROGRESS (NEW SECTION)
# ---------------------------------------------------------
elif page == "Progress":
    st.title("📈 Progress Analytics")
    st.caption("Detailed tracking of student learning milestones and engagement trends.")

    # --- 1. INTERACTIVE FILTER HEADER ---
    with st.container():
        f1, f2, f3 = st.columns([2, 1, 1])
        with f1:
            st.selectbox("Filter by Program", ["All Programs", "Data Science MSc", "AI Ethics", "Machine Learning"], label_visibility="collapsed")
        with f2:
            st.selectbox("Current Cohort", ["Fall 2023", "Spring 2024"], label_visibility="collapsed")
        with f3:
            st.date_input("Select Period", label_visibility="collapsed")

    st.markdown("---")

    # --- 2. ADVANCED KPI ROW (Progress Specific) ---
    p1, p2, p3, p4 = st.columns(4)
    p1.metric("Avg. Completion", "74%", "+5.2%")
    p2.metric("Weekly Active Users", "912", "⚡ High")
    p3.metric("Avg. Quiz Score", "82/100", "+2.1")
    p4.metric("Drop-off Rate", "12%", "-1.5%", delta_color="inverse")

    # --- 3. ANALYTICS CHARTS ---
    st.markdown("### Learning Insights")
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("Engagement Heatmap (Weekly)")
        # Creating a heatmap of learning hours
        engagement_data = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Morning": [45, 52, 38, 60, 42, 21, 15],
            "Afternoon": [88, 76, 82, 90, 70, 30, 20],
            "Evening": [65, 82, 95, 110, 85, 45, 35]
        }).set_index("Day")

        fig_heat = px.imshow(engagement_data,
                             labels=dict(x="Time of Day", y="Day", color="Users Active"),
                             color_continuous_scale="Purples")
        fig_heat.update_layout(height=350)
        st.plotly_chart(fig_heat, use_container_width=True)

    with c2:
        st.subheader("Score Distribution")
        # Histogram showing how many students fall into score brackets
        scores = [55, 60, 65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98]
        fig_dist = px.histogram(scores, nbins=5, color_discrete_sequence=["#818CF8"])
        fig_dist.update_layout(showlegend=False, height=350, bargap=0.1)
        st.plotly_chart(fig_dist, use_container_width=True)

    # --- ALTERNATIVE: PROGRESS OVER TIME ---
    st.subheader("Cumulative Milestone Achievement")
    time_data = pd.DataFrame({
        "Month": ["Sept", "Oct", "Nov", "Dec"],
        "Mod 1": [400, 800, 1100, 1200],
        "Mod 2": [0, 300, 700, 1000],
        "Finals": [0, 0, 100, 600]
    })
    fig_area = px.area(time_data, x="Month", y=["Mod 1", "Mod 2", "Finals"],
                       color_discrete_sequence=["#C7D2FE", "#818CF8", "#4F46E5"])
    st.plotly_chart(fig_area, use_container_width=True)
# ---------------------------------------------------------
# PAGE 4: SETTINGS
# ---------------------------------------------------------
elif page == "Settings":
    st.title("Settings")
    st.caption("Manage platform configuration, branding, and user access levels.")

    # --- 1. HORIZONTAL TABS ---
    # Recreating the navigation bar: Profile, Institution, Notifications, Security
    tab_prof, tab_inst, tab_notif, tab_sec = st.tabs(["Profile", "Institution", "Notifications", "Security"])

    with tab_inst:
        # --- SECTION: GENERAL INFORMATION ---
        st.markdown("### General Information")
        st.info("Configure the basic details of your educational institution.")

        col_name, col_lang = st.columns(2)
        with col_name:
            st.text_input("Platform Name", value="AivancityX Learning")
        with col_lang:
            st.selectbox("Default Language", ["English (US)", "French (FR)", "Spanish (ES)"])

        st.text_area("Institution Description",
                     value="Leading institution in AI and Data Science education.",
                     height=100)

        st.markdown("---")

        # --- SECTION: BRANDING COLORS ---
        st.markdown("### Branding Colors")
        st.caption("Customize the look and feel of your dashboard.")

        c1, c2, c3 = st.columns(3)
        with c1:
            primary = st.color_picker("Primary Color", "#1313EC", help="Used for buttons and active states.")
        with c2:
            accent = st.color_picker("Accent Color", "#6366F1", help="Used for secondary elements.")
        with c3:
            sidebar_bg = st.color_picker("Sidebar Background", "#FFFFFF")

        if st.button("Save Branding Settings", type="primary"):
            st.success("Branding updated successfully!")

        st.markdown("---")

        # --- SECTION: USER ROLE MANAGEMENT ---
        st.markdown("### User Role Management")
        st.caption("Define access levels for different user types.")

        role_data = pd.DataFrame([
            {"Role Name": "Administrator", "Users": 4, "Permissions": "Full Access", "Action": "🔒"},
            {"Role Name": "Professor", "Users": 12, "Permissions": "Course Management", "Action": "✏️"},
            {"Role Name": "Student", "Users": 1240, "Permissions": "Learning Content", "Action": "✏️"}
        ])

        # Formatting the table to match your screenshot
        st.dataframe(
            role_data,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Permissions": st.column_config.TextColumn(
                    "Permissions",
                    help="What this role can do"
                ),
                "Action": st.column_config.TextColumn("Action", width="small")
            }
        )

        if st.button("+ Add Role"):
            st.write("Role creation modal would open here.")

    with tab_prof:
        st.subheader("Admin Profile")
        col_p1, col_p2 = st.columns([1, 3])
        with col_p1:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Placeholder avatar
        with col_p2:
            st.text_input("Full Name", value="Dr. Sarah C.")
            st.text_input("Email", value="sarah.c@aivancity.edu")