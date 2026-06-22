# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
I chose UIC CS professor reviews. This knowledge can be very widespread and vague as to how good/bad a professor really is.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->


**Chunk size:**

200 characters

**Overlap:**

40 characters

**Reasoning:**

Most of my documents consist of short student reviews, discussion posts, and comments rather than long articles. A chunk size of 200 characters is large enough to preserve complete opinions and experiences while remaining focused on a single topic. A 40-character overlap helps preserve context when important information appears near the boundary between two chunks. Smaller chunks could split reviews into fragments that lose meaning, while much larger chunks could combine unrelated opinions and reduce retrieval accuracy.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

all-MiniLM-L6-v2 sentence-transformers

**Top-k:**

4

**Production tradeoff reflection:**

I selected all-MiniLM-L6-v2 because it is free, runs locally, and provides strong semantic search performance for short text documents. If this system were deployed in production, I would consider larger embedding models that provide better semantic understanding and multilingual support. Important factors would include retrieval accuracy, inference speed, operating cost, context length, and the ability to handle diverse writing styles. Larger models may improve retrieval quality but would increase computational cost and latency.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What do students say about CS141? | Students frequently describe CS141 as challenging for beginners, with discussions focusing on pacing and workload. |
| 2 | What concerns do students have about professors who do not actively teach during class? | Students report frustration when professors rely heavily on self-learning and provide limited in-class instruction. |
| 3 | What do students say about CS 401 with Danko? | Students discuss workload, grading practices, and overall teaching quality in the course. |
| 4 | What information can students find about Sara Riazi's CS480 course? | Students discuss teaching style, course difficulty, and experiences with the instructor. |
| 5 | What factors do students consider when evaluating UIC CS professors? | Students commonly discuss teaching effectiveness, workload, grading fairness, exam difficulty, and availability outside class. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The project combines information from RateMyProfessor, Reddit discussions, and grade distribution data. These sources have different writing styles, levels of detail, and reliability, which may make retrieval less consistent.

2. Important information may span multiple comments or paragraphs. If chunking separates related content, retrieval may only return part of the context needed to answer a question accurately.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

Document Ingestion (Python, BeautifulSoup, File Readers) 
             |
             v 
Chunking (Custom chunk_text function) 
             | 
             v 
Embeddings (all-MiniLM-L6-v2) 
             | 
             v 
Vector Store (ChromaDB) 
             | 
             v 
Retrieval (Top-k Semantic Search) 
             | 
             v 
Generation (Groq Llama-3.3-70B)
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

I will use ChatGPT to help implement the document ingestion and chunking pipeline. I will provide the Documents section, Chunking Strategy section, and Architecture diagram from this planning document. I will ask ChatGPT to generate Python code that loads text documents, cleans unnecessary content, and splits them into chunks of 200 characters with a 40-character overlap. I will verify the output by inspecting at least five generated chunks to ensure they are readable, self-contained, and match my chunking specifications.

**Milestone 4 — Embedding and retrieval:**

I will use ChatGPT to help implement embedding generation and vector storage. I will provide the Retrieval Approach section and Architecture diagram. I will ask ChatGPT to generate code that embeds chunks using all-MiniLM-L6-v2, stores them in ChromaDB with metadata, and retrieves the top four most relevant chunks for a query. I will verify correctness by testing several evaluation questions and manually reviewing the retrieved chunks for relevance.

**Milestone 5 — Generation and interface:**

I will use ChatGPT to help implement the grounded response generation system and Gradio interface. I will provide the Retrieval Approach, Evaluation Plan, and grounding requirements from the project instructions. I will ask ChatGPT to generate code that retrieves relevant chunks, sends them to Groq's Llama 3.3 model, and displays answers with source citations in a Gradio interface. I will verify the implementation by testing both answerable and unanswerable questions to ensure the system remains grounded in retrieved documents and refuses unsupported queries.
