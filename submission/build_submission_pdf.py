from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable, Table, TableStyle
)

NAVY = colors.HexColor("#1a2130")
AMBER = colors.HexColor("#b8720a")
GREY = colors.HexColor("#5b6270")
LINE = colors.HexColor("#dcdfe6")
PANEL = colors.HexColor("#f5f3ee")

styles = getSampleStyleSheet()

team_label = ParagraphStyle("team_label", parent=styles["Normal"], fontName="Helvetica-Bold",
                             fontSize=8.5, textColor=AMBER, leading=11, tracking=1)
team_name = ParagraphStyle("team_name", parent=styles["Normal"], fontName="Helvetica-Bold",
                            fontSize=15, textColor=NAVY, leading=18, spaceAfter=1)
team_members = ParagraphStyle("team_members", parent=styles["Normal"], fontName="Helvetica",
                               fontSize=9.5, textColor=GREY, leading=13)

game_title = ParagraphStyle("game_title", parent=styles["Normal"], fontName="Helvetica-Bold",
                             fontSize=30, textColor=NAVY, leading=34, spaceBefore=14, spaceAfter=2)
game_sub = ParagraphStyle("game_sub", parent=styles["Normal"], fontName="Helvetica-Oblique",
                           fontSize=10.5, textColor=AMBER, leading=13, spaceAfter=12)

h2 = ParagraphStyle("h2", parent=styles["Normal"], fontName="Helvetica-Bold",
                     fontSize=11, textColor=NAVY, leading=14, spaceBefore=10, spaceAfter=4)

body = ParagraphStyle("body", parent=styles["Normal"], fontName="Helvetica",
                       fontSize=9.6, textColor=colors.HexColor("#20242e"), leading=13.6,
                       spaceAfter=7, alignment=TA_LEFT)

closing = ParagraphStyle("closing", parent=styles["Normal"], fontName="Helvetica-BoldOblique",
                          fontSize=10.5, textColor=NAVY, leading=14, spaceBefore=8)

page2_title = ParagraphStyle("page2_title", parent=styles["Normal"], fontName="Helvetica-Bold",
                              fontSize=15, textColor=NAVY, leading=18, spaceAfter=2)
page2_sub = ParagraphStyle("page2_sub", parent=styles["Normal"], fontName="Helvetica",
                            fontSize=8.5, textColor=GREY, leading=11, spaceAfter=8)

prompt_num = ParagraphStyle("prompt_num", parent=styles["Normal"], fontName="Helvetica-Bold",
                             fontSize=8, textColor=AMBER, leading=10.5)
prompt_text = ParagraphStyle("prompt_text", parent=styles["Normal"], fontName="Helvetica",
                              fontSize=8, textColor=colors.HexColor("#20242e"), leading=10.8)
prompt_meta = ParagraphStyle("prompt_meta", parent=styles["Normal"], fontName="Helvetica-Oblique",
                              fontSize=8, textColor=GREY, leading=11, spaceAfter=2)

footer_style = ParagraphStyle("footer", parent=styles["Normal"], fontName="Helvetica",
                               fontSize=7.5, textColor=GREY, leading=10)

def hr(color=LINE, thickness=0.75, space_before=4, space_after=8):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                       spaceBefore=space_before, spaceAfter=space_after)

story = []

# ---------- PAGE 1 ----------
story.append(Paragraph("TEAM", team_label))
story.append(Paragraph("SkillRackers", team_name))
story.append(Paragraph("Nagavarapu Mourya (Team Lead) &nbsp;&middot;&nbsp; Surya Teja", team_members))
story.append(hr(space_before=10, space_after=10))

story.append(Paragraph("ONE BULLET", game_title))
story.append(Paragraph("Prompt &amp; Play &mdash; Game Concept &nbsp;/&nbsp; Page 1 of 2", game_sub))

story.append(Paragraph(
    "There is exactly one bullet in the entire game world, and every character in the arena shares it. "
    "It never respawns and never runs low, because it was never really anyone's to begin with &mdash; it is a single, "
    "physical, contested object. Whoever is holding it is the only one who can kill. Everyone else, including the "
    "player most of the time, is unarmed. Even the title screen doesn't sit idle: two AI bots are already fighting "
    "over it behind the menu, so the concept reads instantly, before a single key is pressed.", body))

story.append(Paragraph("How it plays", h2))
story.append(Paragraph(
    "Move with WASD, aim with the mouse. When the round is lying loose on the floor, sprint for it before a hostile "
    "does. Once you're holding it, firing is a single click &mdash; but the instant you pull the trigger you give up "
    "the only thing keeping you alive. The bullet becomes a fast, dodgeable object again and lands wherever it lands, "
    "and now everyone in the room, possibly including the enemy you just barely missed, is racing to claim it. "
    "Five escalating waves test whether you can hold your nerve: take the shot, or wait for a cleaner one. Hostiles "
    "aim faster and more accurately with every wave, and a round left untouched on the floor too long starts to pulse "
    "and relocates itself &mdash; so no one can simply camp and wait the clock out. On phones and tablets, twin virtual "
    "joysticks take over automatically: drag the left half to move, drag the right half to aim in any direction and fire. "
    "The very first time anyone opens it, three short on-screen callouts teach the whole loop by pointing at it as it "
    "happens &mdash; then they never appear again.", body))

story.append(Paragraph("What makes it original", h2))
story.append(Paragraph(
    "Shooters almost always assume abundant, personal ammunition &mdash; tension comes from aim, cover, or managing "
    "a resource across many bullets. One Bullet removes that assumption entirely. Lethality itself becomes a single, "
    "scarce, physical object shared by the whole arena, like a MacGuffin repurposed as a weapon. That single change "
    "produces behaviour the genre rarely sees: baiting an opponent away from the round, breaking line of sight the "
    "instant after you fire, or deliberately not taking a clean shot because reclaiming position afterwards matters "
    "more than the kill. It becomes a game about possession and nerve, not reflexes or ammo counts.", body))

story.append(Paragraph("Feel and craft", h2))
story.append(Paragraph(
    "Every hit is fatal for player and enemy alike, so each encounter is a held breath rather than a drawn-out fight. "
    "Enemies telegraph an incoming shot with a laser sightline, a red vignette rises as danger builds, and screen "
    "shake, particle bursts, brief slow-motion on the killing blow, and live-synthesized Web Audio sound effects give "
    "one tiny object real physical weight. Best wave and elimination count persist between runs. The entire game is "
    "one self-contained, fully responsive HTML/Canvas file &mdash; built and iteratively play-tested across desktop, "
    "tablet and phone with Claude Code as build partner, catching and fixing real bugs along the way.", body))

story.append(Paragraph(
    "There is only one bullet in the world. Everything else is just people trying to get to it first.", closing))

story.append(PageBreak())

# ---------- PAGE 2 ----------
story.append(Paragraph("Prompts Used", page2_title))
story.append(Paragraph("One Bullet &nbsp;&middot;&nbsp; Page 2 of 2 &nbsp;&middot;&nbsp; listed in the order used during development, Claude (Claude Code) as the build partner", page2_sub))

prompts = [
    ("1", "Shared the official Prompt &amp; Play contest guidelines (theme, judging criteria, and submission format) as the brief to work from."),
    ("2", "&ldquo;THE THEME IS HERE! Challenge: Build a Game &mdash; Any Concept, Any Type. Design and build a game &mdash; any concept, any genre, any style you can imagine. The only requirement: it has to be innovative. Use AI prompting to bring your idea to life from concept to final build.&rdquo; (full brief pasted, including judging criteria and the two-page PDF submission format)."),
    ("3", "&ldquo;Research everything and build me for this. As it has AI tools usage so i can use claude code as my teammate. Build me best project of this.&rdquo;"),
    ("4", "Asked to choose a build path &mdash; selected &ldquo;Pitch me ideas&rdquo; from: pitch ideas / I already have a concept / surprise me."),
    ("5", "Reviewed four original concept pitches (One Bullet, Echo Run, The Unreliable Map, Reverse Boss) and chose to proceed with the strongest single-sentence hook."),
    ("6", "&ldquo;Research everything and then go with it. Should be in top teams so need bestest one.&rdquo;"),
    ("7", "&ldquo;I should be in Top 10 teams of this contest. so take time and plan the best.&rdquo;"),
    ("8", "&ldquo;Research everything and then go with it. Should be in top teams so need bestest one.&rdquo; (confirmed direction; proceed to build, test in a live browser, and fix any bugs found before shipping)."),
    ("9", "&ldquo;First project should be worth to judges. So look everything i given details right of the contest.&rdquo; &mdash; prompted re-reading the official guidelines PDF directly to confirm exact submission format (two pages, team header, live link) before finalizing."),
    ("10", "Provided team details (team name and members) to complete the Page 1 header of this submission document."),
    ("11", "&ldquo;What additional we can make now in current game to make it more strong and top one?&rdquo; &mdash; extended the build with a per-wave difficulty curve and flavour text, an untouched-round urgency timer that self-relocates the bullet, brief slow-motion on the killing blow, and persistent best-run tracking."),
    ("12", "&ldquo;See the flaws and fix them too.&rdquo; &mdash; full code review pass; found and fixed a kill wrongly credited from AI friendly fire, a danger-telegraph that no longer matched the new per-wave difficulty, a slow-motion effect leaking into the next wave, and a stuck-movement edge case on losing window focus."),
    ("13", "&ldquo;Make it more perfect. Add features if needed. Need to be in top teams of contest. Fully research, plan, implement and provide me best.&rdquo; &mdash; added a live attract-mode demo (AI bots fight over the round behind the title screen, so the concept reads before a single key is pressed) and a persistent mute toggle for quiet judging environments."),
    ("14", "&ldquo;Make sure it works in all devices. Responsive to all devices freely.&rdquo; / &ldquo;Yes, make sure it is suitable for all devices browser's.&rdquo; &mdash; found that touch input only handled aiming, with no way to move on a phone or tablet; replaced it with twin virtual joysticks (drag left to move, drag right to aim in any direction and fire), fixed the aim math so it isn't limited to one screen half, added adaptive on-screen instructions, and verified the full flow on desktop, tablet and mobile viewports."),
    ("15", "&ldquo;I still don't understand what's the game is. But all i ask is want to be in top 10 teams... choose another game or make current one perfect... i need best and outstanding result with no flaws.&rdquo; &mdash; decided to keep the concept (it is sound and explains in one paragraph) rather than restart, and fixed the real problem: the game never taught itself. Added a first-time-only guided sequence that teaches the whole loop through on-screen callouts tied to what is actually happening (find the round, you're armed, you're unarmed, go again), verified step by step, then never shown again once learned."),
]

rows = []
for n, text in prompts:
    rows.append([Paragraph(n, prompt_num), Paragraph(text, prompt_text)])

t = Table(rows, colWidths=[0.32*inch, 6.28*inch])
t.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("LINEBELOW", (0,0), (-1,-2), 0.5, LINE),
    ("LEFTPADDING", (0,0), (0,-1), 0),
]))
story.append(t)

story.append(Spacer(1, 14))
story.append(hr(space_before=0, space_after=6))
story.append(Paragraph(
    "Live build: https://claude.ai/artifact/Dp7weh9n96RZzAMrtp4DZg &nbsp;&middot;&nbsp; Team SkillRackers &nbsp;&middot;&nbsp; Prompt &amp; Play submission",
    footer_style))

doc = SimpleDocTemplate(
    "/private/tmp/claude-501/-Users-myselfmourya-Library-Application-Support-Claude-scratch-workspaces-f8224a13-d4bd-4b91-a8cb-4471a1736dfe-aa0e57ff-25fb-47f5-b1e8-b3976120acee-scratch-2026-09-26-2e7459/a7996d91-f98a-48c4-90fd-a6ebe2305597/scratchpad/One_Bullet_SkillRackers_Submission.pdf",
    pagesize=letter,
    leftMargin=0.85*inch, rightMargin=0.85*inch,
    topMargin=0.75*inch, bottomMargin=0.7*inch,
    title="One Bullet - Prompt & Play Submission", author="SkillRackers"
)
doc.build(story)
print("done")
