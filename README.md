# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
     I chose UIC CS professor reviews. This knowledge can be very widespread and vague as to how good/bad a professor really is.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | RateMyProfessor | Lists over 100 UIC CS professors with corresponding reviews and ratings from students | https://www.ratemyprofessors.com/search/professors/1111?q=*&did=11 |
| 2 | UIC Grades | Shows course grade data by semester | https://uicgrades.com/index.html |
| 3 | UIC Grade Distribution Report | Shows course grade data by semester | https://secure.oir.uic.edu/gradedistroApp/gradedistroApp.aspx |
| 4 | r/uichicago CS141 class rant | Student discussion of CS141 instruction, pacing, and learning experience | https://www.reddit.com/r/uichicago/comments/1nvrvsq/cs141_class_rant/ |
| 5 | r/uichicago Can we report a professor if he doesn’t teach in class? | Discussion about teaching effectiveness and department response | https://www.reddit.com/r/uichicago/comments/165oa8a/can_we_report_a_professor_if_he_doesnt_teach_in/ |
| 6 | r/uichicago UIC CS discussion | Comments comparing professors and course experiences | https://www.reddit.com/r/uichicago/comments/te6dkf/uic_cs/ |
| 7 | r/uichicago CS 401 with Danko | Student comments about workload, grading, and instructor quality | https://www.reddit.com/r/uichicago/comments/hi54lx/cs_401/ |
| 8 | r/uichicago CS 351 reviews | Discussion of course structure and recent changes | https://www.reddit.com/r/uichicago/comments/1jrkdeh/cs_351_reviews/ |
| 9 | r/uichicago Sara Riazi CS480 | Discussion and references to reviews for a newer UIC CS professor | https://www.reddit.com/r/uichicago/comments/123z060/sara_riazi_cs_480/ |
| 10 | r/uichicago – CS undergrad at UIC | Broader discussion of teaching quality, course difficulty, and student experience | https://www.reddit.com/r/uichicago/comments/1c3qmgr/cs_undergad_at_uic/ |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

500 characters

**Overlap:**

100 characters

**Why these choices fit your documents:**

Most of my documents consist of short student reviews, discussion posts, and comments rather than long articles. A chunk size of 500 characters is large enough to preserve complete opinions and experiences while remaining focused on a single topic. A 100-character overlap helps preserve context when important information appears near the boundary between two chunks. Smaller chunks could split reviews into fragments that lose meaning, while much larger chunks could combine unrelated opinions and reduce retrieval accuracy.

**Final chunk count:**

39 chunks

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->


| # | Source document | Chunk text |
|---|----------------|------------|
| 1 | cs141_rant.txt | Common Themes Identified From Student Discussions Many students reported that CS 141 required substantial independent learning outside of lecture. Frequently mentioned concerns: - ZyBooks serving as the primary learning resource. - Lecture pacing not matching assigned material. - Difficult transition for students with no prior coding experience. - Lab assignments requiring significant outside practice. Frequently mentioned success strategies: - Complete ZyBooks carefully. - Practice coding every |
| 2 | cs141_rant.txt | tice. Frequently mentioned success strategies: - Complete ZyBooks carefully. - Practice coding every day. - Attend office hours. - Ask TAs for help when available. - Supplement lectures with online tutorials. Several students noted that learning programming requires consistent practice and repetition. Students who coded outside of class often reported better outcomes. |
| 3 | cs351_reviews.txt | Additional Information About CS 351 CS 351 focuses on advanced data structures and practical implementation techniques. Students considering the course often ask about: - Workload - Programming projects - Difficulty level - Interview preparation value Skills commonly associated with the course include: - Advanced tree structures - Graph data structures - Hashing techniques - Performance optimization - Algorithm implementation The course may provide useful preparation for technical interviews bec |
| 4 | cs351_reviews.txt | on - Algorithm implementation The course may provide useful preparation for technical interviews because it emphasizes efficient problem solving and data structure selection. Students are generally advised to have a strong understanding of CS 251 concepts before enrolling. Success strategies: - Review data structures beforehand. - Start projects early. - Attend office hours. - Test code extensively. Career and Interview Relevance Students interested in software engineering internships often view |
| 5 | cs351_reviews.txt | y. Career and Interview Relevance Students interested in software engineering internships often viewed CS 351 as useful because it reinforced advanced problem-solving skills. Topics covered in the course may appear during technical interviews and coding assessments. Students frequently recommended: - Reviewing asymptotic analysis. - Practicing implementation of data structures. - Understanding tradeoffs between different solutions. - Learning how performance impacts software design. Many student |

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 2:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 3:**

Top returned chunks:
-
-
-

Relevance explanation:

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query:

Response:

Source attribution:

---

**Grounded response 2**

Query:

Response:

Source attribution:

---

**Out-of-scope query**

Query:

System response (refusal):

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**

**Output format:**

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** 

> **System:** 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*