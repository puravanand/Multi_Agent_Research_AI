
# import streamlit as st
# from main import run_pipeline
# import re
# import time

# st.set_page_config(
#     page_title="ResearchAI | Multi-Agent Research",
#     page_icon="🔬",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

# .stApp {
#     background:
#         radial-gradient(ellipse at 0% 0%, #25205b 0%, transparent 38%),
#         radial-gradient(ellipse at 100% 0%, #103c58 0%, transparent 35%),
#         #0b1020;
#     color: #f4f6ff;
# }
# .block-container {max-width:1450px;padding-top:2rem;padding-bottom:3rem}
# [data-testid="stSidebar"] {
#     background:linear-gradient(180deg,#171b36,#0c1222);
#     border-right:1px solid #303754;
# }
# .hero {
#     padding:32px;border-radius:24px;
#     background:linear-gradient(120deg,#6545df,#864bdc,#138fc5);
#     margin-bottom:24px;
#     box-shadow:0 15px 45px #25205b66;
# }
# .hero h1 {font-size:clamp(30px,4vw,44px);font-weight:800;color:white}
# .hero p {font-size:16px;line-height:1.7;color:#f0edff}
# .section-title {font-size:23px;font-weight:800;margin:24px 0 15px}
# .metric-card,.agent-card {
#     background:linear-gradient(145deg,#1e2948,#141b30);
#     border:1px solid #384361;border-radius:17px;padding:20px;
#     margin-bottom:10px;
# }
# .metric-label {color:#aab6d5;font-size:13px}
# .metric-value {font-size:28px;font-weight:800;color:white}
# .agent-card {padding:16px 18px}
# .agent-name {font-weight:750;font-size:16px;color:white}
# .agent-desc {font-size:13px;color:#aebbd8;margin-top:5px}
# div.stButton>button,div[data-testid="stFormSubmitButton"]>button {
#     background:linear-gradient(100deg,#7856f5,#3987f6);
#     color:white;border:0;border-radius:12px;font-weight:750;min-height:46px;
# }
# .stTextArea textarea {
#     background:#151d33!important;color:white!important;
#     border:1px solid #465477!important;border-radius:12px!important;
# }
# [data-testid="stTabs"] button {color:#c6d0ed;font-weight:650}
# [data-testid="stTabs"] button[aria-selected="true"] {color:#b7a8ff}
# .stDownloadButton button {
#     background:#182642;color:#dce5ff;border:1px solid #53658b;border-radius:10px;
# }
# .footer {text-align:center;color:#8290b2;padding-top:30px;font-size:12px}
# </style>
# """, unsafe_allow_html=True)

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     st.markdown("## 🔬 ResearchAI")
#     st.caption("MULTI-AGENT RESEARCH WORKSPACE")
#     st.divider()
#     st.markdown("### 🧠 Your AI Team")
#     st.markdown("""
#     🔎 **Search Agent** — discovers sources

#     🌐 **Web Scraper** — collects webpage content

#     ✍️ **Writer Chain** — generates the report

#     🛡️ **Review Chain** — evaluates the report
#     """)
#     st.divider()
#     st.caption("Built with Python · LangChain · Streamlit")
#     st.caption("Always verify citations and facts.")

# # ---------------- HERO ----------------
# st.markdown("""
# <div class="hero">
#     <div style="font-size:12px;font-weight:800;letter-spacing:2px">
#         ✦ INTELLIGENT RESEARCH WORKSPACE
#     </div>
#     <h1>Turn Questions Into Research.</h1>
#     <p>Research, synthesize, write and review — all from one AI-powered workspace.</p>
# </div>
# """, unsafe_allow_html=True)

# # ---------------- FEATURE CARDS ----------------
# cols = st.columns(4)
# features = [
#     ("🔎", "Web Research", "Search Agent"),
#     ("🌐", "Source Collection", "Web Scraper"),
#     ("✍️", "Report Writing", "Writer Chain"),
#     ("🛡️", "Quality Review", "Review Chain")
# ]
# for col, (icon, name, desc) in zip(cols, features):
#     with col:
#         st.markdown(f"""
#         <div class="metric-card">
#             <div style="font-size:25px">{icon}</div>
#             <div class="metric-label">{name}</div>
#             <b>{desc}</b>
#         </div>
#         """, unsafe_allow_html=True)

# # ---------------- RESEARCH INPUT ----------------
# st.markdown('<div class="section-title">🚀 Start Research</div>',
#             unsafe_allow_html=True)

# with st.container(border=True):
#     with st.form("research_form"):
#         topic = st.text_area(
#             "Research topic",
#             placeholder="Example: Recent advances in lung cancer diagnosis",
#             height=100
#         )
#         submitted = st.form_submit_button(
#             "✨ Generate Research Report",
#             use_container_width=True
#         )

# if submitted:
#     if not topic.strip():
#         st.warning("Please enter a research topic.")
#     else:
#         # These statuses represent overall pipeline execution.
#         # Exact per-agent status requires stage callbacks from main.py.
#         st.session_state["pipeline_started"] = True
#         st.session_state["research_topic"] = topic.strip()
#         st.session_state.pop("research_result", None)

#         st.markdown('<div class="section-title">⚙️ Pipeline Progress</div>',
#                     unsafe_allow_html=True)

#         progress = st.progress(0)
#         status_box = st.status(
#             "Research pipeline is running...",
#             expanded=True
#         )

#         try:
#             status_box.write("⏳ Running the existing research pipeline...")
#             progress.progress(10)

#             result = run_pipeline(topic.strip())

#             if not isinstance(result, dict):
#                 raise TypeError(
#                     "run_pipeline() must return a dictionary."
#                 )

#             progress.progress(100)
#             status_box.update(
#                 label="✅ Research pipeline completed",
#                 state="complete",
#                 expanded=False
#             )

#             st.session_state["research_result"] = result
#             st.success("Research results are ready!")

#         except Exception as error:
#             status_box.update(
#                 label="❌ Pipeline failed",
#                 state="error",
#                 expanded=True
#             )
#             st.error("An error occurred while running the pipeline.")
#             st.exception(error)

# # ---------------- RESULTS ----------------
# result = st.session_state.get("research_result")
# saved_topic = st.session_state.get("research_topic", "")

# if result:
#     st.divider()
#     st.markdown('<div class="section-title">📊 Research Dashboard</div>',
#                 unsafe_allow_html=True)
#     st.markdown(f"**Topic:** {saved_topic}")

#     report = str(result.get("report", "") or "")
#     review = str(result.get("ranking", "") or "")
#     search_data = str(result.get("search_result", "") or "")
#     scraped_data = str(result.get("web_result", "") or "")

#     # Extract an explicit reviewer score, if present.
#     score = None
#     patterns = [
#         r"(?i)\b(?:overall\s+)?(?:score|rating)\s*(?:is|of|:|=|-)?\s*"
#         r"(\d{1,2}(?:\.\d+)?)\s*(?:/\s*10|out\s+of\s+10)\b",
#         r"(?i)\b(\d{1,2}(?:\.\d+)?)\s*/\s*10\b",
#         r"(?i)\b(\d{1,2}(?:\.\d+)?)\s+out\s+of\s+10\b"
#     ]

#     for pattern in patterns:
#         match = re.search(pattern, review)
#         if match:
#             candidate = float(match.group(1))
#             if 0 <= candidate <= 10:
#                 score = candidate
#                 break

#     # ---------------- RATING ----------------
#     st.markdown('<div class="section-title">⭐ AI Report Rating</div>',
#                 unsafe_allow_html=True)

#     if score is not None:
#         score_col, progress_col = st.columns([1, 2])
#         with score_col:
#             st.markdown(f"""
#             <div class="metric-card">
#                 <div class="metric-label">OVERALL REVIEW SCORE</div>
#                 <div class="metric-value">{score:g}<span
#                 style="font-size:16px;color:#aab6d5"> / 10</span></div>
#             </div>
#             """, unsafe_allow_html=True)
#         with progress_col:
#             st.markdown("#### Quality score")
#             st.progress(score / 10)
#             if score >= 8:
#                 st.success("Strong score according to the AI reviewer.")
#             elif score >= 6:
#                 st.info("Some improvements may be useful.")
#             else:
#                 st.warning("Review the feedback and improve the report.")
#     else:
#         st.info(
#             "The reviewer did not provide a detectable score out of 10. "
#             "See the AI Review tab for the full feedback."
#         )

#     st.caption(
#         "The rating is AI-generated and is not an independently verified score."
#     )

#     # ---------------- TABS ----------------
#     tab_report, tab_review, tab_search, tab_scrape, tab_agents = st.tabs([
#         "📄 Research Report",
#         "🛡️ AI Review",
#         "🔎 Search Results",
#         "🌐 Scraped Content",
#         "✅ Pipeline Status"
#     ])

#     with tab_report:
#         if report:
#             st.markdown(report)
#             st.download_button(
#                 "⬇️ Download Report",
#                 data=report,
#                 file_name="research_report.md",
#                 mime="text/markdown",
#                 use_container_width=True
#             )
#         else:
#             st.info("No report returned.")

#     with tab_review:
#         if review:
#             st.markdown(review)
#             st.download_button(
#                 "⬇️ Download Review",
#                 data=review,
#                 file_name="research_review.md",
#                 mime="text/markdown",
#                 use_container_width=True
#             )
#         else:
#             st.info("No review returned.")

#     with tab_search:
#         st.markdown(search_data or "No search output returned.")

#         if search_data:
#             st.download_button(
#                 "⬇️ Download Search Results",
#                 data=search_data,
#                 file_name="search_results.txt",
#                 mime="text/plain"
#             )

#     with tab_scrape:
#         st.markdown(scraped_data or "No scraped content returned.")

#         if scraped_data:
#             st.download_button(
#                 "⬇️ Download Scraped Content",
#                 data=scraped_data,
#                 file_name="scraped_content.txt",
#                 mime="text/plain"
#             )

#     with tab_agents:
#         st.info(
#             "The existing run_pipeline() function returns its results after "
#             "the pipeline finishes. Therefore this UI cannot truthfully show "
#             "individual agent start/finish ticks in real time without stage "
#             "updates from the backend."
#         )

#         st.markdown("### Pipeline components")
#         st.markdown("""
#         - 🔎 **Search Agent** — runs as part of the backend pipeline
#         - 🌐 **Web Scraper** — collects source content
#         - ✍️ **Writer Chain** — produces the report
#         - 🛡️ **Review Chain** — creates reviewer feedback
#         """)

#         st.caption(
#             "To display a green tick immediately after each individual agent "
#             "finishes, add a small progress callback to main.py. The AI "
#             "agents and tools themselves do not need to be rewritten."
#         )

#     st.warning(
#         "Verify source URLs, statistics, and citations before relying on "
#         "AI-generated research."
#     )

# else:
#     st.markdown('<div class="section-title">✨ How It Works</div>',
#                 unsafe_allow_html=True)
#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.markdown("""
#         <div class="metric-card">
#             <h3>01 · Discover</h3>
#             <p>Search the web for relevant sources.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     with c2:
#         st.markdown("""
#         <div class="metric-card">
#             <h3>02 · Synthesize</h3>
#             <p>Collect information and generate a structured report.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     with c3:
#         st.markdown("""
#         <div class="metric-card">
#             <h3>03 · Review</h3>
#             <p>Inspect the reviewer feedback and score, when provided.</p>
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown("""
# <div class="footer">
#     RESEARCHAI · MULTI-AGENT RESEARCH WORKSPACE<br>
#     Research responsibly. Verify before you cite.
# </div>
# """, unsafe_allow_html=True)
import inspect
import queue
import re
import threading
import time

import streamlit as st

from main import run_pipeline

st.set_page_config(
    page_title="ResearchAI | Multi-Agent Research",
    page_icon="🔬",
    layout="wide",
)

# ======================================================================
# STAGES
# ======================================================================
STAGES = [
    # key, icon, name, running text, done text, color, est. seconds
    ("search", "🔎", "Search Agent", "Searching the web for sources…", "Sources discovered", "#38bdf8", 15),
    ("scrape", "🌐", "Web Scraper", "Collecting webpage content…", "Content collected", "#2dd4bf", 20),
    ("writer", "✍️", "Writer Chain", "Writing the research report…", "Report written", "#a78bfa", 30),
    ("review", "🛡️", "Review Chain", "Reviewing and scoring the report…", "Review complete", "#f472b6", 15),
]
STAGE_KEYS = [s[0] for s in STAGES]

# ======================================================================
# STYLES
# ======================================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"], .stApp {font-family:'Inter',sans-serif;}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, rgba(124,58,237,.35) 0, transparent 35%),
        radial-gradient(circle at 95% 8%, rgba(14,165,233,.30) 0, transparent 35%),
        radial-gradient(circle at 50% 100%, rgba(236,72,153,.18) 0, transparent 40%),
        #070b18;
    color:#eef2ff;
}
#MainMenu, footer, header[data-testid="stHeader"] {visibility:hidden; height:0}
.block-container {max-width:1350px; padding-top:1.5rem; padding-bottom:3rem}

[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#141833,#080c1a);
    border-right:1px solid rgba(255,255,255,.08);
}

/* ---------- HERO ---------- */
@keyframes gradShift {0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.hero {
    position:relative; overflow:hidden;
    padding:42px 38px; border-radius:28px; margin-bottom:26px;
    background:linear-gradient(120deg,#6d28d9,#2563eb,#0891b2,#db2777);
    background-size:300% 300%; animation:gradShift 14s ease infinite;
    box-shadow:0 20px 60px rgba(109,40,217,.35);
}
.hero::after {
    content:""; position:absolute; right:-80px; top:-80px; width:300px; height:300px;
    border-radius:50%; background:rgba(255,255,255,.12); filter:blur(4px);
}
.hero .tag {
    display:inline-block; font-size:12px; font-weight:700; letter-spacing:2px;
    padding:6px 14px; border-radius:999px; background:rgba(255,255,255,.18);
    backdrop-filter:blur(8px);
}
.hero h1 {font-size:clamp(32px,4.5vw,52px); font-weight:800; margin:16px 0 8px; color:#fff; line-height:1.1}
.hero p {font-size:17px; color:rgba(255,255,255,.9); margin:0; max-width:640px}

/* ---------- GENERIC CARDS ---------- */
.glass {
    background:linear-gradient(145deg,rgba(255,255,255,.07),rgba(255,255,255,.02));
    border:1px solid rgba(255,255,255,.10); border-radius:20px;
    padding:20px; backdrop-filter:blur(10px);
    transition:transform .25s ease, border-color .25s ease;
}
.glass:hover {transform:translateY(-4px); border-color:rgba(167,139,250,.6)}
.glass h3 {margin:6px 0 4px; font-size:18px}
.glass p {margin:0; color:#aab6d5; font-size:14px}
.feature-icon {font-size:28px}
.label {color:#9aa8cc; font-size:12px; letter-spacing:1px; text-transform:uppercase}
.big {font-size:32px; font-weight:800; background:linear-gradient(90deg,#a78bfa,#38bdf8);
      -webkit-background-clip:text; background-clip:text; color:transparent}

.section-title {font-size:24px; font-weight:800; margin:30px 0 16px}

/* ---------- PIPELINE TRACKER ---------- */
@keyframes spin {to {transform:rotate(360deg)}}
@keyframes pulseGlow {0%,100%{box-shadow:0 0 0 0 var(--c)} 50%{box-shadow:0 0 22px 2px var(--c)}}
@keyframes pop {0%{transform:scale(.3);opacity:0} 70%{transform:scale(1.2)} 100%{transform:scale(1);opacity:1}}
@keyframes slide {0%{background-position:0 0} 100%{background-position:40px 0}}

.pipe-wrap {display:grid; grid-template-columns:repeat(4,1fr); gap:16px}
@media (max-width:900px){.pipe-wrap{grid-template-columns:1fr 1fr}}
.stage {
    position:relative; padding:22px 18px 18px; border-radius:20px;
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08);
    opacity:.55; transition:all .3s ease;
}
.stage.running {
    opacity:1; background:linear-gradient(160deg,rgba(255,255,255,.10),rgba(255,255,255,.03));
    border-color:var(--c); animation:pulseGlow 1.8s ease-in-out infinite;
}
.stage.done {opacity:1; border-color:rgba(52,211,153,.55); background:linear-gradient(160deg,rgba(16,185,129,.14),rgba(255,255,255,.03))}
.stage.error {opacity:1; border-color:#f87171; background:rgba(239,68,68,.12)}
.stage .top {display:flex; justify-content:space-between; align-items:center}
.stage .emoji {font-size:30px}
.stage .name {font-weight:800; font-size:17px; margin-top:12px}
.stage .desc {font-size:13px; color:#aab6d5; margin-top:4px; min-height:36px}
.badge {font-size:11px; font-weight:700; letter-spacing:1px; padding:4px 10px; border-radius:999px; margin-top:8px; display:inline-block}
.badge.pending {background:rgba(255,255,255,.08); color:#94a3b8}
.badge.running {background:var(--c); color:#0b1020}
.badge.done {background:rgba(52,211,153,.2); color:#6ee7b7}
.badge.error {background:rgba(248,113,113,.2); color:#fca5a5}

.spinner {
    width:28px; height:28px; border-radius:50%;
    border:3px solid rgba(255,255,255,.15); border-top-color:var(--c);
    animation:spin .8s linear infinite;
}
.tick {
    width:28px; height:28px; border-radius:50%; background:#10b981; color:white;
    display:flex; align-items:center; justify-content:center; font-weight:800; font-size:16px;
    animation:pop .4s ease;
}
.cross {width:28px; height:28px; border-radius:50%; background:#ef4444; color:white;
        display:flex; align-items:center; justify-content:center; font-weight:800}
.dot {width:14px; height:14px; border-radius:50%; background:rgba(255,255,255,.2); margin:7px}
.bar {height:5px; border-radius:99px; margin-top:12px; background:rgba(255,255,255,.08); overflow:hidden}
.bar > div {height:100%; width:100%; border-radius:99px;
    background:repeating-linear-gradient(45deg,var(--c),var(--c) 10px,rgba(255,255,255,.35) 10px,rgba(255,255,255,.35) 20px);
    background-size:40px 40px; animation:slide .8s linear infinite}
.bar.full > div {animation:none; background:#10b981}

.overall {display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; color:#c7d2fe; font-weight:600}
.track {height:10px; border-radius:99px; background:rgba(255,255,255,.08); overflow:hidden; margin-bottom:18px}
.track > div {height:100%; border-radius:99px; background:linear-gradient(90deg,#38bdf8,#a78bfa,#f472b6); transition:width .4s ease}
.note {font-size:12px; color:#94a3b8; margin-top:10px}

/* ---------- INPUTS / BUTTONS / TABS ---------- */
.stTextArea textarea {
    background:rgba(15,23,42,.8)!important; color:#fff!important;
    border:1px solid rgba(148,163,184,.3)!important; border-radius:14px!important; font-size:16px!important;
}
.stTextArea textarea:focus {border-color:#a78bfa!important; box-shadow:0 0 0 3px rgba(167,139,250,.25)!important}
div.stButton>button, div[data-testid="stFormSubmitButton"]>button {
    background:linear-gradient(100deg,#7c3aed,#2563eb,#06b6d4); background-size:200% 100%;
    color:#fff; border:0; border-radius:14px; font-weight:800; min-height:50px; font-size:16px;
    transition:all .3s ease;
}
div.stButton>button:hover, div[data-testid="stFormSubmitButton"]>button:hover {
    background-position:100% 0; transform:translateY(-2px); box-shadow:0 10px 30px rgba(99,102,241,.5); color:#fff;
}
.stDownloadButton button {
    background:rgba(255,255,255,.06); color:#e0e7ff; border:1px solid rgba(165,180,252,.4); border-radius:12px; font-weight:600;
}
.stDownloadButton button:hover {border-color:#a78bfa; color:#fff}
[data-testid="stTabs"] button {color:#c7d2fe; font-weight:700}
[data-testid="stTabs"] button[aria-selected="true"] {color:#f0abfc}
.footer {text-align:center; color:#7c89ad; padding-top:36px; font-size:12px}
</style>
""",
    unsafe_allow_html=True,
)


# ======================================================================
# HELPERS
# ======================================================================
def render_pipeline(states, elapsed, estimated=False):
    """Return HTML for the live agent tracker."""
    done_count = sum(1 for k in STAGE_KEYS if states.get(k) == "done")
    running = [k for k in STAGE_KEYS if states.get(k) == "running"]
    pct = int((done_count + (0.5 if running else 0)) / len(STAGES) * 100)
    if done_count == len(STAGES):
        pct = 100

    cards = []
    for key, icon, name, run_txt, done_txt, color, _ in STAGES:
        s = states.get(key, "pending")
        if s == "running":
            indicator = '<div class="spinner"></div>'
            desc, badge = run_txt, "WORKING"
            bar = '<div class="bar"><div></div></div>'
        elif s == "done":
            indicator = '<div class="tick">✓</div>'
            desc, badge = done_txt, "COMPLETED"
            bar = '<div class="bar full"><div></div></div>'
        elif s == "error":
            indicator = '<div class="cross">✕</div>'
            desc, badge = "Something went wrong here", "FAILED"
            bar = ""
        else:
            indicator = '<div class="dot"></div>'
            desc, badge = "Waiting for the previous agent…", "QUEUED"
            bar = ""
        cards.append(
            f'<div class="stage {s}" style="--c:{color}">'
            f'<div class="top"><span class="emoji">{icon}</span>{indicator}</div>'
            f'<div class="name">{name}</div>'
            f'<div class="desc">{desc}</div>'
            f'<span class="badge {s}">{badge}</span>{bar}</div>'
        )

    note = (
        '<div class="note">⚠️ Live stage updates are estimated because main.py does not '
        "report progress yet. See the callback snippet to make them exact.</div>"
        if estimated
        else ""
    )
    return (
        f'<div class="overall"><span>Overall progress · {pct}%</span>'
        f"<span>⏱ {elapsed:0.0f}s</span></div>"
        f'<div class="track"><div style="width:{pct}%"></div></div>'
        f'<div class="pipe-wrap">{"".join(cards)}</div>{note}'
    )


def find_callback_param(func):
    """Return the name of a progress-callback parameter run_pipeline accepts, if any."""
    try:
        params = inspect.signature(func).parameters
    except (TypeError, ValueError):
        return None
    for name in ("progress_callback", "callback", "on_progress", "status_callback", "on_stage"):
        if name in params:
            return name
    return None


def estimated_states(elapsed):
    """Time-based guess of stage states (used only when no real callback exists)."""
    states, t = {}, 0
    for i, (key, *_rest, secs) in enumerate(STAGES):
        t += secs
        if elapsed >= t and i < len(STAGES) - 1:
            states[key] = "done"
        elif elapsed < t - secs:
            states[key] = "pending"
        else:
            states[key] = "running"
    # Only one stage may be "running" at a time
    seen_running = False
    for key in STAGE_KEYS:
        if states[key] == "running":
            if seen_running:
                states[key] = "pending"
            seen_running = True
    return states


def run_with_live_tracker(topic, placeholder):
    """Run the pipeline in a worker thread and animate the tracker meanwhile."""
    q = queue.Queue()
    cb_name = find_callback_param(run_pipeline)
    states = {k: "pending" for k in STAGE_KEYS}
    start = time.time()

    def worker():
        try:
            if cb_name:
                res = run_pipeline(
                    topic, **{cb_name: lambda stage, status: q.put(("evt", stage, status))}
                )
            else:
                res = run_pipeline(topic)
            q.put(("done", res))
        except Exception as exc:  # noqa: BLE001
            q.put(("error", exc))

    threading.Thread(target=worker, daemon=True).start()

    outcome = None
    while outcome is None:
        elapsed = time.time() - start
        try:
            while True:
                msg = q.get_nowait()
                if msg[0] == "evt":
                    _, stage, status = msg
                    stage = str(stage).lower()
                    if stage in states:
                        states[stage] = {"start": "running", "running": "running",
                                         "done": "done", "end": "done"}.get(str(status).lower(), states[stage])
                else:
                    outcome = msg
                    break
        except queue.Empty:
            pass

        if outcome is None:
            shown = states if cb_name else estimated_states(elapsed)
            placeholder.markdown(render_pipeline(shown, elapsed, estimated=not cb_name),
                                 unsafe_allow_html=True)
            time.sleep(0.25)

    elapsed = time.time() - start
    if outcome[0] == "done":
        states = {k: "done" for k in STAGE_KEYS}
    else:
        # mark the active stage as failed
        shown = states if cb_name else estimated_states(elapsed)
        states = {k: ("error" if v == "running" else v) for k, v in shown.items()}
    return outcome, states, elapsed, (not cb_name)


# ======================================================================
# SIDEBAR
# ======================================================================
with st.sidebar:
    st.markdown("## 🔬 ResearchAI")
    st.caption("MULTI-AGENT RESEARCH WORKSPACE")
    st.divider()
    st.markdown("### 🧠 Your AI Team")
    for _, icon, name, _, _, color, _ in STAGES:
        st.markdown(
            f'<div style="padding:10px 12px;margin-bottom:8px;border-radius:12px;'
            f'border-left:4px solid {color};background:rgba(255,255,255,.05)">'
            f"{icon} <b>{name}</b></div>",
            unsafe_allow_html=True,
        )
    st.divider()
    st.caption("Built with Python · LangChain · Streamlit")
    st.caption("Always verify citations and facts.")

# ======================================================================
# HERO
# ======================================================================
st.markdown(
    """
<div class="hero">
<span class="tag">✦ INTELLIGENT RESEARCH WORKSPACE</span>
<h1>Turn Questions Into Research.</h1>
<p>Search, scrape, write and review — a team of AI agents working together in one beautiful workspace.</p>
</div>
""",
    unsafe_allow_html=True,
)

cols = st.columns(4)
for col, (_, icon, name, _, _, color, _) in zip(cols, STAGES):
    with col:
        st.markdown(
            f'<div class="glass" style="border-top:3px solid {color}">'
            f'<div class="feature-icon">{icon}</div><div class="label">Agent</div>'
            f"<b>{name}</b></div>",
            unsafe_allow_html=True,
        )

# ======================================================================
# INPUT
# ======================================================================
st.markdown('<div class="section-title">🚀 Start Research</div>', unsafe_allow_html=True)

with st.container(border=True):
    with st.form("research_form"):
        topic = st.text_area(
            "Research topic",
            placeholder="Example: Recent advances in lung cancer diagnosis",
            height=100,
        )
        submitted = st.form_submit_button("✨ Generate Research Report", use_container_width=True)

# ======================================================================
# RUN
# ======================================================================
if submitted:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        st.session_state.pop("research_result", None)
        st.session_state["research_topic"] = topic.strip()

        st.markdown('<div class="section-title">⚙️ Live Agent Pipeline</div>', unsafe_allow_html=True)
        tracker = st.empty()

        outcome, final_states, took, est = run_with_live_tracker(topic.strip(), tracker)
        tracker.markdown(render_pipeline(final_states, took, estimated=False),
                         unsafe_allow_html=True)
        st.session_state["stage_states"] = final_states
        st.session_state["elapsed"] = took

        if outcome[0] == "done":
            if isinstance(outcome[1], dict):
                st.session_state["research_result"] = outcome[1]
                st.success(f"Research results are ready! (finished in {took:0.0f}s)")
            else:
                st.error("run_pipeline() must return a dictionary.")
        else:
            st.error("An error occurred while running the pipeline.")
            st.exception(outcome[1])

# ======================================================================
# RESULTS
# ======================================================================
result = st.session_state.get("research_result")
saved_topic = st.session_state.get("research_topic", "")

if result:
    if not submitted:
        st.markdown('<div class="section-title">⚙️ Pipeline Summary</div>', unsafe_allow_html=True)
        st.markdown(
            render_pipeline(
                st.session_state.get("stage_states", {k: "done" for k in STAGE_KEYS}),
                st.session_state.get("elapsed", 0),
            ),
            unsafe_allow_html=True,
        )

    st.divider()
    st.markdown('<div class="section-title">📊 Research Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f"**Topic:** {saved_topic}")

    report = str(result.get("report", "") or "")
    review = str(result.get("ranking", "") or "")
    search_data = str(result.get("search_result", "") or "")
    scraped_data = str(result.get("web_result", "") or "")

    score = None
    patterns = [
        r"(?i)\b(?:overall\s+)?(?:score|rating)\s*(?:is|of|:|=|-)?\s*(\d{1,2}(?:\.\d+)?)\s*(?:/\s*10|out\s+of\s+10)\b",
        r"(?i)\b(\d{1,2}(?:\.\d+)?)\s*/\s*10\b",
        r"(?i)\b(\d{1,2}(?:\.\d+)?)\s+out\s+of\s+10\b",
    ]
    for pattern in patterns:
        m = re.search(pattern, review)
        if m and 0 <= float(m.group(1)) <= 10:
            score = float(m.group(1))
            break

    m1, m2, m3, m4 = st.columns(4)
    cards = [
        (m1, "Review score", f"{score:g} / 10" if score is not None else "N/A"),
        (m2, "Report words", f"{len(report.split()):,}"),
        (m3, "Sources text", f"{len(search_data.split()):,} words"),
        (m4, "Time taken", f"{st.session_state.get('elapsed', 0):0.0f}s"),
    ]
    for col, label, value in cards:
        with col:
            st.markdown(
                f'<div class="glass"><div class="label">{label}</div><div class="big">{value}</div></div>',
                unsafe_allow_html=True,
            )

    if score is not None:
        st.progress(score / 10)
        if score >= 8:
            st.success("Strong score according to the AI reviewer.")
        elif score >= 6:
            st.info("Some improvements may be useful.")
        else:
            st.warning("Review the feedback and improve the report.")
    else:
        st.info("The reviewer did not provide a detectable score out of 10. See the AI Review tab.")
    st.caption("The rating is AI-generated and is not an independently verified score.")

    tab_report, tab_review, tab_search, tab_scrape = st.tabs(
        ["📄 Research Report", "🛡️ AI Review", "🔎 Search Results", "🌐 Scraped Content"]
    )

    with tab_report:
        if report:
            st.markdown(report)
            st.download_button("⬇️ Download Report", report, "research_report.md",
                               "text/markdown", use_container_width=True)
        else:
            st.info("No report returned.")

    with tab_review:
        if review:
            st.markdown(review)
            st.download_button("⬇️ Download Review", review, "research_review.md",
                               "text/markdown", use_container_width=True)
        else:
            st.info("No review returned.")

    with tab_search:
        st.markdown(search_data or "No search output returned.")
        if search_data:
            st.download_button("⬇️ Download Search Results", search_data,
                               "search_results.txt", "text/plain")

    with tab_scrape:
        st.markdown(scraped_data or "No scraped content returned.")
        if scraped_data:
            st.download_button("⬇️ Download Scraped Content", scraped_data,
                               "scraped_content.txt", "text/plain")

    st.warning("Verify source URLs, statistics, and citations before relying on AI-generated research.")

else:
    st.markdown('<div class="section-title">✨ How It Works</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    steps = [
        (c1, "01 · Discover", "The Search Agent finds relevant sources on the web.", "#38bdf8"),
        (c2, "02 · Synthesize", "The Scraper collects content and the Writer builds a structured report.", "#a78bfa"),
        (c3, "03 · Review", "The Review Chain evaluates the report and gives a score.", "#f472b6"),
    ]
    for col, title, text, color in steps:
        with col:
            st.markdown(
                f'<div class="glass" style="border-top:3px solid {color}"><h3>{title}</h3><p>{text}</p></div>',
                unsafe_allow_html=True,
            )

st.markdown(
    '<div class="footer">RESEARCHAI · MULTI-AGENT RESEARCH WORKSPACE<br>'
    "Research responsibly. Verify before you cite.</div>",
    unsafe_allow_html=True,
)